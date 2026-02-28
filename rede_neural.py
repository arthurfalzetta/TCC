import numpy as np


class RedeNeural:
    def __init__(self, input_size=3, hidden_size=6, output_size=2):
        #pesos aleatorios
        self.w1 = np.random.randn(input_size, hidden_size)
        self.w2 = np.random.randn(hidden_size, output_size)

    def forward(self, x):
        x = np.array(x)

        h = np.tanh(np.dot(x, self.w1))
        out = np.tanh(np.dot(h, self.w2))

        return out