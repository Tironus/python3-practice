import time
import threading
import concurrent.futures

class Character():
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.gender = 'male'
        self.gold = 100
        self.game_class = 'warrior'
        self.lock = threading.Lock()

    def update_gold(self, transaction, amount):
        print(f'{transaction} starting for {amount}\n')
        # you can also use lock.acquire() or lock.release() functions
        with self.lock:
            new_amt = self.gold
            new_amt += amount
            self.gold = new_amt
        print(f'{transaction} ending for {amount}\n')

if __name__ == '__main__':
    print('creating character\n')
    warrior = Character('Balrokk')
    print('updating gold for character\n')
    print(f'starting gold: {warrior.gold}\n')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        for transaction, amount in [('deposit', 50), ('withdrawal', -150)]:
            e.submit(warrior.update_gold, transaction, amount)
    print(f'ending gold: {warrior.gold}\n')