import sys

#op codes
#operation codes
PRINT_MARCUS   = 1
HALT           = 2
PRINT_NUM      = 3
SAVE           = 4
PRINT_REGISTER = 5
ADD            = 6


print_marcus_program = [
    PRINT_MARCUS,
    PRINT_MARCUS,
    PRINT_MARCUS,
    PRINT_MARCUS,
    HALT,
]

print_some_numbers = [
    PRINT_NUM,
    15,
    PRINT_NUM,
    15,
    PRINT_NUM,
    37,
    PRINT_MARCUS,
    HALT
]

#sample program that adds to 
# register values together
save_num_to_reg =[
    SAVE, #SAVE, VAL, REG_NUM
    65,
    2,
    PRINT_REGISTER,
    2,
    SAVE, # SAVE, VAL, REG_NUM
    14568292,
    6,
    PRINT_REGISTER,
    2,
    PRINT_REGISTER,
    6,
    HALT
]
# sample program that adds to register
#values together
add_two_nums = [
    SAVE,# SAVE number 23 to reg 1
    12,
    1,
    SAVE, #save number as to reg 2
    45,
    2,
    ADD, # reg1 += reg2 add then store value 
    #to the 1st register given
    1,
    2,
    PRINT_REGISTER,
    1,
    SAVE,
    10,
    2,
    ADD,
    1,
    2,
    PRINT_REGISTER,
    1,
    HALT
]

#this is where we "load" a program
memory = print_some_numbers


#lets write a basic computer

#ALL THE CODE BELOW IS THE 'COMPUTER'
running = True
#(PROGRAM COUNT)- EVERY ACTION
pc = 0
registers = [0] * 8


# read from file, and load into memory
# read the filename from comand line arguments
# open the file, and load each line into memory
# lets try not to crash

def load_program_into_memory():
    #rest the memory
    # memory = []
    address = 0
    #get the filename from arguments here
    #get the filename
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Need proper file name passed")
        sys.exit(1)
    
    filename - sys.argv()
    with open(filename) as f:
        for line in f: 
            print(line)
            if line == "":
                continue
            comment_split = line.split("#")
            print(comment_split) # [everything before #, everything after #]
            num = comment_split
            memory[address] = num
            address += 1
    # Now we have loaded a program in to memory



load_program_into_memory()
running =False

# ir= instruction register- create a variable called IR
while running:
    # lets do some things while on!!!
    # receives instructions and executes them
    command = memory[pc]
    # if command is print marcus
    if command == 'PRINT_MARCUS':
    #computer can't read strings
    #so 'PRINT_MARCUS' would be binary number
        print('Marcus!')
        #print name
        pc += 1
    
    #if command is halt
    elif command == HALT:
        running = False
        pc += 1
        #shutdown

    elif command == PRINT_NUM:
        # look at the next line in memory
        # print the number in that spot
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == SAVE:
        # we expect to see two number after 
        #after the instruction
        #number to save, and register location
        num_to_save = memory[pc + 1]
        register = memory[pc + 2]
        registers[register] = num_to_save
        pc += 3
    
    elif command == PRINT_REGISTER:
        #we expect to see one number after instruction
        #number of register location
        register = memory[pc + 1]
        print(registers[register])
        pc += 2

    elif command == ADD:
        #we expect to see two numbers after
        #the instruction
            #both register locations
            #we will save the result into the 
            #first register given to us
        register1 = memory[pc + 1]
        register2 = memory[pc + 2]
        val1 = registers[register1]
        val2 = registers[register2]
        regiseter[register1] = val1 + val2
        pc += 3
    
    else:
    #if command is not recognizable
        print(f'Unknown instruction {command}')
        sys.exit(1)
        #crash
    pass