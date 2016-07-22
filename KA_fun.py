from random import choice 

print "Hi I want to play Rock, Paper Scissiors!"
print "Ready? Let's play best out of three!"
print "Make your move! (r,p, s, or q to quit)"

move = raw_input ("Enter: ")

def rock_paper_scissors(move, my_score, your_score):
	x = choice ("rps")
	if x == "r" and move == "r":
		print "I play Rock."
		print "We have a tie!"
		return my_score, your_score
	elif x == "r" and move == "s":
		print "I play rock!"
		print "Sorry, but I won this round!"
		return my_score+1, your_score 
	elif x == "r" and move == "p":
		print "I play rock!"
		print "Oh man, you win this round :(" 
		return my_score, your_score+1
	elif x == "p" and move == "r":
		print "I play paper!"
		print "Sorry, but I won this round."
		return my_score+1, your_score
	elif x == "p" and move == "p":
		print "I play paper!"
		print "We have a tie!"
		return my_score, your_score
	elif x == "p" and move == "s":
		print "I play paper!"
		print "Oh man, you win this round:("
		return my_score, your_score+1
	elif x == "s" and move == "r":
		print "I play Scissors."
		print "Oh man, you win this round ;("
		return my_score, your_score+1
	elif x == "s" and move == "p":
		print "I play Scissors!"
		print "Sorry, but I won this round."
		return my_score+1, your_score
	elif x == "s" and move == "s":
		print "I play scissors!"
		print "We have a tie!"
		return my_score, your_score
	elif move == "q":
		print "GAME OVER!"
		print "Final score is: You: %d, Me :%d" % (your_score, my_score)

my_score = 0
your_score = 0


while move != "q":
	my_score, your_score = rock_paper_scissors(move, my_score, your_score)
	print my_score, your_score
	move = raw_input ("Enter: ")
	








