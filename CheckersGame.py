\#move = row, column

### USE lATER

class style: #https://stackoverflow.com/questions/24834876/how-can-i-make-text-bold-in-python
  #Using this bc _____
   BOLD = '\033[1m'
   END = '\033[0m'

class checkers(object):
  
  def __init__(self):
    # Initialize board (list), points for both players
    boardList = [
  [" ", " ", "1", " ", " ", " ", " ", " "],
  [" ", " ", " ", "1", " ", "1", " ", " "],
  [" ", " ", "2", " ", " ", " ", " ", " "],
  [" ", " ", " ", "2", " ", " ", " ", " "],
  [" ", " ", " ", " ", "2", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", "2", " ", " "],
  [" ", "2", " ", " ", "♚", " ", " ", " "]]
    
    self.board = boardList
    self.pointsWhite = 8
    self.pointsBlack = 9
    
  def display(self):
    #displays board in readable and logical way
    print style.BOLD + "\n White Score: " + style.END, self.pointsWhite
    print style.BOLD + "\n Black Score: " + style.END, self.pointsBlack
    c = 8
    row = ""
    space = "  "
    print "\n ", " ", "  1", space, "2", space, "3", space, "4", space, "5", space, "6", space, "7", space, "8\n"
    for i in self.board:
      print c, ":", i, "\n" 
      c -= 1
    print " ", " ", "  1", space, "2", space, "3", space, "4", space, "5", space, "6", space, "7", space, "8"
    
    print "\n"
      
  def getMoves(self, move):
    #split string move into usable integer values representing Column and Row
    return int(move[0]), int(move[1])-1
  
  def getPieces(self, piece):
    #split string piece into usable integer values representing Column and Row
    return int(piece[0]), int(piece[1])-1
    
  def getOpponent(self, player):
    #identify opponent
    if player == "1" or player == "♚":
      return "White", "2"
    elif player == "2" or player == "♔":
      return "Black", "1"
      
  def getKing(self, player):
    #identify opponent's king
    if player == "1" or player == "♚":
      return "♔"
    elif player == "2" or player == "♔":
      return "♚"
  
  def movePossible(self, move, piece, player):
    #checks legitimacy of move - is the desired space open
    moveR, moveC = self.getMoves(move)
    
    if self.board[-moveR][moveC] == " ":
      return True
    else:
      return False
  
  def exception(self, pieceR, pieceC):
    opponent = " "
    opponentInt = " "
    
    if self.board[-pieceR][pieceC] == "♔":
      opponentInt = "1"
      opponent = "Black"
    elif self.board[-pieceR][pieceC] == "♚":
      opponentInt = "2"
      opponent = "White"
    return opponent, opponentInt
    
  def validMove(self, move, piece, player):
    #carries out move. player moves to desired place, old place reset to " "
    #board displayed 
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
    
    opponent, opponentInt = self.exception(pieceR, pieceC)
    
    self.board[-moveR][moveC] = self.board[-pieceR][pieceC]
    self.board[-pieceR][pieceC] = " "
    self.display()
    
    
  def negPos(self, player):
    #sub-function to shorten userMove()
    if player == "2":
      return -1
    elif player == "1":
      return 1

  def checkRangeR(self, piece):
    if piece >= -8 and piece <= -1:
      return True
    else
      return False

  def checkRangeC(self, piece):
    if piece >= 0 and piece <= 7:
      return True
    else
      return False

  def kingJump(self, move, piece, opponentInt, pieceR, pieceC, player):
    for i in range(-1, 2, 2):
      for j in range(-1, 2, 2):
        if (self.checkRangeR(-pieceR+i) and self.checkRangeC(pieceC+j) and self.board[-pieceR+i][pieceC+j] == opponentInt and
            self.checkRangeR(-pieceR+2*i) and self.checkRangeC(pieceC+2*j) and self.board[-pieceR+2*i][pieceC+2*j] == " "):
          self.jumpFunc(move, piece, player)
          return True
    return False

  def userMove(self, move, piece, player):
    #checks legitimacy of user move according to checkers rules
    #returns True if move can/was made, false if move cannot be made
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
    
    if -pieceR+self.negPos(player) == -moveR and pieceC-1 == moveC or -pieceR+self.negPos(player) == -moveR and pieceC+1 == moveC:
      if self.movePossible(move, piece, player) == True:
        self.validMove(move, piece, player)
        return True
        
    else:
      return False
  
  def jumpFunc(self, move, piece, player):
    #assigns points to player jumping, calls on validMove to jump, resets square getting jumped over (" ")
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
    
    if self.board[-pieceR][pieceC] == "2" or self.board[-pieceR][pieceC] == "♔":
      self.pointsWhite += 1
    else:
      self.pointsBlack += 1
      
    self.board[-((moveR+(pieceR)) // 2)][((moveC) + (pieceC))//2] = " "
    self.validMove(move, piece, player)
    
  def negPosJump(self, player):
    #sub-function to shorten jump()
    if player == "2":
      return -2
    elif player == "1":
      return 2
  
  def jump(self, move, piece, player):
    #checks legitimacy of jump (if there is a player to jump, and if the jump follows checkers rules)
    #allows user to jump again if possible, returns False if jump invalid
    
    
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
  
    opponent, opponentInt = self.exception(pieceR, pieceC)
    if opponent == " " and opponentInt == " ": #selection
      opponent, opponentInt = self.getOpponent(player)
    
    if (player == "2" and pieceR >= 7) and self.board[-pieceR][pieceC] != "♔" or (player == "1" and pieceR <=2) and self.board[-pieceR][pieceC] != "♚":
      return False
  
    
    #sequencing
    if self.board[-pieceR][pieceC] == player:
      if (self.board[-pieceR+self.negPos(player)][pieceC-1] == opponentInt and self.board[-pieceR+self.negPosJump(player)][pieceC-2] == " " or
          self.board[-pieceR+self.negPos(player)][pieceC+1] == opponentInt and self.board[-pieceR+self.negPosJump(player)][pieceC+2] == " "): #selection
        self.jumpFunc(move, piece, player)
      elif (self.board[-pieceR+self.negPos(player)][pieceC-1] == self.getKing(player) and self.board[-pieceR+self.negPosJump(player)][pieceC-2] == " " or
          self.board[-pieceR+self.negPos(player)][pieceC+1] == self.getKing(player) and self.board[-pieceR+self.negPosJump(player)][pieceC+2] == " "): #selection
        self.jumpFunc(move, piece, player)
    elif self.board[-pieceR][pieceC] == "♔":
      self.kingJump(move, piece, opponentInt, pieceR, pieceC, player)
    elif self.board[-pieceR][pieceC] == "♚":
      self.kingJump(move, piece, opponentInt, pieceR, pieceC, player)
    else:
      return False

    again = input(style.BOLD +"Would you like to jump again? - only applicable if possible [y/n]"+style.END)
    
    while again == "y": #iteration
      piece, move = questions()
      value = self.jump(move, piece, player)
      return value
  
  def king(self, move, piece, player): #ISSUE WITH HOW IT'S PUTTING IN THE VALUES - MAKES SENSE BUT ANNOYING SMH
    #trusts player is king, makes the move
    if self.userMove(move, piece, player) == False:
      if self.jump(move, piece, player) == False:
        return False
    else:
      return True
  
  def convertKing(self, move, player):
    #convert regular player to king according to checkers rules
    moveR = int(move[0])
    moveC = int(move[1])-1
    
    if player == "2" and moveR == 8:
      self.board[-moveR][moveC] = "♔"
      self.display()
    elif player == "1" and moveR == 1:
      self.board[-moveR][moveC] = "♚"
      self.display()
    
  def isKing(self, move, piece, player):
    #checks to make sure player is a king
    pieceR, pieceC = self.getPieces(piece)
    
    if player == "2" and self.board[-pieceR][pieceC] == "♔":
      return self.king(move, piece, player)
    elif player == "1" and self.board[-pieceR][pieceC] == "♚":
      return self.king(move, piece, player)
    else:
      return False
      
    
def gameIntro():
  #use -> shorten main code
  print style.BOLD +"\n C H E C K E R S   G A M E \n"
  print "Black = 1, White = 2"
  
  print "\n Remember, white begins! \n" + style.END
 
def questions():
  #use -> shorten code
  piece = input("Which piece would you like to move? ex: 32 (row 3, column 2)")
  move = input("Which row and column would you like to move to? ex: 41 (row 4, column 1) ")
  return piece, move
 
def rounds():
  #dictates rounds + who's turn it is, no return value
  numberRound = 1
  
  board = checkers()

  board.display()

  gameIntro()
  
  while board.pointsWhite < 12 and board.pointsBlack < 12: 
    piece, move = questions()
    
    if numberRound%2 != 0:
      player = "2"
    else:
      player = "1"
    
    valueKing = board.isKing(move, piece, player)
    value = board.userMove(move, piece, player)
    valueJump = board.jump(move, piece, player)
    
    if value == False and valueJump == False and valueKing == False:
      while value == False:
        print "\n I N V A L I D  M O V E \n"
        piece, move = questions()
        if valueKing == False:
          value = board.king(move, piece)
        else:
          value = board.userMove(move, piece, player)
      
    if move[0] == "8" or move[0] == "1":
      board.convertKing(move, player)
    
    
    opponent, opponentInt = board.getOpponent(player)
    print "\n PLAYER", opponent.upper(), "MOVE \n"
    
    numberRound += 1
  
  
  if player == "1":
    player = "black"
  elif player == "2":
    player = "white"
  
  print "\n"  
  print "\n", style.BOLD + player.upper(), "HAS WON THE MATCH" + style.END, "\n"
# M A I N 
rounds()

####
# 54 65
# 
# 76 54 jump
# 
# 54 36 jump
# 
# 63 85 jump
# 
# 83 74
# 
# 85 63
# 
# 36 25
# 
# 12 21
# 
# 25 14
# 
# 21 32
# 
# 14 23
# 
# 63 52
# 

# 
