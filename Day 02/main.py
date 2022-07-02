print(8 / 3)
print(int(8 / 3))

#round operation
print(round(8 / 3, 2))
print(round(2.66666666, 2))

#floor operation
print(8 // 3)

#type of below expression will be float
print(type(8 / 3))
#type of below expression will be int
print(type(8 // 3))

score = 0
#shorthand expression for score = score + 1
score += 1
#shorthand expression for score = score - 1
score -= 1

#int datatype
score = 2
#float datatype
height = 1.68
#boolean datatype
isWinning = True

#normal print expression
print("Your score is " + score + ", your height is " + height + ", you are winning is " + isWinning)
#F-string
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
