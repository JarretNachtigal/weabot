# from bs4 import BeautifulSoup
import requests


# print title and id search results
def search_title(title):
    # query vrv for 'attack on titan'
    response = requests.get(f"https://api.vrv.co/disc/public/v1/US/M2/-/-/search?q=({title})=6&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Rpc2NcL3B1YmxpY1wvdj9cL1VTXC9NMlwvLVwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTcwMjA2NX19fV19&Signature=TovXLXQ9fIuRFT~WtiuU2e7bt9opMaKE76N08nDyNp4BvE6~fxjZKECutKbyLTxm4AWmWolcJFcf0QvSrKQbDmta2DIF3~w~8FLo63G-qZB6XH1RAgYPs64iaS33-FHhTpbuk103TBqpH5M~4ulBGNl19ke8pIA8jXkSvxYqhOmGx6YVfgCQX4KUmj-LnahEeLmbm4~iVGoySAzyu6di6cfQvLcWTmi7sTAyNNc4wGNvGJe-C1ZlNMdReHNI-Qzx28yIxObReE34kToN3PvjERJemXCPS9A6Coe~caXpeYkNBUDeKTxi-RfUsPeyiNFSlX9tdvYLxLlzfHBpCxRpQQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA")
    response = response.json()["items"]  # into item field of response dict
    items = response[1]["items"]  # should be a list of anime
    # this will list the anime names that have come back from the search by looping through the items list and printing the title field from each dict
    for anime in items:
        print(anime['title'])
        print(anime['id'])


# get series_id from title
def get_id_by_title(title):
    # query vrv for title
    response = requests.get(f"https://api.vrv.co/disc/public/v1/US/M2/-/-/search?q=({title})=6&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Rpc2NcL3B1YmxpY1wvdj9cL1VTXC9NMlwvLVwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTcwMjA2NX19fV19&Signature=TovXLXQ9fIuRFT~WtiuU2e7bt9opMaKE76N08nDyNp4BvE6~fxjZKECutKbyLTxm4AWmWolcJFcf0QvSrKQbDmta2DIF3~w~8FLo63G-qZB6XH1RAgYPs64iaS33-FHhTpbuk103TBqpH5M~4ulBGNl19ke8pIA8jXkSvxYqhOmGx6YVfgCQX4KUmj-LnahEeLmbm4~iVGoySAzyu6di6cfQvLcWTmi7sTAyNNc4wGNvGJe-C1ZlNMdReHNI-Qzx28yIxObReE34kToN3PvjERJemXCPS9A6Coe~caXpeYkNBUDeKTxi-RfUsPeyiNFSlX9tdvYLxLlzfHBpCxRpQQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA")
    response = response.json()["items"]  # into item field of response dict
    items = response[1]["items"]  # should be a list of anime
    # if title matches, return id
    for anime in items:
        if title.casefold() == anime['title'].casefold():
            return anime['id']
    # else prompt new search or quit
    print("not found")


# get seasons from id
def get_seasons(series_id):
    response = requests.get(f'https://api.vrv.co/cms/v2/US/M2/-/seasons?series_id={series_id}&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6XC9cL2FwaS52cnYuY29cL2Ntc1wvdj9cL1VTXC9NMlwvLVwvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY1MTcwMjEyNn19fV19&Signature=UVd1Lfm00GOZJc4U623vB99U86bBcQzApf3voz-JXzJ2c17CgXjPwPhgTVEJCjkLM7pj5wz3tGimRoPTHFtLrNwdjkGkpQ4cNjLq8aecvxLx5Ob~SLZw~LWfTKQpAeqDEbzULJyO~EoZM7bPakbIazcW7F8ZJCwjkFeiomhlfk5prCGST1dosCBc8AuG2nirwXPZB~bbd1mPvk3HpYoZv35Qdqr6JdoYvZ0UWH5hSyncEBGmsjHdwM400rOHttUabmIkFgtiWBIrkUjh7o6CXlBFClYzUhals05pRvTeZZi7y8cbhWpeVOqoB3PyBFjl~JweD4n1CSLBWANdM8BJNQ__&Key-Pair-Id=APKAJMWSQ5S7ZB3MF5VA')
    response = response.json()
    items = response["items"]
    # print season names
    for item in items:
        print(item["title"])
    # return dict of season names and s


# get id of season with series_id and season title
def get_episodes_by_season_id():
    pass


# main method
def main():
    title = "attack on titan"
    season_id = ""
    series_id = get_id_by_title(title)
    get_seasons(series_id)
    get_episodes_by_season_id(season_id)


if __name__ == "__main__":
    main()
