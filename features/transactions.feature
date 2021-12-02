Feature: Validation of transactions within same user accounts i.e saving and current accounts

#  Background: User is logged into his account
#    Given user logged into bank portal
#    And on account page

  Scenario Outline:
    Given Executing <tcId>
    And user has <currentAccount> amount in current account
    And <savingsAccount> amount in saving account
    When user transfers amount of <transferAmount> from saving account to current account
    Then validate balance in current and saving accounts are correct for <testStatus>

    Examples:
      | tcId                            | currentAccount | savingsAccount | transferAmount | testStatus |
      | TC01 - Valid transfer           | 100            | 500            | 250            | PASS       |
      | TC02 - Valid Transfer           | 35             | 800            | 76             | PASS       |
      | TC03 - Zero balance transfer    | 0              | 0              | 35             | FAIL       |
      | TC04 - Negative amount transfer | 10             | -35.5          | 13             | FAIL       |
      | TC05 - Over draft transfer                       | 100            | 30             | 70             | FAIL       |
      | TC06 - Invalid decimal numeration transfer       | 100            | 30             | 0.000001       | FAIL       |
##      | TC07 - Only numeric amount transfers are allowed | 100            | 30             | SDGG_SD        | FAIL       |
      | TC08 - Valid transfer  - Boundary Value          | 100            | 30             | 30             | PASS       |
      | TC09 - Valid transfer  - Boundary Value + 1      | 100            | 30             | 31             | FAIL       |
      | TC10 - Valid transfer  - Boundary Value - 1      | 100            | 30             | 29             | PASS       |