gryffinscore = 0
ravenscore = 0
hufflescore = 0
slytherscore = 0

def reset_score():
    global gryffinscore
    global ravenscore
    global hufflescore
    global slytherscore
    gryffinscore = 0
    ravenscore = 0
    hufflescore = 0
    slytherscore = 0

def add_points(question_response):
    global gryffinscore
    global ravenscore
    global hufflescore
    global slytherscore
    print(question_response["question"])
    if question_response["question"] == "G":
        gryffinscore += 1
    elif question_response["question"] == "HG":
        gryffinscore += 1
        hufflescore += 1
    elif question_response["question"] == "R":
        ravenscore += 1
    elif question_response["question"] == "H":
        hufflescore += 1
    elif question_response["question"] == "S":
        slytherscore += 1
    # print("The current gryffinscore is " + str(gryffinscore))
    print_score()
    return

def sort_user(question_response):
    house_result = ["nothing"]
    max_score = 0
    houses = {"Gryffindor":gryffinscore,"Hufflepuff":hufflescore,"Ravenclaw":ravenscore,"Slytherin":slytherscore}
    for house in houses:
        if houses[house] > max_score:
            house_result = []
            house_result.append(house)
            max_score = houses[house]
        elif houses[house] == max_score:
            house_result.append(house)
    if len(house_result) == 1:
        return house_result[0]
    elif len(house_result) > 1:
        if question_response["question"] == "G":
            return "Gryffindor"
        elif question_response["question"] == "R":
            return "Ravenclaw"
        elif question_response["question"] == "H":
            return "Hufflepuff"
        elif question_response["question"] == "S":
            return "Slytherin"
    else:
        return ("Muggle")

def pick_crest(house):
    if house == "Gryffindor":
        return "Gryffindor-crest.jpg"
    elif house == "Ravenclaw":
        return "Ravenclaw Crest.jpg"
    elif house == "Slytherin":
        return "Slytherin crest.jpg"
    else:
        return "Hufflepuff crest black.jpg"

def print_score():
    global gryffinscore
    global ravenscore
    global hufflescore
    global slytherscore
    print("G: " + str(gryffinscore))
    print("R: " + str(ravenscore))
    print("H: " + str(hufflescore))
    print("S: " + str(slytherscore))    