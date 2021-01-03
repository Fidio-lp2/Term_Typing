import curses

# 
# Allows Japanese input and mouse scrolling in the curses library.
# 
def con(value, window, file):
          values = [value]
          #string = ''
          # pring debug
          #print(type(values[0]))
    
          if 0x00000000 <= value <= 0x0000007F:
                    pass
          elif 0x000000C0 <= value <= 0x000000DF:
                    values.append(window.getch())
                    tmp = join_bits([insert_zero(bin(values[0] & 0b00011111), 5),
                    insert_zero(bin((values[1] & 0b00111111)), 6)])
                    value = int(tmp, 2)
          # japanese judge
          elif 0x000000E0 <= value <= 0x000000EF:
                    values.append(window.getch())
                    values.append(window.getch())
                    tmp = join_bits([insert_zero(bin(values[0] & 0b00001111), 4),
                    insert_zero(bin((values[1] & 0b00111111)), 6),
                    insert_zero(bin((values[2] & 0b00111111)), 6)])
                    #window.addstr(10,10,bin(values[0]))
                    #window.addstr(11,10,bin(values[1]))
                    #window.addstr(12,10,bin(values[2])) # ここの読み込みまでは正常動作を確認.
                    # print debug
                    #print(insert_zero(bin(values[0] & 0b00001111), 6))
                    #print(tmp)
                    value = int(tmp, 2)
                    #string = tmp
          elif 0x000000F0 <= value <= 0x000000F7:
                    values.append(window.getch())
                    values.append(window.getch())
                    tmp = join_bits([insert_zero(bin(values[0] & 0b00001111), 3),
                    insert_zero(bin((values[1] & 0b00111111)), 6),
                    insert_zero(bin((values[2] & 0b00111111)), 6),
                    insert_zero(bin((values[3] & 0b00111111)), 6)])
                    value = int(tmp, 2)
          else :
                    pass

          WHEEL_UP = 259
          WHEEL_DOWN = 258
          ENTER = 10

          # print debug
          #window.addstr(5,1,str(value))

          # judge scroll event
          if value == WHEEL_UP:
                    file.wheel_up_process()
          elif value == WHEEL_DOWN:
                    file.wheel_down_process()
          elif value == ENTER:
                    return value
          else:
                    return chr(value)

#
# Combines binary strings assigned to list types.
#
def join_bits(list):
          tmp = '0b'
          for value in list:
                    tmp += value[2:]
          return tmp

#
# Pad the desired digit 0 to the binary string.
#
def insert_zero(string, times):
          for i in range(0,times):
                    if len(string) == times + 2:
                              break
                    else:
                              string = string[:2] + '0' + string[2:]
          return string
