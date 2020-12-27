import subprocess
import os, re
from termcolor import colored
from colorama import init
init()  # to make coloring works on windows
from DataLoader import DataLoader

## THIS CLASS IS USED AS FOR CHECKING ONLY
class NameViewer(DataLoader):
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

    @staticmethod
    def listAlbumsWithArtistName(root):
        """ Prints all Albums that contain Artist name in a different color. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if artist in album:
                    print(colored(os.path.join(artist, album) + "\t<--- ALBUM CONTAINS ARTIST NAME", "red"))
                else:
                    print(os.path.join(artist, album))

    @staticmethod
    def listAlbumsWhoseAllSongsContainArtistName(root):
        """ Prints all Songs that contain Artist name in a different color. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if all(artist in song for song in os.listdir(os.path.join(root, artist, album))):
                    print(colored(os.path.join(artist, album) + "\t<--- ALL SONGS CONTAIN ARTIST NAME", "red"))
                    for song in os.listdir(os.path.join(root, artist, album)):
                        print("\t" + colored(os.path.join(artist, song), "red"))
                else:
                    print(os.path.join(artist, album))

    @staticmethod
    def listAlbumsWhoseAllSongsContainAlbumName(root):
        """ Prints all Albums that have songs containing Album name in each song title. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if all(album in song for song in os.listdir(os.path.join(root, artist, album))):
                    print(colored(os.path.join(artist, album) + "\t<--- ALL SONGS CONTAIN ALBUM NAME", "red"))
                    for song in os.listdir(os.path.join(root, artist, album)):
                        print("\t" + colored(os.path.join(artist, song), "red"))
                else:
                    print(os.path.join(artist, album))

    @staticmethod
    def listAlbumsWithSongsMatchingBroadcastRegex(root) -> set:
        """ If albums have all songs with proper naming convention, they are printed green.
        They are ready to be moved out as DONE.

        Broadcast naming convention: 01 artist name -- album name -- song name.ext
        """

        for artist in os.listdir(os.path.join(root)):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if all(NameViewer.broadcastRegexPattern.match(song) for song in os.listdir(os.path.join(root, artist, album))):
                    print(colored(os.path.join(root, artist, album), "green"))
                else:
                    print(os.path.join(root, artist, album))

    @staticmethod
    def listAlbumsWithSongsMatchingBasicRegex(root):
        """ If albums have all songs with basic naming convention, they are printed green.
        They are ready to be renamed to broadcast naming convention.

        Basic naming convention: 01 song name.ext
        Broadcast naming convention: 01 artist name -- album name -- song name.ext
        """

        for artist in os.listdir(os.path.join(root)):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if all(NameViewer.basicRegexPattern.match(song) for song in os.listdir(os.path.join(root, artist, album))):
                    print(colored(os.path.join(root, artist, album), "green"))
                else:
                    print(os.path.join(root, artist, album) + " <--- NOT MATCHING BASIC REGEX")
                    for song in os.listdir(os.path.join(root, artist, album)):
                        print(f"\t {song}")





if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\__Atma__Test"
    # NameViewer.listAlbumsWhoseAllSongsContainArtistName(root)
    # NameViewer.listAlbumsWhoseAllSongsContainAlbumName(root)
    NameViewer.listAlbumsWithSongsMatchingBasicRegex(root)
