#! /usr/bin/env python
import os
import dropbox

access_token = os.environ['UNIONDRIVE_DROPBOX_ACCESS_TOKEN']

dbx = dropbox.Dropbox(access_token)
# res = dbx.files_download('/test/text.txt')
res = dbx.files_download_to_file('text.txt', '/test/text.txt')
print(res)
