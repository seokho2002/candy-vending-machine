#final homework in open sourceprograming
def choose_candy_fun():

	# set the number of storage
    mango_avail = 20
    orange_avail = 20
    lemon_avail = 20
    emli_avail = 20

	# continue or not
    cont = "y"

	# the number of candy you want
    total_mango = 0
    total_orange = 0
    total_lemon = 0
    total_emli = 0

	# insert money
    total_money = int(input("Insert your money (Rs): "))
	
	#loop until cont is n or N
    while cont != "n" and cont != "N":
        if cont == "y" or cont == "Y":
            choose_candy = input("Choose flavour : \n1.  Mango(Available = " + str(mango_avail) +
                                 ")   2.  Orange(Available = " + str(orange_avail) +
                                 ")   3.  Lemon(Available = " + str(lemon_avail) +
                                 ")   4.  Emli(Available = " + str(emli_avail) + ")\n(2 Rs./candy).\n")
			
			# choose mango candy 
            if choose_candy == "1":
                if mango_avail == 0:
                    print("Sorry, We have no stock of Mango Candy.")
                else:
                    mango = int(input("How many Mango candies you want?\n"))

					# the candy is available and enough money
                    for i in range(mango):
                        if mango_avail > 0 and total_money >= 2:
                            total_mango += 1
                            mango_avail -= 1
                            total_money -= 2
                            print("Mango Candy " + str(total_mango))

						# not enough money
                        elif total_money < 2:
                            print("Not enough money.")
                            break

						# not enough candies
                        else:
                            print("No more Mango candies available.")
                            break

			# choose orange candy 
            elif choose_candy == "2":
                if orange_avail == 0:
                    print("Sorry, We have no stock of Orange Candy.")
                else:
                    orange = int(input("How many Orange candies you want?\n"))

					#the candy is available and enough money
                    for j in range(orange):
                        if orange_avail > 0 and total_money >= 2:
                            total_orange += 1
                            orange_avail -= 1
                            total_money -= 2
                            print("Orange Candy " + str(total_orange))

						#not enough money
                        elif total_money < 2:
                            print("Not enough money.")
                            break

						#not enough candies
                        else:
                            print("No more Orange candies available.")
                            break

			#choose lemon candy
            elif choose_candy == "3":
                if lemon_avail == 0:
                    print("Sorry, We have no stock of Lemon Candy.")
                else:
                    lemon = int(input("How many Lemon candies you want?\n"))

					# the candy is available and enouth money
                    for k in range(lemon):
                        if lemon_avail > 0 and total_money >= 2:
                            total_lemon += 1
                            lemon_avail -= 1
                            total_money -= 2
                            print("Lemon Candy " + str(total_lemon))

						# not enough money
                        elif total_money < 2:
                            print("Not enough money.")
                            break

						#not enough candies	
                        else:
                            print("No more Lemon candies available.")
                            break

			#choose emli candy
            elif choose_candy == "4":
                if emli_avail == 0:
                    print("Sorry, We have no stock of Emli Candy.")
                else:
                    emli = int(input("How many Emli candies you want?\n"))

					#the candy is available and enough money
                    for l in range(emli):
                        if emli_avail > 0 and total_money >= 2:
                            total_emli += 1
                            emli_avail -= 1
                            total_money -= 2
                            print("Emli Candy " + str(total_emli))

						# not enough money
                        elif total_money < 2:
                            print("Not enough money.")
                            break

						# not enough candies
                        else:
                            print("No more Emli candies available.")
                            break

			#if you input wrong answer 
            else:
                print("Ohh!! You entered wrong input.")

		# print the number of remaining candies 
        print("We have " + str(mango_avail) + " Mango candies, " + str(orange_avail) + " Orange candies, " + str(lemon_avail) + " Lemon candies, " + str(emli_avail) + " Emli Candies in stock.")

		# prnit remaining money 
        print("Remaining money: Rs." + str(total_money))

		# ask continue or not 
        cont = input("Do you want to continue?:(Y/N)\n")

		#if you want end(cont is n or N) calculate the total amount and change
        if cont == "n" or cont == "N":
            total_amount = (total_mango + total_orange + total_lemon + total_emli) * 2
            change = total_money
            print("You got total " + str(total_mango) + " Mango, " + str(total_orange) + " Orange, " + str(total_lemon) + " Lemon, " + str(total_emli) + " Emli Candies.\nTotal amount you spent is: Rs." + str(total_amount))
            print("Change to return: Rs." + str(change))
            input("Thank You for visit!")
            exit()

		#if you want continue, go candy choose
        elif cont == "y" or cont == "Y":
            pass

		# input other answer
        else:
            print("Ohh!!!. You entered wrong input.")

# main funtion loop
while True:
    x = input("Welcome to Chatpatti Candy shop!!!\n\nIf you want to buy candies enter 'Y'.\nOtherwise enter 'N':\n")
    if x == "y" or x == "Y":
        choose_candy_fun()
    elif x == "n" or x == "N":
        break
    else:
        print("Sorry, Invalid Entry!!!")

input("Thank You for visit!")

