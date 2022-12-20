import random
from mathfunctions import*
class Neuron:
    def __init__(self, input):
        self.weights = []
        self.input = input
    def initweights(self):
        for i in range(len(self.input)):
            self.weights.append(random.random())
    def caloutput(self):
        sum = 0
        for i in range(len(self.input)):
            sum += self.input[i] * self.weights[i]
        output = sigmoid(sum)
        return output

class Layer:
    def __init__(self, neu):
        self.num_of_neurons = neu
        self.neurons = []
    def initlayer(self, pre_neu):
        self.pre_neu = pre_neu
        for i in range(self.num_of_neurons):
            self.neurons.append(Neuron(self.pre_neu))
            self.neurons[i].initweights()
    def caloutputs(self):
        output = []
        for i in range(self.num_of_neurons):
            output.append(self.neurons[i].caloutput())
        return output
    def finallayeroutput(self):
        input = self.caloutputs()
        output = softMax(input)
        return output

class Network:
    def __init__(self, neurons_in_layers, inputdata):
        self.neurons_in_layers = neurons_in_layers
        self.num_of_layers = len(self.neurons_in_layers)
        self.inputdata = inputdata
        self.layers = []
    def initlayers(self):
        for i in range(self.num_of_layers):
            self.layers.append(Layer(self.neurons_in_layers[i]))
        self.layers[0].initlayer(self.inputdata)
        for i in range(self.num_of_layers-1):
            self.layers[i+1].initlayer(self.layers[i].caloutputs())
    def runlayers(self, input):
        for i in range(self.num_of_layers):
            self.layers[i].runlayer(input)
    def finaloutput(self):
        output = self.layers[self.num_of_layers-1].finallayeroutput()
        return output

network = Network([4,7,2],[4,6,8,10])
network.initlayers()
print(network.finaloutput())