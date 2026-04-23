def multiply(a: list) -> int:
    result = 1
    for x in a: result *= x 
    return result 

if __name__ == "__main__":
    print("Result:", multiply([1,2,3,4,5]))