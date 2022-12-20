import math

def softMax(input):
    n = float(sum(map(math.exp, input)))
    def soft(input):
        return math.exp(input) / n
    output = map(soft, input)
    return list(output)
def sigmoid(x):
    output = math.exp(x)/(math.exp(x)+1)
    return output
def ReLu(x):
    return max(0,x)
def tanh(x):
    output = 2/(1+math.exp(-2*x))-1
    return output