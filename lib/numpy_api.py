import numpy


def getRandomChoice(amount_of_sells_x: int, amount_of_sells_y: int):
    return numpy.random.choice([0, 1], size=(amount_of_sells_x, amount_of_sells_y), p=[0.8, 0.2])


def getCopy(input):
    return numpy.copy(input)


def getSum(a):
    return numpy.sum(a)


def getArray(input: any):
    return numpy.array(input)
