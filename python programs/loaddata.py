import pickle
f=open("filetxt.txt","rb")
l=pickle.load(f)
print(l)