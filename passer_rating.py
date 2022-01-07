def intro():
	print("Passer Rating\n")
	print("Passer rating, or QBR(Quarterback Rating) is a measure of the efficiency of passers, primarily quarterbacks, in gridiron football.\n")
	
	
def rating():
	
	att = int(input("Passes attempted: "))
	comp = int(input("Completed passes: "))
	yds = int(input("Total yards: "))
	td = int(input("Touchdowns: "))
	ints = int(input("Interceptions: "))
	
	a = ((comp / att) - 0.3) * 5.0
	b = ((yds / att) - 3.0) * 0.25
	c = (td / att) * 20.0
	d = 2.375 - ((ints / att) * 25.0)
	
	passer_rating = (((a + b + c + d) / 6.0) * 100.0)
	if passer_rating > 153.5:
		passer_rating = 153.5
	elif passer_rating < 0:
		passer_rating = 0
	else:
		passer_rating = passer_rating
	
	print("Passer Rating is ", round(passer_rating, 1))
		
def main():
	intro()
	rating()
		
if __name__ == '__main__':
	main()
