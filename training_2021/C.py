chars_to_remove = "-() "
trans_table = str.maketrans('', '', chars_to_remove)
new_n = input().translate(trans_table)
if len(new_n) == 7:
    new_n = '8495' + new_n


def check_number(new_num):
    isYes = False
    number = input().translate(trans_table)
    if len(number) == 7:
        number = '8495' + number
    # одинаковая длина возможна только при одинаковом типе номеров
    if len(number) == len(new_num):
        if number == new_num:
            isYes = True
    # значит у номеров точно разный тип
    elif number[0] == '+':
        if number[2:] == new_num[1:]:
            isYes = True
    elif new_num[0] == '+':
        if new_num[2:] == number[1:]:
            isYes = True
    return isYes


for i in range(3):
    if check_number(new_n):
        print('YES')
    else:
        print("NO")
