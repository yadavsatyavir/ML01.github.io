import os
import numpy
from keras.models import load_model
from keras import backend as K

import nlp_prediction_functios as nlp_pred

APP_ROOT = 'D:\\GITHUB\\Machine Learning\\Application'
text ='Dear John! He loves me very dearly, and hates to have me sick. I tried to have a real earnest reasonable talk with him the other day, and tell him how I wish he would let me go and make a visit to Cousin Henry and Julia.'

resy =  nlp_pred.nlp_predict_next_word_01(APP_ROOT, text)

model = load_model("models/nlp/model_predict_next_word_01.h5")
chars = [line.rstrip('\n') for line in open(os.path.join(APP_ROOT,'models','nlp','char data predict next word 01.txt'))]
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

n_vocab = len(chars)
dataX = []
pattern = text
pattern = pattern[:100]
dataX.append([char_to_int[char] for char in pattern.lower()])
pattern = dataX[0]

# generate characters
alltxt = []
for i in range(300):
	x = numpy.reshape(pattern, (1, len(pattern), 1))
	x = x / float(n_vocab)
	prediction = model.predict(x, verbose=0)
	index = numpy.argmax(prediction)
	result = int_to_char[index]
	alltxt.append(result)
	pattern.append(index)
	pattern = pattern[1:len(pattern)]

alltxt = ''.join(alltxt)
K.clear_session()


