# 💸 Personal Finance Tracker

---

## 💰 Introduction to the program 
 
The Personal Finance Tracker is a Python program that allows users to keep track of their transactions. This 
application allows users to add, view, update, or delete transactions, and they may request a summary of all 
transactions that shows the total amount of income and expenditure. Furthermore, they can add transactions 
from a text file to the JSON file and launch a GUI. It provides a command-line interface (CLI) and a graphical 
user interface (GUI) for easy interaction. This software will provide CRUD operations for managing financial 
transactions while using JSON for data persistence.  

---

## 📖 Guide on how to use the features  
 
## 🔧 CLI Interface:  
This program has 8 features. When the user runs the program, they will see those eight functions and be 
prompted to select which one they wish to utilize.

1️⃣ Add transaction – choice 1 

This feature allows the user to add a new transaction. The program will ask the user to enter amount as an 
integer, non-empty description, type as income or expense and date in the format ‘YYYY-MM-DD’. Then the 
transaction is saved to the system. 

2️⃣ View transactions – choice 2 

This feature let the user to view all the transactions they have entered. If there are no transactions a message 
will display saying that the transaction data is empty. This feature will display data classified with the 
description and amount, type of transaction and data after the description. For one description there might be 
multiple transaction details as the program classify and add the transaction details according to the description. 

3️⃣ Update transactions – choice 3 

If the user wants to update a previously entered transaction, this feature will help the user. The program will 
ask the user to enter the description of the transaction and number of the transaction they want to update and 
this feature lets the user to enter all the details of the particular transaction.

4️⃣ Delete transaction – choice 4 

In case the user has entered a transaction by mistake or no longer need it, they can use this feature to remove 
that transaction. User can enter the description and the number of the transaction which the user wants to 
remove and the program will delete it from records successfully. 

5️⃣ Display summary – choice 5 

Display summary feature provides you with the summary of the transactions. It displays the total of income 
and the total of expenses. This feature calculates separately, the total of the amount with the type of transaction 
‘income’ to get the total of income and ‘expense’ to get the total of expenses. 

6️⃣ Reading bulk transactions – choice 6 

If you have transactions stored in a text file, you can import them into the program and save them using option 
6. The program will ask you to enter the name of the text file with transaction data. If each line contained in 
the file is separated with a comma with information Description, Amount, Type and Date the program will 
import them and save them in the main file. 

7️⃣ Launch GUI – choice 7 

Opens a graphical user interface for more user-friendly and interactive environment for managing transactions. 

8️⃣ Exit – choice 8 

This feature allows the user to exit the program when the user is done with managing the transactions. 
 
## 🖼️GUI Interface :

When you select ‘Launch GUI’ option, a graphical user interface will open. This GUI displays a tabular 
representation of the transactions recorded in the Json file produced using the CLI method. It reads the 
transactions from the json file and displays the amount, description, type, and amount in columns in the GUI. 
There will be two buttons for search and reset along with a text box for the entry of the query which the user 
wants to search in this GUI. 

1️⃣ Search transaction 

The user can enter the Id, amount, description, type and date of the particular transaction in the text box which 
the user wants to filter out and the GUI will only display that selected transaction. User can reset the table to 
its original state by clicking the reset button. It will empty the text box as well. 

2️⃣ Sort transactions 

When the user clicks on a column heading in the transaction display table, it sorts the data based on that 
column in the ascending order. When the user clicks on description and type, it sorts in the alphabetical order. 
If the user clicks on amount, it will get sorted in the ascending order but the program will consider only the 
left most digit. For an example, if the values are 1000,300,4000,20000, the program will sort it like this, 1000, 
20000, 300, 4000. Clicking on the date will give the user the ascending order of the dates. When the user 
clicks on reset, the program will be back to the original state. 

---

## ✔️ Data validation 
 
This program maintains the accuracy of the user’s data by checking it during transaction entry and 
modifications.

🔹 For amount user can enter only an integer or a float value and for the description, user can’t keep that 
slot empty. 

🔹 User can enter either ‘Income’ or ‘Expense’ for the type of transaction and as for the date user can enter 
it in the format ‘YYYY-MM-DD’. 

🔹 When the user needs to enter the number of the transaction they want to delete or update, user can enter 
only a number corresponding to an existing transaction and for the description they can enter only an 
existing description. 

🔹 When entering the file name for bulk reading, user can enter an existing file name in the correct format. 

---

## 📌 Example for usage 
 
1️⃣ Add transaction 

🔸 Enter your choice: 1 

🔸 Enter the amount: 2000

🔸 Enter the description: salary 

🔸 Enter the type of transaction (income/expense): income

🔸 Enter the date: 2023-09-04

2️⃣ View transactions 

🔸 User can see descriptions numbered starting from 1 and transactions which belong to each description 
numbered starting from 1 after the particular description. 
 
3️⃣ Update transaction 

🔸 Choose the description and transaction number you want to update. 

🔸 Change the amount, description, type of transaction or date as needed.  
 
4️⃣ Delete transaction 

🔸 Select the description, transaction number you want to delete. 
 
5️⃣ Reading bulk transactions

🔸 Enter the file name: file_name.txt 
 
6️⃣ Display summary 

🔸 View the total income and total expenses based on transaction. 

---
 
## 🛠️ Set up instructions 
 
📌 Install python: 

Install python from python.org on your system. It is recommended that you download the 
latest version of python.

📌 Download the program: 

Download the ‘financetracker03.py’ file from the repository. 

📌 Install dependencies: 

if necessary, install the required dependencies (tkinter) using pip. 

📌 Run the program: 

Open a terminal or command prompt in the directory where the ‘fianacetracker03.py’ is 
located and run the program by typing the python file name, financetracker.py. 

🤑 For the better use, move the python file and the bulk read text file to a new folder so that the json file will be 
created in the same folder. 
