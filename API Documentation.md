API documentation
List all the functions with an explanation of what each function does, the arguments of the function and what it returns.


1.Function:  def fileExists()
Explanation: define a function that checks whether the file exists or not and checks if the file name entered by the user is a valid file
Arguments: none
Output:runs the openCVWindow function if file can be opened. If file cannot, show message: 'File Error', 'This image path is invalid'


2.Function: def openCVWindow(img_path)
Explanation: opens, reads and resizes image file and runs specified function in response to the mouse click.
Arguments: img_file
Output: detects color

3.Function: def pixel_Location(event, x, y, flags, param) ; while
Explanation: locates exact pixel using color co-ordinate system; determines the color detected through x and y position and obtains color from Colors.csv. 
While: running a while loop that displays the updated name and RGB values for users click position on a coloured rectangle label
Arguments: flags, param
Output: pops out accurate color in text box as well as name of color and RGB value on top left corner of screen.

4.Function: def getColourName(R,G,B)
Explanation: Creates a function that retrieves the name of the colour from the database by looping through 'Colors.csv' 
by computing distance between each color accurately to choose the one with the smallest distance for color selection.
Arguments: R,G,B
Output: returns color name.




