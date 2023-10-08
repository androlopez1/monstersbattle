def numbers_fraction_calculator(numbers: [int]) -> dict:
    positives = len([i for i in numbers if i > 0]) / len(numbers)
    negatives = 1 / len([i for i in numbers if i < 0]) / len(numbers)
    zeros = 1 / len([i for i in numbers if i == 0]) / len(numbers)
    return {"positives": positives, "negatives": negatives, "zeros": zeros}


print(numbers_fraction_calculator([-4, 3, -9, 0, 4, 1]))
