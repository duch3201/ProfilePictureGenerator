# SVG Profile Picture Generator

This code generates SVG profile pictures with random background and avatar colors. It utilizes the generate_profile_picture() function to create SVG code and save it to a file with a random name and the .svg extension.

## Description:

The SVG Profile Picture Generator is a Python code snippet that allows you to generate SVG profile pictures with random background and avatar colors. It uses the generate_profile_picture() function, which creates an SVG code with random colors and saves it to a file with a random name and the .svg extension.

The generated profile pictures can be used in web applications, user profiles, or any other scenario where random profile pictures are needed. The code is easily customizable, allowing you to adjust the color generation logic or incorporate it into your existing Flask, HTML, or JavaScript-based projects.


## Usage
Generate a random profile picture using the generate_profile_picture() function:

```py
    import pfpGen
    profile_picture_filepath = pfpGen.generate_profile_picture(svgOutputPath)
```
The function takes svgOutputPath generates an SVG profile picture, saves it to a file in the specified directory, and returns the filepath of the saved SVG file.

## Info:

    Version: 1.0.0
    Author: Duch3201 (Chris)
    License: GNU General Public License v3.0



## Disclaimer:

This code snippet is provided as-is without any warranties. Use it at your own risk.

Please make sure to update the documentation and info section with your own details, such as your name as the author and the chosen license for your code.

Remember to provide proper attribution for any third-party code or dependencies used in your project.
