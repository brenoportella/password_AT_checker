# PASSWORD AT CHECKER (PORTUGAL)
A script to check the status of passwords from AT (Portugal). 
### Requirements

Before starting, make sure you have Python and pip installed on your system.
- You can check by running:

 ```bash
python --version
pip --version
```
or, on Linux:

 ```bash
python3 --version
pip3 --version
```
### To install (WINDOWS):

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### To Install (LINUX):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
### Input File
Create a xlsx file. In the cell A1 insert the term "NIF", in B1 insert "PASSWORD" and in C1 insert "STATUS". In the roll bellow (A2:B2), insert your list of nifs and passwords, let the STATUS column blank. It will be write by the program.

|NIF | PASSWORD | STATUS|
|-------|-------|-------|
|123456789 | senha123 | |
|987654321 | teste456 | |

Before using the program, please indicate the relative path (relative to main.py) to your codes file (.xlsx) on the INPUT_EXCEL declaration in src/defines.py
