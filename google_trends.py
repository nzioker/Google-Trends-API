from pytrends.request import TrendReq
import pandas as pd


def search_trend(search_term):
    trends_cursor = TrendReq(retries=3)
    keyword_list = []
    keyword_list.append(search_term)
    try:
        trends_cursor.build_payload(keyword_list, cat=0, timeframe="today 12-m")
        data = trends_cursor.interest_over_time()
        return data, search_term
    except IndexError as i:
        return "Enter a search term"
    except KeyError as k:
        return k.args


def save_to_excel(data):
    file_name = generate_file_name(data)
    try:
        return pd.DataFrame(data[0]).to_excel(file_name)
    except IndexError as i:
        return "Enter a search term"
    except Exception as e:
        return e.with_traceback


def generate_file_name(data):
    try:
        file_name = f"{data[1]}_search_results.xlsx"
        return file_name
    except IndexError as i:
        print("Enter a valid search term")


data = search_trend("Pirates")
save_to_excel(data)
