def over_write(List, Dictionary):
    L = List[:]
    d = Dictionary
    """
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    """
    for keys in d.keys():
        if keys == "PHONE":
            L[0][2] = str(int(L[0][2]) - int(d['PHONE']))
        elif keys == "LAPTOP":
            L[1][2] = str(int(L[1][2]) - int(d['LAPTOP']))
        else:
            L[2][2] = str(int(L[2][2]) - int(d['HDD']))
            
    print("\nRemaining Stock Products:\n", L)
        
    with open("products.txt", "w") as files:
        for each in L:
            files.write(",".join(each) + "\n")
    
    return L
