# The shunting yard algorithm is used to convert an infix expression into postfix

def shuntingYard(infixExpression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # Set the precedence of each operator

    operatorStack = []  # Stores the operators and parentheses
    output = []  # Stores the postfix to be returned

    tokenized = getTokenizedInfix(infixExpression)

    for token in tokenized:
        try:
            float(token) # Check if the token is a number by seeing if it can be converted to a float
        except ValueError: # It is not a number (either integer or float)
            if token in precedence: # If the token is an operator...
                while (
                    len(operatorStack) != 0 and # Check if there is no more operators to process
                    operatorStack[-1] != "(" and # Ensure the loop continues until the opening parenthesis is found
                    precedence[token] <= precedence.get(operatorStack[-1], 0) # 0 is used as the default precedence if the operator is not found in the dict
                ):
                    # While there are operators on the stack and the top operator has a higher precedence, pop it and append it to the output
                    output.append(operatorStack.pop())
                operatorStack.append(token) # Push the current operator onto the stack as it has a higher precedence
            elif token == "(":
                # If the token is an opening parenthesis, push it to the stack (used as a marker)
                operatorStack.append(token)
            elif token == ")":
                # If the token is a closing parenthesis...
                while len(operatorStack) != 0 and operatorStack[-1] != "(":
                    # Pop operators from the stack and append to the output until the opening parenthesis is found
                    output.append(operatorStack.pop())
                if len(operatorStack) != 0 and operatorStack[-1] == "(":
                    # If the opening parenthesis is found, discard it
                    operatorStack.pop()
        else:
            output.append(token) # If the token can be turned into a float, then it is a valid number that should be appended
        
    while len(operatorStack) != 0: # Pop the remaining operators from the stack and append to the output
        output.append(operatorStack.pop())
    
    return "|".join(output) # Join the output list together into a string
        
        
def getTokenizedInfix(infixExpression):
    # Creates a list of each token (complete number and operators such as ['28', '+', '2'])
    tokenized = []
    currentNumber = "" # Store each complete number as a string
    
    for char in str(infixExpression):
        try:
            int(char)
        except ValueError:
            if char == ".":
                # currentNumber must be a float, so add the decimal
                currentNumber += "."
            else:
                # char is an operator, end of the currentNumber and the operator is added as a separate token
                if currentNumber != "":
                    tokenized.append(currentNumber)
                    currentNumber = ""
                if char != " ":
                    tokenized.append(char)
        else:
            # Char is a digit, the number continues so add the current digit to currentNumber
            currentNumber += char
    
    if len(currentNumber) != 0: # End of the expression reached. If currentNumber has anything stored, it must be a complete number so append it
        tokenized.append(currentNumber)
    
    return tokenized