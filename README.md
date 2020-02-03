# lutec20202 - Facial Dection with OpenCV and Python
**Source Code for Liberty University Technology &amp; Engineering Club 2020 Club Meeting 2**

## Requirements

1. [Python3](#python-3)
2. [OpenCV Python](#opencv-python)
3. An IDE
    * VS Code
    * PyCharm
4. A Command Shell
    * PowerShell/cmd.exe on Windows
    * Terminal.app on Mac
    * Linux (You'll know what to use)
5. This Repository

## Navigation

* [Installation](#installation)

## Installation

We will be using python3 for this workshop. If you are still using python2, consider moving to python 3 because the Python Foundation has official discontinued support for python2 as of January, 2020

### Python 3

#### Windows:

1. Download python from [python.org](https://python.org)
2. Run installer
3. Be sure to **check** the `Add python to PATH` option

#### Mac:

1. Method 1: (Recomended) Install python3 with homebrew

    **Install homebrew** if you don't already have it.
    Homebrew is a package manager for MacOS much like apt or yum on linux systems.

    Visit [brew.sh](https://brew.sh)

    Paste the following into terminal. You may needs to provide your administrator password to complete the installation.

    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

    **Install Python 3**

    After homebrew is installed you can install python3 with the following command:

    ```
    brew install python3
    ```

2. Method 2: (Alternative) Install python3 with install

   This method is perfectly fine, but if you can get homebrew working, then future updates and development adventures will be much easier.

   Visit [python.org](https://python.org) and grab the MacOS installer

### Install OpenCV Python

We will be using opencv as our computer vision and facial recognition library.

**Prerequiste**: You must have `python` and `pip` installed first.

1. Open a command shell and if `pip` install installed, you can installed opencv for python with the following command:

    ```
    pip install opencv-python
    ```

    Something like the following should show (Powershell):

    ```Powershell
    PS C:\Users\grply> pip install opencv-python
    Collecting opencv-python
    Downloading https://files.pythonhosted.org/packages/c2/6b/f842e7bf62074d7e308c8ca66f9182acf996810c82bd7c63b584626480eb/opencv_python-4.2.0.32-cp38-cp38-win32.whl (24.2MB)
        |████████████████████████████████| 24.2MB 656kB/s
    Collecting numpy>=1.17.3 (from opencv-python)
    Downloading https://files.pythonhosted.org/packages/0e/c3/be53614c4e3490778050e1df48fd463837297d5dd402dae3b500f2050eba/numpy-1.18.1-cp38-cp38-win32.whl (10.8MB)
        |████████████████████████████████| 10.8MB 409kB/s
    Installing collected packages: numpy, opencv-python
    Successfully installed numpy-1.18.1 opencv-python-4.2.0.32
    ```

2. Verify Installation

    If all is working properly, you should be able to running the following with no errors:

    ```Powershell
    PS C:\Users\grply> python                                                                                               Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cv2
    >>> cv2.__version__
    '4.2.0'
    >>>    
    ```

    And you're all set!



