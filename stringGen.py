diq={'NP VP': ['S'], 'V NP': ['VP'], 'VP PP': ['VP'], 'P NP': ['PP'], 'NP PP': ['NP'], 'John': ['NP'], 'soccer': ['NP'], 'school': ['NP'], 'plays': ['V'], 'at': ['P']}

input=['John', 'plays', 'soccer', 'at', 'soccer']
'(S (NP /John/) (VP (VP (V /plays/) (NP /soccer/)) (PP (P /at/) (NP /soccer/))))'

All=set()

def nodify(array):
    arr=[]
    for i in array:
        for j in diq[i]:
            arr.append(j)
    return arr

def premute(array, words):
    if 'S' in array:
        All.add((' '.join(array),' '.join(words) ))

    for i in range (len(array)-1):
        left=array[i]
        right= array[i+1]
        key = left + ' ' + right
        if key in diq:
            for val in diq[key]:
                newWords=words[:]
                newArr=array[:]
                newArr[i]=val
                newArr.pop(i+1)
                if '(' not in newArr[i] :
                    newWords[i]='((%s /%s/) (%s /%s/))' %(array[i],newWords[i], array[i+1], newWords[i+1])
                else:
                    newWords[i] = '(%s (%s %s))' % (val, newWords[i], newWords[i + 1])
                newWords.pop(i + 1)
                premute(newArr,newWords)
#print(nodify(input))
premute(nodify(input), input)
for string in All:

    new=string[1].replace('/(', '').replace(')/','')
    print(string[0], ',', new)







# dict={}
# for i in diq:
#     #print (i)
#     new = i.split(' -> ')
#     if new[1] in dict:
#         dict[new[1]].append(new[0])
#     else:
#         dict[new[1]] = [new[0]]
#    # print('"',new[0],'"', ':[', '"', new[1], '"', '],')
# print( dict)