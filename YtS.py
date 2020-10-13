from __future__ import unicode_literals
from youtubesearchpython import SearchVideos
import youtube_dl
import os


def main():
    name = input('Podaj nazwę piosenki: ')

    search = SearchVideos(name, offset=1, mode="json", max_results=5)
    vidList = search.result()

    i = 0
    linklist = []
    temp = ''

    for item in vidList.split("\n"):
        if "title" in item:
            i += 1
            item = item.strip()
            temp = item.replace('"title": ', '')
        if "duration" in item:
            item = item.strip()
            item = item.replace('"duration": ', '')
            print(i, '.', temp, item)
        if "link" in item:
            item = item.replace('"link": ', '')
            item = item.replace('"', '')
            item = item.strip()
            linklist.append(item)
    number = input('Wybierz numer wybranego utworu (Lub wpisz "A" aby anulować) : ')
    try:
        if number != 'A':
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([linklist[int(number) - 1]])
    except:
        print('Podałeś błędną liczbę bądz znak')



while True:
    os.system('CLS')
    main()
    if input("Czy chcesz kontynuować? T/N : ") == 'N':
        break