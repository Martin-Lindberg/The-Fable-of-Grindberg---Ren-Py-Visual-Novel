# Copyright 2004-2016 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import codecs
import re
import math

import renpy
import textwrap

class CodeGenerator(object):
    """
    This is used to generate and update the GUI code.
    """

    def __init__(self, parameters):
        """
        Generates or updates gui.rpy.
        """

        self.p = parameters

    def load_template(self, filename):

        target = os.path.join(self.p.prefix, filename)

        if os.path.exists(target) and not self.p.replace_code:
            template = target
        else:
            template = os.path.join(self.p.template, filename)

        with codecs.open(template, "r", "utf-8") as f:
            self.lines = [ i.rstrip().replace(u"\ufeff", "") for i in f ]

    def remove_scale(self):

        def scale(m):
            original = int(m.group(1))
            scaled = int(math.ceil(original * self.p.scale))
            return str(scaled)


        lines = [ ]

        for l in self.lines:
            l = re.sub(r'gui.scale\((.*?)\)', scale, l)
            lines.append(l)

        self.lines = lines

    def update_size(self):

        gui_init = "gui.init({}, {})".format(self.p.width, self.p.height)

        lines = [ ]

        for l in self.lines:
            l = re.sub(r'gui.init\(.*?\)', gui_init, l)
            lines.append(l)

        self.lines = lines


    def update_defines(self, replacements):
        """
        Replaces define statements in gui.rpy.
        """

        lines = [ ]

        for l in self.lines:

            m = re.match('^(\s*)define (.*?) =', l)

            if m:
                indent = m.group(1)
                variable = m.group(2)

                if variable in replacements:
                    l = "{}define {} = {}".format(indent, variable, replacements[variable])

            lines.append(l)

        self.lines = lines


    def update_gui_defines(self):
        """
        Replaces define statements in gui.rpy.
        """

        replacements = {
            'gui.accent_color' : repr(self.p.accent_color.hexcode),
            'gui.selected_color' : repr(self.p.selected_color.hexcode),
            'gui.hover_color' : repr(self.p.hover_color.hexcode),
            'gui.muted_color' : repr(self.p.muted_color.hexcode),
            'gui.hover_muted_color' : repr(self.p.hover_muted_color.hexcode),
            'gui.title_color' : repr(self.p.title_color.hexcode),
            'gui.idle_color' : repr(self.p.idle_color.hexcode),
            'gui.idle_small_color' : repr(self.p.idle_small_color.hexcode),
            'gui.insensitive_color' : repr(self.p.insensitive_color.hexcode),
            'gui.text_color' : repr(self.p.text_color.hexcode),
            'gui.interface_text_color' : repr(self.p.text_color.hexcode),
            'gui.choice_text_color' : repr(self.p.choice_color.hexcode),
            }

        self.update_defines(replacements)


    def update_options_defines(self):
        """
        Replaces define statements in options.rpy.
        """


        def quote(s):
            s = s.replace("\\", "\\\\")
            s = s.replace("\"", "\\\"")
            return '"' + s + '"'

        replacements = {
            'config.name' : "_({})".format(quote(self.p.name)),
            'build.name' : quote(self.p.simple_name),
            'config.save_directory' : quote(self.p.savedir),
            }

        self.update_defines(replacements)


    def write_target(self, filename):

        target = os.path.join(self.p.prefix, filename)

        if os.path.exists(target):

            backup = 1

            while True:

                bfn = "{}.{}.bak".format(target, backup)

                if not os.path.exists(bfn):
                    break

                backup += 1

            if not self.p.skip_backup:
                os.rename(target, bfn)

        with codecs.open(target, "w", "utf-8") as f:
            f.write(u"\ufeff")

            for l in self.lines:
                f.write(l + "\r\n")

    def translate_strings(self):

        def replace(m):
            s = eval(m.group(1))
            s = renpy.translation.translate_string(s, language=self.p.language)
            s = renpy.translation.quote_unicode(s)

            quote = m.group(1)[0]

            s = u"_({}{}{})".format(quote, s, quote)

            return s

        lines = [ ]

        for l in self.lines:

            l = re.sub(ur'_\((\".*?\")\)', replace, l)
            l = re.sub(ur'_\((\'.*?\')\)', replace, l)

            lines.append(l)

        self.lines = lines

    def translate_comments(self):

        lines = [ ]

        comment = [ ]
        indent = ""

        for l in self.lines:

            m = re.match(r'^(\s*## )(.*)', l.rstrip())

            if m:

                indent = m.group(1)
                c = m.group(2)

                if comment:
                    c = c.strip()

                comment.append(c)

            else:

                if comment:
                    s = "## " + ' '.join(comment)

                    if s.endswith("#"):
                        hashpad = True
                        s = s.rstrip('# ')
                    else:
                        hashpad = False

                    s = renpy.translation.translate_string(s, language=self.p.language)
                    m = re.match(r'## ([ *]*)(.*)', s)

                    prefix = m.group(1)
                    empty = ' ' * len(prefix)
                    rest = m.group(2)

                    len_prefix = len(indent) + len(prefix)
                    len_wrap = 80 - len_prefix

                    for i, s in enumerate(textwrap.wrap(rest, width=len_wrap)):

                        if i == 0:
                            s = indent + prefix + s
                        else:
                            s = indent + empty + s

                        if hashpad and len(s) < 79:
                            s = s + " " + "#" * (79 - len(s))

                        lines.append(s)

                    comment = [ ]

                lines.append(l)

        self.lines = lines

    def generate_gui(self, fn):
        if not self.p.update_code:
            return

        self.load_template(fn)
        self.update_gui_defines()

        if self.p.replace_code:
            self.remove_scale()
            self.update_size()
            self.translate_strings()
            self.translate_comments()

        self.write_target(fn)

    def generate_code(self, fn):

        target = os.path.join(self.p.prefix, fn)

        if os.path.exists(target):
            return

        self.load_template(fn)

        self.translate_strings()
        self.translate_comments()
        self.update_options_defines()

        self.write_target(fn)
