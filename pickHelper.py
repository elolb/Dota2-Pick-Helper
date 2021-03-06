#! python3
# pickHelper.py
# Calculates and lists the best and the worst heroes you could pick in a given draft, along with the reasons why


import pickle,string
# import the data
file=open("badAgainstDict.pkl","rb")
badAgainstDict=pickle.load(file)
file=open("goodAgainstDict.pkl","rb")
goodAgainstDict=pickle.load(file)
file=open("worksWellDict.pkl","rb")
worksWellDict=pickle.load(file)
file.close()

enemyList=set()
allyList=set()

pick={}
badPick=[]
goodPick=[]
# Get draft heroes as list from user
hero=string.capwords(input("Enter heroes. Press 'e' first if entering enemy (press c to end entering heroes and calculate hero ranks)(press q to quit program)\n"))
while 1:
        if hero in badAgainstDict:
            allyList.add(hero)
            print(hero+" is an ally.")
        elif hero=="Anti Mage":
            hero="Anti-Mage"
            allyList.add(hero) # the hyphen in 'anti-mage' is problematic, use hard coding for now
            print(hero+" is an ally.")
        elif hero=="E":
            hero=string.capwords(input())
            if hero in badAgainstDict:
                enemyList.add(hero)
                print(hero+" is an enemy.")
            elif hero=="Anti Mage": # the hyphen in 'anti-mage' is problematic, use hard coding for now
                hero="Anti-Mage"
                allyList.add(hero)
                print(hero+" is an ally.")
        elif hero=="C":

            # for enemy
            #check what's good against them-> good pick +5
            #check what works well with them-> (less) good pick  +2
            #check who is bad against them-> bad pick  -7
            goodSummary={}
            badSummary={}
            reasonPre="\n\n- " # for each summary line, use new lines and hyphen
            detailPre="\n"
            for enemy in enemyList:
                   for hero in badAgainstDict[enemy]:
                        if hero in pick:
                            pick[hero]+=5
                        else:
                            pick[hero]=5
                        
                        if hero in goodSummary:
                            goodSummary[hero]+=reasonPre+hero+" is good against "+enemy
                        else:
                            goodSummary[hero]=reasonPre+hero+" is good against "+enemy
                        goodSummary[hero]+=detailPre+badAgainstDict[enemy][hero]
                        
            #           print("made "+hero+" increase bcs "+enemy+" is bad against it")
                        
            #      print(enemy+" is good against "+hero)
                   for hero in worksWellDict[enemy]:
                        if hero in pick:
                            pick[hero]+=2
                         
                        else:
                            pick[hero]=2
                        if hero in goodSummary:
                            goodSummary[hero]+=reasonPre+hero+" would be good with their "+enemy+" if they picked it"
                        else:
                            goodSummary[hero]=reasonPre+hero+" would be good with their "+enemy+" if they picked it"
             #          print("made "+hero+" increase bcs its good with "+enemy)
                        goodSummary[hero]+=detailPre+worksWellDict[enemy][hero]
                   for hero in goodAgainstDict[enemy]:
                        if hero in pick:
                            pick[hero]-=7
                        else:
                            pick[hero]=-7
                        if hero in badSummary:
                            badSummary[hero]+=reasonPre+hero+" is bad against "+enemy
                        else:
                            badSummary[hero]=reasonPre+hero+" is bad against "+enemy
            #           print("made "+hero+" decrease bcs "+enemy+" is good against it")
                        badSummary[hero]+=detailPre+goodAgainstDict[enemy][hero]
            # for ally
            #check what works well with them-> good pick +5
            #check what's good against them-> good pick +3
            #check who is bad against them-> slightly bad pick -1

            for ally in allyList:
                   for hero in badAgainstDict[ally]:
                        if hero in pick:
                            pick[hero]+=3
                        else:
                            pick[hero]=3
                        if hero in goodSummary:
                            goodSummary[hero]+=reasonPre+"If enemy picked "+hero+" against "+ally+" it could be bad"
                        else:
                            goodSummary[hero]=reasonPre+"If enemy picked "+hero+" against "+ally+" it could be bad"
            #           print("made "+hero+" increase bcs it is good against "+ally)
                        goodSummary[hero]+=detailPre+badAgainstDict[ally][hero]
                   for hero in worksWellDict[ally]:
                        if hero in pick:
                            pick[hero]+=5
                        else:
                            pick[hero]=5
                        if hero in goodSummary:
                            goodSummary[hero]+=reasonPre+hero+" is good with "+ally
                        else:
                            goodSummary[hero]=reasonPre+hero+" is good with "+ally
            #           print("made "+hero+" increase bcs it is good with "+ally)
                        goodSummary[hero]+=detailPre+worksWellDict[ally][hero]
                   for hero in goodAgainstDict[ally]:
                        if hero in pick:
                            pick[hero]-=1
                        else:
                            pick[hero]=-1
                        if hero in badSummary:
                            badSummary[hero]+=reasonPre+"Better if enemy picks it since "+ally+" is good against it"
                        else:
                            badSummary[hero]=reasonPre+"Better if enemy picks it since "+ally+" is good against it"
                       
                        badSummary[hero]+=detailPre+goodAgainstDict[ally][hero]
            #           print("made "+hero+" decrease bcs " +ally+ " is good against it, so it's better if enemy picks it")   
            ascendingPick={k: v for k, v in sorted(pick.items(), key=lambda item: item[1])}
            print(ascendingPick)
            print("\n")
            for key in ascendingPick:
                if ascendingPick[key]<0:
                    badPick.append(key)
                elif ascendingPick[key]>0:
                    goodPick.append(key)
            goodPick.reverse()
            print("\n\n//// DON\'T PICK THESE ////\n")
            
# show only top 3 for bad pick, top 7 for good pick
            for pick in badPick[0:3]:
                print("\t"+pick)
                print("\n"+badSummary[pick]+"\n\n")
                
            print("\n\n//// PICK THESE ////\n")
            for pick in goodPick[0:7]:
                print("\t"+pick)
                print("\n"+goodSummary[pick]+"\n\n")

# reset for new draft
            enemyList=set()
            allyList=set()

            pick={}
            badPick=[]
            goodPick=[]
        elif hero=="Q":
            break
        else:
            print("???")
        hero=string.capwords(input("\nEnter heroes. (e:enemy, c:calculate, q:quit)\n"))
        
        
