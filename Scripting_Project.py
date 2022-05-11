import random

class Player():
    def __init__(self, money):
        self.__money = money #The players money
        self.__hand = [] #The players current hand
        self.__bet = 25 #The default bet, is set later withing a function
        self.__total = 0 #The total amount of the cards the player has
        self.__sitout = 0 #The amount of times a certain player has entered a 0 bet

    def get_player_money(self):
        return self.__money
        
    def reset(self):
        if(self.__total > 0):
            self.__total = 0
        self.__hand = []

    def get_sit_out(self): #This function is to check how many times someone has sit out
        return self.__sitout

    def sit_out(self): #This function is for if someone enters 0 into the bet
        self.__sitout += 1
    
    def set_player_bet(self, bet): #This fucntion sets the players bet that is passed
        self.__bet = bet
        if (bet <= self.__money and bet >= 25):
            self.__money = self.__money - self.__bet

    def get_player_bet(self): #This function return the players bet
        return self.__bet

    def player_bet(self, bet): #When the player bets, this function is called and it subtracts bet from money
        if (bet <= self.__money):
            self.__money = self.__money - bet

    def player_win(self): #This function is called when the player wins, it doubles your bet and adds it to money
        self.__money += self.__bet * 2

    def player_black_jack_win(self): #This function is called when the player wins by black jack, it triples your money and adds it to money
        self.__money += self.__bet * 3

    def player_tie(self): #If there is a tie between player and dealer this function is called and it just gives back the money the player bet
        self.__money += self.__bet

    def set_player_card(self): #Sets the players current hand
        self.__hand.append(shoe.draw_card())
        self.__hand.append(shoe.draw_card())

    def hit(self,card_num): #This function is called when the player chooses hit, and it addes the total of the hit card to total 
        self.__hand.append(shoe.draw_card())
        if (self.__hand[card_num].get_value() == "King" or self.__hand[card_num].get_value() == "Queen" or self.__hand[card_num].get_value() == "Jack"):
            self.__total += 10
        elif (self.__hand[card_num].get_value() == "Ace"):
            choice = input("Would you like ace to be 1 or 11:")
            if (choice == "11"):
                self.__total += 11
            elif (choice == "1"):
                self.__total += 1
        else:
            self.__total += int(self.__hand[card_num].get_value())

    def double(self): #When player chooses double, this function is called and it doubles the players bet, and takes away the money
        self.__money -= self.__bet
        self.__bet += self.__bet

    def set_total(self): #Sets the total of the players current hand to total
        for card in self.__hand:
            if (card.get_value() == "King" or card.get_value() == "Queen" or card.get_value() == "Jack"):
                self.__total += 10
            elif (card.get_value() == "Ace"):
                choice = input("Would you like ace to be 1 or 11:")
                if (choice == "11"):
                    self.__total += 11
                elif (choice == "1"):
                    self.__total += 1
            else:
                self.__total += int(card.get_value())
        return self.__total

    def get_total(self): #Returns the total of the cards that are currently in the players hand
        return self.__total

    def show_hand(self): #Shows the players current hand
        for card in self.__hand:
            card.show()


class Dealer():
    def __init__(self):
        self.__hand = []
        self.__total = 0

    def set_dealer_hand(self): #Sets the dealers hand
        self.__hand.append(shoe.draw_card())
        self.__hand.append(shoe.draw_card())

    def set_total_two(self): #Sets the total of the other card to total
        if (self.__hand[1].get_value() == "King"
                or self.__hand[1].get_value() == "Queen"
                or self.__hand[1].get_value() == "Jack"):
            self.__total += 10
        elif (self.__hand[1].get_value() == "Ace"):
            choice = random.randint(1, 2)
            if (choice == 1):
                self.__total += 11
            elif (choice == 2):
                self.__total += 1
        else:
            self.__total += int(self.__hand[1].get_value())
        return self.__total

    def set_total_one(self): #Sets the total of only one card to total
        if (self.__hand[0].get_value() == "King"
                or self.__hand[0].get_value() == "Queen"
                or self.__hand[0].get_value() == "Jack"):
            self.__total += 10
        elif (self.__hand[0].get_value() == "Ace"):
            choice = random.randint(1, 2)
            if (choice == 1):
                self.__total += 11
            elif (choice == 2):
                self.__total += 1
        else:
            self.__total += int(self.__hand[0].get_value())
        return self.__total

    def get_total(self): #Returns the total of the cards in the current hand
        return self.__total

    def hit(self,card_num): #When dealer has less than 17 hit is called
        self.__hand.append(shoe.draw_card())
        if (self.__hand[card_num].get_value() == "King" or self.__hand[card_num].get_value() == "Queen" or self.__hand[card_num].get_value() == "Jack"):
            self.__total += 10
        elif (self.__hand[card_num].get_value() == "Ace"):
            choice = input("Would you like ace to be 1 or 11:")
            if (choice == "11"):
                self.__total += 11
            elif (choice == "1"):
                self.__total += 1
        else:
            self.__total += int(self.__hand[card_num].get_value())

    def show_hand(self): #Shows the dealers whole hand
        for card in self.__hand:
            card.show()

    def show_one(self): #Shows only one of the dealers cards
        return self.__hand[0].show()


class Card():
    def __init__(self, suit, value, color):
        self.__suit = suit
        self.__value = value
        self.__color = color

    def show(self): #Shows the card
        print("Color: {} ".format(self.__color))
        print("{} of {}\n".format(self.__value, self.__suit))

    def get_value(self): #Gets the value of the current card
        return self.__value


class Deck():
    def __init__(self):
        self.__cards = []
        self.__build()

    def __build(self): #Builds the deck of 52 cards
        for j in range(1, 4):  #loop for sets of each suite
            for i in range(1, 13):  #Loop for number of cards in each suite.
                if (j == 1):
                    if (i == 1):
                        self.__cards.append(Card("Clubs", "Ace", "Black"))
                    elif (i > 1 and i <= 10):
                        self.__cards.append(Card("Clubs", i, "Black"))
                    elif (i == 11):
                        self.__cards.append(Card("Clubs", "King", "Black"))
                    elif (i == 12):
                        self.__cards.append(Card("Clubs", "Queen", "Black"))
                    elif (i == 13):
                        self.__cards.append(Card("Clubs", "Jack", "Black"))
                elif (j == 2):
                    if (i == 1):
                        self.__cards.append(Card("Spades", "Ace", "Black"))
                    elif (i > 1 and i <= 10):
                        self.__cards.append(Card("Spades", i, "Black"))
                    elif (i == 11):
                        self.__cards.append(Card("Spades", "King", "Black"))
                    elif (i == 12):
                        self.__cards.append(Card("Spades", "Queen", "Black"))
                    elif (i == 13):
                        self.__cards.append(Card("Spades", "Jack", "Black"))
                elif (j == 3):
                    if (i == 1):
                        self.__cards.append(Card("Hearts", "Ace", "Red"))
                    elif (i > 1 and i <= 10):
                        self.__cards.append(Card("Hearts", i, "Red"))
                    elif (i == 11):
                        self.__cards.append(Card("Hearts", "King", "Red"))
                    elif (i == 12):
                        self.__cards.append(Card("Hearts", "Queen", "Red"))
                    elif (i == 13):
                        self.__cards.append(Card("Hearts", "Jack", "Red"))
                elif (j == 4):
                    if (i == 1):
                        self.__cards.append(Card("Diamonds", "Ace", "Red"))
                    elif (i > 1 and i <= 10):
                        self.__cards.append(Card("Diamonds", i, "Red"))
                    elif (i == 11):
                        self.__cards.append(Card("Diamonds", "King", "Red"))
                    elif (i == 12):
                        self.__cards.append(Card("Diamonds", "Queen", "Red"))
                    elif (i == 13):
                        self.__cards.append(Card("Diamonds", "Jack", "Red"))

    def show(self): #Shows the whole deck (This is just for checking if there's anything in the class)
        for i in self.__cards:
            i.show()

    def shuffle(self): #Shuffling the deck
        for i in range(len(self.__cards) - 1, 0, -1): 
            r = random.randint(0, i)
            self.__cards[i], self.__cards[r] = self.__cards[r], self.__cards[i]

    def draw_card_deck(self): #Drawing a card from the deck directly
        return self.__cards.pop()


class Shoe():
    def __init__(self): 
        self.__shoe = []

    def add_deck(self, deck):  #Adding a deck class object to the shoe
        self.__shoe.append(deck)

    def draw_card(self): #Drawing a card from the shoe
        r = random.randint(0, 3)
        return self.__shoe[r].draw_card_deck()

    def show(
        self
    ):  #This function is mostly just for checking if the decks of cards are in the Shoe class
        for i in self.__shoe:
            i.show()

    def shuffle_shoe(self): #To shuffle the whole shoe
        for i in self.__shoe:
            i.shuffle()


def clear_screen():
    print('\x1bc')


#Main
Player_list = []
rand_player_amnt = 1
for i in range(0, rand_player_amnt):  #Loop to set all of the players begnning amounts randomly.
    rand_amnt = random.randint(500, 5000)
    Player_list.append(Player(rand_amnt))
for game_loop in range(0, 10):
    curr_game = True
    for i in range(0,len(Player_list)):
        Player_list[i].reset()
    shoe = Shoe()
    deck = Deck()
    dealer = Dealer()
    round = 1
    card_num = 1
    dealer_card_num = 1
    curr_play = 0  #Current player
    for i in range(1, 8):  #Adding all of the decks to the shoe and shuffling them then shuffling the shoe afterwards
        deck.shuffle()
        shoe.add_deck(deck)
    shoe.shuffle_shoe()
    if(game_loop >= 1):
        if(Player_list[curr_play].get_player_money() < 25):
            print("You have run out of money!")
            print("You lost, better luck next time")
            break
    print("Bank:{}".format(Player_list[curr_play].get_player_money()))
    bet = int(input(("Please enter a bet amount for player {}:".format(curr_play+1))))
    if(bet == 0):
        print("You have chosen to sit out")
        Player_list[i].sit_out()
        if(Player_list[i].get_sit_out() >= 3):
            print("You have chosen to sitout 3 times and are now out of the game, goodbye")
            break
        continue
    while (bet < 25 or bet > Player_list[0].get_player_money()-25):
        bet = int(input("Please enter an amount greater than 25 and less than bank amount"))
    Player_list[curr_play].set_player_bet(bet)
    clear_screen()
    print("This table has {} players\n".format(len(Player_list)))
    for i in range(0, len(Player_list)):
        Player_list[i].set_player_card()
    dealer.set_dealer_hand()
    if (Player_list[curr_play].get_player_money() >= 25 ):
        while (curr_game):
            print("Game {}".format(game_loop+1))
            print("Dealer cardnumbers:")
            dealer.show_one() 
            if (round == 1):
                print("Total value: {}".format(dealer.set_total_one()))
            elif (round > 1):
                print("Total Value: {} ".format(dealer.get_total()))
            print("-------------")
            for i in range(0, len(Player_list)):
                print("Player {}".format(i + 1))
                Player_list[i].show_hand()
                if (round == 1):
                    print("Total Value: {} Total bet: {} In bank: {}".format(
                        Player_list[i].set_total(),
                        Player_list[i].get_player_bet(),
                        Player_list[i].get_player_money()))
                elif (round > 1):
                    print("Total Value: {} Total bet: {} In bank: {}".format(
                        Player_list[i].get_total(),
                        Player_list[i].get_player_bet(),
                        Player_list[i].get_player_money()))
                print("--------------")
            print("\n")
            print("Current Player {} in round {}\n".format(curr_play + 1, round))
            if (round < 3):
                print("Please choose 1,2 or 3")
                choice = int(input("Options available: 1.Hit 2.Double 3.Stand "))
                if (choice < 1 or choice > 3):
                    print("Please choose a correct number")
                    choice = int(input("1.Hit 2.Double 3.Stand"))
            elif (round >= 3):
                print("Please choose 1, or 2")
                choice = int(input("Options available: 1.Hit 2.Stand"))
                if(choice == 2):
                    choice = 3
            if choice == 1:
                clear_screen()
                print("You have chosen hit")
                card_num += 1
                Player_list[curr_play].hit(card_num)
                if(Player_list[curr_play].get_total() > 21):
                    break
                print ("Total: {}".format(Player_list[curr_play].get_total()))
            elif choice == 2:
                clear_screen()
                print("You have chosen double")
                if (Player_list[curr_play].get_player_money() < Player_list[curr_play].get_player_bet()):
                    print("You have tried to bet more than you have")
                    print("You lose")
                    exit(0)
                Player_list[curr_play].double()
                card_num += 1
                Player_list[curr_play].hit(card_num)
                break
            elif choice == 3:
                clear_screen()
                print("You have chosen to stand")
                break
            if (curr_play < len(Player_list) - 1):
                curr_play += 1
            elif (curr_play >= len(Player_list) - 1):
                curr_play = 0
            round += 1
        if (Player_list[curr_play].get_total() > 21):
            Player_list[curr_play].show_hand()
            print("Total: {}".format(Player_list[curr_play].get_total()))
            print("BUST, you have gone over 21 and are out of the current game")
            continue
        clear_screen()
        print("Dealer is now revealing cards")
        dealer.set_total_two()
        while(dealer.get_total() < 17):
            dealer_card_num += 1
            dealer.hit(dealer_card_num)
            if(dealer.get_total() > 21):
                clear_screen()
                print("Dealer Hand:")
                dealer.show_hand()
                print("Total:{}\n".format(dealer.get_total()))
                print("Dealer has gone over 21 and lost all players who are left win")
                for i in range(0,len(Player_list)):
                    if(Player_list[i].get_total() == 21):
                        print("Player {} has gotten blackjack".format(i+1))
                        Player_list[i].player_black_jack_win()
                    else:
                        Player_list[i].player_win()
                continue
            else:
                continue
        if(dealer.get_total() > 21):
            continue
        dealer.show_hand()
        print("Total: {}".format(dealer.get_total()))
        print("------------")
        print("Player Cards:\n")
        Player_list[curr_play].show_hand()
        print("Total: {}".format(Player_list[curr_play].get_total()))
        if(Player_list[curr_play].get_total() == 21 and dealer.get_total() == 21):
            print("You and the dealer have gotten blackjack!")
            Player_list[curr_play].player_win()
            continue
        elif(Player_list[curr_play].get_total() == 21):
            print("You have gotten blackjack and won!")
            Player_list[curr_play].player_black_jack_win()
            continue
        elif(dealer.get_total() == 21):
            print("The dealer has blackjack, everyone loses")
            continue
        elif(dealer.get_total() > Player_list[curr_play].get_total()):
            print("The dealer has a higher score, dealer wins")
            continue
        elif(dealer.get_total() < Player_list[curr_play].get_total()):
            print("You have gotten higher than the dealer you win!")
            Player_list[curr_play].player_win()
            continue
        elif(dealer.get_total() == Player_list[curr_play].get_total()):
            print("You and the dealer have gotten the same score, it is a tie!")
            Player_list[curr_play].player_tie()
            continue
    else:
        print("You have lost, better luck next time!")
        exit(0)
print("See you again!")