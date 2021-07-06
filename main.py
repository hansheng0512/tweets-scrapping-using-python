import os

MAX_RESULT = 100
DATE_START = '2020-06-01'
DATE_END = '2020-07-01'
HASHTAG = 'relax'
JSON_FILENAME = 'text-query-tweets'

os.system(f'snscrape --jsonl --progress --max-results {MAX_RESULT} --since {DATE_START} twitter-hashtag "{HASHTAG} until:{DATE_END}" > {JSON_FILENAME}.json')
