# dashlib
A Python library that makes sending requests to the Geometry Dash servers and reading the responses easier. Special thanks to WylieMaster and everybody else contributed to [the GDDocs](https://wyliemaster.github.io/gddocs/#/) as it was the only source of information for the endpoints.  
[Library Documentation](README.md#how-to-use)

## Implemented features
 - [x] Level downloading.\
 - [x] Level uploading. \
 - [x] Level searching. \
 - [x] `GDLevel` class (because the kind of level objects the server returns are unreadable)
 - [x] User info fetching (using account ID).\
 - [x] User class `GDUser`

## Features to implement
 - [ ] Liking/disliking\
 - [ ] User searching\
 - [ ] Getting users by Player ID\
 - [ ] Leaderboard fetching\
 - [ ] Level Leaderboard fetching\
 - [ ] Commenting\
 - [ ] Posting\
 - [ ] User comment history fetching\
 - [ ] Icon image generation\
 - [ ] Icon kit class

## How to use
 ### Installing
  Use the following command to install this library-
  ```bash
  python -m pip install dashlib
  ```
 ### Level Downloading
  Use the `downloadLevel()` function to download levels. Example code-
  ```python
  from dashlib import *
  retray=downloadLevel(6508283) #1.5 seconds
  print(retray.levelName) #ReTraY
  print(retray.levelID) #6508283
  print(retray.password) #1532211
  print(retray.stars) #2
  ```
  Alternatively, use `fetchLevel()` or `fetchLevels` as these are faster, but the level string (the data for the level),password,upload and update date, and the low detail mode status is not available.
  ```python
  from dashlib import *
  retray=fetchLevel(6508283) #0.5 seconds
  some_levels=fetchLevels([128,6508283,4454123]) #still 0.5s as this is in a single request.
  print(retray.levelName) #ReTraY
  print(some_levels[0].levelName,some_levels[1].levelName,some_levels[2].levelName) #1st level, ReTraY, Sonar
  ```
  ### Level Searching
   Use the `searchForLevels()` function to search for levels. Example code-
   ```python
   res=searchForLevels(type=TYPE_SEARCH,page=0,query="bloodbath",difficultyFilter=FILTER_DEMON,demonFilter=DEMONFILTER_EXTREME)
   print(res[0].levelName) #Bloodbath
   print(res[0].levelID) #res[0].levelID
   ```
   

   #### Parameters
   \
    `type`:    Use TYPE_SEARCH,TYPE_MOSTDOWNLOAD,TYPE_MOSTLIKE,etc constants to set the type of the search,\
    `page`:    The page number.\
    `query`:   For TYPE_SEARCH, this is the search query,\
            For TYPE_USERSLEVELS, this is the user ID of the user's levels to search,\
            For TYPE_LISTOFID, this is a comma seperated list of level IDs\
    `difficultyFilter`:   Use FILTER_NA and FILTER_EASY to FILTER_DEMON or None(default) to filter the difficulty\
    `demonFilter`:     If difficultyFilter is FILTER_DEMON, then use DEMONFILTER_EASY,DEMONFILTER_MEDIUM,...,DEMONFILTER_EXTREME to filter which kind of demon to search, or use None(default).\
    `length`:    Use LENGTH_TINY to LENGTH_XL and LENGTH_PLAT to filter by level length, or use None (default).\
    `uncompleted`,`completed`,`featured`,`original`,`twoPlayer`,`coins`,`epic`,`legendary`,`mythic`,`noStar`,`star`:\
        If any of these are True, filters by levels that have the respective property. If False, does not apply that filter.\
        (so if `completed`=False it will show **BOTH** the levels that are completed and those that are not.)\
    `completedLevelIDs`:     If using uncompleted or completed=True, this list specifies which level IDs are completed. Otherwise, it does not matter.\
    `followedUsers`:   If type=TYPE_FOLLOWED, this is a list of user IDs that are followed.\
  ### User info fetching
   You can get user info using the `getUserInfo()` function. Example-\
   ```python
   from dashlib import *
   user=getUserInfo(14134) #AeonAir's account ID.
   print(user.username) #AeonAir
   print(user.diamonds) #45396 (however many diamonds he has)
   print(user.secretCoins) #164
   print(user.stars) #40840
   print(user.moons) #456
   ```
## Credits and resources
 Special thanks to the people who maintain and have contributed to [the GDDocs](https://wyliemaster.github.io/gddocs/#/). This was pretty much the only source of information.\
 Also thanks to Colon for making [GDBrowser](https://gdbrowser.com/). I did not want to open geometry dash every time I wanted to check something. (and it also would have lagged my potato laptop)
