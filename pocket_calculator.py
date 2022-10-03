current_value = 0
operation_performed = ""
recent_value = 0
expression = str(current_value)

def get_value():
    return int(current_value)

def clear(clr_input = 0):
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
    global current_value
    # For reptition:
    global recent_value
    global operation_performed
    global expression

    recent_value = int(value_input)
    operation_performed = operation_input

    print("CV" + str(current_value))

    if operation_input == "+":
        current_value += int(recent_value)
    elif operation_input == "-":
        current_value -= int(recent_value)
    elif operation_input == "*":
        current_value *= int(recent_value)
    elif operation_input == "":
        current_value = int(current_value)
    else:
        current_value = int(current_value/recent_value)

    if operation_performed != "":
        expression = "(" + expression + ")" + operation_performed + str(recent_value)
    else:
        expression = str(recent_value)

    return int(current_value)

def repeat():
    global recent_value
    if operation_performed == "":
        recent_value = current_value
    step(operation_performed, recent_value)
    return int(current_value)

def get_expr():
    return expression
