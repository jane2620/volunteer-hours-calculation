"""
program that takes input from file of pen pal names
as usual, must be spelled exactly right (which can be difficult)
automatically adds 30 minutes to each pen pal each time you run it
(so only run once each time a letter is sent)
No input other than file names (don't have to type out names like AC hours)
highlight excel document from names --> total minutes and paste into 'ExcelPaste' text file

Potential improvement:
- at the beginning of the year when pen pals start, save all indices of pen pal names
- that way, you don't have to read/index the file/names each time
- more efficient but the program runs pretty quickly anyway
"""


def penpalhours():
    # same as AC hours, isolating profiles from raw excel data
    a = open("ExcelPaste", "r")
    initlines = a.readlines()
    profiles = []
    for i in initlines:
        profiles.append(i.split())
    names = []
    for i in range(len(profiles)):
        names.append(profiles[i][1] + profiles[i][0])

    # opening/reading files to get names
    # will need to update the penpalnames file next year
    b = open("penpalnames", "r")
    initnames = b.readlines()
    c = open("penpalhoursfinal", "w")

    # if names match, add 30 minutes to sponsored hours column
    for i in range(len(initnames)):
        for z in range(len(profiles)):
            if initnames[i] == profiles[z][1] + profiles[z][0] + "\n":
                temp = int(profiles[z][3]) + 30
                profiles[z][3] = str(temp)

    # prints final sponsored hours with additions to pen pals
    for i in range(len(profiles)):
        c.write(profiles[i][3])
        c.write("\n")


# won't return any print statements
# just returns "Process finished with exit code 0"
penpalhours()
