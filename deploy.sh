#!/usr/bin/env bash


echo "$TRAVIS_BRANCH"
echo "$TRAVIS_EVENT_TYPE" 

if [ "master" == "$TRAVIS_BRANCH" ] && [ "$TRAVIS_EVENT_TYPE" == "push" ]; then
	echo "Build was triggered by push to master ";
else
  echo "Build was not triggered by push to master";
fi