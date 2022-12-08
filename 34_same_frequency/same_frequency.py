def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    coll1 = {}
    coll2 = {}
    num1 = str(num1)
    num2 = str(num2)
    for x in num1:
        coll1[x] = coll1.get(x, 1) + 1
    for x in num2:
        coll2[x] = coll2.get(x, 1) + 1
    return coll1 == coll2
    
    
