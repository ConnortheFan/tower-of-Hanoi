


def load_board():
  print(A)
  print(B)
  print(C)
  print("")

def move(start, end):
  global number_of_moves
  number_of_moves += 1
  print("Move", number_of_moves)
  i = len(start) - 1
  mover = start.pop(i)
  end.append(mover)
  load_board()

def find_number(number):
  if number in A:
    return A
  elif number in B:
    return B
  elif number in C:
    return C

def check_available(number, location):
  return number == location[len(location)-1]

def free_space(start, end):
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
  if len(end) == 1:
    return True
  elif number > end[len(end)-1]:
    return False
  else:
    return True

def reversed_list(number):
  x = list(range(1, number+1))
  x.reverse()
  return x

def reversed_list_in(list, location):
  answer = True
  for i in list:
    if i in location:
      answer = True
    else:
      answer = False
      break
  return answer
  
def move_stack(number, end):
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

A = ["A"]
B = ["B"]
C = ["C"]

length = 15
for i in reversed_list(length):
  A.append(i)
  
load_board()
number_of_moves = 0

move_stack(15,C)