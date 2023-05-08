def pay_debts(receiver,player_accounts,imd_accounts,debts):
    print("/**************DEBTS**********/")
    max_debts = 0
    intermediary =""
    print(receiver)
    print(player_accounts)
    print(imd_accounts)
    print(debts)
    for key in debts.keys():
        print(key)
        if max_debts < debts[key][receiver]:
            max_debts = debts[key][receiver]
            intermediary=key
            print('dentro if',intermediary)
    
    if intermediary != '':
        debts[intermediary][receiver] -= player_accounts[receiver]
        
    #print(receiver,intermediary,max_debts)

        


def pay_taxes(sender,intermediary,amount,commision,imd_accounts,debts,player):
    if(player[sender] < amount+commision and player[sender]>commision):
        imd_accounts[intermediary] += commision
        player[sender] -= commision
    elif player[sender] < amount+commision and player[sender]<commision:
        imd_accounts[intermediary] += player[sender]
        debts[intermediary][sender] += commision-player[sender]
        player[sender]=0




def check_transaction(sender,receiver,amount,intermediary,fee,player_accounts,imd_accounts,debts):

    commission = (amount * fee) /100
    if player_accounts[sender] < commission + amount:
        pay_taxes(sender,intermediary,amount,commission,imd_accounts,debts,player_accounts)
    else :
        player_accounts[receiver] += amount
        imd_accounts[intermediary] += commission 
        player_accounts[sender] -= (commission + amount)
        pay_debts(receiver,player_accounts,imd_accounts,debts)



def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log):
    player_accounts = {acn1: init_amount, acn2: init_amount, acn3: init_amount}
    imd_accounts = {imd_acn1: 0, imd_acn2: 0}
    debts = {imd_acn1: {acn1: 0, acn2: 0, acn3: 0}, imd_acn2: {acn1: 0, acn2: 0, acn3: 0}} 
    for transaction in transact_log:
        sender, receiver = (transaction[0])
        amount = transaction[1]
        intermediary = transaction[2]
        fee = transaction[3]
        check_transaction(sender,receiver,amount,intermediary,fee,player_accounts,imd_accounts,debts)
    return(player_accounts,imd_accounts,debts)

        
        
            
if __name__ == '__main__':
        
    res = ex1('0x5B23', '0xC78D' , '0x44AE' , '0x1612' , '0x90FF' , 1000 ,
        [ (('0x44AE', '0x5B23'),  800, '0x1612',  4),
          (('0x44AE', '0xC78D'),  800, '0x90FF', 10),
          (('0xC78D', '0x5B23'),  400, '0x1612',  8),
          (('0x44AE', '0xC78D'), 1800, '0x90FF', 12),
          (('0x5B23', '0x44AE'),  100, '0x1612',  2)

        ])
    
    #print('result',res)
    
    