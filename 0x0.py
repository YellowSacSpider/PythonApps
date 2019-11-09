import pyautogui
import cv2
import numpy
import time
import sys, string, os

lolOpened = False
_automatedBot = False
_optionChoosed = False

def lolDir():
    global lolOpened
    global _automatedBot
    global _optionChoosed
    
    if lolOpened == False:
        #print("Please write your fully lol location (Example: C:\Riot Games\League of Legends\):")
        #lolOpen = input()
        #os.chdir(lolOpen)
        #os.system('LeagueClient.exe')
        print("Execution success")
        lolOpened = True
    while(_optionChoosed == False):
        if lolOpened == True:
            print('You want automated bot? Y/N')
            automatedBot = input()

            if automatedBot == 'Y':
                _automatedBot = True
                _optionChoosed = True
                print('Done! Bot automated(Waiting for Play button...)')
                playButton()      
        
            if automatedBot == 'N':
                _automatedBot = False
                _optionChoosed = True
                print('Done! Bot unautomated')
            
            
            if automatedBot != 'N' and automatedBot != 'Y':
                print('Wrong command!')
        
def playButton():
    playButtonLocation = None
    while playButtonLocation is None:
        playButtonLocation = pyautogui.locateOnScreen('play.png', grayscale=True, confidence=.8)
        print('Wait for image...')
        
        if playButtonLocation != None:
            playButtonPoint = pyautogui.center(playButtonLocation)
            playButtonX, playButtonY = playButtonPoint
            print(playButtonLocation)
            time.sleep(5)
            pyautogui.click(playButtonX, playButtonY)
            botsButton()

def botsButton():
    botsButtonLocation = None
    while botsButtonLocation is None:
        botsButtonLocation = pyautogui.locateOnScreen('botsButton.png', grayscale=True, confidence=.8)
        print('Wait for image...')
    
        if botsButtonLocation != None:
            botsButtonPoint = pyautogui.center(botsButtonLocation)
            botsButtonX, botsButtonY = botsButtonPoint
            print(botsButtonLocation)
            time.sleep(5)
            pyautogui.click(botsButtonX, botsButtonY)
            introButton()

def introButton():
    introButtonLocation = None
    while introButtonLocation is None:
        introButtonLocation = pyautogui.locateOnScreen('introButton.png', grayscale=True, confidence=.8)
        print('Wait for image...')
    
        if introButtonLocation != None:
            introButtonPoint = pyautogui.center(introButtonLocation)
            introButtonX, introButtonY = introButtonPoint
            print(introButtonLocation)
            time.sleep(5)
            pyautogui.click(introButtonX, introButtonY)
            findButton()

def findButton():
    findButtonLocation = None
    while findButtonLocation is None:
        findButtonLocation = pyautogui.locateOnScreen('findButton.png', grayscale=True, confidence=.8)
        print('Wait for image...')
    
        if findButtonLocation != None:
            findButtonPoint = pyautogui.center(findButtonLocation)
            findButtonX, findButtonY = findButtonPoint
            print(findButtonLocation)
            time.sleep(5)
            pyautogui.click(findButtonX, findButtonY)

lolDir()