# Dota2-Pick-Helper
Calculates and lists the best and the worst heroes you could pick in a given draft, along with the reasons why.

This console application uses information on the counter pages at the Dota 2 Fandom Wiki to rank heroes based on the ally and enemy team. It also tells you why a hero is good or bad to pick. You can use this information to make the best of your hero's strengths in a given draft.

# How to Use
 1. Run scraper.py. You only need to run it once, before using the pick helper for the first time. It will scrape the counter information from each hero's page from the website (for example https://dota2.fandom.com/wiki/Alchemist/Counters).
  
    As of July 2021 the hero list is up to date with the last hero added being Dawnbreaker.

 2. Run pickHelper.py. You can enter as many heroes as you want. You need to enter the hero's full name but it is case-insensitive so no need to capitalize.

# Example
![image](https://user-images.githubusercontent.com/75650001/124483321-defd6e00-ddb2-11eb-9245-8a7855f9844c.png)

Entering some enemy and ally heroes.


![image](https://user-images.githubusercontent.com/75650001/124483437-02281d80-ddb3-11eb-87e7-ed30a1ddadb4.png)

Pressing c shows the results. Ranking of heroes can be seen.

![image](https://user-images.githubusercontent.com/75650001/124483612-34d21600-ddb3-11eb-808a-656842099985.png)

Bad picks are listed with the reasons and the hero interactions.

![image](https://user-images.githubusercontent.com/75650001/124483888-7f539280-ddb3-11eb-804c-efa2bedea52d.png)

Pick suggestions.

# Accuracy

The accuracy of the suggestions are highly related to the information on the Dota 2 Wiki pages that were entered by the community but also the weights we give to the different interactions. As it is, this application places high value to the enemy team not having heroes that work well together, to avoiding ally heroes getting countered and to having heroes that work well together on the ally team. You can tweak the following numbers in the code if you for example care more about countering the enemy picks:

_for enemy_
 
            check what's good against them-> good pick +5
            check what works well with them-> (less) good pick  +2  
            check who is bad against them-> bad pick  -7  

 _for ally_
 
            check what works well with them-> good pick +5
            check what's good against them->  good pick +3
            check who is bad against them-> slightly bad pick -1
            
At any rate take the pick suggestions with a grain of salt. The main advantage of an application like this is that you can see why a particular suggestion is being made. The application combines the relevant information from the website and presents it in a richer and more customized way than if you were to look at a single hero counter page.
