def pay_taxes(sender,intermediary,amount,commision,imd_accounts,debts,player):
    print("/**************PAY TAXES**********/")
    print('pay_taxes_sender',sender)
    print('pay_taxes_intermediary',intermediary)
    print('amount',amount)
    print('pay_taxes_commission',commision)
    print('dents_sender',imd_accounts)
    print('debts',debts)
    print('player',player)

    if(player[sender] < amount+commision and player[sender]>commision):
        imd_accounts[intermediary] += commision
        player[sender] -= commision
    elif player[sender] < amount+commision and player[sender]<commision:
        imd_accounts[intermediary] += player[sender]
        debts[intermediary][sender] += commision-player[sender]
        player[sender]=0




def check_transaction(sender,receiver,amount,intermediary,fee,player_accounts,imd_accounts,debts):
    print('/********************CHECK TRANSACTIONS**************/')

    commission = (amount * fee) /100
    print('commission',commission)

    if player_accounts[sender] < commission + amount:
        pay_taxes(sender,intermediary,amount,commission,imd_accounts,debts,player_accounts)
        print("Transazione non disponibile")
    else :
        print("Transazione Disponibile")
        player_accounts[receiver] += amount
        imd_accounts[intermediary] += commission 
        player_accounts[sender] -= (commission + amount)
   


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
        print('/********************EX 1**************/')
        print(player_accounts)
        print(imd_accounts)
    return(player_accounts,imd_accounts,debts)

        
        
            
if __name__ == '__main__':
        
    res = ex1('0x5B23', '0xC78D' , '0x44AE' , '0x1612' , '0x90FF' , 1000 ,
        [ (('0x44AE', '0x5B23'),  800, '0x1612',  4),
          (('0x44AE', '0xC78D'),  800, '0x90FF', 10),
          (('0xC78D', '0x5B23'),  400, '0x1612',  8),
          (('0x44AE', '0xC78D'), 1800, '0x90FF', 12),
          (('0x5B23', '0x44AE'),  100, '0x1612',  2)
        ])
    
    print('result',res)
    
    