from pytube import YouTube
from tqdm import tqdm
import os

link = input("Please Provide Your link: ")

yt = YouTube(link)
print("Video Title:", yt.title)

videos = yt.streams.filter(progressive=True)
vid = list(enumerate(videos))
for i, stream in vid:
    print(f"{i}: {stream}")

strm = int(input("Please Provide the index of the stream you want to download: "))

video_stream = videos[strm]


video_size = video_stream.filesize


downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")


with tqdm(total=video_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
    video_stream.download(output_path=downloads_folder, filename=yt.title)
    pbar.update(video_size)

print(f"Successful download to {downloads_folder}")
