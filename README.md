# Socket Programming in Python

<!-- TODO: Add Project Description -->

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
   pip install -r requirements.txt
   ```

<!-- 1. Initialize the Database
  
    ```sh
    cd db
    python Database.py
    ``` -->

1. Run the application. Open two terminal windows. \
   one for the server and one for the client
   
   ```sh
   cd Chatbot
   python server.py
   python client.py
   ```
