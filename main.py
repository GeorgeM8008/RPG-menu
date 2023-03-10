


def menu():
  choice = input("Action: ") 
  direction = ['go north', 'go south', 'go west', 'go east']
  actions = ['explore', 'fight', 'defend', 'quit']

             
  if choice == "go north":
    print("You decide to " + direction[0])
    while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
      menu()


        
  elif choice == "go south":
    print("You decide to " + direction[1])
    while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
      menu()


        
  elif choice == "go west":
    print("You decide to " + direction[2])
    while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
      menu()


        
  elif choice == "go east":
    print("You decide to " + direction[3])
    while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
      menu()


        
  elif choice == "explore":
     print("You decide to " + direction[3])
    while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
      menu()

  elif choice == "attack":
  elif choice == "defend":
  elif choice == "quit":
    while choice == "Go North" or "go north" or "go south" or "Go South" or "go west" or "Go West" or "explore" or "attack" or "defend" or "quit" or "Quit":
      print("You decide to " + choice)
      if choice == "quit" or "Quit":
        break
      else: 
        menu()
  elif choice != "Go North" or choice != "go north" or choice != "go south" or choice != "Go South" or choice != "go west" or choice != "Go West" or choice != "explore" or choice != "attack" or choice != "defend" or choice != "quit" or choice != "Quit":
    print("I didn't understand that.")
    menu()


print(" ")
menu()