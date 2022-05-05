# from bs4 import BeautifulSoup
import requests
import json


# this method will request vrv normally and get the policy, signature, and key_pair_id dynamically
def get_vrv_fields():
    pass
    # print title and id search results


def search_title(title):
    # fields for formatting query url
    title = title.replace(" ", "%20")
    policy = "eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Rpc2NcL3B1YmxpY1wvdj9cL1VTXC9NMlwvLVwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTc4ODQ2NX19fV19"
    signature = "Ny3UchW9fcQoCax557d4ooTKnJihH~hoHHSuI4dF~OttmZEn7qd2mLOIstHtXl0xFffkInJRzCIuCzSM4EwJDPg49mCCkEKegEOdOf6iKIMFTz8KLej5GWvfpvfcLbHrc17ToHzCAyElNglNzgFmQ6xSihDNV8bzCYpDjWZb1rrb6hPIMj7AtCLxEFxvsE9Za6RIIdvkuZ1FW6wEu-mAiHf9MiHotO63GjPS8TCZV824u8zBCFFJC0~L6Y1FSU3AetLKz-wvsWoTfOwdX2M2s7kq8IkICzfD~LF37x~4UC8toNp4wRMvg3wMhpsBUaPlrDT1NCo1b1bROdFym~y03A__"
    key_pair_id = "APKAJMWSQ5S7ZB3MF5VA"
    # full url to query
    url = f"https://api.vrv.co/disc/public/v1/US/M2/-/-/search?q={title}&n=6&Policy={policy}&Signature={signature}&Key-Pair-Id={key_pair_id}"
    # query vrv for 'title'
    response = requests.get(url).json()
    # write json response to file
    with open('data.json', 'w') as f:
        json.dump(response, f)
    response = response["items"]  # go into item field of response dict
    items = response[1]["items"]  # should be a list of anime
    # this will list the anime names that have come back from the search by looping through the items list and printing the title field from each dict
    titles_and_ids = []
    for anime in items:
        titles_and_ids.append(
            {"title": anime['title'], "series_id": anime['id']})
    return titles_and_ids


# get series_id from title
# will fail if title string is not an exact non-case sensitive match,
# should use return value from search_title() method
def get_id_by_title(title):
    # search query vrv for title
    # response = requests.get(f"https://vrv.co/?q={title}")
    # these are the fields used in the api call url, need to be filled dynamically
    # policy = "eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Rpc2NcL3B1YmxpY1wvdj9cL1VTXC9NMlwvLVwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTc4ODQ2NX19fV19"
    # signature = "Ny3UchW9fcQoCax557d4ooTKnJihH~hoHHSuI4dF~OttmZEn7qd2mLOIstHtXl0xFffkInJRzCIuCzSM4EwJDPg49mCCkEKegEOdOf6iKIMFTz8KLej5GWvfpvfcLbHrc17ToHzCAyElNglNzgFmQ6xSihDNV8bzCYpDjWZb1rrb6hPIMj7AtCLxEFxvsE9Za6RIIdvkuZ1FW6wEu-mAiHf9MiHotO63GjPS8TCZV824u8zBCFFJC0~L6Y1FSU3AetLKz-wvsWoTfOwdX2M2s7kq8IkICzfD~LF37x~4UC8toNp4wRMvg3wMhpsBUaPlrDT1NCo1b1bROdFym~y03A__"
    # key_pair_id = "APKAJMWSQ5S7ZB3MF5VA"
    # response = requests.get(
    #     f"https://api.vrv.co/disc/public/v1/US/M2/-/-/search?q=({title})=6&Policy={policy}&Signature={signature}&Key-Pair-Id={key_pair_id}")
    # response = response.json()["items"]  # into item field of response dict
    # items = response[1]["items"]  # should be a list of anime
    # if title matches, return id
    # for anime in items:
    #     if title.casefold() == anime['title'].casefold():
    #         return anime['id']
    # else prompt new search or quit
    print("not found")


# get seasons from series_id (id on vrv)
def get_seasons(series_id):
    response = requests.get(f'https://api.vrv.co/cms/v2/US/M2/-/seasons?series_id={series_id}&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Ntc1wvdj9cL1VTXC9NMlwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTcwMjEyNn19fV19&Signature=UVd1Lfm00GOZJc4U623vB99U86bBcQzApf3voz-JXzJ2c17CgXjPwPhgTVEJCjkLM7pj5wz3tGimRoPTHFtLrNwdjkGkpQ4cNjLq8aecvxLx5Ob~SLZw~LWfTKQpAeqDEbzULJyO~EoZM7bPakbIazcW7F8ZJCwjkFeiomhlfk5prCGST1dosCBc8AuG2nirwXPZB~bbd1mPvk3HpYoZv35Qdqr6JdoYvZ0UWH5hSyncEBGmsjHdwM400rOHttUabmIkFgtiWBIrkUjh7o6CXlBFClYzUhals05pRvTeZZi7y8cbhWpeVOqoB3PyBFjl~JweD4n1CSLBWANdM8BJNQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA')
    response = response.json()
    items = response["items"]
    # print season names
    for item in items:
        print(item["title"])
    # return list dict of season names ids


# prompt user to decide the correct show from the list of dics
# return a tuple (title, series_id)
def decide_anime(titles_and_ids):
    for i, anime in enumerate(titles_and_ids):
        print(f"[{i+1}] {anime['title']}")
    num = int(input("please choose the number corresponding to the correct anime"))
    return titles_and_ids[num-1]['title'], titles_and_ids[num-1]['series_id']


# get id of season with series_id and season title
def get_episodes_by_season_id():
    pass


# main method
def main():
    get_vrv_fields()
    title_input = "attack on titan"
    # this is the list of search results - list of dicts
    titles_and_ids = search_title(title_input)
    print(titles_and_ids)
    # these the the title and series id of the chosen anime
    title, series_id = decide_anime(titles_and_ids)
    print(title, series_id)
    # this is the season_id of the chosen show/season
    season_id = ""

    # series_id = get_id_by_title(title)
    # get_seasons(series_id)
    # get_episodes_by_season_id(season_id)


if __name__ == "__main__":
    main()
