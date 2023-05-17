import asyncio
import re

from bilibili_api import video
import jsonLoader
import pandas as pd

async def main() -> None:
    details = []
    data = jsonLoader.loadJsonFile("full.json")
    #print(data)
    url_data = jsonLoader.getJsonData(data, "url")
    #print(url_data)
    bvlist = jsonLoader.get_bv(url_data)
    print(bvlist)
    for bvid in bvlist:
        v = video.Video(bvid=bvid)
        info = await v.get_info()
        # if info["title"].find('南京航空航天大学') != -1:
        #     details.append(info)
        details.append(info)
        #df = pd.DataFrame(details)
        #pd.to_excel("details.xlsx", df)
        jsonLoader.saveJsonFile("details.json", details)
        print(details)
    # 实例化 Video 类
    # v = video.Video(bvid="BV1yM411G76R")
    # # 获取信息
    # info = await v.get_info()
    # # 打印信息
    # print(info)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())