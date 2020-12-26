import os, shutil
from DataLoader import DataLoader
from termcolor import colored
from colorama import init
init()  # to make coloring works on windows


class Mover(DataLoader):
    """  Class responsible for moving files to another place.

    """
    @staticmethod
    def moveAlbumsWithProperSongNames(root) -> None:
        """ If albums have all songs with proper naming convention, they are moved to folder.
            Naming convention: 01 Artist -- Album -- Song.ext
        """
        for artist in os.listdir(os.path.join(root)):
            albumsDoneFolder = "! ATMA NAME NORMALIZATION DONE !"
            parDir = os.path.join(root, os.pardir)

            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if all(Mover.broadcastRegexPattern.match(song) for song in os.listdir(os.path.join(root, artist, album))):
                    src = os.path.join(root, artist, album)
                    dst = os.path.join(parDir, albumsDoneFolder, artist, album)
                    try:
                        os.mkdir(os.path.join(parDir, albumsDoneFolder))
                        print(f"moving {src} to {dst}")
                        shutil.move(src, dst)
                    except FileExistsError as e:
                        print(f"moving {src} to {dst}")
                        shutil.move(src, dst)



if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\__Atma__Test"
    Mover.listAlbumsWithSongsMatchingBasicRegex(root)