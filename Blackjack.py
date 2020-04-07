import random
import time

playing = True

# ESTABLISH SUIT, RANK, AND CARD VALUES

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks =	("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
	"Jack", "Queen", "King", "Ace")


card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
"Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11} # have to use these 


# ESTABLISH CLASSES

class Card():


	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "{} of {}".format(self.rank, self.suit)


class Deck(Card):

	# CREATE A DECK

	def __init__(self):
		self.deck = []
		for suit in suits: # for 4 times,
			for rank in ranks: # for 13 times
				cards_ = Card(suit, rank)
				self.deck.append(cards_)
		
				 # fill deck with 52 instances
				
	
	def __str__(self):
		return "{} of {}s".format(self.suit, self.rank)
		
				
	def shuffle(self):
		generated_card = random.choice(self.deck)
		return generated_card

	def deal_cards(self): 

		deck_card_1 = Deck()
		deck_card_2 = Deck()
		deck_card_3 = Deck()
		deck_card_4 = Deck()
		global player_card
		global dealer_card
		global player_card2
		global dealer_card2
		player_card = deck_card_1.shuffle()
		dealer_card = deck_card_2.shuffle()
		player_card2 = deck_card_3.shuffle()
		dealer_card2 = deck_card_4.shuffle()



class Hand(Deck):


	def __init__(self):
		self.cards = [] # list holding player's current hand
		self.value = 0 # value of the card with given rank
		self.aces = 0 # attribute to keep track of aces drawn. Could be 1 or 11

		# Add the card to our hand

	def add_card(self, card):
		self.cards.append(card) # add our card to our hand
		self.rank_key = card.rank
		self.suit_key = card.suit
		value_of_card = str(card_values.get(card.rank))
		 # find the value of the card
		if int(value_of_card) <= 10:
			self.value += int(value_of_card)
		elif int(value_of_card) == 11: # if value of a card is 11, if the value of all your cards is less than or equal to 10, than add 11 to your value as the ace value.
			if self.value <= 10:
				self.aces += 1
				self.value += 11
			else:
				pass
		print("\n")
		

	def __str__(self):
		return "Here is your current hand: " + str(self.cards[0]) + " & " + str(self.cards[1])

	def adjust_for_ace(self, card, rank):
		if rank == "Ace":
			if self.value <= 10: # ace will be added
				self.aces += 1
			elif self.value >= 11: # if the value of cards is 11 or more, then ace will count as 1. 
				self.value += 1
		else:
			pass
		 


class Chips():

	def __init__(self):
		self.chip_value = 100
		
	def win_bet(self, bet):
		self.chip_value += bet
		print("\n")
		print("Your value of chips is: " + str(self.chip_value))
		return self.chip_value

	def lose_bet(self, bet):
		self.chip_value -= bet
		print("\n")
		print("Your value of chips is: " + str(self.chip_value))
		return self.chip_value
		# if lose_bet, update chip_value -=
		# if dealer wins, or self.value > 21:
		# print("Youve lost your bet!")
		# self.chip_value -= self.bet

	def push(self, bet):
		pass

chip_inst = Chips() # chip instance		
d_inst = Deck() # deck instance
player_hand = Hand() # hand instance
dealer_hand = Hand() # dealer instance


# FUNCTION FOR PLACING BETS

def place_bet():
	taking_bets = True
	while taking_bets:
		try:
			bet_amount = int(input("Enter your bet: "))
			print("\n")
		except:
			print("You need to type a number!")
		if bet_amount > chip_inst.chip_value:
			print("You can't bet more than $" + str(chip_inst.chip_value) + ". Please bet again.")
			continue
		else:
			print("You have " + str(chip_inst.chip_value) + " chips.")
			print("\n")
			print("You have bet " + str(bet_amount))
			return bet_amount
			break



# FUNCTION FOR TAKING HITS
# Should be called anytime a player requests a hit or dealer_hand.value is less than 17.

def hit(deck, hand):

	hit_card = deck.shuffle() # generate hit card
	rank_hit = hit_card.rank # establish rank of hit card
	if hand == dealer_hand:
		print("-----")
		print("Dealer draws a {} of {}".format(rank_hit, hit_card.suit))
		while dealer_hand.value < 17 and rank_hit == "Ace": # while the value of the dealer's hand is < 17, and an ace is drawn, update the value by 1. 
			hand.value += 1 # add card to the deck. hand.value will be updated here
			print("Dealer's new value is: " + str(hand.value)) # print value to the screen
			print("\n") 
			return hand.value
			if dealer_hand.value == 10:
				hand.value += 11
				print("Dealer's new value is: " + str(hand.value))
				print("\n")
				return hand.value
			else:
				pass
		hand.add_card(hit_card)
		print("Dealer's new value is: " + str(hand.value))
		return hand.value
	elif hand == player_hand:
		print("-----")
		print("You draw a {} of {}".format(rank_hit, hit_card.suit))
		while hand.adjust_for_ace(hit_card, rank_hit): # while an ace exists: 
			print("Your new value is: " + str(hand.value))
			return hand.value
			break
		hand.add_card(hit_card)
		print("Your new value is: " + str(hand.value)) # print value to the screen
		return hand.value
		


def hit_or_stand(deck, hand): 

	global playing

	while playing:
		hit_ask = input("Do you want to hit or stand?(h/s) ")
		if hit_ask == "h":
			hit(d_inst, player_hand)
			if hand.value < 21:
				print("The value of your hand is now: " + str(hand.value))
				print("\n")
				continue
			elif hand.value > 21:
				print("The value of your hand is now: " + str(hand.value))
				print("\n")
				print("You have busted!")
				break
			elif hand.value == 21:
				print("The value of your hand is now " + str(hand.value))
				print("\n")
				print("Blackjack!")
				break
		elif hit_ask == "s":
			while dealer_hand.value < 17: # dealer must keep hitting until hand value is 17 or higher. 
				hit(d_inst, dealer_hand)
				time.sleep(1)
				if dealer_hand.value >= 17 and dealer_hand.value <= 20: # If value of dealers hand is in range (17-20)
					print("The value of the dealer's hand is: " + str(dealer_hand.value))
					return dealer_hand.value
				elif dealer_hand.value == 21:
					print("Dealer has 21!")
					return dealer_hand.value
				elif dealer_hand.value > 21:
					print("Dealer has over 21!")
					return dealer_hand.value
		elif hit_ask != "h" or hi_task != "s":
			print("Please enter 'h' to hit or 's' to stay please!")
			continue
			

def show_some(player, dealer):
	print("Player has drawn: " + str(player_card))
	time.sleep(1)
	print("Dealer has drawn: " + str(dealer_card))
	time.sleep(1)
	print("Player's second card is: " + str(player_card2))
	time.sleep(3)
	print("-----")
	print("Player's total value: " + str(player_hand.value))

def player_busts():
	print("Player Busts! Dealer wins.")
	chip_inst.lose_bet(bet_amnt) # lose bet
	
def player_wins(deck, hand):
	print("Player wins!")
	chip_inst.win_bet(bet_amnt) # win bet
	time.sleep(1)
	print("You now have {} worth of chips".format(chip_inst.chip_value))
	
def dealer_busts(deck, hand):
	print("The Dealer has busted! Player wins.")
	chip_inst.win_bet(bet_amnt) # win bet
	

def dealer_wins(deck, hand):
	print("The Dealer has won! Player loses")
	chip_inst.lose_bet(bet_amnt) # lose bet

def push(player_hand, dealer_hand):
	# chip_inst.push(bet)
	print("Push! Both the dealer and player have the same amount.")


# GAME	
	
while True:

	print("Welcome to Blackjack!")
	print("\n")
	time.sleep(1)
	print("--Shuffling Deck--")
	d_inst.shuffle() # shuffle cards
	time.sleep(1)
	print("--Dealing Cards--") 
	d_inst.deal_cards() # deal cards
	time.sleep(1)
	print("\n")
	bet_amnt = place_bet() # take bet from player
	time.sleep(1)

	if player_card.rank or player_card2.rank == "Ace":
		
		player_hand.adjust_for_ace(player_card, player_card.rank) # Ace check
		player_hand.add_card(player_card) # display cards and add them to your hand
		dealer_hand.add_card(dealer_card) # add dealer_hand
		player_hand.adjust_for_ace(player_card2, player_card2.rank) # Ace check on card 2
		player_hand.add_card(player_card2) # display cards and add them to your hand
	
	while playing:

		print("--DISPLAYING CARDS--")
		time.sleep(1)

		show_some(player_hand, dealer_hand)

		if player_hand.value == 21:
			print("Blackjack! Player wins")
			player_wins(d_inst, player_hand)
			break

		time.sleep(1)
		print("\n")

		hit_or_stand(d_inst, player_hand) # if not blackjack, ask if player wants to hit or stand 
		# hit or stand will return dealer_hand.value
		time.sleep(1) 

		if (dealer_hand.value >= 17 and dealer_hand.value <=20) and (player_hand.value < dealer_hand.value):
			# if neither are at 21, but player value is less than dealer_value
			dealer_wins(d_inst, dealer_hand)
			print("Player has less than the dealer. Dealer wins!")
			break 

		elif ((dealer_hand.value >= 17 and dealer_hand.value <=20) and (player_hand.value >=17 and player_hand.value <=20)) and (player_hand.value > dealer_hand.value):
			player_wins(d_inst, player_hand)
			break

		elif dealer_hand.value == 21:
			print("Dealer has blackjack!")
			dealer_wins(d_inst, dealer_hand)
			break

		elif dealer_hand.value > 21:
			player_wins(d_inst, player_hand)	
			break

		elif dealer_hand.value == player_hand.value:
			push(player_hand, dealer_hand)
			break


		elif player_hand.value == 21: # if players hand is 21
			player_wins(d_inst, player_hand) # run player wins function
			print("Blackjack! Player wins")
			break

		elif player_hand.value > 21: # if the player's hand's value is over 21
			player_busts() # run the player bust function
			break # break out of playing loop


	if chip_inst.chip_value == 0:
		print("You are out of money to play!")
		time.sleep(1)
		print("------")
		time.sleep(1)
		print("If you'd like to reset with $100, please close out the game and restart.")
		break
	elif chip_inst.chip_value >= 1:
		play_again = input("Would you like to play again? (y/n): ")
		if play_again == "y":
			player_hand.value = 0
			dealer_hand.value = 0
			print("\n")
			continue
		else:
			break
