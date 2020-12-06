categories = ['brand', 'seats', 'color', 'price']

available_cars = {
	
	'impreza' : {
	'brand' : 'subaru',
	'seats' : 5,
	'color' : 'red',
	'price' : 40,
	},

	'mustang' : {
	'brand' : 'ford',
	'seats' : 2,
	'color' : 'white',
	'price' : 55,
	},

	'sonata' : {
	'brand' : 'hyundai',
	'seats' : 5,
	'color' : 'silver',
	'price' : 35,
	},
}



prompt = "Welcome to my car rental service."
prompt += "\nWhat are you looking for in a car?"
prompt += "\n\n- - -"
prompt += "\n\nBrand"
prompt += "\nSeats"
prompt += "\nColor"
prompt += "\nPrice"
prompt += "\n\nPlease type which of these is your priority: "

priority = raw_input(prompt).lower()


if priority in categories:
	print("\nWe will match you with vehicles that fit with your priorities.")
	print("Your top priority is: " + priority.title() + "\n")
	if priority == 'color':
		print("We have cars available in these colors:")
		for car, aspect in available_cars.items():
			print("\t" + aspect['color'].title())
		color_choice = raw_input("\nWhich of these colors do you prefer?\nPlease enter your choice: ").lower()
		for car, aspect in available_cars.items():
			if color_choice in aspect['color']:
				print("\nBased on your priorities, we recommend this car:\n" + 
					aspect['brand'].title() + " " + car.title() + ", with the following characteristics:\n" + 
					"Seats: " + str(aspect['seats']) + "\n" +
					"Color: " + aspect['color'].title() + "\n" +
					"Price: $" + str(aspect['price']) + " per day"
					)
		



	# elif:	
		


else:
	print("\nYour top priority is: " + priority.title() + "\nSorry, your priority does not match with any of our available cars.")














