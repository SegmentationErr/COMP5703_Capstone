import requests
from urllib import parse
import json
import time
import csv


url = "https://twitter.com/i/api/2/search/adaptive.json?\
include_profile_interstitial_type=1&\
include_blocking=1&\
include_blocked_by=1&\
include_followed_by=1&\
include_want_retweets=1&\
include_mute_edge=1&\
include_can_dm=1&\
include_can_media_tag=1&\
include_ext_has_nft_avatar=1&\
skip_status=1&\
cards_platform=Web-12&\
include_cards=1&\
include_ext_alt_text=true&\
include_ext_limited_action_results=false&\
include_quote_count=true&\
include_reply_count=1&\
tweet_mode=extended&\
include_ext_collab_control=true&\
include_entities=true&\
include_user_entities=true&\
include_ext_media_color=true&\
include_ext_media_availability=true&\
include_ext_sensitive_media_warning=true&\
include_ext_trusted_friends_metadata=true&\
send_error_codes=true&\
simple_quoted_tweet=true&\
q={} +filter:replies&\
count=20&\
query_source=typed_query&\
{}\
pc=1&\
spelling_corrections=1&\
include_ext_edit_control=true&\
ext=mediaStats%2ChighlightedLabel%2ChasNftAvatar%2CvoiceInfo%2Cenrichments%2CsuperFollowMetadata%2CunmentionInfo%2CeditControl%2Ccollab_control%2Cvibe"



url_token = 'https://api.twitter.com/1.1/guest/activate.json'

keyStr = '85e82633ee641185741ba00acf5703441798c3d5b07effa1c58d65ca8730a415f8840f6c89e65a3af4a991caf6a4b1bdf3c30b2ad2c458cad7f7efe17a334219a7d3e64ac5dcd60adeeb07da8e2a6b23'

# cookies_str += ';ct0={}'.format(keyStr)

cookies = {}

cookies['guest_id_ads'] = 'v1%3A166489189940018919'
cookies['att'] = '1-a8Bhc9qFX6oYkF9hOw4XKyIhIcLmodaT3jkHcXiH'
cookies['ct0'] = keyStr
cookies['auth_token'] = 'd6d19433384b43e95b6e2b33e3365bbbb24cf1ae'
cookies['lang'] = 'en'
cookies['guest_id'] = 'v1%3A166489189940018919'
cookies['twid'] = 'u%3D1571902423895253000'
cookies['personalization_id'] = '"v1_AVj4YU1IzO9cCFYvadoFVw=="'
cookies['guest_id_marketing'] = 'v1%3A166489189940018919'
cookies['mbox'] = 'session#94ab9fbcbea246788577a5227a8ba567#1653569580|PC#94ab9fbcbea246788577a5227a8ba567.36_0#1716812520'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Referer': 'https://twitter.com/',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'x-csrf-token': keyStr,
    'x-twitter-client-language': 'en',
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
}

query = '({}) lang:en until:{} since:{}'

row_id = 1
csvfile = open('out.login.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(['id', 'created_at', 'full_text'])


# def parse_cookie():
#     cookies_lst = cookies_str.split(";")
#     for cookie in cookies_lst:
#         name, value = cookie.strip().split("=", 1)
#         cookies[name] = value



def formate_time2time_stamp(time_):
    return int(time.mktime(time.strptime(time_, "%Y-%m-%d")))


def time_stamp2formate_time(time_):
    return time.strftime("%Y-%m-%d", time.localtime(int(time_)))


def q_list_get(key_word, since, until):
    since_p = formate_time2time_stamp(since)
    until_p = formate_time2time_stamp(until)
    step = 60 * 60 * 24
    while since_p < until_p:
        next = since_p + step
        yield query.format(key_word, time_stamp2formate_time(next), time_stamp2formate_time(since_p))
        since_p = next


def get_token():
    token = json.loads(requests.post(url_token, headers=headers).text)['guest_token']
    headers['x-guest-token'] = token


if __name__ == "__main__":
    # parse_cookie()
    key_word = 'Bitcoin OR BTC'
    since = '2017-09-01'
    until = '2022-01-01'
    num = 0
    tweet_list = []
    cursor = ''
    for q_ in q_list_get(key_word, since, until):
        try:
            cursor = ''
            while True:
                # Get a new x-guest-token
                # if num > 500:
                #     get_token()=
                #     num = 0
                # num += 1
                if cursor == '':
                    format_url = url.format(parse.quote(q_), cursor)
                else:
                    format_url = url.format(parse.quote(q_), 'cursor={}&'.format(cursor))
                # format_url
                res = requests.get(format_url, headers=headers, cookies=cookies)
                root = json.loads(res.text)
                tweets = root['globalObjects']['tweets']
                if not tweets:
                    break
                for i in tweets.values():
                    created_at = i['created_at']
                    date = time.strptime(created_at, "%a %b %d %H:%M:%S %z %Y")
                    created_at = time.strftime("%Y-%m-%d %H:%M:%S", date)
                    full_text = i['full_text']
                    writer.writerow([row_id, created_at, full_text])
                    row_id += 1
                    print(created_at + ": " + full_text)

                next = root.get('timeline', {}).get('instructions', [])

                if len(next) > 1:
                    cursor = next[-1]\
                        .get('replaceEntry', {})\
                        .get('entry', {})\
                        .get('content', {})\
                        .get('operation', {}) \
                        .get('cursor', {})\
                        .get('value', '')
                else:
                    cursor = next[0]\
                        .get('addEntries', {})\
                        .get('entries', [{}])[-1]\
                        .get('content', {})\
                        .get('operation', {}) \
                        .get('cursor', {})\
                        .get('value', '')
                if not cursor:
                    cursor = ''
        except Exception as e:
            print(e)

csvfile.close()

def to_json():
    with open('./out.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(tweet_list, ensure_ascii=False))


