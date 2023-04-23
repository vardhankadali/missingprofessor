

# Missing Professor

A treasure hunt-like game where the player must decode and solve puzzles in order to save a missing professor before it's too late.

![codeblock](/images/home.jpg)
<!-- TOC -->
# Table of contents

- [Steps to set up the Project](#steps-to-set-up-the-project)
- [Soft Skils Being Assessed](#soft-skils-being-assessed)
- [Detailed Walkthrough](#detailed-walkthrough)
    - [Pharmacy](#pharmacy)
    - [The Map](#the-map)
    - [The Locked House](#the-locked-house)
    - [The Office](#the-office)
    - [House Unlocked](#house-unlocked)
    - [Laboratory](#laboratory)
    - [Three new places on the map](#three-new-places-on-the-map)
    - [Factory](#factory)
    - [Factory Basement](#factory-basement)
    - [The Final Escape](#the-final-escape)
- [Additional Features](#additional-features)

<!-- /TOC -->

# Steps to set up the Project
- You can directly open and start playing the game by following this [link]("https://missingprofessor.onrender.com/").
- If you wish to do this project on your own, setting it up and modifying is simple. Download the files or clone this repository to your laptop or desktop.

` git clone https://github.com/vardhankadali/missingprofessor.git `

- After cloning, install all the required python packages in the requirements.txt file.

`pip install -r requirements.txt`

- Choose any database and replace the link in the _ _init_ _.py file in the missingprofessor folder with the link of your database, or simply use sqlite3 database.

![codeblock](/images/code.png)

- Run the app.py file in the missingprofessor folder in order to run the application.

# Soft Skils Being Assessed

- Observation skills
- Attention to detail
- Memory
- Problem solving



# Detailed Walkthrough 

- As soon as the player opens the game, a breif description is given, followed by an option to start the game.
![](/images/home.jpg)

- The player will be asked to Login/Register in order to start the game.

- Once the player has successfully logged in, the game begins. 

- The player is given a brief description and is asked to go to the pharmacy in order to start the investigation.
![](/images/user.jpg)

## 1. Pharmacy

- The player is encountered with a simple directions puzzle, which is only given to throw off the concerntration of the player away from the first main clue: The medicine name, Fluticasone.
![](/images/pharmacy1.jpg)

- The player is given an option to view the map.

## 2. The Map

- The player is provided with an interactive map, which is available for the rest of the game.
![](/images/map1.jpg)
- Some of the places in the map are hidden, which are unlocked as the player progresses along in the game.
- The player can access the map anytime from the navigation bar.
![](/images/navbar1.jpg)
![](/images/navbar.jpg)

## 3. The Locked House

- If the player decides to go to the house first, the house is shown to be locked, and that they need to find the key in order to get in.
![](/images/houselocked.jpg)

## 4. The Office

- The office is the first place where the player is actually needed to start thinking. At first glance it looks like a normal room. But there are two hidden clickable areas, which the player can click to find clues and objects.
![](/images/office.jpg)

- The two highlighted areas in the picture above show the clickable areas. The desk and the bookshelf.

- Upon clicking the desk, the drawer opens and the player can find the house key there, which can be picked up by clicking on it. Picking up the key automatically grants access to the house.
![](/images/key1.jpg)
![](/images/emptydrawer.jpg)

- Upon clicking the bookshelf, the diary of the missing professor is found. There are some more clues about the next place the player needs to go to, along with another important clue: The date of dissapperance. A new part of the map is also unlocked.
![](/images/diary.jpg)

## 5. House Unlocked

- As the player has found the key, the house is now unlocked. Inside the house, there is a hidden clue in the potrait on the wall. Upon clicking this potrait, the player is given a closer look of it. The potrait contains the name of the dog, which is used required later on.
![](/images/houseunlocked.jpg)
![](/images/dogpic.jpg)

## 6. Laboratory

- The map now has a new location, the laboratory.
![](/images/map2.jpg)

- The Laboratory is locked, and the player needs to enter a password in order to unlock it. There is a hint given that the password is the name of the professor's dog, which the player might've found while looking around in the house.
![](/images/lablocked.jpg)
- Upon entering the right password, the lab is unlocked and the player can go inside.
![](/images/labunlocked.jpg)
- The lab is said to be searched and an audio recording from the day of the professor's disapperance is said to be found. The player is given an option to listen to the audio.
![](/images/labaudio.jpg)
- In this audio recording, it is found out that the professor has been kidnapped, and is being held at a place 10 minutes from the lab. Also a hint to the place and to solve the PIN to that place is given. New parts of the map are unlocked.

## 7. Three new places on the map

- Three new places are unlocked on the map, completing it. The player needs to choose the right place carefully, as two of them are deadends; the mansion and the warehouse.
![](/images/map3.jpg)
![](/images/mansion.jpg)
![](/images/warehouse.jpg)

## 8. Factory

- The factory matches the breif description given in the audio recording. The place is locked, with a PIN lock. The PIN is said to be the date of the professors disappearence in the audio recording; 15th April, which the player must figure out from the previous clues. The pin is 1504.
![](/images/factorylocked.jpg)

## 9. Factory Basement

- The player finally finds the professor in this place. But, she seems to be having an asthma attack, and the player must choose the right medicine (hint given in the pharmacy) to give her. Choosing any of the three wrong ones will result in the professor dying, and the entire progress being reset, forcing the player to replay the entire game.
![](/images/failed.jpg)
- Choosing the correct option leads to the final part of the game.
![](/images/basement.jpg)
![](/images/saved.jpg)

## 10. The Final Escape
- The player is given the option to escape, which starts a fun little game, where the player needs to dodge bullets by clicking as soon as the screen turns red, three times.
![](/images/escape1.jpg)
![](/images/escape2.jpg)
![](/images/escape3.jpg)
- The played cannot lose this mini game as it just involves clicking on the screen. Upon completing this part, the game is complete and the user is given an option to restart the game.
![](/images/success.jpg)


# Additional Features

- This web app has an Admin Page, which only the admin accounts have access to. In here, the current progress of every registered user can be monitored.
![](/images/admin3.jpg)
- In order to access this page, you must login with an admin account. The Admin Dashboard option is only available to admin accounts.
![](/images/admin1.jpg)
![](/images/admin2.jpg)


