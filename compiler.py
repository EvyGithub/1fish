# lol why did I make this
# also I think I'm gonna call this 1><> or 1Fish or onefish if you really don't want numbers in the first letter of a title or whatever

code = "155+/dd++"
stack = []
codeIndex = 0
cmd = ""
output = ""

while codeIndex < len(code):
    cmd = code[codeIndex]

    # pushing a number 0-9 to the stack
    if cmd in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        stack.insert(0, int(cmd)) # adds 0, 1, 2, 3, or whatever to stack

    # math operations; pops the top 2 values, and then does #1 [operation] #2. so if you do "52-" then it will push 5, then 2, [5, 2], and do the first minus the second
    elif cmd in ["+", "-", "*", "/", "|", "^", "%"]:
        temp2 = stack.pop(0)
        temp1 = stack.pop(0) # it moves the values by 1 index decrease, that's why

        if cmd == "+":   # addition
            temp3 = temp1 + temp2

        elif cmd == "-": # subtraction
            temp3 = temp1 - temp2

        elif cmd == "*": # multiplication
            temp3 = temp1 * temp2

        elif cmd == "/": # division
            temp3 = temp1 / temp2

        elif cmd == "|": # floor division, because the only other character I can think of is \ and that doesn't work for me
            temp3 = temp1 // temp2

        elif cmd == "%": # modulo
            temp3 = temp1 % temp2

        elif cmd == "^": # exponent
            temp3 = temp1 ** temp2

        stack.insert(0, temp3)
        
    # outputting, ASCII/unicode; outputting the number. (if you have 35 (you could use "67+5*"), and use "n" (67+5*n), it would output 65, not "A")
    elif cmd == "o":
        temp = stack.pop(0)
        output += chr(temp)
    elif cmd == "n":
        output += str(stack.pop(0))

    # comparing (> = <);
    elif cmd in [">", "<", "="]:
        temp1 = stack.pop(0)
        temp2 = stack.pop(0)

        if cmd == "=":
            if temp1 == temp2:
                temp3 = 1
            else:
                temp3 = 0
        
        elif cmd == "<":
            if temp1 < temp2:
                temp3 = 1
            else:
                temp3 = 0

        elif cmd == ">":
            if temp1 > temp2:
                temp3 = 1
            else:
                temp3 = 0

        stack.insert(0, temp3)
    
    # "l"; push the length of the stack onto the stack
    elif cmd == "l":
        stack.insert(0, len(stack))

    # duplicate; d = only top value, D = whole stack
    elif cmd in ["d", "D"]:
        newstack = []

        if cmd == "d":     # top value
            stack.insert(0, stack[0])

        elif cmd == "D":   # whole stack
            stack += stack

    # clear
    elif cmd == "c":
        stack = []


    # yes
    codeIndex += 1


print("\n" * 69 + "Stack (end of execution):")
print(stack)
print("\n\nOutput:\n")
print(output)