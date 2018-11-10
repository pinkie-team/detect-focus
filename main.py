import math


def calc_kouten():
    try:
        l = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
        theta1 = math.atan2(y2-y1, x2-x1)
        theta2 = math.acos((pow(l, 2) + pow(r1, 2) - pow(r2, 2)) / (2 * l * r1))
    except ValueError:
        return {'x1': 0.0, 'y1': 0.0, 'x2': 0.0, 'y2': 0.0}

    xi1 = x1 + r1 * math.cos(theta1 + theta2)
    yi1 = y1 + r1 * math.sin(theta1 + theta2)
    xi2 = x1 + r1 * math.cos(theta1 - theta2)
    yi2 = y1 + r1 * math.sin(theta1 - theta2)

    return {'x1': xi1, 'y1': yi1, 'x2': xi2, 'y2': yi2}


def is_collision():
    kouten = calc_kouten()
    dx1 = abs(kouten['x1'] - x3)
    dx2 = abs(kouten['x2'] - x3)

    dy1 = abs(kouten['y1'] - y3)
    dy2 = abs(kouten['y2'] - x3)

    if math.sqrt(pow(dx1, 2)+pow(dy1, 2)) <= r3:
        print('************************')
        print('交点1: {} {}'.format(dx1, dy1))
        print('************************')
        return True
    if math.sqrt(pow(dx2, 2)+pow(dy2, 2)) <= r3:
        print('************************')
        print('交点2: {} {}'.format(dx2, dy2))
        print('************************')
        return True

    return False


if __name__ == '__main__':
    DEBUG = True

    if DEBUG:
        window_width = 1440
        window_height = 900
        x1, x2, x3 = 100.0, window_width / 2.0, window_width - 100.0
        y1, y2, y3 = window_height - 100, 100.0, window_height - 100.0
    else:
        window_width = 1824
        window_height = 984
        x1, x2, x3 = 516.8, 1064.0, 1611.2
        y1, y2, y3 = 278.8, 574.0, 869.2

    r1, r2, r3 = 1.0, 1.0, 1.0

    while not is_collision():
        r1 += 1.0
        r2 += 1.0
        r3 += 1.0
