class Player():
    def __init__(self, num,wallet_credit):
        self.wallet = wallet_credit
        self.num = num
        self.debt = {}
        
class Intermediate():
    def __init__(self, num):
        self.wallet = 0
        self.num = num        
   
def transact(acn1, acn2, val):
    if acn1.wallet < val:
        print('Transact not possible!\n')
        return 
    acn1.wallet = acn1.wallet - val
    acn2.wallet = acn2.wallet + val

def pay_fee(acn, imd_acn, val, fee): 
    new_val = float(val*fee/100)   
    if acn.wallet < new_val:
        imd_acn.wallet += acn.wallet
        remaining_fee = new_val - acn.wallet
        acn.wallet = 0 
        if acn.debt[imd_acn.num] in acn.debt:
            acn.debt[imd_acn.num] = remaining_fee
        else:
            acn.debt[imd_acn.num] += remaining_fee
    acn.wallet = acn.wallet - new_val
    imd_acn.wallet = imd_acn.wallet + new_val
    return (True, 0)
    
        
def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log):
    player1 = Player(acn1,init_amount)
    player2 = Player(acn2,init_amount)
    player3 = Player(acn3,init_amount)

    #print(player1.num)
    #print(player2.num)
    #print(player3.num)      
      
    intermediate1 = Intermediate(imd_acn1) 
    intermediate2 = Intermediate(imd_acn2)  

    player1.debt[intermediate1.num]
    player1.debt[intermediate2.num]

    print(player1.num)

    #print(intermediate1.num)
    #print(intermediate2.num)   
        
    for payment in transact_log:
        print(payment)
        if payment[0][0] == player1.num and payment[0][1]==player2.num:
            transact(player1, player2, payment[1])
            pay_fee(player1, intermediate1, payment[1], payment[3])
        elif payment[0][0] == player1.num and payment[0][1]==player3.num:
            transact(player1, player3, payment[1])
            pay_fee(player1, intermediate1, payment[1], payment[3])
        elif payment[0][0] == player2.num and payment[0][1]==player3.num:
            transact(player2, player3, payment[1])
            pay_fee(player2, intermediate1, payment[1], payment[3])
    return ([player1.wallet, player2.wallet, player3.wallet], [intermediate1.wallet, intermediate2.wallet], 
            [[player1.debt[intermediate1.num], player2.debt[intermediate1.num], player3.debt[intermediate1.num]], 
            [[player1.debt[intermediate2.num], player2.debt[intermediate2.num], player3.debt[intermediate2.num]]]])    
        
        
            
if __name__ == '__main__':
        
    res = ex1('0x5B23', '0xC78D' , '0x44AE' , '0x1612' , '0x90FF' , 1000 ,
        [ (('0x44AE', '0x5B23'),  800, '0x1612',  4),
          (('0x44AE', '0xC78D'),  800, '0x90FF', 10),
          (('0xC78D', '0x5B23'),  400, '0x1612',  8),
          (('0x44AE', '0xC78D'), 1800, '0x90FF', 12),
          (('0x5B23', '0x44AE'),  100, '0x1612',  2)
        ])
    
    print(res)