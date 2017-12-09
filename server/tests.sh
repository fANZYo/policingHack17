#!/bin/sh

HOST="http://127.0.0.1:5000"

# Using CURL to test the API. 
echo "\n-> No JSON"
curl -X POST $HOST/createCrime
echo "\n-> test empty JSON"
curl -H "Content-Type: application/json" -X POST -d '{}' $HOST/createCrime
echo "\n-> Random JSON"
curl -H "Content-Type: application/json" -d '{"hello":"world"}' $HOST/createCrime
echo "\n-> Valid input"
curl -H "Content-Type: application/json" -d '{"officer":"me","title":"AAA","description":"AA"}' $HOST/createCrime
echo "\n-> Add something to the list"
curl -H "Content-Type: application/json" -d '{"uuid":"61efe834eee37d49fd3fcc3740e521b3297215de3005fd652866a6adecf29edd","title":"me","description":"AA","state":"fun"}' $HOST/updateCrime
echo "\n-> list reports"
curl $HOST/listReports
echo "\n-> update meta"
curl -H "Content-Type: application/json" -d '{"uuid":"61efe834eee37d49fd3fcc3740e521b3297215de3005fd652866a6adecf29edd","title":"testnow"}' $HOST/updateMeta
