
# Expense Tracker v2.0: Business
# Requirements

import json

def add_new_expense(expense_list):
     expense_item_new={}
     
     item_name=input("item Name : ")
     item_value= int(input("item value : "))
     item_category=input("item category : ")
           
     expense_item_new.update({"name"    : item_name } )
     expense_item_new.update({"amount"  : item_value } )
     expense_item_new.update({"category": item_category } )
     
     print(expense_item_new)
     print(type(expense_item_new))
     
     expense_list.append (expense_item_new)
          
#------------------------------------------------------------
def save_data_List_file(expense_list):
     
     print("Save data")
     print(expense_list)
         
     result=""
     
     for data_dic in expense_list:
         result += json.dumps(data_dic) + "\n"
          
     print("\n",result)
     
    
     with open("data1_expense.txt", "w") as f:
        f.write(result)

     #open and read the file after the appending:

     with open("data1_expense.txt") as f:
        print("\n Save one by one item : \n",f.read(),"\n\n")
     
     
     #----------------------------------------------------
     print("\n Save Shortcut method : ")       
     with open("data1_expense.json", "w") as f:
        json.dump(expense_list, f, indent=4)
     print("\nData saved successfully! (Shortcut method ) ")
        
     with open("data1_expense.txt") as f:
       print(" \n",f.read(),"\n\n")

#----------------------------------------------------
def load_data_from_file_to_List():

    print("Load Data")
    result = []

    with open("data1_expense.txt", "r") as f:

        for line in f:
            data_dic = json.loads(line)
            result.append(data_dic)

    return result
  
#----------------------------------------------------
  
def check_file_exists_or_not():
    
   try:
        with open("data1_expense.txt", "r") as f:
           print("File not Exists")
           return True

   except FileNotFoundError:
           print("File not Exists")
           return False 

#----------------------------------------------------
def view_all_expense(data):   
    print("Name  :  Amount  :  Category ")  
    for res in data:
       print(f"{res["name"]}   :   {res["amount"]}     :    {res["category"]} ")  

#----------------------------------------------------
def view_category_wise_expense(data):   
   
   

    category_summary = {}

    for res in data:
        category = res["category"]
        amount = res["amount"]
        category_summary[category] = category_summary.get(category, 0) + amount
        
    print("category_summary : ",category_summary)
    print("Category   :   Amount     :   no_of_items  ")
     
    for category, amount in category_summary.items():
        no_of_items= no_of_items = sum( 1 for res in data if res["category"] == category )
        print(f"{category}   :   {amount}  : ({no_of_items}) " )
    
    max_category, max_amount = max(     category_summary.items(),     key=lambda item: item[1]    )
    print("Max (Category  &  Amount) : ", max_category, max_amount)
    
    min_category, min_amount = min(     category_summary.items(),     key=lambda item: item[1]    )
    print("Min (Category  &  Amount) : ", min_category, min_amount)
        
        
    total_category_count =  len(category_summary)   
    total_amount         =  sum(category_summary.values())   
    avg_amt              =  total_amount/total_category_count
    
    print(f"Total_Category_amount_Average  :  {total_category_count} ,  {total_amount} , {avg_amt} " )
        
    total_noof_items = len(data)
    
    
#----------------------------------------------------
def view_category_wise_count(data):   
   
    print("Category   :   Amount")

    category_summary = {}

    for res in data:
        category = res["category"]
        amount = 1
        category_summary[category] = category_summary.get(category, 0) + amount
    print("category_summary : ",category_summary)
    for category, amount in category_summary.items():
        print(f"{category}   :   {amount}")
        
    total_amount =  sum(category_summary.values())   
    print("Total_amount : ", total_amount)
    
#----------------------------------------------------
def view_specific_category(data):
     
    category=input("\nEnter category Name : ") 
      
    print("Category   :   Amount")

    category_summary = {}

    for res in data:
        if res["category"]==category:
           category = res["category"]
           amount = res["amount"]
           category_summary[category] = category_summary.get(category, 0) + amount
           print(f"{category}   :   {amount}")
           
    print("category_summary : ",category_summary)
    for category, amount in category_summary.items():
        print(f"{category}   :   {amount}")
        
    total_amount =  sum(category_summary.values())   
    print("Total_amount : ", total_amount)

    
#=====================================================================================
#=====================================================================================

expense_list =[]
expense_category_list={}

if check_file_exists_or_not():
   expense_list=load_data_from_file_to_List()
   print("\nExisting File Data : ", expense_list)
else: 
   with open("data1_expense.txt", "w") as f:
        print("Create New File ")
  
while True: 
  
  print("\n")
  print("    1: add expense , 2: edit expense 3: delete expense  \n" \
        "    4: view all expense, 5: View category wise expense 6: View category wise count 7: view specific category \n" \
        "    8:    9: Save data  0: Quit \n")
  
  a=int(input("Enter No : "))
  
  if a==1:
    print("\nExpense List (before insert) : " , expense_list) 
    add_new_expense(expense_list)
    print("\nExpense List (After insert ): " , expense_list) 
    save_data_List_file(expense_list)
    
  elif a==4:   
    view_all_expense(expense_list)
    
  elif a==5:   
     view_category_wise_expense(expense_list)
  
  elif a==6:   
    view_category_wise_count(expense_list)
  
  elif a==7:   
      view_specific_category(expense_list)
          
  elif a==8:
      print("Load Data ")
      
  elif a==9:
    print("Save Data")
    save_data_List_file(expense_list)
    print("Load Data ")
    expense_list=load_data_from_file_to_List()
    print( expense_list)  
  
       
  elif a==0:
    print("Exit Program")
    break
      
          
  