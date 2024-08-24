import os
import sys
import threading

import boto3

s3 = boto3.client('s3')

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


s3.upload_file(
    r'C:\Users\BarryAwure\Downloads\HOP School of HArvest (HSH) Training Manual - Module 1.pdf', 
    'my-unique-bucket-name-49', 'HOP School of HArvest (HSH) Training Manual - Module 1.pdf',
    Callback=ProgressPercentage('HOP School of HArvest (HSH) Training Manual - Module 1.pdf')
)