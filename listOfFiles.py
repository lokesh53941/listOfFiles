import os
path = input("enter the path" )
for root,dirs,files in os.walk(path):
    for f in files:
        print(os.path.join(root,f))
