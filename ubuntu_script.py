"""
    small script to add/remove software or run commands with a fresh ubuntu/ debian install

    Example:
        $python3 ubuntu_script.py
"""

import os

import numpy as np
import wget

commands = [
    # COMMANDS TO RUN AT START OF SCRIPT
    ["sudo apt update", "sudo apt upgrade"],
    # COMMANDS TO RUN AT END OF SCRIPT
    [
        "sudo apt autoremove",
        #
        # associate jupyter nb with ipynb
        "python3 -m nbopen.install_xdg",
        #
        #  create local binary folder and add to path
        "mkdir /home/$USER/bin",
        'echo export PATH="/home/$USER/bin:$PATH" >>  ~/.bashrc',
        #
        # python-related
        "python3 -m spacy download en",
    ],
]

apt = [
    # TO INSTALL
    [
        "snapd",
        "git",
        "synaptic",
        "ubuntu_restricted_extras",
        "calibre",
        # "gdebi",
        "texstudio",
        "texlive-latex-recommended",
        "texlive-extra",
        "texlive-full",
        "python-pygments",
        "chktex",  # latex linter
        # "quodlibet",
        "keepassxc",
        "octave",
        "pdf-arranger",
        "vlc",
        "gnome-tweaks",
        "krita",
        "cmake",
        "golang",
    ],
    # TO REMOVE
    ["gnome-games", "gnome-calculator"],
]

snap = [
    # TO INSTALL
    [
        "snap-store",
        # "nvim --beta --classic",
        "zoom-client",
        "signal-desktop",
        "slack --classic",
        "pdfmixtool",
    ],
    # TO REMOVE
    [],
]

pip = [
    # TO INSTALL
    [
        "statsmodels",
        "torch",
        "Keras",
        "tqdm",
        "spacy",
        "Pygments",
        "pandas",
        "numpy",
        "nltk",
        "notebook",
        "nbopen",
        "seaborn",
        "flake8",
        "black",
        "pydocstyle",
        "sklearn",
        "unidecode",
        "pipenv",
        "ibm_db",
    ],
    # TO REMOVE
    [],
]


def main():

    pass
    for com in commands[0]:
        try:
            os.system(com)
        except:
            pass

    # install apt packages
    for package in apt[0]:
        try:
            os.system("sudo apt install " + package)
        except:
            pass

    # remove apt packages
    for package in apt[1]:
        try:
            os.system("sudo apt remove " + package)
        except:
            pass

    # install snap packages
    for package in snap[0]:
        try:
            os.system("sudo snap install " + package)
        except:
            pass

    # remove snap packages
    for package in snap[1]:
        try:
            os.system("sudo snap remove " + package)
        except:
            pass

    # install pip packages
    for package in pip[0]:
        try:
            os.system("pip3 install " + package)
        except:
            pass

    # install pip packages
    for package in pip[1]:
        try:
            os.system("pip3 remove " + package)
        except:
            pass

    # run misc commands
    for com in commands[1]:
        try:
            os.system(com)
        except:
            pass


if __name__ == "__main__":
    main()
