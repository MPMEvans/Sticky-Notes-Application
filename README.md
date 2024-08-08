This is a basic sticky notes application written in Python using Django for the HTML and CSS portions for managing tasks on a locally hosted website. It supports adding, editing and deleting tasks.

To run the application, change your directory to where you have saved the files, and then in the command line type the following:
python main.py makemigrations
python main.py migrate
python main.py runserver

After typing the final command, something similar to this will appear:
System check identified no issues (0 silenced).
August 08, 2024 - 13:50:19
Django version 5.0.6, using settings 'bulletin_board.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

You can then go to the ip address specified at the "Starting development server at http://127.0.0.1:8000/", or your localhost server to use the application.
