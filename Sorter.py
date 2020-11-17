import os, shutil


class Sorter:
    """ Class responsible for sorting folders. """

    @staticmethod
    def sortArtistFolders(root):
        """ Sort artist folders. """
        mp = Sorter._mapArtistPathToArtist(root)
        Sorter._createArtistFolders(root, mp)

    @staticmethod
    def _mapArtistPathToArtist(root) -> dict:
        """
        Map artist path artist.
        This method will return map where key is the name of the artist and values is the path to the album.
        """
        mp = {}
        for folder in os.listdir(root):
            if not os.path.isdir(os.path.join(root, folder)):
                continue
            isAlbum = all(os.path.isfile(os.path.join(root, folder, file)) for file in os.listdir(os.path.join(root, folder)))
            if isAlbum:
                try:
                    artistName = folder.split(" - ")[0]
                    folderPath = os.path.join(root, folder)
                    mp[folderPath] = artistName
                except FileExistsError as e:
                    print(e)
        return mp

    @staticmethod
    def _createArtistFolders(root, map: dict):
        """ Create artist folders. """
        for folderPath, artistName in map.items():
            try:
                print("making " + os.path.join(root, artistName))
                os.mkdir(os.path.join(root, artistName))
            except Exception as e:
                print(e)  # uz existuje
            for artist in map.keys():
                try:
                    shutil.move(folderPath, os.path.join(root, artistName))
                except shutil.Error as e:
                    print(e)




if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\Music"

    pp = r"C:\Users\lukas.kotatko\Music\michael stearns"
    ppp = r"C:\Users\lukas.kotatko\Music\(033) Jason van Wyk - Attachment - eilean [75] (2016) CD"
    #
    # Sorter.sortArtistFolders(root)
    print(Sorter.sortArtistFolders(root))
