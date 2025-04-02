# CMPT_354_project
A database application for CMPT 354 @ SFU

## How to Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command: (Note -  ensure your terminal wimndow, powershell etc ,has permissions for script executions enabled.)
```
$ source ./env/bin/activate
```
or
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