# AutoVisionBlocker
The goal is to automatically perform vision blocking in pictures of RPG dungeons. This would allow vision blocking to be created automatically and incorporated into MapTool maps.
## How to use
I don't have a GUI made up, so here is how you use it:

### First:
Make sure the image works in maptool. I don't know why some .png images work and other don't. this won't magically fix the image so the file needs to work by itself before any vision blocking can be added.
### MapMaker.py
On the bottom of the file you will see ``` makeMap("samples/forest.png",'forestMap') ```. Change them to the path to the image, and the desired filename respectively. You will then run the script and if all goes well your map will be in the output directory. :)
#### Fine-tuning
In the map maker class you will see ```raw_array = ProcessImage(pathToOriginalImg, 3)countedArray = CreateSquares(raw_array, 3)```. Some images require some modifying of the "resolution" of the image and the size of VB squares drawn. Of course you can dive in and change anything you want, but feel free to edit the numbers of the 'resolution' in the ProcessImage function and the VB square size in the CreateSquares function. Larger, blocky maps can get away with larger VB square sizes.
#### How it works:
It basically makes the image greyscale and increases contrast to try and differentiate between "objects" (usually black) and non-objects (usually white). Look in the temp/processed.png to see what the map looks like before the black squares are counted. If you see this is incorrect for your image, you will need to go into PreProcess.py to edit the contrast levels and whatnot. The default levels I've found work pretty well.

Here it is in action!
![pre](/images/pre.PNG)
![post](/images/post.PNG)
