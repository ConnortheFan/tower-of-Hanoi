# “Tower of Hanoi” is a game in which you have 3 pegs (call them left, middle, and right) and a tower of different-sized rings on left. 
# The rings are stacked such that, from bottom-to-top, they go from largest-to-smallest.

# The goal of the game is to move the entire tower from left to right, but with the following constraints: 
# (1) you must move a single ring from one peg to another in any given move, and 
# (2) you cannot place a ring on top of another ring smaller than itself (but you can place a ring on top of another ring larger than itself). 
# In addition to simply moving the tower from left to right, you also want to try to minimize the number of moves.


def load_board():
  '''
  Print the current state of the board
  '''
  print(A)
  print(B)
  print(C)
  print("")

def move(start, end):
  '''
  Move the top ring from start to end.
  Also counts the number of moves made.
  '''
  global number_of_moves
  number_of_moves += 1
  print("Move", number_of_moves)
  i = len(start) - 1
  mover = start.pop(i)
  end.append(mover)
  load_board()

def find_number(number):
  '''
  Given a certain number representig a ring:
  Find and return which peg the ring is on
  '''
  if number in A:
    return A
  elif number in B:
    return B
  elif number in C:
    return C

def check_available(number, location):
  '''
  Return if the number is at the top of the peg represented by location
  '''
  return number == location[len(location)-1]

def free_space(start, end):
  '''
  Given 2 pegs, start and end, return the remaining peg
  '''
  if start == A:
    if end == B:
      return C
    elif end == C:
      return B
  elif start == B:
    if end == A:
      return C
    elif end == C:
      return A
  elif start == C:
    if end == A:
      return B
    elif end == B:
      return A

def valid_move(number, end):
  '''
  Check if moving a certain ring represented by number is able to move to the peg, end
  '''
  if len(end) == 1:
    return True
  elif number > end[len(end)-1]:
    return False
  else:
    return True

def reversed_list(number):
  '''
  Given a number, return the list from 1 to that number.
  Ex. Given 5, return [1,2,3,4,5]
  '''
  x = list(range(1, number+1))
  x.reverse()
  return x

def reversed_list_in(list, location):
  '''
  Given a list, return if that list is in location.
  Meant to be used with reversed_list(number).
  Can check if a peg has all consecutive rings.
  '''
  answer = True
  for i in list:
    if i in location:
      answer = True
    else:
      answer = False
      break
  return answer
  
def move_stack(number, end):
  '''
  The main function of the whole algorithm.
  Given a number, move the consecutive stack from that number to end.
  Also prints relevent information.
  '''
  while not reversed_list_in(reversed_list(number), end):
    # print(reversed_list(number))
    print("Number:", number)
    start = find_number(number)
    print("Start:",start)
    available = check_available(number, start)
    print("Available?",available)
    print("Valid move?", valid_move(number, end))
    if (available) and (valid_move(number, end)):
      move(start, end)
      if number != 1:
        new_number = number - 1
        move_stack(new_number, end)
      
    else:
      new_number = number - 1
      print("New number:",new_number)
      other = free_space(start, end)
      print("New space",other)
      print("")
      move_stack(new_number, other)

# A = left
# B = middle
# C = right

A = ["A"]
B = ["B"]
C = ["C"]

length = 15
for i in reversed_list(length):
  A.append(i)
  
load_board()
number_of_moves = 0

move_stack(15,C)
