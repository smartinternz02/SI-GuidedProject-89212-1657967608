from flask import Flask, render_template, request# Flask-It is our framework which we are going to use to run/serve our application.
#request-for accessing file which was uploaded by the user on our application.

from PIL import Image #used for manipulating image uploaded by the user.
import numpy as np #used for numerical analysis
from tensorflow.keras.models import load_model#to load our model trained with MNIST data
import tensorflow as tf#to run our model.


app = Flask(__name__) #our flask app
model = load_model("C:/project/temp/templates/models/mnistCNN.h5") #loading the model


@app.route('/') #default route
def upload_file():
   return render_template('main.html') #rendering html page
@app.route('/about') #Main page route
def upload_file1():
   return render_template('main.html') #rendering html page
@app.route('/upload') #main page route
def upload_file2():
   return render_template('index6.html')


@app.route('/predict', methods = ['POST']) #route for our predictio
def upload_image_file():
   if request.method == 'POST': 
      img = Image.open(request.files['file'].stream).convert("L")# convert image to monochrome
      img = img.resize((28,28))# resizing of input image
      im2arr = np.array(img)#converting to image
      im2arr = im2arr.reshape(1,28,28,1) #reshaping according to our requirement
      #y_pred = (model.predict(im2arr) > 0.5).astype("int32")#model.predict_classes(im2arr) #predicting the results (model.predict(im2arr) > 0.5).astype("int32")
      predict_x=model.predict(im2arr)
      y_pred=np.argmax(predict_x,axis=1)
      a=y_pred[0]
      y_pred=a
      print(a)
      #print(y_pred[0]) #printing our result in prompt
      #return 'Predicted Number: ' + str(y_pred) #returning our output
      
      if(y_pred == 0) :
        return render_template("0.html",showcase =  str(y_pred))
      elif(y_pred == 1) :
        return render_template("1.html",showcase =  str(y_pred))
      elif(y_pred == 2) :
        return render_template("2.html",showcase =  str(y_pred))
      elif(y_pred == 3) :
        return render_template("3.html",showcase =  str(y_pred))
      elif(y_pred == 4) :
        return render_template("4.html",showcase =  str(y_pred))
      elif(y_pred == 5) :
        return render_template("5.html",showcase =  str(y_pred))
      elif(y_pred == 6) :
        return render_template("6.html",showcase =  str(y_pred))
      elif(y_pred == 7) :
        return render_template("7.html",showcase =  str(y_pred))
      elif(y_pred == 8) :
        return render_template("8.html",showcase =  str(y_pred))
      else :
        return render_template("9.html",showcase =  str(y_pred))
   else:
        return None
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
   #app.run(debug = True) #running our flask app
