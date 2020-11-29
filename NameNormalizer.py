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
    def _stripToken(token, *args):
        """ Strip specified token from a filepath. """
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].replace(token, " "))
        if src == dst:
            return
        print(f"Stripping {token} from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def stripTokenFromArtistName(token, root) -> None:
        """ Deletes a specified token from all artist folder names. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            NameNormalizer._stripToken(token, root, artist)

    @staticmethod
    def stripTokenFromAlbumName(token, root) -> None:
        """ Deletes a specified token from all artist folder names. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer._stripToken(token, root, artist, album)

    @staticmethod
    def stripTokenFromSongName(token, root) -> None:
        """ Deletes a specified token or string from all songs names """
        for path, dirs, folders in os.walk(root):
            for file in folders:
                NameNormalizer._stripToken(token, path, file)

    @staticmethod
    def _stripReg(regex, *args) -> None:
        """ Strip regex expression from a filepath. """
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], re.sub(regex, " ", args[-1]))
        if src == dst:
            return
        print(f"Striping Regex {regex} from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def stripRegFromArtistName(regex, root) -> None:
        """ Deletes string that matches regex expression form artist name. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            NameNormalizer._stripReg(regex, root, artist)

    @staticmethod
    def stripRegFromAlbumName(regex, root) -> None:
        """ Deletes string that matches regex expression form album name. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer._stripReg(regex, root, artist, album)

    @staticmethod
    def stripRegFromSongName(regex, root) -> None:
        """ Deletes string that matches regex expression form song name. """
        for path, dirs, folders in os.walk(root):
            for file in folders:
                NameNormalizer._stripReg(regex, path, file)

    @staticmethod
    def _lowercase(*args):
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].lower())
        if src == dst:
            return
        print(f"Lowercasing from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def _uppercase(*args):
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].upper())
        if src == dst:
            return
        print(f"Uppercasing from {src} -> {dst}")
        os.rename(src, dst)

    @staticmethod
    def lowercaseArtist(root):
        """ Lowercase all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            if artist != artist.lower():
                NameNormalizer._lowercase(root, artist)

    @staticmethod
    def uppercaseArtist(root):
        """ Uppercase all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            if artist != artist.upper():
                NameNormalizer._uppercase(root, artist)

    @staticmethod
    def titlecaseArtist(root):
        """ Titlecase all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            if artist != artist.title():
                NameNormalizer._titlecase(root, artist)

    @staticmethod
    def lowercaseAlbum(root):
        """ Lowercase all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if album != album.lower():
                    NameNormalizer._lowercase(root, artist, album)

    @staticmethod
    def uppercaseAlbum(root):
        """ Uppercase all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if album != album.upper():
                    NameNormalizer._uppercase(root, artist, album)

    @staticmethod
    def titlecaseAlbum(root):
        """ Titlecase all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if album != album.title():
                    NameNormalizer._titlecase(root, artist, album)

    @staticmethod
    def stripWhitespaceFromArtist(root):
        """ Strips additional (multiple) whitespace from all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            NameNormalizer._stripWhitespace(root, artist)

    @staticmethod
    def stripWhitespaceFromAlbum(root):
        """ Strips additional (multiple) whitespace from all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer._stripWhitespace(root, artist, album)

    @staticmethod
    def _stripWhitespace(*args):
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


    @staticmethod
    def _titlecase(*args):
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].title())
        if src == dst:
            return
        print(f"Titlecasing from {src} -> {dst}")
        os.rename(src, dst)


    @staticmethod
    def stripArtistFromAlbum(root):
        """
        Strip artist name from album name.
        Some name have this format Steve Roach - Early Man.
        This Function has to make it so that Steve Roach - Early Man becomes Early Man
        """

        for artist in os.listdir(root):
            for album in os.listdir(os.path.join(root, artist)):
                if artist in album and " - " in album:
                    src = os.path.join(root, artist, album)
                    dst = os.path.join(root, artist, album.replace(artist + " - ", ""))
                    print("striping artist from " + album + " -> " + album.replace(artist + " - ", ""))
                    os.rename(src, dst)


if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\OneDrive - EP Commodities, a.s\Plocha\testing folder"

    NameNormalizer.stripArtistFromAlbum(root)
