import check50
from re import escape

@check50.check()
def exists():
    """bank.py exists"""
    check50.exists("helloplus.py")

@check50.check(exists)
def testHello():
    """input of \"Rick\" yields output of Hello Rick! I am delighted to meet you"""
    input = "Rick"
    output = "Hello Rick! I am delighted to meet you"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


