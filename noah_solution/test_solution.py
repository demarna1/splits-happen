# Test solution.py

import solution

# Test bowling_score using the test inputs file
with open('test_inputs.txt') as input_file:
    for line in input_file.readlines():
        # file format is '<game> <score>'
        values = line.strip().split(' ')
        game = values[0]
        expected = int(values[1])
        actual = solution.bowling_score(game)
        result = 'passed' if actual == expected else 'failed'
        print 'Test {} for {}, expected = {}, actual = {}'.format(result, game, expected, actual)

