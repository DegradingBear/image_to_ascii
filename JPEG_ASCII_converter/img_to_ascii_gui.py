import tkinter as tk
import Ascii_Image_Converter as ascii_2_im
from os import getcwd


class ascii_converter_gui():
    def __init__(self):
        #initialise converter
        self.converter = ascii_2_im.image_to_ascii()
        self.converter.scale_height(0.4)
        self.converter.ascii_map(ascii_2_im.MESSAGES_ASCII_MAP)
        #setup window
        self.window = tk.Tk()
        self.window.title("image to ascii converter")


        #generalised field dictionary
        self.inputs = {}
        inputs_to_add = [
            ("image_path", "image path: "),
            ("character_width", "character width: "),
            ("vert_scale", "vertical scale, y in [0,1]: "),
            ("ascii_map", "ascii map string (dark to light): "),
            ("row_start", "row starter: "),
            ("save_path", "path to save text: "),
            ("font", "font size (this will increase width): ")
        ]

        #add each input, done this way for easy of adding inputs
        for input_field in inputs_to_add:
            wrapper = tk.Frame(self.window)
            text_input = tk.Text(wrapper, height=1, width=30)
            self.inputs[input_field[0]] = text_input
            text_input.pack(side=tk.RIGHT)

            label = tk.Label(wrapper, text=input_field[1])
            label.pack(side=tk.LEFT)

            wrapper.pack()

        #any extra inputs that arent boiler plate
        invert_frame = tk.Frame(self.window)
        self._invert = tk.IntVar()
        invert_check = tk.Checkbutton(invert_frame, variable=self._invert)
        invert_check.pack(side=tk.RIGHT)
        invert_label = tk.Label(invert_frame, text="invert colour: ")
        invert_label.pack(side=tk.LEFT)
        invert_frame.pack()

        #widget to execute  function
        run_converter_button = tk.Button(self.window, text="[ convert ]", command = self.convert)
        run_converter_button.pack()


    def convert(self):

        input_getter = lambda k: self.inputs[k].get("1.0", "end-1c")
        #get image path field
        image_path = input_getter("image_path")

        #get character width field
        character_width = input_getter("character_width")
        if character_width.isdigit():
            self.converter.image_width(int(character_width))

        #get vertical_scale field
        vertical_scale = input_getter("vert_scale")
        if vertical_scale.replace(".","").isnumeric():
            vertical_scale = float(vertical_scale)
        else:
            vertical_scale = False
        self.converter.scale_height(float(vertical_scale))

        #get ascii map field
        ascii_map = input_getter("ascii_map")
        if ascii_map:
            self.converter.ascii_map(ascii_map)
        else:
            self.converter.ascii_map(ascii_2_im.TERMINAL_ASCII_MAP) #default

        #line prefix
        line_starter = input_getter("row_start")
        if line_starter:
            self.converter.row_beginner(line_starter)

        #get the save path
        save_path = input_getter("save_path")
        path_to_save = None
        if save_path:
            if not save_path.endswith(".txt"):
                save_path += ".txt"
            path_to_save = save_path

        #font size
        font_size = input_getter("font")
        font_to_set = 10 #default
        if font_size.isdigit():
            font_to_set = int(font_size)


        invert = self._invert.get()

        result = self.converter.image_to_ascii(image_path, text_file_path=path_to_save, invert=bool(invert))
        if not result:
            self.error_popup("invalid image file path")
            return

        response_window = tk.Toplevel(self.window)
        response_window.title("result")
        tk.Label(response_window, text=result, font=("Courier", font_to_set)).pack(side=tk.LEFT)


    def run(self):
        self.window.mainloop()

    def error_popup(self, message:str):
        error_window = tk.Toplevel(self.window)
        error_window.geometry("200x50")
        error_window.title("ERROR")
        tk.Label(error_window, text=message, font=("aerial bold",20)).pack(anchor=tk.CENTER, expand=True)


if __name__ == "__main__":
    convert_gui = ascii_converter_gui()
    convert_gui.run()