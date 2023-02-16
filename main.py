def main():
    # display the intro screen.
    intro()
  
    try:  
  # Get the number gallons.
      gallons_needed = int(input('Enter the number of gallons: '))
   
  # Convert the gallons to liters.
      gallons_to_liters(gallons_needed)
      
    except:
      print("An execption occurred, try again by entering only a number")
      print()
      main()

  # The intro function displays an introductory screen.
def intro():
    print('This program converts measurements')
    print('in gallons to fluid liters. For your')
    print('reference the formula is:')
    print('1 gallon = 3.785 fluid liters')
    print()

  # The gallons_to_liters function accepts a number of
  # gallons and displays the equivalent number of liters.
def gallons_to_liters(gallons):
    liters = gallons * 3.785
    print('That converts to', liters, 'liters.')

  # Call the main function.
main()