#  last updated 5/05/22 by tariq / jon 
# to do:    to finish 

"""
if time allows:
* 2 dimentional array for players results of rounds

8-5-22
1. tidy messages to user 
2. change all variables names and function names to be consistant
3. after all code done: 
    1. tidy messages for debug (remove)




5-5-22 - to do
>>>>>>>>>>>>>>>>>>>>>>>>>    today: write files
1. stop game orderly
2. tidy messages end of round/game
2. write files .csv



to do:
* tidy naming of variables
* tidy messages and screen visibility
* add 'game' variable so games can be distinguished
    *add this to game csv

end round
end game
** writing files

3. ???? 2nd login after register - if difficult - ask for 2 logins

29-4-22
1. ok register 2nd user y/n
2. done already before -- before registering 2nd user - validate 2nd user not already exist

what is changed in this version: 
-user 2 playerName1 and password validted to see if credentials are in file
-register two users to play game and both are validated

=============================================================
1. JON map flow chart of all the code with all the function
2. Tariq - try to validate login of player 2 - ok
2.5 register more than player at the time
3. tidy all messages - check if required
4. add 2nd player login to validation
5. priority : deal with end-of-round (files: additions of data) etc
6. priority: deal with end-of-game functions
"""

"""
############## game ####################### 

 This game introduce a multi prisoners
 kkjojo oi0i0o oi

"""
import os
from os import curdir, path
import random
from datetime import datetime
from datetime import time
from datetime import datetime
from time import sleep
import csv
#from typing import _VT

usersFile = "playersFile.txt"
gameDataDirectory = "TariqPrisionersDilema_GamesData"
messageTransfer = "no message";
global menuCounter 

def writeGameDataToFile(winner):
    print()
    inFile= False
 
    print("arrived at function writGameDataToFile()")
    print("# *20" + " write game data")
    print("round time: =" + str(gameDateTime))
    #print("round time: =" + str(roundDateTime))
    print("total rounds in game: " + str(roundsNumberInGame))
    print("playerName1 =" + playerName1)
    print("playerName2 =" + playerName2)
    print("relation between players: "+ relationBetweenPlayers)
    print("playerOne's Moves where = "+ str(playerOneMoveList))
    print("playerTwo's Move's were = "+ str(playerTwoMoveList))
    print("player one points: " + str(player1Points))
    print("player two points: "+ str(player2Points))
    print("the winner was: "+ winner)

    gameNameFinal = "Tariqgame"+ str(gameDateTime)


    global gameDataHeader #add gaame + date time as one entry
    gameDataHeader= ['GameName','Game_Date_Time', 'Round_Number','Rounds_per_game','Player_1','Player_2','Relation','Player_1_moves','player_2_moves', playerName1 + '_points', playerName2+'_points','game_winner','game_winner_points']

    gameDataCSV = [
        [currentGameNumberFinal, gameDateTime, str(roundsNumberInGame),str(roundsNumberInGame),playerName1, playerName2,relationBetweenPlayers,playerOneMoveList, playerTwoMoveList,player1Points,player2Points,winner, gameWinnerPoints]
        ]

    #gameNameFinal
    dirNameGame ="games_directory"


    with open(dirNameGame + '/gameData.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        
        
        if gameDataHeaderSearch(gameDataHeader) == True:
        #if inFile ==True :
            writer.writerows(gameDataCSV)
        else:
            writer.writerow(gameDataHeader)
            writer.writerows(gameDataCSV)



    with open((dirNameGame+ '/Game'+str(currentGameNumber) + ".csv"), 'a', encoding='UTF8', newline='') as f:
        writer =csv.writer(f)

        writer.writerow(gameDataHeader)
        writer.writerows(gameDataCSV)
     
    finalRoundWinner = winner
   
        
    finalMsg()



def gameDataHeaderSearch(gameDataHeader):
    dirNameGame ="games_directory"

    f = open(dirNameGame + "/gameData.csv" ,"r")
    fl = f.readlines()

        #user1 name search
    for x in fl:
         if "GameName" == x.split(",")[0]:
             return True
         else: 
                return False
         f.close



def writeRoundData(currentRound):
    print()

    gameName = "TariqGame"+ str(gameDateTime) + str(roundDateTime)
    roundNumber = str(currentRound)
    playerOneName = playerName1
    playerTwoName = playerName2
    relationOfPlayers = relationBetweenPlayers
    global player1Move
    player1Move = playerOneMove
    global player2Move
    player2Move = playerTwoMove
    playerOnePoints = str(player1Points)
    playerTwoPoints = str(player2Points)



    global currentGameNumberFinal
    currentGameNumberFinal = "Game " + str(currentGameNumber)



#---------------------------------------------------------------
    #if playerOnePoints > playerTwoPoints:
    #    roundWinner = playerOneName
    #    draw = ""
   

    #elif playerOneScore < playerTwoScore:
    #    roundWinner = playerTwoName
    #    draw = ""

    #elif playerOneScore == playerTwoScore:
    #    roundWinner = ""

#---------------------------------------------------------------

    #global roundDataHeader
    #roundDataHeader = ['GameName','Round_Number','Player_1_name','Player_2_name','Relation','Player_1_move','player_2_move','player_1_points','player_2_points','Round_Winner']
    finalRoundWinner= ''
    global roundDataCSV
    roundDataCSV = [
        [currentGameNumberFinal, str(gameDateTime) ,currentRound,str(roundsNumberInGame),playerOneName, playerTwoName, relationOfPlayers, player1Move, player2Move, playerOnePoints, playerTwoPoints, roundWinner]
    ]
    #gameName
    with open('roundsData.csv', 'a', encoding='UTF8', newline='') as CSV:
        writer = csv.writer(CSV)



        if roundDataHeaderSearch(roundDataHeader) == True:
        #if inFile ==True :
            writer.writerows(roundDataCSV)
        else:
            writer.writerow(roundDataHeader)
            writer.writerows(roundDataCSV)

#-----------------------------------------------------------
    dirNamePlayer = "Players_directory"

    with open(dirNamePlayer+ "/player_"+str(playerOneName) + ".csv", 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(roundDataCSV)
        f.close

#-----------------------------------------------------------

    with open( dirNamePlayer+"/player_"+ str(playerTwoName) + ".csv", 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(roundDataCSV)
        f.close

    #writeRoundDataToFile(currentRound)

def roundDataHeaderSearch(roundDataHeader):

        f = open("roundsData.csv" ,"r")
        fl = f.readlines()

        #user1 name search
        for x in fl:
            if "GameName" == x.split(",")[0]:
                return True
            else: 
                return False
        f.close



        


def gameDataPrintHeader(winner):#old code not being used for now
    global gameDataHeader
    gameDataHeader= ['Game Name','Round Number','Player 1 name','Player 2 name','Relation','Player one moves','player two moves','player one points','player two points','winner']

    with open('gameData.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)


        writer.writerow(gameDataHeader)
    writeGameDataToFile(winner)



def roundDataWriteHeader(currentRound):#old code not being used for now
    global roundDataHeader
    roundDataHeader = ['Game name','Round Number','Player 1 name','Player 2 name','Relation','Player one move','player two move','player one points','player two points']
   
    with open('roundsData.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        #writer = csv.DictWriter(f, fieldnames=fieldnames)
        # write the header

        writer.writerow(roundDataHeader)
    #writeRoundDataToFile(currentRound)
    


def RoundData (currentRound, playerOneScore, playerTwoScore, user1, user2):
    global player1Points
    global player2Points
    player1Points = playerOneScore
    player2Points = playerTwoScore

    global playerName1
    playerName1 = user1

    global playerName2
    playerName2 = user2
    print()
    print("\n \n ***************** end of round ***********************")
    print("you arrived at RoundData() function \n \n")
    print("*****************************************playerName1 =" + playerName1)
    print("*****************************************playerName2 =" + playerName2)
    global roundDateTime
    roundDateTime = datetime.now()


    print ("date time signature = " + str(roundDateTime))

  
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>playerOneMove = "+ playerOneMove)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>playerTwoMove = "+ playerTwoMove)

    global playerOneMoveList
    playerOneMoveList.append(playerOneMove)

    global playerTwoMoveList
    playerTwoMoveList.append(playerTwoMove)

    print(playerOneMoveList)
    print(playerTwoMoveList)
    #print("relationship between players was: " + relationBetweenPlayers) 
   # print("the total number of round in the game was: " +str(roundsNumberInGame))

    print("player one's score was:" + str(player1Points))
    print("player two's score was:" + str(player2Points))

    if player1Points > player2Points:
        global roundWinner
        roundWinner = playerName1
        draw = ""
   

    elif player1Points < player2Points:
        roundWinner = playerName2
        draw = ""

    elif player1Points == player2Points:
        roundWinner = ""

   

    writeRoundData(currentRound)
           


def gameData(playerOneScore, playerTwoScore, user1, user2, winner, loser, draw):
 
    player1Points = playerOneScore
    player2Points = playerTwoScore
    
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!going to sleep screen and clear screen data")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!going to wait 4 seconds")
    #sleep(4)
    #os.system('cls')

    print("\n \n ***************** end of round data ***********************")
    print("you arrived at gameData() function \n \n")



    print("*****************************************playerName1 =" + playerName1)
    print("*****************************************playerName2 =" + playerName2)
    #gameName = "tariqGame" + str(gameDateTime)
    #gameDateTime = datetime.now()

    gameNameRoundData = "tariqGame" + str(gameDateTime)

    print ("date time signature = " + str(gameDateTime))

  
    print("relationship between players was: " + relationBetweenPlayers) 
    print("the total number of round in the game was: " +str(roundsNumberInGame))
    #roundNumberOfGameTotalRounds = 0
    #winner = 0
    #loser = 0
    print("player one's score was:" + str(player1Points))
    print("player two's score was:" + str(player2Points))
    print("the winner was: "+ winner)
    print("the loser was: "+ loser)
    print("player one's moves were: " + str(playerOneMoveList))
    print("player two's moves were: " + str(playerTwoMoveList))

    writeGameDataToFile(winner)

def roundPlay(currentRound, playerOneScore, playerTwoScore, user1, user2):
   

     if (int(currentRound) != 0):
         print("prinint round info")
         RoundData (currentRound, playerOneScore, playerTwoScore, user1, user2)
         #writeRoundDataToFile(currentRound):
     
     if (int(currentRound) < int(roundsNumberInGame)):
         print("\ \ in function roundPlay(): when current round < totalRounds:  choose move \ \ ")    
         currentRound = currentRound + 1
         #writeRoundDataToFile(currentRound):
         playersChooseMove(currentRound, playerOneScore, playerTwoScore, user1, user2)

     else: 
        print("\ \ in function roundPlay(): when current round => totalRounds:  display game data \ \ ")    

        endOfGame(playerOneScore, playerTwoScore, user1, user2)



def playGame(menuOption, user1, user2):
    #global currentRound
    currentRound = 0
    menuSelection = menuOption
    global playerOneScore
    global playerTwoScore
    playerOneScore = 0
    playerTwoScore = 0


    displayRulesAndPlay(menuOption)
    gameSetup(user1, user2)


    roundPlay(currentRound, playerOneScore, playerTwoScore, user1, user2)# used to test logic before filling functions
    
 


def gameSetup(user1, user2):
     playerOneName = user1
     playerTwoName = user2
     fileValid = False

  #-----------------------------------
     print()
     print()
     print ("#" * 80)
     print("#" * 10 + " " * 60 + "#" * 10)
     print("#" * 10 + " " * 60 + "#" * 10)
     print()
     print(" " * 5 + " The game will start with: " + playerOneName +", and " +playerTwoName+ "!" + " " * 1)
     print()
     print("#" * 10 + " " * 60 + "#" * 10)
     print("#" * 10 + " " * 60 + "#" * 10)
     print ("#" * 80)
     print()
     print()
  #-----------------------------------
     global gameDateTime
     gameDateTime = str(datetime.now())
     global currentRound
     global roundsNumberInGame
     roundsNumberInGame = input("please enter the number of rounds you'd like to play: ----------> ")

     global relationBetweenPlayers 

     relationBetweenPlayers = ""
#-----------------------------------------------------------


     dirNameGame = "games_directory"
     with open("currentGameNumber.txt", "r") as f:
         global currentGameNumber
         currentGameNumber= f.read()
         print(currentGameNumber)
         f.close

     with open("currentGameNumber.txt", "w") as f:
         currentGameNumber = int(currentGameNumber) + int(1)
         f.write(str(currentGameNumber))
         print(currentGameNumber)
         f.close
        
 
     global roundDataHeader
     roundDataHeader = ['GameName','Game_date_time','Round_Number','Rounds_per_game','Player_1','Player_2','Relation','Player_1_move','player_2_move', 'player1_points', 'Player2_points','Round_Winner']
 #----------------------------------------------------------

    
     with open(dirNameGame +'/Game'+str(currentGameNumber) + ".csv", 'w', encoding='UTF8', newline='') as f:
         f.close
#-----------------------------------------------------------


#-----------------------------------------------------------


     global playerOneMoveList
     global playerTwoMoveList

     playerOneMoveList =[]
     playerTwoMoveList = []

     currentRound=0
    
 #-----------------------------------
     print()
     print()
     print ("#" * 80)
     print("#" * 10 + " " * 60 + "#" * 10)
     print("#" * 10 + " " * 60 + "#" * 10)
     print()
     print(" " * 5 + " The game will start with: " + playerOneName +", and " +playerTwoName+ "!" + " " * 1)
     print(" " * 5 + " the players relationships are : " +relationBetweenPlayers + " " * 1)
     print(" " * 5 + " the game is set for : " +roundsNumberInGame + " " * 1)
     print()
     print("#" * 10 + " " * 60 + "#" * 10)
     print("#" * 10 + " " * 60 + "#" * 10)
     print ("#" * 80)
     print()
     print()

  #-----------------------------------


     #print ("Game is starting between: " + playerOneName + " and: " + playerTwoName + ", Who are: " + relationBetweenPlayers)
     #print("the game will be " + roundsNumberInGame + " rounds long")

     selectPlayerToStart(user1,user2)

     #---------------------------------

     reply = input ("Please enter relationship between players (s for strangers, f for friends, c for colleagues): ")

     if reply == "s":
        relationBetweenPlayers = "strangers"

     elif reply == "f":
        relationBetweenPlayers = "friends"

     elif reply == "c":
        relationBetweenPlayers = "colleagues"

     else:
         print()
         print("*****Error: please select between 's', 'f' and 'c'*****")
         gameSetup(user1, user2)
         #message = "wrong answer"
     
     global relationBetweenPlayer1andPlayer2 
     global relationBetweenPlayer2andPlayer1 
     relationBetweenPlayer1andPlayer2 = relationBetweenPlayers
     relationBetweenPlayer2andPlayer1 = relationBetweenPlayers

     if 1 <= int(roundsNumberInGame) <= 15:
        print("\n \n \n You have chosen to play "+ roundsNumberInGame + " rounds \n \n \n")
        #gameStart(user1,user2, playerOneScore, playerTwoScore)

     else: 
        print()
        print("*****Error: please enter a round number between 1 and 15 *****")
        gameSetup(user1, user2)

     dirNamePlayer = "Players_directory"

     if os.path.exists(dirNamePlayer+ "/Player_"+str(playerOneName) + ".csv"):
        print("player 1 file already exists")
     else:
        with open(dirNamePlayer+ "/Player_"+str(playerOneName) + ".csv", 'a', encoding='UTF8', newline='') as f:
             writer = csv.writer(f)
             writer.writerow(roundDataHeader)

 
#-----------------------------------------------------------
     if os.path.exists(dirNamePlayer+ "/Player_"+str(playerTwoName) + ".csv"):
        print("player 2 file already exists")
     else:
        with open(dirNamePlayer+ "/Player_"+ str(playerTwoName) + ".csv", 'a', encoding='UTF8', newline='') as f:
             writer = csv.writer(f)
             writer.writerow(roundDataHeader)



def selectPlayerToStart(user1, user2):
    playerOneName = user1
    playerTwoName =user2
    print("you have arrived at the select player to start function(user1)")
    players = [playerOneName , playerTwoName]
    print("players array before random shuffle = : " + str(players))
    random.shuffle(players)
    print("players array after random shuffle = : " + str(players))
    global currentPlayer
    currentPlayer = players[0]
    print("current player is : " + currentPlayer)

        
def playersChooseMove(currentRound, playerOneScore, playerTwoScore, user1, user2):
   print("*****you arrived at playersChooseMove() function, current round is "+ str(currentRound) + ", out of game round target of " + str(roundsNumberInGame)+"******")
   print()
   global playerOneMove
   playerOneMove = "playerOneMove - no move recorded yet"
   global playerTwoMove 
   playerTwoMove = "playerTwoMove - no move recorded yet"
   playerOneMove = input("Player 1 please make your move ('C' OR 'D'): ")
   playerTwoMove = input("Player 2 please make your move ('C' OR 'D'): ")
   print()
   print("round " +str(currentRound) + " of " +str(roundsNumberInGame) +  ", player one chose: "+ playerOneMove + " and player two chose: "+ playerTwoMove)

   calculateRoundScores(currentRound, roundsNumberInGame, playerOneMove, playerTwoMove, playerOneScore, playerTwoScore,user1, user2)
   

def calculateRoundScores(currentRound, roundsNumberInGame, playerOneMove, playerTwoMove, playerOneScore, playerTwoScore,user1, user2):
    print("AT ENTERING THE FUNCTION: player1 score is " + str(playerOneScore) + ", player2 score = " + str(playerTwoScore))

    if playerOneMove.upper() == "D" and playerTwoMove.upper() == "D":
         playerOneScore = playerOneScore + 1
         playerTwoScore = playerTwoScore + 1

    elif playerOneMove.upper() == "C" and playerTwoMove.upper() == "C":
         playerOneScore = playerOneScore + 2
         playerTwoScore = playerTwoScore + 2

    elif playerOneMove.upper() =="C" and playerTwoMove.upper() == "D":
         playerOneScore = playerOneScore + 0
         playerTwoScore = playerTwoScore + 3

    elif playerOneMove.upper() =="D" and playerTwoMove.upper() == "C":
         playerOneScore = playerOneScore + 3
         playerTwoScore = playerTwoScore + 0

    else:
        print()
        print("*****Error: please select between only 'C' and 'D'****** ")
        playersChooseMove(currentRound, playerOneScore, playerTwoScore, user1, user2)


    print()
    print("Player one score is: " + str(playerOneScore) + ", player1 move was: " + playerOneMove + ", and player two score is: " + str(playerTwoScore) + ", player2 move was: "+ playerTwoMove)

    roundPlay(currentRound, playerOneScore, playerTwoScore, user1 , user2)

def caculateGameScores():
     print("you arrived at CaculateGameScores() function")

def roundScoresWriteToFile():
    print("arrived at def roundScoresWriteToFile():")

def endOfRound():
    print("you arrived at the end of round function ()")

def finalMsg():
    print("******************you have reache the end after finishing the game!*****************")
    message = "thanks for playing Tariq's prisioners dilema"
    quit(message)

def endOfGame(playerOneScore, playerTwoScore, user1, user2):#

    print("you arrived at endOfGame functions()")

    print("Player ones score was: "+ str(playerOneScore) +" and player twos score was: " + str(playerTwoScore))

    if playerOneScore > playerTwoScore:
        global winner
        winner = user1
        loser = user2
        draw = ""
        global gameWinnerPoints
        gameWinnerPoints = playerOneScore
        print("the winner is : " + winner)
        print("the loser is : " + loser)
        gameData(playerOneScore, playerTwoScore, user1, user2, winner , loser, draw)
   

    elif playerOneScore < playerTwoScore:
        winner = user2
        loser = user1
        draw = ""
        gameWinnerPoints = playerTwoScore
        print("the winner is :" + winner)
        print("the loser is : " + loser)
        gameData(playerOneScore, playerTwoScore, user1, user2, winner , loser, draw)

    elif playerOneScore == playerTwoScore:
        winner = ""
        loser = ""
        draw = "draw"
        print("draw - there was no winner or loser")
        gameData(playerOneScore, playerTwoScore, user1, user2, winner , loser, draw)

def quitOrPlay(menuOption, user1, user2):
    print("Player 1 is: "+ user1, ", and Player 2 is "+ user2)
    print()
    print("***would you like to play game or quit '1' to play and 'q' to quit***")
    userInput = input("please make a selection: ")

    if userInput == "1":
        playGame(menuOption, user1, user2)
    if userInput.lower == "q":
        message = "quiting program"
        quit(message)#add quit 2 function option
    else:
        print()
        print("******Error: wrong input, please select between '1' or 'q' ")
        quitOrPlay(menuOption, user1, user2)

def main():
    menuCounter = 0
    mainNav(menuCounter)

def mainNav(menuCount):
    menuCounter = menuCount
    print()
    print()

    #sleep(4)
    os.system('cls')
    print ("#" * 80)
    print("#" * 10 + " " * 60 + "#" * 10)
    print("#" * 10 + "       Welcome to Tariq's Prisioners Dilema game   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "       Please choose one of the following options: " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "              1 - Log in and play game             " + " " * 9 + "#" * 10 )
    print("#" * 10 + "              2 - Register account                 " + " " * 9 + "#" * 10 )
    print("#" * 10 + "              q - quit                             " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + " " * 60 + "#" * 10)
    print ("#" * 80 + "\n")




    menuSelectVar = True
    arrivedFrom = "menuSelect"

    while menuCounter < 5 and  menuSelectVar == True:

        menuResponse = input("please select an option: ------> ")
        print()
        menuCounter = menuCounter + 1
        print("*******************===========>>>>> menu counter is: " + str(menuCounter))

        if menuResponse == "1" or menuResponse == "2" or menuResponse == "3" or menuResponse.lower() == "q":
            # .lower(), .upper(), .isupper(), .islower()
            #menuValid = True
            if menuResponse == "1":
                menuSelectVar = False
                userAndPasswordInput("login", menuCounter)
                #login(playerName1)

            if menuResponse == "2":
                menuSelectVar = False
                userAndPasswordInput("register", menuCounter)
                #register()

            if menuResponse == "3":
                menuSelectVar = False
                playGame("playGame")
                

            if menuResponse == "q":
                menuSelectVar = False
                message = "are you sure you want to quit2? - menu counter =  " + str(menuCounter)
                quit2(message, arrivedFrom, menuCounter)

        else:
            if menuCounter >= 5:
                message = "too many tries"
                quit(message)
            else:
                print("your selection is invalid, you selected:" + menuResponse + " - please try again")
                mainNav(menuCounter)
   

def quit(message):
    messageReceived = message
    print(messageReceived + "- quitting")
    exit()



def userAndPasswordInput(menuOption, menuCounter):
    menuSelection = menuOption
    global playerName1
    playerName1 = "playerName1 not known yet"
    global playerName2
    playerName2 = "playerName2 not known yet"

    if menuSelection == "login":
        os.system('cls')
        print ("#" * 80)
        print("#" * 10 + " " * 60 + "#" * 10)
        print("#" * 10 + "       please enter details of player1             " + " " * 9 + "#" * 10 )
        print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
        #print("#" * 10 + "       Please choose one of the following options: " + " " * 9 + "#" * 10 )
        print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
        print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
        print("#" * 10 + " " * 60 + "#" * 10)
        print ("#" * 80 + "\n")
        print("please enter details of player1 ")
        playerName1 = input("player1 name: ----------> ")
        passWord = input("please enter player1 password: ----------> ")
        print()
        print("please enter details of player2 ")
        playerName2 = input("please enter player2 name: ----------> ")
        passWord2 = input("please enter player2 password: ---------->  ")

        if playerName1 == playerName2:
            print("users have to have different names, please retry")
            userAndPasswordInput(menuSelection, menuCounter)
        else:
            #login(menuSelection ,playerName2 , passWord2, menuCounter)
            login(menuSelection ,playerName1 , passWord, menuCounter, playerName2, passWord2)

    else:
        #register 
        playerName1 = input("please enter Player 1 playerName1 (between 3 to 12 chars, alphaNumeric, no special chars): ")
        passWord = input("please enter password (between 8 to 15 chars, at least 1 upper case, 1 numeric, 1 special char): ")
        register(menuSelection , playerName1 , passWord, menuCounter)

def login(menuSelection, user1 , pw, menuCounter, playerName2, passWord2):
    user2 = playerName2
    print()
    print()
    #print("you have arrived at the login function, with playerName1= " + user1 + " and your password = " + pw + " ,user2 is: " + user2)
    print()
    if validateUserInUserFile(user1) == True:
        if validatePWInUserFile(menuSelection , pw, menuCounter) == True:
            if playerTwoLoginUser(playerName2) == True:
                if playerTwoLoginPw(passWord2):
                    print("************login credentials are correct, you are now logged in************")
                    print()
                    playGame(menuSelection, user1, user2)

                    #quitOrPlay(menuSelection, user1, user2)
    else: 
        messageTransfer ="######## " + user1+ " does not exists, please select how to proceed #######"
        print()
        quit2(messageTransfer, menuSelection, menuCounter)

def playerTwoLoginUser(playerName2):#trying to login for second player
    playerName1 = playerName2
    inFile = False
    print("welcome to the player two login function()")
    print()

    f = open("playersFile.txt" ,"r")
    fl = f.readlines()

    #user name search
    for x in fl:
       if playerName1 == x.split(" ")[0]:
           inFile = True

    if inFile == True:
        print("**playerName1 matches!**")
        print()
        return True

    else:
        print(playerName1 + " - **There is no match**")
        print()
        return False

def playerTwoLoginPw(passWord2):#trying to login for second player
    passWord = passWord2
    inFile = False


    f = open("playersFile.txt" ,"r")
    fl = f.readlines()

    #password search
    for x in fl:
       if passWord == x.split()[1]:
           inFile = True

    if inFile == True:
        print("**pw matches!**")
        print()
        return True

    else:
        print(passWord + " - **There is no match**")
        print()
        return False

def register(menuSelection, user1, pw, menuCounter):

    if validateUserInUserFile(user1) == True:
        print("*** User1 name already exists please select a different user1 name.***")
        messageTransfer = "######## A problem has occured while trying to register, please select how to proceed #######"
        quit2(messageTransfer, menuSelection, menuCounter )
    else:
        print("**playerName1 is allowed, moving on**")
        validateUserChars(menuSelection, user1, pw, menuCounter)

def validateUserInUserFile(userNamw):


    #check if file exists
    if os.path.exists("playersFile.txt"):
        fileValid = True
    else:
        print ("The users file does not exist")
        fileValid = False

    #dirNamePlayer = "Players_directory"

    #open file and read playerName1
    if fileValid == True:
        playerName1 = userNamw
        inFile = False
        f = open("playersFile.txt" ,"r+")
        fl = f.readlines()

        #user1 name search
        for x in fl:
            if playerName1 == x.split(" ")[0]:
                inFile = True
        if inFile:
            print("**playerName1 matches!**")
            print()
            fileValid = True
            return fileValid
        else:
            print(playerName1 + " - **There is no match**")
            print()
            fileValid = False
            return fileValid
        f.close()

def validatePWInUserFile(menuSelection, PW, menuCounter):
    #set valid user1 to true as you will only get here if the playerName1 is valid
    validUser = True

    if validUser == True:
        pw = PW
        PWinFile = False
        f = open("playersFile.txt","r")
        fl = f.readlines()
        #PW name search
        for x in fl:
            if pw == x.split()[1]:
                print()
                print("**Password matches!**")
                print()
                PWinFile = True

        if PWinFile:
            print()
            print( "***There is a match of user and pw!***")
            print()
            fileValid = True
            return fileValid
        else:
            print()
            print( "***playerName1 and password do not match*** ")
            print()
            messageTransfer = "######## A problem has occured while trying to login, please select how to proceed #######"
            quit2(messageTransfer, menuSelection, menuCounter)
        f.close()
    
def validateUserChars(menuSelection, user1, pw, menuCounter):
    playerName1 = user1
    password = pw

    if (validateUserCharsLength(playerName1) == True):
        if validateUserCharsStart2Chars(playerName1) == True:
            if validateUseralnum(playerName1) == True:
                print()
                #print("**playerName1 login credentials are correct, checking pw**")
                print()
                validatePWChars(menuSelection ,user1, password, menuCounter)
                print()
            else:
                messageTransfer = "######## A problem has occured while trying to register, please select how to proceed #######"
                quit2(messageTransfer, menuSelection, menuCounter)
        else:
            messageTransfer = "######## A problem has occured while trying to register, please select how to proceed #######"
            quit2(messageTransfer, menuSelection, menuCounter)

    else: 
         messageTransfer = "######## A problem has occured while trying to register, please select how to proceed #######"
         quit2(messageTransfer, menuSelection, menuCounter)

def validateUserCharsLength(playerName1):
    user1 = playerName1
    print()
   # print("arrived at function validateUserCharsLength function")
    print()
    #print (len(user1))

    #more than 2 less than 12
    if len(user1) >= 2:
        if len(user1) <= 12:
            return True
    else:
        print("***Your playerName1 must be between 2 and 12 characters.***")
        print()
        return False

def validateUserCharsStart2Chars(playerName1):
    user1 = playerName1
    #print("arrived at function validateUserCharsStart2Chars function")
    print()

    
    if user1[0:2].isalpha():
        print()
        return True
    else:
        print("***The first two characters of the playerName1 must be letters.***")
        print()
        return False

def validateUseralnum(playerName1):
    user1 = playerName1


    if user1.isalnum() == True:
        return True
    else:
        print("***The playerName1 must consist of both letters and numbers.***")
        print()
        return False




def validatePWChars(menuSelection, user1 , pw, menuCounter):
    password = pw
    print()
    dirNamePlayer ="Players_directory"

    if validatePWLength(pw) == True: #tested working
        if validatePWOneDigit(pw) == True: #testd working
            if validatePWUpperCase(pw) == True: #tested working
                if validatePWAlphaNumeric(pw) == False: #testd working
                    #add special character validation?
                    print("**Password credentials validated returning to ...**")
                    print()
                    #test function to test that all logic is correct
                    f = open(dirNamePlayer + "/playersFile.txt" , "a")
                    f.write("\n")
                    f.write ( user1 + " " +password)
                    f.close()
                    registerPlayerTwo(menuSelection, user1, password, menuCounter)
                    #playerTwoRegister(menuSelection, user1, password, menuCounter)
                    #quitOrPlay(menuSelection)
                    print()

                else:
                     messageTransfer = "######## A problem has occured while trying to register, please select how to proceed1 #######"
                     quit2(messageTransfer, menuSelection, menuCounter)
            else: 
                messageTransfer = "######## A problem has occured while trying to register, please select how to proceed 2#######"
                quit2(messageTransfer, menuSelection, menuCounter)
        else:
            messageTransfer = "######## A problem has occured while trying to register, please select how to proceed 3#######"
            quit2(messageTransfer, menuSelection, menuCounter)
    else: 
         messageTransfer = "######## A problem has occured while trying to register, please select how to proceed 4#######"
         quit2(messageTransfer, menuSelection, menuCounter)


    


def validatePWLength(pw):
    password = pw
     #check password is less than 12 and more than 8 characters
    if len(password) >= 8:
        if len(password) <= 12:
            print()
            return True
    else:
        print("***The password must be between 8 and 12 characters long.***")
        print()
        return False

def validatePWOneDigit(pw):
    password = pw
    #print("hello one digit")
    digitYN = False

    for digit in password:
        if digit.isdigit():
           # print("@@@@@@@@@@@ letter is DIGIT @@@@@@@@@ " + digit)
            digitYN = True

    
    #print ("after finding digit, ahowing now ")
    if digitYN == True:
        print()
        return True
    else:
        print("***The password must contain at least 1 digit.***")
        print()
        return False

def validatePWUpperCase(pw):
    password = pw
    upper = False
    for letter in password:
        if letter.isupper():
            #print("@@@@@@@@@@@ letter is upper @@@@@@@@@ " + letter)
            upper = True
            break
    
    if upper == True:
        print()
        return True
    else:
        print("***The password must contain at least 1 upper case letter.***")
        print()
        return False

def validatePWAlphaNumeric(pw):
    password = pw

    if password.isalnum() == True:
        return True
    else:
        print("***The password is not alpha numeric - it is ok***")
        print()
        return False

#test function to test that all logic is correct
def codeLogicCorrect():
    print("*********you made it!***********")
    exit()

def registerPlayerTwo(menuSelection, user1, password, menuCounter):
    print("would you like to register a second player? enter 'Y' for yes or 'N' for no")

    registerChoice = input(" please make your decision: ")

    if registerChoice.upper() == "Y":
        playerTwoRegister(menuSelection, user1, password, menuCounter)

    elif registerChoice.upper() == "N":
        userAndPasswordInput("login", menuCounter)





def playerTwoRegister(menuSelection, user1, passWord, menuCounter):
    print("****Please register a second person to play the game!****")
    playerName1Reg2 = input("please enter Player two playerName1 (between 3 to 12 chars, alphaNumeric, no special chars): ")
    passWordReg2 = input("please enter password (between 8 to 15 chars, at least 1 upper case, 1 numeric, 1 special char): ")

    if (validateUserTwoCharsLength(playerName1Reg2) == True):
        if validateUserTwoCharsStart2Chars(playerName1Reg2) == True:
            if validateUserTwoalnum(playerName1Reg2) == True:
                validatePWCharsUserTwo(menuSelection ,user1, playerName1Reg2, passWordReg2, menuCounter)
            else:
                messageTransfer = "######## A problem has occured while trying to register, please select how to proceed #######"
                quit2(messageTransfer, menuSelection, menuCounter)
        else:
            messageTransfer = "######## A problem has occured while trying to register, please select how to proceed #######"
            quit2(messageTransfer, menuSelection, menuCounter)

    else: 
         messageTransfer = "######## A problem has occured while trying to register, please select how to proceed #######"
         quit2(messageTransfer, menuSelection, menuCounter)
    #quitOrPlayReg(menuSelection, user1, passWord, playerName1Reg2, passWordReg2)

def quitOrPlayReg(menuSelection, user1, playerName1Reg2, passWordReg2):
    menuOption = menuSelection
    user2 = playerName1Reg2
    print("Player 1 is: "+ user1, ", and Player 2 is: "+ user2)
    print()
    print("***would you like to play game or quit '1' to play and 'q' to quit***")
    userInput = input("please make a selection: ")

    if userInput == "1":
        playGame(menuOption, user1, user2)
    if userInput.lower == "q":
        message = "quiting program, goodbye"
        quit(message)#add quit 2 function option
    else:
        print("******Error: wrong input, please select between '1' or 'q' ")
        quitOrPlayReg(menuSelection, user1, playerName1Reg2, passWordReg2)


def validateUserTwoCharsLength(playerName1Reg2):
    user1 = playerName1Reg2
    print()
   # print("arrived at function validateUserCharsLength function")
    print()
    #print (len(user1))

    #more than 2 less than 12
    if len(user1) >= 2:
        if len(user1) <= 12:
            return True
    else:
        print("***Your playerName1 must be between 2 and 12 characters.***")
        return False

def validateUserTwoCharsStart2Chars(playerName1Reg2):
    user1 = playerName1Reg2
    print()
  
    
    if user1[0:2].isalpha():
        print()
        return True
    else:
        print("***The first two characters of the playerName1 must be letters.***")
        print()
        return False

def validateUserTwoalnum(playerName1Reg2):
    user1 = playerName1Reg2


    if user1.isalnum() == True:
        print()
        return True
    else:
        print("***The playerName1 must consist of both letters and numbers.***")
        print()
        return False

def validatePWCharsUserTwo(menuSelection ,user1, playerName1Reg2, passWordReg2, menuCounter):
    menuCounter = menuSelection
    user2 = playerName1Reg2
    password = passWordReg2
    dirNamePlayer ="Players_directory"
    if validatePWLengthUserTwo(passWordReg2) == True: #tested working
        if validatePWOneDigitUserTwo(passWordReg2) == True: #testd working
            if validatePWUpperCaseUserTwo(passWordReg2) == True: #tested working
                if validatePWAlphaNumericUserTwo(passWordReg2) == False: #testd working
                    print("**Password credentials validated returning to ...**")
                    print()
                    #test function to test that all logic is correct
                    f = open(dirNamePlayer +"/playersFile.txt" , "a")
                    f.write("\n")
                    f.write (playerName1Reg2 + " " +passWordReg2)
                    f.close()
                    playGame(menuSelection, user1, user2)
                    print()

                else:
                     messageTransfer = "######## A problem has occured while trying to register, please select how to proceed1 #######"
                     quit2(messageTransfer, menuSelection, menuCounter)
            else: 
                messageTransfer = "######## A problem has occured while trying to register, please select how to proceed 2#######"
                quit2(messageTransfer, menuSelection, menuCounter)
        else:
            messageTransfer = "######## A problem has occured while trying to register, please select how to proceed 3#######"
            quit2(messageTransfer, menuSelection, menuCounter)
    else: 
         messageTransfer = "######## A problem has occured while trying to register, please select how to proceed 4#######"
         quit2(messageTransfer, menuSelection, menuCounter)

def validatePWLengthUserTwo(passWordReg2):
    password = passWordReg2
     #check password is less than 12 and more than 8 characters
    if len(password) >= 8:
        if len(password) <= 12:
            print("**debug: Password length correct**")
            print()
            return True
    else:
        print("***The password must be between 8 and 12 characters long.***")
        print()
        return False

def validatePWOneDigitUserTwo(passWordReg2):
    password = passWordReg2
    #print("hello one digit")
    digitYN = False

    for digit in password:
        if digit.isdigit():
           # print("@@@@@@@@@@@ letter is DIGIT @@@@@@@@@ " + digit)
            digitYN = True

    
    #print ("after finding digit, ahowing now ")
    if digitYN == True:
        print()
        return True
    else:
        print("***The password must contain at least 1 digit.***")
        print()
        return False

def validatePWUpperCaseUserTwo(passWordReg2):
    password = passWordReg2
    upper = False
    for letter in password:
        if letter.isupper():
            #print("@@@@@@@@@@@ letter is upper @@@@@@@@@ " + letter)
            upper = True
            break
    
    if upper == True:
        print()
        return True
    else:
        print("***The password must contain at least 1 upper case letter.***")
        print()
        return False

def validatePWAlphaNumericUserTwo(passWordReg2):
    password = passWordReg2

    if password.isalnum() == True:
        print()
        return True
    else:
        print("***The password is not alpha numeric - it is ok***")
        print()
        return False

def quit2(message, arrivedFrom, menuCounter):
    if menuCounter <5:
        messageTransferred = message
        print()
        print (messageTransferred)
        print (" to go back to  " + arrivedFrom + ", please enter 1 , or q for quit")
        print()
        quitResponse = input("Please make your selection: ")
        print()
    else:
        print("***You have made too many attempts- exiting the program***")
        exit()

    if quitResponse == "1":

        if arrivedFrom == "menuSelect":
            print("leaving quit2 **********menu counter = " + str(menuCounter) + "*********************")
            mainNav(menuCounter)

        if arrivedFrom == "login":
            arrivedFrom="login"
            menuCounter = menuCounter + 1
            userAndPasswordInput(arrivedFrom, menuCounter)

        if arrivedFrom == "register":
            arrivedFrom="register"
            menuCounter = menuCounter + 1
            userAndPasswordInput(arrivedFrom, menuCounter)
    
    else: 
            exit()



def displayRulesAndPlay(menuOption):
    menuSelection = menuOption
    print()
    #-------------------------
        #sleep(4)
    os.system('cls')
    print ("#" * 80)
    print("#" * 10 + " " * 60 + "#" * 10)
    print("#" * 10 + "             Tariq's prisioners Dilema             " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "           scenario and rules of the game          " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                      A. scenario                  " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  You are both people who have committed a crime,  " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  and the police are questioning you in seperate rooms.  " + " " * 3 + "#" * 10 )
    print("#" * 10 + "  you have two choices between you:                " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  option1: 'co-operate' and not talk to the police " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  option2: 'defect' and turn on your friend        " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  option2: 'defect' and turn on your friend        " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  however, if one person helps the police,         " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  they can get a shorter jail sentence which is tempting." + " " * 3 + "#" * 10 )
    print("#" * 10 + "  if both people help the police they both get a reduced sentence, " + " " * 1 + "#" * 2 )
    print("#" * 10 + "  but not as short as they would if they turned on their friende   " + " " * 1 + "#" * 2 )
    print("#" * 10 + "  and finally if both people dont help the police -" + " " * 9 + "#" * 10 )
    print("#" * 10 + "  they will both get an even longer sentence       " + " " * 9 + "#" * 10 )

    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + " the screen will freeze now for 10 seconds for easy reading" + " " * 1 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )

    sleep(10)
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "                B. things to consider:             " + " " * 9 + "#" * 10 )
    print("#" * 10 + "- will your friend turn on you in order to not go to jail?  " + " " * 5 + "#" * 9 )
    print("#" * 10 + "- should you turn on your friend to try and save yourself  " + " " * 5 + "#" * 9 )
    print("#" * 10 + "- can you trust that your friend have your best intrests at heart? " + " " * 1 + "#" * 2 )
   
    print("#" * 10 + "  in order to play this scenario as a game the sentences - " + " " * 1 + "#" * 10 )
    print("#" * 10 + "                   -have been changed to points            " + " " * 1 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  the aim of the game is to end the game with the most-" + " " * 5 + "#" * 10 )
    print("#" * 10 + "  -points and higher points are awarded to those who turn-" + " " * 6 + "#" * 6)
    print("#" * 10 + "   -on the other player" + " " * 41 + "#" * 6)
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  this is done in order to test the trust of both players- " + " " * 5 + "#" * 6 )
    print("#" * 10 + "           -by tempting them with deception " + " " * 16 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )

    sleep(10)
    print("#" * 10 + "                C. how to play:                    " + " " * 9 + "#" * 10 )
    print("#" * 10 + "  -Whoever starts first must choose between 2 options:   " + " " * 3 + "#" * 10 )
    print("#" * 10 + "                               'co-operate' or 'defect'  " + " " * 3 + "#" * 10 )

    print("#" * 10 + "  -the player who starts second must do the same   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "-you will be scored based on the decisions made by eachother:" + " " * 1 + "#" * 8 )
    print("#" * 10 + "     - if both players defect they both receive 1 point    " + " " * 1 + "#" * 10 )
    print("#" * 10 + "     - if both players co-operate they both receive 2 point" + " " * 1 + "#" * 10 )
    print("#" * 10 + "     - if player one co-operates while player two defects, " + " " * 1 + "#" * 10 )
    print("#" * 10 + "              player two receives 3 points " + " " * 17 + "#" * 10 )
    print("#" * 10 + "                                                   " + " " * 9 + "#" * 10 )
    print("#" * 10 + "     - if player two co-operates while player one defects, " + " " * 1 + "#" * 10 )
    print("#" * 10 + "              player one receives 3 points " + " " * 17 + "#" * 10 )


    print("#" * 10 + " " * 60 + "#" * 10)
    print ("#" * 80 + "\n")

    #turn back on after testing
    #sleep(20)




    #--------------------
 

    if menuSelection == "playGame" or "login":
        return True

    else:
        message = "message from game"
        quit(message)


main()

            
  