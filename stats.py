import argparse

OurTP=[]
OurExtras=0
OurMistakes=0
HisTP=[]
HisExtras=0
HisMistakes=0
total=0


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()
    filepath = args.filepath
    with open(filepath,"r") as f:
        lines = f.readlines()
        for line in lines:
            if line.__contains__("_"):
                line = line.replace('\n','')
                total+=1
                image=line.split("_")
                print(image)
                if image[1]=="T":
                    OurTP.append(image[0])
                    OurExtras+=int(image[3])
                else: OurMistakes+=int(image[3])
                if image[2]=="T":
                    HisTP.append(image[0])
                    HisExtras+=int(image[4].split(" ")[0])
                else: HisMistakes+=int(image[4].split(" ")[0])

    print("Our TPR is "+str(len(OurTP)/total))
    print("Upon Successfull identification we identify an average of "+str(OurExtras/len(OurTP))+" extra objects")
    print("Upon Unsuccessfull identification we identify an average of "+str(OurMistakes/(total-len(OurTP)))+" extra objects")


    print("His TPR is "+str(len(HisTP)/total))
    print("Upon Successfull identification he identifies an average of "+str(HisExtras/len(HisTP))+" extra objects")
    print("Upon Unsuccessfull identification he identifies an average of "+str(HisMistakes/(total-len(HisTP)))+" extra objects")

