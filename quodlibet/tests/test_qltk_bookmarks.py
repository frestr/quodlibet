# -*- coding: utf-8 -*-
# Copyright 2012 Christoph Reiter
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from senf import fsnative

from tests import TestCase

from quodlibet.qltk.bookmarks import EditBookmarks, MenuItems
from quodlibet.player.nullbe import NullPlayer
from quodlibet.library import SongLibrary
from quodlibet.formats import AudioFile
from quodlibet import config


class TBookmarks(TestCase):
    def setUp(self):
        config.init()
        player = NullPlayer()
        song = AudioFile()
        song.bookmarks = [(10, "bla")]
        song.sanitize(fsnative(u"/"))
        player.song = song
        self.player = player

    def tearDown(self):
        self.player.destroy()
        config.quit()

    def test_edit_window(self):
        EditBookmarks(None, SongLibrary(), self.player).destroy()

    def test_menu_items(self):
        MenuItems(self.player.song.bookmarks, self.player, False)
