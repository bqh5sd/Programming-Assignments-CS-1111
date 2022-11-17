#Omid Akbari
#bqh5sd


def maxServed(fptr, year=1, served=1):
    data = fptr.read().strip().split('\n')

    ref = -1
    max_locality = ""

    for current_data in data[1:]:
        current_data = current_data.split(",")
        for i in range(8):
            if current_data[i] == "":
                current_data[i] = "0"
        if served == 0:
            if int(current_data[3]) > ref:
                ref = int(current_data[3])
                max_locality = current_data[2]
        if served == 1:
            if int(current_data[4]) > ref:
                ref = int(current_data[4])
                max_locality = current_data[2]
        if served == 2:
            if int(current_data[6]) > ref:
                ref = int(current_data[6])
                max_locality = current_data[2]


    return max_locality


