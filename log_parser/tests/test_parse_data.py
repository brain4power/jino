from log_parser.__main__ import Parser


def test_parse_data():
    parser = Parser('')
    data = 'Jul 10 13:23:35 srv24-s-st postfix/smtpd[16005]: EC1ECDF0510: client=vpn2-a234.Voronezh.golden.ru[212.46.226.234], sasl_method=LOGIN, sasl_username=karepova@start-cbs.ru'
    parser._parse_data(data)
    assert 'EC1ECDF0510' in parser.ids
    assert parser.users['karepova@start-cbs.ru'] == parser.ids['EC1ECDF0510']

    data2 = 'Jul 10 13:23:50 srv24-s-st postfix/smtp[16375]: EC1ECDF0510: to=<1680827@mail.ru>, relay=mxs.mail.ru[94.100.176.20]:25, delay=15, delays=11/0/0.02/4, dsn=2.0.0, status=sent (250 OK id=1SoWf6-0000Dv-Lf)'
    parser._parse_data(data2)
    assert parser.users['karepova@start-cbs.ru'].sent_mails == 1
    assert parser.users['karepova@start-cbs.ru'].successful_mails == 1

    data3 = 'Jul 10 13:39:13 srv24-s-st postfix/qmgr[3043]: EC1ECDF0510: from=<karepova@start-cbs.ru>, status=expired, returned to sender'
    parser._parse_data(data3)
    assert parser.users['karepova@start-cbs.ru'].failed_mails == 1
    assert parser.users['karepova@start-cbs.ru'].sent_mails == 2

    data4 = 'Jul 10 13:23:50 srv24-s-st postfix/qmgr[3043]: EC1ECDF0510: removed'
    parser._parse_data(data4)
    assert parser.ids == {}
