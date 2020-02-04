import sys
import docopt
import cv2
import matplotlib.pyplot as plt

USAGE = """

LU TEC Facial Analyzer v1.0

Usage:
    luface.py <image> [--model=MODEL] [--min-size=MINSIZE]

Arguments:
    <image>     Path to image to analyze for faces

Options:
    --model=MODEL           Haar Cascade Model [Default: ./models/haarcascade_frontalface_default.xml]
    --min-size=MINSIZE      Min size in pixels of faces to detect [Default: 30]
"""

class FacialRecognizer(object):
    def __init__(self, options):

        # Control Options from command line
        self.opts = options

        # Class-wide variables
        self.ipath = ""
        self.cascade = None
        self.image = None
        self.gray = None

    def load_image(self, ipath):
        """Loads and image from disk"""

        # TODO: Load Image as Numpy array from disk

        # TODO: Convert image to black and white


    def detect_faces(self, display=False):
        """"Returns array of coordinates where a face may be"""

        print("Detecting Faces in: {}".format(self.ipath))
        
        # TODO: Get Cascade path from command line options


        # TODO: Load Haar Cascade to Detect Faces


        # TODO: Get Min size from command line options


        # TODO: Run cascade detection

        # TODO: If display option is True, show image with faces identified


                # TODO: Draw a green rectangle


            # TODO: Display Image



if __name__ == "__main__":

    # TODO: Parse command line options with docopt
    options = docopt.docopt(USAGE)

    # TODO: Instantiate Facial Recognizer


    # TODO: Load and Image to analyze


    # TODO: Get faces in image
