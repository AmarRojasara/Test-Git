a = [1,2,3,4,5,1,2,3]

def count(numbers):
    frequency={}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    
    return frequency

A = count(a)
print(A)   

B = set(a)
print(B)

# Adding new Content for second commit.