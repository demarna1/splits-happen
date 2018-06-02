import sys

# Return the base value of a single roll
def get_base_value(roll, previous):
    if roll == 'X':
        return 10
    elif roll == '/':
        # Note: can't have two '/'s in a row, so this recursion is OK
        return 10 - get_base_value(previous, '')
    elif roll == '-':
        return 0
    else:
        return int(roll)

# Get the multiplier bonus for a roll
def get_multiplier(previous, previousx2, frame):
    multiplier = 1
    if previous == 'X' or previous == '/':
        multiplier += 1
    if previousx2 == 'X':
        multiplier += 1
    # phase out the multiplier during the extra frames
    multiplier -= max(10, frame) - 10
    return multiplier

def bowling_score(game):
    frame = 1
    mid_frame = False
    previous = ''
    previousx2 = ''
    total_score = 0

    for roll in game:
        # update the score
        base_value = get_base_value(roll, previous)
        multiplier = get_multiplier(previous, previousx2, frame)
        total_score += base_value * multiplier

        # update the frame number
        if mid_frame or roll == 'X':
            mid_frame = False
            frame += 1
        else:
            mid_frame = True

        # set previous values
        previousx2 = previous
        previous = roll

    return total_score

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python solution.py <input>'
        sys.exit(1)
    game = sys.argv[1]
    print 'input = {}'.format(game)
    print 'score = {}'.format(bowling_score(game))

