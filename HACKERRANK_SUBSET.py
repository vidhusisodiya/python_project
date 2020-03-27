def count_substring(string, sub_string):
    len1 = len(string)
    len2 = len(sub_string)
    j = 0
    counter = 0
    while (j < len1):
        if (string[j] == sub_string[0]):
            if (string[j:j + len2] == sub_string):
                counter += 1
        j += 1

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)