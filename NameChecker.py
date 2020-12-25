
import os, re
from termcolor import colored
from colorama import init
init()  # to make coloring works on windows

## THIS CLASS IS USED AS THIRD
class NameChecker:
    """ Class validating Artist, Albums and Song names.
        At this point, the form of Artist name should be plain Artist Name (eg. Steve Roach)
        At this point, the form of Album should be:
        1] plain Album Name (eg. Early Man)
        2] Album Name - Artist Name (eg. Steve Roach - Early Man)

        This class is responsible for checking each album is in proper folder and has proper string.
        Folder name called Steve Roach - Early Man has to be in directory Steve Roach
    """

    @staticmethod
    def listAllArtist(root):
        """ Print all Artist folders to the console. """
        for artist in os.listdir(root):
            if os.path.isdir(os.path.join(root, artist)):
                print(artist)
            else:
                print(colored(artist, "red"))

    @staticmethod
    def listAllAlbums(root):
        """ Print all Albums folders to the console. Albums should be at second level, if at this level is file, it will be printed in red. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if os.path.isdir(os.path.join(root, artist, album)):
                    print(album)
                else:
                    print(colored(album, "red"))

    @staticmethod
    def listAllSongs(root):
        """ Print all Songs to the console. Songs should be at third level, if at this level is album (directory), it will be printed in red. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                for song in os.listdir(os.path.join(root, artist, album)):
                    if os.path.isdir(os.path.join(root, artist, album, song)):
                        print(colored(song, "red"))
                    else:
                        print(song)


if __name__ == "__main__":
    root = r"E:\__ATMA__TEST"
    NameChecker.listAllArtist(root)