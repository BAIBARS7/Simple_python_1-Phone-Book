phone_book = {
"12121212":"amal",
"455454545": "saysd",
"323221": "koki",
"sam": "zocx",
	
}

#vaild_number

def valid_number(number):
    count = 0
    for char in number:
        count += 1
    if count != 10:
        return False
    for char in number:
        if char < '0' or char > '9':
            return False
    return True

#find_by_number

def find_name_by_number():
	phone_number = input("enter the number:")
	if valid_number(phone_number):
		for number in phone_book:
		    if  phone_number == number:
			    print(phone_book[phone_number])
			    return
		print("sorry, this number is not found")
	else:
	    print("this is invalid number")

#find_by_name

def find_number_by_name():
	name = input("enter the name: ")
	for number, owner in phone_book.items():
		if owner == name:
			print(number)
			return
		print("sorry, the name is not found")
	
	#add_new_contact

def add_new_contect():
	new_name = input("add new name: " )
	new_number = input("add the number: ")
	if valid_number(new_number):
		phone_book[new_number] = new_name
		print("contact add successfully")
	else:
	     print("this is invalid number")

#func

	find_name_by_number()
	find_number_by_name()
	add_new_contect()		
