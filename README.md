# CMPT_354_project
A database application for CMPT 354 @ SFU

## Usage
  - There is a login and registration screen, although authentication has not been implemented. Feel free to use these features to create your own user
  - The Entire Appication can be used with our seeded daata - Ex) Alice Smith, USER_ID: 1 - can be used to test the application. 
  - A USER_ID is needed to perform features because of this. 

## How to Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command: (Note -  ensure your terminal window, powershell etc ,has permissions for script executions enabled.) It may look something like: 'Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass' depending on usage.
- macOS & Linux
```
$ source ./env/bin/activate
```
or
- Windows
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Generate Tuples: if an old library.db exists, setup_db.py deletes it and refreshes the tuples for ease of use and testing.
```
$ python setup_db.py
```

6. To run the app, run the command:
```
$ python app.py
```
