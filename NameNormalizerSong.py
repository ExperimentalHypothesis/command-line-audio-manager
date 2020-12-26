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
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                for song in os.listdir(os.path.join(root, artist, album)):
                    if song != song.lower():
                        NameNormalizer.lowercase(root, artist, album, song)

    @staticmethod
    def uppercase(root) -> None:
        """ Make song name uppercase. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                for song in os.listdir(os.path.join(root, artist, album)):
                    if song != song.upper():
                        NameNormalizer.uppercase(root, artist, album, song)

    @staticmethod
    def titlecase(root) -> None:
        """ Make song name titlecase. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                for song in os.listdir(os.path.join(root, artist, album)):
                    song_name, ext = os.path.splitext(os.path.join(root, artist, album, song))
                    if song != os.path.basename(song_name.title() + ext):
                        src_name = os.path.join(root, artist, album, song)
                        dst_name = os.path.join(root, artist, album, song_name.title() + ext)
                        print(f"Titlecasing from {src_name} -> {dst_name}")
                        os.rename(src_name, dst_name)

    @staticmethod
    def stripWhitespace(root):
        """ Strips additional (multiple) whitespace from all albums. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                for song in os.listdir(os.path.join(root, artist, album)):
                    NameNormalizer.stripWhitespace(root, artist, album, song)

    @staticmethod
    def stripArtistNameFromSong(root):
        """ Removes artist name from song name in albums where ALL songs contain artist name. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer.stripStringFromAlbumsSong(artist, root, artist, album)

    @staticmethod
    def stripAlbumNameFromSong(root):
        """ Removes artist name from song name in albums where ALL songs contain artist name. """
        for artist in os.listdir(root):
            if not os.path.isdir(os.path.join(root, artist)):
                continue
            for album in os.listdir(os.path.join(root, artist)):
                if not os.path.isdir(os.path.join(root, artist, album)):
                    continue
                NameNormalizer.stripStringFromAlbumsSong(album, root, artist, album)





if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\__Atma__Test"

    SongNameNormalizer.stripAlbumNameFromSong(root)