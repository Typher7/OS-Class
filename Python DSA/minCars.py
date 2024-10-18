#test case 1: Persons = [1,4,1], Seats = [1,5,1], returns 2

def solution(persons, seats):
    seats.sort(reverse=True)
    total_persons = sum(persons)
    
    for i in range(len(seats)):
        total_persons -= seats[i]
        if total_persons <= 0:
            return i + 1
    return 0
print("Min cars: ", solution([2,3,4,2], [2,5,7,2]))

