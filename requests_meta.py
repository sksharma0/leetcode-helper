"""
Fill the below headers with your data
to get the data, go to inspect in your browser, select network tab, 
filter questions on status=solved, right click on the network request, copy as curl
get the required fields from curl request
update the headers which are different in your request, or empty in this request
"""

url = 'https://leetcode.com/graphql/'

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.7',
    'content-type': 'application/json',
    'cookie': '<your-cookie>',
    'origin': 'https://leetcode.com',
    'priority': 'u=1, i',
    'random-uuid': '<your-uuid>',
    'referer': 'https://leetcode.com/problemset/?status=AC',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'uuuserid': '<your-uuuserid>',
    'x-csrftoken': '<your-token>'
}

json_request = {"query":"\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\n  problemsetQuestionList: questionList(\n    categorySlug: $categorySlug\n    limit: $limit\n    skip: $skip\n    filters: $filters\n  ) {\n    total: totalNum\n    questions: data {\n      acRate\n      difficulty\n      freqBar\n      frontendQuestionId: questionFrontendId\n      isFavor\n      paidOnly: isPaidOnly\n      status\n      title\n      titleSlug\n      topicTags {\n        name\n        id\n        slug\n      }\n      hasSolution\n      hasVideoSolution\n    }\n  }\n}\n    ",
                "variables":{"categorySlug":"all-code-essentials",
                            "skip":0,
                            "limit": 5000,
                            "filters":{"status":"AC"}},
                "operationName":"problemsetQuestionList"}

json_request_get_submissions = {"query":"\n    query submissionList($offset: Int\u0021, $limit: Int\u0021, $lastKey: String, $questionSlug: String\u0021, $lang: Int, $status: Int) {\n  questionSubmissionList(\n    offset: $offset\n    limit: $limit\n    lastKey: $lastKey\n    questionSlug: $questionSlug\n    lang: $lang\n    status: $status\n  ) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      title\n      titleSlug\n      status\n      statusDisplay\n      lang\n      langName\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      hasNotes\n      notes\n      flagType\n      topicTags {\n        id\n      }\n    }\n  }\n}\n    ",
                                "variables":{"questionSlug":"",
                                             "offset":0,
                                             "limit":20,
                                             "lastKey":None},
                                "operationName":"submissionList"}