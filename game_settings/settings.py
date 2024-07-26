''' Game general functions '''

settings_terrain = {
    'desert': 30,
    'forest': 30,
    'swamp': 20,
    'field': 20,
}

def win_condition(player):

  has_won = False
  current_score = 0
  try:  
    if player.res6 >= 30:
      has_won = True
    elif player.res1 + player.res2 > player.res3 >= 2:
      has_won = True
    else:
      has_won = False
  except:
    print(Exception)
  else:
    return has_won