#
# prepare the file data
#

import curses
import shutil
import subprocess

class Display:
          progress = 0
          file_len = 0
          file_data = []
          input_line = []
          count = 0
          miss_count = 0
          count_len = 0
          screen_x = 0
          screen_y = 0
          corsor_first_pos_x = 0
          corsor_first_pos_y = 0
          corsor_limit_right_x = 0
          corsor_limit_left_x = 0
          corsor_limit_upon_y = 0
          corsor_limit_bottom_y = 0
    #win
    #def __init__(self):
    #    global win
    #    win = window

          def readfile(self, file_name):
                    with open('Assets/' + file_name, 'r') as f:

                              self.file_data = f.readlines()
                              self.file_len = len(self.file_data)
                              fill_lengs = len(str(len(self.file_data))) + 1

                              self.corsor_first_pos_x = fill_lengs + 3
                              self.corsor_first_pos_y = 1

                              tmpx = ((subprocess.run(['tput','cols'],stdout=subprocess.PIPE)).stdout).rstrip()
                              tmpy = ((subprocess.run(['tput','lines'],stdout=subprocess.PIPE)).stdout).rstrip()
                              self.screen_x = int(tmpx)
                              self.screen_y = int(tmpy)
                              self.corsor_limit_right_x = self.screen_x + 1
                              self.corsor_limit_bottom_y = self.screen_y + 1
                              self.corsor_limit_left_x = fill_lengs + 3
                              self.corsor_limit_upon_y = 1

                    for i in range(0,len(self.file_data),1):
                              self.input_line.append(str(i+1).zfill(fill_lengs) + ': ' + self.file_data[i].rstrip())
                              self.count += len(self.file_data[i].rstrip())
                              self.count_len = len(str(self.count))
                              #win.addstr(i,i+1,line)

          def get_screen_x(self):
                    return self.screen_x

          def get_screen_y(self):
                    return self.screen_y

          def get_data(self):
                    return self.file_data
          
          def get_len(self):
                    return self.file_len

          def get_corsor_first_pos_x(self):
                    return self.corsor_first_pos_x

          def get_corsor_first_pos_y(self):
                    return self.corsor_first_pos_y

          def get_progress(self):
                    return self.progress

          def get_count(self):
                    return self.count

          def get_count_len(self):
                    return self.count_len

          def get_miss_count(self):
                    return self.miss_count

          def increase_miss_count(self):
                    self.miss_count +=1

          def decrease_count(self):
                    self.count -= 1
                    return self. count

          def print_text(self, window):
                    try:
                              win = window
                              for i in range(1,len(self.input_line)+1,1):
                                        if i <= self.screen_y-2 :
                                                  win.addstr(i,1,self.input_line[i-1])
                    except curses.error:
                              pass

          #
          # pressed enter process
          #
          def enter_process(self,win):
                    self.progress += 1

                    if 0  <= (self.file_len - self.progress - (self.screen_y-2)):
                              # init window
                              for i in range(1,self.screen_y-1,1):
                                        win.addstr(i,1,' '*(self.screen_x-2))
                              # print
                              for i in range(1,len(self.input_line),1):
                                        if i <= self.screen_y-2:
                                                  win.addstr(i,1,self.input_line[i+self.progress-1])

          #
          # wheel up process
          #
          def wheel_up_process(self):
                    pass

          #
          # wheel down process
          #
          def wheel_down_process(self):
                    pass
