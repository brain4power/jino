from log_parser.__main__ import Parser, User


def test_get_general_information():
    parser = Parser('')
    user1 = User('email_1')
    user1.sent_mails = 2
    user1.failed_mails = 1
    user1.successful_mails = 1
    parser.users['some_id_1'] = user1
    user2 = User('email_2')
    user2.sent_mails = 5
    user2.successful_mails = 5
    parser.users['some_id_2'] = user2

    assert parser.get_general_information() == 'Всего отправлено писем успешно: 6, с ошибками: 1'
