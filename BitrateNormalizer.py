import os, subprocess

class BitrateNormalizer:
    """ Class responsible for normalizing bitrate and audio formats. """

    CODEC = " [lame]"
    FOLDER_NAME_NORM = "! ATMA NAME NORMALIZATION DONE !"
    FOLDER_BITRATE_NORM = "! ATMA BITRATE NORMALIZATION DONE !"

    # TODO add other
    EXT_MP3 = "mp3"
    EXT_FLAC = "flac"
    EXT_WMA = "wma"

    @staticmethod
    def normalizeSongBitrate(root):
        """ Normalize song bitrate to 128k ."""
        parDir = os.path.join(root, os.pardir)

        try:
            os.mkdir(os.path.join(parDir, BitrateNormalizer.FOLDER_BITRATE_NORM))
        except FileExistsError as e:
            pass

        for paths, dirs, files in os.walk(root):
            for file in files:
                src = os.path.join(paths, file)
                if src.endswith(BitrateNormalizer.EXT_FLAC):
                    BitrateNormalizer._normalize(src, BitrateNormalizer.EXT_FLAC)
                elif src.endswith(BitrateNormalizer.EXT_MP3):
                    BitrateNormalizer._normalize(src, BitrateNormalizer.EXT_MP3)
                elif src.endswith(BitrateNormalizer.EXT_WMA):
                    BitrateNormalizer._normalize(src, BitrateNormalizer.EXT_WMA)

    @staticmethod
    def _normalize(inputPath: str, audioExtension: str):
        """ Convert all formats to mp3 and normalize its bitrate. """
        outputPath = inputPath[:inputPath.rfind(".")] + BitrateNormalizer.CODEC + inputPath[inputPath.rfind("."):]
        outputPath = outputPath.replace(BitrateNormalizer.FOLDER_NAME_NORM, BitrateNormalizer.FOLDER_BITRATE_NORM)
        outputPath = outputPath.replace(audioExtension, BitrateNormalizer.EXT_MP3)
        outputDirs = os.path.split(outputPath)[0]
        if not os.path.exists(outputDirs):
            os.makedirs(outputDirs)
        if not os.path.exists(outputPath):
            print(f"Encoding from {inputPath} to {outputPath}")
            subprocess.run(f'ffmpeg -i "{inputPath}" -metadata comment="ripped with lame @128k" -codec:a libmp3lame -b:a 128k -ar 44100 "{outputPath}"')


if __name__ == "__main__":
    root = r"C:\Users\lukas.kotatko\! ATMA NAME NORMALIZATION DONE !"
    # file = r"C:\Users\lukas.kotatko\! ATMA NAME NORMALIZATION DONE !\chyekk, china doll\01 edward ka-spel -- chyekk, china doll -- lines.flac"
    BitrateNormalizer.normalizeSongBitrate(root)

