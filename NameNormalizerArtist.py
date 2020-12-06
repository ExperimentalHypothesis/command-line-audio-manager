import os

from NameNormalizer import NameNormalizer


class ArtistNameNormalizer(NameNormalizer):
    """ Class handling everything concerning artist folders renaming. """

    @staticmethod
    def stripToken(token, root) -> None:
        """ Deletes a specified token from all artist folder names. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            NameNormalizer.stripToken(token, root, artist)

    @staticmethod
    def stripReg(regex, root) -> None:
        """ Deletes string that matches regex expression form artist name. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            NameNormalizer.stripReg(regex, root, artist)

    @staticmethod
    def stripWhitespace(root):
        """ Strips additional (multiple) whitespace from all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            NameNormalizer.stripWhitespace(root, artist)

    @staticmethod
    def lowercase(root):
        """ Lowercase all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            if artist != artist.lower():
                NameNormalizer.lowercase(root, artist)

    @staticmethod
    def uppercase(root):
        """ Uppercase all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            if artist != artist.upper():
                NameNormalizer.uppercase(root, artist)

    @staticmethod
    def titlecase(root):
        """ Titlecase all artists. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            if artist != artist.title():
                NameNormalizer.titlecase(root, artist)


