import re, os, shutil
from termcolor import colored
from colorama import init
init()  # to make coloring works on windows

class SongNameChecker:
    """ Class responsible for check the song pattern match
        eg: 01 Edward Ka-Spel -- The Minus Touch -- The Beast With 6 Fingers.flac

        if I have album with this, move it away as done.
    """

    ext = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.dct', '.dss',
           '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.mp3', '.mpc', '.msv', '.nmf',
           '.nsf', '.ogg', '.oga', '.mogg', '.opus', '.ra', '.rm', '.raw', '.sln', '.tta', '.voc', '.vox', '.wav',
           '.wma', '.wv', '.webm', '.8svx']

    # REGEX PATTERNS
    # one CD leading zero: 01 Edward Ka-Spel -- The Minus Touch -- The Beast With 6 Fingers.flac
    pattern = re.compile(r"(^\d\d)(\s)([\w+\s().,:#=\-`&'?!\[\]]*)(\s)(--)(\s)([\w+\s().,:#=\-`&'?!\[\]]*)(\s)(--)(\s)([\w+\s().,:#=\-`&'?!\[\]]*)$")

    @staticmethod
    def showAlbumsWithProperSongNames(root) -> set:
        """ If albums have all songs with proper naming convention, they are printed green.
            Naming convention: 01 Artist -- Album -- Song.ext
        """
        for artist in os.listdir(os.path.join(root)):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if all(SongNameChecker.pattern.match(song) for song in os.listdir(os.path.join(root, artist, album))):
                    print(colored(os.path.join(root, artist, album), "green"))
                else:
                    print(os.path.join(root, artist, album))

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
                if all(SongNameChecker.pattern.match(song) for song in os.listdir(os.path.join(root, artist, album))):
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
    SongNameChecker.moveAlbumsWithProperSongNames(root)