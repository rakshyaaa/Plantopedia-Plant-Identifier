from fastai.vision import *
from fastai import *
from PIL import Image as im
import torchvision.transforms as T

class plantPredict:
    def __init__(self):
        path= ('./models')
        self.learn = load_learner(path = path)
        #print(self.learn)

    def prediction(self, image):
        #print(image)
        #print(type(image))
        img_pil = im.open(image) #image temporary file to pillow object
        img_tensor = T.ToTensor()(img_pil) #pillow object to tensor
        img_fastai = Image(img_tensor)
        pred_class,pred_idx,outputs = self.learn.predict(img_fastai)
        # print(pred_class)
        outputs = torch.max(outputs)
        probabilility = (float(outputs))
        percentage = round((probabilility * 100),3)
        s = "I'm " + str(percentage) + " % sure that it was " + str(pred_class) + ". "
        if percentage < 60:
            pred_class = ""
        return s, str(pred_class)

