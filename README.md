# Dota2-Pick-Helper
Calculates and lists the best and the worst heroes you could pick in a given draft, along with the reasons why.

This console application uses information on the counter pages at the Dota 2 Fandom Wiki to rank heroes based on the ally and enemy team. It also tells you why a hero is good or bad to pick. You can use this information to make the best of your hero's strengths in a given draft.

# How to Use
 1. Run scraper.py. You only need to run it once, before using the pick helper for the first time. It will scrape the counter information from each hero's page from the website (for example https://dota2.fandom.com/wiki/Alchemist/Counters).
  
    As of July 2021 the hero list is up to date with the last hero added being Dawnbreaker.

 2. Run pickHelper.py. You can enter as many heroes as you want. You need to enter the hero's full name but it is case-insensitive so no need to capitalize.
