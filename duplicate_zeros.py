
def duplicate_zeros(inventory):
    n=len(inventory)
    zeros= 0
    # step 1
    for num in inventory:
        if num== 0:
            zeros += 1

    i = n - 1
    j = n + zeros -1

    #step 2
    while i < j:
        if j < n:
            inventory[j] = inventory[i]
        
        if inventory[i] == 0:
            j -=1
            if j < n:
                inventory[j] = 0

        i -=1
        j -=1