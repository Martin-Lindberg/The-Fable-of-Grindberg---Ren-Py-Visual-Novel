# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image martin = "Martin domare.jpg"
image linn = "Linn glad.jpg"
image Grindy = "Grindy.jpg"
image skola = "Skola.jpg"
image gata = "Gata.jpg"
image soffa = "soffa.jpg"
image bänk = "bänk.jpg"
image trädgård = "Trädgård.jpg"
image rum = "Rum.jpg"
image aula = "aula.jpg"
image norrsken = "norrsken.jpg"
image svart = "black.jpg"
image space = "space.jpg"
image grindberg glad = "Grindberg Glad.png" 
image grindberg ledsen = "Grindberg ledsen.png"
image dan = "Dan.png"
image victor glad = "Victor glad.png"
image victor panik = "Victor panik.png"
image mårten glad = "Mårten glad.png"
image mårten stress = "Mårten stress.png"
image mårten stress cykel = "Mårten stress cykel.png"
image sam ond = "Sam ond.png"
image sam glad = "Sam glad.png"
image sam disguise = "Sam glad disguise.png"
image sam ledsen = "Sam ledsen.png"
image vidar glad = "Vidar glad.png"
image vidar2 = "Vidar glad2.png"
image vidar3 = "Vidar glad3.png"
image vidar4 = "Vidar glad4.png"
image vidar5 = "Vidar glad5.png"
image vidar6 = "Vidar glad6.png"
image vidar7 = "Vidar glad7.png"
image vidar ledsen = "Vidar ledsen.png"




# Declare characters used by this game.
define b = Character('Berättare', color="#c8ffc8")
define g = Character('Grindberg', color="#FFA500")
define s = Character('Sam', color="#CC6600")
define vid = Character('Vidar', color="#3333FF")
define m = Character('Mårten', color="#99CC00")
define vic = Character('Victor', color="#99CC00")
define mvic = Character('Mårten & Victor', color="#FFA500")
define o = Character('???', color="#FFA500")
define f = Character('Främling', color="#99CC00")
define br = Character('Brüno', color="#FFA500")
define d = Character('Dan', color="#3333FF")






# The game starts here.
label start:
    
    #fixa svart bakgrund
    
    show svart:
        zoom 5
    
    b "..."
    
    play music "O Fortuna.mp3"
    
    b "I begynnelsen fanns ingenting"
    
    b "Allt bestod av mörker"
    
    b "Allt levande famlade efter något att klänga sig fast vid"
    
    b "Alla sökte ett ljus som kunde leda dem i en värld fylld av mörker"
    
    b "Och en dag föddes detta ljus"
    
    b "Detta ljus sken över allt levande och befriade världen från allt mörker"
    
    b "Och idag ska ni få höra en historia om detta ljus..."
    
    #Få någon att designa en ny titelskärm
    
    scene Grindy
    
    "The Fable of Grindberg"
    
    stop music fadeout 1

    scene skola
    
    play music "Deduction.mp3"
    
    b "Det var en gång en Simon, Simon Grindberg."
    
    b "Han var kung över KG, ett mäktigt litet rike i mitten av Stockholm."
    
    b "De flesta såg Simon som en vis och rättmätig kung, med djup stämma tilltalade han sina undersåtar varje morgon:"
    
    show grindberg glad:
        xalign .9 yalign .5
    
    g "-Amen tjena"
    
    hide grindberg glad with dissolve
    
    b "Han var den visaste kung som någonsin hade existerat."
    
    b "Han var snygg, sexig och singel och såg till att alla på KG var lyckliga."
    
    b "Men allt förändrades en dag när den elaka trollkarlen Sam Molavi försökte att stoppa kungen."
    
    stop music fadeout 1
    
    scene soffa
    
    show sam ond:
        xalign .1 yalign .5
        
    play sound "ont skratt.mp3"
    
    s "-Moahaha! Jag skall ta över världen."
    
    s "-Med mina många svåra ord och min förkärlek för nior ska jag få Grindberg på fall och regera med järnhand!"
    
    b "Sam var en ond jävel som älskade progressiv housemusik, svåra accord och att göra livet surt för Kung Grindberg."
    
    hide sam ond
    
    b "Till sin hjälp hade han Vidar, en kille som gillade två saker: att sova och att röka."
    
    show vidar glad:
        xalign .1 yalign .5
       
    b "Varför han hjälpte Sam var oklart. Han kanske hade en armé av cigg också."
    
    hide vidar glad with dissolve
    
    scene bänk with fade
    
    play music "prat.mp3"
    play music "Your Affection.mp3"
    
    show grindberg glad:
            xalign .9 yalign .5
    
    b "En dag var Kung Grindberg ute och gick som vanligt på sina ägor."
    
    b "Då kom plötsligt...!"
    
    show mårten glad at left
    
    show victor glad at center
    
    b "Två av hans allra mest lojala tjänare, Mårten och Victor, fram bakom en bänk."
    
    b "De båda var rufsiga i håret och täckta av rivmärken."
    
    b "De var tätt omslingrade runt varandra, mer närgångna än Drottningarna Evelina och Ruby av grannlandet Snuskotopia."
    
    b "De hade endast ögon för varandra, men när kungen harklade sig vände sig båda mot honom med breda léenden."
    
    vic "-O store Gravi! Vad roligt att se er!" 
         
    vic "-Ni har väl inte glömt vad som händer ikväll! Det är ju eder viktigaste dag på hela året."
    
    b "Det var nämligen filmquiz nere på folkets hus."
    
    b "Detta var årets höjdpunkt för Simon, filmälskare som han var."
    
    b "Han njöt av att briljera med sina kunskaper om diverse filmer och regissörer." 
    
    b "Han hade dock aldrig vunnit..."
    
    b "Men var han alltid fast besluten om att \"Mamma Mia\" hade fått åtta oscars, alla tilldelade Benny Andersson..."
    
    g "-Självklart är jag förberedd. Jag kan omöjligen förlora i år, jag har sett \"Apocalypse Now\" fyra gånger nu."
    
    m "..."
    
    vic "..."
    
    vic "-Ers nåd, inte för att besvära er men..."
    
    vic "-Jag betvivlar att det kommer komma några frågor om just den filmen..."
    
    g "-Inte det? Victor, du och din nästan ihopväxta andra hälft har varit mina närmsta rådgivare sedan tidernas begynnelse."
    
    g "-Säg mig, vad tror ni att jag bör se istället?"
    
    b "De båda spärrade upp ögonen."
    
    mvic "*harkel"
    
    mvic "-Gravity, Gravity, Gravity, Gravity, Gravity, Gravity, Gravity"
    
    g "..."
    
    g "-Amen..."
    
    g "-Tjena..."
    
    b "Och så gick Grindberg sin väg, med ett frö av oro planterat i sig."
    
    hide grindberg glad with dissolve
    
    vic "Glöm inte: klockan sju, ers majestät!"
    
    b "Grindberg nickade till svar och fortsatte gå."
    
    b "Vems historia vill du följa nu?"
    
    menu: 
        
        "Kung Grindberg, såklart!":
            
            jump choice_grindberg
            
        "Mårten verkar som den riktiga huvudkaraktären i den här historien":
            
            jump choice_mårten
            
    label choice_grindberg:
            
        $ menu_flag = True
            
        scene norrsken zoom 10
            
        show grindberg ledsen at right
            
        b "Senare på kvällen satt Grindberg och såg upp på himlen."
            
        b "Det var en vacker kväll, alldeles tyst och med ett vackert norrsken i skyn."
            
        b "Men kung Simon var ändå inte glad."
            
        g "..."
            
        g "Det är något som inte stämmer här."
            
        g "Sam vinner ju varje år och han brukar aldrig bli sjuk."
            
        show vidar2 at left
            
        b "Plötslig kom Vidar fram bakom ett hörn."
            
        vid "Eyy."
            
        g "Amen tjena."
            
        b "De stod under tystnad en stund, Vidar tände en cigarett."
            
        g "Kan jag också få en?"
            
        vid "Visst."
            
        g "Amen tack då."
            
        b "De stod tysta tills den sista glöden hade slocknat."
            
        b "Omgivna av den stickande doften av cigarettrök lät de tystnaden fylla natten och de båda njöt av varandras sällskap."
            
        b "Grindberg hade inte känt sig så lugn på länge."
            
        b "Han insåg att det här inte var rätt, stå och röka med sin ärkefiendes hejduk."
            
        b "Men den söta smaken av förbjuden frukt var för lockande."
            
        b "Skulle han?..."
            
        b "Grindberg vred sig sakta mot Vidar."
            
        menu: 
                
            "Kyss Vidar":
                jump choice1_yes
                
            "Fega ur":
                jump choice1_no
                    
        label choice1_yes:
            $ menu_flag = True
                
            g "Vidar, jag..."
                
            b "Han blev direkt avbruten av Vidar."
                
            vid "Håll käft och kom hit bara."
                
            b "Grindberg blev helt ställd, han had aldrig väntat sig att Vidar skulle vara den som tog initiativet."
                
            g "Okej då, nice."
                
            b "Sa Simon Grindberg med sin djupa stämma."
                
            jump choice_yes_done
                
        label choice1_no:
            $ menu_flag = False
                    
            g "Du, Vidar?"
                
            vid "Mmm?"
                
            g "Jag ska nog gå hem nu."
                
            b "Vidar såg likgiltig ut."
                
            vid "Okej, tja."
                
            b "Vidar släckte sin sista cigg och avlägsnade sig snabbt från området."
                
            jump choice_no_done
                
            label choice_yes_done:
                
            label choice_no_done:
                
            jump choice_grindberg_done
                
            label choice_grindberg_done:
                
            jump choice1_done
            
    label choice_mårten:
               
        $ menu_flag = False
    
        vic "Min lilla quickscope-snutteplutt? Tycker du inte att kungen verkar lite disträ i år?"
    
        m "Så sant, så sant, min knivälskare."
    
        m "Måtte det gå bra för honom ikväll..."
    
        m "-Nåja, jag borde väl också förbereda mig."
    
        b "Mårten ställde också upp i år, mest för nöjes skull då han egentligen visste mer om TV-serier och datorer än om film."
    
        hide victor glad
    
        hide mårten glad
    
        b "De båda såg på varandra en sista gång innan de motvilligt gick åt var sitt håll." 
    
        b "Därefter ekade endast tomhet på ägorna."
    
        stop music fadeout 1
    
        b "...eller inte!"
    
        play music "Osomatsu-San.mp3"
    
        b "Plötsligt kom trollkarlen Sam fram ur sin gömma bakom ett hörn."
    
        show sam ond:
            xalign .1 yalign .5
    
        s "-Tung baba, detta äro min chans!" 
    
        s "-Ikväll kommer jag, Sam Molavi, att besegra Simon Grindberg i ärlig kamp och därmed etablera mig själv som regent över detta etablissemang!"
    
        s "-Jag har en plan."
    
        s "-VIDAR!"
    
        show vidar glad:
            xalign .9 yalign .5
    
        vid "-Eyy"
    
        s "-Hämta min grafräknare!"
    
        s "-Jag behöver...\n...kalkylera \n"
    
        s "-Och ta av dig den där hatten!"
    
        s "-Du ser infantil ut."
    
        hide sam ond with dissolve
    
        hide vidar glad with dissolve
    
        stop music fadeout 1
            
        jump choice_mårten_done
            
        label choice_mårten_done:
            
        label choice1_done:
    
        scene trädgård with fade
    
        show grindberg ledsen:
            xalign .9 yalign .5
            
    b "Morgonen därpå var Grindberg lite orolig inför kvällens tävling."
    
    b "Han visste att Sam skulle tävla emot honom och säkert ställa till med bråk."
    
    b "Trots att varken Sam eller Grindberg någonsin hade vunnit första pris i filmquizen så var det alltid Sam som lyckades bäst av de båda."
    
    b "Simon var duktig, han visste en hel del om film."
    
    b "Men Sam hade alltid en tendens att förvirra Simon med sin konstiga vokabulär."
    
    g "-Vad ska jag göra?"
    
    b "Sa Simon med sin djupa stämma."
    
    g "-Sam kommer att ställa till det igen, jag är säker på det"
    
    show mårten glad at left
    
    b "Då kom Mårten gående med ett brev i handen."
    
    m "-Ers nåd?"
    
    m "-Jag har bud till er från Sam Molavi."
    
    b "Grindberg rynkade förvånat pannan och tog emot brevet."
    
    play music "Who's There.mp3"
    
    hide grindberg ledsen with dissolve
    
    hide mårten glad with dissolve
    
    show sam glad:
        xalign .1 yalign .5
    
    s "\"Kära konung Grindberg. Det smärtar vederbörande att behöva meddela om att jag resignerar från kvällens kamp på Folkets Hus.\""
    
    s "\"Jag har ådragit mig sjukdom och skall därför titta på Eurovisionsslagerfestivalen i min soffa drickande en varm kopp java.\""
    
    s "\"Jag önskar eder lycka och välgång ikväll samt att ni må lämna tävlingen som vinnare.\""
    
    s "\"Beder vänligen //Sam Molavi\""
    
    stop music fadeout 3
    
    hide sam glad with dissolve
    
    show mårten glad at left
    
    show grindberg ledsen:
        xalign .9 yalign .5
    
    g "-..."
    
    m "-...?"
    
    g "-Asså, jag förstår inte..."
    
    m "-Han drar sig ur..."
    
    g "-..."
    
    m "-..."
    
    b "Efter en lång tystnad gick det plötsligt upp för Kung Grindberg vad detta innebar."
    
    g "-Åh, jaha...vad bra! Då kommer jag säkert att kunna vinna ikväll"
    
    g "Detta kommer att bli storartat! Inget kan stoppa mig nu!"
    
    b "Men litade han verkligen på det?"
    
    menu:
        
        "Ja.":
            jump choice2_yes
        
        "Nej.":
            jump choice2_no
        
    label choice2_yes:
            
        $ menu_flag = True
            
        b "Visst gjorde han det!"
        
        b "Med Sam ur vägen var segern som i en liten ask för kungen."
        
        jump choice2_done
        
    label choice2_no:
           
        $ menu_flag = False
            
        b "Nää, något var skumt"
        
        b "Det var olikt Sam att dra sig ur på det här sättet."
        
        b "Dessutom: Varför meddela sin värsta ärkefiende om detta?"
        
        jump choice2_done
        
    label choice2_done:
    
    b "Oavsett vad Sam hade för intentioner så visste Simon att han var tvungen att komma på en ordentlig strategi för att försäkra sin vinst."
    
    g "-Mårten, min käre vän."
    
    g "-Du har alltid stått vid min sida. Hur ska jag vinna ikväll?"
    
    m "-..."
    
    m "{size=-10} Gravity, Gravity, Gravity, Gravity..."
    
    g "-Hursa?"
    
    m "-..."
    
    m "-Inget, ni bör se lite mer aktuell film och om möjligt lite fler klassiker, \"Sound Of Music\", \"Sjunde Inseglet\", \"Star Wars\""
    
    g "-..."
    
    show grindberg glad:
            xalign .9 yalign .5
    
    g "-GENIALISKT!"
    
    g "-Självklart borde jag göra det! Tack, Mårten!"
    
    hide grindberg ledsen
    
    b "Och så ringde han genast Hemmakväll och beställde ett gäng filmer."
    
    b "Han gick därefter in i sin kungliga kammare och stängde efter sig."
    
    hide grindberg glad with dissolve
    
    b "Mårten oroade sig för sin konung."
    
    b "Han brukade aldrig bete sig såhär."
    
    b "I ena stunden var han glad och i den andra mycket förvirrad eller orolig."
    
    b "Han gick sakta ner för trapporna med tunga steg då han plötsligt slogs av en tanke."
    
    m "\"Vem var det egentligen som brukade vinna filmquizen varje år???\""
    
    hide mårten glad
    
    show vidar glad
    
    show vidar2 at left
    
    show vidar3 at right
    
    show vidar4:
        xalign .9 yalign .5
        
    show vidar5:
        xalign .2 yalign .5
        
    show vidar6:
        xalign .99 yalign .5
    "VIDAR!!!"
    
    m "-Såklart! Sam ser till att Vidar vinner och passar samtidigt på att försöka med någon lurig plan!"
    
    m "-Jag måste stoppa honom!"
    
    m "-Men först..."
    
    menu:
        "Mega Makeout-session med Victor.":
            jump choice3_yes
    
        "Trumlektion.":
            jump choice3_no
            
    label choice3_yes: 
            
        $ menu_flag = True
            
    scene black
            
    play music "Muscle Blues.mp3"
    "..."
    
    "..."
    
    "..."
    
    jump choice3_done
        
    label choice3_no:
            
        $ menu_flag = False
            
        "..."
        
        "Skulle inte tro det ;)"
        
        jump choice3_yes
        
    label choice3_done:
    
    b "Han spenderade många timmar i Victors svettiga sovrum."
    
    b "De båda tog en powernap i varandras armar."
    
    b "Han vaknade efter ett långt tag med brännande smärtor i... höften... och drog sakta på sig sina kläder."
    
    b "En sista blick på sin ständiga CS:GO-partner och sedan öppnade han dörren och klev ut."
    
    stop music fadeout .5
        
    m "-Nu till att stoppa Sam!"
    
    scene rum with fade
    
    b "Han skyndade genast till Grindbergs kammare."
    
    play music "Border of Insanity.mp3"
    
    b "Bara för att upptäcka att den stod tom!"
    
    m "-Helvete! Vad är klockan?"
    
    b "Den var tjugo minuter i sju."
    
    scene gata
    
    show mårten stress cykel at left
    
    b "Han skyndade sig genast iväg till folkets hus så snabbt han kunde med sin cykel."
    
    m "-Jag måste hinna, kungens liv kanske står på spel..."
    
    m "-Vänta nu..."
    
    b "Hur stor sannolikhet var det?"
    
    b "Vem sa att Sam ljög från början?"
    
    b "(Okej, JAG sa det men shhh...)"
    
    m "-Kan det vara så att Sam faktiskt är sjuk?"
    
    menu:
        "Han är ju hyvens och så...":
            jump choice4_yes
            
        "Sam går icke att lita på.":
            jump choice4_no
            
    label choice4_yes:
        
        $ menu_flag = True
            
    m "-Varför oroa sig, det ska nog gå bra."
    
    b "Dock kunde han inte sakta ner farten, han hade nu endast 10 minuter på sig innan tävlingen började."
    
    jump choice4_done
    
    label choice4_no:
        
        $ menu_flag = False
        
    m "-NEJ! Jag måste skynda mig!"
    
    b "Och så ökade han farten ännu lite till."
    
    jump choice4_done
    
    label choice4_done:
        
    scene aula
    
    m "*pust *stånk *stön"
    
    show mårten stress at left
    
    m "-Jag...orkar...inte"
    
    m "-men jag hann! JAG HANN! WOOOOOOOOOOOOOOOOOOOOOAAAAAAAAAAA!!!"
    
    play music "New Days.mp3"
    
    b "Tomt som FAN var det."
    
    b "Fast vad hade han förväntat sig, det var ju trots allt FOLKETS HUS..."
    
    b "{size=-10} Ingen hänger på folkets hus..."
    
    m "-Jag ser kungen."
    
    b "Och mycket riktigt."
    
    hide mårten stress
    
    show grindberg glad:
        xalign .9 yalign .5
        
    b "Där framme satt han tillsammans med två andra personer."
    
    show vidar glad:
        xalign .1 yalign .5
        
    b "Vidar"
    
    b "Och en för Mårten okänd kille."
    
    show dan at center
    
    b "Alla såg ut att vara fullt uppslukade av Tarzan som spelades på en projektorskärm framför dem."
    
    m "-Tarzan...nice..."
    
    b "Då kom en man fram och började be om allas uppmärksamhet"
    
    stop music fadeout 2
    
    hide vidar glad with dissolve
    
    hide grindberg glad with dissolve
    
    hide dan with dissolve
    
    show sam disguise:
        xalign .3 yalign .5
    
    o "-Lüstring alles!"
    
    o "-Ich bien Brüno!"
    
    play music "A New World Fool.mp3"
    
    br "-Unt idag skall jag vara domare på denna tävling."
    
    br "-Ich accepterar inget füsk eller dåliga svaren-geheiht."
    
    br "-Må bästa zanstocker vinna."
    
    hide sam disguise with dissolve
    
    m "..."
    
    m "..."
    
    b "Mårten talade tyska."
    
    b "Det gjorde inte \"Brüno\"."
    
    m "-Whatever, inte som att jag inte kan svara på frågorna ändå."
    
    b "Trodde han, ja..."
    
    show sam disguise:
        xalign .1 yalign .5
    
    br "-Kan alles tagen zier aufdieplatzen?"
    
    b "Alla slog sig ner runt ett bord."
    
    br "-Ni skall nu allez svara på frågor, jaa?"
    
    br "-Ni får poängen när ni svaren rätt."
    
    br "-ünt minuspoängen när ni svaren spünkel!"
    
    br "-Alles klar, herr kommisar?!"
    
    b "Mårten såg hur Grindberg nervöst skruvade på sig i sin stol."
    
    show grindberg ledsen:
        xalign .9 yalign .5
    
    b "Han hade givetvis inte den blekaste om vad \"Brüno\" pratade om."
    
    b "Det hade inte Mårten heller, för den delen."
    
    hide grindberg ledsen with dissolve
    
    show vidar glad:
        xalign .9 yalign .5
    
    b "Vidar såg dock oberörd ut, detsamma gällde den okända personen."
    
    stop music fadeout 1
    
    hide vidar glad with dissolve
    
    show dan at right
    
    f "-Ursäkta, ursäkta!!"
    
    play music "Cirno's Perfect Math Class.mp3"
    
    b "Kläckte Främlingen ur sig."
    
    f "-Jo, jag har lite intressanta filosofiska teorier här ikväll som jag kanske kunde anse lämpliga för vad vi pratar om så skulle jag kanske..."
    
    br "-LÅS! Här ställs inga frågor! Jag ställer frågorna!"
    
    f "{size=-10} jomenjagtänkteattdetkanskevarviktigtförjagharfaktiskttänktganskamycketeastereggpåvadjagbordesägaochsåharvijuganskamyckettidochså..."
    
    br "-NEIN NEIN NEIN NEIN NEIN NEIN NEIN NEIN NEIN NEIN NIEN NEIN NEIN NEIN NEIN NEIN!!!!"
    
    f "-..."
    
    stop music fadeout 2.5
    
    hide dan with dissolve
    
    br "*harkel"
    
    br "-Javol! Första frågan!"
    
    br "-Vidar!"
    
    play music "Pokémon Theme.mp3"
    
    show vidar glad:
        xalign .9 yalign .5
    
    vid "-Eyy"
    
    br "-Vad bist den kända frasen Der Trollkaren säger i Sagan om Ringen i Moria?"
    
    vid "-..."
    
    vid "-You shall not pass."
    
    br "-Korrektum! Bra Vidar!!!!"
    
    hide vidar glad with dissolve
    
    br "*harkel"
    
    br "-Nästa fråga:"
    
    br "-Mårten"
    
    m "-Hmm?"
    
    br "-Vem skrev müsiken i filmen Crna mačka, beli mačor?"
    
    m "-..."
    
    m "-..."
    
    m "-pass?"
    
    br "-NEIN!"
    
    br "-Rätt svar bist Dr. Nelle Karajlic!"
    
    m "\"Orättvist, Vidars fråga var ju aslätt\""
    
    br "-Schawasenstucke, kung Simon!!"
    
    stop music fadeout 1
    
    show grindberg ledsen:
        xalign .9 yalign .5
        
    g "-Eeh, va?"
    
    br "-Din frågenfarenvaren bist gevolferslaf."
    
    g "-..."
    
    br "-Der firskilof bist i meine arsenhollegefeight?"
    
    g "-..."
    
    br "-FEL!"
    
    br "-Rätt svar var gul"
    
    br "-En så lätt fråga... Är ni säker på att ni bör vara med i denna tävling?"
    
    b "-Grindberg såg om möjligt ännu mer ledsen ut."
    
    hide grindberg ledsen with dissolve
    
    br "-Dan"
    
    show dan at right
    
    play music "Mario Kart - Wario´s Gold Mine.mp3"
    
    f "-Jaa! Jag är här! Är det jag?! Förresten! har du tänkt på hur vi kanske inte kan se färg på riktigt utan bara genom kaninernas..."
    
    br "-NEIN!!!"
    
    f "-..."
    
    b "Främligen hette alltså Dan...han var hyper."
    
    b "Väldigt hyper..."
    
    br "-Hur många oscars har mamma mia fått?"
    
    b "Grindberg fick plötsligt något mörkt i blicken."
    
    d "-Inga?"
    
    br "-..."
    
    br "-Rätt..."
    
    hide dan with dissolve
    
    stop music fadeout 2
    
    show grindberg ledsen:
        xalign .9 yalign .5
    
    b "Simons ögon dog..."
    
    b "Han hade tappat allt hopp om att han kunde svara rätt på någonting."
    
    b "Han var värdelös."
    
    b "Han passade inte som kung, vem vill regeras av en kung som inte kan något om film."
    
    b "Han skulle precis resa sig från sin stol och ge upp när plötsligt!..."
    
    hide grindberg ledsen
    
    play sound "explosion.mp3"
    
    "Boom!"
    
    b "Dörren till folkets hus slogs upp och en man endast iförd en T-shirt med Counter-Strike-tryck på rusade in i rummet."
    
    show victor panik at right
    
    vic "-MÅÅÅÅÅÅRTEEEEEEEN!!!"
    
    vic "-Var är duuuu???"
    
    vic "-Jag har glömt att spela in IDOOOOOOOL!!!"
    
    hide victor panik at right
    
    b "Kraften från dörren drev in en enorm vindpust som skakade om hela salen och slog Brüno rakt i ansiktet!"
    
    #släng in spear of justice här
    
    play music "Spear of Justice.mp3"
    
    show sam ledsen:
        xalign .2 yalign .5
        
    "..."
        
    show sam ledsen:
        xalign .2 yalign .5 zoom 1.5
        
    "..."
    
    show sam ledsen:
        xalign .2 yalign .5 zoom 2.0
        
    "..."
    
    show sam ledsen:
        xalign .2 yalign .2 zoom 3.0
        
    "..."
    
    show sam ledsen:
        xalign .2 yalign .5 zoom 1.0
        
    s "NEEEEEEJ! Detta äro en omöjlighet!"
    
    s "-Jag ska bli regent! Vederbörande! Blasfemi!!!!!!"
    
    show grindberg glad:
        xalign .9 yalign .5
                            
    g "-Så det var DU!"
    
    g "-Det här var din plan från början!"
    
    g "-Att få mig, KUNG SIMON GRINDBERG att avgå från tronen!"
    
    g "-Du skall bestraffas, Sam Molavi!"
    
    b "Och så gav Simon Sam en spark så hård att han flög hela vägen upp i rymden!"
    
    hide grindberg glad
    
    scene space
    
    show sam ledsen
    
    s "Neeeeeeeej!"
    
    scene aula
    
    stop music fadeout .3
    
    show grindberg glad:
        xalign .9 yalign .5
        
    "..."
    
    show vidar ledsen:
        xalign .1 yalign .5
        
    play music "Earth, Wind & Fire - September.mp3"
        
    g "-Vad ska jag göra med dig, då?"
    
    vid "-..."
    
    g "-Nåå, du har ju trots allt inte orsakat någon skada sååå...du är fri att gå."
    
    hide vidar ledsen
    
    show vidar glad:
        xalign .1 yalign .5
        
    vid "Säkert?"
    
    g "-På ett villkor."
    
    hide vidar glad
    
    show vidar ledsen:
        xalign .1 yalign .5
        
    g "-Du skall bli min nya högra hand. Jag kan behöva lite filmtips."
    
    g "-Och ta av dig den där jävla hatten!"
    
    b "Sa Simon Grindberg."
    
    b "Med sin djupa stämma."
    
    stop music fadeout 1
    
    $ renpy.movie_cutscene("credits.ogg")
        
    return
