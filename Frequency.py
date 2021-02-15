test_str = input("Please enter a string: ")
def most_frequent(test_str):
    res = {} 
    for keys in test_str: 
      res[keys] = res.get(keys, 0) + 1
    # printing result  
    result = sorted(res.items() , key=lambda t : t[1], reverse = True)
    print(result)
most_frequent(test_str)
