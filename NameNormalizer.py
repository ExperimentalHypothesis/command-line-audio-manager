import os, argparse, re, shutil


##  THIS CLASS IS USED FIRST
class NameNormalizer:
    """
    Class responsible for normalizing names for artist folders, album folders and song files.

    Artist name is normalized if it has only name of artist (eg. Steve Roach) or if it has name of album separated with - (eg. Steve Roach - Early Man)
    Album name is normalized if it has only name of album (eg. Early Man) or if it has name of artist separated with - (eg. Steve Roach - Early Man)
    Song name is normalized if it has number and name of song with extension (eg. 01 - Hey You.mp3)

    The goal of this class is to clean out all the additional chars, spaces numbers, abbreviations etc. that are often part of the name.

    Normalization of names if the first step in processing.

    It is done using CLI interface so that it is simpler and faster then manual renaming on filesystem.
    """

    @staticmethod
    def stripToken(token, *args):
        """ Strip specified token from a filepath. """
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].replace(token, " "))
        if src == dst:
            return
        print(f"Stripping {token} from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def stripReg(regex, *args) -> None:
        """ Strip regex expression from a filepath. """
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], re.sub(regex, " ", args[-1]))
        if src == dst:
            return
        print(f"Striping Regex {regex} from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def lowercase(*args):
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].lower())
        if src == dst:
            return
        print(f"Lowercasing from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def uppercase(*args):
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].upper())
        if src == dst:
            return
        print(f"Uppercasing from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def titlecase(*args):
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].title())
        if src == dst:
            return
        print(f"Titlecasing from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def stripWhitespace(*args):
        """ Strip additional whitespaces. """
        filename = args[-1]
        src = os.path.join(*args)
        hasExtraWhitespace = filename[0] == " " or filename[-1] == " " or "  " in filename

        if hasExtraWhitespace:
            filename = re.sub(r"[\s]+", " ", filename)
            dst = os.path.join(*args[0:-1], filename.strip())
            print(f"Stripping extra whitespace from {src} -> {dst}")
            try:
                os.rename(src, dst)
            except FileExistsError as e:
                print(e)
                print("removing duplicates")
                shutil.rmtree(src)







if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\OneDrive - EP Commodities, a.s\Plocha\testing folder"
    NameNormalizer.stripArtistFromAlbum(root)
