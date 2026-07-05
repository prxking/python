#fobj=open("pyth.txt","w")
#fobj=open("pyth.txt","w")
#fobj.write("python is a high level programming language")
#fobj.close()
#fobj=open("pyth.txt","r")
#print(fobj.readlines())
import pickle
data={name:"python",age:31}
with open("pyth.txt","w") as f:
    pickle.dump(data,f)

