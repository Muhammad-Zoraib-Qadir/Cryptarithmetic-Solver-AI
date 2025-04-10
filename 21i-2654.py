import time
import itertools
from collections import deque

def time_function(function):
    def wrapper(*args, **kwargs):
        start_time = time.process_time()
        result = function(*args, **kwargs)
        elapsed_time = time.process_time() - start_time
        print(f"{function.__name__} took {elapsed_time:.5f}s")
        return result
    return wrapper

def validate_solution(words, letter_mapping):
    values = [sum(letter_mapping[letter] * (10 ** (len(word) - idx - 1)) for idx, letter in enumerate(word)) for word in words]
    if sum(values[:-1]) == values[-1]:
        return letter_mapping  
    return None

def validate_partial_solution(words, letter_mapping):
    assigned_digits = set()
    for letter, digit in letter_mapping.items():
        if digit == 0 and any(word.startswith(letter) for word in words):
            return False  # Leading digit constraint violated
        if digit in assigned_digits:
            return False  # Duplicate digit assignment
        assigned_digits.add(digit)
    return True

@time_function #Use to calculate the time complexity
def solve_using_dfs(words):
    unique_letters = set(''.join(words))
    available_digits = range(10)
    letter_frequency = {letter: sum(letter in word for word in words) for letter in unique_letters}
    for letter in sorted(unique_letters, key=lambda x: -letter_frequency[x]):
        available_digits = sorted(available_digits, key=lambda x: letter_frequency[x] if x in letter_frequency else 0, reverse=True)
        for perm in itertools.permutations(available_digits, len(unique_letters)):
            letter_mapping = dict(zip(unique_letters, perm))
            if any(letter_mapping[word[0]] == 0 for word in words):
                continue
            if validate_solution(words, letter_mapping):
                return letter_mapping


@time_function
def bfs_heuristic(words):
    unique_letters = set(''.join(words))
    available_digits = range(10)
    queue = deque()
    for perm in itertools.permutations(available_digits, len(unique_letters)):
        letter_mapping = dict(zip(unique_letters, perm))
        if any(letter_mapping[word[0]] == 0 for word in words):
            continue
        queue.append(letter_mapping)
    while queue:
        # Sort the remaining letters based on the number of available digits for each
        remaining_letters = set(unique_letters) - set(queue[0].keys())
        sorted_remaining_letters = sorted(remaining_letters, key=lambda x: len([d for d in available_digits if d not in queue[0].values()]), reverse=True)

        letter_mapping = queue.popleft()
        if not validate_partial_solution(words, letter_mapping):
            continue  # Prune this branch if it violates constraints
        result = validate_solution(words, letter_mapping)
        if result:
            return result

        if not remaining_letters:
            continue
        new_letter = sorted_remaining_letters[0]  # Select the most constrained variable
        for digit in available_digits:
            if digit not in letter_mapping.values():
                new_letter_mapping = letter_mapping.copy()
                new_letter_mapping[new_letter] = digit
                queue.append(new_letter_mapping)

# Take input words from the user
words = input("Enter words separated by spaces: ").split()

result_dfs = solve_using_dfs(words)
if result_dfs:
    print("DFS solution:")
    for word in words:
        value = sum(result_dfs[letter] * (10 ** (len(word) - idx - 1)) for idx, letter in enumerate(word))
        print(f"{word} = {value}")
print("Space complexity of the DFS algorithm is O(N), where N is the number of unique letters in the input words.")
result_bfs = bfs_heuristic(words)
if result_bfs:
    print("BFS HEURISTIC solution:")
    for word in words:
        value = sum(result_bfs[letter] * (10 ** (len(word) - idx - 1)) for idx, letter in enumerate(word))
        print(f"{word} = {value}")
print("Space complexity of the BFS algorithm is also O(N), where N is the number of unique letters in the input words.")

