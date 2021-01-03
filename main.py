#
# manager
#

import time
import curses
import random
from modules import convert
from modules import display
from modules import help
import sys
import os

curses.initscr()

def main():

          filename = ""

          files = os.listdir("./Assets")

          try:
                    if sys.argv[1] in files:
                              filename = sys.argv[1]
                    else :
                              filename = "Hello.java"
                    
          except IndexError:
                    filename = "Hello.java"

          dis = display.Display()
          dis.readfile(filename)

          win = curses.newwin(dis.get_screen_y(),dis.get_screen_x(),0,0)
          win.border(0)

          curses.noecho()
          curses.curs_set(0)
          win.keypad(1)
          #win.timeout(100)

          time_display = False
          time_detail_display = False
          count_display = False
          miss_count = False

          if "-h" in sys.argv:
                    help.helpwindow(win)
          if "-t" in sys.argv:
                    time_display = True
          if "-tt" in sys.argv:
                    time_detail_display = True
          if "-c" in sys.argv:
                    count_display = True
          if "-m" in sys.argv:
                    miss_count = True

          win.addstr(0,2,"< press start >")

          dis.print_text(win)
          value = win.getch()
          win.nodelay(1)

          win.border(0)

          time_begin = time.perf_counter()
          all_count = dis.get_count()

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

                                                  time_interval = time.perf_counter()

                                                  # display meta
                                                  win.addstr(dis.get_screen_y()-1,2,str(dis.get_progress()+1) + '/' + str(dis.get_len()))
                                                  if time_detail_display:
                                                            win.addstr(dis.get_screen_y()-1,8,"tt:" + str('{:.2f}'.format(time_interval-time_begin)))
                                                  elif time_display:
                                                            win.addstr(dis.get_screen_y()-1,14,"t:" + str(int(time_interval)-int(time_begin)))
                                                  if count_display:
                                                            win.addstr(dis.get_screen_y()-1,20,"c:" + str(dis.get_count()).zfill(dis.get_count_len()))
                                                  if miss_count:
                                                            win.addstr(dis.get_screen_y()-1,30,"m:" + str(dis.get_miss_count()).zfill(dis.get_count_len()))


                                                  # cursor
                                                  try:
                                                            win.addstr(i+dis.get_corsor_first_pos_y()-new_line,
                                                            k+dis.get_corsor_first_pos_x(),dis.get_data()[i][k],curses.A_REVERSE)
                                                  except curses.error:
                                                            pass

                                                  #win.addstr(11,10,str(k))

                                                  # input process
                                                  try:
                                                            if convert.con(value ,win, dis) == dis.get_data()[i][k]:

                                                                      dis.decrease_count()

                                                                      win.addstr(i+dis.get_corsor_first_pos_y()-new_line,
                                                                      k+dis.get_corsor_first_pos_x(),dis.get_data()[i][k],
                                                                      curses.A_UNDERLINE)

                                                                      break

                                                            # enter
                                                            elif k == len(dis.get_data()[i]) -1:

                                                                      if i == len(dis.get_data())-1:
                                                                                pass

                                                                      elif value == 10:
                                                                                if 0  < (dis.get_len() - dis.get_progress() - (dis.get_screen_y()-2)):
                                                                                         new_line += 1
                                                                                dis.enter_process(win)
                                                                                break
                                                            elif value != -1:
                                                                      dis.increase_miss_count()


                                                  except ValueError:
                                                            pass

                              #if i == 3:
                              #    break
    
          except KeyboardInterrupt:
                    curses.endwin()
                    print("System has been killed.")
                    sys.exit(0)

          curses.endwin()

          time_end = time.perf_counter()
          take_time = time_end - time_begin
          

          print("Practicing finished! Thank you for your hard work." )
          print("type_times:" + str(all_count) + " miss_types:" + str(dis.get_miss_count()) + 
          " took_times:" + str('{:.2f}'.format(take_time)) + " per_seconds:" + str('{:.2f}'.format(all_count / take_time)) + "type/s")


if __name__ == "__main__":
          main()

def helpwindow():
          pass