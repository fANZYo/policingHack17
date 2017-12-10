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
curl -H "Content-Type: application/json" -d '{"officer":"me","name":"AAA","description":"AA"}' $HOST/createCrime
echo "\n-> Add something to the list"
curl -v -H "Content-Type: application/json" -d '{"crimeID":"899c8df4e956334979f94acbf29800b5c79a1a1ee1a27859d45e24d3f890707e","name":"I cant belive this!","description":"AA","state":"fun"}' $HOST/updateCrime
echo "\n-> list reports"
curl $HOST/listReports
echo "\n-> update meta"
curl -H "Content-Type: application/json" -d '{"crimeID":"000001","name":"Did You See This Coming?"}' $HOST/updateMeta
#curl -H "Content-Type: application/json" -d '{"crimeID":"61efe834eee37d49fd3fcc3740e521b3297215de3005fd652866a6adecf29edd"}' $HOST/deleteReport
curl -H "Content-Type: application/json" -d '{"crimeID":"fdf627342438304b0c962bc4251bc998353d1f538238dcc7ca4dd9d565a2c5ea","uuidState":"6c30aa9f91ce685e529a82599990a53ddb634ad975706943df017e2e55aee1e2"}' $HOST/deleteState
curl $HOST/listReports
