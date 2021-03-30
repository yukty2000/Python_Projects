

def binary_search(my_list,item) :
	l = 0
	h = len(my_list) - 1

	m = None

	while(l < h) :

		m = (l + h) // 2

		if my_list[m] == item :
			break

		elif my_list[m] < item :
			l = m + 1

		else :
			h = m - 1

	if(my_list[m] == item or my_list[l] == item) : 
		return True

	return False

print(binary_search([45,65,99,153],99))


