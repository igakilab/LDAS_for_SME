# -*- coding: utf-8 -*-
import pyinotify

wm = pyinotify.WatchManager()  # Watch Manager

mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY  # watched events


class EventHandler(pyinotify.ProcessEvent):
    
    def process_IN_CREATE(self, event):
	#ファイルが作成された時に呼ばれる
	print event
	print "Create:", event.pathname

    def process_IN_DELETE(self, event):
        #ファイルが削除された時に呼ばれる
        print event
        print "Delete:", event.pathname

    def process_IN_MODIFY(self, event):
	#ファイルが編集された時に呼ばれる
        print event
        print "Modify:", event.pathname


handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('./etc', mask, rec=True)
notifier.loop()
