import os
from DataLoader import DataLoader


class Deleter(DataLoader):
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

    @staticmethod
    def deleteNonAudioFiles(root):
        """ Prints all Songs that contain artist name in a different color. """
        for paths, dirs, folders in os.walk(root):
            for file in folders:
                if not file.endswith(tuple(Deleter.audioExtensions)):
                    print(f"removing {os.path.join(paths, file)}")
                    os.remove(os.path.join(paths, file))


if __name__ == "__main__":
    root = r"E:\__ATMA__TEST"

    Deleter.deleteNonAudioFiles(root)