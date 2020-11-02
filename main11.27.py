# Manuel Duran 1584885
def printRoster():

    keys = list(players.keys())

    keys.sort()

    # printing the roster
    print("ROSTER")
    for key in keys:
        print("Jersey number: %d, Rating: %d" % (key, players[key]))


# dictionary to store players jersey number (rating and keys as values)
players = {}

#  loop 5 times
for i in range(5):
    # ask user to enter player (i+1)'s jersey number and read
    jno = int(input("Enter player %d's jersey number:\n" % (i + 1)))

    # ask user to enter player (i+1)'s rating and read
    players[jno] = int(input("Enter player %d's rating:\n" % (i + 1)))

    # print new line
    print("")

printRoster()

# iterate while loop
while True:

    # print menu
    print(
        "\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n")

    # read user option
    option = input("Choose an option:\n")

    if option == 'o':
        printRoster()

    # if user option is 'a'
    elif option == 'a':
        # read new player's jersey number
        jno = int(input("Enter a new player's jersey number:\n"))

        # read new player's rating
        rating = int(input("Enter the player's rating:\n"))

        # add player details into players dictionary
        players[jno] = rating

    # if user option is 'd'
    elif option == 'd':
        # reads jersey number
        jno = int(input("Enter a player's jersey number:\n"))

        # checks to see if jersey number is in dictionary
        if jno in list(players.keys()):
            # deletes player
            del players[jno]

    elif option == 'u':
        # read a player's jersey number
        jno = int(input("Enter a player's jersey number:\n"))

        # read new player's rating
        rating = int(input("Enter a new rating for player:\n"))

        # updating player details into the dictionary
        players[jno] = rating

    elif option == 'r':
        # reads rating
        rating = int(input("Enter a rating:\n"))

        # retrieve all players jersey numbers
        keys = list(players.keys())

        # sort jersey numbers again
        keys.sort()

        # print players above given rating
        print("ABOVE %d" % (rating))

        count = 0
        for key in keys:
            # print player's rating and jersey number
            if (players[key] > rating):
                print("Jersey number: %d, Rating: %d" % (key, players[key]))

                # count 1
                count += 1

        # if no players have above given rating, print the error message
        if (count == 0):
            print("No players found above %d rating" % (rating))

    # if user option is q then stop the program
    if option == "q":
        break


