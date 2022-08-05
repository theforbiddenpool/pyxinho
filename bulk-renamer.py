import os
from sys import platform

def is_linux():
  if not platform.startswith('linux'):
    exit("OS not supported")

def rename_all(path: str):
  i = 0
  abspath = os.path.abspath(path)

  for filename in os.listdir(abspath):
    extension = os.path.splitext(filename)[1]

    original_name = os.path.join(abspath, filename)
    new_name = os.path.join(abspath, str(i) + extension)

    os.rename(original_name, new_name)
    print("Renamed "+original_name+" to "+new_name)
    i += 1
  print("\nRenamed "+str(i)+" files")


def main():
  is_linux()

  try:
    path = input("Path to directory: ")
    
    if not os.path.exists(path):
      raise Exception("Path doesn't exist")
    
    while True:
      should_rename_all = input("Rename all files? [Y/n] ").lower()
      if should_rename_all == 'y' or should_rename_all == '':
        rename_all(path)
        break
      elif should_rename_all == 'n':
        print("no!")
        break
      else:
        print("\nPlease only enter Y or N!")
  except Exception as error:
    print("\n" + error)

if __name__ == '__main__':
    main()

