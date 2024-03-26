# videoGame.py
# main.py
# Name: Harsh Shah
# email: shahh4@mail.uc.edu
# Assignment Number: Midterm Exam
# Due Date: 03/07/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Solving a game so it won't crash when project is run.
# Anything else that's relevant: Imported project from Github but it crashes. 


if __name__ != "__main__":
    import random
    def play():
        '''
        returns True if you won, False if you lost 
        '''
        if random.randint(0,100) == 10:
            raise Exception("Game Crashed")
        return random.choice([True, False])