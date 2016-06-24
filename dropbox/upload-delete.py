#! /usr/bin/env python
"""
filename: UUID/name.txt
chunk:    UUID/0.chunk
chunk:    UUID/1.chunk
chunk:    UUID/2.chunk
...

"""
import io
import itertools
import os
import shutil
import time
import uuid

import dropbox

bucket_name = '/YOUR_BUCKET_NAME'

token = os.environ['UNIONDRIVE_DROPBOX_ACCESS_TOKEN']
dbx = dropbox.Dropbox(token)

chunk_size = 100 * 1024 * 1024  # 100MB

dbx.files_create_folder(bucket_name)
for entry in os.scandir('.'):
    if entry.is_file():
        code = uuid.uuid4().hex
        target_path = os.path.join(bucket_name, code)
        dbx.files_create_folder(target_path)

        with io.BytesIO(entry.name.encode()) as fp:
            fp.seek(0)
            name_path = os.path.join(target_path, 'name.txt')
            dbx.files_upload(fp, name_path)

        with open(entry.name, 'rb') as fp:
            for ii in itertools.count():
                buf = fp.read(chunk_size)
                if not buf:  # empty
                    break

                dp = io.BytesIO(buf)
                dp.seek(0)
                chunk_path = os.path.join(
                    target_path, '{}.chunk'.format(ii))
                dbx.files_upload(dp, chunk_path)

    shutil.move(entry.name, 'trash')
    print('{} -> OK'.format(entry.name))
    time.sleep(1)
