#
# manager
#

import curses
import random
from modules import convert
from modules import display
import sys

curses.initscr()

def main():

          try:
                    filename = sys.argv[1]
                    
          except IndexError:
                    filename = "Hello.java"

          dis = display.Display()
          dis.readfile(filename)
          

          win = curses.newwin(dis.get_screen_y(),dis.get_screen_x(),0,0)
          win.border(0)

          curses.noecho()
          curses.curs_set(0)
          win.keypad(1)
          win.nodelay(1)
          win.timeout(100)

          dis.print_text(win)

          # header and futter
          win.addstr(0,2,'< '+filename+' >')          

          value = ''

          # new line 
          new_line = 0

          try:

                    for i in range(0,len(dis.get_data()),1):  
                              for k in range(0,len(dis.get_data()[i]),1):
                                        while True:

                                                  win.timeout(10)
                                                  value = win.getch()

                                                  win.addstr(dis.get_screen_y()-1,2,str(dis.get_progress()+1) + ' / ' + str(dis.get_len()))

                                                  # cursor
                                                  try:      
                                                            win.addstr(i+dis.get_corsor_first_pos_y()-new_line,
                                                            k+dis.get_corsor_first_pos_x(),dis.get_data()[i][k],curses.A_REVERSE)
                                                  except curses.error:
                                                            pass

                                                  win.addstr(11,10,str(k))

                                                  # エンターキーを押されたとき、最後の列の文字を打ち終えていたならば終わらせる、この戦いをって感じでEnterKeyの入力を受け付ける.
                                                  # また、エンターキーを押下時、enter_processが起動したらカーソル位置を変えないためのプログラムの構築も必要.
                                                  try:
                                                            if convert.con(value ,win, dis) == dis.get_data()[i][k]:

                                                                      win.addstr(i+dis.get_corsor_first_pos_y()-new_line,
                                                                      k+dis.get_corsor_first_pos_x(),dis.get_data()[i][k],
                                                                      curses.A_UNDERLINE)

                                                                      break

                                                            # 改行エスケープシーケンスも含まれるので！
                                                            elif k == len(dis.get_data()[i]) -1:

                                                                      if i == len(dis.get_data())-1:
                                                                                pass

                                                                      elif value == 10:
                                                                                if 0  < (dis.get_len() - dis.get_progress() - (dis.get_screen_y()-2)):
                                                                                         new_line += 1
                                                                                dis.enter_process(win)
                                                                                break


                                                  except ValueError:
                                                            pass

                              #if i == 3:
                              #    break
    
          except KeyboardInterrupt:
                    curses.endwin()
                    print("システムが強制終了しました")
                    sys.exit(0)

          curses.endwin()
          print("Practicing finished! お疲れ様です！")


if __name__ == "__main__":
          main()