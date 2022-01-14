import time

hbd = """
█▄█ █▀█ █▀█ █▀█ █▄█
█▀█ █▀█ █▀▀ █▀▀ ░█
 
 █▀█ ▀ █▀█ ▀█▀ █  █ █▀▄ █▀█ █ █ █
 ███ █ █▄█  █  ████ █ █ █▄█  █  █
 █▄█ █ █ ▀█ █  █  █ █▄▀ █▀█  █  ▄
 """

def firework_animation():
    # Listen, just, listen okay. 
    # I have no idea what I'm doing. Is this a great approach to what I'm trying to do? No. Do I know a better approach? Also no
    # But it's going to work. oooooooooOOOWEEEEEEEEEEEEEEE
    firework_line0 = "                                   .''.       \n"
    firework_line1 = "       .''.      .        *''*    :_\/_:     . \n"
    firework_line2 = "      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.\n"
    firework_line3 = "  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-\n"
    firework_line4 = " :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'\n"
    firework_line5 = " : /\ : :::::     *_\/_*     -= o =-  /)\    '  *\n"
    firework_line6 = "  '..'  ':::'     * /\ *     .'/.\'.   '\n"
    firework_line7 = "      *            *..*         :\n"
    firework_line8 = "      *                          \n"
    firework_line9 = "      *                          \n"
    # Time to introduce some spaces UP IN HERE. BECAUSE IT'S GOING TO WORK
    # For reference I'm talking about ascii terminal animation. Never done it, first try, first thought as well
    # This should totally work yeah?
    firework_list = [firework_line0, firework_line1, firework_line2, firework_line3, firework_line4, firework_line5, firework_line6, firework_line7, firework_line8, firework_line9]
    firework = ""
    for i in range(len(firework_list)):
        firework += firework_list[i]
    print(firework)

    # 30 iterations should mimic like 30 frames... yeah?
    for i in range(30):
        firework = ""
        for j in range(len(firework_list)):
            # this is the animation aranic ancient magic
            if i % 5 == 0:
                firework += firework_list[j][:25] + "     " + firework_list[j][25:]
                pass
            elif i % 2 == 0:
                firework += "  " + firework_list[j]
            else:
                firework += firework_list[j]
        print(firework)
        time.sleep(0.15)
            
def drinks_animation():
    drink0 = "      (     (           o\n"
    drink1 = "  (                      _'\n"
    drink2 = "   )        (           {_}\n"
    drink3 = "  (          )          |=|\n"
    drink4 = "  #         (    '      | |\n"
    drink5 = "         o   #  o   o   |@|\n"
    drink6 = "(        . o  _o_._'_  /___\\\n"
    drink7 = " )      o_.__'\~~~~~/  |   |\n"
    drink8 = "(      \~~~~~/ '-.-'   |   |\n"
    drink9 = " )      '-.-'    |     |   |\n"   # I refuse to make it drink10 and have things shifted to the right by 1 character. NO
    drinka = "#         |     _|_    |   |\n"
    drinkb = "         _|_           |___|\n"
    
    drink_list = [drink0, drink1, drink2, drink3,
    drink4, drink5, drink6, drink7,
    drink8, drink9, drinka, drinkb]

    drink = ""

    for i in range(len(drink_list)):
        drink += drink_list[i]
    print(drink)

    # How about another 30 frames animation eh? Because I totally know what I'm doing this time 8)
    for i in range(30):
        drink = ""
        for j in range(len(drink_list)):
            if i % 2 == 0 and j < 6:
                drink += drink_list[j][1:20].replace('(', ')') + " " + drink_list[j][20:]  # this should shift things by 1 to the left, absolutely, yes sir yes sir
            else:
                drink += drink_list[j]
        print(drink)
        time.sleep(0.15)

    pass

print(hbd)
time.sleep(1.5)
firework_animation()
drinks_animation()
