# Smith-Waterman Algorithm

import numpy

sequence1 = "GAATTCAGTTA"
sequence2 = "GGATCGA"

m = 5                                        # Match score
s = -3                                       # Mismatch score
w = -4                                       # Gap penalty
row = len(sequence2) + 1
col = len(sequence1) + 1
max_value,p,q = 0,0,0

# Initialization Step ...................................

scoringMatrix = numpy.full((row,col), 0).tolist()
directionMatrix = numpy.full((row-1,col-1), '').tolist()


# Matrix filling Step (Scoring) .........................

for i in range(1,row):
    for j in range(1,col):
        
        U = scoringMatrix[i-1][j] + w
        L = scoringMatrix[i][j-1] + w

        if sequence2[i-1] == sequence1[j-1]:
            D = scoringMatrix[i-1][j-1] + m
        else:
            D = scoringMatrix[i-1][j-1] + s
            
        mm = max(D,L,U,0)
        
        if mm == D:
            directionMatrix[i-1][j-1] = 'D'
            scoringMatrix[i][j] = D
        elif mm == L:
            directionMatrix[i-1][j-1] = 'L'
            scoringMatrix[i][j] = L
        elif mm == U:
            directionMatrix[i-1][j-1] = 'U'
            scoringMatrix[i][j] = U


# Traceback Step .......................................

max_value = 0

for i in range(1,row):
    if max_value < scoringMatrix[i][col-1]:
        max_value = scoringMatrix[i][col-1]
        p,q = i,col-1

for i in range(1,col):
    if max_value < scoringMatrix[row-1][i]:
        max_value = scoringMatrix[row-1][i]
        p,q = row-1,i

i,j=p,q
s1,s2 = "",""

while i!=0 or j!=0:

    if directionMatrix[i-1][j-1] == 'L':
        j-=1
        s1=s1+sequence1[j]
        s2=s2+'-'
    elif directionMatrix[i-1][j-1] == 'U':
        i-=1
        s1=s1+'-'
        s2=s2+sequence1[i]
    else:
        i-=1
        j-=1
        s1=s1+sequence1[j]
        s2=s2+sequence2[i]

# print('Scoring matrix:\n')
# for i in range(0,row):
#     print(scoringMatrix[i])

# print('\n\n\n\nDirection matrix:\n')
# for i in range(0,row-1):
#     print(directionMatrix[i])

print('\n\nMaximum local alignment score: {}\n'.format(max_value))
print('\nResulting local alignment:\n')
print(s1[::-1])
print(s2[::-1])


# Maximum local alignment score: 14


# Resulting local alignment:

# GAATTC-A
# GGA-TCCA