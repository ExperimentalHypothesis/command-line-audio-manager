import os

from NameNormalizer import NameNormalizer


class AlbumNameNormalizer(NameNormalizer):
    """ Class handling everything concerning album folders renaming. """

    @staticmethod
    def stripToken(token, root) -> None:
        """ Deletes a specified token from all artist folder names. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer.stripToken(token, root, artist, album)

    @staticmethod
    def stripReg(regex, root) -> None:
        """ Deletes string that matches regex expression form album name. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer.stripReg(regex, root, artist, album)

    @staticmethod
    def stripWhitespace(root):
        """ Strips additional (multiple) whitespace from all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer.stripWhitespace(root, artist, album)

    @staticmethod
    def lowercase(root):
        """ Lowercase all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if album != album.lower():
                    NameNormalizer.lowercase(root, artist, album)

    @staticmethod
    def uppercase(root):
        """ Uppercase all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if album != album.upper():
                    NameNormalizer.uppercase(root, artist, album)

    @staticmethod
    def titlecase(root):
        """ Titlecase all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                if album != album.title():
                    NameNormalizer.titlecase(root, artist, album)

    @staticmethod
    def stripArtist(root):
        """
        Strip artist name from album name.
        Some name have this format Steve Roach - Early Man.
        This Function has to make it so that Steve Roach - Early Man becomes Early Man
        """
        for artist in os.listdir(root):
            for album in os.listdir(os.path.join(root, artist)):
                if artist in album:
                    src = os.path.join(root, artist, album)
                    dst = os.path.join(root, artist, album.replace(artist, ""))
                    print("striping artist from " + album + " -> " + album.replace(artist, ""))
                    os.rename(src, dst)