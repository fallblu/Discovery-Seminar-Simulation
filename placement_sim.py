import placement_logic

poll_results = {
    1: .0128,
    2: .0128,
    3: .0128,
    4: .0128,
    5: .0128,
    6: .0128,
    7: .0128,
    8: .0128,
    9: .0128,
    10: .0128,
    11: .0128,
    12: .0128,
    13: .0385,
    14: .0513,
    15: .0513,
    16: .0513,
    17: .0513,
    18: .0513,
    19: .0513,
    20: .0513,
    21: .0513,
    22: .0513,
    23: .0641,
    24: .0641,
    25: .0897,
    26: .1282,
}

print(placement_logic.simulate_dsc(26, 16, 350, 5, 1_000, False, poll_results)[1])
print(placement_logic.simulate_dsc(26, 16, 360, 5, 1_000, False, poll_results)[1])
print(placement_logic.simulate_dsc(26, 16, 370, 5, 1_000, False, poll_results)[1])
print(placement_logic.simulate_dsc(26, 16, 380, 5, 1_000, False, poll_results)[1])
print(placement_logic.simulate_dsc(26, 16, 390, 5, 1_000, False, poll_results)[1])
print(placement_logic.simulate_dsc(26, 16, 400, 5, 1_000, False, poll_results)[1])