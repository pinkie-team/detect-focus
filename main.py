import math


def calc_kouten():
    results = {
        'x12a': 0.0, 'y12a': 0.0, 'x12b': 0.0, 'y12b': 0.0,
        'x13a': 0.0, 'y13a': 0.0, 'x13b': 0.0, 'y13b': 0.0,
        'x23a': 0.0, 'y23a': 0.0, 'x23b': 0.0, 'y23b': 0.0
    }

    try:
        l12 = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        theta12a = math.atan2(y2 - y1, x2 - x1)
        theta12b = math.acos((pow(l12, 2) + pow(r1, 2) - pow(r2, 2)) / (2 * l12 * r1))

        # 円1,2の交点
        x12a = x1 + r1 * math.cos(theta12a + theta12b)
        y12a = y1 + r1 * math.sin(theta12a + theta12b)
        x12b = x1 + r1 * math.cos(theta12a - theta12b)
        y12b = y1 + r1 * math.sin(theta12a - theta12b)

        results['x12a'] = x12a
        results['y12a'] = y12a
        results['x12b'] = x12b
        results['y12b'] = y12b
    except ValueError:
        pass

    try:
        l23 = math.sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))
        theta23a = math.atan2(y3 - y2, x3 - x2)
        theta23b = math.acos((pow(l23, 2) + pow(r2, 2) - pow(r3, 2)) / (2 * l23 * r2))

        # 円2,3の交点
        x23a = x2 + r2 * math.cos(theta23a + theta23b)
        y23a = y2 + r2 * math.sin(theta23a + theta23b)
        x23b = x2 + r2 * math.cos(theta23a - theta23b)
        y23b = y2 + r2 * math.sin(theta23a - theta23b)

        results['x23a'] = x23a
        results['y23a'] = y23a
        results['x23b'] = x23b
        results['y23b'] = y23b
    except ValueError:
        pass

    try:
        l13 = math.sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))
        theta13a = math.atan2(y3 - y1, x3 - x1)
        theta13b = math.acos((pow(l13, 2) + pow(r1, 2) - pow(r3, 2)) / (2 * l13 * r1))

        # 円1,3の交点
        x13a = x1 + r1 * math.cos(theta13a + theta13b)
        y13a = y1 + r1 * math.sin(theta13a + theta13b)
        x13b = x1 + r1 * math.cos(theta13a - theta13b)
        y13b = y1 + r1 * math.sin(theta13a - theta13b)

        results['x13a'] = x13a
        results['y13a'] = y13a
        results['x13b'] = x13b
        results['y13b'] = y13b
    except ValueError:
        pass

    # print(results)
    # print('***************************')

    return results


def is_collision():
    kouten = calc_kouten()

    dx12a = abs(kouten['x12a'] - x3)
    dy12a = abs(kouten['y12a'] - y3)
    dx12b = abs(kouten['x12b'] - x3)
    dy12b = abs(kouten['y12b'] - y3)

    dx13a = abs(kouten['x13a'] - x2)
    dy13a = abs(kouten['y13a'] - y2)
    dx13b = abs(kouten['x13b'] - x2)
    dy13b = abs(kouten['y13b'] - y2)

    dx23a = abs(kouten['x23a'] - x1)
    dy23a = abs(kouten['y23a'] - y1)
    dx23b = abs(kouten['x23b'] - x1)
    dy23b = abs(kouten['y23b'] - y1)

    # 円1,2の交点aが円3の半径内にあるかどうか
    if math.sqrt(pow(dx12a, 2) + pow(dy12a, 2)) <= r3 and kouten['x12a'] != 0 and kouten['y12a'] != 0:
        print('************************')
        print('1,2 A: {} {}'.format(kouten['x12a'], kouten['y12a']))
        print('************************')
        return True

    # 円1,2の交点bが円3の半径内にあるかどうか
    if math.sqrt(pow(dx12b, 2) + pow(dy12b, 2)) <= r3 and kouten['x12b'] != 0 and kouten['y12b'] != 0:
        print('************************')
        print('1,2 B: {} {}'.format(kouten['x12b'], kouten['y12b']))
        print('************************')
        return True

    # 円1,3の交点aが円2の半径内にあるかどうか
    if math.sqrt(pow(dx13a, 2) + pow(dy13a, 2)) <= r2 and kouten['x13a'] != 0 and kouten['y13a'] != 0:
        print('************************')
        print('1,3 A: {} {}'.format(kouten['x13a'], kouten['y13a']))
        print('************************')
        return True

    # 円1,3の交点bが円2の半径内にあるかどうか
    if math.sqrt(pow(dx13b, 2) + pow(dy13b, 2)) <= r2 and kouten['x13b'] != 0 and kouten['y13b'] != 0:
        print('************************')
        print('1,3 B: {} {}'.format(kouten['x13b'], kouten['y13b']))
        print('************************')
        return True

    # 円2,3の交点aが円1の半径内にあるかどうか
    if math.sqrt(pow(dx23a, 2) + pow(dy23a, 2)) <= r1 and kouten['x23a'] != 0 and kouten['y23a'] != 0:
        print('************************')
        print('2,3 A: {} {}'.format(kouten['x23a'], kouten['y23a']))
        print('************************')
        return True

    # 円2,3の交点bが円1の半径内にあるかどうか
    if math.sqrt(pow(dx23b, 2) + pow(dy23b, 2)) <= r1 and kouten['x23b'] != 0 and kouten['y23b'] != 0:
        print('************************')
        print('2,3 B: {} {}'.format(kouten['x23b'], kouten['y23b']))
        print('************************')
        return True

    return False


def get_remove_interger_zero_count(decimal_values):
    """
    与えられた数値の整数部に0があるパターンを除去するには何倍すれば良いかを求める
    :param decimal_values:  センサー値
    :type:   list
    :return:    何倍すれば全ての数値から0.111といった整数部が0のパターンを除去できるか
    :rtype: int
    """
    count = 0

    for decimal_value in decimal_values:
        tmp_count = 0
        integer = math.modf(decimal_value)[1]

        while integer == 0:
            decimal_value *= 10
            integer = math.modf(decimal_value)[1]
            tmp_count += 1

        if count < tmp_count:
            count = tmp_count

    return count


if __name__ == '__main__':
    DEBUG = True
    SOUND = True

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

    # 取得したセンサー値（振動なら0.01とか、音なら0.5や11.5とか）
    if SOUND:
        # TODO abs付けて絶対値にしよう！！　半径を増やす際にマイナスになって円が表示されなくなるぞ。
        decimal_value1, decimal_value2, decimal_value3 = abs(2.285823), abs(0.858796), abs(0.0257178)  # 音（センサーから来た生データにはマイナスが付与されているので）
        max_count = get_remove_interger_zero_count([decimal_value1, decimal_value2, decimal_value3])
        value1, value2, value3 = decimal_value1*pow(10, max_count), decimal_value2*pow(10, max_count), decimal_value3*pow(10, max_count)
        min_value = min(value1, value2, value3)

        r1_plus = value1 / min_value
        r2_plus = value2 / min_value
        r3_plus = value3 / min_value
    else:
        decimal_value1, decimal_value2, decimal_value3 = 0.05110727995634079, 0.02403908036649227, 0.012767072767019272  # 振動
        r1_plus = 0.1 / decimal_value1
        r2_plus = 0.1 / decimal_value2
        r3_plus = 0.1 / decimal_value3

    loop_count = 0
    while not is_collision():
        loop_count += 1

        if loop_count >= 300000:
            print('**********************')
            print('many loop')
            print('**********************')
            # TODO 無限ループに入りそうになったら、適当な座標を指定して表示しておく（ランダムにしてどっか表示とか）
            break
        r1 += r1_plus
        r2 += r2_plus
        r3 += r3_plus

    print(loop_count)
