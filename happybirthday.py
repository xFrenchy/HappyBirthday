import time

hbd = """
█▄█ █▀█ █▀█ █▀█ █▄█
█▀█ █▀█ █▀▀ █▀▀ ░█
 
 █▀█ ▀ █▀█ ▀█▀ █  █ █▀▄ █▀█ █ █ █
 ███ █ █▄█  █  ████ █ █ █▄█  █  █
 █▄█ █ █ ▀█ █  █  █ █▄▀ █▀█  █  ▄
 """

firework = """
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
      *
      *
"""

# Listen, just, listen okay. 
# I have no idea what I'm doing. Is this a great approach to what I'm trying to do? No. Do I know a better approach? Also no
# But it's going to work. oooooooooOOOWEEEEEEEEEEEEEEE
firework_line0 = "                                   .''.       "
firework_line1 = "       .''.      .        *''*    :_\/_:     . "
firework_line2 = "      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'."
firework_line3 = "  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-"
firework_line4 = " :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'"
firework_line5 = " : /\ : :::::     *_\/_*     -= o =-  /)\    '  *"
firework_line6 = "  '..'  ':::'     * /\ *     .'/.\'.   '"
firework_line7 = "      *            *..*         :"
firework_line8 = "      *"
firework_line9 = "      *"

def firework_animation():
    firework_line0 = "                                   .''.       \n"
    firework_line1 = "       .''.      .        *''*    :_\/_:     . \n"
    firework_line2 = "      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.\n"
    firework_line3 = "  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-\n"
    firework_line4 = " :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'\n"
    firework_line5 = " : /\ : :::::     *_\/_*     -= o =-  /)\    '  *\n"
    firework_line6 = "  '..'  ':::'     * /\ *     .'/.\'.   '\n"
    firework_line7 = "      *            *..*         :\n"
    firework_line8 = "      *\n"
    firework_line9 = "      *\n"
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
        for j in range(len(firework_list)):
            pass

print(hbd)
time.sleep(1.5)
firework_animation()