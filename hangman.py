import random 

words = ["book","tree","python","bag","umberella","clock","engineer"]
joon=10

word = random.choice(words)

a = []
for i in range(len(word)):
    a.append('_')

        while joon>0:
           print(''.join(a))
           if((''.join(a))== word):
               print('winer')
               break
            b - input()
            b = b.lower()
            if (b in word):
                print('true'= joon)
            for i in range(len(word)):
                if (word[i]== b):
                    a[i] = b
        else:
            joon=-1
            print('ashtebh')
            
