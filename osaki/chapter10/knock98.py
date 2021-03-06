from gensim.models import word2vec
from knock96 import mk_country
from matplotlib.pyplot import show
from scipy.cluster.hierarchy import ward,dendrogram

model=word2vec.Word2Vec.load("knock90.model")

d=mk_country(open("../chapter09/country_list.txt","r"))
vec_list=[]
name_list=[]

for key,value in d.items():
    vec_list+=[value]
    name_list+=[key]

result=ward(vec_list)
dendrogram(result,labels=name_list)
show()
