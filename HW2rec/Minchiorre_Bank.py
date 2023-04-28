class Player():
    def __init__(self, num):
        self.wallet = 1000
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
    for payment in transact_log:
        transact(payment[0][0], payment[0][1], payment[1])
        pay_fee(payment[0][0], payment[2], payment[1], payment[3])
    return ([acn1.wallet, acn2.wallet, acn3.wallet], [imd_acn1.wallet, imd_acn2.wallet], 
            [[acn1.debt[imd_acn1.num], acn2.debt[imd_acn1.num], acn3.debt[imd_acn1.num]], 
            [[acn1.debt[imd_acn2.num], acn2.debt[imd_acn2.num], acn3.debt[imd_acn2.num]]]])    
        
        
            
if __name__ == '__main__':
        
    player1 = Player('0x5B23')
    player2 = Player('0xC78D')
    player3 = Player('0x44AE')
      
    intermediate1 = Intermediate('0x1612') 
    intermediate2 = Intermediate('0x90FF')     
    
    res = ex1(player1.num, player2.num, player3.num, intermediate1.num, intermediate2.num, 1000,
        [ ((0x44AE, 0x5B23),  800, 0x1612,  4),
          ((0x44AE, 0xC78D),  800, 0x90FF, 10),
          ((0xC78D, 0x5B23),  400, 0x1612,  8),
          ((0x44AE, 0xC78D), 1800, 0x90FF, 12),
          ((0x5B23, 0x44AE),  100, 0x1612,  2)
        ])
    
    print(res)