import time

for h in range(1,60):
    
    print(f'{h} hour')
    for m in range(1,60):
        
        print(f'{m} minutes')
        for s in range(1,60):
            time.sleep(1)
            print(f'{s} seconds')