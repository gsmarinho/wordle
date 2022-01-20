import random

def split (word):
    return [char  for char in word]

dictionary = ["abuse","adult","agent","anger","apple","award","basis","beach","birth","block","blood","board","brain","bread","break","brown","buyer","cause","chain","chair","chest","chief","child","china","claim","class","clock","coach","coast","court","cover","cream","crime","cross","crowd","crown","cycle","dance","death","depth","doubt","draft","drama","dream","dress","drink","drive","earth","enemy","entry","error","event","faith","fault","field","fight","final","floor","focus","force","frame","frank","front","fruit","glass","grant","grass","green","group","guide","heart","henry","horse","hotel","house","image","index","input","issue","japan","jones","judge","knife","laura","layer","level","lewis","light","limit","lunch","major","march","match","metal","model","money","month","motor","mouth","music","night","noise","north","novel","nurse","offer","order","other","owner","panel","paper","party","peace","peter","phase","phone","piece","pilot","pitch","place","plane","plant","plate","point","pound","power","press","price","pride","prize","proof","proxy","queen","radio","range","ratio","reply","right","river","round","route","rugby","scale","scene","scope","score","sense","shape","share","sheep","sheet","shift","shirt","shock","sight","simon","skill","sleep","smile","smith","smoke","sound","south","space","speed","spite","sport","squad","staff","stage","start","state","steam","steel","stock","stone","store","study","stuff","style","sugar","table","taste","terry","theme","thing","title","total","touch","tower","track","trade","train","trend","trial","trust","truth","uncle","union","unity","value","video","visit","voice","waste","watch","water","while","white","whole","woman","world","youth","layer","label","split"]

dictionaryHard = ["amain","ambit","ambry","ament","amice","ancon","elbow","anear","anele","anent","anile","anion","anker","ankus","anole","antre","apian","appui","araba","arefy","arete","argil","argol","argol","armet","arras","arris","arval","assot","atimy","atlas","atony","aubin","aught","aulic","azoth","azure","baize","barre","batik","baton","bavin","beata","beele","beira","belay","benet","berge","besom","bezel","bifid","bight","bilbo","bilge","bitts","biune","blain","blype","bodge","bogan","bolar","bolus","boman","bombe","bonce","bongo","borne","bosky","bosun","boult","bower","boyau","brach","brail","brank","brash","braxy","bream","breme","breve","broch","broma","bruit","buffe","bulla","bulse","burke","burse","cabas","cable","cabre","cadge","calix","calyx","caman","caple","caret","cavil","cella","cento"]

#wordToGuess = random.choice(dictionary)

while True:
    level = input("\nWanna play hard or easy?")
    if level == "easy":
        wordToGuess = random.choice(dictionary)
        j = 5
        break
    elif level == "hard":
        wordToGuess = random.choice(dictionaryHard)
        j = 20
        break
    else:
        print("\nCome on, it's not too dificult type easy or hard! :)")

while j > 0: #5 tries to guess the word
    print("\nGuess the 5 letters word. You have ",j,"attempts.")
    guess = input("\nType your guess: ")
    userGuess = split(guess) #function to split the word
    word = split (wordToGuess)
    result = []
    size = len(userGuess)
    if size != 5:
        print ("\nMust be 5 character word")
    
    else:
        if guess in dictionary or guess in dictionaryHard:
            
            if userGuess == word:
                print ("\nYES,", guess," is the answer!!")
                exit()
            else:
                i = 0
                while i in range (0,5):# 5 character word to compare
                    if userGuess[i] == word[i]:# check character in right spot
                        result.append (userGuess[i])
                    else:
                        if userGuess[i] in word:# check if word contains the character in any spot
                            print(userGuess[i], " is into another spot")
                            result.append("_")
                        else:
                            result.append("_")
                    i += 1
            result = "".join(result)# list to string
            print (result)
            j -= 1
        else:
            print ("\nYour guess is not in the dictionary list")
print (wordToGuess,"was the answer.")


   
    


