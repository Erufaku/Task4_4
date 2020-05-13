import os
from scipy import misc
from numpy import uint8 as u8
from imageio import imread
from imageio import imwrite
a = input()
x,y,w,h,inputfile,outputfile = a.split(' ')
x = int(x)
y = int(y)
w = int(w)
h = int(h)
im = imread(inputfile)
if(x<0): x = 0
if(y<0): y = 0
H = len(im)
W = len(im[0])
print(H,W)
Wigth = int(x+w)
Height = int(y+h)
if(int(x+w) > W): Wigth = W
if(int(y+h) > H): Height = H
om = imwrite(outputfile,im[x:Wigth,y:Height,0])
