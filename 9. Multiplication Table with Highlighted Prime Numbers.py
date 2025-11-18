n = int(input("Enter the number of multiplication tables you want: "))
for i in range(1, n + 1):
    print(f"The multiplication table for {i} is:")
    for j in range(1, 13):
        product = i * j
        if product > 1:
            is_prime = True
            for x in range(2, int(product**0.5) + 1):
                if product % x == 0:
                    is_prime = False
                    break
        else:
            is_prime = False
        display_product = str(product) + "*" if is_prime else str(product)   
        print(f"{i}x{j}={display_product}")
    print()
