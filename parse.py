from nltk import Tree


# read lines from silly-corpus and format its strings
silly=[]
with open('silly-corpus', 'rt') as f:
    for row in f:
        silly.append(row.replace('\n', ''))

#update the Grammar value based on lines in silly-corpus
def dynamicGrammar():
    global diq
    for string in silly:
        t = Tree.fromstring(string)
        updateGrammar(t)

    for i in dynamic_grammar:
        val = i.split(' -> ')
        symbol = val[0]
        dynamic_grammar[i] = dynamic_grammar[i]/symbols[symbol]
        print(i, dynamic_grammar[i])

    diq = dynamic_grammar


#uniform grammar values
diq={"S -> NP VP":1,
     "VP -> V NP": 0.5,
     "VP -> VP PP": 0.5,
     "PP -> P NP": 1,
     "NP -> NP PP": 0.25,
     "NP -> John": 0.25,
     "NP -> soccer":0.25,
     "NP -> school":0.25,
     "V -> plays":1,
     "P -> at": 1}

symbols = {"NP": 0,
            "VP": 0,
            "PP": 0,
            "V": 0,
            "P": 0,
            "S": 0,
           }


dynamic_grammar={}



# helper to format the tree label
def parse(Tree):
    String = str(Tree)
    chars='()/'
    for i in chars:
        String = String.replace(i, '')

    return String.replace(' ', ' -> ')

# help to print with correct indents
def pprint(label, *arg):
    spaces=''
    for i in range(20 - len(label)):
        spaces = spaces + ' '
    print(label, spaces, *arg)

# find the probability of given Tree
def getValue(Tree):
    if len(Tree)==1:
        label = parse(Tree)
        value = diq[label]
        pprint(label, 'leaf', value)
        return value

    left = Tree[0]
    right = Tree[1]
    selfLabel = '%s -> %s %s' % (Tree.label(), left.label(), right.label())
    selfValue = diq[selfLabel]

    leftVal = getValue(left)
    rightVal = getValue(right)

    pprint(selfLabel, 'total:', selfValue * leftVal * rightVal, 'children:', leftVal ,',' , rightVal, 'self:' ,selfValue   )
    return selfValue * leftVal * rightVal

#given a tree, update the curent grammar values
def updateGrammar(Tree):
    if len(Tree)==1:
        label = parse(Tree)
        #print(label)
        symbols[Tree.label()] += 1
        if label in dynamic_grammar:
            dynamic_grammar[label]+=1
        else:
            dynamic_grammar[label]=1
        return

    left = Tree[0]
    right = Tree[1]
    selfLabel = '%s -> %s %s' % (Tree.label(), left.label(), right.label())
    symbols[Tree.label()]+=1
    updateGrammar(left)
    updateGrammar(right)
    if selfLabel in dynamic_grammar:
        dynamic_grammar[selfLabel]+=1
    else:
        dynamic_grammar[selfLabel]=1

    return

#Uncomment this to use dynamic Grammar from silly corpus
#dynamicGrammar()



#2a john plays soccer at soccer
#print(getValue(Tree.fromstring('(S (NP /John/) (VP (V /plays/) (NP (NP /soccer/) (PP (P /at/) (NP /soccer/)))))')))
#print(getValue(Tree.fromstring('(S (NP /John/) (VP (VP (V /plays/) (NP /soccer/)) (PP (P /at/) (NP /soccer/))))')))

#2b for john plays soccer at school
print(getValue(Tree.fromstring('(S (NP /John/) (VP (VP (V /plays/) (NP /soccer/)) (PP (P /at/) (NP /school/))))')))
print(getValue(Tree.fromstring('(S (NP /John/) (VP (V /plays/) (NP (NP /soccer/) (PP (P /at/) (NP /school/)))))')))

#2b for john plays soccer
print(getValue(Tree.fromstring('(S (NP /John/) (VP (V /plays/) (NP /soccer/)))')))