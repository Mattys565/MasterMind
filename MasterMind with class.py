import random
import os

class MasterMind:
    def __init__(self):
        self.ball_nb = 4
        self.round_nb = 12
        self.colors = {
                        'R' : '🔴',
                        'O' : '🟠',
                        'G' : '🟢',
                        'Y' : '🟡',
                        'B' : '🔵',
                        'P' : '🟣'
                    }
        
        self.scores = {
                    'B':'⚫', #Good color and good position
                    'W' : '⚪' #Good color but wrong position
                    }
        
        self.historical = [[],[]]
        self.solution = self.solution_generator()

    
    def solution_generator(self):
        return random.choices(sorted(self.colors.keys()), k=self.ball_nb) #Generate a solution and we allow the doubles

    def player_colors(self):

        test_color = input("Type the colors you want to try (e.g., RGPY): ").upper()

        if len(test_color) !=  self.ball_nb: # Check the number of character
            print('ERROR: Only 4 character are expected')
            return self.player_colors()
        
        for letter in test_color: # Check if the character is allowed
            if(letter in self.colors):
                continue
            else: 
                print('ERROR: You typed a wrong character')
                return self.player_colors()

        return list(test_color) # return a list containing each color that we want to try



    def compare_color(self,test_color):

        final_score = [] 
        sol = self.solution.copy() 
        idx_already_treated =[] # 'good position and good color' needs to be count once

        for idx, color in enumerate(test_color):

            if (color in self.solution) and (color == self.solution[idx]): # Here, we check if the position AND the color is good

                final_score.append(self.scores['B'])
                sol.remove(color) 
                idx_already_treated.append(idx)
                continue
        
        for idx,color in enumerate(test_color): # Here, we check only if the color is good
            if idx in idx_already_treated: continue

            elif(color in sol):
                final_score.append(self.scores['W'])
                sol.remove(color)
                
            else: final_score.append(' ')

        order = {'⚫': 0, '⚪': 1, ' ': 2}
        final_score.sort(key=lambda x: order[x]) # We must not know which color corresponds to which score, so we sort in an arbitrary order the final score
        return final_score
    
    def main_display(self): # We display the rules and the main presentation

        print('     '*4,'⚫ MasterMind ⚫')
        print('='*60)
        print('🟠 Rules: \n', '   - Type the first letter of the color you want to test:')
        for letter,emoji  in self.colors.items():
            print('    '*3,letter,' ➔  ',emoji)
        
        print('\n   - You are assigned a score for each attempt:')
        print('   '*3,'- Good Position and Good color: ','  ➔  ',self.scores['B'])
        print('   '*3,'- Wrong Position and Good color: ',' ➔  ',self.scores['W'])
        print('\n   - You win when your score is ',self.scores['B']*4)
        print('='*60)


    def round_display(self): # At each round we want to display the historical
            for i in range(len(self.historical[0])):
                tested_color = []
                for j in range( self.ball_nb ):
                    tested_color.append(self.colors[self.historical[0][i][j]])
                print(i,'  ' ,''.join(tested_color),' | ',"".join(self.historical[1][i]))
    
    def play(self):

        self.main_display()
        i=0
        while i <= self.round_nb:

            if i==self.round_nb:
                print('='*25,'You Lost !','='*25)
                break

            test_color = self.player_colors()
            os.system('cls') 
            self.main_display()
            score = self.compare_color(test_color)
            self.historical[0].append(test_color)
            self.historical[1].append(score)
            self.round_display()

            if score == list(self.scores['B']*4):
                print('='*25,'Victory !!','='*25)
                break
            i+=1

        print('='*60)

        replay = input('Do you want to play again? (yes/no)  ').upper()
        if replay == 'YES':
            self.play()
        elif replay == 'NO':
            print('Tchao !')
        else: print('That was not in your choices !!')



if __name__ == '__main__':
    game = MasterMind()
    game.play()