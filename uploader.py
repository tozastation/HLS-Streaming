# Import Minio library.
import os
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio(
    '127.0.0.1:9000',
    access_key='hogehoge',
    secret_key='hogehoge',
    secure=False
    )
# Make a bucket with the make_bucket API call.
try:
    minioClient.make_bucket("canon", location="")
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    raise

try:
    hlsList = os.listdir(os.getcwd()+"/output")
    for a in hlsList:
        minioClient.fput_object('canon', a, './output/'+a)
except ResponseError as err:
    print(err)