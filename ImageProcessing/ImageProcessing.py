from PIL import Image 
import random

def makeBnW(image) :
    pixelsOP = []
    pixels = list(image.getdata())
    for pixel in pixels :
        tupp=[]
        summ = int((pixel[0]+pixel[1]+pixel[2])/3)
        tupp.append(summ)
        tupp.append(summ)
        tupp.append(summ)
        pixelsOP.append(tuple(tupp) )
    image_out = Image.new(image.mode,image.size)
    image_out.putdata(pixelsOP)
    image_out.save("C:\\Users\\Hp\\Desktop\\ImageProcessing\\BnW.jpg")
    image_out.close()

def makeGrainy(image) :
    pixelsOP = []
    pixels = list(image.getdata())
    for pixel in pixels :
        tupp=[]
        summ = int((pixel[0]+pixel[1]+pixel[2])/3)
        num=random.randint(0,100)
        tupp.append(summ+num)
        tupp.append(summ+num)
        tupp.append(summ+num)
        pixelsOP.append(tuple(tupp) )
    image_out = Image.new(image.mode,image.size)
    image_out.putdata(pixelsOP)
    image_out.save("C:\\Users\\Hp\\Desktop\\ImageProcessing\\grainy.jpg")
    image_out.close()
    
def onlyRed(image) :
    pixelsOP = []
    pixels = list(image.getdata())
    for pixel in pixels :
        tupp=[]
        summ = int((pixel[0]+pixel[1]+pixel[2])/3)
        if (pixel[0]>(pixel[1]+pixel[2]) and pixel[0]/1.8>pixel[1]):
            tupp.append(pixel[0])
        else:
            tupp.append(summ)
        tupp.append(summ)
        tupp.append(summ)
        pixelsOP.append(tuple(tupp) )
    image_out = Image.new(image.mode,image.size)
    image_out.putdata(pixelsOP)
    image_out.save("C:\\Users\\Hp\\Desktop\\ImageProcessing\\Only_Red.jpg")
    image_out.close()    


def makeNegative(image) :
    pixelsOP = []
    pixels = list(image.getdata())
    for pixel in pixels :
        tupp=[]
        
        tupp.append(255-pixel[0])
        tupp.append(255-pixel[1])
        tupp.append(255-pixel[2])
        pixelsOP.append(tuple(tupp) )
    image_out = Image.new(image.mode,image.size)
    image_out.putdata(pixelsOP)
    image_out.save("C:\\Users\\Hp\\Desktop\\ImageProcessing\\negative.jpg")
    image_out.close()


def reverseNegative(image) :
    pixelsOP = []
    pixels = list(image.getdata())
    for pixel in pixels :
        tupp=[]
        
        tupp.append(255-pixel[0])
        tupp.append(255-pixel[1])
        tupp.append(255-pixel[2])
        pixelsOP.append(tuple(tupp) )
    image_out = Image.new(image.mode,image.size)
    image_out.putdata(pixelsOP)
    image_out.save("C:\\Users\\Hp\\Desktop\\ImageProcessing\\negative_reverse.jpg")
    image_out.close()
    
def swapRnG(image) :
    pixelsOP = []
    pixels = list(image.getdata())
    for pixel in pixels :
        tupp=[]
        tupp.append(pixel[1])
        tupp.append(pixel[0])
        tupp.append(pixel[2])
        pixelsOP.append(tuple(tupp) )
    image_out = Image.new(image.mode,image.size)
    image_out.putdata(pixelsOP)
    image_out.save("C:\\Users\\Hp\\Desktop\\ImageProcessing\\swapped_RnG.jpg")
    image_out.close()
    
def halfNegative(image) :
    pixelsOP = []
    pixels = list(image.getdata())
    width,height = image.size
    cnt=0;
    for pixel in pixels :
        tupp=[]
        if(cnt<width and cnt >width/2):
            summ = int((pixel[0]+pixel[1]+pixel[2])/3)
            tupp.append(summ)
            tupp.append(summ)
            tupp.append(summ)
        else:
            tupp.append(pixel[0])
            tupp.append(pixel[1])
            tupp.append(pixel[2])
        pixelsOP.append(tuple(tupp) )
        cnt+=1
        if(cnt==width):
            cnt=0
    image_out = Image.new(image.mode,image.size)
    image_out.putdata(pixelsOP)
    image_out.save("C:\\Users\\Hp\\Desktop\\ImageProcessing\\half_BnW.jpg")
    image_out.close()
    


image = Image.open(r"C:\\Users\\Hp\\Desktop\\red.jpg")
image1 = Image.open(r"C:\\Users\\Hp\\Desktop\\buddha.jfif")
onlyRed(image)
swapRnG(image)
makeBnW(image)
makeNegative(image)
reverseNegative(image1)
makeGrainy(image)
halfNegative(image)