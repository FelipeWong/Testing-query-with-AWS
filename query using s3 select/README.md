Put the following script into the EC2 userdata:
<pre><code>curl ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz -o access_log.gz
gunzip access_log.gz
iconv -c -t UTF8 access_log -o access_log_utf8
aws s3 cp access_log s3://${Your-Bucket}/access_log
aws s3 cp access_log_utf8 s3://${Your-Bucket}/access_log_utf8
</pre></code>

Run the following AWS CLI:
<pre><code>aws s3api select-object-content \
    --bucket ${Your-Bucket} \
    --key access_log_utf8 \
    --expression "SELECT COUNT(*) FROM s3object s;" \
    --expression-type 'SQL' \
    --input-serialization '{"CSV": {}, "CompressionType": "NONE"}' \
    --output-serialization '{"CSV": {}}' "q1.csv"
</pre></code>

or run the python script:
<pre><code>python3 total_count
</pre></code>