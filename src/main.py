import random


def sum_func(num_a, num_b):
    return num_a + num_b


def mult_func(num_a, num_b):
    return num_a * num_b


def main():
    """main"""
    num_a = random.randint(1, 10)
    num_b = random.randint(1, 10)
    num_sum = sum_func(num_a, num_b)
    num_mul = mult_func(num_a, num_b)
    print(f"num_sum: {num_sum}")
    print(f"num_mul: {num_mul}")


if __name__ == "__main__":
    main()
