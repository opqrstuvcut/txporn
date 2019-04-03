#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import unicodedata
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageColor import getrgb

DPI = (100, 100)


def count_char(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in ["F", "W", "A"]:
            count += 1
        else:
            count += .5
    return count


def parse_argument():
    parser = argparse.ArgumentParser("txporn", add_help=True)
    parser.add_argument("--text", "-t", help="input text", type=str)
    parser.add_argument("--font", "-f", help="font name or font file path", type=str, default="Meiryo")
    parser.add_argument("--font_size", "-s", help="font size", type=int, default=20)
    parser.add_argument("--color", "-c", help="text color(color name or color code, e.g. #ffffff)", default="black")
    parser.add_argument("--text_transparency", "-a", help="text transparency (0 ~ 1)", type=float, default=0)
    parser.add_argument("--output_dir_path", "-o", help="output dirctory path", type=str, default="./")
    args = parser.parse_args()
    return args


def main():
    args = parse_argument()

    length = count_char(args.text)
    fontsize = args.font_size
    width_p = int(fontsize / 72. * DPI[0] * length)
    height_p = int(fontsize / 72. * DPI[1])
    color_rgba = getrgb(args.color) + (int((1. - args.text_transparency) * 255),)

    # write text
    img = Image.new('RGBA', (width_p, height_p), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font=args.font, size=fontsize)
    draw.text((0, 0), args.text, font=font, fill=color_rgba)

    # remove margin
    crop = img.split()[-1].getbbox()
    img = img.crop(crop)

    # make directory
    dir_path = args.output_dir_path
    if dir_path:
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)

    output_path = os.path.join(dir_path, args.text + ".png")
    img.save(output_path, dpi=DPI)


if __name__ == '__main__':
    main()
