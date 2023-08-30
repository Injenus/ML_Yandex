cur_temp, target_temp = map(int, input().split())
mode = input()
final_temp = cur_temp
if mode == 'freeze':
    final_temp = target_temp if target_temp < cur_temp else cur_temp
elif mode == 'heat':
    final_temp = target_temp if target_temp > cur_temp else cur_temp
elif mode == 'auto':
    final_temp = target_temp
elif mode == 'fan':
    pass
print(final_temp)
