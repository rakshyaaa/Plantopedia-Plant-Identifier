from fastai.vision import *

class plantPredict:
    def __init__(self):
        path= ('./models')
        learn = load_learner(path = path)
        # print(learn)
    
    def prediction(Imageurl):
        img = open_image(Imageurl)
        pred_class,pred_idx,outputs = learn.predict(img)
        print(pred_class.oj)
