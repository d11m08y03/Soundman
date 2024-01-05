import os

def readfile(filename: str) -> list[str]:
    file = open(filename, "r")
    details = []

    for line in file:
        details.append(line.strip())

    file.close()

    return details

def soundman(url: str, artist: str, track: str, album: str) -> None:
    if os.path.exists(os.path.join("~/Music/", f"\'{album}\'/")):
        print("Album directory exists.")
    else:
        print(f"Created directory ~/Music/{album}")
        os.system(f"mkdir ~/Music/\'{album}\'")

    outputFile = f"~/Music/\'{album}\'/\'{track}.mp3\'"
    os.system(f"yt-dlp -x --audio-format mp3 {url} -o {outputFile}")

    if album.lower() != "null":
        os.system(f"id3v2 -a \'{artist}\' -A \'{album}\' {outputFile}")
    else:
        os.system(f"id3v2 -a \'{artist}\' {outputFile}")

def main() -> None:
    details = readfile("./input.txt")

    for i in range(0, len(details) - 3, 4):
        url = details[i]
        artist = details[i + 1]
        track = details[i + 2]
        album = details[i + 3]

        soundman(url, artist, track, album)

if __name__ == "__main__":
    main()
