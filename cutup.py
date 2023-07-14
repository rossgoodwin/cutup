from sys import argv

script, book, ll = argv

# Open single page text file (original source)
f = open(book, "r")
text = f.read()
f.close()

# Set line length
lineLength = int(ll)

# Split text into word tokens
tokens = text.split()

# Split tokens into lines
curLine = []
lines = [] # 2D list

charCount = 0

for t in tokens:
    charCount += len(t)+1
    if charCount <= lineLength+1:
        curLine.append(t)
    else:
        lines.append(curLine)
        curLine = []
        charCount = len(t)+1
        curLine.append(t)

# Make horizontal cut
hCutPt = int(len(lines)/2)
hSections = [lines[:hCutPt], lines[hCutPt:]]

# Make vertical cut
sections = [[] for i in range(4)] # 3D list
for i in range(4):
    for l in hSections[int(i/2)]:
        sections[i].append([])

for i in range(2):
    lineCount = 0
    for l in hSections[i]:
        charCount = 0
        for w in l:
            charCount += len(w)+1
            if charCount <= lineLength/2 + 1:
                sections[0+i*2][lineCount].append(w)
            else:
                sections[1+i*2][lineCount].append(w)
        # sections[0+i*2][lineCount].append('\n')
        lineCount+=1

# Rearrange per Burroughs' instructions
sections.reverse()

# Print result with line breaks
for i in [0, 2]:
    for j in range(len(sections[i])):
        print (' '.join(sections[i][j]), ' '.join(sections[i+1][j]))
