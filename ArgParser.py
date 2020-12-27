import argparse

from NameNormalizerArtist import ArtistNameNormalizer
from NameNormalizerAlbum import AlbumNameNormalizer
from NameNormalizerSong import SongNameNormalizer
from NameViewer import NameViewer
from FilesMover import Mover
from FilesDeleter import Deleter
from BitrateNormalizer import BitrateNormalizer

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
        parser.add_argument("-alcl",    "--cleartokenfromalbum", help="remove letter/word from album, has to be used with -T flag where you specify the token", action="store_true")
        parser.add_argument("-alrgx",   "--clearregexfromalbum", help="remove regex expression from album, has to be used with -X flag where you specify the regex", action="store_true")
        parser.add_argument("-alws",    "--clearwhitespacefromalbum", help="remove extra whitespace from album", action="store_true")
        parser.add_argument("-altc",    "--titlecasealbum",  help="titlecase album", action="store_true")
        parser.add_argument("-allc",    "--lowercasealbum", help="lowercase album", action="store_true")
        parser.add_argument("-aluc",    "--uppercasealbum", help="uppercase album", action="store_true")
        parser.add_argument("-alclar",  "--clearartistfromalbum", action="store_true")   # !!! use after moving to folders

        # renaming songs
        parser.add_argument("-socl",    "--cleartokenfromsong", action="store_true")
        parser.add_argument("-sorgx",   "--clearregexfromsong", action="store_true")
        parser.add_argument("-sows",    "--stripwhitespacefromsong", action="store_true")
        parser.add_argument("-solc",    "--lowercasesong", action="store_true")
        parser.add_argument("-souc",    "--uppercasesong", action="store_true")
        parser.add_argument("-sotc",    "--titlecasesong", action="store_true")

        # listing artists, albums, songs, checking naming conventions, marking them in color. this is for quick visual reference about current state
        parser.add_argument("-arls",    "--listartists", help="prints out artist folder to terminal, it prints out all files and folders what are in first level", action="store_true")
        parser.add_argument("-alls",    "--listalbums", help="prints out albums folder to terminal, it prints out all files and folders what are in second level", action="store_true")
        parser.add_argument("-sols",    "--listsongs", help="prints out songs folder to terminal, it prints out all files what are in third level", action="store_true")
        parser.add_argument("-aals",    "--listalbumswithartistname", help="albums that have artist name as part of its name will be printed in red", action="store_true")
        parser.add_argument("-alarls",  "--listalbumswithartistnameinallsongs", help="albums that have all songs which contain artist name are printed in red", action="store_true")
        parser.add_argument("-alalls",  "--listalbumswithalbumnameinallsongs", help="albums that have all songs which contain albums name are printed in red", action="store_true")
        parser.add_argument("-bargxls", "--listalbumsmatchbasicregex", help="all albums that have songs with proper naming convention [01 song name.ext] will printed green. These are ready to be renamed to broadcast.", action="store_true" )
        parser.add_argument("-brogxls", "--listalbumsmatchbroadcastregex", help="all albums that have songs with proper naming convention [01 artist name -- album name -- song name.ext] will printed green. These are ready to be moved away.", action="store_true" )

        # moving files
        parser.add_argument("-mval",     "--movealbums", help="all albums that have songs with proper naming convention [01 Artist -- Album -- Song.ext] will moved to special folder", action="store_true" )

        # deleting files from filesystem
        parser.add_argument("-deem",    "--deleteempty", help="deletes all folder where no files are left", action="store_true")
        parser.add_argument("-dewa",    "--deletewithoutaudio", help="delete folder without audio", action="store_true")
        parser.add_argument("-dena",    "--deletenonaudio", help="delete non audio files", action="store_true")

        # bitrate normalization for broadcast
        parser.add_argument("--norm"    "--normalizebitrate", help="normalizes bitrate for radio server [set up to 128k]", action="store_true")



        # general setters
        parser.add_argument("-R", "--root", type=str, required=True)
        parser.add_argument("-T", "--token", type=str, required=False)
        parser.add_argument("-X", "--regex", type=str, required=False)
        return parser.parse_args()

    @staticmethod
    def run():
        """ Run function based on CLI arguments input. """
        args = ArgParser._parseArgs()

        # renaming artist
        if args.cleartokenfromartist: ArtistNameNormalizer.stripToken(args.token, args.root)
        elif args.clearregexfromartist: ArtistNameNormalizer.stripReg(args.regex, args.root)
        elif args.clearwhitespacefromartist: ArtistNameNormalizer.stripWhitespace(args.root)
        elif args.lowercaseartist: ArtistNameNormalizer.lowercase(args.root)
        elif args.uppercaseartist: ArtistNameNormalizer.uppercase(args.root)
        elif args.titlecaseartist: ArtistNameNormalizer.titlecase(args.root)

        # renaming albums
        elif args.cleartokenfromalbum: AlbumNameNormalizer.stripToken(args.token, args.root)
        elif args.clearregexfromalbum: AlbumNameNormalizer.stripReg(args.regex, args.root)
        elif args.clearwhitespacefromalbum: AlbumNameNormalizer.stripWhitespace(args.root)
        elif args.titlecasealbum: AlbumNameNormalizer.titlecase(args.root)
        elif args.lowercasealbum: AlbumNameNormalizer.lowercase(args.root)
        elif args.uppercasealbum: AlbumNameNormalizer.uppercase(args.root)
        elif args.clearartistfromalbum: AlbumNameNormalizer.stripArtist(args.root)

        # renaming songs
        elif args.cleartokenfromsong: SongNameNormalizer.stripToken(args.token, args.root)
        elif args.clearregexfromsong: SongNameNormalizer.stripToken(args.token, args.root)
        elif args.stripwhitespacefromsong: SongNameNormalizer.stripWhitespace(args.root)
        elif args.lowercasesong: SongNameNormalizer.lowercase(args.root)
        elif args.uppercasesong: SongNameNormalizer.uppercase(args.root)
        elif args.titlecasesong: SongNameNormalizer.titlecase(args.root)

        # listing artists, albums, songs, checking naming conventions, marking them in color. this is for quick visual reference about current state
        elif args.listartists: NameViewer.listAllArtist(args.root)
        elif args.listalbums: NameViewer.listAllAlbums(args.root)
        elif args.listsongs: NameViewer.listAllSongs(args.root)
        elif args.listalbumswithartistname: NameViewer.listAlbumsWithArtistName(args.root)
        elif args.listalbumswithartistnameinallsongs: NameViewer.listAlbumsWhoseAllSongsContainArtistName(args.root)
        elif args.listalbumswithalbumnameinallsongs: NameViewer.listAlbumsWhoseAllSongsContainAlbumName(args.root)
        elif args.listalbumsmatchbasicregex: NameViewer.listAlbumsWithSongsMatchingBasicRegex(args.root)
        elif args.listalbumsmatchbroadcastregex: NameViewer.listAlbumsWithSongsMatchingBroadcastRegex(args.root)

        # moving files
        elif args.movealbums: Mover.moveAlbumsWithProperSongNames(args.root)

        # deleting some data
        elif args.deleteempty: Deleter.deleteEmptyFolders(args.root)
        elif args.deletewithoutaudio: Deleter.deleteFoldersWithoutAudio(args.root)
        elif args.deletenonaudio: Deleter.deleteNonAudioFiles(args.root)

        # bitrate normalization for broadcastin
        elif args.normalizebitrate: BitrateNormalizer.normalizeSongBitrate(args.root)
