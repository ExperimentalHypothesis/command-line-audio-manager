import argparse
import NameNormalizer

class ArgParser:
    """ Class reponsible for parsing command line args. """

    def _parseArgs():
        """ Prepare the parse args. """
        parser = argparse.ArgumentParser()

        parser.add_argument("-strar", "--striptokenfromartist", action="store_true")
        parser.add_argument("-stral", "--striptokenfromalbum", action="store_true")
        parser.add_argument("-strso", "--striptokenfromsong", action="store_true")
        parser.add_argument("-T", "--token", type=str, required=True)
        parser.add_argument("-R", "--root", type=str, required=True)
        
        return parser.parse_args()

    def run():
        """ Run function based on CLI arguments input. """
        args = ArgParser._parseArgs()

        if args.striptokenfromartist:
            NameNormalizer.NameNormalizer.stripTokenFromArtistName(args.token, args.root)
        elif args.striptokenfromalbum:
            NameNormalizer.NameNormalizer.stripTokenFromAlbumName(args.token, args.root)
        elif args.striptokenfromsong:
            NameNormalizer.NameNormalizer.stripTokenFromSongName(args.token, args.root)
        
# if __name__ == "__main__":
#     print("hello")
#     ArgParser.runCommands()