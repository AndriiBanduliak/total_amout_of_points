def points(games):
    counter = 0
    for i in games:
        scores_str = i.split(':')
        first_score = int(scores_str[0])
        second_score = int(scores_str[1])
        if first_score > second_score:
            counter +=3
        elif first_score == second_score:
            counter +=1
    return(counter)
	pass