import turtle
from swordfunc import *

turtle.colormode(255)
#drawing of pommel
for x in range (0, 41, 20):
	squaredrawing2(x,0,20,39,29,13)

squaredrawing2(40,20,20,39,29,13)
for y in range (0,41,20):
	squaredrawing2(0,y,20,39,29,13)
	squaredrawing2(20,y,20,39,29,13)

#this code could not be abstracted due to the weird set of co-ordinates, may look into how to abstract later... for now we have this
#drawing of hilt and hand guard
squaredrawing2(80,100,20,39,29,13)
squaredrawing2(100,80,20,39,29,13)

squaredrawing2(100,100,20,109,73,27)
squaredrawing2(80,120,20,109,73,27)
squaredrawing2(80,140,20,109,73,27)
squaredrawing2(60,160,20,87,59,22)
squaredrawing2(120,80,20,109,73,27)
squaredrawing2(140,80,20,87,59,22)
squaredrawing2(160,60,20,87,59,22)

squaredrawing2(60,120,20,39,29,13)
squaredrawing2(60,140,20,39,29,13)
squaredrawing2(40,160,20,39,29,13)
squaredrawing2(40,180,20,39,29,13)
squaredrawing2(60,180,20,39,29,13)
squaredrawing2(80,160,20,39,29,13)
squaredrawing2(100,140,20,39,29,13)
squaredrawing2(100,120,20,39,29,13)

squaredrawing2(120,60,20,39,29,13)
squaredrawing2(140,60,20,39,29,13)
squaredrawing2(160,40,20,39,29,13)
squaredrawing2(180,40,20,39,29,13)
squaredrawing2(180,60,20,39,29,13)
squaredrawing2(160,80,20,39,29,13)
squaredrawing2(140,100,20,39,29,13)
squaredrawing2(120,100,20,39,29,13)

squaredrawing2(20,20,20,87,59,22)

squaredrawing2(40,40,20,109,73,27)

squaredrawing2(60,40,20,48,35,15)
squaredrawing2(80,60,20,48,35,15)


squaredrawing2(40,60,20,64,47,19)
squaredrawing2(60,80,20,64,47,19)


squaredrawing2(60,60,20,140,94,33)

squaredrawing2(80,80,20,109,73,27)

#the blade
for y in range(160,301,20):
	x=y-40
	squaredrawing2(x,y,20,61,44,17)

for x in range (160,321, 20):
	y=x-40
	squaredrawing2(x,y,20,61,44,17)

squaredrawing2(320,300,20,61,44,17)
squaredrawing2(320,320,20,61,44,17)
squaredrawing2(300,320,20,61,44,17)#these 4 lines are too strangely positioned to work with the previous loop
squaredrawing2(280,320,20,61,44,17)

for x in range (120,301,20):
	y=x
	squaredrawing2(x,y,20,117,79,28)

for x in range (120,281,20):
	y=x+20
	squaredrawing2(x,y,20,140,94,33)


for x in range(140,301,20):
	y=x-20
	squaredrawing2(x,y,20,140,94,33)






# the stone sword begins here






for x in range (0, 41, 20):
	squaredrawing3(x,0,20,60,60,60)

squaredrawing3(40,20,20,60,60,60)
for y in range (0,41,20):
	squaredrawing3(0,y,20,60,60,60)
	squaredrawing3(20,y,20,60,60,60)

#drawing of hilt and hand guard
squaredrawing3(80,100,20,60,60,60)
squaredrawing3(100,80,20,60,60,60)

squaredrawing3(100,100,20,107,107,107)
squaredrawing3(80,120,20,107,107,107)
squaredrawing3(80,140,20,107,107,107)
squaredrawing3(60,160,20,84,84,84)
squaredrawing3(120,80,20,107,107,107)
squaredrawing3(140,80,20,84,84,84)
squaredrawing3(160,60,20,84,84,84)

squaredrawing3(60,120,20,60,60,60)
squaredrawing3(60,140,20,60,60,60)
squaredrawing3(40,160,20,60,60,60)
squaredrawing3(40,180,20,60,60,60)
squaredrawing3(60,180,20,60,60,60)
squaredrawing3(80,160,20,60,60,60)
squaredrawing3(100,140,20,60,60,60)
squaredrawing3(100,120,20,60,60,60)

squaredrawing3(120,60,20,60,60,60)
squaredrawing3(140,60,20,60,60,60)
squaredrawing3(160,40,20,60,60,60)
squaredrawing3(180,40,20,60,60,60)
squaredrawing3(180,60,20,60,60,60)
squaredrawing3(160,80,20,60,60,60)
squaredrawing3(140,100,20,60,60,60)
squaredrawing3(120,100,20,60,60,60)

squaredrawing3(20,20,20,107,107,107)

squaredrawing3(40,40,20,109,73,27)

squaredrawing3(60,40,20,48,35,15)
squaredrawing3(80,60,20,48,35,15)


squaredrawing3(40,60,20,64,47,19)
squaredrawing3(60,80,20,64,47,19)


squaredrawing3(60,60,20,140,94,33)

squaredrawing3(80,80,20,109,73,27)

#the blade
for y in range(160,301,20):
	x=y-40
	squaredrawing3(x,y,20,71,71,71)

for x in range (160,321, 20):
	y=x-40
	squaredrawing3(x,y,20,71,71,71)

squaredrawing3(320,300,20,71,71,71)
squaredrawing3(320,320,20,71,71,71)
squaredrawing3(300,320,20,71,71,71)
squaredrawing3(280,320,20,71,71,71)
for x in range (120,301,20):
	y=x
	squaredrawing3(x,y,20,174,174,174)

for x in range (120,281,20):
	y=x+20
	squaredrawing3(x,y,20,195,195,195)


for x in range(140,301,20):
	y=x-20
	squaredrawing3(x,y,20,195,195,195)





#iron sword begins here


for x in range (0, 41, 20):
	squaredrawing4(x,0,20,38,38,38)

squaredrawing4(40,20,20,38,38,38)
for y in range (0,41,20):
	squaredrawing4(0,y,20,38,38,38)
	squaredrawing4(20,y,20,38,38,38)

#drawing of hilt and hand guard
squaredrawing4(80,100,20,38,38,38)
squaredrawing4(100,80,20,38,38,38)

squaredrawing4(100,100,20,121,121,121)
squaredrawing4(80,120,20,121,121,121)
squaredrawing4(80,140,20,121,121,121)
squaredrawing4(60,160,20,93,93,93)
squaredrawing4(120,80,20,121,121,121)
squaredrawing4(140,80,20,93,93,93)
squaredrawing4(160,60,20,93,93,93)

squaredrawing4(60,120,20,38,38,38)
squaredrawing4(60,140,20,38,38,38)
squaredrawing4(40,160,20,38,38,38)
squaredrawing4(40,180,20,38,38,38)
squaredrawing4(60,180,20,38,38,38)
squaredrawing4(80,160,20,38,38,38)
squaredrawing4(100,140,20,38,38,38)
squaredrawing4(100,120,20,38,38,38)

squaredrawing4(120,60,20,38,38,38)
squaredrawing4(140,60,20,38,38,38)
squaredrawing4(160,40,20,38,38,38)
squaredrawing4(180,40,20,38,38,38)
squaredrawing4(180,60,20,38,38,38)
squaredrawing4(160,80,20,38,38,38)
squaredrawing4(140,100,20,38,38,38)
squaredrawing4(120,100,20,38,38,38)

squaredrawing4(20,20,20,121,121,121)

squaredrawing4(40,40,20,109,73,27)

squaredrawing4(60,40,20,48,35,15)
squaredrawing4(80,60,20,48,35,15)


squaredrawing4(40,60,20,64,47,19)
squaredrawing4(60,80,20,64,47,19)


squaredrawing4(60,60,20,140,94,33)

squaredrawing4(80,80,20,109,73,27)

#the blade
for y in range(160,301,20):
	x=y-40
	squaredrawing4(x,y,20,61,61,61)

for x in range (160,321, 20):
	y=x-40
	squaredrawing4(x,y,20,61,61,61)

squaredrawing4(320,300,20,61,61,61)
squaredrawing4(320,320,20,61,61,61)
squaredrawing4(300,320,20,61,61,61)
squaredrawing4(280,320,20,61,61,61)
for x in range (120,301,20):
	y=x
	squaredrawing4(x,y,20,221,221,221)

for x in range (120,281,20):
	y=x+20
	squaredrawing4(x,y,20,255,255,255)


for x in range(140,301,20):
	y=x-20
	squaredrawing4(x,y,20,255,255,255)



#gold sword beginning


for x in range (0, 41, 20):
	squaredrawing5(x,0,20,62,63,9)

squaredrawing5(40,20,20,63,63,9)
for y in range (0,41,20):
	squaredrawing5(0,y,20,63,63,9)
	squaredrawing5(20,y,20,63,63,9)

#drawing of hilt and hand guard
squaredrawing5(80,100,20,62,63,9)
squaredrawing5(100,80,20,62,63,9)

squaredrawing5(100,100,20,185,189,28)
squaredrawing5(80,120,20,185,189,28)
squaredrawing5(80,140,20,185,189,28)
squaredrawing5(60,160,20,138,139,21)
squaredrawing5(120,80,20,185,189,28)
squaredrawing5(140,80,20,138,139,21)
squaredrawing5(160,60,20,138,139,21)

squaredrawing5(60,120,20,62,63,9)
squaredrawing5(60,140,20,62,63,9)
squaredrawing5(40,160,20,62,63,9)
squaredrawing5(40,180,20,62,63,9)
squaredrawing5(60,180,20,62,63,9)
squaredrawing5(80,160,20,62,63,9)
squaredrawing5(100,140,20,62,63,9)
squaredrawing5(100,120,20,62,63,9)

squaredrawing5(120,60,20,62,63,9)
squaredrawing5(140,60,20,62,63,9)
squaredrawing5(160,40,20,62,63,9)
squaredrawing5(180,40,20,62,63,9)
squaredrawing5(180,60,20,62,63,9)
squaredrawing5(160,80,20,62,63,9)
squaredrawing5(140,100,20,62,63,9)
squaredrawing5(120,100,20,62,63,9)

squaredrawing5(20,20,20,185,189,28)

squaredrawing5(40,40,20,109,73,27)

squaredrawing5(60,40,20,48,35,15)
squaredrawing5(80,60,20,48,35,15)


squaredrawing5(40,60,20,64,47,19)
squaredrawing5(60,80,20,64,47,19)


squaredrawing5(60,60,20,140,94,33)

squaredrawing5(80,80,20,109,73,27)

#the blade
for y in range(160,301,20):
	x=y-40
	squaredrawing5(x,y,20,81,83,12)

for x in range (160,321, 20):
	y=x-40
	squaredrawing5(x,y,20,81,83,12)

squaredrawing5(320,300,20,81,83,12)
squaredrawing5(320,320,20,81,83,12)
squaredrawing5(300,320,20,81,83,12)
squaredrawing5(280,320,20,81,83,12)
for x in range (120,301,20):
	y=x
	squaredrawing5(x,y,20,213,218,32)

for x in range (120,281,20):
	y=x+20
	squaredrawing5(x,y,20,249,250,98)


for x in range(140,301,20):
	y=x-20
	squaredrawing5(x,y,20,249,250,98)


#diamond sword begins



for x in range (0, 41, 20):
	squaredrawing(x,0,20,19,35,35)

squaredrawing(40,20,20,19,35,35)
for y in range (0,41,20):
	squaredrawing(0,y,20,19,35,35)
	squaredrawing(20,y,20,19,35,35)

#drawing of hilt and hand guard
squaredrawing(80,100,20,19,35,35)
squaredrawing(100,80,20,19,35,35)

squaredrawing(100,100,20,55,130,129)
squaredrawing(80,120,20,55,130,129)
squaredrawing(80,140,20,55,130,129)
squaredrawing(60,160,20,39,93,92)
squaredrawing(120,80,20,55,130,129)
squaredrawing(140,80,20,39,93,92)
squaredrawing(160,60,20,39,93,92)

squaredrawing(60,120,20,19,35,35)
squaredrawing(60,140,20,19,35,35)
squaredrawing(40,160,20,19,35,35)
squaredrawing(40,180,20,19,35,35)
squaredrawing(60,180,20,19,35,35)
squaredrawing(80,160,20,19,35,35)
squaredrawing(100,140,20,19,35,35)
squaredrawing(100,120,20,19,35,35)

squaredrawing(120,60,20,19,35,35)
squaredrawing(140,60,20,19,35,35)
squaredrawing(160,40,20,19,35,35)
squaredrawing(180,40,20,19,35,35)
squaredrawing(180,60,20,19,35,35)
squaredrawing(160,80,20,19,35,35)
squaredrawing(140,100,20,19,35,35)
squaredrawing(120,100,20,19,35,35)

squaredrawing(20,20,20,55,130,129)

squaredrawing(40,40,20,109,73,27)

squaredrawing(60,40,20,48,35,15)
squaredrawing(80,60,20,48,35,15)


squaredrawing(40,60,20,64,47,19)
squaredrawing(60,80,20,64,47,19)


squaredrawing(60,60,20,140,94,33)

squaredrawing(80,80,20,109,73,27)

#the blade
for y in range(160,301,20):
	x=y-40
	squaredrawing(x,y,20,24,48,48)

for x in range (160,321, 20):
	y=x-40
	squaredrawing(x,y,20,24,48,48)

squaredrawing(320,300,20,24,48,48)
squaredrawing(320,320,20,24,48,48)
squaredrawing(300,320,20,24,48,48)
squaredrawing(280,320,20,24,48,48)
for x in range (120,301,20):
	y=x
	squaredrawing(x,y,20,77,183,181)

for x in range (120,281,20):
	y=x+20
	squaredrawing(x,y,20,92,218,216)


for x in range(140,301,20):
	y=x-20
	squaredrawing(x,y,20,92,218,216)







turtle.done()


