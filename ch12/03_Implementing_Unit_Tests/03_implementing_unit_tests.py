#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
import numpy as np

# Create a nested gate: $f(x) = a1 * x + b1$
# 
# 
#   a1 --
#       |
#       |-- (multiply)--
#       |               |
#   x --                |-- (add) -->output
#                       |
#                   b1 --
# 



class MyCustomGate(tf.keras.layers.Layer):
 
    def __init__(self, units, a1, b1):
        super(MyCustomGate, self).__init__()
        self.units = units
        self.a1 = a1
        self.b1 = b1

    # Compute f(x) = a1 * x + b1
    def call(self, inputs):
        return inputs * self.a1 + self.b1



class MyCustomGateTest(tf.test.TestCase):

    def setUp(self):
        super(MyCustomGateTest, self).setUp()
        # Configure the layer with 1 unit, a1 = 2 et b1=1
        self.my_custom_gate = MyCustomGate(1,2,1)

    def testMyCustomGateOutput(self):
        input_x = np.array([[1,0,0,1],
                           [1,0,0,1]])
        output = self.my_custom_gate(input_x)
        expected_output = np.array([[3,1,1,3], [3,1,1,3]])

        self.assertAllEqual(output, expected_output)


tf.test.main()


