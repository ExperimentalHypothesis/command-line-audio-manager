import argparse
import NameNormalizer


class ArgParser:
    """ Class responsible for parsing command line args. """

    @staticmethod
    def _parseArgs():
        """ Prepare the parse args. """
        parser = argparse.ArgumentParser()

        parser.add_argument("-lcar", "--lowercaseartist", action="store_true")
        parser.add_argument("-lcal", "--lowercasealbum", action="store_true")
        # parser.add_argument("-lcso", "--lowercasesong", action="store_true")
        parser.add_argument("-ucar", "--uppercaseartist", action="store_true")
        parser.add_argument("-ucal", "--uppercasealbum", action="store_true")
        # parser.add_argument("-ucso", "--uppercasesong", action="store_true")
        parser.add_argument("-tcar", "--titlecaseartist", action="store_true")
        parser.add_argument("-tcal", "--titlecasealbum", action="store_true")
        # parser.add_argument("tcso", "--titlecasesong", action="store_true")
        parser.add_argument("-rnar", "--striptokenfromartist", action="store_true")
        parser.add_argument("-rnal", "--striptokenfromalbum", action="store_true")
        parser.add_argument("-rnso", "--striptokenfromsong", action="store_true")
        parser.add_argument("-rgxar", "--stripregexfromartist", action="store_true")
        parser.add_argument("-rgxal", "--stripregexfromalbum", action="store_true")
        parser.add_argument("-rgxso", "--stripregexfromsong", action="store_true")
        parser.add_argument("-T", "--token", type=str, required=False)
        parser.add_argument("-R", "--root", type=str, required=True)
        return parser.parse_args()

    @staticmethod
    def run():
        """ Run function based on CLI arguments input. """
        args = ArgParser._parseArgs()

        if args.striptokenfromartist:
            NameNormalizer.NameNormalizer.stripTokenFromArtistName(args.token, args.root)
        elif args.striptokenfromalbum:
            NameNormalizer.NameNormalizer.stripTokenFromAlbumName(args.token, args.root)
        elif args.striptokenfromsong:
            NameNormalizer.NameNormalizer.stripTokenFromSongName(args.token, args.root)
        elif args.stripregexfromartist:
            NameNormalizer.NameNormalizer.stripRegFromArtistName(args.token, args.root)
        elif args.stripregexfromalbum:
            NameNormalizer.NameNormalizer.stripRegFromAlbumName(args.token, args.root)
        elif args.stripregexfromsong:
            NameNormalizer.NameNormalizer.stripRegFromSongName(args.token, args.root)
        elif args.lowercaseartist:
            NameNormalizer.NameNormalizer.lowercaseArtist(args.root)
        elif args.lowercasealbum:
            NameNormalizer.NameNormalizer.lowercaseAlbum(args.root)
        # elif args.lowercasesong:
        #     NameNormalizer.NameNormalizer.lowercaseSong()
        elif args.uppercaseartist:
            NameNormalizer.NameNormalizer.uppercaseArtist(args.root)
        elif args.uppercasealbum:
            NameNormalizer.NameNormalizer.uppercaseAlbum(args.root)
        # elif args.uppercasesong:
        #     NameNormalizer.NameNormalizer.uppercaseSong()
        elif args.titlecaseartist:
            NameNormalizer.NameNormalizer.titlecaseArtist(args.root)
        elif args.titlecasealbum:
            NameNormalizer.NameNormalizer.titlecaseAlbum(args.root)
        # elif args.titlecasesong:
        #     NameNormalizer.NameNormalizer.titlecaseSong(args.root)



# if __name__ == "__main__":
#     print("hello")
#     ArgParser.runCommands()