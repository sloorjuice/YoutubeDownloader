from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog
class Main():
    def __init__(self) -> None:
        root = tk.Tk()
        icon = tk.PhotoImage(file = 'icon.png')
        root.wm_iconphoto(False, icon)
        root.windowTitle = root.title("Youtube Downloader")
        root.geometry("400x100")
        
        self.URL_var=tk.StringVar()
        
        # creating a label for 
        # name using widget Label
        name_label = tk.Label(root, text = 'Enter Youtube URL', font=('calibre',10, 'bold'))
        
        # creating a entry for input
        # name using widget Entry
        URL_entry = tk.Entry(root,textvariable = self.URL_var, font=('calibre',10,'normal'))

        # creating a button using the widget 
        # Button that will call the submit function 
        sub_btn=tk.Button(root,text = 'Submit', command = self.submit)
        
        
        
        # placing the label and entry in
        # the required position using grid
        # method
        name_label.grid(row=0,column=0)
        URL_entry.grid(row=0,column=1)
        sub_btn.grid(row=1,column=1)
        
        # performing an infinite loop 
        # for the window to display
        root.mainloop()
        
    def submit(self):
        URL=self.URL_var.get()
        print("The URL is : " + URL)
        self.URL_var.set("")
        path = self.open_file_dialog()
        if path:
            print("Downloading video...")
            self.download_video(URL,path)
        else:
            print("Invalid save location.")

    def download_video(self,url, save_path):
        try:
            yt = YouTube(url)
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res_stream = streams.get_highest_resolution()
            highest_res_stream.download(output_path=save_path)
            print("Video Downloaded Successsfully")
        except Exception as e:
            print(e)
            
    def open_file_dialog(self):
        folder = filedialog.askdirectory()
        if folder:
            print(f"Selected folder {folder}.")

        return folder

if __name__ == "__main__":
    main = Main()
