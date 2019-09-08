# AutoVisionBlocker
The goal is to automatically perform vision blocking in pictures of RPG dungeons. This would allow vision blocking to be created automatically and incorporated into MapTool maps.
## How to use
I don't have a GUI made up, so here is how you use it:

### First:
Make sure the image works in maptool. I don't know why some .png images work and other don't. this won't magically fix the image so the file needs to work by itself before any vision blocking can be added.
### MapMaker.py
On the bottom of the file you will see ``` makeMap("samples/forest.png",'forestMap') ```. Change them to the path to the image, and the desired filename respectively. You will then run the script and if all goes well your map will be in the output directory. :)
Here it is in action!
![pre](/images/pre.PNG)
![post](/images/post.PNG)
