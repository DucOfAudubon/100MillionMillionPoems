#!/usr/bin/env python
# coding: utf-8

# In[1]:


#this imports a library that lets the program generate random numbers

import random


# In[2]:


#All this is doing is making a specific way for the computer to recognize a "Sonnet"
#It's not as complicated as it looks. It's just a list of lines.

class Sonnet:
    
    def __init__(self, 
                 line1,
                 line2,
                 line3,
                 line4,
                 line5,
                 line6,
                 line7,
                 line8,
                 line9,
                 line10,
                 line11,
                 line12,
                 line13,
                 line14):
        self.lines = []
        self.lines.append(line1)
        self.lines.append(line2)
        self.lines.append(line3)
        self.lines.append(line4)
        self.lines.append(line5)
        self.lines.append(line6)
        self.lines.append(line7)
        self.lines.append(line8)
        self.lines.append(line9)
        self.lines.append(line10)
        self.lines.append(line11)
        self.lines.append(line12)
        self.lines.append(line13)
        self.lines.append(line14)
        
    def setLine(self, n, line):
        self.lines[n-1] = line
        
    def printSonnet(self):
        for line in self.lines:
            print(line)
    
    def compareTo(self, second_sonnet):
        for line in self.lines:
            ind = self.lines.index(line)
            other_line = second_sonnet.lines[ind]
            if line != other_line:
                return False
        return True
        
    pass


# In[3]:


#This is where I put in the content for all the sonnets.

sonnet1 = Sonnet("King Carlos turns his coat for better fees",
           "and sleeves are wrapped round horns of buffalo",
           "that tinned hornedbeef we stored smells more like cheese",
           "so stink the rotting skins from long ago",
           "I stille can call to mind those hours of ease",
           "the gauchos waving flags bravissimo",
           "we chill like nudists put on ice to freeze",
           "to pass the time we stage a little show",
           "From Salta to the Pole is quite a trot",
           "you mix with that you'll find you've had your lot",
           "if you drink mate you're an Argentine",
           "Those Latin states spin like a weathercock",
           "the Spanish language tickles the ear baroque",
           "unless the bell is quiet and charltintin"
                )

sonnet2 = Sonnet("The Parthenon horse looks nervous on the frieze",
           "since Elgin seems to think the nose de trop",
           "the Turk you see was deeply mired in sleaze",
           "the re in all his songs came out as doh",
           "The Parthenon horse is shivering in the biz",
           "benumbing London's dandies as they beau",
           "the flanks protected by chevaux de frise",
           "when March's hailstones batter the batteau",
           "Plato's Hellas surely wasn't sot",
           "with wits enough to fill a witenagemot",
           "as Socrates dies looking just Silene",
           "Its famous sculptures founder on a rock",
           "one carts off debris marble from the block",
           "if Europe or its destiny is keen"
                )

sonnet3 = Sonnet("The Breton tar lights up his duty-frees",
           "and sniffs the smoke that sets his nose aglow",
           "the chosen fruit is hued a bright cerise",
           "all during Lent one fruit's the ratio",
           "Remember friends those isles where live your Friese",
           "where shoals of herring boats now lie below",
           "that heap of goods occasions some unease",
           "when from afar we see the bushes grow",
           "We dry the fish sea bream or some burbot",
           "the shark is smoked on beds of bergamot",
           "while coming home we find the wind turned mean",
           "All's sold the prawns the lobsters our whole stock",
           "say sorry that no whales came back to dock",
           "so we are cousins now to king baleen"
                )

sonnet4 = Sonnet("At five o'clock he rests in his marquise",
           "consuming tea and nibbling cream gateaux",
           "the native driver's waiting in the breeze",
           "across the hillocks comes a steady blow",
           "So plain a plain's not what one often sees",
           "as castles blaze and palaces burn low",
           "a daring baron pockets th' abkaris",
           "the fireman makes his mighty hoses flow",
           "Milord has lisped from Malibar to Swat",
           "at Chandrigar the peasant sniffs the pot",
           "shame gives the colonel's brow a greasy sheen",
           "Such ancestry is merely poppycock",
           "the Indies have enough without that schlock",
           "the shield of vair or or's but briefly seen"
                )

sonnet5 = Sonnet("The gorgeous youth helps Hestia's heart unfreeze",
           "he's cast out like a snobby Romeo",
           "he wore his toga like an old chemise",
           "you pluck narcissi or you're very slow",
           "Those snaps of Pisa's tower are bound to please",
           "where Galileo once took pots to throw",
           "a Tuscan scribed the stone with his imprese",
           "the Greeks and Romans read and thought",
           "A witty wind stops Ities speaking rot",
           "in Florence tourists see a deal of grot",
           "you can't quote Virgil in a limousine",
           "Those transalpine relations interlock?",
           "the bankers in Provence exchange baiock?",
           "both Beaune and Chianti flow from Hippocrene?"
                )

sonnet6 = Sonnet("He's well inclined to capture his valise",
           "enough to spur on any picaro",
           "he'd much to learn despite his four degrees",
           "there's naught as dry as sacks of haricot",
           "He hates he hates the work of sequestrees",
           "so keen to part poor bumpkins from their dough",
           "going up to visit town is quite a wheeze",
           "it frightens Berry and the Morvandiaux",
           "Faced with mud you'll turn up your culotte",
           "we'll smack the dibbing kiddie's little bot",
           "manure not slush besmirched his gabardine",
           "You'll come to miss the peasant in his smock",
           "you start to travel looking like a brock",
           "at least the metro's one place where you've been"
                )

sonnet7 = Sonnet("When each of you with all his heart agrees",
           "being twinned is better far than single-o",
           "it's finding out that's likely to displease",
           "we always hope to keep ourselves so-so",
           "And thus it was a sib steeped in sottise",
           "who beggared gave his rags the old heave-ho",
           "e'en low bro's lead to diaporeses",
           "when parents sanctify the babygro",
           "The genealogist finds every blot",
           "to cease from scratching parchment he cannot",
           "he'd really like to root out the cuckquean",
           "Oh brother even when you groan I grok",
           "I quite forgive you when you run amok",
           "true twinship blames whatever's in the gene"
                )

sonnet8 = Sonnet("So now the bard spurns iambs and trochees",
           "to aggravate the layman and the shmo",
           "he writes reviews that read like journalese",
           "which freshens up the tribal rumbelow",
           "Just one was right and not those SOBs",
           "the mob demands that verse be comme il faut",
           "both are right not that vague congeries",
           "most people like to read the words they know",
           "Th' inspiréd poet isn't polyglot",
           "in his brain one tongue is all he's got",
           "e'en stol'n from th' celts his muse remains his queen",
           "O bard your solo readings make me mock",
           "I nominate you as a gapingstock",
           "the metromaniacs outdo Racine"
                )

sonnet9 = Sonnet("The conjuror eats watches pens or keys",
           "any diner chooses escargots",
           "eat fire your mouth will taste like antifreeze",
           "who knows if sharks will feast on bummalo",
           "The Papuan sucks his friend's apophyses",
           "those greedy mice leave nothing for the crow",
           "mixing broom with chives shows expertise",
           "but offering kids a sweetie that's no-no",
           "The wolf adores the cock and the cocotte",
           "a cat will munch a bird but spurn shallot",
           "the local road laps up leaked gasoline",
           "We've all downed plonk from Calais to Bangkok",
           "at meetings nibble nuts and watch the clock",
           "but best is grilled black pudding with sardine"
                )

sonnet10 = Sonnet("One's left with only sorrow and disease",
           "the undertakers peer and say Oho",
           "the timid mutter into their goatees",
           "you hear your spouse pay off the medico",
           "You get like dirty goods on busy quays",
           "your mind turns more and more to gloom and woe",
           "for death casts piles of shit on pedigrees",
           "with moth and rust we settle all we owe",
           "The brave man cries I do not care a jot",
           "the coward mutters Why was I begot?",
           "the masons give your tomb a final clean",
           "Oh reader thinking thus your heart will lock",
           "you cannot number off each ploch and pock",
           "clear from the start the ending is foreseen"
                 )

#This is assembling the sonnets

sonnets = [sonnet1,
          sonnet2,
          sonnet3,
          sonnet4,
          sonnet5,
          sonnet6,
          sonnet7,
          sonnet8,
          sonnet9,
          sonnet10,
          ]


# In[4]:


#This is a function which creates a random sonnet from the sonnets that exist

def randomSonnet():
    lines = []
    #Loop through adding one line at a time
    for i in range(14):
        #Select a random sonnet
        sonnet_num = random.randint(0,9)
        working_sonnet = sonnets[sonnet_num]
        #Add the next line to the sonnet from the corresponding line in the randomly chosen sonnet
        lines.append(working_sonnet.lines[i])
    sonnet = Sonnet(lines[0],
                   lines[1],
                   lines[2],
                   lines[3],
                   lines[4],
                   lines[5],
                   lines[6],
                   lines[7],
                   lines[8],
                   lines[9],
                   lines[10],
                   lines[11],
                   lines[12],
                   lines[13]
                   )
    return sonnet


# In[5]:


#Assigns a randomly created sonnet to a variable
#To generate a new sonnet in the next cell, re-run this cell and then the next one

final_sonnet = randomSonnet()


# In[6]:


#re-running this cell will not change your sonnet unless you re-run the one before

final_sonnet.printSonnet()


# In[7]:


#This function will create a list of random sonnets

def mulSonnets(n):
    sonnets = []
    #loop n times
    for i in range(0,n):
        new_sonnet = randomSonnet()
        sonnets.append(new_sonnet)
    return sonnets

#This function will print the list of sonnets you pass to it

def printMulSon(sonnet_list):
    for sonnet in sonnet_list:
        sonnet.printSonnet()
        print()


# In[8]:


#print 1000 randomly created sonnets
list_of_sonnets = mulSonnets(1000)

printMulSon(list_of_sonnets)


# In[9]:


#Check if the first sonnet is ever repeated

def checkForRepeats(list_of_sonnets):
    count = 0
    for sonnet in list_of_sonnets:
        ind = list_of_sonnets.index(sonnet)
        for comp_sonnet in list_of_sonnets[ind+1:]:
            second_ind = list_of_sonnets[ind+1:].index(comp_sonnet) + ind
            if(sonnet.compareTo(comp_sonnet)):
                print("Found a repeated sonnet.")
                print("Sonnet numbers " + str(ind+1) + " and " + str(second_ind+2) + " are the same")
                return True
            count += 1
            if(count%50000==0):
                print(str(count) + " sonnets checked so far")
    print(str(count) + " tests run. No repeats found.")
    return False

#Note, this takes a lot longer for larger numbers. It will take 100x as long to do 10000 poems as 1000
checkForRepeats(list_of_sonnets)


# In[ ]:





# In[ ]:





# In[ ]:




