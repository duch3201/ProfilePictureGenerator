import os
import random
import string

def get_random_color():
    color = '%06x' % random.randint(0, 0xFFFFFF)
    return color

def generate_profile_picture(svgOutputPath):
    # Generate random background color
    bg_color = get_random_color()

    # Generate random avatar color
    avatar_color = get_random_color()

    # Create SVG code with random colors
    svg_code = f'''
    <svg width="60" height="61" viewBox="0 0 60 61" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g clip-path="url(#clip0_6_475)">
            <rect y="0.245117" width="60" height="60" rx="30" fill="white"/>
            <rect x="18" y="10.2451" width="24" height="24" rx="12" fill="#{avatar_color}"/>
            <rect x="-15" y="40.2451" width="90" height="90" rx="45" fill="#{avatar_color}"/>
        </g>
        <defs>
            <clipPath id="clip0_6_475">
                <rect y="0.245117" width="60" height="60" rx="30" fill="white"/>
            </clipPath>
        </defs>
    </svg>
    '''

    # Generate a random filename with .svg extension
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.svg'
    filepath = os.path.join(svgOutputPath, filename)  # Update the path to your desired save directory

    # Save the SVG code to a file
    with open(filepath, 'w') as file:
        file.write(svg_code)

    return filepath
