#!/bin/sh

curl -F file=@"$1" -F channels=#general -F token=<YOUR_API_TOKEN> -F title="$2" -F filename="dailybash" https://slack.com/api/files.upload
