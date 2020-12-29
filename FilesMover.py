import os, shutil
from DataLoader import DataLoader
from termcolor import colored
from colorama import init
init()  # to make coloring works on windows


class Mover(DataLoader):
    """  Class responsible for moving files to another place."""

    @staticmethod
    def moveAlbumsWithSongsMatchingBroadcastRegex(root) -> None:
        """ If albums have all songs with proper naming convention, they are moved to folder.

            Naming convention: 01 Artist -- Album -- Song.ext
        """
        folderNameNorm = "! ATMA NAME NORMALIZATION DONE !"
        parDir = os.path.join(root, os.pardir)

        for artist in os.listdir(os.path.join(root)):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if all(Mover.broadcastRegexPattern.match(song) for song in os.listdir(os.path.join(root, artist, album))):
                    src = os.path.join(root, artist, album)
                    dst = os.path.join(parDir, folderNameNorm, artist, album)
                    try:
                        os.mkdir(os.path.join(parDir, folderNameNorm))
                        print(f"moving {src} to {dst}")
                        shutil.move(src, dst)
                    except FileExistsError as e:
                        print(f"moving {src} to {dst}")
                        shutil.move(src, dst)
