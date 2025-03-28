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

3. Then run the command:
```
$ source ./env/bin/activate

```
4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```
5. To create database schema run:
```
$ python setup_db.py 

```
6. To insert the 10 realistic tuples run:
```
$ python seed_data.py

```

7. To look at Library Items