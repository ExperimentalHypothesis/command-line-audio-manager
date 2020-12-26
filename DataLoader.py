import re


class DataLoader:
    """ This class provides data that need to be shared across multiple other classes. """

    audioExtensions = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.dct',
                       '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.mp3', '.mpc',
                       '.msv', '.nmf', '.nsf', '.ogg', '.oga', '.mogg', '.opus', '.ra', '.rm', '.raw', '.sln', '.tta', '.voc', '.vox',
                       '.wav', '.wma', '.wv', '.webm', '.8svx']

    broadcastRegexPattern = re.compile(r"(^\d\d)(\s)([\w+\s().,:#=\-`&'?!\[\]]*)(\s)(--)(\s)([\w+\s().,:#=\-`&'?!\[\]]*)(\s)(--)(\s)([\w+\s().,:#=\-`&'?!\[\]]*)$")