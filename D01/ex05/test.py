import sys

def all_in():
   if (len(sys.argv) == 2):
      str_full = str(sys.argv[1])
      l_str = str_full.split(",")
      for x in l_str:
         title_str = x.strip().title()
         if len(title_str):
            print("." + title_str + ".")


se nao tiver nas listas
   printar = l_str.strip() + "texto de saida"




if __name__ == '__main__':
    all_in()