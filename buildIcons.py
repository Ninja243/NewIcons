import os
import subprocess

for svg in os.listdir("SVGs"):
	subprocess.run(["convert", "-density", "384", "SVGs/"+svg, "-define", "icon:auto-resize", "ICOs/"+svg+".ico"])
