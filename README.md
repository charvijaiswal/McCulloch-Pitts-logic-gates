# McCulloch-Pitts-logic-gates
This repository demonstrates the implementation of various logic gates using the McCulloch-Pitts Neuron Model. The McCulloch-Pitts neuron is a fundamental concept in neural networks and artificial intelligence, and this project showcases its application in creating basic logical operations.

McCulloch-Pitts neuron model:
The very first step towards the perceptron we use today was taken in 1943 by McCulloch and Pitts, by mimicking the functionality of a biological neuron.

Model Architecture:
The motivation behind the McCulloh Pitt’s Model is a biological neuron. A biological neuron takes an input signal from the dendrites and after processing it passes onto other connected neurons as the output if the signal is received positively, through axons and synapses. This is the basic working of a biological neuron which is interpreted and mimicked using the McCulloh Pitt’s Model.

![image](https://github.com/user-attachments/assets/6ac16888-90ac-4f17-8b27-fb0c21a48efe)


McCulloch Pitt’s model of neuron is a fairly simple model which consists of some (n) binary inputs with some weight associated with each one of them. An input is known as ‘inhibitory input’ if the weight associated with the input is of negative magnitude and is known as ‘excitatory input’ if the weight associated with the input is of positive magnitude. As the inputs are binary, they can take either of the 2 values, 0 or 1. 


The inputs of the McCulloch-Pitts neuron could be either 0 or 1. It has a threshold function as an activation function. So, the output signal yout is 1 if the input ysum is greater than or equal to a given threshold value, else 0. The diagrammatic representation of the model is as follows:
![image](https://github.com/user-attachments/assets/be109b57-339b-425e-8dc2-17b23ed80d2b)

Then we have a summation junction that aggregates all the weighted inputs and then passes the result to the activation function. The activation function is a threshold function that gives out 1 as the output if the sum of the weighted inputs is equal to or above the threshold value and 0 otherwise.
Mathematical Representation:

![image](https://github.com/user-attachments/assets/e53015ca-c539-488a-8398-5c1f739577f3)



