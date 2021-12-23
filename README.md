# Socket Programming in Python

## About the Project

This is a GUI application that serves psychological questionnaires to clients and gives them the overall results

## Protocol Used

We used **TCP** protocol for the Transportation Layer.

## Prerequisites

- Python 3.8 or higher

## Set up your environment

1. Clone the repo
   - HTTPS
     ```sh
     git clone https://github.com/RamadanIbrahem98/sockbot.git
     ```
   - SSH
     ```sh
     git clone git@github.com:RamadanIbrahem98/sockbot.git
     ```
   - Download as Zip file
1. Create a Virtual Environment (Optional)
   ```sh
   python -m venv .env
   ```
1. Activate the virtual environment

   - using CMD
     ```sh
     .\.env\Scripts\activate
     ```
   - using PowerShell
     ```sh
     .\.env\Scripts\Activate.ps1
     ```
   - using Bash
     ```sh
     source .env/bin/activate
     ```

1. Install the requirements and dependancies

   ```sh
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

1. Run the application. Open two terminal windows. \
   one for the server and one for the client. (don't forget to enable the environment on both terminal windows)
   
   ```sh
   cd src
   python TCPServerMultiClients.py
   ```
   
   ```sh
   cd src
   python ClientApp.py
   ```

## Project Structure

|        Files&Folders        	|                                                        Purpose                                                       	|
|:---------------------------	|:--------------------------------------------------------------------------------------------------------------------	|
| src/                        	| Contains all files for the project.                                                                                  	|
| src/db/                     	| Contains the files responsible for the Database queries.                                                             	|
| src/db/Database.py          	| Database class for executing SQL statements on an SQLite Database.                                                   	|
| src/db/initialization.sql   	| File contains all queries that initialize the database with the main tables and data.                                	|
| src/db/database.db          	| Generated DB file after running the app for the first time. you can view it in any DB Browser that supports SQLite3. 	|
| src/db/talk.py              	| File contains the class that uses the database to read all questionnaires data.                                      	|
| src/Security/               	| Contains security files implementations.                                                                             	|
| src/Security/Security.py    	| Contains a class responsible for encryption and decryption of hosts messages.                                        	|
| **src/Security/.env**        	| **File that HAS to be created after cloning the repository and add the variable called ENCRYPTION_KEY.**             	|
| src/TCPClient/              	| Contains all of the client logic implementations.                                                                    	|
| src/TCPClient/TCPClient.py  	| Contains the class responsible for handling client messages to and from the server.                                  	|
| src/TCPServer/              	| Contains all of the server logic implementations.                                                                    	|
| src/TCPServer/TCPServer.py  	| Contains the class responsible for handling server responses to one client messages.                                 	|
| src/TCPServer/Response.py   	| Contains the Response class which takes user input and returns the server response to that.                          	|
| src/ClientApp.py            	| Contains the PyQt5 GUI instance that allows the client of interacting with the server.                               	|
| src/TCPServerMultiClient.py 	| Contains the implementation of a class that is responsible for handling multiple clients at the same time.           	|
| src/GUI.py                  	| Contains the PyQt5 GUI class implementation.                                                                         	|
| src/HOST_PORT.json          	| Contains constants representing the host and port for the application.                                               	|

## Current Problems

Although the Server is able to handle multiple clients, it is using the same response class, so we can't let multiple users take the questionnaire at the same time
