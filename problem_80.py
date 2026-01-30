# Problem 80: Find mode (most frequent element)
# Find and fix the error

def find_mode(lst):
    if not lst:
        return [] 
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1

    max_freq = max(freq.values())
   
    modes = [key for key, value in freq.items() if value == max_freq]
    return modes

numbers = [1, 2, 2, 3, 3, 3, 4]
print(f"Mode: {find_mode(numbers)}")  

numbers2 = [1, 1, 2, 2, 3]
print(f"Mode: {find_mode(numbers2)}")
