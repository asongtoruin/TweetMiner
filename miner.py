#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from glob import glob

import tweepy

class Miner:
    def __init__(self, key_folder='keys'):
        # Set up authorisation
        self.auth = self.__authourise(key_folder)

        # Intiialise API
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)

    @staticmethod
    def __read_first_line(file_path):
        with open(file_path) as f:
            first_line = f.read().splitlines()[0].strip()
        return first_line

    def __get_key(self, key_folder, key_name):
        key_path = path.join(key_folder, key_name)
        if path.isfile(key_path):
            return self.__read_first_line(key_path)
        else:
            for wildcard_path in glob(key_path + '.*'):
                return self.__read_first_line(wildcard_path)

    def __authourise(self, key_folder):
        key_names = ('consumer_key', 'consumer_secret',
                     'access_token', 'access_token_secret')
        keys = {k: self.__get_key(key_folder, k) for k in key_names}

        auth = tweepy.OAuthHandler(keys['consumer_key'],
                                   keys['consumer_secret'])
        auth.set_access_token(keys['access_token'], keys['access_token_secret'])

        return auth

if __name__ == '__main__':
    tm = Miner()
    print(tm.api)