import os

from NameNormalizer import NameNormalizer


class SongNameNormalizer(NameNormalizer):
    """ Class handling everything concerning song renaming. """

    @staticmethod
    def stripToken(token, root) -> None:
        """ Deletes a specified token or string from all songs names """
        for path, dirs, folders in os.walk(root):
            for file in folders:
                NameNormalizer.stripToken(token, path, file)

    @staticmethod
    def stripReg(regex, root) -> None:
        """ Deletes string that matches regex expression form song name. """
        for path, dirs, folders in os.walk(root):
            for file in folders:
                NameNormalizer.stripReg(regex, path, file)

    @staticmethod
    def lowercase(root) -> None:
        """ Make song name lowercase. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                for song in os.listdir(os.path.join(root, artist, album)):
                    if song != song.lower():
                        NameNormalizer.lowercase(root, artist, album, song)

    def uppercase(root) -> None:
        """ Make song name uppercase. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                for song in os.listdir(os.path.join(root, artist, album)):
                    if song != song.upper():
                        NameNormalizer.uppercase(root, artist, album, song)

    def title(root) -> None:
        """ Make song name uppercase. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                for song in os.listdir(os.path.join(root, artist, album)):
                    if song != song.title():
                        NameNormalizer.titlecase(root, artist, album, song)