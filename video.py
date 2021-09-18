# Importing libraries

import sys
from youtube_dl import YoutubeDL
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)





import chromedriver_autoinstaller

PATH=resource_path("")
path=chromedriver_autoinstaller.install(PATH)
          
import platform
from tkinter import *
from tkinter import filedialog
import time
import random
ac=str(random.randint(1,20))
b=str(random.randint(20,38))
y=Tk()
logo= PhotoImage(file=resource_path("Untitled.png"))
y.iconphoto(False,logo)
y.title("Youtube Video Downloader")
y.resizable(0,0)
def find_file():
    aaa=filedialog.askdirectory(title="Select folder to download videos")
    return aaa
def create_folder():
    ad=find_file()
    global ac
    global b
    ads=os.path.join(ad,f"Video{ac}{b}")
    os.mkdir(ads)
    return ads

defe=Entry(bg="white")
defe.grid(row=2,column=2)
adj=Label(text="Enter the name of the video(s) you want to download :")
adj.grid(row=2,column=1)
ack=Label(text="How many videos you want to download?")
ack.grid(row=3,column=1)
dee=Entry(bg="white")
dee.grid(row=3,column=2)
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(path,options=options)
driver.maximize_window()
def download_images():
    
    abc=[]
    
    asd=create_folder()        
    
    defei=str(defe.get())
    deee=int(dee.get())
    ii=0
    driver.get(f"https://www.youtube.in/results?search_query={defei}")
    r=driver.find_elements_by_class_name("yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail")
    abc.extend(r)
    while ii<=deee:
        
        if ii>=deee:
            break
        
      
        for video in abc:
            if video==None:
                print("lapislzauli")
                abc.remove(video)
            elif ii>=deee:
                break
            elif ii==len(abc):   
                driver.execute_script("window.scrollBy(0,925)", "")  
            time.sleep(5)
            eeyo=video.get_attribute("href")
            if eeyo==None:
                print("ggoogggooo")
               
               
            youtube_dl_opts={}
            
            
            try:
                
                with YoutubeDL(youtube_dl_opts) as ydl:
                    info_dict = ydl.extract_info(eeyo, download=False)
                    video_title = info_dict.get('title', None)
                    if "/"in video_title:
                        video_title=video_title.replace("/","∕")
                    video_duration = info_dict.get("duration",None)
                    if "\"" in video_title:
                        video_title=video_title.replace("\"","`")
                    if "|" in video_title:
                        video_title=video_title.replace("|","∣")
                    print(video_duration)

                    if video_duration ==0.0:
                        
                        abc=abc[ii+1:]
                        
                        print("stupid")
                        continue
                        
                        
              
                    
                os.system(f"youtube-dl -o  \"{asd}//{video_title}.mp4\" {eeyo} --abort-on-error ")
                
            
                
                print("zownloaded") 
                print(ii)  
                ii+=1 
            except:
                try:
                 abc.remove(video) 
                 print("hey,i m dead")
                except:
                 print(4*12)
                 igo=(ii*2)-1
                 abc=abc[igo:]
                 print(len(abc))
                 continue  
                  
        driver.execute_script("window.scrollBy(0,925)", "")  
        r=driver.find_elements_by_class_name("yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail")
        abc.extend(r)
        igo=(ii*2)
        
        abc=abc[igo:]  
        
        print(f"herererere {len(abc)}")       
    asd=asd.replace("/","\\")        
    if platform.system()=="Windows":           
        os.system(f"explorer \"{asd}\"") 
    elif platform.system()=="Linux":
        os.system(f"nautilus {asd}")  
    elif platform.system()=="Darwin":
        os.system(f"open /{asd}") 
    driver.quit()
    y.destroy()           
   
aadg=Button(y,bg="red",text="Download!",command=lambda:download_images(),activebackground="dark red",activeforeground="grey")
aadg.grid(row=4,column=1)

y.mainloop()

        
        
    
    
   
"""

"""