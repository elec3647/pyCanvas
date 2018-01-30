# coding=utf-8
import json
import os
import requests


class Quiz(object):
    def __init__(self, title, **kwargs):
        self.title = title
        self.shuffle_answers = True
        self.time_limit = 5
        self.description = None
        self.quiz_type = "assignment"
        self.show_correct_answers = True

        # Any optional items
        for key, value in kwargs.items():
            self.__setattr__(key, value)

        """
        self.assignment_group_id = None
        self.hide_results
        self.show_correct_answers_last_attempt
        self.show_correct_answers_at
        self.hide_correct_answers_at
        self.allowed_attempts
        self.scoring_policy
        self.one_question_at_a_time
        self.cant_go_back
        self.access_code
        self.ip_filter
        self.due_at = "2011-10-21T18:48Z"
        self.lock_at
        self.unlock_at
        self.published = False
        self.one_time_results
        self.only_visible_to_overrides
        """

    def __str__(self):
        return str(self.__dict__)

    def json(self):
        return json.dumps(dict(quiz=self.__dict__))

    def create(self, title, description=None):
        pass

    def edit(self):
        self.notify_of_update = False


class QuizPoster(object):
    def __init__(self, api_key, course_id, base_url="https://auburn.instructure.com/api/v1"):
        self.course_id = course_id
        self.api_key = api_key
        self.header = {
            'Authorization': 'Bearer {API_KEY}'.format(API_KEY=self.api_key),
            'Content-Type': 'application/json'
        }
        self.base_url = base_url
        self.post_path = "courses/{course_id}/quizzes".format(course_id=self.course_id)
        self.s = requests.Session()

    def post(self, quiz_object):
        my_url = os.path.join(self.base_url, self.post_path)
        quiz_data = quiz_object.json()
        ret = self.s.post(my_url, data=quiz_data, headers=self.header)
        return ret.json()


if __name__ == '__main__':
    for cnt in range(1, 15):
        key = open('.api_key').read().strip()
        course = open('.course').read().strip()
        quiz = Quiz("Lab Session %d Quiz" % cnt)
        poster = QuizPoster(key, course)
        quiz_return = poster.post(quiz)
        #quiz.__dict__ = quiz_return
        #print(quiz.quiz_reports_url)
        #pprint(quiz_return)
        #pprint(quiz)
        #print()
