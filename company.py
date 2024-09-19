class Account:
    def __init__(self, account_id,company):
        self.account_id =account_id
        self.company = company
        self.income = 0
        self.expense =0
        self.is_expense_approved = False

    def add_income(self, amount):
        self.income += amount
    def add_expense(self, amount):
        if self.is_expense_approved:
            self.expense += amount
        else:
           print(" Expenses are not approved at this time")
    def approve_expense(self):
        self.is_expense_approved = True

    def get_balance(self):
        return self.income - self.expense
class company:
    def __init__(self, name , owner):
        self.name = name
        self.owner = owner
        self.accounts = [ ]
    def create_account(self, account_id):
        account = Account(account_id, self)
        self.accounts.append(account)
        return account

    def get_accounts(self):
       return self.accounts
   
 #role can b admin or owner or a user   
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
    def create_company(self , company_name):
        if self.role =='owner' or self.role == 'website_owner' :
            return company(company_name, self)
        else:
             print(f"{self.username} is not allowed to create a company.")
             return None
    def create_account(self, company, account_id):
        if self == company.owner:
            return company.create_account(account_id)       
        else: 
            print("only the comapny owner can create account")
            return None
    def add_income(self, account , amount):
        if self.role == "admin":
            account.add_income(amount)
        else:
            print ("only admin can add in it")       
    def add_expense(self, account, amount ):
        if self.role != "admin":
           account.add_expense(amount)
        else:
            print("admins cannot submit Expense")
    def approve_expense(self , account):
        if self.role == "admin" :
            account.approve_expense()      
        else:
            print ("only admins can be approve the expenses")  
             
    def view_reports(self , company):
        if self.role =="owner" and self == company.owner:
            return[ account.get_balance()for account in company.get_accounts()]
        elif self.role =="website_owner":
            return[( company.name , [account.get_balance() for account in company.get_accounts()])]
        else:
            print("unauthorized access")
            return None
website_owner = User("website_admin" , "website_owner")
company_owner = User("muntaha", "owner")
admin = User("admin_user" , "admin")
regular_user = User("regular_user", "regular")



#by creating account and company
my_company = company_owner.create_company("Hicks Tec")
account_1  = company_owner.create_account(my_company, "B001")   
#admin (adding income)
admin.add_income( account_1, 1000)


#regular users submitted expenses
regular_user.add_expense(account_1, 600) 
 #admins approved expenses
admin.approve_expense(account_1)
   
regular_user.add_expense(account_1, 600)

# View 
print("Company owner's report:", company_owner.view_reports(my_company))
print("Website owner's report:", website_owner.view_reports(my_company))