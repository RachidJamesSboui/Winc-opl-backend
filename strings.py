# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)
report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'

print(scorers)
print(report)

player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name = player[player.find(' '):-1]
last_name_len = len(last_name)

print(first_name)
print(last_name)
print(last_name_len)

'''heb hier dus geprogrammeerd dat ik de lengte van de achternaam wil, -1
want de spatie wordt altijd meegeteld'''

name_short = player[0] + '. ' + player[5:11]

chant = (player[0:4]+'! ')*4
print(chant)

good_chant = chant[-1] != ' '
print(good_chant)
