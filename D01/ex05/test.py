"""    k.lower() == oqueeurecebi.lower() """

import sys

def all_in():
   if (len(sys.argv) == 2):
      str_full = str(sys.argv[1])
      l_str = str_full.split(",")
      for x in l_str:
         print(x)



if __name__ == '__main__':
    all_in()