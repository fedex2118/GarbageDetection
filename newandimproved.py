import argparse
import cv2
from os import listdir
from os.path import isfile, join
from collections import OrderedDict
import collections



def drawsquare(img, b,show):
    height, width, channels = img.shape
    xn1= int(b[3]*width/2)
    yn1= int(b[4]*height/2)
    xn = int(b[1]*width)-xn1
    yn = int(b[2]*height)-yn1
    xn1= int(b[3]*width)
    yn1= int(b[4]*height)


    #leftmost = left
    
    cv2.rectangle(
        img,
        (xn, yn),
        (xn + xn1, yn + yn1),
        (200,0,0),
        3
    )
    if show:
        resized_img = cv2.resize(img, (1080, 920))

    # Show result
    
        cv2.imshow("Square", resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




def computeApproxArea(d,img):
    area=0
    total=0
    height, width, channels = img.shape
    kernel_size = 500
    w=1/kernel_size
    h=1/kernel_size
    for x in range(kernel_size):
        for y in range(kernel_size):
            total+=1
            cont = False
            kernel = [0,w*x+w/2,h*y+h/2,w,h]
            for bbox in d:
                b_left=bbox[1]-(bbox[3]/2)
                b_right = bbox[1]+(bbox[3]/2)
                b_top = bbox[2]-(bbox[4]/2)
                b_bottom = bbox[2]+(bbox[4]/2)
                left=w*x
                right = w*(x+1)
                top = h*y
                bottom = h*(y+1)
                inside = b_left<=left<=b_right and b_left<=right<=b_right and b_top<=top<=b_bottom and b_top<=bottom<=b_bottom 
                if inside:
                    #drawsquare(img,kernel,False)
                    area += 1
                    break
    #drawsquare(img,kernel,True)
    return float(area/total)



#x,y,w,h
if __name__=="__main__":
    results={}
    area = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("--computeAll",type=bool,default=False)
    parser.add_argument("--imageName")
    parser.add_argument("--location",default=".")
    args = parser.parse_args()
    computeAll = args.computeAll
    location = args.location
    if computeAll:
        skipped = 0
        filenames = [f for f in listdir(location) if isfile(join(location, f))]
        for file in filenames:
            area = 0
            d={}
            try:
                with open(location+"/labels/"+(file.split(".")[0]+".txt"),"r") as f:
                    img = cv2.imread(location+"/"+file)
                    if img is None:
                        raise FileNotFoundError("Image not found or path is incorrect")
                    height, width, channels = img.shape
                    totalArea = height*width
                    boxes = f.readlines()
                    for b in boxes:

                        b = b.replace('\n',"")
                        b = b.split(" ")
                        for x in range(len(b)):
                            b[x]= float(b[x])
                        w = float(width)*float(b[3])
                        h = float(height)*float(b[4])
                        if (-int(w*h)) in d.keys():
                            d[-int(w*h)].append(b)
                        else: d[-int(w*h)]=[b]


                od = collections.OrderedDict(sorted(d.items()))
                results[file]=computeApproxArea(od,img)
  
            except FileNotFoundError:
                results[file]=0

        for w in sorted(results, key=results.get, reverse=True):
            print(w, results[w])
        print(skipped)

    else:
        imageName = args.imageName
        try:
            with open(location+"/labels/"+(imageName.split(".")[0]+".txt"),"r") as f:
                img = cv2.imread(location+"/"+imageName)
                d=[]
                if img is None:
                    raise FileNotFoundError("Image not found or path is incorrect")
                height, width, channels = img.shape
                totalArea = height*width
                boxes = f.readlines()
                for b in boxes:
                    b = b.replace('\n',"")
                    b = b.split(" ")
                    for x in range(len(b)):
                        b[x]= float(b[x])
                    d.append(b)
                area = computeApproxArea(d,img)
                
            print(area)
        except FileNotFoundError:
            print("file not found")
            print(0)
            print(0)




