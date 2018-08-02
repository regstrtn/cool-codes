import os
import imageio


plotsDir = './plots/'
filelist = os.listdir(plotsDir)
print(filelist)

def makeGif(filelist):
	images = []
	for filename in filelist:
		images.append(imageio.imread(plotsDir+filename))
	imageio.mimsave("3danimation.gif", images, duration = 0.3)

makeGif(filelist)

