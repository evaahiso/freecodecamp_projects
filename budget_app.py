class Category:

    def __init__(self, description):
        self.ledger = []
        self.balance = 0
        self.description = description
    
    def __repr__(self):
        title = self.description.center(30, "*") + "\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += item["description"][:23].ljust(23) + "{:.2f}".format(item["amount"]).rjust(7) + "\n"
            total += item["amount"]
        output = title + items + "Total: " + "{:.2f}".format(total)
        return output
    
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + category.description)
            category.deposit(amount, "Transfer from " + self.description)
            print(category.ledger)
            print(self.ledger)
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    total_amount = 0
    percentages = []
    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                total_amount += item["amount"]
    for category in categories:
        category_amount = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_amount += item["amount"]
        percentages.append((category_amount / total_amount) * 100)
    
    lines = ["100|", " 90|", " 80|", " 70|", " 60|", " 50|", " 40|", " 30|", " 20|", " 10|", "  0|"]
    for percentage in percentages:
        if percentage >= 100:
            for i, line in enumerate(lines):
                lines[i] += " o "
        elif percentage >= 90 and percentage < 100:
            for i in range(1, len(lines)):
                lines[i] += " o "
        elif percentage >= 80 and percentage < 90:
            for i in range(2, len(lines)):
                lines[i] += " o "
        elif percentage >= 70 and percentage < 80:
            for i in range(3, len(lines)):
                lines[i] += " o "
        elif percentage >= 60 and percentage < 70:
            for i in range(4, len(lines)):
                lines[i] += " o "
        elif percentage >= 50 and percentage < 60:
            for i in range(5, len(lines)):
                lines[i] += " o "
        elif percentage >= 40 and percentage < 50:
            for i in range(6, len(lines)):
                lines[i] += " o "
        elif percentage >= 30 and percentage < 40:
            for i in range(7, len(lines)):
                lines[i] += " o "
        elif percentage >= 20 and percentage < 30:
            for i in range(8, len(lines)):
                lines[i] += " o "
        elif percentage >= 10 and percentage < 20:
            for i in range(9, len(lines)):
                lines[i] += " o "
        elif percentage >= 0 and percentage < 10:
            for i in range(10, len(lines)):
                lines[i] += " o "
    
    # printing
    print("\n")
    print("Percentage spent by category")
    for item in lines:
        print(item)
    print("    ----------")
    longest_description = 0
    for category in categories:
        if len(category.description) > longest_description:
            longest_description = len(category.description)
    for i in range(longest_description):
        line = "    "
        for category in categories:
            if i < len(category.description):
                line += " " + category.description[i] + " "
            else:
                line += "   "
        print(line)

# testing
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
clothing.deposit(1000, "initial deposit")
clothing.withdraw(10.15, "groceries")
clothing.withdraw(15.89, "restaurant and more food for dessert")

create_spend_chart([food, clothing])