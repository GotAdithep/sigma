class xx:
    def __init__(self):

        self.account_database = []


    def create_account(self,num, type, name, init_balance):
        index = self.search_account_db(num)
        if index == -1:
            account = {}
            account["account_number"] = num
            account["type"] = type
            account["account_name"] = name
            account["balance"] = init_balance
            self.account_database.append(account)
        else:
            print("Account", num, "already exists")


    def delete_account(self,num):
        index = self.search_account_db(num)
        if index != -1:
            print("Deleting account:", self.account_database[index]["account_number"])
            del self.account_database[index]
        else:
            print(num, "invalid account number; nothing to be deleted.")


    def search_account_db(self, account_num):
        for i in range(len(self.account_database)):
            if self.account_database[i]["account_number"] == account_num:
                return i
        return -1


    def deposit(self,account_num, amount):
        index = self.search_account_db(account_num)
        if index != -1:
            print("Depositing", amount, "to", self.account_database[index]["account_number"])
            self.account_database[index]["balance"] += amount
        else:
            print(account_num, "invalid account number; no deposit action performed.")


    def withdraw(self,account_num, amount):
        index = self.search_account_db(account_num)
        if index != -1:
            if self.account_database[index]["balance"] >= amount:
                print("Withdrawing", amount, "from", self.account_database[index]["account_number"])
                self.account_database[index]["balance"] -= amount
            else:
                print("withdrawal amount", amount, "exceeds the balance of", self.account_database[index]["balance"], "for",
                      account_num, "account.")
        else:
            print(account_num, "invalid account number; no withdrawal action performed.")


    def show_account(self, account_num):
        index = self.search_account_db(account_num)
        if index != -1:
            print("Showing details for", self.account_database[index]["account_number"])
            print(self.account_database[index])
        else:
            print(account_num, "invalid account number; nothing to be shown for.")

a=xx()
a.create_account("0000", "saving", "David Patterson", 1000)
a.create_account("0001", "checking", "John Hennessy", 2000)
a.create_account("0003", "saving", "Mark Hill", 3000)
a.create_account("0004", "saving", "David Wood", 4000)
a.create_account("0004", "saving", "David Wood", 4000)
print(a.account_database)
a.show_account('0003')
a.deposit('0003', 50)
a.show_account('0003')
a.withdraw('0003', 25)
a.show_account('0003')
a.delete_account('0003')
a.show_account('0003')
a.deposit('0003', 50)
a.withdraw('0001', 6000)