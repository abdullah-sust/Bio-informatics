# Needleman-Wunsch

import numpy

sequence1 = "GAATTCAGTTA"
sequence2 = "GGATCGA"

m = 5                                        # Match score
s = -3                                       # Mismatch score
w = -4                                       # Gap penalty
row = len(sequence2) + 1
col = len(sequence1) + 1

# Initialization Step ..................................

scoringMatrix = numpy.full((row,col), 0).tolist()
directionMatrix = numpy.full((row-1,col-1), '').tolist()

for i in range(1,col):
    scoringMatrix[0][i] = scoringMatrix[0][i-1] + w
    
for i in range(1,row):
    scoringMatrix[i][0] = scoringMatrix[i-1][0] + w

# Matrix filling Step (Scoring) .........................

for i in range(1,row):
    for j in range(1,col):
        U = scoringMatrix[i-1][j] + w
        L = scoringMatrix[i][j-1] + w
        
        if sequence2[i-1] == sequence1[j-1]:
            D = scoringMatrix[i-1][j-1] + m           
        else:
            D = scoringMatrix[i-1][j-1] + s

        if D >= U and D >= L:
            directionMatrix[i-1][j-1] = 'D'
            scoringMatrix[i][j] = D
        elif U > L:
            directionMatrix[i-1][j-1] = 'U'
            scoringMatrix[i][j] = U
        else:
            directionMatrix[i-1][j-1] = 'L'
            scoringMatrix[i][j] = L

# Traceback Step ............................................

i,j=row-1,col-1
s2 = ""

while i!=0 or j!=0:

    if directionMatrix[i-1][j-1] == 'L':
        j-=1
        s2=s2+'-'
    else:
        i-=1
        j-=1
        s2=s2+sequence2[i]

# print('Scoring matrix:\n')
# for i in range(0,row):
#     print(scoringMatrix[i])

# print('\n\n\n\nDirection matrix:\n')
# for i in range(0,row-1):
#     print(directionMatrix[i])

print('\n\nMaximum global alignment score: {}\n'.format(scoringMatrix[row-1][col-1]))
print('\nResulting global alignment:\n')
print(sequence1)
print(s2[::-1])


# Maximum global alignment score: 11


# Resulting global alignment:

# GAATTCAGTTA
# GGA-TC-G--A