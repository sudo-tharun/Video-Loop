from os import name
import cv2,time,os,pytube
from pytube import YouTube
from moviepy.editor import *
import numpy as np
from ffpyplayer.player import MediaPlayer
import pytube,pygame


def setLoop(startpoint,endpoint): 
    clip=VideoFileClip("Retrieved Video.mp4")
    clip = clip.subclip(startpoint,endpoint)
    clip.preview()
    clip.close()


def setDuration(title):
    clip = VideoFileClip(title)
    duration=clip.duration
    print("\n Duration of the clip is: " , duration)
    print("\n Give input without any special characters (in seconds)!!")
    startpoint=int(input("\n Enter the starting point from where the video to be played: "))
    endpoint=int(input("\n Enter the end point of the video till where the video to be played: "))
    try:
        if startpoint<0 or endpoint>duration:
            print("\n Duration invalid!")
            c=int(input("\n Do you wish to try again? \n 1. Retry   2. Exit"))
            if c==1:
                print("\n Enter the correct bounds of the duration! ")
                setDuration(title) 
            else:
                exit()
        number=int(input("\n Enter number of times the video should be played: "))
        for i in range(number):
            time.sleep(1)
            setLoop(startpoint,endpoint)
            print("The number of times the video has been played: ",(i+1))
    except OSError:
        print("Input is invalid")
    print("The video with desired conditions has been successfully played!")
    clip.close()
    return


def retrieveVideo(URL):
    try:
        yt = YouTube(URL)
        print("\n Retrieving Video details....")
        time.sleep(1)
        print("\n Title of video:   ",yt.title)
        time.sleep(1)
        print("\n Length of video:  ",yt.length,"seconds")
        time.sleep(1)
        stream = str(yt.streams.filter(progressive=True))
        stream = stream[1:]
        stream = stream[:-1]
        streamlist = stream.split(", ")
        print("\n All available options for quality:\n")
        if len(streamlist)<=1:
            print("Video is not available for download from YouTube! ")
            print("Exiting the application!")
            exit()
        for i in range(0,len(streamlist)):
            st = streamlist[i].split(" ")
            print(i+1,") ",st[1]," and ",st[3],sep='')
        tag = int(input("\n Enter the itag of your preferred stream to view:   "))
        ys = yt.streams.get_by_itag(tag)
        print("\n Retrieving video...")
        time.sleep(2)
        print("\n Speed of retrieval depends on your internet speed and the quality of video chosen!")
        nameoffile="Retrieved video"
        ys.download(filename=nameoffile)
        print("\n Your video is almost ready to play!!")
        time.sleep(3)
        print("\n Retrieval completed!!")
        print()
        nameoffile+=".mp4"
        setDuration(nameoffile)
    except:
        print("\n There is an Error in the input of the URL!!")
        choice=int(input("\n Do you wish to try again? \n 1. Yes    2. No \n "))
        if choice==1:
            mainFunction()
        else:
            print("Exiting from the application...!!")
            exit()
    return


def changeNameofFile(nameoffile):
    print("\n The name should not include any special characters. Only alphabets are allowed!!")
    newName=input("\n Enter the name to which the file has to modified: ")
    newName+=".mp4"
    os.rename(nameoffile,newName)
    print("\n Your downloaded file " + '" ' +nameoffile+' "' + " has been successfully renamed to: ",newName)
    exit()


def mainFunction():
    print("\n Note that the application supports only YouTube URLs.")
    URL=input("\n Provide the URL of the video to be retrieved: ")
    retrieveVideo(URL)
    print("\n Choose one of the actions on the file. Changes cannot be undone!")
    choiceoffile=int(input("\n 1. Rename    2. Delete  \n "))
    if choiceoffile==1:
        changeNameofFile("Retrieved Video.mp4")
    else:
        os.remove("Retrieved Video.mp4")
        print("The retrieved video has been successfully deleted!")
        exit()


if __name__=="__main__":
    mainFunction()

