import qrcode
import qrcode.image.svg
import argparse
import datetime
from os import getcwd
from os.path import join, basename
import pathlib

def create_qr_code(data, output=None, method='basic'):
    # define a method to choose which factory metho to use
    # possible values 'basic' 'fragment' 'path'
    method = "basic"

    data = "Some text that you want to store in the qrcode"

    if method == 'basic':
    # Simple factory, just a set of rects.
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
    # Fragment factory (also just a set of rects)
        factory = qrcode.image.svg.SvgFragmentImage
    elif method == 'path':
    # Combined path factory, fixes white space that may occur when zooming
        factory = qrcode.image.svg.SvgPathImage

    # Set data to qrcode
    img = qrcode.make(data, image_factory = factory)

    # no output save image w/ datetime to where this program is called from
    if output is None:
        output = join(getcwd(), datetime.datetime.now().isoformat() + '.svg')
    # only a file name is supplied but not a full path
    elif output and basename(output) == output:
        output = join(getcwd(), output)
    else:
        output = output
        # Save svg file somewhere
        img.save(output)