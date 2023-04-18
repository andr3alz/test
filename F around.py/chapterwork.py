# def display_message():
#     """this program will display a message as a function"""
#     print("this function saves a block of code")

# display_message()

# def favorite_books(books):
#     """books we like"""
#     print(" I love books, one of my favorites is, " + books.title() + "!" )

# favorite_books("the shinning")
# favorite_books("cujo")


# def make_shirt(text,shirt_size):
#     '''tshirt message and size'''
#     print("Your T-Shirt will say " + text.title()+ "in size " + shirt_size + "!")

# make_shirt(text='tuttit fuckin frutti ',shirt_size='large')
### Tshirt

# def make_shirt(text=' i love python',size='large'):
#     print("your shirt will say" + text + " and is size "+ size )

# make_shirt()
# make_shirt(size="medium")

# make_shirt(text="SUCK IT EASY")
#t shirt two
#************************            
#cities
#***********************
# def Describe_cities(city,country="mexico"):
#     print("The city of "+ city.title() + " is in " + country + "! ")

# Describe_cities("Mexico City")
# Describe_cities("Cabo san lucas")
# Describe_cities(country="canada",city="toronto")

# def get_formatted_name(first_name, last_name, middle_name=' '):
#     """retun a full name neatly formatted"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name +  ' '  + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name("jimi", "hendrix")
# print(musician)
# musician = get_formatted_name('john','hooker','lee')
# print(musician)

# def build_person (first_name, last_name, age= ''):
#     '''return a dictionary pf information about a person.'''
#     person = {'first' : first_name, 'last' : last_name}
#     if age:
#         person ['age'] = age

#     return person


# musician = build_person ('jimi', 'hendirx', age =27) 
# print(musician)
# def make_alblum(name, alblum, tracks= ''):
#    music_alblum= {'artist ': name, 'record' : alblum }
#    if tracks:
#       music_alblum ['tracks'] = tracks
#    return music_alblum

# while True:
#    print("\n Please give me an artist and alblum:")
#    print('("enter q at anytime to quit")')

#    A_name= input("artist: ")
#    if A_name== 'q':
#       break
#    Al_name= input("Alblum: ")
#    if Al_name == 'q':
#       break
#while loop above******


# music_1 = make_alblum ('opiv', 'knowledge')
# print(music_1)
# music_2 = make_alblum ('rhiana', 'envy')
# print(music_2)
# music_3 = make_alblum ('greenday', 'dookie', '14')
# print(music_3)



# def greet_users(names):
#     for names in names:
#         msg= "hello, " + names.title() + "!"
#         print(msg)
# pppl_who_suck= ['karen','kyle','susan']
# greet_users(pppl_who_suck)
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)
#*********passing a list***********

# unprinted_designs = ['iphone case','robot pendent','dodecahedron']
# completed_models = []
# #simulate printing each design, until none are left
# #move each design to completed_models after printing
# while unprinted_designs:
#     current_design= unprinted_designs.pop()
#     #simulate creating a 3d print from the design
#     print ("printing model: " + current_design)
#     completed_models.append(current_design)

# print("\n the following models have been printed: ")
# for completed_model in completed_models:
#   print (completed_model)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)

# def show_completed_models (completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone', 'robot pendant', 'dode']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)



