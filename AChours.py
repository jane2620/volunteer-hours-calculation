"""
file that takes input of raw excel document and returns column of AC hours
adds 40 minutes to each inputted name
easily input/output data to copy/paste into excel document
be careful for nicknames
highlight excel document from names --> total minutes and paste into 'ExcelPaste' text file
make sure names on excel spreadsheet are ONLY first and last (combine middle initials w/ first name)
"""


def achours(initfile, finalfile):
    # initial input from you with names and number of minutes to give
    # format example: JaneCastleman JackHamilton LauraRay
    # must be spelled exactly right w/ capitalization and no space between first and last names
    initinput = input("Names: ")

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

    names = initinput.split(" ")
    # random temp variables
    # mostly for counting, checking, etc.
    count = 0
    var = 0
    boolean = False

    # checks inputted names against profiles to give hours to inputted names
    # adds 40 minutes to AC hours column
    # count/profiles print statements are for checking if number of names counted matches number inputted
    # prints out names that didn't match (e.g. if misspelled)
    for i in range(len(names)):
        for z in range(len(profiles)):
            var += 1
            if names[i] == profiles[z][0]:
                temp = int(profiles[z][1])
                temp += 40
                profiles[z][1] = str(temp)
                count += 1
                boolean = True
            if not boolean and var == len(profiles):
                print(names[i])
    print(count)

    # prints updated hours to one column in final file which can be pasted back into Excel document
    b = open(finalfile, "w")
    for i in range(len(profiles)):
        b.write(profiles[i][1])
        b.write("\n")


# calls function with text files you want
achours("ExcelPaste", "ACHoursFinal")
