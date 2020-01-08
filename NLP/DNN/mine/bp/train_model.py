from keras.models import Model
from keras.layers import Dense, Input, Dropout
import numpy as np
from keras import regularizers


def get_data(path):
    with open(path) as f:
        lines = f.readlines()
        lines = [eval(line.strip()) for line in lines]
        x = [line[0] for line in lines]
        y = [line[1] for line in lines]
        # print('x===', x)
        # print('y===', y)
        # x, y = zip(*lines)
        x = np.array(x)
        y = np.array(y)
        # print(type(x))
        return x, y


x, y = get_data('data/data')

'''
Get the dense model layer01
'''
dense_1 = Dense(input_dim=4, activation='sigmoid', units=5, name='layer1')
print('typeof(dense_1)={}'.format(type(dense_1)))

'''
Fit the input params to the dense
'''

input = Input(shape=(4,))
result_1 = dense_1(input)
print('typeof result1 = {}'.format(type(result_1)))
dropout = Dropout(0.2)
print('typeof dropout = {}'.format(type(dropout)))
layer1 = dropout(result_1)
print('type of the layer1={}'.format(type(layer1)))

'''
Get the dense layer_02
'''
# dense2 = Dense(units=6, activation='sigmoid', name='layer2', kernel_regularizer=regularizers.l1(0.02))(layer1)
dense2 = Dense(units=5, activation='sigmoid', name='layer2', kernel_regularizer=regularizers.l1(0.02))(layer1)

dropout = Dropout(0.2)
layer2 = dropout(dense2)
print('the type of layer2 is={}'.format(type(layer2)))
'''
Get the output layer
'''

'''
add the layer3 with 5units,sigmoid activation,l1 regularation
'''
layer3 = Dense(name='layer3', units=5, activation='sigmoid', kernel_regularizer=regularizers.l1(0.02))(layer2)

# output_layer = Dense(units=3, activation='softmax')(layer2)
output_layer = Dense(units=3, activation='softmax')(layer3)

'''
init the Model
'''
model = Model(inputs=input, outputs=output_layer)

# model.compile(optimizer='RMSProp', loss='categorical_crossentropy')
model.compile(optimizer='adam', loss='categorical_crossentropy')

model.fit(x, y, batch_size=8, shuffle=True, epochs=100)

'''
Evaluate the model with AUC and ROC
'''
# print('optimizer with RMSProp Done!')
print('optimizer with adam Done!')