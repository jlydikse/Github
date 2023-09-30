# Overview

<p>I have always been interested in working with databases, but haven't always been good at it, so I decided to create a small database Python program that communicates with sqlite3 in order to create the database and perform various SQL commands. I wanted to practice and perfect the CRUD operations within SQL using this approach, and I feel like I did a pretty great job!</p>

<p>The database I chose to create is based on a board game I helped create with the youth group I am partially in charge on for my church. We spent probably 4 months of activities creating a board game with the kids that answers a simple question, "What if, the reason there are no mythological creatures on earth anymore, is because they could not get onto Noah's Ark for some reason?" The program I created goes through and creates various tables in a database named "Dagee.db" within sqlite3.</p>

The reason I made this is because I want to make this physical board game into a playable game that you can play on your computer or maybe an app or something like that. I don't have it all planned out or anything, but I am excited to learn about those processes and which platform I should choose. I want to be able to present this to the youth group members before they age out of the program.



[Software Demo Video](https://youtu.be/ReDdkR4q5H4)

# Relational Database

I created this database in sqlite3 and the overall database is called Dungee.db.

{I created the tables into logical separations of the cards you play with in the game. There are 5 total tables that I created: an ark table for the visualization of the ark piece of the board game, a rain_resource table which stores the cards that represent the various water cards you can draw during the game, food_resources which store the various foods that you can feed your mythological creatures to keep them alive, mythological_creatures which stores the various mythological creatures you can draw in the game, and finally special_cards which stores a number of special cards within that table.}

# Development Environment

{This was created in VScode IDE using Python and importing sqlite3}


# Useful Websites

{Make a list of websites that you found helpful in this project}

- [SQL Shack](https://www.sqlshack.com/crud-operations-in-sql-server/)
- [CrowdStrike](https://www.crowdstrike.com/cybersecurity-101/observability/crud/)

# Future Work

{This is a live document in that I am still going to be working on this and using this as a platform to improve and learn. Below I have listed some of the improvements I need to make in order to polish and complete this project further.}

- I need to actually have a functioning gui that pulls up the cards and virtually simulates you playing the game within a gui
- I need to implement some more logical conditions so that this game can run instead of just creating the database and doing the sql portion, which is basically most of what I've completed.
- I want to add to this database and think deeper about how I should join the tables such that there are some more meaningful insights or entirely new things I can make from them.