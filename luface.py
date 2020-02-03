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
        print("Loading Image: {}".format(ipath))

        # Load Image as Numpy array from disk
        self.image = cv2.imread(ipath)

        # Convert image to black and white
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        print("Image Loaded: {}".format(ipath))

    def detect_faces(self, display=False):
        """"Returns array of coordinates where a face may be"""

        print("Detecting Faces in: {}".format(self.ipath))
        
        # Get Cascade path from command line options
        cascade_path = self.opts['--model']
        print(cascade_path)
        print("Loading Facial Cascade Classifier:", cascade_path)

        # Load Haar Cascade to Detect Faces
        self.cascade = cv2.CascadeClassifier(cascade_path)

        # Get Min size from command line options
        min_size = int(self.opts['--min-size'])
        print(min_size)

        # Run cascade detection
        faces = self.cascade.detectMultiScale(
            self.gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(min_size, min_size)
        )

        print("Found {} faces.".format(len(faces)))
        print(faces)

        # If display option is True, show image with faces identified
        if display:
            for (x, y, w, h) in faces:

                # Draw a green rectangle
                cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # cv2.imshow("Detection Results", self.image)
            # cv2.waitKey(0)

            # Display Image
            plt.imshow(self.image)
            plt.show()


if __name__ == "__main__":

    # Parse command line options with docopt
    options = docopt.docopt(USAGE)

    # Instantiate facial recognition class
    facerec = FacialRecognizer(options)

    # Load and Image to analyze
    facerec.load_image(options['<image>'])

    # Get faces in image
    faces = facerec.detect_faces(display=True)