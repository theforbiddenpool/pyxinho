import os
from sys import platform

def is_linux():
  if not platform.startswith('linux'):
    exit("OS not supported")

def main():
  is_linux()

  try:
    path = input("Path to directory: ")
    
    if not os.path.exists(path):
      raise Exception("Path doesn't exist")
    
    while True:
      rename_all_files = input("Rename all files? [Y/n] ").lower()
      if rename_all_files == 'y':
        print("yes!")
        break
      elif rename_all_files == 'n':
        print("no!")
        break
      else:
        print("\nPlease only enter Y or N!")
  except Exception as error:
    print(error)
  
  # i = 0
  # path = ""
  # for filename in os.listdir(path):
  #   my_dest = "img" + str(i) + ".jpg"
  #   my_source = path + filename
  #   my_dest = path + my_dest
  #   os.rename(my_dest, my_source)
  #   i += 1

if __name__ == '__main__':
    main()

