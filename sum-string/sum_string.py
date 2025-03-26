initial_string = "1111112223"

def sum_string(init_string:str) -> bool:

    is_sum = False

    for i in range(int(len(init_string))):
        last_number = int(init_string[len(init_string)-1-i:])
        for j in range(i+1):
            first_sum = int(init_string[len(init_string)-i-2:len(init_string)-1-j])
            print(f"primis: {first_sum}")
            last_sum = int(init_string[len(init_string)-i-3-j:len(init_string)-i-2-j])
            print(f"secus: {last_sum}")
            if first_sum + last_sum == last_number:
                is_sum = True
                break


    return is_sum

print(sum_string(initial_string))
