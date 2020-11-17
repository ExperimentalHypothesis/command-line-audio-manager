import os


class FolderBuilder:
    """ Class responsible for creating new folders for albums/artist/songs. """

    @staticmethod
    def checkIfAlbum(root):
        """ Check if current folder is artist or album. """
        for folder in os.listdir(root):
            if not os.path.isdir(os.path.join(root, folder)):
                continue
            if FolderBuilder._isAlbum(os.path.join(root, folder)):
                print(os.path.join(root, folder) + " contains only files -> is Album folder")  # DEBUG
                artist = FolderBuilder._extractArtistName(folder)
                if not os.path.exists(os.path.join(root, artist)):
                    print("mkdir slozky " + os.path.join(root, artist))
                    os.mkdir(os.path.join(root, artist)) # // vytvor tu slozku s nazvem autora


                # // presun tuhle ze ktery si to extrahoval tam do tyhle
            else:
                print(os.path.join(root, folder) + " contains at least one dir -> is Artist folder")  # DEBUG

    @staticmethod
    def _extractArtistName(inputName):
        """
        Extract artist name from a folder name:
        eg: folder name is Mathias Grassow - Ambient Signum -> artist name is Mathias Grassow
        all the folders name should have one - separating artistName from albumName
        """
        artist, album = inputName.split(" - ")
        return artist


    @staticmethod
    def _isAlbum(inputPath):
        """ Check if it is album. """
        return all(os.path.isfile(os.path.join(inputPath, i)) for i in os.listdir(inputPath))
        #     print(inputPath + " contains only files -> is Album folder")
        #     return True
        # else:
        #     print(inputPath + " contains at least one dir -> is Artist folder")
        #     return False



if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\Music"

    pp = r"C:\Users\lukas.kotatko\Music\michael stearns"
    ppp = r"C:\Users\lukas.kotatko\Music\(033) Jason van Wyk - Attachment - eilean [75] (2016) CD"

    FolderBuilder.checkIfAlbum(root)
