import inquirer
from omdb import *
from weather import *

while True:
    COMMAND1="1:Movie-this"
    COMMAND2="2:Spotify-this-song"
    COMMAND3="3:Weather-this"
    COMMAND4="4:Quit"
    questions = [
    inquirer.List('command',
                    message="Enter command",
                    choices=[COMMAND1, COMMAND2, COMMAND3, COMMAND4]
                ),
    ]
    answers = inquirer.prompt(questions)
    command = answers["command"]
    if command == COMMAND1:
        movieName = input("Enter movie name:")
        search_movie(movieName)

    if command == COMMAND3:
        cityName = input("Enter city name: ")
        search_weather(cityName)
    
    if command == COMMAND4:
        exit()

  