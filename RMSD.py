import numpy as np
import argparse

parser = argparse.ArgumentParser()
#Cheat sheet of arguments to be used with the script
parser.add_argument("-inp", "--input", dest = "input", default = "file.xyz", help="Name of iput XYZ file")
parser.add_argument("-s", "--steps", dest = "steps", default = "200", help="Number of optimization steps used!")
args = parser.parse_args()


with open(args.input) as f:
    #Determines how many atoms in file
    numberofatoms = int(f.readline().rstrip())
g = open(args.input,"r")
content = g.readlines()
g.close()
#determines how many frames the file has
numberofrows = int(len(content)/(numberofatoms+2))

#Total optimization steps
totalsteps = int(args.steps)

totalRMSD = []

for j in range(numberofrows-1,numberofrows):
    Atoms1 = []
    Atoms2 = []
    newRMSD = []

    #Gets position from frame n
    for i in range(j*(numberofatoms+2)+2,j*(numberofatoms+2)+numberofatoms+2):
        Atoms1.append([float(content[i].split()[1]),float(content[i].split()[2]),float(content[i].split()[3])])
    #Gets position from frame n-1
    for i in range((j-1)*(numberofatoms+2)+2,(j-1)*(numberofatoms+2)+numberofatoms+2):
        Atoms2.append([float(content[i].split()[1]),float(content[i].split()[2]),float(content[i].split()[3])])

    #Calculates RMSD for individual atoms
    for i in range(len(Atoms1)):
        RMSD = np.sqrt((Atoms1[i][0] - Atoms2[i][0])**2 + (Atoms1[i][1] - Atoms2[i][1])**2 + (Atoms1[i][2] - Atoms2[i][2])**2)
        newRMSD.append(RMSD)

    #Calculates RMSD for whole system
    RMSDVal = 0
    for i in range(len(newRMSD)):
        RMSDVal += newRMSD[i]    

    #Checks if RMSD value is 0 and is below total optimization steps.
    if numberofrows<totalsteps:
        if RMSDVal == 0:
            print("Structure Optimized!")
        else:
            print("Structure NOT Optimized!")
    else:
        print("Structure NOT Optimized!")
