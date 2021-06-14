import re
import discord
import numpy as np
from cairosvg import svg2png


class PangoPic:
    def __init__(self):
        self.hex_regex = re.compile("^[0-9a-fA-F]{6}")
        with open("utils/pango-logo.svg", "rb") as f:
            self.pangoSVG = f.read().decode("utf-8")
        self.pango_color = str(self.pangoSVG).find("#FF6B00;}")
        self.pango_bg = str(self.pangoSVG).find("opacity:0.6; fill:#FFFFFF;}")
        self.pangoSVG = list(self.pangoSVG)


    def str2hex(self, new_color):
        if new_color.replace(" ", "").replace(",", "") == "":  # handles empty messages
            raise ValueError
        if new_color[0] == "#" and self.hex_regex.match(new_color[1:]) is not None and len(
                new_color) == 7:  # handles the "#XXXXXX" hex colours
            new_color = new_color[1:]
        elif " " in new_color or "," in new_color:
            if " " in new_color and "," in new_color:  # handles the "R,        G,    B" colours
                new_color = new_color.replace(" ", "")
            elif "," in new_color:  # handles the "R,G,B" colours
                new_color = np.array(new_color.split(","), dtype=int)
            elif " " in new_color:  # handles the "R G B" colours
                new_color = np.array(new_color.split(" "), dtype=int)
            if isinstance(new_color, np.ndarray) and len(new_color) == 3 and np.any(new_color >= 0) and np.any(
                    new_color <= 255):
                new_color = "%02x%02x%02x" % tuple(new_color)
            else:
                raise ValueError
        if self.hex_regex.match(new_color) is not None and len(new_color) == 6:
            return new_color
        raise ValueError

    def do_profile_picture(self, msg):
        try:
            colors = msg.split(" ")
            if len(colors) == 6:  # R G B and R G B
                colors = (",".join(colors[:3]), ",".join(colors[3:]))
            elif len(colors) == 2:  # Hexa/Hexa or R,G,B/R,G,B or Hexa/R,G,B or R,G,B/Hexa
                colors = (colors[0], colors[1])
            elif len(colors) == 4:
                if len(colors[0]) >= 6:  # Hexa/R G B
                    colors = (colors[0], ",".join(colors[1:]))
                elif len(colors[3]) >= 6:  # R G B/Hexa
                    colors = (",".join(colors[:3]), colors[3])
            elif len(colors) == 3: #R G B
                colors = (",".join(colors[:3]),)
            elif len(colors) == 1: #Hexa
                colors = colors
            else:
                raise ValueError
            self.pangoSVG[self.pango_color + 1: self.pango_color + 7] = self.str2hex(colors[0])
            if len(colors) == 2:
                self.pangoSVG[self.pango_bg: self.pango_bg + 25] = "opacity:1.0; fill:#{}".format(self.str2hex(colors[1]))
            else:
                self.pangoSVG[self.pango_bg: self.pango_bg + 25] = "opacity:0.6; fill:#FFFFFF"
            svg2png("".join(self.pangoSVG), write_to="utils/pango-logo.png")
            return "Here is your personalized profile picture!", discord.File("utils/pango-logo.png")
        except:
            raise ValueError