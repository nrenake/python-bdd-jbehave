from features.utils.BankAccountManager import BankAccountManager

ban1=BankAccountManager(100,300)
ban1.transferAmountFromSavingToAccount(200)
print(ban1.savingAccountBalance)
