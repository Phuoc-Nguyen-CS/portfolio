import colorsys
import os
from django.conf import settings
from colorthief import ColorThief

def get_base_and_complementary_colors(icon_filename):
    # Get the path to your static directory
    icon_folder = os.path.join(settings.BASE_DIR, 'my_app', 'static', 'icons')
    
    # Get the full path of the icon
    icon_path = os.path.join(icon_folder, icon_filename)
    
    # Extract the dominant color from the icon
    color_thief = ColorThief(icon_path)
    dominant_color = color_thief.get_color(quality=1)
    
    # Calculate the complementary color (as before)
    def complementary_color(rgb):
        import colorsys
        r, g, b = [x / 255.0 for x in rgb]
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        h = (h + 0.5) % 1.0  # Add 180° to hue
        comp_r, comp_g, comp_b = colorsys.hsv_to_rgb(h, s, v)
        return tuple(int(x * 255) for x in (comp_r, comp_g, comp_b))

    def rgb_to_hex(rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    complementary = complementary_color(dominant_color)

    return {
        "base_color": rgb_to_hex(dominant_color),
        "complementary_color": rgb_to_hex(complementary),
    }

# Example usage
colors = get_base_and_complementary_colors('html.png')

# Calculate the opposite rgb value
def rgb_to_complementary(rgb):
    r, g, b = [x / 255.0 for x in rgb]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h = (h + 0.5) % 1.0 # 180 the hue
    comp_r, comp_g, comp_b = colorsys.hsv_to_rgb(h, s, v)
    return tuple(int(x * 255) for x in (comp_r, comp_g, comp_b))

