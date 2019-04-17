from log_parser.__main__ import Parser, User


def test_get_detailed_information():
    parser = Parser('')
    user1 = User('email_1')
    user1.sent_mails = 2
    user1.failed_mails = 1
    user1.successful_mails = 1
    parser.users['email_1'] = user1

    assert parser.get_detailed_information() == 'С ящика email_1 было отправлено 2 писем. Из них 1 успешно, а 1 нет.\n'
