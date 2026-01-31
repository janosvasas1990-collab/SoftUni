group = int(input())
days = int(input())
coins = 0
total = 0

for i in range (1, days + 1):
    if i % 10 == 0:
        group -= 2
        
    if i % 15 == 0:
        group += 5
    
    coins += 50
    coins -= 2 * group
    speech = False
    flag = False
    
    if i % 3 == 0:
        coins -= 3 * group
        speech = True
    
    if i % 5 == 0:
        coins += 20 * group
        flag = True
    
    if speech and flag:
        coins -= 2 * group
        
    
total = int(coins / group)       
print(f"{group} companions received {total} coins each.") 