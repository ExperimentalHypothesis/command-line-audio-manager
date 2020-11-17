import os

class FolderBuilder:
    """ Class responsible for creating new folders for albums/artist/songs. """

    @staticmethod
    def checkIfAlbum(root):
        """ Check if current folder is artist or album. """
        for folder in os.listdir(root):
            if not os.path.isdir(os.path.join(root, folder)):
                continue
            FolderBuilder._isAlbum(os.path.join(root, folder)) # c:lukas/music/Jasonwanwyk--


    @staticmethod
    def _isAlbum(inputPath):
        """ Check if it is album. """
        if all(os.path.isfile(os.path.join(inputPath, i)) for i in os.listdir(inputPath)):
            print(inputPath + " contains only files -> is Album folder")
            return True
        else:
            print(inputPath + " contains at least one dir -> is Artist folder")
            return False



if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\Music"

    pp = r"C:\Users\lukas.kotatko\Music\michael stearns"
    ppp = r"C:\Users\lukas.kotatko\Music\(033) Jason van Wyk - Attachment - eilean [75] (2016) CD"


    FolderBuilder.checkIfAlbum(root)
