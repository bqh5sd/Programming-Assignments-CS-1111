#Omid Akbari
#bqh5sd

#Global Variable set up
current_value = 0
operation_performed = ""
recent_value = 0
expression = str(current_value)

def get_value():
    '''
    The purpose of this function is to return the current value
    :return: Returns the current value which has been calculated
    '''
    return int(current_value)

def clear(clr_input = 0):
    '''
    The purpose of this function is to rest the calculator to it's intial value and objects. When no parameter input is added to the function
    the function defults the input to 0
    :param clr_input: This is an optional parameter which is added after the calculator is reset. The clr_input value is substituted for the 
    current value
    :return: This function returns the current value
    '''
    #set all global variables to inital conditions
    global current_value
    global recent_value
    global expression
    global operation_performed
    current_value = clr_input
    recent_value = 0
    expression = str(current_value)
    operation_performed = ""
    return int(current_value)

def step(operation_input, value_input):
    '''
    The purpose of this function is to perform numerical and string operations to calculate simple mathematical operations 
    :param operation_input: This input provides the mathematical operation which will be utilized to calculate 
    :param value_input: This input provides the numerical value which will be performed given the operation_input
    :return: This function will return the updated current value after operation is completed
    '''
    global current_value
    # For reptition:
    global recent_value
    global operation_performed
    global expression

    #updating recent value and operation performed after inputs
    recent_value = int(value_input)
    operation_performed = operation_input

    #Perform calculations with given parameters to update the current value
    if operation_input == "+":
        current_value += recent_value
    elif operation_input == "-":
        current_value -= recent_value
    elif operation_input == "*":
        current_value *= recent_value
    elif operation_input == "":
        current_value = current_value
    else:
        current_value = int(current_value/recent_value)

    #Update the current 
    if operation_performed != "":
        expression = "(" + expression + ")" + operation_performed + str(recent_value)
    else:
        expression = str(recent_value)

    return int(current_value)

def repeat():
    '''
    The purpose of this function is to repeat the previous step operation. When no operation has been performed prior, this function will 
    simply return the recent current value
    :return: This function will return the current value after repeating a step
    '''
    global recent_value
    #In the case that clear functio is used, operation performed is an empty string, therefore, the recent value will simply be the current value
    if operation_performed == "":
        recent_value = current_value
    step(operation_performed, recent_value)
    return int(current_value)

def get_expr():
    '''
    The purpose of this function is to return the current and previous expression after an operation('s) is/are performed 
    :return: Returns the current expression including the previous expression embedded 
    '''
    return expression
