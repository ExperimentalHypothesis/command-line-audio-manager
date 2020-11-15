import os, argparse

import math

class NameNormalizer:
    
    # def __init__(self, root:str):
    #     """ Specify the root path """
    #     self.root = root

    # def __str__(self):
    #     return f"NameNormalizer - {self.root}"

    def _stripToken(token, *args):
        """ Strip specified token from a filepath. """
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].replace(token, " "))
        if src == dst:
            return 
        print(f"Stripping {token} from {src} -> {dst}")
        os.rename(src, dst)

    def stripTokenFromArtistName(token, root) -> None:
        """ Deletes a specified token from all artist folder names. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            NameNormalizer._stripToken(token, root, artist)

    def stripTokenFromAlbumName(token, root) -> None:
        """ Deletes a specified token from all artist folder names. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer._stripToken(token, root, artist, album)

    def stripTokenFromSongName(token, root) -> None:
        """ Deletes a specified token or string from all songs names """
        for path, dirs, folders in os.walk(root):
            for file in folders:
                NameNormalizer._stripToken(token, path, file)


# if __name__ == "__main__":
#     runCommands()




