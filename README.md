# Discovery Seminar Simulation

This is a small project born out of the Oxford College GroupMe. The goal of this project is to simulate the ranking and placement process for discovery seminars this fall. 

The function single_placement_sim takes the number of classes, the max class size, the number of students, and the number of allowed placements and returns a dictionary containing each possible rank as key and the number of students recieving each rank. The function simulate_dsc() takes all aformentioned arguments along with the number of iterations the user wants to simulate and returns a list of 2 dictonaries, the first of which contains the average number of students recieving each rank and the second containing these values as a percentage of the total student body.

The program now has the ability to consider an uneven distribution if class preferances. 

The results of the poll presented a challenge in that many of the classes recieved 0 votes, making it difficult to model these classes accurately given there is basically no info on their popularity. What I did to attempt to accurately repersent the preferences anyways was to add .5 to each class with 0 picks and to remove picks from the two high outliers and the two classes with 3 picks to keep the number of total rankings 39.

## Results

These are the results after running a few 10,000 iteration simulations with varying student body sizes and the rounded off survey results

350 - 1: 0.6812, 2: 0.1156, 3: 0.05638, 4: 0.03444, 5: 0.02436

360 - 1: 0.6674, 2: 0.1156, 3: 0.05776, 4: 0.03637, 5: 0.02579

370 - 1: 0.6537, 2: 0.1167, 3: 0.05901, 4: 0.03748, 5: 0.02686

380 - 1: 0.6408, 2: 0.1167, 3: 0.06031, 4: 0.03922, 5: 0.02800

390 - 1: 0.6271, 2: 0.1170, 3: 0.06181, 4: 0.04054, 5: 0.02988

400 - 1: 0.6175, 2: 0.1162, 3: 0.06198, 4: 0.04170, 5: 0.03058

## Why these results aren't perfect (and are actually probably pretty bad!)

**1. The rounding of the poll results is really, really bad...**

It's really hard to make an accurate model based on popularity when almost half of your classes (12/26) give you nothing beyond the fact that they're selected less than about 2.5% of the time. In consequence, any guesses made as to the popularity of these classes is going to suck.

In retrospect, this all could have been fixed if I had just added options to enter in 2nd, 3rd, 4th, and 5th classes. Oh well.

**2. This is not the most efficient way to handle rankings!**

An example of a situation in which this method of filling classes until they're full rather than actually placing efficiently falls short is as follows:

Person A's rankings are 1: Seminar 3, 2: Seminar 1, 3: Seminar 2
Person B's rankings are 1: Seminar 3, 2: Seminar 2, 3: Seminar 4

person A is placed in their first choice before person B and the class fills as a result. Seminar 2 also happens to be full so person B is placed into Seminar 4, their 3rd rank class. All of this happens while Seminar 1, person A's second choice is still open. An efficient placement algorithm would forgo placing person A in their first choice, instead placing them in Seminar 2, a 1 rank reduction so that person B could have a 2 rank improvement from Seminar 4 to Seminar 3.

I will probably eventually revise this to add a more efficent placement alg but at the moment I'm satisfied with what I have.