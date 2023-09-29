# define the player class 
class player:
  def play(self):
    print("the player is playing cricket.")
# define the batsman class,derived from the player 
class batsman(player):
    def play (self):
      print("the batsman is batting.")
# define the derived class bowler
class bowler(player):
    def play(self):
      print ("the bowler is bowling.")
#create object of batsman and bowler classes 
batsman=batsman()
bowler=bowler()
#call the play() method for each object 
batsman.play()
bowler.play()
            