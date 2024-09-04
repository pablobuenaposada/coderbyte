import boto3
from botocore import UNSIGNED
from botocore.client import Config

BUCKET_NAME = "coderbytechallengesandbox"
PREFIX = "__cb__"
TOKEN = "awn51gvi3d"

s3 = boto3.resource("s3", config=Config(signature_version=UNSIGNED))
bucket = s3.Bucket(BUCKET_NAME)

for obj in bucket.objects.filter(Prefix=PREFIX):
    print(
        "".join(
            [
                "X" if (i + 1) % 3 == 0 else char
                for i, char in enumerate(
                    f'{obj.get()["Body"].read().decode("utf-8")}{TOKEN}'
                )
            ]
        )
    )
    break