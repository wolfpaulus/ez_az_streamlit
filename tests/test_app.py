"""
Test the app module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest
from app import ui


class Test(TestCase):
    at = AppTest.from_file("./src/app.py")
    at.run()
    print(at)
    assert at.title[0].value == "Streamlit Demo"
    assert at.subheader[0].value.startswith("..")
    assert not at.exception