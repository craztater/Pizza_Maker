import shutil

size = 0
MAX_SIZE = (shutil.get_terminal_size().columns // 6) - 1

def main():
	size = get_number_of_people()	
	pizza(size)
	people(size)
	
	
	
def get_number_of_people():
	while True:
		size = input("Enter the number of people who want to eat a pizza: ")
		try:
		    size = int(size)
		    if size <= MAX_SIZE:
		        return size
		    else:
		        print(f"\nSorry, we don't have that much pizza! :( \nCome again with {MAX_SIZE} or less.\n")
		except ValueError:
		    print("Invalid input. Please enter an integer.")
		except Exception as e:
		    print(f"An unexpected error occurred: {e}")
            
            
def pizza(size):
	pizza_width = size * 6
	
	#top line
	print('\n  ' + '_' * pizza_width)
		
	## first curve
	print(' /' + ' . ' * ((pizza_width//2) - (pizza_width//6)) + '\\')
	
	## second curve
	print('/' + ' o ' * ((pizza_width//2) - (pizza_width//6)) + '  \\')
	
	## the pie
	for _ in range((pizza_width//6)):
        	print('|' + '  o' * ((pizza_width // 3) + 1) + '|')
        	print('|' + ' o ' * ((pizza_width // 3) + 1) + '|')
        
	## first bottom curve
	print('\\' + '  o' * ((pizza_width//2) - (pizza_width//6)) + '  /')
	
	## seccond bottom curve
	print(' \\' + '___' * ((pizza_width//2) - (pizza_width//6)) + '/')
		
	
def people(size):

	print()
	for head in range(size):
		print("0     ", end='')
	print()
	
	for body in range(size):
		print("|//   ", end='')
	print()
		
	for legs in range(size):
		print("//    ", end='')
	print()



main()
