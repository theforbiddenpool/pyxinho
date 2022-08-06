import os

def rename_all(path: str):
  i = 0
  abspath = os.path.abspath(path)

  prefix = input("Enter a suffix for the new name (press enter if none): ")

  for filename in os.listdir(abspath):
    extension = os.path.splitext(filename)[1]

    original_name = os.path.join(abspath, filename)
    new_name = os.path.join(abspath, prefix + '_' + str(i) + extension)

    j = 1
    while os.path.exists(new_name):
      if new_name == original_name:
        break

      new_name = os.path.join(abspath, str(i) + "_" + str(j) + extension)
      if j == 10:
        raise Exception("New file name already exists and couldn't be renamed")
      j += 1

    os.rename(original_name, new_name)
    print("Renamed %s to %s" %(original_name, new_name))
    i += 1
  print("\nRenamed %d files" %i)


def main():
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

