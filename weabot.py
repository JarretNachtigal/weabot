# from bs4 import BeautifulSoup
import requests


# print title and id search results
# FUTURE: prompt user with a list of indexed titles from searchg results + 'none' and ask them to give index
def search_title(title):
    # query vrv for 'title'
    response = requests.get(f"https://api.vrv.co/disc/public/v1/US/M2/-/-/search?q=({title})=6&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Rpc2NcL3B1YmxpY1wvdj9cL1VTXC9NMlwvLVwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTcwMjA2NX19fV19&Signature=TovXLXQ9fIuRFT~WtiuU2e7bt9opMaKE76N08nDyNp4BvE6~fxjZKECutKbyLTxm4AWmWolcJFcf0QvSrKQbDmta2DIF3~w~8FLo63G-qZB6XH1RAgYPs64iaS33-FHhTpbuk103TBqpH5M~4ulBGNl19ke8pIA8jXkSvxYqhOmGx6YVfgCQX4KUmj-LnahEeLmbm4~iVGoySAzyu6di6cfQvLcWTmi7sTAyNNc4wGNvGJe-C1ZlNMdReHNI-Qzx28yIxObReE34kToN3PvjERJemXCPS9A6Coe~caXpeYkNBUDeKTxi-RfUsPeyiNFSlX9tdvYLxLlzfHBpCxRpQQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA")
    response = response.json()["items"]  # into item field of response dict
    items = response[1]["items"]  # should be a list of anime
    # this will list the anime names that have come back from the search by looping through the items list and printing the title field from each dict
    titles_and_ids = []
    for anime in items:
        titles_and_ids.append(
            {"title": anime['title'], "series_id": anime['id']})
        # print(anime['title'])
        # print(anime['id'])
    return titles_and_ids


# get series_id from title
# will fail if title string is not an exact non-case sensitive match,
# should use return value from search_title() method
def get_id_by_title(title):
    # search query vrv for title
    response = requests.get(f"https://api.vrv.co/disc/public/v1/US/M2/-/-/search?q=({title})=6&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Rpc2NcL3B1YmxpY1wvdj9cL1VTXC9NMlwvLVwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTcwMjA2NX19fV19&Signature=TovXLXQ9fIuRFT~WtiuU2e7bt9opMaKE76N08nDyNp4BvE6~fxjZKECutKbyLTxm4AWmWolcJFcf0QvSrKQbDmta2DIF3~w~8FLo63G-qZB6XH1RAgYPs64iaS33-FHhTpbuk103TBqpH5M~4ulBGNl19ke8pIA8jXkSvxYqhOmGx6YVfgCQX4KUmj-LnahEeLmbm4~iVGoySAzyu6di6cfQvLcWTmi7sTAyNNc4wGNvGJe-C1ZlNMdReHNI-Qzx28yIxObReE34kToN3PvjERJemXCPS9A6Coe~caXpeYkNBUDeKTxi-RfUsPeyiNFSlX9tdvYLxLlzfHBpCxRpQQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA")
    response = response.json()["items"]  # into item field of response dict
    items = response[1]["items"]  # should be a list of anime
    # if title matches, return id
    for anime in items:
        if title.casefold() == anime['title'].casefold():
            return anime['id']
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
    # return dict of season names and s


# prompt user to decide the correct show from the list of dics
# return a tuple (title, series_id)
def decide_anime(titles_and_ids):
    pass


# get id of season with series_id and season title
def get_episodes_by_season_id():
    pass


# main method
def main():
    title_input = input("what title?")
    # this is the list of search results - list of dicts
    titles_and_ids = search_title(title_input)
    title, series_id = decide_anime(titles_and_ids)
    season_id = ""
    series_id = get_id_by_title(title)
    get_seasons(series_id)
    get_episodes_by_season_id(season_id)


if __name__ == "__main__":
    main()
