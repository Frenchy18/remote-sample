import math

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    variance = sum((x-mean)**2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {f"total: {total}, mean: {mean}, std_dev: {std_dev}"}
