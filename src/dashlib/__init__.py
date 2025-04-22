import requests
import base64
import hashlib  # sha1() lives there
from typing import Literal
#credits to everybody who made and maintained this GD Documentation- https://wyliemaster.github.io/gddocs/
#id of retray is 6508283
#id of 1st level is 128
#=======CONSTANTS=======
#Level Difficulties

DIFFICULTY_NA=0
DIFFICULTY_EASY=1
DIFFICULTY_NORMAL=2
DIFFICULTY_HARD=3
DIFFICULTY_HARDER=4
DIFFICULTY_INSANE=5
DIFFICULTY_EASYDEMON=6
DIFFICULTY_MEDIUMDEMON=7
DIFFICULTY_HARDDEMON=8
DIFFICULTY_INSANEDEMON=9
DIFFICULTY_EXTREMEDEMON=10
DIFFICULTY_AUTO=11
#Level lengths
LENGTH_TINY=0
LENGTH_SHORT=1
LENGTH_MEDIUM=2
LENGTH_LONG=3
LENGTH_XL=4
LENGTH_PLAT=5
#Search Types
TYPE_SEARCH=0
TYPE_MOSTDOWNLOAD=1
TYPE_MOSTLIKE=2
TYPE_TRENDING=3
TYPE_RECENT=4
TYPE_USERSLEVELS=5
"""Search for a specific user's levels"""
TYPE_FEATURED=6
TYPE_MAGIC=7
TYPE_SENT=8
TYPE_LEVELLIST=25
"""This is for ingame 2.2 level lists.Not to be confused with TYPE_LISTOFLVL, which is for passing in a list of IDs and getting the search results for them."""
TYPE_LISTOFID=26
"""This is for lists of IDs. Not to be confused with TYPE_LISTOFLVL, which is for in-game 2.2 level lists"""
TYPE_AWARDED=11
TYPE_FOLLOWED=12
"""You will have to pass in `followedUsers`"""
TYPE_MODELIKEGDWORLD=15
TYPE_HALLOFFAME=16
TYPE_DAILIES=21
TYPE_WEEKLIES=22
TYPE_LIST=25
#Search Difficulty Filters
FILTER_NA=-1
FILTER_DEMON=-2
FILTER_EASY=1
FILTER_NORMAL=2
FILTER_HARD=3
FILTER_HARDER=4
FILTER_INSANE=5
#Search Demon Filters
DEMONFILTER_EASY=1
DEMONFILTER_MEDIUM=2
DEMONFILTER_HARD=3
DEMONFILTER_INSANE=4
DEMONFILTER_EXTREME=5

#========CLASSES========
class GDLevel:
    """A class used to represent a geometry dash level.
    
    Attributes-
        levelID     The id of the level
        levelName	The name of the level
        description	The level description.

        levelString	All the data for the level
        version	The version of the level published
        playerID	The player ID of the level author
        difficultyDenominator	Returns 0 if the level is N/A, returns 10 if a difficulty is assigned. Use `isNA` insted.
        difficultyNumerator     The nominator used for calculating the level difficulty. Divided by the denominator to get the difficulty icon. Nowadays just 0 = unrated, 10 = easy, 20 = normal, 30 = hard, 40 = harder, 50 = insane. Can be also used to determine the demon difficulty as a side-effect of the voting system. Use `difficulty` instead.
        downloads	The amount of times the level has been downloaded
        officialSong	The official song number used by the level, if applicable.
        gameVersionOrg	The original indicator for the GD version the level was uploaded in. Versions 1.0 to 1.6 use version numbers 1 to 7 respectively. Version 10 is 1.7. Otherwise, divide the version number by ten to get the correct number. Use gameVersion instead.
        gameVersion     The version number times 10.
        likes	likes - dislikes
        length	A number from 0-4, where 0 is tiny and 4 is XL and 5 is platformer. Use the variables LENGTH_TINY LENGTH_XL and LENGTH_PLAT to know which int is which.
        dislikes	dislikes - likes
        isDemon	If the level's difficulty is demon
        stars	The amount of stars rewarded for completing the level
        featureScore	0 if the level is not featured, otherwise a positive number. The higher it is, the higher the level appears on the featured levels list.
        isAuto	If the level's difficulty is auto
        recordString	appears in the GJGameLevel parser but is unused

        password	The password required to copy the level.
        uploadDate	The approximate date the level was uploaded on
        updateDate	The approximate date the level was last updated on
        copiedID	The ID the of the original level (if the level was copied)
        twoPlayer	Whether the level uses two player mode
        customSongID	The ID of the custom Newgrounds song used in the level
        extraString	The extraString passed when uploading the level. Its use is currently unknown
        coins	The number of user coins placed in the level
        verifiedCoins	If the level's user coins are verified (silver)
        starsRequested	The star value requested for the level
        lowDetailMode	If the level has a low detail checkbox
        dailyNumber	Daily/weekly levels only. Returns which daily/weekly the level was (e.g. the 500th daily level). Subtract 100,000 if the level is weekly
        epic	The epic rating for the level. 0 = none, 1 = epic, 2 = legendary, 3 = mythic.
        demon Difficulty	The difficulty of the demon rating. 3 = easy, 4 = medium, 0 = hard, 5 = insane, 6 = extreme. Can also be used to determine the level difficulty non-demons had before rating as a side-effect of the voting system.
        isGauntlet	if the level is in a gauntlet
        objects	The amount of objects in the level, used to determine if the level is considered "large". It caps at 65535
        editorTime	the total number of seconds spend on the current copy of a level
        editorTimeCopies	The accumulative total of seconds spend on previous copies of the level
        sfxIDs	The list of all SFX IDs in the level
        songIDs	The list of all song IDs in the level
        verificationFrames	How long the level took to verify (in frames, assume 240 FPS)
        """
    
    levelID:int #key 1 in a level object, https://wyliemaster.github.io/gddocs/#/resources/server/level
    """The id of the level"""
    levelName:str #2
    """The name of the level"""
    description:str #3 make sure to b64 decode
    """The level description"""
    levelString:str #4 I will not implement any way to level strings yet
    """All the data for the level in the game's default format."""
    version:int|None #5
    """The version of the level published"""
    playerID:int #6
    """The player ID of the level author"""
    #7 doesnt exist
    difficultyDenominator: int #8
    """Returns 0 if the level is N/A, returns 10 if a difficulty is assigned. Use `isNA` instead."""
    difficultyNumerator: int #9
    """The nominator used for calculating the level difficulty. Divided by the denominator to get the difficulty icon. Nowadays just 0 = unrated, 10 = easy, 20 = normal, 30 = hard, 40 = harder, 50 = insane. Can be also used to determine the demon difficulty as a side-effect of the voting system. Use `difficulty` instead."""
    difficulty:int #implement it
    """The difficulty of the level. Use the constants DIFFICULTY_EASY to DIFFICULTY_EASYDEMON for reference. 0 is NA 1 is easy 2 is normal... 6 is easy demon... 10 is extreme demon 11 is auto."""
    downloads:int #10
    """The amount of times the level has been downloaded"""
    #11 is setCompletes, removed in 2.1
    officialSong:int|None #12
    """The official song number used by the level, if applicable"""
    gameVersionOrg:int #13
    """NOTE: Use `gameVersion` instead.The GD version the level was uploaded in in the original format. Versions 1.0 to 1.6 use version numbers 1 to 7 respectively. Version 10 is 1.7. Otherwise, divide the version number by ten to get the correct number."""
    gameVersion:int #13 with implementy stuff
    """The game version, multiplied by 10."""
    likes:int #14
    """	likes - dislikes"""
    length:int #15
    """A number from 0-4, where 0 is tiny and 4 is XL and 5 is platformer"""
    dislikes:int #16
    """	dislikes - likes"""
    isDemon:bool #17 converted
    """If the level's difficulty is demon"""
    stars:int #18
    """	The amount of stars rewarded for completing the level"""
    featureScore:int #19
    """	0 if the level is not featured, otherwise a positive number. The higher it is, the higher the level appears on the featured levels list."""
    isAuto:bool #25
    """	If the level's difficulty is auto"""
    password:int #27 but xor decrypt using key 26364
    """The password required to copy the level"""
    uploadDate:str #28
    """The approximate date the level was uploaded on"""
    updateDate: str #29
    """The approximate date the level was last updated on"""
    copiedId: int|None #30
    """The ID the of the original level (if the level was copied)"""
    twoPlayer:bool #31
    """	Whether the level uses two player mode"""
    customSongID:int|None #35
    """The ID of the custom Newgrounds song used in the level"""
    extraString:str|None #36
    """The extraString passed when uploading the level. Its use is currently unknown"""
    coins:int #37
    """The number of user coins placed in the level"""
    verifiedCoins:int #38
    """If the level's user coins are verified (silver)."""
    starsRequested:int #39
    """The star value requested for the level"""
    lowDetailMode:bool #40
    """The star value requested for the level"""
    dailyNumber:int #41
    """	If the level has a low detail checkbox"""
    epic:int #42
    """	Daily/weekly levels only. Returns which daily/weekly the level was (e.g. the 500th daily level). Subtract 100,000 if the level is weekly"""
    demonDifficulty:int#43
    """NOTE: Use `difficulty` instead. The difficulty of the demon rating. 3 = easy, 4 = medium, 0 = hard, 5 = insane, 6 = extreme. Can also be used to determine the level difficulty non-demons had before rating as a side-effect of the voting system."""
    isGauntlet:bool#44
    """If the level is in a gauntlet"""
    objects:int#45
    """The amount of objects in the level, used to determine if the level is considered "large". It caps at 65535"""
    editorTime:int#46
    """The total number of seconds spend on the current copy of a level"""
    editorTimeCopies:int#47
    """	The accumulative total of seconds spend on previous copies of the level"""
    songIDs:list[int]#52 split by comma
    """The list of all song IDs in the level"""
    sfxIDs:list[int]#53 split by comma
    """The list of all SFX IDs in the level"""
    verificationFrames:int #57
    """	How long the level took to verify (in frames, assume 240 FPS)"""
    isNA:bool#57
    """If the level shows a difficulty face of N/A"""

    

    
    def __init__(self,levelWithHashes:str):
        """Create a GDLevel object from a level in double-colon format with integrity hashes, as returned by the server endpoint `downloadGJLevel22`.
        This function does not actually use the integrity hashes yet."""
        level=levelWithHashes.split("#")[0] 
        dic:dict[str,str]=parseDoubleColonString(level)
        self.levelID:int =int_handled(dic.get('1','0')) 
        self.levelName:str=dic.get('2',"")
        try:
            self.description:str=base64.b64decode(dic.get('3',"").encode("ascii")).decode("ascii")
        except:
            self.description:str="Error getting description- Encoded "+dic.get('3',"")
        self.levelString:str=dic.get('4',None)
        self.version:int|None=dic.get('5',None)
        self.playerID:int=int_handled(dic.get('6','0'))
        difficultyDenominator=int_handled(dic.get('8','0'))
        self.difficultyDenominator: int =int_handled(dic.get('8','0'))
        difficultyNumerator=int_handled(dic.get('9','0'))
        self.difficultyNumerator: int =int_handled(dic.get('9','0'))
        self.downloads:int =int_handled(dic.get('10','0'))
        
        self.officialSong:int|None =int_handled(dic.get('8',0))
        self.gameVersionOrg:int =int_handled(dic.get('13',0))
        self.likes:int =int_handled(dic.get('14',0))
        self.length:int =int_handled(dic.get('15',0))
        self.dislikes:int =int_handled(dic.get('16',0))
        isDemonOrg=dic.get('17','')
        isDemon=False
        if isDemonOrg=='1':
            isDemon=True
        self.isDemon:bool=isDemon #17 converted
        self.stars:int=int_handled(dic.get('18',0)) #18
        self.featureScore:int=int_handled(dic.get('19',0)) #19
        isAutoOrg=dic.get('25','')
        isAuto=False
        if isAutoOrg=='1':
            isAuto=True
        self.isAuto:bool=isAuto #25
        self.password:int=int_handled(decode_level_password(dic.get('27',""))) #27 but xor decrypt using key 26364
        self.uploadDate:str=dic.get('28','') #28
        self.updateDate: str=dic.get('29','') #29
        self.copiedId: int=int_handled(dic.get('30','0')) #30
        twoPlayerOrg=dic.get('25','')
        twoPlayer=False
        if twoPlayerOrg=='1':
            twoPlayer=True
        self.twoPlayer:bool=twoPlayer #31
        self.customSongID:int|None=int_handled(dic.get('35','0')) #35
        self.extraString:str|None=dic.get('36','') #36
        self.coins:int=int_handled(dic.get('37','0')) #37
        self.verifiedCoins:int=int_handled(dic.get('38','0')) #38
        self.starsRequested:int=int_handled(dic.get('39','0')) #39
        islowDetailModeOrg=dic.get('40','')
        islowDetailMode=False
        if islowDetailModeOrg=='1':
            islowDetailMode=True
        self.lowDetailMode:bool=islowDetailMode #40
        self.dailyNumber:int=int_handled(dic.get('41','0')) #41
        self.epic:int =int_handled(dic.get('42','0'))#42
        self.demonDifficulty:int=int_handled(dic.get('43','0'))#43
        isGauntletOrg=dic.get('44','')
        isGauntlet=False
        if isGauntletOrg=='1':
            isGauntlet=True
        self.isGauntlet:bool=isGauntlet#44
        self.objects:int=int_handled(dic.get('45','0'))#45
        self.editorTime:int=int_handled(dic.get('46','0'))#46
        self.editorTimeCopies:int=int_handled(dic.get('47','0'))#47
        songIDsOrg=dic.get('52','').split(",")
        songIDs=[]
        for i in songIDsOrg:
            songIDs.append(int_handled(i))
        sfxIDsOrg=dic.get('53','').split(",")
        sfxIDs=[]
        for i in sfxIDsOrg:
            sfxIDs.append(int_handled(i))
        self.songIDs:list[int]=songIDs#52 split by comma
        self.sfxIDs:list[int]=sfxIDs#53 split by comma
        self.verificationFrames:int=int_handled(dic.get('57','0')) #57
        if self.isAuto:
            difficulty=DIFFICULTY_AUTO
        elif not isDemon:
            difficulty=int_handled(difficultyNumerator/10)
        else:
            if self.demonDifficulty==3:
                difficulty=DIFFICULTY_EASYDEMON
            if self.demonDifficulty==4:
                difficulty=DIFFICULTY_MEDIUMDEMON
            if self.demonDifficulty==0:
                difficulty=DIFFICULTY_HARDDEMON
            if self.demonDifficulty==5:
                difficulty=DIFFICULTY_INSANEDEMON
            if self.demonDifficulty==6:
                difficulty=DIFFICULTY_EXTREMEDEMON
        self.difficulty:int=difficulty
        gameVersion=0
        if self.gameVersionOrg==1:gameVersion=10
        if self.gameVersionOrg==2:gameVersion=11
        if self.gameVersionOrg==3:gameVersion=12
        if self.gameVersionOrg==4:gameVersion=13
        if self.gameVersionOrg==5:gameVersion=14
        if self.gameVersionOrg==6:gameVersion=15
        if self.gameVersionOrg==7:gameVersion=16
        if self.gameVersionOrg==10:gameVersion=17
        if self.gameVersionOrg>10:gameVersion=self.gameVersionOrg
        self.gameVersion:int=gameVersion
        if self.difficultyDenominator==10:
            self.isNA=False
        else:
            self.isNA=True
    def __str__(self):
        return f"<level {self.levelName} with ID {self.levelID}>"
class GDFetchedLevel(GDLevel):
    """A class used to represent a geometry dash level that was obtained from the search result. Obtaining levels from the search results (using `fetchLevel()`
    , `fetchLevels()` or `searchForLevels()`) is WAY faster than downloading them (you can even get multiple in a a single request), but `uploadDate`, `updateDate`,
    `lowDetailMode`, `password` and (especially) `levelString` are not available.
    
    Attributes (same as `GDLevel` but without some variables)-
        levelID     The id of the level
        levelName	The name of the level
        description	The level description.
        version	The version of the level published
        playerID	The player ID of the level author
        difficultyDenominator	Returns 0 if the level is N/A, returns 10 if a difficulty is assigned. Use `isNA` insted.
        difficultyNumerator     The nominator used for calculating the level difficulty. Divided by the denominator to get the difficulty icon. Nowadays just 0 = unrated, 10 = easy, 20 = normal, 30 = hard, 40 = harder, 50 = insane. Can be also used to determine the demon difficulty as a side-effect of the voting system. Use `difficulty` instead.
        downloads	The amount of times the level has been downloaded
        officialSong	The official song number used by the level, if applicable.
        gameVersionOrg	The original indicator for the GD version the level was uploaded in. Versions 1.0 to 1.6 use version numbers 1 to 7 respectively. Version 10 is 1.7. Otherwise, divide the version number by ten to get the correct number. Use gameVersion instead.
        gameVersion     The version number times 10.
        likes	likes - dislikes
        length	A number from 0-4, where 0 is tiny and 4 is XL and 5 is platformer. Use the variables LENGTH_TINY LENGTH_XL and LENGTH_PLAT to know which int is which.
        dislikes	dislikes - likes
        isDemon	If the level's difficulty is demon
        stars	The amount of stars rewarded for completing the level
        featureScore	0 if the level is not featured, otherwise a positive number. The higher it is, the higher the level appears on the featured levels list.
        isAuto	If the level's difficulty is auto
        recordString	appears in the GJGameLevel parser but is unused
        copiedID	The ID the of the original level (if the level was copied)
        twoPlayer	Whether the level uses two player mode
        customSongID	The ID of the custom Newgrounds song used in the level
        extraString	The extraString passed when uploading the level. Its use is currently unknown
        coins	The number of user coins placed in the level
        verifiedCoins	If the level's user coins are verified (silver)
        starsRequested	The star value requested for the level
        dailyNumber	Daily/weekly levels only. Returns which daily/weekly the level was (e.g. the 500th daily level). Subtract 100,000 if the level is weekly
        epic	The epic rating for the level. 0 = none, 1 = epic, 2 = legendary, 3 = mythic.
        demon Difficulty	The difficulty of the demon rating. 3 = easy, 4 = medium, 0 = hard, 5 = insane, 6 = extreme. Can also be used to determine the level difficulty non-demons had before rating as a side-effect of the voting system.
        isGauntlet	if the level is in a gauntlet
        objects	The amount of objects in the level, used to determine if the level is considered "large". It caps at 65535
        editorTime	the total number of seconds spend on the current copy of a level
        editorTimeCopies	The accumulative total of seconds spend on previous copies of the level
        sfxIDs	The list of all SFX IDs in the level
        songIDs	The list of all song IDs in the level
        verificationFrames	How long the level took to verify (in frames, assume 240 FPS)
        """
    levelID:int #key 1 in a level object, https://wyliemaster.github.io/gddocs/#/resources/server/level
    """The id of the level"""
    levelName:str #2
    """The name of the level"""
    description:str #3 make sure to b64 decode
    """The level description"""
    version:int|None #5
    """The version of the level published"""
    playerID:int #6
    """The player ID of the level author"""
    #7 doesnt exist
    difficultyDenominator: int #8
    """Returns 0 if the level is N/A, returns 10 if a difficulty is assigned. Use `isNA` instead."""
    difficultyNumerator: int #9
    """The nominator used for calculating the level difficulty. Divided by the denominator to get the difficulty icon. Nowadays just 0 = unrated, 10 = easy, 20 = normal, 30 = hard, 40 = harder, 50 = insane. Can be also used to determine the demon difficulty as a side-effect of the voting system. Use `difficulty` instead."""
    difficulty:int #implement it
    """The difficulty of the level. Use the constants DIFFICULTY_EASY to DIFFICULTY_EASYDEMON for reference. 0 is NA 1 is easy 2 is normal... 6 is easy demon... 10 is extreme demon 11 is auto."""
    downloads:int #10
    """The amount of times the level has been downloaded"""
    #11 is setCompletes, removed in 2.1
    officialSong:int|None #12
    """The official song number used by the level, if applicable"""
    gameVersionOrg:int #13
    """NOTE: Use `gameVersion` instead.The GD version the level was uploaded in in the original format. Versions 1.0 to 1.6 use version numbers 1 to 7 respectively. Version 10 is 1.7. Otherwise, divide the version number by ten to get the correct number."""
    gameVersion:int #13 with implementy stuff
    """The game version, multiplied by 10."""
    likes:int #14
    """	likes - dislikes"""
    length:int #15
    """A number from 0-4, where 0 is tiny and 4 is XL and 5 is platformer"""
    dislikes:int #16
    """	dislikes - likes"""
    isDemon:bool #17 converted
    """If the level's difficulty is demon"""
    stars:int #18
    """	The amount of stars rewarded for completing the level"""
    featureScore:int #19
    """	0 if the level is not featured, otherwise a positive number. The higher it is, the higher the level appears on the featured levels list."""
    isAuto:bool #25
    """	If the level's difficulty is auto"""
    copiedId: int|None #30
    """The ID the of the original level (if the level was copied)"""
    twoPlayer:bool #31
    """	Whether the level uses two player mode"""
    customSongID:int|None #35
    """The ID of the custom Newgrounds song used in the level"""
    extraString:str|None #36
    """The extraString passed when uploading the level. Its use is currently unknown"""
    coins:int #37
    """The number of user coins placed in the level"""
    verifiedCoins:int #38
    """If the level's user coins are verified (silver)."""
    starsRequested:int #39
    """The star value requested for the level"""
    dailyNumber:int #41
    """	If the level has a low detail checkbox"""
    epic:int #42
    """	Daily/weekly levels only. Returns which daily/weekly the level was (e.g. the 500th daily level). Subtract 100,000 if the level is weekly"""
    demonDifficulty:int#43
    """NOTE: Use `difficulty` instead. The difficulty of the demon rating. 3 = easy, 4 = medium, 0 = hard, 5 = insane, 6 = extreme. Can also be used to determine the level difficulty non-demons had before rating as a side-effect of the voting system."""
    isGauntlet:bool#44
    """If the level is in a gauntlet"""
    objects:int#45
    """The amount of objects in the level, used to determine if the level is considered "large". It caps at 65535"""
    editorTime:int#46
    """The total number of seconds spend on the current copy of a level"""
    editorTimeCopies:int#47
    """	The accumulative total of seconds spend on previous copies of the level"""
    songIDs:list[int]#52 split by comma
    """The list of all song IDs in the level"""
    sfxIDs:list[int]#53 split by comma
    """The list of all SFX IDs in the level"""
    verificationFrames:int #57
    """	How long the level took to verify (in frames, assume 240 FPS)"""
    isNA:bool#57
    """If the level shows a difficulty face of N/A"""
    def __init__(self,levelWithHashes:str):
        """Create a GDFetchedLevel object from a fetched level in double-colon format."""
        level=levelWithHashes.split("#")[0] 
        dic:dict[str,str]=parseDoubleColonString(level)
        self.levelID:int =int_handled(dic.get('1','0')) 
        self.levelName:str=dic.get('2',"")
        try:
            self.description:str=base64.b64decode(dic.get('3',"").encode("ascii")).decode("ascii")
        except:
            
            self.description:str="Error getting description- Encoded "+dic.get('3',"")
        self.version:int|None=dic.get('5',None)
        self.playerID:int=int_handled(dic.get('6','0'))
        difficultyDenominator=int_handled(dic.get('8','0'))
        self.difficultyDenominator: int =int_handled(dic.get('8','0'))
        difficultyNumerator=int_handled(dic.get('9','0'))
        self.difficultyNumerator: int =int_handled(dic.get('9','0'))
        self.downloads:int =int_handled(dic.get('10','0'))
        
        self.officialSong:int|None =int_handled(dic.get('8',0))
        self.gameVersionOrg:int =int_handled(dic.get('13',0))
        self.likes:int =int_handled(dic.get('14',0))
        self.length:int =int_handled(dic.get('15',0))
        self.dislikes:int =int_handled(dic.get('16',0))
        isDemonOrg=dic.get('17','')
        isDemon=False
        if isDemonOrg=='1':
            isDemon=True
        self.isDemon:bool=isDemon #17 converted
        self.stars:int=int_handled(dic.get('18',0)) #18
        self.featureScore:int=int_handled(dic.get('19',0)) #19
        isAutoOrg=dic.get('25','')
        isAuto=False
        if isAutoOrg=='1':
            isAuto=True
        self.isAuto:bool=isAuto #25


        self.copiedId: int=int_handled(dic.get('30','0')) #30
        twoPlayerOrg=dic.get('25','')
        twoPlayer=False
        if twoPlayerOrg=='1':
            twoPlayer=True
        self.twoPlayer:bool=twoPlayer #31
        self.customSongID:int|None=int_handled(dic.get('35','0')) #35
        self.extraString:str|None=dic.get('36','') #36
        self.coins:int=int_handled(dic.get('37','0')) #37
        self.verifiedCoins:int=int_handled(dic.get('38','0')) #38
        self.starsRequested:int=int_handled(dic.get('39','0')) #39

        self.dailyNumber:int=int_handled(dic.get('41','0')) #41
        self.epic:int =int_handled(dic.get('42','0'))#42
        self.demonDifficulty:int=int_handled(dic.get('43','0'))#43
        isGauntletOrg=dic.get('44','')
        isGauntlet=False
        if isGauntletOrg=='1':
            isGauntlet=True
        self.isGauntlet:bool=isGauntlet#44
        self.objects:int=int_handled(dic.get('45','0'))#45
        self.editorTime:int=int_handled(dic.get('46','0'))#46
        self.editorTimeCopies:int=int_handled(dic.get('47','0'))#47
        songIDsOrg=dic.get('52','').split(",")
        songIDs=[]
        for i in songIDsOrg:
            songIDs.append(int_handled(i))
        sfxIDsOrg=dic.get('53','').split(",")
        sfxIDs=[]
        for i in sfxIDsOrg:
            sfxIDs.append(int_handled(i))
        self.songIDs:list[int]=songIDs#52 split by comma
        self.sfxIDs:list[int]=sfxIDs#53 split by comma
        self.verificationFrames:int=int_handled(dic.get('57','0')) #57
        if self.isAuto:
            difficulty=DIFFICULTY_AUTO
        elif not isDemon:
            difficulty=int_handled(difficultyNumerator/10)
        else:
            if self.demonDifficulty==3:
                difficulty=DIFFICULTY_EASYDEMON
            if self.demonDifficulty==4:
                difficulty=DIFFICULTY_MEDIUMDEMON
            if self.demonDifficulty==0:
                difficulty=DIFFICULTY_HARDDEMON
            if self.demonDifficulty==5:
                difficulty=DIFFICULTY_INSANEDEMON
            if self.demonDifficulty==6:
                difficulty=DIFFICULTY_EXTREMEDEMON
        self.difficulty:int=difficulty
        gameVersion=0
        if self.gameVersionOrg==1:gameVersion=10
        if self.gameVersionOrg==2:gameVersion=11
        if self.gameVersionOrg==3:gameVersion=12
        if self.gameVersionOrg==4:gameVersion=13
        if self.gameVersionOrg==5:gameVersion=14
        if self.gameVersionOrg==6:gameVersion=15
        if self.gameVersionOrg==7:gameVersion=16
        if self.gameVersionOrg==10:gameVersion=17
        if self.gameVersionOrg>10:gameVersion=self.gameVersionOrg
        self.gameVersion:int=gameVersion
        if self.difficultyDenominator==10:
            self.isNA=False
        else:
            self.isNA=True
class GDUser:
    """A class used to represent a GD User."""
    def __init__(self,userstr):
        """Create a GD User object from a double colon string as returned by the endpoint `getGJUserInfo20`."""
        user=parseDoubleColonString(userstr)
        
        self.username=user.get("1","")
        self.playerID=int_handled(user.get("2",0))
        """The player ID of the player. This is NOT the account ID."""
        self.stars=int_handled(user.get("3",0))
        self.demons=int_handled(user.get("4",0))
        self.ranking=int_handled(user.get("6",0))
        self.creatorpoints=int_handled(user.get("8",0))
        self.unknownIconID=int_handled(user.get("9",0))
        """I don't know what this is because `cubeID` exists"""
        self.color1=int_handled(user.get("10",0))
        self.color2=int_handled(user.get("11",0))
        self.secretCoins=int_handled(user.get("13",0))
        self.profileIcon=int_handled(user.get("14",0))
        self.accountID=int_handled(user.get("16",0))
        self.usercoins=int_handled(user.get("17",0))
        self.messageState=int_handled(user.get("18",0))
        """0: All, 1: Only friends, 2: None"""
        self.friendReqState=int_handled(user.get("19",0))
        """0:All, 1:None"""
        self.youtubeURL=user.get("20","")
        self.cubeID=int_handled(user.get("21",0))
        self.shipID=int_handled(user.get("22",0))
        self.ballID=int_handled(user.get("23",0))
        self.ufoID=int_handled(user.get("24",0))
        self.waveID=int_handled(user.get("25",0))
        self.robotID=int_handled(user.get("26",0))
        self.streakID=int_handled(user.get("27",0))
        self.glowID=int_handled(user.get("28",0))
        self.isRegistered=int_handled(user.get("29",0))
        self.globalRank=int_handled(user.get("30",0))
        self.spiderID=int_handled(user.get("43",0))
        self.twitterURL=user.get("44","")
        self.twitchURL=user.get("45","")
        self.diamonds=int_handled(user.get("46",0))
        self.deathEffectID=int_handled(user.get("48",0))
        self.modLevel=int_handled(user.get("49",0))
        """0:Not moderator, 1:Normal moderator, 2:Elder Moderator"""
        self.commentHistoryState=int_handled(user.get("50",-1))
        """0:All, 1:Friends only, 2:None, -1:Failed to fetch"""
        self.glowColor=int_handled(user.get("51",0))
        self.moons=int_handled(user.get("52",0))
        self.swingID=int_handled(user.get("53",0))
        self.jetpackID=int_handled(user.get("54",0))
        self.demonBreakdownStr=user.get("55","")
        """Breakdown of the player's demons, in the format `{easy},{medium},{hard}.{insane},{extreme},{easyPlatformer},{mediumPlatformer},{hardPlatformer},{insanePlatformer},{extremePlatformer},{weekly},{gauntlet}`"""
        self.classicBreakdownStr=user.get("56","")
        """Breakdown of the player's classic mode non-demons, in the format `{auto},{easy},{normal},{hard},{harder},{insane},{daily},{gauntlet}`"""
        self.platformerBreakdownStr=user.get("57","")
        """Breakdown of the player's platformer mode non-demons, in the format `{auto},{easy},{normal},{hard},{harder},{insane}`"""
class GDCommentOrPost:
    """A class used to represent a geometry dash comment."""

    def __init__(self,commentStr:str):
        dic=parseDoubleColonString(commentStr.split(":")[0],sep="~")
        self.levelID=int_handled(dic.get("1",0))
        try:
            self.comment=base64.b64decode(dic.get("2","").encode("ascii")).decode("ascii")
            """The content of the comment"""
        except:
            self.comment="Failed to base64 decode comment- encoded value: "+dic.get("2","")
            """The content of the comment"""
        self.content=self.comment
        """The content of the comment"""
        self.playerID=int_handled(dic.get("3",0))
        self.likes=int_handled(dic.get("4",0))
        self.dislikes=int_handled(dic.get("5",0))
        self.messageID=int_handled(dic.get("6",0))
        self.accountID=int_handled(dic.get("8",0))
        isFlaggedSpam=False
        if dic.get("7","") == "1":
            isFlaggedSpam=True
        self.isFlaggedSpam=isFlaggedSpam
        self.commentAge=dic.get("9","")
        """How long has it been since the comment was posted."""
        self.percent=int_handled(dic.get("10",-1))
        """-1 if no percent"""
        self.modBadge=int_handled(dic.get("11",0))
        """0=not mod, 1=normal mod, 2=elder mod"""
        self.modChatColor=dic.get("12","")
        """Comma separated list of the RGB values of the moderator's chat color - only appears if the players modBadge > 0"""
        if len(commentStr.split(":"))==1:
            return #this is an account comment
        dic2=parseDoubleColonString(commentStr.split(":")[1],sep="~")
        self.userName=dic2.get("1","")
        self.accountID=int_handled(dic2.get("16",0))
        self.authorStars=int_handled(dic2.get("3",0))
        self.profileIcon=int_handled(dic2.get("9",0))
        """The icon ID of the icon showed in the corner of the comment."""
        self.playerColor=int_handled(dic2.get("10",0))
        self.playerColor2=int_handled(dic2.get("11",0))
        self.profileIconForm=["cube","ship","ball","ufo","wave","robot","spider","swing","jetpack"][int_handled(dic2.get("14",0))]
        self.glow=bool(int_handled(dic2.get("15",0)))
        return
    def getFullAuthorInfo(self):
        """Gets full info the author (as a user object)"""
        return getUserInfo(self.accountID)
#======FUNCTIONS========
#Utilities (mainly used for other functions)
def int_handled(*args,**kwargs):
    try:
        a=int(*args,**kwargs)
    except ValueError:
        a=0
    finally:
        return a
def decode_level_password(password: str) -> str:
        """Decodes the password of a level using the server provided password string 
        (not the one you get using `level.password` which is the original password)."""
        # decode the password from base64
        decoded_base64 = base64.b64decode(password.encode()).decode()
        # put it through the xor cipher with the key "26364")
        decoded = xor_cipher_cyclic(decoded_base64, "26364") 
        return decoded
def generate_upload_seed(data: str, chars: int = 50) -> str:
    """Generates the upload seed used for level uploading."""
    # GD currently uses 50 characters for level upload seed
    if len(data) < chars:
        return data  # not enough data to generate
    step = len(data) // chars
    return data[::step][:chars]
def generate_chk(values= [], key: str = "", salt: str = "")->str:
    """Generates a CHK. CHK is a common parameter in requests, which is intended to improve security."""
    values.append(salt)

    string = ("").join(map(str, values))  # assure "str" type and connect values

    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor_cipher_cyclic(hashed, key)  # we discuss this one in encryption/xor
    final = base64.urlsafe_b64encode(xored.encode()).decode()
    return final
def generate_gjp2(password: str = "", salt: str = "mI29fmAnxgTs") -> str:
    """Generate the gjp2 of a password, used in actions that require sign-in.  Note- NEVER hardcode your password, GJP or GJP2 as that's all someone needs to log in to your account.
    Args-
        `password` The password to convert to gjp2
        `salt` The salt used. Defaults to `mI29fmAnxgTs` as that is the currently used salt for gjp2 generation. """
    password += salt
    hash = hashlib.sha1(password.encode()).hexdigest()
    return hash
def xor_cipher_cyclic(inp,key):
    """Use a cyclic XOR cipher on `inp` using key `key` and return the result. 
    
    This is used for various tasks such as getting level copy passwords. The same function is used to both decrypt and encrypt the input."""
    result = ""
    for i in range(0,len(inp)): 
      byte = ord(inp[i])
      xKey = ord(key[i % len(key)])
      result += chr(byte ^ xKey)
    return result
def parseDoubleColonString(string:str,sep:str=":") ->dict[str,str]:
    """Convert a double-colon string `string` into a dictionary.
    
    Many things in geometry dash (such as levels) are returned by the server in a double-colon string format.
    Double colon strings are formatted like so- `key:value:key:value:...`"""
    lis=string.split(sep)
    i=0
    keys=[]
    values=[]
    while(i<len(lis)):
        keys.append(lis[i])
        i=i+1
        try:
            values.append(lis[i])
            i=i+1
        except:
            #print("Odd number of values in double-colon string.") # debug
            pass
    dic = dict(zip(keys, values))
    return dic
#Library features
def downloadLevel(lvlid: int) -> GDLevel:
    """Downloads a Geometry Dash level using a given ID and returns it as a `GDLevel` object.
    
    This function sends a request to http://www.boomlings.com/database/downloadGJLevel22.php to fetch the level."""
    headers = {
        "User-Agent": ""
    }

    data = {
        "levelID": lvlid,
        "secret": "Wmfd2893gb7"
    }

    url = "http://www.boomlings.com/database/downloadGJLevel22.php"

    req = requests.post(url=url, data=data, headers=headers)
    lvl=GDLevel(req.text)
    return lvl
def uploadLevel(level:GDLevel,username:str,accountID:int,gjp2:str,levelID=0,gameVersion=22,password=None,originalID=None,version=None,officialSong=None,customSong=None)->str:
    """Upload a level to the server using the `uploadGJLevel21` endpoint.
    
    If `levelID` is not zero, tries to update the level with id `levelID`.
    
    When `password`, `originalID`, `version`, `officialSong` or `customSong` is left as None, tries getting it from the level passed in.
    Set `originalID` to 0 if the level is not copied, set `officialSong` or `customSong` to 0 if the level doesn't use the respective kind of song."""
    if password==None:
        password=level.password
    if originalID==None:
        originalID=level.copiedId
    if version==None:
        version=level.version
    if officialSong==None:
        officialSong=level.officialSong
    if customSong==None:
        customSong=level.customSongID
    uploadData={"gameVersion":gameVersion, 
    "accountID": accountID,
    "userName": username,
    "gjp2":gjp2,
    "seed2": generate_chk(key="41274", values=[generate_upload_seed(level.levelString)], salt="xI25fpAapCQg"), #generate from level string,
    "levelID": levelID, 
    "password":password, 
    "original":originalID,
    "levelName":level.levelName,
    "levelDesc": level.description,
    "levelString":level.levelString,
    "levelVersion":version, 
    "audioTrack":officialSong,
    "levelLength":level.length,
    "songID":customSong,
    "coins":level.coins,
    "ldm":level.lowDetailMode,
    "objects":level.objects,
    "auto":level.isAuto,
    "twoPlayer":level.twoPlayer,
    "requestedStars":level.starsRequested,
    "secret":"Wmfd2893gb7",
    #optional, put to prove legitimacy
    "wt":level.editorTime, 
    "wt2":level.editorTimeCopies 
    }
    headers = {
    "User-Agent": ""
    }
    url = "http://www.boomlings.com/database/uploadGJLevel21.php"
    
    req = requests.post(url=url, data=uploadData, headers=headers)
    return req.text
def searchForLevels(type=TYPE_MOSTLIKE,page:int=0,query:str|None=None,difficultyFilter=None,demonFilter=None,length=None,uncompleted=False,completed=False,completedLevelIDs:list=[],featured=False,original=False,twoPlayer=False,coins=False,epic=False,legendary=False,mythic=False,noStar=False,star=False,followedUsers:list=[])->list[GDFetchedLevel]:
    """This function is used to search levels by name and/or filter.
    
    Args-
        `type`:    Use TYPE_SEARCH,TYPE_MOSTDOWNLOAD,TYPE_MOSTLIKE,etc constants to set the type of the search.
        `page`:    The page number.
        `query`:   For TYPE_SEARCH, this is the search query,
                For TYPE_USERSLEVELS, this is the user ID of the user's levels to search,
                For TYPE_LISTOFID, this is a comma seperated list of level IDs
        `difficultyFilter`:   Use FILTER_NA and FILTER_EASY to FILTER_DEMON or None(default) to filter the difficulty
        `demonFilter`:     If difficultyFilter is FILTER_DEMON, then use DEMONFILTER_EASY,DEMONFILTER_MEDIUM,...,DEMONFILTER_EXTREME to filter which kind of demon to search, or use None(default).
        `length`:    Use LENGTH_TINY to LENGTH_XL and LENGTH_PLAT to filter by level length, or use None (default).
        `uncompleted`,`completed`,`featured`,`original`,`twoPlayer`,`coins`,`epic`,`legendary`,`mythic`,`noStar`,`star`:
            If any of these are True, filters by levels that have the respective property. If False, does not apply that filter.
            (so if `completed`=False it will show **BOTH** the levels that are completed and those that are not.)
        `completedLevelIDs`:     If using uncompleted or completed=True, this list specifies which level IDs are completed. Otherwise, it does not matter.
        `followedUsers`:   If type=TYPE_FOLLOWED, this is a list of user IDs that are followed.
    """
    for i,e in enumerate(completedLevelIDs):
        completedLevelIDs[i]=str(e)
    for i,e in enumerate(followedUsers):
        followedUsers[i]=str(e)
    headers = {
    "User-Agent": ""
    }
    data = {
    "star": int(star),
    "noStar":int(noStar),
    "uncompleted":int(uncompleted),
    "onlyCompleted":int(completed),
    "completedLevels":"("+(",".join(completedLevelIDs))+")",
    "type": type,
    "secret": "Wmfd2893gb7",
    "page":page,
    "featured":int(featured),
    "original":int(original),
    "twoPlayer":int(twoPlayer),
    "coins":int(coins),
    "epic":int(epic),
    "mythic":int(legendary),
    "legendary":int(mythic),
    "followed":",".join(followedUsers)
    }
    if query != None:
        data.update({"str":query})
    if difficultyFilter != None:
        data.update({"diff":difficultyFilter})
    if demonFilter != None:
        data.update({"demonFilter":demonFilter})
    if length !=None:
        data.update({"len":length})
    url = "http://www.boomlings.com/database/getGJLevels21.php"
    req = requests.post(url=url, data=data, headers=headers)
    reqtext=req.text
    levelstrs=reqtext.split("#")[0].split("|")
    levels=[]
    for i in levelstrs:
        levels.append(GDFetchedLevel(i))
    return levels
def fetchLevel(lvlid:int) ->GDFetchedLevel:
    """Fetch a level by searching for it using TYPE_LISTOFID. This is WAY faster than downloading it using `downloadLevel()` and can fetch multiple levels in a single request (see `fetchLevels()`)"""
    level=searchForLevels(type=TYPE_LISTOFID,query=str(lvlid))[0]
    return level
def fetchLevels(lvlids:list[int]) ->list[GDFetchedLevel]:
    """Fetch levels by searching for them using TYPE_LISTOFID (uses only one request for all the levels). This is WAY faster than downloading it using `downloadLevel()`. If you want to do this for one level only, see `fetchLevel()`"""
    for i,e in enumerate(lvlids):
        lvlids[i]=str(e)
    levels=searchForLevels(type=TYPE_LISTOFID,query=",".join(lvlids))
    return levels
def getUserInfo(accountID)->GDUser:
    """Gets info about a user using accountID."""
    url = "http://www.boomlings.com/database/getGJUserInfo20.php"
    data = {
        "secret": "Wmfd2893gb7",
        "targetAccountID": str(accountID)
    }
    headers = {
        "User-Agent": ""  # Empty User-Agent
    }

    req= requests.post(url, data=data, headers=headers)
    reqtext=req.text
    user=GDUser(reqtext)
    return user

'''
The endpoint seems to trigger a Cloudflare warning, so it has been commented. Remove the triple quotes at the start and end and remove this message to re-add the function.
def getUserWithName(name:str)->GDUser:
    """Gets info about a user using username."""
    data = {
        "secret": "Wmfd2893gb7",
        "str": name,
        "gameVersion":22
    }

    req = requests.post('http://boomlings.com/database/getGJUsers20.php', data=data)
    try:
        user=GDUser(req.text)
        ###print(req.text) #for debug
    except:
        user=GDUser("1:ERROR_User_not_found")
    return user  
'''  

def getLevelComments(lvlid:int,page:int=0,sortRecent:bool=False)->list[GDCommentOrPost]:
    """Get the comments of a level."""
    data = {
        "levelID": lvlid,
        "page": page,
        "mode":int(not sortRecent),
        "secret": "Wmfd2893gb7"
    }

    headers = {
        "User-Agent": ""
    }

    url = "http://www.boomlings.com/database/getGJComments21.php"
    req = requests.post(url, data=data, headers=headers)
    comments=req.text.split("|")
    for i,e in enumerate(comments):
        comments[i]=GDCommentOrPost(e)
    return comments

def getUserPosts(accountID:int,page:int=0,):
    """Gets a user's posts/account comments."""
    data = {
        "accountID": accountID,  
        "page": page,
        "secret": "Wmfd2893gb7"
    }

    headers = {
        "User-Agent": ""
    }

    url = "http://www.boomlings.com/database/getGJAccountComments20.php"
    req = requests.post(url, data=data, headers=headers)
    posts=req.text.split("|")
    for i,e in enumerate(posts):
        posts[i]=GDCommentOrPost(e)
    return posts
def getCommentHistory(playerID:int,page:int=0,sortRecent:bool=True):
    """Get the comment history of a player. **The player ID is NOT the account ID**"""
    data = {
        "userID": playerID, # DevExit's player ID
        "page": page,
        "mode": int(sortRecent),
        "secret": "Wmfd2893gb7"
    }

    req = requests.post("http://boomlings.com/database/getGJCommentHistory.php", data=data)
    comments=req.text.split("|")
    for i,e in enumerate(comments):
        comments[i]=GDCommentOrPost(e)
    return comments
def createAccountPost(accountID,gjp2,contents):
    """Posts on an account and returns the comment ID (posts are technically "account comments"), or -1 if the request was rejected."""
    data = {
        "accountID": accountID,
        "gjp2": gjp2, 
        "comment": base64.b64encode(contents.encode("ascii")).decode("ascii"),
        "secret": "Wmfd2893gb7",
    }

    req = requests.post('http://boomlings.com/database/uploadGJAccComment20.php', data=data)
    try:
        ID=int(req.text)
        return ID
    except:
        return req.text

def commentToLevel(username,accountID,gjp2,contents,levelID,percent=0):
    """Comment on a level and return the commentID or -1 if the request was rejected by the server."""

    
    encoded=base64.b64encode(contents.encode("ascii")).decode("ascii")
    chk = generate_chk(key="29481", values=[username, encoded, levelID, percent], salt="0xPT6iUrtws0J")


    data = {
        "accountID": accountID, 
        "gjp2": gjp2, 
        "userName": username,
        "comment": encoded,
        "levelID": levelID,
        "percent": percent,
        "chk": chk,
        "secret": "Wmfd2893gb7"
    }

    req = requests.post("http://boomlings.com/database/uploadGJComment21.php", data=data)
    return req.text

def deletePost(accountID,gjp2,commentID):
    """Deletes a post and returns "1"(as a string) if successful and "-1" if there was an error."""
    data = {
        "accountID": accountID, # DevExit's account ID
        "gjp2": gjp2, # This would be DevExit's password encoded with GJP encryption
        "commentID": commentID,
        "secret": "Wmfd2893gb7"
    }

    req = requests.post('http://boomlings.com/database/deleteGJAccComment20.php', data=data)
    return req.text

def deleteLevelComment(accountID,gjp2,commentID,levelID):
    """Deletes a level comment and returns "1"(as a string) if successful and "-1" if there was an error."""
    data = {
            "accountID": accountID, # DevExit's account ID
            "gjp": gjp2, # This would be DevExit's password encoded with GJP encryption
            "commentID": commentID,
            "levelID": levelID,
            "secret": "Wmfd2893gb7"
    }

    req = requests.post("http://boomlings.com/database/deleteGJComment20.php", data=data)
    return req.text


def likeItem(ID,type,accountID,gjp2,dislike=False):
    """Likes/dislikes a level, comment, post or a list. `type`=1 for level, 2 for comment, 3 for post and 4 for list."""
    data = {
        "secret": "Wmfd2893gb7",
        "itemID": ID,
        "type": type,
        "like": int(not dislike),
        "accountID": accountID,
        "gjp2":gjp2
    }

    req = requests.post('http://boomlings.com/database/likeGJItem211.php', data=data)
    return req.text

