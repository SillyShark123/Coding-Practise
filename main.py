#Jakub szafraniec
#lornshill academy
#19/08/2020

NamesInGroup = []
PupilPrice = []
counter = 0
y = True
n = False
totalPrice = 0


GroupName = input("What is the name of the group?: ")
NoOfPupils = int(input("How many people are in " + GroupName + "?: "))
while NoOfPupils < 4 and NoOfPupils > 10:
  print("Sorry enter a group number between 4 and 10")
  NoOfPupils = int(input("How many people are in " + GroupName + "?: "))


for counter in range(NoOfPupils):
    counter += 1
    PupilName = input("What is the name of the pupil number " + str(counter)+ ":")
    PupilOrder = input("Please enter 'y' if you want a photo and 'n' if you do not: ")
    while PupilOrder != "y" and PupilOrder != "n":
      print("please enter either y or n")
      PupilOrder = input("Please enter 'y' if you want a photo and 'n' if you do not: ")

    if PupilOrder == "y":
      price = float(4.99)
    else:
      price = float(3.00)
    NamesInGroup.append(PupilName)
    totalPrice += price
    PupilPrice.append(price)

print("Group: "+"(" + GroupName+")"+" Number In Group: " + "("+str(NoOfPupils)+")")

for counter in range(len(NamesInGroup)):
  print("Pupil:"+NamesInGroup[counter]+" Due:" + str(PupilPrice[counter]))
  
print("total due is: "+ str(totalPrice))


