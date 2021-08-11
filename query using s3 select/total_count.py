#!/usr/bin/env/env python3
import boto3

s3 = boto3.client('s3',
                  region_name='us-east-1')

r = s3.select_object_content(
    Bucket='abc882021',
    Key='access_log_utf8',
    ExpressionType='SQL',
    Expression="SELECT COUNT(*) FROM s3object s",
    RequestProgress={
        'Enabled': True
    },
    InputSerialization={
        'CSV': {
            "FileHeaderInfo": "NONE",
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
