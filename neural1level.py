#!usr/bin/python

#FEEDFORWARD NEURAL NETWORK ---- INPUT LAYER, HIDDEN LAYERS AND OUTPUT LAYER
from numpy import exp, array, random, dot



class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) -1


class NeuralNetwork():
    def __init__(self, layer1, layer2, layer3, layer4):
        self.layer1 = layer1
        self.layer2 = layer2
        self.layer3 = layer3
        self.layer4 = layer4

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1- x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            output_from_layer1, output_from_layer2, output_from_layer3, output_from_layer4 = self.think(training_set_inputs)

            layer4_error = training_set_outputs - output_from_layer4
            layer4_delta = layer4_error * self.__sigmoid_derivative(output_from_layer4)


            layer3_error = layer4_delta.dot(self.layer4.synaptic_weights.T)
            layer3_delta = layer3_error * self.__sigmoid_derivative(output_from_layer3)


            layer2_error = layer3_delta.dot(self.layer3.synaptic_weights.T) #backpropagation
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer2)


            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer1)

            layer1_adjustement = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustement = output_from_layer1.T.dot(layer2_delta)
            layer3_adjustement = output_from_layer2.T.dot(layer3_delta)
            layer4_adjustement = output_from_layer3.T.dot(layer4_delta)

            self.layer1.synaptic_weights += layer1_adjustement
            self.layer2.synaptic_weights += layer2_adjustement
            self.layer3.synaptic_weights += layer3_adjustement
            self.layer4.synaptic_weights += layer4_adjustement

    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        output_from_layer3 = self.__sigmoid(dot(output_from_layer2, self.layer3.synaptic_weights))
        output_from_layer4 = self.__sigmoid(dot(output_from_layer3, self.layer4.synaptic_weights))
        return output_from_layer1, output_from_layer2, output_from_layer3, output_from_layer4


    def print_weights(self):
        print "     Layer 1 (10 neurons, each with 3 inputs): "
        print  self.layer1.synaptic_weights
        print "     Layer 2 (5 neuron, 10 inputs): "
        print  self.layer2.synaptic_weights
        print "     Layer 3 (5 neuron, 5 inputs): "
        print  self.layer3.synaptic_weights
        print "     Layer 4 (1 neuron, 5 inputs): "
        print  self.layer4.synaptic_weights



if __name__ == "__main__":

    random.seed(1)


    layer1 = NeuronLayer(3, 3)

    layer2 = NeuronLayer(3, 3)

    layer3 = NeuronLayer(3, 3)

    layer4 = NeuronLayer(1, 3)

    neural_network = NeuralNetwork(layer1, layer2, layer3, layer4)

    print "Stage 1) Random starting synaptic weights: "
    neural_network.print_weights()


    training_set_inputs = array([[0,0,1],[0,1,1],[1,0,1], [0,1,0],[1,0,0],[1,1,1],[0,0,0]])
    training_set_outputs = array([[0,1,1,1,1,0,0]]).T


    neural_network.train(training_set_inputs, training_set_outputs, 1000000)


    print "Stage 2) New synaptic weights after training: "
    neural_network.print_weights()


    print "Stage 3) Considering a new situation [1,1,0] -> ?: "
    hidden_state1, hidden_state2, hidden_state3, output = neural_network.think(array([1,1,0]))
    print output
