balance = 5000000
withdraw = int(input("Withdrawal Ammount: "))

# Is the amount a multiple of 10?
# Is the amount within the daily withdrawal limit?
# Does the user have sufficient funds in their account to make the withdrawal?

if withdraw % 10 == 0:
    if 50000 <= withdraw <= 1000000:
        if balance > withdraw:
            print("Ammount successfully withdrawn")
        else:
            print("I'm afraid you are broke")
    else:
        print("Amount is not within daily withdrawal limit")
else:
    print("Ammount is not a multiple of 10")