

def ham_doi_tien(amount, coins):
    results = [];
    coins.sort(reverse = True)
    for coin in coins:
        # dieu kien cho la gi?
        while(amount >= coin):
            results.append(coin)
            amount-=coin
    return results        

coins = [200, 100, 50, 20]
amount = 370
results = ham_doi_tien(amount, coins)
for coin in results:
    print(coin)