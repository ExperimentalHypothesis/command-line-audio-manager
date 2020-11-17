import os


class Deleter:
    """ Class responsible for deleting files and folders. """

    @staticmethod
    def deleteFoldersWithoutAudio(root):
        """ Delete folders where no audio files are left. """
        pass

    @staticmethod
    def deleteEmptyFolders(root):
        """ Delete folder where no files are left. """
        for folder in os.listdir(root):
            if os.path.isdir(os.path.join(root, folder)) and not os.listdir(os.path.join(root, folder)):
                print(f"Removing empty dir {os.path.join(root, folder)}")
                os.rmdir(os.path.join(root, folder))


if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\Music"

    Deleter.deleteEmptyFolders(root)