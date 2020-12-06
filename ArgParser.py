import argparse
# import NameNormalizer
from NameNormalizerArtist import ArtistNameNormalizer

class ArgParser:
    """ Class responsible for parsing command line args. """

    @staticmethod
    def _parseArgs():
        """ Prepare the parse args. """
        parser = argparse.ArgumentParser()

        # renaming artists
        parser.add_argument("-arcl",    "--cleartokenfromartist", help="remove letter/word from artist, has to be used with -T flag where you specify the token", action="store_true")
        parser.add_argument("-arrgx",   "--clearregexfromartist", help="remove regex expression from artist, has to be used with -X flag where you specify the regex", action="store_true")
        parser.add_argument("-arws",    "--clearwhitespacefromartist", help="remove extra whitespace from artist", action="store_true")
        parser.add_argument("-arlc",    "--lowercaseartist", help="lowercase artist", action="store_true")
        parser.add_argument("-aruc",    "--uppercaseartist", help="uppercase artist", action="store_true")
        parser.add_argument("-artc",    "--titlecaseartist", help="titlecase artist", action="store_true")

        # renaming albums
        parser.add_argument("-alcl",    "--cleartokenfromalbum", action="store_true")
        parser.add_argument("-alrgx",   "--clearregexfromalbum", action="store_true")
        parser.add_argument("-alws",    "--clearwhitespacefromalbum", action="store_true")
        parser.add_argument("-altc",    "--titlecasealbum", action="store_true")
        parser.add_argument("-allc",    "--lowercasealbum", action="store_true")
        parser.add_argument("-aluc",    "--uppercasealbum", action="store_true")
        parser.add_argument("-alclar",  "--clearartistfromalbum", action="store_true")   # use after moving to folders

        # renaming songs
        parser.add_argument("-sorn",    "--cleartokenfromsong", action="store_true")
        parser.add_argument("-sorgx",   "--clearregexfromsong", action="store_true")
        parser.add_argument("-sosw",    "--stripwhitespacefromsong", action="store_true")
        parser.add_argument("-solc",    "--lowercasesong", action="store_true")
        parser.add_argument("-souc",    "--uppercasesong", action="store_true")
        parser.add_argument("-sotc",    "--titlecasesong", action="store_true")

        # general setters
        parser.add_argument("-R", "--root", type=str, required=True)
        parser.add_argument("-T", "--token", type=str, required=False)
        parser.add_argument("-X", "--regex", type=str, required=False)
        return parser.parse_args()

    @staticmethod
    def run():
        """ Run function based on CLI arguments input. """
        args = ArgParser._parseArgs()

        # renaming artists
        if args.cleartokenfromartist:
            ArtistNameNormalizer.stripToken(args.token, args.root)
        elif args.clearregexfromartist:
            ArtistNameNormalizer.stripReg(args.regex, args.root)
        elif args.clearwhitespacefromartist:
            ArtistNameNormalizer.stripWhitespace(args.root)
        elif args.lowercaseartist:
            ArtistNameNormalizer.lowercase(args.root)
        elif args.uppercaseartist:
            ArtistNameNormalizer.uppercase(args.root)
        elif args.titlecaseartist:
            ArtistNameNormalizer.titlecase(args.root)

        # renaming albums
        # elif args
        #
        #
        # elif args.striptokenfromalbum:
        #     NameNormalizer.NameNormalizer.stripTokenFromAlbumName(args.token, args.root)
        # elif args.striptokenfromsong:
        #     NameNormalizer.NameNormalizer.stripTokenFromSongName(args.token, args.root)
        # elif args.stripregexfromartist:
        #     NameNormalizer.NameNormalizer.stripRegFromArtistName(args.token, args.root)
        # elif args.stripregexfromalbum:
        #     NameNormalizer.NameNormalizer.stripRegFromAlbumName(args.token, args.root)
        # elif args.stripregexfromsong:
        #     NameNormalizer.NameNormalizer.stripRegFromSongName(args.token, args.root)
        # elif args.lowercaseartist:
        #     NameNormalizer.NameNormalizer.lowercaseArtist(args.root)
        # elif args.lowercasealbum:
        #     NameNormalizer.NameNormalizer.lowercaseAlbum(args.root)
        # # elif args.lowercasesong:
        # #     NameNormalizer.NameNormalizer.lowercaseSong()
        # elif args.uppercaseartist:
        #     NameNormalizer.NameNormalizer.uppercaseArtist(args.root)
        # elif args.uppercasealbum:
        #     NameNormalizer.NameNormalizer.uppercaseAlbum(args.root)
        # # elif args.uppercasesong:
        # #     NameNormalizer.NameNormalizer.uppercaseSong()
        # elif args.titlecaseartist:
        #     NameNormalizer.NameNormalizer.titlecaseArtist(args.root)
        # elif args.titlecasealbum:
        #     NameNormalizer.NameNormalizer.titlecaseAlbum(args.root)
        # # elif args.titlecasesong:
        # #     NameNormalizer.NameNormalizer.titlecaseSong(args.root)
        # elif args.stripwhitespacefromartist:
        #     NameNormalizer.NameNormalizer.stripWhitespaceFromArtist(args.root)
        # elif args.stripwhitespacefromalbum:
        #     NameNormalizer.NameNormalizer.stripWhitespaceFromAlbum(args.root)
        # elif args.stripartist:
        #     NameNormalizer.NameNormalizer.stripArtistFromAlbum(args.root)

#
#
# if __name__ == "__main__":
#     print("hello")
#     ArgParser.runCommands()