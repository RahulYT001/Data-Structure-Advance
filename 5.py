def occurrence(main_string, sub_string):
    count = 0
    start = 0
    while start < len(main_string):
        pos = main_string.find(sub_string, start)
        if pos != -1:
            count += 1
            start = pos + 1  
        else:
            break
    print(f"The substring '{sub_string}' occurs {count} times in the main string.")

main_string = input("Enter the main string: ")
sub_string = input("Enter the substring: ")

occurrence(main_string, sub_string)
