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
    print(f"saving output to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help="Enter text to QR'ize.")
    parser.add_argument('--output', '-o', type=str, default=None,
    help="Output full path or file name to save svg qr code as, if not supplied creates"
    " Timestamped svg file within the directory this utility is called from")
    parser.add_argument('--method', '-m', type=str, default='basic', 
    help='''Enter factory method to use to create qr code
     basic - simple factory, just a set of rects.
     fragment - fragment factory, also just a set of rects
     path - combined path factory, fixes white space that may occur when zooming''')
    args = parser.parse_args()

    create_qr_code(data=args.input, output=args.output, method=args.method)

