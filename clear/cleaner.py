import os, shutil
import glob
class clean :

    def cleanframes():
        filelist=glob.glob("gen/frames/*.jpg")
        for file in filelist:
          os.remove(file)
          
    def cleanVids():      
        filelist=glob.glob("gen/vids/*.mp4")
        for file in filelist:
          os.remove(file)
          
#if __name__ == '__main__':
#    clean().cleanVids()
