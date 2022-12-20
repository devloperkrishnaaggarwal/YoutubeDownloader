from pytube import YouTube, Playlist
import os


# Download audio of a playlist
def downloadPlaylistAudio(link):
    youtubePlaylist = Playlist(
        "https://www.youtube.com/playlist?list=PLH_3DEgkVOfsyso9b_fvjtgST9inA5aVf")
    for video in youtubePlaylist.videos:
        video.streams.get_audio_only().download()

    print("Success!")

# Download video with audio of a playlist


def downloadPlaylistVideo(link):
    youtubePlaylist = Playlist(link)
    formatOfVideo = input(
        'In Which format you want to download:\n360p\n720p\n1080p\n Type your format: ')

    if formatOfVideo.startswith('360') and (formatOfVideo.endswith('p') or ('0')):
        for video in youtubePlaylist.videos:
            video.streams.get_by_itag(18).download()
    elif formatOfVideo.startswith('720') and (formatOfVideo.endswith('p') or ('0')):
        for video in youtubePlaylist.videos:
            video.streams.get_by_itag(22).download()
    elif formatOfVideo.startswith('1080') and (formatOfVideo.endswith('p') or ('0')):
        for video in youtubePlaylist.videos:
            video.streams.get_by_itag(137).download()
    else:
        print('Please enter the correct input.')

    print("Success!")

# Download audio of a video


def downloadAudio(link, name):
    youtubeVideo = YouTube(link)

    youtubeVideo.streams.get_audio_only().download(output_path=os.path.abspath(
        'E:\\code\\pythonp\\projects\\Serious projects\\1 youtube downloader'), filename=f"{name}.mp3")
    print("Success!")

# Download video and audio of a video


def downloadVideo(link, name):
    youtubeVideo = YouTube(link)
    formatOfVideo = input(
        'In Which format you want to download:\n360p\n720p\n1080p\n Type your format: ')
    if formatOfVideo.startswith('360') and (formatOfVideo.endswith('p') or ('0')):
        youtubeVideo.streams.get_by_itag(18).download(output_path=os.path.abspath(
            'E:\\code\\pythonp\\projects\\Serious projects\\1 youtube downloader'), filename=f"{name}.mp4")
    elif formatOfVideo.startswith('720') and (formatOfVideo.endswith('p') or ('0')):
        youtubeVideo.streams.get_by_itag(22).download(output_path=os.path.abspath(
            'E:\\code\\pythonp\\projects\\Serious projects\\1 youtube downloader'), filename=f"{name}.mp4")
    elif formatOfVideo.startswith('1080') and (formatOfVideo.endswith('p') or ('0')):
        youtubeVideo.streams.get_by_itag(137).download(output_path=os.path.abspath(
            'E:\\code\\pythonp\\projects\\Serious projects\\1 youtube downloader'), filename=f"{name}.mp4")
    else:
        print('Please enter the correct input.')

    print("Success!")


if __name__ == "__main__":
    enteringInp = input(
        "Do you want to download a single video or a playlist\nIf you want single video then press 1 \nIf you want a playlist then press 2\n")
    if enteringInp == '1':
        secondInp = input(
            "Do you want it in audio only or video with audio \nWrite audio for audio only\n write video for video with audio\nType what you want: ")

        if secondInp == 'audio':
            linkInp = input('Link of the video: ')
            nameInp = input('what name do you want for the audio: ')
            downloadAudio(linkInp, nameInp)
        elif secondInp == "video":
            linkInp = input('Link of the video: ')
            nameInp = input('what name do you want for the video: ')
            downloadVideo(linkInp, nameInp)
    elif enteringInp == '2':
        secondInp = input(
            "Do you want it in audio only or video with audio \nWrite audio for audio only\n write video for video with audio\nType what you want: ")
        if secondInp == 'audio':
            linkInp = input('Link of the playlist: ')

            downloadPlaylistAudio(linkInp)
        elif secondInp == "video":
            linkInp = input('Link of the playlist: ')

            downloadPlaylistVideo(linkInp)
        else:
            print("Please enter correctly...")
    else:
        print("Please type correct number..")


