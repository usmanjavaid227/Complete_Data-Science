import pickle
l=[1,2,3,4,5,6,7,8]
file=open("filetxt.txt", "wb")
pickle.dump(l,file)
file.close()