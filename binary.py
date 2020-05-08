#bitwise operations
# if val1 is True and val2 is false:

#ADD (& for binary)
#   01011010
#&  10101111
#-----------
#   00001010


#  OR ( | )
#   01011010
#   10101111
#-----------
#   11111111

#Exclusive 'OR'
# XOR
#




TABLES 

AND B

A B  A AND B
____________
0| 0|  0
0| 1|  0
1| 0|  0
1| 1|  1

A OR B

A| B| OR
____________
0| 0|  0
0| 1|  0
1| 0|  0
1| 1|  1

# Exclusive -or
A |B | XOR
_____________
0 |0 | 0
0 |1 | 1
1 |0 | 1
1 |1 | 0


# A| NOT A|(CAN ALSO BE A ~)
A |NOT A
_________
0| 1    |
1| 0    |
 


## SHIFTING
## A << some_number # shifts all bits in A by some amount to the left
## B >> some_number # shifts all bits in A by some amount to the right

#0b1110 >> 1 == 0b0111 #(this is the same as /2)
#0b1110 << 2 == 0b11100


## MASKING 
#       vv extract these bits 0b01 == 1

x = 0b01001100
#shit x by 3 to the right
y = x >> 3 # 0b00001001

#mask y with 0b0000011
#    0b00000011
#and 0b00001001
#--------------
#    0b00000001


# given 0b10100010
# give me the first two bits