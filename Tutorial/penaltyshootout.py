import random

class PenaltyShooter:
    def __init__(self, shooting):
        if ( 1 <= shooting <= 10 ):
            self.shooting = shooting
        else:
            print("ERROR: skill value must be in the range 1-10")
            print("Set to default: 2")
            self.shooting = 2

    def shoot(self, goal):
        goal.simulate( self )


class GoalKeeper:
    def __init__(self, defence):
        if ( 1 <= defence <= 10 ):
            self.defence = defence
        else:
            print("ERROR: skill value must be in the range 1-10")
            print("Set to default: 2")
            self.defence = 2


class Goal:
    def __init__(self, goalkeeper):
        self.gk = goalkeeper

    def simulate(self, shooter):
        goalchance = ["goal!" for i in range( int(shooter.shooting)*2 )]
        savedchance = ["saved" for i in range( int(self.gk.defence) )]

        chances = goalchance + savedchance

        result = random.choice( chances )
        print("result: " + result)
        

steven_gerrard = PenaltyShooter( 9 )
iker_casillas = GoalKeeper( 8 )
anfield_goal = Goal( iker_casillas )

# Simulation:
  #- steven_gerrard.shoot( anfield_goal )
  #- steven_gerrard.shoot( anfield_goal )
  #- steven_gerrard.shoot( anfield_goal )
