"""
file that takes input of raw excel document and returns column of sponsored
adds any number of minutes to each inputted name
easily input/output data to copy/paste into excel document
be careful for nicknames
highlight excel document from names --> total minutes and paste into 'ExcelPaste' text file
same thing as AC program but it's not set at 40 minutes
be careful to not put two spaces between names/numbers
potential improvement: rather than using input(" "), just write the list yourself
(e.g. just type in line 25: initinput = [name1, minutes1, name2, minutes2, etc.])

Hour type/column:
- names = 0
- achievement center = 1
- sponsored = 2
- outside = 3
"""


def otherhours(initfile, finalfile, column):
    # initial input from you with names and number of minutes to give
    # format: FirstLast minutesgiven
    # example: JaneCastleman 60 JackHamilton 120 LauraRay 300
    # must be spelled exactly right w/ capitalization and no space
    initinput = input("Names & minutes: ")

    # opens file & organizes into 2D array of names & minutes
    a = open(initfile, "r")
    initlines = a.readlines()
    profiles = []
    for i in initlines:
        profiles.append(i.split())

    for i in range(len(profiles)):
        tempvar = profiles[i][1] + profiles[i][0]
        profiles[i][0] = tempvar
        profiles[i].pop(1)

    # adds names and minutes to separate lists using for loop with double step
    # even though lists are separate, the index is the same for both
    # so names[i] is the person who should get minutes[i]
    inputs = initinput.split(" ")
    names = []
    minutes = []
    for i in range(0, len(inputs) - 1, 2):
        names.append(inputs[i])
        minutes.append(inputs[i + 1])

    # random temp variables oops
    # mostly for counting, checking, etc.
    count = 0
    var = 0
    boolean = False

    # checks inputted names against profiles to give hours to inputted names
    # adds corresponding minutes
    for i in range(len(names)):
        for z in range(len(profiles)):
            var += 1
            if names[i] == profiles[z][0]:
                temp = int(profiles[z][column])
                temp += int(minutes[i])
                profiles[z][column] = str(temp)
                count += 1
                boolean = True
                print(names[i])
            if not boolean and var == len(profiles):
                # prints out names that didn't match (e.g. if misspelled)
                print("not counted: " + names[i])

    # count print statement are for checking if number of names counted matches number inputted
    print("Names counted: " + str(count))

    # prints updated hours to one column which can be pasted back into Excel document
    b = open(finalfile, "w")
    for i in range(len(profiles)):
        b.write(profiles[i][column])
        b.write("\n")


# calls function with text files you want
# delete pound symbol for which you want
otherhours("ExcelPaste", "SponsoredHoursFinal", 2)
# otherhours("ExcelPaste", "OutsideHoursFinal", 3)
