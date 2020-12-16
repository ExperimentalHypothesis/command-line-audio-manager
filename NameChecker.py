
import os, re
from termcolor import colored


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
            print(artist)

    @staticmethod
    def listAllAlbums(root):
        """ Print all Albums folders to the console. """
        for artist in os.listdir(root):
            for album in os.listdir(os.path.join(root, artist)):
                print(album)

    @staticmethod
    def listAllSongs(root):
        """ Print all Albums folders to the console. """
        for artist in os.listdir(root):
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                for song in os.listdir(os.path.join(root, artist, album)):
                    print(song)

    @staticmethod
    def prr():
        print(colored('hello', 'red'), colored('world', 'green'))



if __name__ == "__main__":
    NameChecker.prr()