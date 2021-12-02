
dataInfo ={'amala':"Amla, also known as Indian gooseberries, grows on a flowering tree of the same name. The small berries are round and bright or yellow-green. ",
 'baganbilas':"Bougainvilleas (Bougainvillea species) are tropical and subtropical woody vines of the Four-O’Clock family (Nyctaginaceae). ",
 'gulbahar':"This is gulbhar info",
 'japakusum':"This is japakusum info",
 'laliguras':"This is lalgiuras",
 'lapsi':"this is lapsi",
 'neem': "this is neem",
 'sunakhari': "this is sunakhari",
 'tulsi':"this is tulsi",
 'yarshagumba': "this is yarshagumba",
'':'Opps! The confidence is very low. This might not be a plant.'
}

class info:
    def __init__(self):
        self.data = dataInfo
    def getinfo(self, name):
        # print(name)
        # print(type(name))
        # print(self.data[name])
        return self.data[name]