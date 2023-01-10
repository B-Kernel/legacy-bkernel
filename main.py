#Pre-Determined Variables
vardir = [["Bootloader.fun","Registry.fun"], ["Booted.var"], ["Command.inp"]]
booted = False
location = 0
#Imported Extensions
import random
import os
import time
#Bootloader
def Bootloader():
  if booted == False:
    print("Booting B Kernel...")
    time.sleep(random.randint(0, 5))
    print("B Kernel")
    return True
  else:
    print("Error 0x001 - Bootloader Instance Already Running")
#Registry
def Registry(x = 0):
  if x == 0: #Prints all Commands
    print(vardir[0]) #.fun Commands
    print(vardir[1]) #.var Commands
    print(vardir[2]) #.inp Commands
  elif x == "fun":
    print(vardir[0]) #only prints .fun Commands
  elif x == "var":
    print(vardir[1]) #only prints .var Commands
  elif x == "inp":
    print(vardir[2]) #only prints .inp Commands
#Post-Determined Variables
booted = Bootloader()
#Default Directory: /workspaces/bkernel
#I'll do this when I finish with my work D:
#Okay, I'll make a REGISTRY, you make a Directory sounds good
while booted == True:
  print("Type a command:")
  command = str(input("/workspaces/bkernel "))
  if "registry" in command:
    if command == "registry fun":
      Registry("fun")
    elif command == "registry var":
      Registry("var")
    elif command == "registry inp":
      Registry("inp")
    elif command == "registry":
      Registry()
    else:
      print("Error 0x002 - Not Found")
  elif "execute" in command:
    if command == "execute Bootloader.fun":
      Bootloader()
      print("Completed.")
    elif command == "execute Registry.fun":
      Registry()
      print("Completed")
    else:
      print("Error 0x003 -  File Cannot be Executed")
  elif "whereami" in command:
    if location == 0:
      print("/workspaces/bkernel")