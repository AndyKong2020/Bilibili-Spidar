import asyncio
import jsonLoader
import pandas as pd

def main():
    videos = jsonLoader.loadJsonFile("details.json")
    titles = jsonLoader.getJsonData(videos, "title")
    for video in videos:
        print(video["title"])


if __name__ == '__main__':
    main()