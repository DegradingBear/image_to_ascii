# image_to_ascii
Tkinter gui that converts a given image into ascii text based on a grey scale mapping to 'darkness' of ascii character.
To run, run the 'img_to_ascii_gui.py' file in terminal.

|Paramter| effect|
|---|---|
|image path| path (relative to python file location) of image to be converted|
|character width|(optional) how many ascii characters WIDE the string should be (height is scaled accordingly by original aspect ratio of image|
|vertical scale|(optional) scale factor to scale image vertically as converting to ascii can often warp this axis (because characters arent perfect squares|
|ascii_map (dark to light)|(optional) allows you to define a custom character string to convert into, provide characters in order of how 'dark' they are. ie "#" covers much more area than "." so it should go later on (its 'brighter')|
|row starter|(optional) prepend any sequence of characters to the start of each line (useful to add images as comments in code!)|
|path to save text|(optional) the file path (again relative to the python file) to save the text file to. if left blank text will not be saved, only displayed in gui window|
|font size|(optional)font size of the characters in the popup window|
