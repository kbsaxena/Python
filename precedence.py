a = 1
b = 2
c = 3

#precedence

print(a + b * c)   ## 1 + 2 * 3  => 1 + 6

print((a + b) * c)  ## 3 * 3

print(a + (b * c))  ## 1 + 6


#Associativity

print(a - b - c)  # left to right 1-2-3 => -1-3 => -4

print((a - b) - c) 

print(a - (b - c)) # right ot left as brackets are at last


print (-a + b)  ## => -1+2 => 1

print (-(a + b)) ## => -3


# increment and decrement

a += 10
print(a)  ## 11

b -= 50
print(b)  ## -48



