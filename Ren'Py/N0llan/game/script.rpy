# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

image gård = "KTH 12.jpg"


# Declare characters used by this game.
define b = Character('Berättare', color="#ffffff")
define n = Character('N0llan', color="#c8ffc8")
define r = Character('Ronya', color="#7733ff")
define t = Character('Gud', color="#481f6f")
define j = Character('Johan', color="#109a46")
define g = Character('Groth', color="#c22249")
define me = Character('Melabitch', color="#f22c45")
define rsa = Character('RSA', color="#ffffff")




# The game starts here.
label start:
    
    scene gård

    b "KTH"
    
    b "En skola olik alla andra."

    b "En plats fylld av magi och underverk."
    
    b "Men också av många faror"
    
    b "RSA, Inpisk, drifveriet och många fler sätter skräck i alla studenter på campus."
    
    b "Att komma in på KTH är en utmaning i sig."
    
    b "Men att överleva när man väl är inne, det är en helt annan sak."
    
    b "Särskilt en grupp av individer lever extra farligt."
    
    b "Det här är historien om en av dessa."
    
    b "HÄR SKA DET STÅ NOLLAN"
    
    

    return
