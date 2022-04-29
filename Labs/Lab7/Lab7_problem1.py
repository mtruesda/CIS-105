#
# This program will create a superhero name using birth date
# @MyronTruesdale
# 5/3/2020
# Lab 7 - Problem 1
#

# dictionaries
monthSet = {'January':'Garnet', 'February':'Amethyst', 'March':'Aquamarine', 'April':'Quartz', 'May':'Emerald',
            'June':'Pearl', 'July':'Ruby', 'August':'Peridot', 'September':'Sapphire', 'October':'Tourmaline',
            'November':'Citrine', 'December':'Turquoise'}
daySet = {'1':'Dog', '2':'Cat', '3':'Cow', '4':'Horse', '5':'Sheep', '6':'Goat', '7':'Pidgeon', '8':'Fox',
          '9':'Deer', '10':'Duck', '11':'Chicken', '12':'Rabbit', '13':'Hamster', '14':'Goldfish', '15':'Mouse',
          '16':'Turtle', '17':'Bear', '18':'Pig', '19':'Peacock', '20':'Eagle', '21':'Owl', '22':'Turkey',
          '23':'Muskrat', '24':'Otter', '25':'Lynx', '26':'Wolverine', '27':'Porcupine', '28':'Moose',
          '29':'Reindeer', '30':'Raccoon', '31':'Hawk'}

# introductory function
def intro():
    print('This program will create a superhero name using birth date')

# main function
def main():
    # collects user inputs
    birthMonth = input('What month were you born? ')
    while(birthMonth.capitalize() not in monthSet):
        print('Enter an actual month')
        birthMonth = input('What month were you born? ')
    
    birthDay = input('What day were you born? ')
    while(birthDay not in daySet):
        print('Enter a valid day')
        birthDay = input('What day were you born? ')
        
    # ensures the first letter is capitalized
    birthMonth = birthMonth.capitalize()
            
    print("""Your "superhero name" is """ + monthSet[birthMonth] + ' ' + daySet[birthDay])

intro()
main()
