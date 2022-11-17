#Omid Akbari
#bqh5sd

def find_max(dict):

    ref = -1
    max_locality = ""

    for local, value in dict.items():
        if value > ref:
            ref = value
            max_locality = local
    return max_locality


def maxServed(fptr, year, served=1):
    data = fptr.read().strip().split('\n')

    dict = {}

    for current_data in data[1:]:
        current_data = current_data.split(",")
        for i in range(8):
            if current_data[i] == "":
                current_data[i] = "0"
        if served == 0:
            if int(current_data[0]) == year:
                if current_data[2] in dict:
                    dict[current_data[2]] = dict[current_data[2]] + int(current_data[3])
                else:
                    dict[current_data[2]] = int(current_data[3])

        if served == 1:
            if int(current_data[0]) == year:
                if current_data[2] in dict:
                    dict[current_data[2]] = dict[current_data[2]] + int(current_data[4])
                else:
                    dict[current_data[2]] = int(current_data[4])
        if served == 2:
            if int(current_data[0]) == year:
                if current_data[2] in dict:
                    dict[current_data[2]] = dict[current_data[2]] + int(current_data[6])
                else:
                    dict[current_data[2]] = int(current_data[6])

    return find_max(dict)
