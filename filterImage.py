# List all files
import os
import re
import json 
import pandas as pd


def jpeg_res(filename):

   # open image for reading in binary mode
   with open(filename,'rb') as img_file:

    # height of image (in 2 bytes) is at 164th position
    img_file.seek(163)

    # read the 2 bytes
    twoBytes = img_file.read(2)

    # calculate height
    height = (twoBytes[0] << 8) + a[1]

    # next 2 bytes is width
    twoBytes = img_file.read(2)

       # calculate width
    width = (twoBytes[0] << 8) + twoBytes[1]
    
    #input(width,height)
    # print("The resolution of the image is",width,"x",height)
    return '{} x {}'.format(width,height)


folder = os.getcwd()
list_file=[]
list_path=[]
extension=[]

for (dirpath, dirnames, filenames) in os.walk('.'):
    for files in filenames: 
        if os.path.splitext(files)[1][1:].strip() in ("jpg","png"):  #filter extension type
            list_file.append(files)
            list_path1=(folder+(str(os.path.join(dirpath,files)))[1:])
            list_path.append(list_path1)
            extension1 = os.path.splitext(files)[1][1:].strip() 
            extension.append(extension1)

size=[]
for path in list_path:
    size.append(jpeg_res(path))
size


data = {'filename':list_file,'location':list_path,'extension':extension,'size': size}
dataFrame = pd.DataFrame(data)

#export to json

result = dataFrame.to_json(orient="index")
parsed = json.loads(result)
json_object=json.dumps(parsed, indent=4)  

# Writing to sample.json 
with open("ouput.json", "w") as outfile: 
    outfile.write(json_object)