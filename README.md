## Python

First install python and add it to your environment variables in Windows so you can use it in powershell.

## Installing dependencies
`pip install requests`\
`pip install openpyxl`\

## Setting up League Client
You need to do these steps every time you restart your League Client.\
Get the port & password of the League Client\
1. Start the League Client\
2. Find your game folder e.g. C:\Games\League of Legends\
3. Open the `lockfile` file and copy what is in it. It is formatted like this: `Process Name : Process ID : Port : Password : Protocol`\

Paste the values in the `config.py`\
1. Port in PORT_NUMBER\
2. Password in USERNAME_PASSWORD after the `:`\

Run the program with Python: `py main.py`\
