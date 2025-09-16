#importing shuffle
from random import shuffle
#creating function for shuffling a list
def shuffle_list(mylist):
  shuffle(mylist)
  return mylist
creating a list adn calling the function
list1=['','0','']
shuffle_list(list1)
#creating the function for player guessing
def player_guess():
  guess=''
  while guess not in ['0','1','2']:
    guess=input('pick a number o 1 or 2:')
  
  return int(guess)
#calling player guess function
player_guess()
assigning playe_guess function result to variable
index=player_guess()
index
#function to check player guess and shuffle function
def check_guess(shuffle_list,guess):
  if shuffle_list[guess] == '0':
    print('correct')
  else:
    print('wrong guess')
    print(shuffle_list)
#final results
#initial list
list1=['o','','']
#shuffled list
mix_list=shuffle_list(list1)
#user guess
guess=player_guess()
#guess check
check_guess(mix_list,guess)
