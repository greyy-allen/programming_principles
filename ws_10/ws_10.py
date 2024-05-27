class GoCard:
    def __init__(self, initialBal):
        self.balance = round(initialBal, 2)
        self.record = [initialBal]

    def ride(self, amount):
        self.balance -= amount
        self.balance = round(self.balance, 2)
        self.record.append((-amount))

    def topup(self, amount):
        self.balance += amount
        self.balance = round(self.balance, 2)
        self.record.append((amount))

    def getBalance(self):
        return self.balance

    def print_sta(self):
        print("Statement: ")
        print("{:<20} {:<15} {:<15}".format("Event", "Amount($)", "Balance($)"))
        print("{:<20} {:<15} {:<15}".format("Initial Balance", " ", self.record[0]))

        current_balance = self.record[0]

        for i, amount in enumerate(self.record):
            if i != 0 and amount < 0:
                current_balance += amount
                amount = abs(amount)
                print("{:<20} {:<15} {:<15}".format("Ride", amount, round(current_balance, 2)))
            else:
                current_balance += amount
                amount = abs(amount)
                print("{:<20} {:<15} {:<15}".format("Top Up", amount, round(current_balance, 2)))

        print("{:<20} {:<15} {:<15}".format("Final Balance", " ", round(current_balance, 2)))

bal = float(input("Current Balance is: "))
myGoCard = GoCard(bal)
command=input("? ")

while command.strip() != 'q':

    cm = command.split()

    if len(cm) == 2 and cm[0] == 'r':
        try:
            amount = float(cm[1])
            myGoCard.ride(amount)
        except:
            print("Bad Command")

    elif len(cm) == 2 and cm[0] == 't':
        try:
            amount = float(cm[1])
            myGoCard.topup(amount)
        except:
            print("Bad Command")

    elif len(cm) == 1 and cm[0] == 'b':
        print(myGoCard.getBalance())

    else:
        print("Bad Command")

    command = input("? ")

myGoCard.print_sta()
