import os, shutil


##  THIS CLASS IS USED SECOND
class Sorter:
    """ Class responsible for sorting folders in root.
        There are several scenarios:
        1] the folder in root is Album and artist name can be parsed from the Album name (eg. "Steve Roach - Early Man"), it that case this folder will be moved to "Steve Roach" folder
        2] the folder in root is Album and artist name can not be parsed from the Album name (eg. "Early Man"). In this case, it will be moved to ! UNKNOWN ALBUMS !
        3] the folder in root is Artist folder, nothing is done
    """

    @staticmethod
    def sortArtistFolders(root):
        """ Sort artist folders. """
        mp = Sorter._mapArtistPathToArtist(root)
        Sorter._createArtistFolders(root, mp)

    @staticmethod
    def _mapArtistPathToArtist(root) -> dict:
        """
        This method will iterate over a directory and return map
        where key is the name of the artist and values is the path to the album.

        If the folder is an artist folder (having subdirectory), it will be skipped
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
                    print(folderPath + " is album")
                    Sorter._moveFoldersToUnknown(folderPath)
                except FileExistsError as e:
                    print(e)
        return mp

    @staticmethod
    def _moveFoldersToUnknown(folderPath) -> None:
        """ Move folders whose artist name cannot be parsed to unknown. """
        head, tail = os.path.split(folderPath)  # C:\Users\lukas.kotatko\OneDrive - EP Commodities, a.s\Plocha\testing folder              Nomenclature
        folderName = "! UNKNOWN ALBUMS - UNABLE TO PARSE ARTIST NAMES !"
        unknownFolderPath = os.path.join(head, folderName)
        try:
            os.mkdir(unknownFolderPath)
        except FileExistsError as e:
            print("folder " + unknownFolderPath + " exists, not creating..") # uz existuje:
        shutil.move(folderPath, unknownFolderPath)


    @staticmethod
    def _createArtistFolders(root, map: dict):
        """ This method will create folders based on artist names. """
        for folderPath, artistName in map.items():
            try:
                os.mkdir(os.path.join(root, artistName))
            except FileExistsError as e:
                print("folder " + os.path.join(root, artistName) + " exists, not creating..")  # uz existuje
            for artist in map.keys():
                try:
                    shutil.move(folderPath, os.path.join(root, artistName))
                except shutil.Error as e:
                    print(e)




if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\OneDrive - EP Commodities, a.s\Plocha\testing folder"

    pp = r"C:\Users\lukas.kotatko\Music\michael stearns"
    ppp = r"C:\Users\lukas.kotatko\Music\(033) Jason van Wyk - Attachment - eilean [75] (2016) CD"
    #
    # Sorter.sortArtistFolders(root)
    res  = Sorter._mapArtistPathToArtist(root)
