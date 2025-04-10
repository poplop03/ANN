import numpy as np
w = np.matrix('-0.1 0.2 -0.3')
x = np.matrix('-1 0 0')


def step(input):
    if input > 0:
        return 1
    else:
        return 0

print(    )
y = step(w*x.getT())
print(y)