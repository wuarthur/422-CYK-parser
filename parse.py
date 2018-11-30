from nltk import Tree
t = Tree.fromstring('(S(NP /John/) (VP (V /plays/) (NP (NP /soccer/) (PP (P /at/) (NP /soccer/)))))')



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



def parse(Tree):
    String = str(Tree)
    chars='()/'
    for i in chars:
        String = String.replace(i, '')

    return String.replace(' ', ' -> ')


def pprint(label, *arg):
    spaces=''
    for i in range(20 - len(label)):
        spaces = spaces + ' '
    print(label, spaces, *arg)

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


print(getValue(t))

