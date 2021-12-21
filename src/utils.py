from pathlib import Path
import logging
import logging.handlers
import pygame

debug = True

# répertoires utiles du jeu ----------------------
#
#  racine (répertoire d'installation)
#     | - src
#     | - images
#     | - log
ROOT_DIR = Path(__file__).parent.parent
IMAGES_DIR = ROOT_DIR.joinpath("images")
LOGS_DIR = ROOT_DIR.joinpath("log")

# log ---------------------------------------------
# format du log
FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT)
# création du log
log = logging.getLogger("project-march")
# log au niveau debug (affiche et enregistre tous les messages)
if debug:
    log.setLevel(logging.DEBUG)
else:
    log.setLevel(logging.info)
# stockage aussi dans une fichier (garde les 10 derniers fichiers
file_handler = logging.handlers.RotatingFileHandler(LOGS_DIR.joinpath("project-march.log"), mode="a",
                                                    backupCount=10, maxBytes=30000)
log.addHandler(file_handler)


# fonctions --------------------------------------
def load_image(filename):
    """load_image: loads an image from the image directory"""
    log.debug(f"loading image: {filename}")
    return pygame.image.load(str(IMAGES_DIR.joinpath(filename)))