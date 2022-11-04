'''
    An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking , so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

    climbingLeaderboard has the following parameter(s):

    int ranked[n]: the leaderboard scores
    int player[m]: the player’s scores

    Returns
    int[m]: the player’s rank after each new score
'''

def climbingLeaderboard(ranked, player):
    '''
        Tracks the ranking of a player on the leaderboard

        :param ranked: <list> List of the ranked players
        :param player: <list> List of player scores after each game

        :return: <list> Rank of player after each game
    '''

    reverse_sorted_ranked = sorted(list(set(ranked)), reverse=True)
    ranks_over_games = []

    for score in range(len(player)):
        for rank in range(len(reverse_sorted_ranked)):
            if player[score] < reverse_sorted_ranked[-1]:
                reverse_sorted_ranked.append(player[score])
                ranks_over_games.append(len(reverse_sorted_ranked))
                break
            elif player[score] == reverse_sorted_ranked[-1]:
                reverse_sorted_ranked.insert(-1, player[score])
                ranks_over_games.append(len(reverse_sorted_ranked))
                break
            elif player[score] > reverse_sorted_ranked[0]:
                reverse_sorted_ranked.insert(0, player[score])
                ranks_over_games.append(1)
                break
            elif player[score] == reverse_sorted_ranked[0]:
                reverse_sorted_ranked.insert(0, player[score])
                ranks_over_games.append(1)
                break
            elif player[score] == reverse_sorted_ranked[rank]:
                reverse_sorted_ranked.insert(rank, player[score])
                ranks_over_games.append(rank + 1)
                break
            elif player[score] < reverse_sorted_ranked[rank]:
                continue
            else:
                reverse_sorted_ranked.insert(rank, player[score])
                ranks_over_games.append(rank + 1)
                break
    return ranks_over_games

a = climbingLeaderboard([100,90,90,80], [70,80,105])
print(a)
b = climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120])
print(b)
