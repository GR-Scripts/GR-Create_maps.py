# create_maps.py

---

## Overview

`create_maps.py` is a simple Python script to quickly create resource folders for **FiveM** projects. It generates folders with a custom name, each containing:
- A basic `fxmanifest.lua` file.
- An empty `stream` directory for your assets.

This is ideal for developers who need to set up multiple maps at once.

---

## Requirements

- **Python 3.x**
- **Visual Studio Code** (or any text editor/IDE).

---

## How to Use

1. **Open the Script in Visual Studio Code:**
   - Copy and paste this file into a new file in **Visual Studio Code**, e.g., `create_maps.py`.

2. **Customize the Settings:**
   At the bottom of the script, edit the following variables:

base_name = "Your map name" # Base name for the folders 
number_of_maps = 126 # Number of folders to create 
start_number = 1 # Start numbering from this value


3. **Run the Script:**
- Open a terminal in VS Code.
- Run the script using:

  ```
  python create_maps.py
  ```

4. **Check the Output:**
The script will create folders in the current directory (or a specified base path) with the following structure:

Your map name_1/ fxmanifest.lua stream/ 
Your map name_2/ fxmanifest.lua stream/ ...


After completion, you’ll see a message in the terminal, such as:

Done: Created 126 maps with the name 'Your map name_<number>'.


---

## Example Setup

To create 5 folders named `test_map_1` through `test_map_5`:

1. Update the script:

base_name = "test_map" 
number_of_maps = 5 
start_number = 1

2. Run the script, and the folders will appear in the current directory.

---

## Why Use This?

- **Save Time**: Quickly set up multiple resource folders without repetitive manual work.
- **Customizable**: Adjust folder names, counts, and starting numbers with ease.
- **Beginner-Friendly**: Simple script designed for ease of use in **Visual Studio Code**.

---

## Contributing

Have ideas for improvements or additional features? Feel free to open an issue or submit a pull request!

---

## License

This project is licensed under the **MIT License**. Check the `LICENSE` file for details.