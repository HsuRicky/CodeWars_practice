# https://www.codewars.com/kata/5dfd129673aa2c002591f65d
def calculate_expected_value(game):
    data = game[1]
    expected_value = sum(map(lambda x: x[0] * x[1], data))
    return expected_value

def find_best_game(games):
    best_game = None
    best_expected_value = float('-inf')

    for game in games:
        expected_value = calculate_expected_value(game)
        if expected_value > best_expected_value:
            best_game = game[0]
            best_expected_value = expected_value

    return best_game


        


# g1 = ("Breakeven Steven", ((0.5, 20), (0.5, -20)))
# g2 = ("Go big or go home", ((0.99, -10), (0.01, 980)))
# g3 = ("Steady Eddy", ((0.51, -10), (0.49, 10)))
# g4 = ("The staircase", ((0.75, -100), (0.10, 100),
#                             (0.05, 200),(0.05, 300),
#                             (0.05, 400)))

# print(find_best_game((g1, g2)))
# print(find_best_game((g1, g2, g3, g4)))
# print(find_best_game((g2, g3)))
# print(find_best_game((g2, g3, g4)))
# print(find_best_game((g3, g4)))