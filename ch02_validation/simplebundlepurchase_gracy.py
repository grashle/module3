# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:55:47 2018

@author: 612383423
"""
### Chapter 8: Mobile Data Bundle purchase program

def DataBundlePurchase(truePasscode, balance):
    counter = 0
    if passwordCheck(truePasscode):
        while counter < 3:
            if counter == 0:
                answer=input('''
                             Login successful. What do you want to do today? 
                             Press 1 to view your credit balance
                             Press 2 to purchase data
                             Press 3 to top up your account.
                             
                                 ''')
            else: 
                answer = input("Please, try again: ")
            if answer == '1': 
                return checkBalance(balance)
            elif answer =='2': 
                if checkNumber():
                    return buyData(balance)
                else:
                    return 'Sorry, your phone number is not valid.'
            elif answer == '3':
                return topupBalance(balance)
            elif checkType(answer, "1, 2 or 3") or checkLength(answer, 1):
                counter += 1
            else:
                counter += 1       
        return('locked out after 3 attempts') 
    else: 
        return 'locked out after 3 attempts'
    
    
def passwordCheck(truePasscode): 
    counter = 0
    while counter < 3:
      try:
        attempt = (input('Please enter your 4-digit password: '))
        if attempt == truePasscode:
            return True
        elif checkType(attempt, "numbers") or checkLength(attempt, 4):
            counter += 1
        else:
            counter += 1
            raise EOFError
      except EOFError:
        print("Sorry, that doesn't match our records.")
        continue # This causes it to continue
    return False

def checkLength(answer, length):
    try:
        if len(answer)!= length:
            raise ValueError
    except ValueError:
        print("Required number of digits: {}.".format(length))
        return True   
    return False

def checkType(answer, requirement):
    try:
        if not answer.isdigit():
            raise TypeError
    except TypeError:
        print("Type {} only please.".format(requirement))
        return True   
    return False

def checkBalance(balance):
    if balance > 0:
        return ( 'Your balance is £{}'.format(balance))
    else: 
        return ('Your balance is insufficient: £{}'.format(balance))
    
    
def checkNumber():     
    counter = 0
    while counter < 3:
      try:
        phone_number = input('Please enter your phone number: ')
        if checkType(phone_number, "numbers") or checkLength(phone_number, 2):
            counter += 1
        else:
            confirm_number = input ('Thanks. Please enter your number again to confirm: ')
            if phone_number == confirm_number:
                return True
            else: 
                counter2 = 0
                while counter2 < 3:
                    reconfirm_number = input('The number is not matching. Please, try again.')
                    if reconfirm_number == phone_number:
                        return True
                    else:
                        counter2 += 1
                return False
      except EOFError:
        print("Sorry, that doesn't match our records.")
        continue # This causes it to continue
    return False
    
def buyData(balance):
    print('\nThanks for confirming your number. Your current balance is £{}'.format(balance))
    print('\nAs you can only purchase in multiples of £5, the max you can spend is...')
    highest_price(balance)
    user_pays = (input('How much do you want to spend on data? multiples of £5 only, please: '))
    counter = 1
    while counter < 3:
        try:
            if checkType(user_pays, 'amount'):
                counter += 1
            elif float(user_pays) > float(balance):
                counter += 1
                raise Exception
            elif (int(user_pays)%5)!=0:
                counter += 1
                raise ArithmeticError
            else: 
                new_balance = float(balance)-float(user_pays)
                new_balance_2dp = round(new_balance, 2)
                return ('Purchase successful! Your new balance is £{}'.format(new_balance_2dp))
        except ArithmeticError:
            print('Sorry, the amount you requested is not a multiple of £5.')
        except Exception:
            print('Sorry, you don\'t have enough money to purchase. The max you can spend is:')
            highest_price(balance)
        user_pays = (input('How much do you want to spend on data? multiples of £5 only, please: '))
    return 'locked out after 3 attempts'
        
def highest_price(balance):
    int_balance = int(balance)
    for i in range (int_balance-5,int_balance):
        if(i%5==0):
            max = i
            print ('£',max)
            return
        
def topupBalance (balance):
    user_topup = (input('Your current balance is £{}. How much do you want to top up? multiples of £5 only, please: '.format(balance)))
    counter = 1
    while counter < 3:
        try:
            if checkType(user_topup, 'amount'):
                counter += 1
            elif (int(user_topup)%5)!=0:
                counter += 1
                raise ArithmeticError
            else: 
                new_topup_balance = float(balance)+float(user_topup)
                new_topup_balance_2dp = round(new_topup_balance, 2)
                return ('Purchase successful! Your new balance is £{}'.format(new_topup_balance_2dp))
        except ArithmeticError:
            print('Sorry, the amount you requested is not a multiple of £5.')
        user_topup = (input('Your current balance is £{}. How much do you want to top up? multiples of £5 only, please: '.format(balance)))
    return 'locked out after 3 attempts'
