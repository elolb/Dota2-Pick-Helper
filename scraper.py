#! python3
# scraper.py
# Scrapes the counter lists from gamepedia. Collects the necessary data for the pick helper.

# Data
heroList=["Abaddon","Alchemist","Ancient Apparition","Anti-Mage","Arc Warden","Axe","Bane","Batrider","Beastmaster","Bloodseeker","Bounty Hunter",\
          "Brewmaster","Bristleback","Broodmother","Centaur Warrunner","Chaos Knight","Chen","Clinkz","Clockwerk","Crystal Maiden","Dark Seer","Dark Willow",\
          "Dawnbreaker","Dazzle","Death Prophet","Disruptor","Doom","Dragon Knight","Drow Ranger","Earth Spirit","Earthshaker","Elder Titan","Ember Spirit","Enchantress",\
          "Enigma","Faceless Void","Grimstroke","Gyrocopter","Hoodwink","Huskar","Invoker","Io","Jakiro","Juggernaut","Keeper of the Light","Kunkka","Legion Commander","Leshrac",\
          "Lich","Lifestealer","Lina","Lion","Lone Druid","Luna","Lycan","Mars","Magnus","Medusa","Meepo","Mirana","Monkey King","Morphling","Naga Siren",\
          "Nature\'s Prophet","Necrophos","Night Stalker","Nyx Assassin","Ogre Magi","Omniknight","Oracle","Outworld Devourer","Pangolier","Phantom Assassin",\
          "Phantom Lancer","Phoenix","Puck","Pudge","Pugna","Queen of Pain","Razor","Riki","Rubick","Sand King","Shadow Demon","Shadow Fiend","Shadow Shaman",\
          "Silencer","Skywrath Mage","Slardar","Slark","Snapfire","Sniper","Spectre","Spirit Breaker","Storm Spirit","Sven","Techies","Templar Assassin","Terrorblade",\
          "Tidehunter","Timbersaw","Tinker","Tiny","Treant Protector","Troll Warlord","Tusk","Underlord","Undying","Ursa","Vengeful Spirit","Venomancer",\
          "Viper","Visage","Void Spirit","Warlock","Weaver","Windranger","Winter Wyvern","Witch Doctor","Wraith King","Zeus"]
counterLinkPre='https://dota2.gamepedia.com/'
counterLinkPost='/Counters'


# Scraping

import requests,bs4,pickle

file=open('List.txt', "w")
count=0

badAgainstDict={}
badAgainstOthersDict={}
goodAgainstDict={}
goodAgainstOthersDict={}
worksWellDict={}
worksWellOthersDict={}

   
for hero in heroList:
    site=requests.get(counterLinkPre+hero+counterLinkPost)
    site.raise_for_status()
    soup=bs4.BeautifulSoup(site.text,'html.parser')
#print(soup.find('span',id="Bad_against..."))

#select bold (only hero names are in bold on the website)
    counters=soup.select('b')
#for each hero create 6 lists
    badAgainst={}
    badAgainstOthers={}
    goodAgainst={}
    goodAgainstOthers={}
    worksWell={}
    worksWellOthers={}

# for x in some_list: sets x to each element of some_list, not each index. 
# for each hero name
    for i in counters:
        if (i.findNext('h2').getText()=='Good against...[edit]' ):
            # if(i.findNext('h3'.find('span')['id']=='Others'):
            detail=i.findNext('ul').getText()
            badAgainst[i.getText()]=detail
#print(badAgainst)

    for i in counters:
        if (i.findNext('h2').getText()=='Works well with...[edit]' ):
            detail=i.findNext('ul').getText()
            goodAgainst[i.getText()]=detail
#print(goodAgainst)

    for i in counters:
        if (i.findNext('h2').getText()=='Navigation menu' ):
            detail=i.findNext('ul').getText()
            worksWell[i.getText()]=detail
#print(worksWellW)
   # if len(badAgainst
    badAgainstDict[hero]=badAgainst
    goodAgainstDict[hero]=goodAgainst
    worksWellDict[hero]=worksWell

    
    print(hero+" list extracted from "+ counterLinkPre+hero+counterLinkPost+"...")
    count=count+1
#with open(file, "w", encoding="utf-8") as f:
 #   f.write(str(badAgainstDict))
  #  f.write(str(goodAgainstDict))
   # f.write(str(worksWellDict))
#file.write(str(badAgainstDict))
#file.write(str(goodAgainstDict))
#file.write(str(worksWellDict))
file=open("badAgainstDict.pkl","wb")
pickle.dump(badAgainstDict, file, pickle.HIGHEST_PROTOCOL)
file.close()
file2=open("goodAgainstDict.pkl","wb")
pickle.dump(goodAgainstDict, file2, pickle.HIGHEST_PROTOCOL)
file2.close()
file3=open("worksWellDict.pkl","wb")
pickle.dump(worksWellDict, file3, pickle.HIGHEST_PROTOCOL)
file3.close()
file=open("badAgainst.pkl","wb")
pickle.dump(badAgainst, file, pickle.HIGHEST_PROTOCOL)
file.close()
file2=open("goodAgainst.pkl","wb")
pickle.dump(goodAgainst, file2, pickle.HIGHEST_PROTOCOL)
file2.close()
file3=open("worksWell.pkl","wb")
pickle.dump(worksWell, file3, pickle.HIGHEST_PROTOCOL)
file3.close()
print("DONE. "+str(count)+" heroes counters are extracted.")    
