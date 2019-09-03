"""
This is a quick and dirty version of what I think we are trying to do.

Basic concept:
1) Load up a png 
2) Figure out 
"""


Nsy = 19 #squares across
Nsx = 23 #squares downward

img = mpimg.imread("samples/dungeon.png")
# sets image to array of pixels
Npx, Npy = img.shape[0],img.shape[1]
#number of pixels in either direction
print(img.shape)
print(img[0,0])
print(Npx, Npy)
print(float(Npx)/Nsx, float(Npy)/Nsy) #THIS WILL BE CONSTANT THROUGHOUT DUNGEONS
Nspx, Nspy = float(Npx)/Nsx, float(Npy)/Nsy #SAME WITH THIS PROBLY
#number of pixels per pathfinder square
#The pixels aren't perfect. fuck us, right?

#Loop over all squares and find the average color, if it's close to black then
#take note
fill_array = np.empty((Nsx,Nsy))
eps = 0.001 #if ave is less than this then it's black
#NOTE: Apparently the img is indexed Nsy x Nsx,
#as in, down is the x-direction.
for i in range(Nsx):
    for j in range(Nsy):
        x0,x1 = int(i*Nspx),int((i+1)*Nspx)
        y0,y1 = int(j*Nspy),int((j+1)*Nspy)
        ave = np.mean(img[x0:x1,y0:y1])
        #this is the average of all the pixels within that maptool grid square thing
        if i==0 and j ==0:
            #initialize the image
            p = plt.imshow(img[x0:x1,y0:y1])
            print(img[x0:x1, y0:y1])
        else:
            p.set_data(img[x0:x1,y0:y1])
        print (i,j,ave)
        if ave < eps:# or ave!=ave:
            #plt.pause(0.5)
            fill_array[i,j] = ave #1 #fill it in
        else:
            fill_array[i,j] = ave
            #plt.pause(5.0)
            continue
        continue
    continue

print(fill_array.shape, fill_array.flatten().shape)
print(np.max(fill_array), np.min(fill_array))
plt.clf()
plt.hist(fill_array.flatten(),bins=100)
plt.show()
#print fill_array
plt.imshow(img)
plt.show()
