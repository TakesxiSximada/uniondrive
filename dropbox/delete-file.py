#! /usr/bin/env python
import os
import dropbox

access_token = os.environ['UNIONDRIVE_DROPBOX_ACCESS_TOKEN']

dbx = dropbox.Dropbox(access_token)
res = dbx.files_delete('/test/text.txt')
print(res)
