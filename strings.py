# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_0, str(goal_0), scorer_1, str(goal_1)
report = f'{scorer_0} scored in the {goal_0}nd minute'f'\n{scorer_1} scored in the {goal_1}th minute'

print(scorers)
print(report)

player = 'Ruud Gullit'
first_name = player.find(' ')
last_name = player[5:11]

'''ik heb uren gegoogled en verdwaald geraakt in tutorial hell, 
   ik kan helaas nergens vinden hoe ik voor last_name zoek vanaf de spatie (' ') tot het laatste karakter 
   of hoe ik .find .len .[] in 1 regel mag en kan gebruiken'''

last_name_len = len(last_name)
name_short = player[0] + '. ' + player[5:11]
chant = (player[0:4]+'! ')*first_name
good_chant = chant.find(' ') != ' '
print(player)
print(first_name)
print(last_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)

''' Is het mogelijk dat men het antwoord geeft, of laat zien wat er bij last_name_len en scorers zou moeten staan
    Want ik zit nu ruim een week vast op een zeer kleine opdracht en ik begrijp gewoon niet wat er nu van me gevraagd
    word daar ik wel het idee heb dat ik de stof voldoende begrijp en toepas'''
