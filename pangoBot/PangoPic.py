import colorsys
import re
import discord
import numpy as np
from cairosvg import svg2png


class PangoPic:
    def __init__(self):
        self.hex_regex = re.compile("^[0-9a-fA-F]{6}")
        with open("utils/pango-logo.svg", "rb") as f:
            self.pangoSVG = f.read().decode("utf-8")
        index, self.colorToIndex = 0, {}
        while 1:
            index = self.pangoSVG.find("#", index + 1)
            if index == -1:
                break
            if not self.hex_regex.match(self.pangoSVG[index + 1: index + 7]):
                continue
            col = self.pangoSVG[index + 1:index + 7]
            if col not in self.colorToIndex:
                self.colorToIndex[col] = [index + 1]
            else:
                self.colorToIndex[col].append(index + 1)
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
            color = msg.split(" ")
            if len(color) == 3: #R G B
                color = (",".join(color[:3]),)
            elif len(color) == 1: #Hexa
                color = color
            else:
                raise ValueError
            if "random" in color:
                for idc in self.colorToIndex.values():
                    for i in idc:
                        self.pangoSVG[i: i + 6] = '%02X%02X%02X' % tuple(np.random.randint(0, 255, 3))
            else:
                rgb_new_color = self.hex_to_rgb(self.str2hex(color[0]))
                hsv_new_color = colorsys.rgb_to_hsv(rgb_new_color[0], rgb_new_color[1], rgb_new_color[2])

                for color, idc in self.colorToIndex.items():
                    color = self.hex_to_rgb(color)
                    hsv = colorsys.rgb_to_hsv(color[0], color[1], color[2])
                    rgb = colorsys.hsv_to_rgb(hsv_new_color[0], hsv_new_color[1] * hsv[1], hsv_new_color[2] * hsv[2] / 255)
                    for i in idc:
                        self.pangoSVG[i: i + 6] = '%02X%02X%02X' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))
            svg2png("".join(self.pangoSVG), write_to="utils/pango-logo.png")
            return "Here is your personalized profile picture!", discord.File("utils/pango-logo.png")
        except:
            raise ValueError

    def hex_to_rgb(self, value):
        if "0x" in value:
            value = str(value)[2:]
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))