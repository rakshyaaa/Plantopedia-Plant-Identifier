from fastai.vision import *


path = Path('../models')
print(path)
learn = load_learner(path = path)
print(learn)
