import os

def main():
  i = 0
  path = ""
  for filename in os.listdir(path):
    my_dest = "img" + str(i) + ".jpg"
    my_source = path + filename
    my_dest = path + my_dest
    os.rename(my_dest, my_source)
    i += 1

if __name__ == '__main__': # run main function when program is called
    main()

