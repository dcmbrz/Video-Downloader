from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt= YouTube(url)
        streams= yt.streams.filter(progress= True, file_extension='mp4')
        hightest_res_stream= streams.get_highest_resolution()
        hightest_res_stream.download(output_path=save_path)
    except Exception as e:
        print(e)
        

def open_file_dialog():
    folder= filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')




if __name__ == '__main__':
    root= tk.Tk()
    root.withdraw()
    
    video_url= input('Please enter a YouTube url: ')
    save_dir= open_file_dialog()
    
    if save_dir:
        print('Download in progress...')
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")