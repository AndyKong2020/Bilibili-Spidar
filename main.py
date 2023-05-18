import asyncio
import jsonLoader
import pandas as pd


def main():
    df_roster = pd.read_excel("roster.xlsx")
    print(df_roster)
    school_ids = df_roster["学校"].tolist()
    print(school_ids)
    videos = jsonLoader.loadJsonFile("full.json")
    titles = jsonLoader.getJsonData(videos, "title")
    bvids = jsonLoader.getJsonData(videos, "bvid")
    urls = ['https://www.bilibili.com/video/' + bvid for bvid in bvids]
    df_details = pd.DataFrame({"title": titles, "bvid": bvids, "url": urls})
    print(df_details)
    df_details.to_excel("details.xlsx", index=False)
    with pd.ExcelWriter("roster.xlsx", mode="a", engine='openpyxl') as writer:
        df_details.to_excel(writer, sheet_name="all", index=False)
        for school_id in school_ids:
            df_school = pd.DataFrame(df_details[df_details["title"].str.contains(school_id)])
            df_school.to_excel(writer, sheet_name=school_id, index=False)
    # print(titles)
    # for video in videos:
    #     print(video["title"])


if __name__ == '__main__':
    main()
