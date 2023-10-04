from pytube import YouTube
from tqdm import tqdm

link = input("Please Provide Your link: ")

yt = YouTube(link)
print("Video Title:", yt.title)

videos = yt.streams.filter(progressive=True)
vid = list(enumerate(videos))
for i, stream in vid:
    print(f"{i}: {stream}")

strm = int(input("Please Provide the index of the stream you want to download: "))

video_stream = videos[strm]

# Get the video size for the progress bar
video_size = video_stream.filesize

# Download the video with a loading bar
with tqdm(total=video_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
    video_stream.download(output_path="downloads", filename=yt.title)
    pbar.update(video_size)

print("Successful download...!!")
