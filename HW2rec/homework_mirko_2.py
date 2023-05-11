def pay_debts(receiver,player_accounts,imd_accounts):
    '''print("/**************DEBTS**********/")'''
    dict_of_occurenceris = {}
    for value in player_accounts[receiver][1].values():
        if value !=0 and value not in dict_of_occurenceris.keys():
            dict_of_occurenceris[value] = 1
        elif value in dict_of_occurenceris.keys():
            dict_of_occurenceris[value] += 1

    for imd_keys in player_accounts[receiver][1].keys():
        for imd_debts in player_accounts[receiver][1].values():
            if imd_debts in dict_of_occurenceris.keys():
                if player_accounts[receiver][0] <=0 or player_accounts[receiver][1][imd_keys] ==0:
                    print()
                else:
                    player_accounts[receiver][1][imd_keys] -= player_accounts[receiver][0] / dict_of_occurenceris[imd_debts]
                    player_accounts[receiver][0] -= player_accounts[receiver][0] / dict_of_occurenceris[imd_debts]

    print(player_accounts)




def pay_taxes(sender,intermediary,amount,commision,imd_accounts,debts,player):
    if(player[sender][0] < amount+commision and player[sender][0]>commision):
        imd_accounts[intermediary] += commision
        player[sender][0] -= commision
    elif player[sender][0] < amount+commision and player[sender][0]<commision:
        imd_accounts[intermediary] += player[sender][0]
        player[sender][1][intermediary]+= commision-player[sender][0]
        debts[intermediary][sender] += commision-player[sender][0]
        player[sender][0]=0




def check_transaction(sender,receiver,amount,intermediary,fee,player_accounts,imd_accounts,debts):
    commission = (amount * fee) /100
    if player_accounts[sender][0] < commission + amount:
        pay_taxes(sender,intermediary,amount,commission,imd_accounts,debts,player_accounts)
    else :
        player_accounts[receiver][0] += amount
        imd_accounts[intermediary] += commission 
        player_accounts[sender][0] -= (commission + amount)
        pay_debts(receiver,player_accounts,imd_accounts)



def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log):
    player_accounts = {acn1: [init_amount,{imd_acn1:0,imd_acn2:0}], acn2: [init_amount,{imd_acn1:0,imd_acn2:0}], acn3: [init_amount,{imd_acn1:0,imd_acn2:0}]}
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
    
    