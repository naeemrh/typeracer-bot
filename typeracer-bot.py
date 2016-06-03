from SendKeys import SendKeys
from time import sleep
sleep(3)

text = """<text here>"""

SendKeys(text, pause = 0.05, with_spaces = True)
