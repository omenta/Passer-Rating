comp = 0
att = 1 # Attempted passes can't be zero.
yds = 0
td = 0
ints = 0 


#passer_rating = (((a + b + c + c) / 6) * 100)

def intro():
	print("Passer rating, or QBR(Quarterback Rating) is a measure of the efficiency of passers, primarily quarterbacks, in gridiron football.")
	
def inputs():
	att = input("Passes attempted: ")
	comp = input("Completed passes: ")
	yds = input("Total yards: ")
	td = input("Touchdowns: ")
	ints = input("Interceptions: ")

def rating():
	
	a = ((comp / att) - 0.3) * 5.0
	b = ((yds / att) - 3.0) * 0.25
	c = (td / att) * 20.0
	d = 2.375 - ((ints / att) * 25.0)
	
	passer_rating = (((a + b + c + d) / 6.0) * 100.0)
	
	print("Passer Rating is ", passer_rating)
	
def main():
	intro()
	inputs()
	rating()
	
if __name__ == '__main__':
    main()
