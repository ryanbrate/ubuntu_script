"""
    small script to add/remove software or run commands with a fresh ubuntu/ debian install

    Example:
        $python3 ubuntu_script.py
"""

import os

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
        #  add ~/bin to path
        "mkdir /home/$USER/bin",
        'echo export PATH="/home/$USER/bin:$PATH" >>  ~/.bashrc',
        #
        # python-related
        "python3 -m spacy download en",
        #
        # symbolic links
        # nautilus scripts
        "ln -s ~/bin/vimdiff.py ~/.local/share/nautilus/scripts",
        # application launchers
        "ln -s ~/bin/application_launchers/Jupyter\ Lab.desktop ~/.local/share/applications/Jupyter\ Lab.desktop",
        "ln -s ~/bin/application_launchers/Jupyter\ Notebook.desktop ~/.local/share/applications/Jupyter\ Notebook.desktop",
        # jupyter-gvim integration
        "ln -s ~/bin/open_vim_in_jupyter.py ~/.ipython/profile_default/startup/open_vim_in_jupyter.py",
    ],
]

apt = [
    # TO INSTALL
    [
        # "snapd",
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
        # "octave",
        # "pdf-arranger",
        # "vlc",
        # "gnome-tweaks",
        "cmake",
        # "golang",
        "python3-pip",
        "r-base-core",
        "exuberant-ctags",
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
        "jupyter",
        "jupyterlab",
        "pynvim",
        # "jedi-language-server",
        "python-language-server[all]",
    ],
    # TO REMOVE
    [],
]


def main():

    pass
    for hello in commands[0]:
        try:
            os.system(hello)
        except:
            pass

    # install apt packages
    for package in apt[0]:
        try:
            os.system("sudo apt install --yes " + package)
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
    for hello in commands[1]:
        try:
            os.system(hello)
        except:
            pass


if __name__ == "__main__":
    main()
