import os, argparse, re

class NameNormalizer:

    # def __init__(self, root:str):
    #     """ Specify the root path """
    #     self.root = root

    # def __str__(self):
    #     return f"NameNormalizer - {self.root}"

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
        dst = os.path.join(*args[0:1], re.sub(regex, " ", args[-1]))
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
    def _titlecase(*args):
        src = os.path.join(*args)
        dst = os.path.join(*args[0:-1], args[-1].title())
        if src == dst:
            return
        print(f"Titlecasing from {src} -> {dst}")
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







# if __name__ == "__main__":
#     runCommands()
