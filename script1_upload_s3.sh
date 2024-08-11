#!/bin/sh
set -o nounset
set -o errexit
set -o xtrace


echo "Uploading listardynamo.zip to s3"
aws s3 cp $(pwd)/listardynamo/listardynamo.zip s3://s3demomanve/code/listardynamo.zip
sleep 5

echo "Uploading listars3.zip to s3"
aws s3 cp $(pwd)/listars3/listars3.zip s3://s3demomanve/code/listars3.zip
sleep 5

echo "Uploading index.html to s3"
aws s3 cp $(pwd)/cloudfront/index.html s3://s3demomanve/index.html