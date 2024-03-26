# main.py
# Name: Harsh Shah
# email: shahh4@mail.uc.edu
# Assignment Number: Midterm Exam
# Due Date: 03/07/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Solving a game so it won't crash when project is run.
# Anything else that's relevant: Imported project from Github but it crashes. 

from videoGamePackage.videoGame import *


if __name__ == "__main__":
    play()
    totalPlays = 1000
    won = 0
    lost = 0
    
    for i in range(0, totalPlays):
        
        if play():
            won = won + 1
        else:
            lost = lost + 1
            
        try:
            play() 
        except Exception:
            None
        
        percentage_won = (won/totalPlays)
        #round(percentage_won,2)
        print("Total plays: " ,totalPlays, " , won = ",won, " , lost = ", lost, " percentage won = " , percentage_won) 

        
      
            

    
