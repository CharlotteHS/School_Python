#counting sheep

import time
amount = 10
#sheep amount variable

wait = 1
#wait time variable

for sheep in range(10,10010,10):
    # from 10 -> 10000 in intervals of 10

    print("Sheep", amount)
    amount = amount + 10
    #each loop the amount increases by 10

    time.sleep(wait)
    wait = wait + 1
    #increase the wait time by 1 each loop