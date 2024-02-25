#!/bin/bash

echo "Running chilli bot on port 5006"
cd chilli/
rasa run actions -p 5056 &
rasa run -m models --enable-api --cors "*" -p 5006 &

echo "Running chilli punjabi bot on port 5007"
cd ../chilli-pun
rasa run actions -p 5057 &
rasa run -m models --enable-api --cors "*" -p 5007 &

echo "Running citrus bot on port 5008"
cd ../citrus
rasa run actions -p 5058 &
rasa run -m models --enable-api --cors "*" -p 5008 &

echo "Running citrus punjabi bot on port 5009"
cd ../citrus-pun
rasa run actions -p 5059 &
rasa run -m models --enable-api --cors "*" -p 5009 &

echo "Running garlic bot on port 5010"
cd ../garlic
rasa run actions -p 5060 &
rasa run -m models --enable-api --cors "*" -p 5010 &

echo "Running garlic punjabi bot on port 5011"
cd ../garlic-pun
rasa run actions -p 5061 &
rasa run -m models --enable-api --cors "*" -p 5011 &

echo "Running guava bot on port 5012"
cd ../guava
rasa run actions -p 5062 &
rasa run -m models --enable-api --cors "*" -p 5012 &

echo "Running guava punjabi bot on port 5013"
cd ../guava-pun
rasa run actions -p 5063 &
rasa run -m models --enable-api --cors "*" -p 5013 &

echo "Running pea bot on port 5014"
cd ../pea
rasa run actions -p 5064 &
rasa run -m models --enable-api --cors "*" -p 5014 &

echo "Running pea punjabi bot on port 5015"
cd ../pea-pun
rasa run actions -p 5065 &
rasa run -m models --enable-api --cors "*" -p 5015 &

echo "Running rice bot on port 5016"
cd ../rice
rasa run actions -p 5066 &
rasa run -m models --enable-api --cors "*" -p 5016 &

echo "Running rice punjabi bot on port 5017"
cd ../rice-pun
rasa run actions -p 5067 &
rasa run -m models --enable-api --cors "*" -p 5017 &

echo "Running wheat bot on port 5018"
cd ../wheat
rasa run actions -p 5068 &
rasa run -m models --enable-api --cors "*" -p 5018 &

echo "Running wheat punjabi bot on port 5019"
cd ../wheat-pun
rasa run actions -p 5069 &
rasa run -m models --enable-api --cors "*" -p 5019 &