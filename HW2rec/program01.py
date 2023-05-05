def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log):
    # Inizializzazione dei conti dei giocatori e degli intermediari
    player_accounts = {acn1: init_amount, acn2: init_amount, acn3: init_amount}
    imd_accounts = {imd_acn1: 0, imd_acn2: 0}
    debts = {imd_acn1: {acn1: 0, acn2: 0, acn3: 0}, imd_acn2: {acn1: 0, acn2: 0, acn3: 0}}

    # Ciclo sulle transazioni
    for transaction in transact_log:
        print(transaction)
        sender, receiver = transaction[0]
        print("sender receiver", sender,receiver)
        amount = transaction[1]
        print("amount", amount)
        intermediary = transaction[2]
        print(intermediary)
        commission_rate = transaction[3]
        print(commission_rate)

        # Calcolo dell'importo della commissione di transazione
        commission = amount * commission_rate / 100

        print('player account sender',player_accounts[sender])

        # Controllo del saldo del mittente
        if player_accounts[sender] < amount + commission:
            # Se il saldo non è sufficiente, l'intermediario riceve solo la commissione
            print('commision',commission)
            player_accounts[sender] = player_accounts[sender]-commission
            print(player_accounts[sender])
            debts[intermediary][sender] += amount + commission - commission * 2
        else:
            # Altrimenti, la transazione viene effettuata e l'intermediario riceve la commissione e l'importo trasferito
            player_accounts[sender] -= amount + commission
            print(player_accounts[sender])
            player_accounts[receiver] += amount
            print(player_accounts[receiver])
            imd_accounts[intermediary] += commission
            print(imd_accounts[intermediary])
            # Controllo dei debiti residui
            if debts[intermediary][sender] < 0:
                # Se il mittente ha un debito residuo con l'intermediario, viene saldato in parte o totalmente
                debt = debts[intermediary][sender]
                if debt + amount + commission <= 0:
                    debts[intermediary][sender] = 0
                else:
                    debts[intermediary][sender] += amount + commission
            #else:
                # Altrimenti, l'intermediario mantiene un credito con il mittente
                #debts[intermediary][sender] -= commission

    # Creazione delle liste di output
    player_balances = [player_accounts[acn1], player_accounts[acn2], player_accounts[acn3]]
    intermediary_earnings = [imd_accounts[imd_acn1], imd_accounts[imd_acn2]]
    debts_list = [[debts[imd_acn1][acn1], debts[imd_acn1][acn2], debts[imd_acn1][acn3]],
                  [debts[imd_acn2][acn1], debts[imd_acn2][acn2], debts[imd_acn2][acn3]]]

    # Restituzione dei risultati come una tupla
    return (player_balances, intermediary_earnings, debts_list)


if __name__ == '__main__':
        
    res = ex1('0x5B23', '0xC78D' , '0x44AE' , '0x1612' , '0x90FF' , 1000 ,
        [ (('0x44AE', '0x5B23'),  800, '0x1612',  4),
            (('0x44AE', '0xC78D'),  800, '0x90FF', 10),
        ])
    
    print(res)
