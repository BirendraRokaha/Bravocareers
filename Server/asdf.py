import os,os.path,shutil


#Change current working directory to Downloads
os.chdir('/Users/Birendra Rokaha/Downloads')

'''
def mkDir(dirName):
    os.mkdir(dirName)
'''
#list of extensions
doc =( ".doc",".docx",".txt",".pdf",".rtf",".csv")
ppt =( ".ppt", ".pptx")
img =(".jpg",".jpeg",".png",".svg")
'''
# my old way of doing 
sourcePath='/Users/Birendra Rokaha/Downloads'
files = [f for f in os.listdir('.') if os.path.isfile(f)]
sourcefiles = os.listdir(sourcePath)
for file in files:
    if file.endswith(tuple(ppt)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/PowerPoint'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    elif file.endswith(tuple(doc)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Documents'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    elif file.endswith(tuple(img)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Images'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    elif file.endswith('.exe'):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Applications'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    else:
        destinationPath = '/Users/Birendra Rokaha/Downloads/Others'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
'''


## way of doing 

# Setting destination directories
def get_destination(f):
    destinationPath = os.getcwd()
    if f.endswith(tuple(ppt)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/PowerPoint'
    elif f.endswith(tuple(doc)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Documents'
    elif f.endswith(tuple(img)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Images'
    elif f.endswith('.exe'):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Applications'
    else:
        destinationPath = '/Users/Birendra Rokaha/Downloads/Others'
    return destinationPath
# setting sourcepath and listing all the files form sourcepath
sourcePath= os.getcwd()
sourcefiles = os.listdir(sourcePath)

# Assigning dir according to the file extensions and transfering
for file in sourcefiles:
    before = os.path.join(sourcePath, file)
    if not os.path.isfile(before):
        continue 
    dPaths = get_destination(file)
    after = os.path.join(dPaths, file)
    shutil.move(before, after)
