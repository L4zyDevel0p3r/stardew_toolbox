"""
MIT License

Copyright (c) 2021 MSProgrammerPy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from lxml import etree as ET
import os
from decorators import force_str

SAVES_PATH = os.path.join("C:\\Users", str(os.getlogin()), "AppData\\Roaming\\StardewValley\\Saves\\")


class ToolBox:
    def __init__(self, save_name: str):
        save_name = str(save_name)
        # Save Path
        self.save_path = os.path.join(SAVES_PATH, save_name + "\\")
        # SaveGameInfo
        self.sgi = "SaveGameInfo"
        # Farm file. e.g MyFarm_671651513
        self.ff = save_name

        self.read()

    @staticmethod
    def save_exists(name: str):
        """
        Checks if there is a save with the specified name.
        """
        save_path = os.path.join(SAVES_PATH, name + "\\")

        if os.path.exists(save_path):
            files = [file for file in os.listdir(save_path) if os.path.isfile(os.path.join(save_path, file))]

            if "SaveGameInfo" in files and name in files:
                return True

        return False

    def read(self):
        """
        Reads SaveGameInfo file and Farm file.
        """

        # Reading SaveGameInfo
        self._sgi_tree = ET.parse(os.path.join(self.save_path, self.sgi))
        self._sgi_root = self._sgi_tree.getroot()

        # Reading Farm file
        self._ff_tree = ET.parse(os.path.join(self.save_path, self.ff))
        self._ff_root = self._ff_tree.getroot()

    def save(self):
        """
        Saves SaveGameInfo file and Farm file.
        """

        self._sgi_tree.write(os.path.join(self.save_path, self.sgi), encoding="UTF-8", xml_declaration=True)
        self._ff_tree.write(os.path.join(self.save_path, self.ff), encoding="UTF-8", xml_declaration=True)

    @force_str
    def _update_sgi(self, key: str, value: str):
        """
        Use this function instead of repeating "self._sgi_root.find('key').text = value" in every function.
        """
        self._sgi_root.find(key).text = value

    @force_str
    def _update_ff(self, key: str, value: str):
        """
        Use this function instead of repeating "self._ff_root.find('player').find('key').text = value" in every function.
        """
        self._ff_root.find("player").find(key).text = value

    def get(self, key: str):
        return self._sgi_root.find(key).text

    def change_name(self, new_name: str):
        """
        Change character name.
        """

        self._update_sgi(key="name", value=new_name)
        self._update_ff(key="name", value=new_name)

    def change_farm_name(self, new_name: str):
        """
        Change farm name.
        """

        self._update_sgi(key="farmName", value=new_name)
        self._update_ff(key="farmName", value=new_name)

    def change_favorite_thing(self, value: str):
        """
        Change favorite thing.
        """

        self._update_sgi(key="favoriteThing", value=value)
        self._update_ff(key="favoriteThing", value=value)

    def change_money(self, value: str):
        """
        Change the character money to the specified value.
        """

        self._update_sgi(key="money", value=value)
        self._update_ff(key="money", value=value)

    def change_qicoins(self, value: str):
        """
        Change the character's Qi Coins (Club Coins) to the specified value.
        """

        self._update_sgi(key="clubCoins", value=value)
        self._update_ff(key="clubCoins", value=value)

    def change_qigems(self, value: str):
        """
        Change the character's Qi Gems to the specified value.
        """

        self._update_sgi(key="qiGems", value=value)
        self._update_ff(key="qiGems", value=value)
