#Manuel Duran 1584885
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # percentage method
    def get_win_percentage(self):
        # calculating the percentage
        percentage = self.team_wins / (self.team_wins + self.team_losses)

        # returns the answer back up
        return percentage
# main code
if __name__ == '__main__':
    team = Team()
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    # printing
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')