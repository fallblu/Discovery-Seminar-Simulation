# Discovery Seminar Simulation

This is a small project born out of the Oxford College GroupMe. The goal of this project is to simulate the ranking and placement process for discovery seminars this fall. 

The function single_placement_sim takes the number of classes, the max class size, the number of students, and the number of allowed placements and returns a dictionary containing each possible rank as key and the number of students recieving each rank. The function simulate_dsc() takes all aformentioned arguments along with the number of iterations the user wants to simulate and returns a list of 2 dictonaries, the first of which contains the average number of students recieving each rank and the second containing these values as a percentage of the total student body.

The program now has the ability to consider an uneven distribution if class preferances. Tonight I will plug the results of the poll conducted on GroupMe into it and publish the results.