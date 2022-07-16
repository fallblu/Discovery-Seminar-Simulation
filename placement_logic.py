from random import randint

def single_placement_sim(seminars:int, max_class_size:int, students:int, preferences:int) -> dict:
    """This function simulates the discovery seminar scenario: a number of students ranking classes with a student limit."""
    """Output is a dictonary containing the number of students recieving each possible ranked preference."""

    student_rankings = {}
    for student in range(students):
        student_ranking = []
        while len(student_ranking) < preferences:
            rank = randint(1, seminars)
            if rank not in student_ranking:
                student_ranking.append(rank)
        student_rankings[student + 1] = student_ranking
    """Generates dictionary 'student_rankings' with student numbers and their preferences."""
    
    #print(student_rankings)

    requests_per_seminar = {}
    for seminar in range(seminars):     
        preference_list = []
        for preference in range(preferences):  
            preference_count = 0  
            for rankings in student_rankings.values():
                preference_count += 1 if rankings[preference] == seminar + 1 else 0
            preference_list.append(preference_count)
        requests_per_seminar[seminar + 1] = preference_list
    """Generates from 'student_rankings' dictionary 'Seminar_requests' with the total class ranking for each numbered seminar."""

    seminar_placements = {index + 1: 0 for index in range(seminars)}
    preferences_dict = {index + 1: 0 for index in range(preferences)}
    for student, rankings in student_rankings.items():
        for ranking in rankings:
            if seminar_placements[ranking] < max_class_size:
                seminar_placements[ranking] += 1
                preferences_dict[rankings.index(ranking) + 1] += 1
                break
    """Generates 'preferences_dict' containing desired info."""            

    #print(requests_per_seminar)

    return preferences_dict

def simulate_dsc(seminars:int, max_class_size:int, students:int, preferences:int, iterations:int) -> dict:
    """Runs single_placement_sim() iterations times and averages ranking totals"""

    average_placements = {index + 1: 0 for index in range(preferences)}
    for iteration in range(iterations):
        placements = single_placement_sim(seminars, max_class_size, students, preferences)
        for index in range(preferences):
            average_placements[index + 1] += placements[index + 1]
    for index in range(preferences):
        average_placements[index + 1] /= iterations

    percentage_placements = {ranking: total/students for ranking, total in average_placements.items()}

    return [average_placements, percentage_placements]


