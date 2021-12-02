from behave import *

from utils.BankAccountManager import BankAccountManager


@given('Executing {tcId}')
def step_impl(context, tcId):
    print('Executing TC - ', tcId)


# @given('executing {tcId} and expected test status {testStatus}')
# def step_impl(context, tcId, testStatus):
#     context.tcId = tcId
#     context.testStatus = testStatus


@given('user has {currentAccount:g} amount in current account')
def step_impl(context, currentAccount):
    context.curAmt = currentAccount


@given('{savingsAccount:g} amount in saving account')
def step_impl(context, savingsAccount):
    context.savAmt = savingsAccount


@when('user transfers amount of {transferAmount:g} from saving account to current account')
def step_impl(context, transferAmount):
    context.traAmt = transferAmount
    context.actualStatus = 'PASS'
    if (context.traAmt < 0 or context.traAmt < 0.001):
        context.actualStatus = 'FAIL'
    elif context.traAmt > context.savAmt:
        context.actualStatus = 'FAIL'
    else:
        context.bam = BankAccountManager(context.curAmt, context.savAmt)
        context.bam.transferAmount(context.traAmt)


@then('validate balance in current and saving accounts are correct for {testStatus}')
def step_impl(context, testStatus):
    assert (context.actualStatus == testStatus)
    if testStatus == 'PASS':
        assert (context.bam.currentActBalance == context.curAmt + context.traAmt)
        assert (context.bam.savingAccountBalance == context.savAmt - context.traAmt)
