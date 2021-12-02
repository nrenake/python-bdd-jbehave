class BankAccountManager:
    def __init__(self, currentActBalance, savingAccountBalance):
        self.currentActBalance = currentActBalance
        self.savingAccountBalance = savingAccountBalance

    def transferAmountFromSavingToAccount(self, transferAmount):
        self.currentActBalance = self.currentActBalance + transferAmount
        self.savingAccountBalance = self.savingAccountBalance - transferAmount