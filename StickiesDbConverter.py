import sys
stickiesDb = open("StickiesDatabase", "r", encoding="cp437")
try:
    newF = open(sys.argv[1], "w")
    x = stickiesDb.readlines()[7:]
    x[0] = ' '.join(x[0].split()[2:])

    for ind, line in enumerate(x):
        x[ind] = line[:-2]
        if ind == len(x) - 1:
            print(x[ind])
            newF.write(x[ind][:-117] + "\n")
        else:
            newF.write(x[ind] + "\n")
    newF.close()
except IndexError as e:
    print("Please include a file name to write your StickiesDatabase to.")
    exit(1)

finally:
    stickiesDb.close()



