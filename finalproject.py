#Manuel Duran 1584885

import copy
import csv
from operator import itemgetter
from datetime import date,datetime

# making the lists to implement the csv data
mfl = []
prl = []
sdl = []

# including data from each csv file
with open("ManufacturerList.csv") as manlist:
    ml = csv.reader(manlist)
    for line in ml:
        mfl.append(line)
with open("PriceList.csv") as pricelist:
    pl = csv.reader(pricelist)
    for line in pl:
        prl.append(line)
with open("ServiceDatesList.csv") as sdlist:
    sl = csv.reader(sdlist)
    for line in sl:
        sdl.append(line)

# making the lists to go by order ID
new_mfl = (sorted(mfl, key=itemgetter(0)))
new_prl = (sorted(prl, key=itemgetter(0)))
new_sdl = (sorted(sdl, key=itemgetter(0)))

# service dates and missing prices are now added to the (main) list
for x in range(0, len(new_mfl)):
    new_mfl[x].append(new_prl[x][1])
for x in range(0, len(new_mfl)):
    new_mfl[x].append(new_sdl[x][1])

# moving the item status to the end of the list
for x in range(0, len(new_mfl)):
    new_mfl[x].append(new_mfl[x].pop(3))
    
final_list = new_mfl
full_inventory = (sorted(final_list, key=itemgetter(1)))

# making the full inventory list
with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)

    for x in range(0, len(full_inventory)):
        fiwrite.writerow(full_inventory[x])

# constructing the list item types
item_type = final_list
tower_list = []
laptop_list = []
phone_list = []

#analyzing each list for specific item types and then creating their own lists
for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower_list.append(item_type[x])
    elif item_type[x][2] == "phone":
        phone_list.append(item_type[x])
    elif item_type[x][2] == "laptop":
        laptop_list.append(item_type[x])

# without the item type in each of these files
# making the file for item types
with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)
    temp_laptop_list = copy.deepcopy(laptop_list)
    for i in range(0, len(temp_laptop_list)):
    	temp_laptop_list[i].remove("laptop")

    for x in range(0, len(temp_laptop_list)):
        liwrite.writerow(temp_laptop_list[x])

with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)
    temp_phone_list = copy.deepcopy(phone_list)
    for i in range(0, len(temp_phone_list)):
    	temp_phone_list[i].remove("phone")
 
    for x in range(0, len(temp_phone_list)):
        piwrite.writerow(temp_phone_list[x])

with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)
    temp_tower_list = copy.deepcopy(tower_list)
    for i in range(0, len(temp_tower_list)):
    	temp_tower_list[i].remove("tower")


    for x in range(0, len(temp_tower_list)):
        tiwrite.writerow(temp_tower_list[x])

# making a completely new list for damaged products

damagedlist = []

for x in range(0, len(item_type)):
    if item_type[x][5] == "damaged":
        damagedlist.append(item_type[x])
    # else:
    # print("DEBUG TEST")

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))


# writing a damaged products file
with open('DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)

    for x in range(0, len(damagedlist)):
        diwrite.writerow(damagedlist[x])

pastservicedatelist = []
todaysdate = datetime.now()

# adding data to the PastServiceDateList if date is bad or not compatible
for row in full_inventory:
    if datetime.strptime(row[4], "%m/%d/%Y") < todaysdate:
        temp_list = [row[0],row[1],row[2],row[3],row[4]]
        pastservicedatelist.append(temp_list)
    # else:
    # print("DEBUG TEST")

#do logic sorting past service date list based on service date
pastservicedatelist.sort(key=lambda row : datetime.strptime(row[4], "%m/%d/%Y"))
    
# for line in pastservicedatelist:
#     print(line)
# write past service date list
with open('PastServiceDateInventory.csv', 'w') as newfile:
    pastservicedatewrite = csv.writer(newfile)
    for x in range(0, len(pastservicedatelist)):
        pastservicedatewrite.writerow(pastservicedatelist[x])
        # else:
        # print("DEBUG TEST")

# Asking the user for their manufacturer and item type

# arrays that store the available inventories
manufacturers = ["Dell", "Lenovo", "Apple"]
typeVar = ["tower", "laptop", "phone"]


user_manuf = str(input("Enter your manufacturer: "))


# print(final_list)
your_item = []

# Q is the exit value so while the input does not equal q, execute the program
while (user_manuf != "q"):
    # initialize the variables to empty string and false
    typeFound = False
    manufacturerFound = False
    manufacturerBrand = ""
    typeOfItem = ""
    # checking to see if user_manuf includes any manufacturers
    for a in range(0, len(manufacturers)):
        if manufacturers[a] in user_manuf and user_manuf.count(manufacturers[a]) == 1:
            manufacturerBrand = manufacturers[a]
            manufacturerFound = True
        # if manufacturer already found but another one appears, initialize variables again and display no such item in inventory
        elif manufacturers[a] in user_manuf and user_manuf.count(manufacturers[a]) == 1 and manufacturerFound == True:
            manufacturerBrand = ""
            manufacturerFound = False
    user_type = str(input("Please enter your item type: "))
    # checking to see if user_type includes any item types
    for b in range(0, len(typeVar)):
        if typeVar[b] in user_type and user_type.count(typeVar[b]) == 1:
            typeOfItem = typeVar[b]
            typeFound = True
        # if item type already found but another one appears, initialize variables again and display no such item in inventory
        elif typeVar[b] in user_type and user_type.count(typeVar[b]) == 1 and typeFound == True:
            typeOfItem = ""
            typeFound = False
    for x in range(0, len(final_list)):
        # print(str(final_list[x]))
        # if ('Dell' in str(final_list[x])):
        #     print('dell found')
        if manufacturerBrand in str(final_list[x]) and typeOfItem in str(final_list[x]):
            your_item.append(final_list[x])
            # If nothing was added to the list that means the product does not exist
            # if a valid manufacturer and item type was found
    if len(your_item) != 0 and manufacturerFound == True and typeFound == True:
        for i in range(len(item_type)):
            # if it is not damaged, not the same item, and a manufacturer has the same item type
            if (item_type[i][2] == your_item[0][2] and item_type[i][5] != "damaged" and item_type[i][1] != your_item[0][1]):
                print("You may also like:" + str(item_type[i]))
                # else:
                    # print("DEBUG TEST")
        your_item = sorted(your_item, key=itemgetter(4), reverse=True)
        print("Your Item is: ", your_item[0])
        your_item = []
    else:
        print("No such item in Inventory")

    user_manuf = str(input("Enter your manufacturer, or q to exit query: "))