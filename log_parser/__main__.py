import re

regexp_client_connect = r' (.{11}):.+sasl_method=.+sasl_username=(.+)'
regexp_message_sent = r' (.{11}):.+status=(\w+)'
regexp_id_cleaned = r' (.{11}): removed'


class User:
    def __init__(self, email):
        self.email = email
        self.sent_mails = 0
        self.successful_mails = 0
        self.failed_mails = 0


class Parser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = {}
        self.ids = {}

    def handle_file(self):
        with open(self.file_path, 'r') as fl:
            for line in fl.readlines():
                self._parse_data(line)

    def _parse_data(self, line):
        match = re.findall(regexp_client_connect, line)
        if match:
            new_id = match[0][0]
            user_mail = match[0][1]
            if user_mail not in self.users:
                self.users[user_mail] = User(user_mail)
            self.ids[new_id] = self.users[user_mail]
        else:
            match = re.findall(regexp_message_sent, line)
            if match:
                work_id = match[0][0]
                status = match[0][1]
                if work_id in self.ids:
                    if status == 'sent':
                        self.ids[work_id].successful_mails += 1
                        self.ids[work_id].sent_mails += 1
                    elif status == 'expired':
                        self.ids[work_id].failed_mails += 1
                        self.ids[work_id].sent_mails += 1
            else:
                match = re.findall(regexp_id_cleaned, line)
                if match:
                    if match[0] in self.ids:
                        self.ids.pop(match[0])

    def get_detailed_information(self):
        result = ''
        for each in self.users:
            sent_mails = self.users[each].sent_mails
            successful_mails = self.users[each].successful_mails
            failed_mails = self.users[each].failed_mails
            if sent_mails:
                if failed_mails:
                    result += 'С ящика {0} было отправлено {1} писем. Из них {2} успешно, а {3} нет.\n'.format(
                        each, sent_mails, successful_mails, failed_mails)
                else:
                    result += 'С ящика {0} было отправлено {1} писем. Из них {2} успешно.\n'.format(
                        each, sent_mails, successful_mails)
        return result

    def get_general_information(self):
        successful_mails = 0
        failed_mails = 0
        for each in self.users:
            successful_mails += self.users[each].successful_mails
            failed_mails += self.users[each].failed_mails
        return f'Всего отправлено писем успешно: {successful_mails}, с ошибками: {failed_mails}'
