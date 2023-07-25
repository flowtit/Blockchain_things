import random
import time

def print_key_space(key_lengths):
    for key_length in key_lengths:
        key_space = 2**key_length
        print(f"Key length: {key_length} bits, Key space: {key_space}")

def generate_key_value(key_length):
        key_space = 2**key_length
        target_key = hex(random.randint(0, key_space - 1)) 
        print(f"Key length: {key_length} bits, Target key value: {target_key}")

def brute_force_key_search(key_length):
    key_space = 2**key_length
    target_key = hex(random.randint(0, key_space - 1))
    start_time = time.time()
    for i in range(key_space):
        if hex(i) == target_key:
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Key found: {target_key} after {elapsed_time:.2f} ms")
            break

def main():
    key_lengths = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    user_input = int(input("Enter 1 to get output the number of key options, enter 2 to generate a key value or enter 3 to brute force value: "))
    if user_input == 1:
        print_key_space(key_lengths)
    elif user_input == 2:
        key_length = int(input("Enter key length (in bits): "))
        generate_key_value(key_length)
    elif user_input == 3:
        key_length = int(input("Enter key length (in bits): "))
        brute_force_key_search(key_length)

if __name__ == "__main__":
    main()
