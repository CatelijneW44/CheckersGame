#move = row, column

### USE lATER

class style: #https://stackoverflow.com/questions/24834876/how-can-i-make-text-bold-in-python
   BOLD = '\033[1m'
   END = '\033[0m'

#USE LATER
#RETRY WORK

class checkers(object):
  
  def __init__(self):
    # Initialize board (list), points for both players
    boardList = [
  ["1", " ", "1", " ", " ", " ", "1", " "],
  [" ", "1", " ", "2", " ", " ", " ", "1"],
  ["1", " ", "1", " ", "1", " ", "1", " "],
  [" ", " ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", "1", " ", " ", " "],
  [" ", "2", " ", "2", " ", "2", " ", "2"],
  ["2", " ", "2", " ", "2", " ", "2", " "],
  [" ", "2", " ", "2", " ", "2", " ", "2"]]
    
    self.board = boardList
    self.pointsWhite = 0
    self.pointsBlack = 0
    
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
      
  def getMoves(self, move):
    #split string move into usable integer values representing Column and Row
    return int(move[0]), int(move[1])-1
  
  def getPieces(self, piece):
    #split string piece into usable integer values representing Column and Row
    return int(piece[0]), int(piece[1])-1
    
  def getOpponent(self, player):
    #identify opponent
    if player == "1":
      return "White", "2"
    elif player == "2":
      return "Black", "1"
  
  def movePossible(self, move, piece, player):
    #checks legitimacy of move - is the desired space open
    moveR, moveC = self.getMoves(move)
    
    if self.board[-moveR][moveC] == " ":
      return True
    else:
      return False
      
  def validMove(self, move, piece, player):
    #carries out move. player moves to desired place, old place reset to " "
    #board displayed 
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
    
    self.board[-moveR][moveC] = player
    self.board[-pieceR][pieceC] = " "
    self.display()
    
  def negPos(self, player):
    #sub-function to shorten userMove()
    if player == "2":
      return -1
    elif player == "1":
      return 1
    
  def userMove(self, move, piece, competitor):
    #checks legitimacy of user move according to checkers rules
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
    
  
    if competitor == "♔":
      player = "2"
    elif competitor == "♚":
      player = "1"
    else:
      player = competitor
    
    if -pieceR+self.negPos(player) == -moveR and pieceC-1 == moveC or -pieceR+self.negPos(player) == -moveR and pieceC+1 == moveC:
      if self.movePossible(move, piece, player) == True:
        self.validMove(move, piece, competitor)
        return True
        
    else:
      return False
  
  def jumpFunc(self, move, piece, player):
    #assigns points to player jumping, calls on validMove to jump, resets square getting jumped over (" ")
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
    
    if player == "2":
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
  
  def jump(self, move, piece, competitor):
    #checks legitimacy of jump (if there is a player to jump, and if the jump follows checkers rules)
    #allows user to jump again if possible
    
    moveR, moveC = self.getMoves(move)
    pieceR, pieceC = self.getPieces(piece)
    
    if competitor == "♔":
      player = "2"
    elif competitor == "♚":
      player = "1"
    else:
      player = competitor
      
    opponent, opponentInt = self.getOpponent(competitor)
    print type(opponentInt)
    
    if (player == "2" and pieceR >= 7) or (player == "1" and pieceR <=2):
      return False
      
    elif self.board[-pieceR+self.negPos(player)][pieceC-1] == opponentInt and self.board[-pieceR+self.negPosJump(player)][pieceC-2] == " " or self.board[-pieceR+self.negPos(player)][pieceC+1] == opponentInt and self.board[-pieceR+self.negPosJump(player)][pieceC+2] == " ":
      self.jumpFunc(move, piece, competitor)
      print "I ran the JumpFunc"
    else:
      return False

    again = input(style.BOLD +"Would you like to jump again? - only applicable if possible [y/n]"+style.END)
    
    if again == "y":
      piece, move = questions()
      value = self.jump(move, piece, player)
      
    elif again == "n":
      print "\n PLAYER", opponent.upper(), "MOVE \n"
  
  def king(self, move, piece, player):
    #trusts player is king, makes the move
    self.userMove(move, piece, player)
  
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
    moveR, moveC = self.getMoves(move)
    
    if player == "2" and self.board[-moveR][moveC] == "♔":
      self.king(move, piece, "♔")
      return True
    elif player == "1" and self.board[-moveR][moveC] == "♚":
      self.king(move, piece, "♚")
      return True
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
  #dictates rounds + who's turn it is
  numberRound = 1
  puttingOff = 1
  
  board = checkers()

  board.display()

  gameIntro()
  
  while board.pointsWhite < 12 or board.pointsBlack < 12: #while any move can be made
    piece, move = questions()
    
    if numberRound%2 != 0:
      player = "2"
    else:
      player = "1"
      
      
    value = board.userMove(move, piece, player)
    valueJump = board.jump(move, piece, player)
    if value == False and valueJump == False:
      while value == False:
        piece, move = questions()
        value = board.userMove(move, piece, player)
        
    board.isKing(move, piece, player)
      
    if move[0] == "8" or move[0] == "1":
      board.convertKing(move, player)
    
    
    
    numberRound += 1
  
# M A I N 
rounds()
