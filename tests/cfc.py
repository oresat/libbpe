"""simple program to convert raw cfc images to viewable file types"""

import argparse
import os

import cv2
import numpy as np


def cfc(infile: str, columns: int, rows: int):
    """main cfc function"""

    path = os.path.split(infile)
    appnd = path[1]
    newpath = os.path.split(path[0])
    fout = newpath[0] + "/converted/" + appnd
    outfile = fout + ".png"

    with open(infile, "rb") as f:
        raw = f.read()
    data = np.frombuffer(raw, dtype=np.uint16).reshape(columns, rows)
    # reshape() parameters are for end image dimensions
    data = np.copy(data)
    # override with a copy that is mutable
    data //= 64
    # manipulate image for displaying - scale 14-bits to 8-bits
    data = data.astype(np.uint8)
    data = np.invert(data)
    # invert black/white values
    cv2.imwrite(outfile, data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("colmuns")
    parser.add_argument("rows")
    args = parser.parse_args()
    cfc(args.infile, args.columns, args.rows)
