# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image deer normal = "Deerstandingnormalcrop1.png"
image deer surprised = "Deerstandingsurprisecrop.png"
image forest lying = "meadowlying1.jpg" 
# Declare characters used by this game.
define d = Character('Daana', color="#663300")
define y = Character('You', color="#66CC00")

# The game starts here.
label start:
    
    play music "rainforest_ambience.mp3"
    
    scene forest lying with dissolve
    
    y "What is this? Where am I?"
    
    "The headache is confusing you, your eyes are foggy but you can hear the sound of birds and a voice in the distance."
    
    show deer normal at right with dissolve

    d "\"There, you finally woke up.\""
    
    "A proud doe is standing in front of you with a worried look on her face."

    y "\"Who are you?\""
    
    d "\"My name is Daana, I am the keeper of this meadow. Who are you?\""
    
    "You open your mouth to answer her question but no words come out."
    
    "Despite how hard you try you can not seem to remember a single thing about who you are or why you are here."
    
    y "How come I don't remember anything...?"
    
    y "\"I.... don't know...\""
    
    d "\"Poor thing... \""
    
    d "\"This isn't a good place to sleep in, though.\""
    
    d "\"If you'd like I can take you to a safe place to gather your strength.\""
    
    d "\"Will you follow me?\""
    
    "You consider your options:"
    
    "Either you follow the doe and trust in her, she seems nice."
    
    "Or you could decline her proposal and continue on your own, after all, she IS a talking doe."
    
    
    menu: 
        
        "Follow Daana":
        
         jump follow
        
        "Explore on your own":
        
         jump explore
        
label follow:
    
   y "I have no clue where I am and here I have someone who might be able to help me remember."
   
   y "There is no reason for me to not accept!"
    
   y "\"Thank you very much, I would gladly follow you!\""
   
   y "\"Where shall we go?\""
   
   "Daana looks at you with a slight frown on her face."
   
   d "\"Well, that´s the tricky part.\""
   
   d "\"You see, the forest isn´t as safe as it used to be.\""
   
   d "\"The blight is becoming a bigger problem than I expected and I am not sure if we can find a perfectly safe path back to my home.\""
   
   "You nod slightly and try to understand what she just said."
   
   "Safe?"
   
   "Blight?"
   
   "You look around you but you notice nothing unusual about the little meadow that you are standing in."
   
   "It´s actually quite beautiful."
   
   d "\"We have been here for too long, it isn´t safe for us to be out here.\""
   
   "Her words make you a bit nervous."
   
   "What dangers can there be in such a beautiful forest?"
   
   d "\"Follow me! I will try to lead us along a safe path.\""
   
   "As you follow the doe out of the meadow you start noticing the environment changing around you."
   
   "What earlier was bright and green has now darkened and you can see that some of the bushes and trees around you have withered and died."
   
   y "What happened here?"
   
   d "The blight has struck hard, everyday it spreads further and further into the forest."
   
   d "This isn´t even close to how bad it is in other areas."
   
   "There she goes again, talking about this \"blight\""
   
   "You´re not sure if you should ask her more about it now. Your head still hurts quite a lot."
   
   "You decide to stay silent and follow Daana further."
   
   "You walk for what feels like an eternity and when the deer finally stops you feel quite fatigued."
   
   d "Here, we have reached my home."
   
   d "You should be safe here."
   
   "She bows down as to welcome you in."
   
   "You give her a tired smile and enter through the hole underneath the tree."
   
   "As you squirm your way in you realize that your body feels unusual
   
   #Få in nått skoj slut här. Asså inte ett slut men så att de inte branchar in i varandra.

label explore:
    
    y "I´m not sure that I can trust her."
    
    y "She seems nice, but all of this is too wierd for me to handle at the moment."
    
    y "I think I´m better off on my own."
    
    y "\"Thank you for your kindness but I think that I am fine on my own.\""
    
    d "\"Okay, but if you need me, here´s a whistle.\""
    
    d "\"Use it only if you´re in grave danger.\""
    
    "You take the whistle and start to wander down a path leading out of the meadow.\""
    
    jump val
    label val:
$ ui.window()
$ ui.hbox(xalign=0.5, yalign=0.5)

$ ui.textbutton("Left", clicked=ui.returns("Left"))
$ ui.textbutton("Straight", clicked=ui.returns("Straight"))
$ ui.textbutton("Right", clicked=ui.returns("Right"))

$ ui.close()
$ result = ui.interact()
if result == "Left":
    y "This part of the forest looks really gloomy..."
    
    y "Should I continue?"
    jump left
elif result == "Right":
    y "This part of the forest doesn't look to bad..."
    
    y "Should I continue?"
    jump Right
    
else: 
    y "I wonder where this leads..."
    
    y "Should I continue?"
    jump Straight
    
##########
label left:
    
    
$ ui.vbox(xalign=0.5, yalign=0.5)
$ ui.textbutton("Continue", clicked=ui.returns(1))
$ ui.textbutton("Go back", clicked=ui.returns(2))
$ ui.close()

$ result = ui.interact()
if result == 1:
    "Let's see where this leads!"
    
    jump go
    
else:
    "I think going back would be safer..."
    
    jump val

    
##########
label Right:
    
    
$ ui.vbox(xalign=0.5, yalign=0.5)
$ ui.textbutton("Continue", clicked=ui.returns(1))
$ ui.textbutton("Go back", clicked=ui.returns(2))
$ ui.close()

$ result = ui.interact()
if result == 1:
    "Let's see where this leads!"
    
    jump go
    
else:
    "I think maybe another path would be better..."
    
    jump val
    
##########
label Straight:      
    
    
$ ui.vbox(xalign=0.5, yalign=0.5)
$ ui.textbutton("Continue", clicked=ui.returns(1))
$ ui.textbutton("Go back", clicked=ui.returns(2))
$ ui.close()

$ result = ui.interact()
if result == 1:
    "Let's see where this leads!"
    
    jump go
    
else:
    "I should go back and see what other paths there are..."
    
jump val

##########
label go:
    
    
