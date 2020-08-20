#Jakub szafraniec
#lornshill academy
#19/08/2020

#Initialization
NamesInGroup = []
PupilPrice = []
counter = 0
y = True
n = False
totalPrice = 0

#Asking for first inputs
GroupName = input("What is the name of the group?: ")
NoOfPupils = float(input("How many people are in " + GroupName + "?: "))
#Input validation
while NoOfPupils < 4 and NoOfPupils > 10 or not NoOfPupils.is_integer():
  print("Sorry enter a group number between 4 and 10")
  NoOfPupils = float(input("How many people are in " + GroupName + "?: "))
NoOfPupils = int(NoOfPupils)

#Fixed loop which is linked to input of NoOfPupils (First Input)
for counter in range(NoOfPupils):
    counter += 1
    PupilName = input("What is the name of the pupil number " + str(counter)+ ":")
    PupilOrder = input("Please enter 'y' if you want a photo and 'n' if you do not: ")
    #Input validation
    while PupilOrder != "y" and PupilOrder != "n":
      print("please enter either y or n")
      PupilOrder = input("Please enter 'y' if you want a photo and 'n' if you do not: ")
    #If statement which gives right price to order
    if PupilOrder == "y":
      price = float(4.99)
    else:
      price = float(3.00)
    #appending apropriate date to arrays
    NamesInGroup.append(PupilName)
    totalPrice += price
    PupilPrice.append(price)

print("Group: "+"(" + GroupName+")"+" Number In Group: " + "("+str(NoOfPupils)+")")

#fixed loop which prints all arrays
for counter in range(len(NamesInGroup)):
  print("Person "+str(counter)+":"'{:10} {:10}'.format(NamesInGroup[counter],str(PupilPrice[counter])))
  #print("Pupil:"+NamesInGroup[counter]+" Due:" + str(PupilPrice[counter]))

#Print statement which shows the total price of everything
print("total due is: "+ str(totalPrice))


