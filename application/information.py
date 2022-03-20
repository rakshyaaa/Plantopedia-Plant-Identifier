
dataInfo ={'amala':"Aamla, also known as Indian gooseberries, grows on a flowering tree of the same name. The small berries are round and bright or yellow-green. ",
 'baganbilas':"Bougainvilleas (Bougainvillea species) are tropical and subtropical woody vines of the Four-O’Clock family (Nyctaginaceae). ",
 'gulbahar':"Gulbahar (Daisy),any of several species of flowering plants belonging to the aster family (Asteraceae). The name daisy commonly denotes the oxeye daisy (Leucanthemum vulgare), the Shasta daisy (L. ×superbum), and the English, or true, daisy (Bellis perennis). These and other plants called daisies are distinguished by a composite flower head composed of 15 to 30 white ray flowers surrounding a centre consisting of bright yellow disk flowers, though other colour combinations are common. ",
 'japakusum':"Japakusum (Hibiscus), is a genus of flowering plants in the mallow family, Malvaceae. The genus is quite large, comprising several hundred species that are native to warm-temperate, subtropical and tropical regions throughout the world. Hibiscus flowers are available in White, Red, Yellow, Pink, Purple, Peach, and Orange colours. In some species of Hibiscus, flowers colour changes with age.",
 'laliguras':"Laliguras (Rhododendron) are plants with beautiful flowers and glossy leaves. The name rhododendron comes from the Greek words for rose (rhodon) and tree (dendron). There are many kinds of rhododendron. Most are evergreen, meaning that they keep their leaves all year. However, some kinds lose their leaves each autumn. These kinds are usually called azaleas. Rhododendrons also vary greatly in size. Some are tiny shrubs or groundcover that are only 4 inches (10 centimeters) tall. Others are treelike plants that grow more than 40 feet (12 meters) tall.",
 'lapsi':"Lapsi (Choerospondias axillaris), known in English as the Nepali hog plum, is a tree in the family Anacardiaceae. It is a common fruit in Nepal also called lapsi and aamli in Nepal Bhasa. It is native to Nepal. Its fruit is about 3 centimeters long and has a soft whitish sour flesh and green to yellow skin. The fruit is made into pickles, fruit tarts, and sour, spicy candy in Nepal. ",
 'neem': "Neem(Azadirachta indica) also called nim or margosa, fast-growing tree of the mahogany family (Meliaceae), valued as a medicinal plant, as a source of organic pesticides, and for its timber. ",
 'sunakhari': "Sunakhari(Orchid), s a member of Asparagales, an order of monocotyledonous flowering plants that also includes the asparagus and iris families. The word orchid is derived from the Greek word (orchis) for testicle because of the shape of the root tubers in some species of the genus Orchis. These nonwoody perennial plants are generally terrestrial or epiphytic herbs.",
 'tulsi':"Tulsi (Holy Basil) flowering plant of the mint family (Lamiaceae) grown for its aromatic leaves. The plant is widely used in Ayurvedic and folk medicine, often as an herbal tea for a variety of ailments, and is considered sacred in Hinduism. It is also used as a culinary herb with a pungent flavour that intensifies with cooking.  ",
 'yarshagumba': "Yarsagumba is a unique caterpillar-fungus fusion that occurs when parasitic mushroom spores (Ophiocordyceps sinensis) infect and mummify a ghost moth larva living in the soil. A spindly fungus later sprouts from the dead caterpillar host head. Yarsagumba thrives in the picturesque peaks of the Himalayas, at altitudes of between 3000 and 5000 meters, in Nepal, India and Bhutan, and also on the “roof of the world” — the Tibetan Plateau.",
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