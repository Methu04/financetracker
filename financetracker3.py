# Importing modules
import tkinter as tk
from tkinter import ttk
from tkinter import END
import json
from datetime import datetime

# Global dictionary to store transactions
transactions = {}

# File handling functions
def load_transactions():
    global transactions
    try:
        with open("cw.json","r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        save_transactions()
        

def save_transactions():
    global transactions
    with open("cw.json","w") as f:
        f.write(json.dumps(transactions,indent =1))


def read_bulk_transactions_from_file():
    #taking user inputs for the particular json file name
    file_name = input('Enter the file name : ')
    try:
        with open(file_name, 'r') as fo:
            for line in fo:
                line = line.strip().split(',')
                #checking whether the list contain 4 items
                if len(line) == 4:
                    Description = line[0]
                    Amount = float(line[1])
                    Type = line[2].capitalize()
                    Date = line[3]
                    
                #If the description not in transaction, it will create a new key and an empty list
                if Description not in transactions:
                    transactions[Description] = []
                    #then it will append the values
                transactions[Description].append({"Amount":Amount,"Type":Type,"Date":Date})
            save_transactions()
        print("Transaction added successfully !!!")
    except:
        print('Enter file name in format (file_name.txt)')

# Error handling function        
def errors_in_input(data,input_statement,error_message = ("Enter correct data !")):
    while(True):
        #Handling the error when entering the amount - empty / letters / characters
        if data == "Amount" :    
            try :
                value = float(input(input_statement))

            except:
                # If the user input empty / letters / characters , error message will display
                print(error_message)
                
            else:
                # If there's no error , value will be returned
                return value
            
        # If the user input empty / letters / characters, program will ask the user to enter the correct value continuously

        if data == "TypeOfTransaction" :  
            value = input(input_statement).capitalize()
            if value == "Income" or value == "Expense":
                return value
            else:
                continue
        # If the discription is empty , error message will display
        
        if data == "Decsription" :
            value = input(input_statement)
            if value:
                return value
            else:
                print(error_message)
                continue

        # If the date is not in the given format the error message will display
        
        if data == "Date":
            value = input(input_statement)
            try:
                value = datetime.strptime(value,'%Y-%m-%d').date()
                return str(value)
            except ValueError:
                print(error_message,"type date in yyyy-m-d")
                continue

# Feature implementations
def add_transaction():
    global transactions
    #Taking user inputs
    Amount = errors_in_input("Amount","Enter the amount : ")
    Description = errors_in_input("Decsription","Enter the description: ")
    TypeOfTransaction = errors_in_input("TypeOfTransaction","Enter the type of transaction (income/expense) : ")
    Date = errors_in_input("Date","Enter the date : ")
    #creating transaction dictionary
    transaction = {"Amount":Amount,"Type":TypeOfTransaction,"Date":Date}
    #Adding the transaction to the relevant description
    # transaction dictionary with the same description will get appended to a list to that description as the key in the main dictionary
    if Description in transactions:
        transactions[Description].append(transaction)
    else:
        transactions[Description] = [transaction]
    save_transactions()
    print("Transaction saved successfully !!!")

def view_transactions():
    #if the mainlist is empty
    if len(transactions) == 0 :
        print("Transaction data is empty.")

    #displaying transactions one by one under the description
    count = 0    
    for Descript, transaction_list in transactions.items():
        #giving the description a number
        count += 1
        print(f"{count}.{Descript}:")
        i = 0
        for expense in transaction_list:
            #giving each transaction a number under the description
            i += 1
            #getting values from the dictionary
            amount = expense.get('Amount')
            date = expense.get('Date')
            TypeOfTransaction = expense.get('Type')
            print(f"{i} . Amount: {amount} |Type: {TypeOfTransaction} | Date: {date}")
        print()

def update_transaction():
    if len(transactions) == 0 :
        print("Transaction data is empty.")
    else:
        view_transactions()
        #using the loop checking whether the entered description exist, if not ask the user to enter the description again
        while True:
            trans_desc = input("Enter transaction description you want to update : ")
            if trans_desc in transactions:
                break
            else:
                print("Enter valid description !!!")
                continue
        #using the loop checking whether the entered number exist, if not ask the user to enter the number again
        while True:
            try:
                update_trans = int(input("Enter the transaction number : "))
                #if the user input a letter/space/empty , the error message will display
            except ValueError:
                print("Enter correct data !!!")
            else:
                if 0 < update_trans <= len(transactions[trans_desc]):
                    break
                else:
                    print("Transaction number doesn't exist")
                    continue
        #if there's no error, ask user to input data to be updated
        Amount = errors_in_input("Amount","Enter the amount : ")
        Decsription = errors_in_input("Decsription","Enter the description : ")
        TypeOfTransaction = errors_in_input("TypeOfTransaction","Enter the type of transaction (income/expense) : ")
        Date = errors_in_input("Date","Enter the date : ")
        # accessing the transaction for the given transaction and index of the transaction in the value list
        # [update_trans - 1] should be taken as the user give the number of the transaction , not the index
        transactions[trans_desc][update_trans - 1] = {"Amount":Amount,"Type":TypeOfTransaction,"Date":Date}
        print(f"Transaction {update_trans} is updated successfully !!!")
        save_transactions()
        view_transactions()

def delete_transaction():
    if len(transactions) == 0 :
        print("Transaction data is empty.")
    else:
        view_transactions()
        #using the loop checking whether the entered description exist, if not ask the user to enter the description again
        while True:
            trans_desc = input("Enter transaction description you want to delete : ")
            if trans_desc in transactions:
                break
            else:
                print("Enter valid description !!!")
                continue
        #using the loop checking whether the entered number exist, if not ask the user to enter the number again
        while True:
            try:
                delete_trans = int(input("Enter which transaction you want to delete : "))
            #if the user input a letter/space/empty , the error message will display
            except ValueError:
                print("Enter correct data !!!")
            else:
                if 0 < delete_trans <= len(transactions[trans_desc]):
                    break
                else:
                    print("Transaction number doesn't exist")
                    continue
        #deleting the transaction according to the given description and transaction number
        #[delete_trans - 1] is taken to calculate the index
        del transactions[trans_desc][delete_trans - 1]
        print(f"Transaction {delete_trans} is deleted !!!")
        #After deleting , if the list of the description is empty, removing the description
        if len(transactions[trans_desc]) == 0:
            del transactions[trans_desc]
        save_transactions()
        view_transactions()

def display_summary():
    view_transactions()
    # Displaying total amount of expenses and income
    total_income = 0
    total_expenses = 0
    #checking the type of transaction and calculating the total income and expenses seperately
    for key,transaction in transactions.items():
        for expense in transaction:
            if "Type" in expense:
                if expense["Type"] == "Income":
                     #if the type is Income, getting the value of the amount and adding it to the total_income
                    total_income += expense.get("Amount")
                elif expense["Type"] == "Expense":
                    #if the type is Expense, getting the value of the amount and adding it to the total_expense
                    total_expenses += expense.get("Amount")

    print (f"Total income = {total_income} and total expenses = {total_expenses}")

class FinanceTrackerGUI:
    def __init__(self, root):
        #root window title
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        #default size
        self.root.geometry('1000x600')
        #theme colour
        self.style = ttk.Style()
        self.style.theme_use('clam')
        #loading transactions
        self.transactions = self.load_transactions("cw.json")
        self.original_transactions = self.transactions.copy()

    def create_widgets(self):
        # Frame for table and scrollbar
        self.frame = ttk.Frame(self.root,relief = tk.GROOVE)
        self.frame.pack(fill = tk.BOTH,expand = True)


        # Treeview for displaying transactions
        self.table = ttk.Treeview(self.frame,columns = ("Transaction_ID","Description","Amount","Type","Date"), show='headings')
        
        self.table.heading("Transaction_ID",text = "Transaction ID")
        self.table.heading("Description",text = "Description",command=lambda: self.sort_by_column("Description", False))        
        self.table.heading("Amount",text = "Amount",command=lambda: self.sort_by_column("Amount", False))
        self.table.heading("Type",text = "Type",command=lambda: self.sort_by_column("Type", False))
        self.table.heading("Date",text = "Date",command=lambda: self.sort_by_column("Date", False))

        
        self.desc_button = ttk.Button(self.root,text = "Description",command=lambda: self.sort_by_column("Description", True))
        self.desc_button.pack(side = "left",padx = 10,pady = 10)
        self.amount_button = ttk.Button(self.root,text = "Amount",command=lambda: self.sort_by_column("Amount", True))
        self.amount_button.pack(side = "left",padx = 10,pady = 10)
        self.type_button = ttk.Button(self.root,text = "Type",command=lambda: self.sort_by_column("Type", True))
        self.type_button.pack(side = "left",padx = 10,pady = 10)
        self.date_button = ttk.Button(self.root,text = "Date",command=lambda: self.sort_by_column("Date", True))
        self.date_button.pack(side = "left",padx = 10,pady = 10)

        self.table.column("Transaction_ID", anchor='center')
        self.table.column("Description", anchor='center')
        self.table.column("Amount", anchor='center')
        self.table.column("Type", anchor='center')
        self.table.column("Date", anchor='center')
        
        self.table.pack(fill = tk.BOTH,expand = True)
        

        # Scrollbar for the Treeview
        self.scrollbar = ttk.Scrollbar(self.table,orient = "vertical",command = self.table.yview)
        self.table.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.pack(side = "right",fill = "y")


        # Search bar and button
        self.search_bar = tk.StringVar()
        self.search_entry = ttk.Entry(self.root,textvariable= self.search_bar)
        self.search_entry.pack(side = "top",padx = 10,pady = 10)
        self.search_button = ttk.Button(self.root,text = "Search",command = self.search_transactions)
        self.search_button.pack(side = "top",padx = 10,pady = 10)


        #reset button
        self.reset_button = ttk.Button(self.root,text = "Reset",command = self.reset_transactions)
        self.reset_button.pack(side = "right",padx = 10,pady = 10)

    def load_transactions(self, filename):
            try:
                with open(filename,"r") as f:
                    transactions = json.load(f)
                    return transactions
            except FileNotFoundError:
                self.transactions = {}

    def display_transactions(self, transactions):
            # Remove existing entries
            for data in self.table.get_children():
                self.table.delete(data)
            # Add transactions to the treeview
            trans_id = 0
            for self.descript, self.transaction_list in self.transactions.items():
                trans_id+1
                for self.expense in self.transaction_list:
                    trans_id+=1
                    self.table.insert('', index='end', values=(trans_id,
                                      f'{self.descript}',
                                      self.expense['Amount'],
                                      self.expense['Type'],
                                      self.expense['Date']))

    def search_transactions(self):
            #creating a temp count for the filtered transactions
            temp_cnt = 0
            #getting the search entry as the query
            query = self.search_entry.get()
            #clears existing entries from the Treeview
            for data in self.table.get_children():
                self.table.delete(data)
            #iterates over the transaction data and insert matching transactions into the Treeview
            for keys, values in self.transactions.items():
                for transaction in values:
                    if (query in str(keys) or
                        query in str(transaction['Amount']) or
                        query in str(transaction['Date']) or
                        query in str(transaction['Type'])):
                        temp_cnt += 1
                        self.table.insert('',index='end',values=(temp_cnt,
                                      f'{keys}',
                                      transaction['Amount'],
                                      transaction['Type'],
                                      transaction['Date']))

    def sort_by_column(self, col, reverse):
            #retriew the elements from the Treeview
            elements = self.table.get_children("")
            
            #creates a list of tuples containing values and corresponding Id
            data = []
            for i in elements:
                value = self.table.set(i,col)
                data.append((value,i))
                
            #sort the list of tuples
            if reverse:
                data.sort(reverse = True)
            else:
                data.sort()
            #moves the Treeview entries according to the sorted order
            for count in range(len(data)):
                self.table.move(data[count][1],"",count)

    def reset_transactions(self):
            # clears the search entry box
            self.search_entry.delete(0,END)
            #displays the original transactions
            self.display_transactions(self.original_transactions)

#launches the GUI for the program                
def launch_gui():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()


def main_menu():
    load_transactions()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Read bulk transactions from file")
        print("7. Launch GUI")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            read_bulk_transactions_from_file()
        elif choice == '7':
            launch_gui()
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()   
