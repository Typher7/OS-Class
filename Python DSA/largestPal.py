#Test case: "39878" returns 898
from collections import Counter

def solution(string):
    freq = Counter(string)
    mid = ""
    half = []

    for digit in sorted(freq.keys(), reverse=True):
        count = freq[digit]

        half.append(digit * (count // 2)) #add largest even part of the digit to half of pal

        if count % 2 == 1 and mid == "":
            mid = digit
        
    first_half = ''.join(half)
    second_half = first_half[::-1] #reverse first half

    largest_pal = first_half + mid + second_half

    return largest_pal.lstrip('0') or '0'


print(solution("398798"))
