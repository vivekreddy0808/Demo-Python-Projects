def my_name()
  print (' Hello This Vivek !!')
my_name()

def my_new_friend(name):
  print (f' hey {name} ')
# my_new_friend('vi')

def greeting(greet, name, place):
  '''
  Function consist of 3 arguments
  >>> greet ( greet, name, place)
  print " Hey, greeting for {name} wel to {palce}"
  '''
  print (f' Hey!!! {name}, {greet} welcome to {place}')

greeting('Welcome', 'Rocky', 'Hyderabad')

# Default Arguments
def greeting(name,greet='Welcome', place='Hyderabad'):
  '''
  Function consist of 3 arguments
  >>> greet ( greet, name, place)
  print " Hey, greeting for {name} wel to {palce}"
  '''
  print (f' Hey!!! {name}, {greet} welcome to {place}')

greeting('Rocky')

#Named Arguments

def greeting(name,greet='Welcome', place='Hyderabad'):
  '''
  Function consist of 3 arguments
  >>> greet ( greet, name, place)
  print " Hey, greeting for {name} wel to {palce}"
  '''
  print (f' Hey!!! {name}, {greet} welcome to {place}')

greeting(name='Rocky', greet='Welcome', place='Hyderabad')

def sum(a, b):
  '''
  Add two numbers & display sum
  '''
 return a+b
print(sum(1,2))