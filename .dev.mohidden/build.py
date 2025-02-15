import os
import shutil
import time

buildPath = ".build.mohidden"
projectPath = ".build.mohidden/project"
buildTime = time.time()
buildName = "DynamicMusic-MME_Telvanni-" +str(int(buildTime))

os.chdir("..")

if os.path.isdir(buildPath):
  shutil.rmtree(buildPath)

os.makedirs(buildPath)
os.makedirs(projectPath)

shutil.copytree("scripts", projectPath +"/scripts")
shutil.make_archive(buildPath +"/" +buildName, 'zip', projectPath)
