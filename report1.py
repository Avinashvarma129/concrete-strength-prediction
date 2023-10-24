import numpy as np
import pandas as pd
from sklearn import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate

import sqlite3
con = sqlite3.connect('concrete1')
training_data = np.genfromtxt('conc.csv', delimiter=',')
inputs = training_data[:,:-1]
outputs = training_data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = DecisionTreeClassifier()
classifier.fit(training_inputs, training_outputs)
with con:
  cur = con.cursor()
  cur.execute('SELECT * FROM mainingr'); 
  result1 = cur.fetchall()
  for row in result1:
    s2 = int(row[0])
    s3 = int(row[1])
    s4 = int(row[2])
    s5 = int(row[3])
  cur.execute('SELECT * FROM otheringr'); 
  result2 = cur.fetchall()
  for row in result2:
    s1 = float(row[0])
    s6 = float(row[1])
    s7 = float(row[2])
    s8 = int(row[3])
result = str(" ")
testSet = [[s1,s2,s3,s4,s5,s6,s7,s8]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
if (int(predictions) ==0):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 1 to 10 MPa')+ "<br/>"
elif (int(predictions) ==1):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 11 to 20 MPa')+ "<br/>"
elif (int(predictions) ==2):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 21 to 30 MPa')+ "<br/>"
elif (int(predictions) ==3):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 31 to 40 MPa')+ "<br/>"
elif (int(predictions) ==4):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 41 to 50 MPa')+ "<br/>"
elif (int(predictions) ==5):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 51 to 60 MPa')+ "<br/>"
elif (int(predictions) ==6):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 61 to 70 MPa')+ "<br/>"
elif (int(predictions) ==7):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 71 to 80 MPa')+ "<br/>"
elif (int(predictions) ==8):
   result = result + str('Predicted compressive strength range of the given concrete mix is: 81 to 90 MPa')+ "<br/>"
else:
   result = result + str('Predicted compressive strength range of the given concrete mix is: 91 to 100 MPa')+ "<br/>"
items = []
items.append(platypus.Paragraph(result,PS('body')))
doc = SimpleDocTemplate('concrep.pdf')
doc.multiBuild(items)
print('Concrete Compressive Strength Report Successfully Generated')
