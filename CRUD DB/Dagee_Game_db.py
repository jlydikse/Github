import sqlite3

connection = sqlite3.connect("Dagee.db")

# this object is now in charge of all
# communication with our database
cursor = connection.cursor()

# create a table in the database
# (name, value, type [1 = good or 2 = bad ])

cursor.execute("create table ark (game_id integer, capacity integer, status integer)")

ark = [
    
]

# create a table in the database
# (name, value, type [1 = good or 2 = bad ])

cursor.execute("create table rain_resources (resource_name text, resource_value integer, resource_type int)")

rain_resources = [
    ("raindrop", 1, 2),
    ("drizzle", 3, 2),
    ("rainstorm", 5, 2),
    ("flood", 10, 2)
]

# we will need to use cursor.executemany because we will be loading multiple lines at once

cursor.executemany("insert into rain_resources values (?, ?, ?)", rain_resources)

# this makes the table readable within the ide
for x in cursor.execute("select * from rain_resources"):
    print(x)

print("----------------------")

# create a table in the database
# (name, value, type [1 = good or 2 = bad ])

cursor.execute("create table food_resources (food_resource_name text, food_description text, food_type int)")

food_resources = [
    ("Magical Mallows", "This is a magical marshmallow you can feed certain animals", 1),
    ("Mythical Carrots", "This is a mythical carrot you can feed certain animals", 1),
    ("Mysterious Mangoes", "This is a mysterious mango you can feed certain animals", 1),
    ("Mystical Bananas", "This is a mystical banana you can feed certain animals", 1),
    ("Miraculous Mushrooms", "This is a miraculous mushroom you can feed certain animals", 1),
    ("Poison", "Makes you go one less space", 2)
]

cursor.executemany("insert into food_resources values (?, ?, ?)", food_resources)

for x in cursor.execute("select * from food_resources"):
    print(x)

# I changed my mind, and don't want to include Mysterious Mangoes

print("----------------------")

cursor.execute("delete from food_resources where food_resource_name = ?", ("Mysterious Mangoes",))

for x in cursor.execute("select * from food_resources"):
    print(x)

print("----------------------")

cursor.execute("create table mythological_creatures (mythological_creature_name text, mythological_creature_description text, mythological_creature_value integer)")

# (name, description, type [1 = good or 2 = bad ])

mythological_creatures = [
    ("Trash Panda", "Trash Panda replaces a current creature on the field", 1),
    ("Phoenix", "You can place this creature on the field", 1),
    ("Plata-Dragon", "You can place this creature on the field", 1),
    ("Unicorn", "You can place this creature on the field", 1),
    ("Dirty Goblin", "This goblin forces you to pay back your debts to him by selling him your creatures you have in  your hand", 2)
]

cursor.executemany("insert into mythological_creatures values (?, ?, ?)", mythological_creatures)

for x in cursor.execute("select * from mythological_creatures"):
    print(x)

print("----------------------")

cursor.execute("create table special_cards (special_cards_name text, special_cards_description text, special_cards_type integer)")

# (name, description, type [1 = good or 2 = bad ])
special_cards = [
    ("Bucket", "Removes 1 raindrop", 1),
    ("Flood", "Adds 10 rain points to the field", 2),
    ("Bye-Bye", "Choose an animal you have and put it at the bottom of the deck", 1),
    ("See the future", "Look into the future by peaking at the top three cards on the deck", 1),
    ("Time-Traveling Bible", "See what cards were drawn and put back and see if there's one you want now (bottom 5 cards)", 2)

]

cursor.executemany("insert into special_cards values (?, ?, ?)", special_cards)

for x in cursor.execute("select * from special_cards"):
    print(x)

print("----------------------")

# here I am purposefully selecting a hand that will be bad for the user

your_hand = [cursor.execute("select * from rain_resources where resource_type = 2").fetchall(),
             cursor.execute("select * from mythological_creatures limit 2 offset 3").fetchall(),
             cursor.execute("select * from special_cards limit 1 offset 4").fetchall(),
             cursor.execute("select * from food_resources where food_type = 2").fetchall()]

mythological_creatures_in_hand = your_hand[1]

# format the data correctly
# the (creature_name, _, _) is to help separate each item into three variables
# the only one we really care about is creature_name, so the others are just placeholders

ark_data = [(index + 1, creature_name, 1) for index, (creature_name, _, _) in enumerate(mythological_creatures_in_hand)]

cursor.executemany("insert into ark(game_id, capacity, status) values(?, ?, ?)", ark_data)

print("")
print("The hand you were dealt:")
print("")
for cards in your_hand:
    for row in cards:
        print(row[0])

# separator
print("----------------------")
print("Mythological Creatures Saved from The Great Flood: ")
print("")

# this will print out all the mythological creatures you got onto the ark

for row in cursor.execute("select * from ark"):
    print(row[1])

print("----------------------")

### I am performing a join from food_resources and mythological_creatures ###

print("----------------------")

cursor.execute("""
        select food_resources.food_resource_name,
               food_resources.food_type,
               mythological_creatures.mythological_creature_name,
               mythological_creatures.mythological_creature_value
               
        from food_resources

        join mythological_creatures 
        
        on food_resources.food_type = mythological_creatures.mythological_creature_value
        
        where food_resources.food_type = 2;
        
""")

joined_table = cursor.fetchall()

# print out the joined_table
print("")
print("What creature can eat a type 2 foods")

print("")
print("Food Resource Name | Food Type | Mythological Creature Name | Mythological Creature Type")
print("________________________________________________________________________________________")

# figured the alignment should be 18, 9 and 26 respectively
for row in joined_table:
    print("{:<18} | {:<9} | {:<26} | {}".format(row[0], row[1], row[2], row[3]))

# This is the same join as above, but now it 
# will only show the food and creatures food type = 1
cursor.execute("""
        select food_resources.food_resource_name,
               food_resources.food_type,
               mythological_creatures.mythological_creature_name,
               mythological_creatures.mythological_creature_value
               
        from food_resources

        join mythological_creatures 
        
        on food_resources.food_type = mythological_creatures.mythological_creature_value
        
        where food_resources.food_type = 1;
        
""")
joined_table2 = cursor.fetchall()

# print out the joined_table
print("")
print("What creature can eat a type 1 foods")

print("")
print("Food Resource Name   | Food Type | Mythological Creature Name | Mythological Creature Type")
print("________________________________________________________________________________________")

# figured the alignment should be 18, 9 and 26 respectively
# unless it is for Miraculous Mushrooms, which needs reformatting
# in the else statement below
for row in joined_table2:
    if row[0] != "Miraculous Mushrooms":
        print("{:<20} | {:<9} | {:<26} | {}".format(row[0], row[1], row[2], row[3]))
    else:
        print("{:<18} | {:<9} | {:<26} | {}".format(row[0], row[1], row[2], row[3]))

# this functions just like a git commit command within to a github repo
# committing all the code that came before it to the SQLite3 db
connection.commit()

# close your connection here
# this is required when working with SQLite3
connection.close()



