Notes: 
To convert .ipynb (notebook file) to .py command on cmd is:
	jupyter nbconvert --to script xxx.ipynb
To create .exe file, delete all 'build' and 'dist' and '.spec' files, command on cmd is:
	pyinstaller --onefile xxx.py
For each update, remember to:
	Change the version number in banner, as well as the version number when writing file.

GOAL:
Read from 2 inputs, collect certain data from each, and create a readable and printable pdf.
This project will use the Python libraries such as Pandas for reading excel sheets, and reportlab for creating PDF

This project is 90% done, however need to test more and polish the structure.
Main notebook: Project2.ipynb
