import itertools
import time


def main():
    loops = input("How many loops? ")
    start = time.time()
    max_loop = int(loops)
    total_combinations = 0
    number_divisible = 0
    for i in range(1, max_loop+1):
        for combo in itertools.combinations(range(1, max_loop+1), i):
            print(combo)
            total_combinations += 1
            sum = 0
            for item in combo:
                sum = sum + item
            if sum % 5 == 0:
                number_divisible += 1
    end = time.time()
    print("Total combinations =",total_combinations)
    print("Total Divisible by 5 =", number_divisible)
    print("Time to complete:", end - start, "seconds")
    
    
    
if __name__ == "__main__":
    main()