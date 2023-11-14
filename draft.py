import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers.fields import FieldsWebElement
from helpers.assertions import Assertion
from conftest import *
from data.user import TEST_USER


for i in range(1, 43):
    b = f'(//*[@class="styles_sitemapItem__Novv5"])[{i}]'
    print(b)







