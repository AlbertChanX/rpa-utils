import re
import logging
import pytest
from pprint import pprint

from rpa_utils import web

logging.basicConfig(level=logging.DEBUG)


class Test:
    """
    pytest -s test_decompile.py::Test::test_decompile
    """

    def test_decompile(self):
        files = {'pyc': open('ierror.cpython-36.pyc', 'rb')}
        res = web.custom_request('http://tools.bugscaner.com/api/decompyle/', 'POST', files=files)
        assert isinstance(res, dict)
        code = res['info']
        reg = re.compile(r'<pre.*?>(.*?)</pre>', re.S)
        res = re.findall(reg, code)
        pprint(res[0])
        codes = res[0]
        with open('pycode.py', 'w', encoding='utf-8') as f:
            codes = codes.encode('utf-8').decode('unicode_escape')
            codes = codes.splitlines()
            for line in codes[6:]:
                f.writelines(line + '\n')


if __name__ == '__main__':
    pytest.main()
