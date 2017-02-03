import random
def generate_list():
	alist = [x for x in range(random.randint(-10,10))]
	assert len(alist)>1 ,"alist is empty"
	assert sum(alist)>(-100) ,"alist is less than -100"
	return alist

def printIt():
	print(generate_list())

def main():
	printIt()


if __name__=='__main__':
	print("Test printIt():")
	main()
