################### Scope ####################

# Global vs Local Scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink():
  drinks_count = 2
  print(drinks_count)

drink()
# print(drinks_count)

# Global Scope

player_health = 10

def drink():
  drinks_count = 2
  print(player_health)

drink()
