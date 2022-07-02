print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))

if height >= 120:
  print("You can ride the rollercoaster.")
  age = int(input("Enter your age: "))
  if age < 12:
    print("You need to pay ₹600/-")
  elif age <= 18:
    print("You need to pay ₹800/-")
  else:
    print("You need to pay ₹1200/-")
else:
  print("Sorry! The minimum height required to ride the rollercoaster is 120cm.")
