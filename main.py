import asyncio
import jsonLoader
import pandas as pd


def main():
    videos = jsonLoader.loadJsonFile("details.json")
    titles = jsonLoader.getJsonData(videos, "title")
    bvids = jsonLoader.getJsonData(videos, "bvid")
    urls = ['https://www.bilibili.com/video/' + bvid for bvid in bvids]
    df = pd.DataFrame({"title": titles, "bvid": bvids, "url": urls})
    print(df)
    df.to_excel("details.xlsx", index=False)
    # print(titles)
    # for video in videos:
    #     print(video["title"])


if __name__ == '__main__':
    main()
