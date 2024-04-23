def format_coefficient(coefficient):
    if coefficient == 0:
        return ''
    elif coefficient == 1:
        return '+'
    elif coefficient == -1:
        return '-'
    elif coefficient > 0:
        return '+' + str(coefficient)
    else:
        return str(coefficient)


def reformat(a, b, c) -> str:
    result = format_coefficient(a) + 'x' + format_coefficient(b) + 'y' + format_coefficient(c)
    # Remove leading '+' if present
    if result[0] == '+':
        result = result[1:]

    # Remove leading '1' if present
    if result[:2] == '+1':
        result = '+' + result[2:]
    return result


a, b, c = map(int, input().split())
result = reformat(a, b, c)
print(result)
