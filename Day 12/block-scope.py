# There is no Block Scope

game_level = 3

def create_enemy():
  enemies = ["Skeleton", "Zombies", "Aliens"]
  if game_level < 5:
    new_enemy = enemies[0]
    
  print(new_enemy)
  
create_enemy()

# print(new_enemy)
