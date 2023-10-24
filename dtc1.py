import numpy as np
import pandas as pd
from sklearn import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
training_data = np.genfromtxt('conc.csv', delimiter=',')
inputs = training_data[:,:-1]
outputs = training_data[:, -1]
training_inputs = inputs[:900]
training_outputs = outputs[:900]
testing_inputs = inputs[900:]
testing_outputs = outputs[900:]
classifier = DecisionTreeClassifier()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of DT Classifier on testing data is: " + str(accuracy))
testSet = [[540,1040,676,162,0,0,2.5,28]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
if (int(predictions) ==0):
   print('Predicted compressive strength range of the first concrete mix is: 1 to 10 MPa')
elif (int(predictions) ==1):
   print('Predicted compressive strength range of the first concrete mix is: 11 to 20 MPa')
elif (int(predictions) ==2):
   print('Predicted compressive strength range of the first concrete mix is: 21 to 30 MPa')
elif (int(predictions) ==3):
   print('Predicted compressive strength range of the first concrete mix is: 31 to 40 MPa')
elif (int(predictions) ==4):
   print('Predicted compressive strength range of the first concrete mix is: 41 to 50 MPa')
elif (int(predictions) ==5):
   print('Predicted compressive strength range of the first concrete mix is: 51 to 60 MPa')
elif (int(predictions) ==6):
   print('Predicted compressive strength range of the first concrete mix is: 61 to 70 MPa')
elif (int(predictions) ==7):
   print('Predicted compressive strength range of the first concrete mix is: 71 to 80 MPa')
elif (int(predictions) ==8):
   print('Predicted compressive strength range of the first concrete mix is: 81 to 90 MPa')
else:
   print('Predicted compressive strength range of the first concrete mix is: 91 to 100 MPa')
testSet = [[198.6,978.4,825.5,192,132.4,0,0,28]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
if (int(predictions) ==0):
   print('Predicted compressive strength range of the second concrete mix is: 1 to 10 MPa')
elif (int(predictions) ==1):
   print('Predicted compressive strength range of the second concrete mix is: 11 to 20 MPa')
elif (int(predictions) ==2):
   print('Predicted compressive strength range of the second concrete mix is: 21 to 30 MPa')
elif (int(predictions) ==3):
   print('Predicted compressive strength range of the second concrete mix is: 31 to 40 MPa')
elif (int(predictions) ==4):
   print('Predicted compressive strength range of the second concrete mix is: 41 to 50 MPa')
elif (int(predictions) ==5):
   print('Predicted compressive strength range of the second concrete mix is: 51 to 60 MPa')
elif (int(predictions) ==6):
   print('Predicted compressive strength range of the second concrete mix is: 61 to 70 MPa')
elif (int(predictions) ==7):
   print('Predicted compressive strength range of the second concrete mix is: 71 to 80 MPa')
elif (int(predictions) ==8):
   print('Predicted compressive strength range of the second concrete mix is: 81 to 90 MPa')
else:
   print('Predicted compressive strength range of the second concrete mix is: 91 to 100 MPa')