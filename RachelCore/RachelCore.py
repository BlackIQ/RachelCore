"""
    RachelCore

    Amirhossein Mohammadi

    https://github.com/BlackIQ/Rachel
    https://github.com/BlackIQ/RachelCore
"""

import os
import webbrowser
import googlesearch
from time import *
import random
import requests

class dt:
    """
        Date and Time class
        It this class there are date methods, time methods
    """

    @staticmethod
    def Date():
        # Returns Date
        print()

    @staticmethod
    def Time():
        # Returns Time
        print()


class start:
    """
        Star class
        In this class there are start methods
    """

    @staticmethod
    def start():
        # Returns somethings for start
        print()

    @staticmethod
    def hello():
        # Returns answers fot hello
        print()

class close:
    """
        Close class
        Here are methods for ending app
    """

    @staticmethod
    def bye():
        # Returns answers for bye
        print()

    @staticmethod
    def Goodnight():
        # Returns answers for goodnight
        print()

    @staticmethod
    def Sleep():
        # Returns answers for gn
        print()


class cli:
    """
        CLI class
        We have cli stuff here. Like clear or change bg color
    """

    @staticmethod
    def clear():
        os.system("clear")


class software:
    """
        Software class
        Uninstall, Update and other software methods are here
    """

    version = 'Version'

    @staticmethod
    def uninstall():
        # Uninstalling
        print()

    @staticmethod
    def update():
        # Updating
        print()


def search_in_net(text):
    results = googlesearch.search(text)
    i = 0
    for result in results:
        print(f"[{i}]" + result)
        i += 1
    num = input('\n[?] Insert number to open url in browser : ')
    if num:
        webbrowser.open(results[int(num)])
    return ''