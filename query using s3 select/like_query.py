#!/usr/bin/env/env python3
import boto3

s3 = boto3.client('s3',
                  region_name='us-east-1')

r = s3.select_object_content(
    Bucket='abc882021',
    Key='access_log_utf8',
    ExpressionType='SQL',
    Expression="SELECT s._1 FROM S3Object s WHERE (s._1 LIKE '%.com') LIMIT 5",
    # Expression="SELECT MAX(s._1) FROM s3object s WHERE (s._3 LIKE '%18/Aug%') OR (s._3 LIKE '%19/Aug%') OR (s._3 LIKE '%20/Aug%')",
    RequestProgress={
        'Enabled': True
    },
    InputSerialization={
        'CSV': {
            "FileHeaderInfo": "NONE",
            'FieldDelimiter': '-',
            'AllowQuotedRecordDelimiter': True
        },
        'CompressionType': 'NONE',
    },
    OutputSerialization={'CSV': {}},
)

for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")
        print(statsDetails['BytesScanned'])
        print("Stats details bytesProcessed: ")
        print(statsDetails['BytesProcessed'])
