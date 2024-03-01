# First install Python on your PC, open your online or offline IDE, and run this command("pip install sketchpy") in Terminal.
# Type the path of the jpg image in the second line of code and run this code.


from sketchpy import canvas
myObject = canvas.sketch_from_image("Path of jpg image which is saved in your PC")
myObject.draw()