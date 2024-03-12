#!/usr/bin/python3
for alpha_lower_case in range(ord('a'), ord('z')+1):
    if alpha_lower_case == ord('e') or alpha_lower_case == ord('q'):
        continue
    print("{:c}".format(alpha_lower_case), end="")
