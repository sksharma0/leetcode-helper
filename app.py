import json
from tqdm import tqdm
import requests
import pandas as pd
from datetime import datetime
from requests_meta import url, headers, json_request, json_request_get_submissions

# need to load questions meta from leetcode or not, load for the first time
load = False

if load:
    # Get Accepted Solutions
    response = requests.post(
        url = url,
        headers = headers,
        json = json_request
    )

    response = json.loads(response.text)
    questions = response['data']['problemsetQuestionList']['questions']
    questions_dict = [
        {
            'question': question['frontendQuestionId'],
            'difficulty': question['difficulty'],
            'name': question['title']
        } for question in questions
    ]
    for i, question in tqdm(enumerate(questions_dict)):
        headers['referer'] = f'https://leetcode.com/problems/{questions[i]["titleSlug"]}/submissions/'
        json_request_get_submissions['variables']['questionSlug'] = questions[i]["titleSlug"]
        submissions = requests.post(
            url = url,
            headers = headers,
            json = json_request_get_submissions
        )
        submissions = json.loads(submissions.text)['data']['questionSubmissionList']['submissions']
        accepted_submissions = [submission for submission in submissions if submission['status']==10]
        question['latest_accepted_timestamp'] = accepted_submissions[0]['timestamp']
        question['link'] = f'https://leetcode.com/problems/{questions[i]["titleSlug"]}/'
    pd.DataFrame(questions_dict, index=None).to_csv('solved_questions.csv', index=False)

else:
    questions_meta_path = 'solved_questions.csv'
    questions_meta = pd.read_csv(questions_meta_path, index_col=False)

    # AC questions submitted before 1-Jan-2024
    date = 1
    month = 1
    year = 2024
    questions_to_solve = questions_meta[questions_meta.latest_accepted_timestamp.apply(lambda x: datetime.fromtimestamp(x))<datetime(year, month, date)]
    questions_to_solve.to_csv('questions_to_solve.csv', index=False)
