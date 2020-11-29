
import os, re

## THIS CLASS IS USED AS THIRD
class Checker:
    """ Class validating Artist and ALbums names.
        At this point, the form of Artist name should be plain Artist Name (eg. Steve Roach)
        At this point, the form of Album should be:
        1] plain Album Name (eg. Early Man)
        2] Album Name - Artist Name (eg. Steve Roach - Early Man)

        This class is responsible for checking each album is in proper folder and has proper string.
        Folder name called Steve Roach - Early Man has to be in directory Steve Roach
    """

    @staticmethod
    def validateArtistNames(root):
        """ Check the names. """
        for artist in os.listdir(root):
            pass
