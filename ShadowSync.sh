#!/bin/bash
PIBOT_DIR=~/pibot/tiddlyServer
GIT_DIR=./pi/tiddlyServer

while [ 1 ]; do
  rsync --archive --delete --itemize-changes --exclude="__pycache__" --exclude="blocklyTemp"  ${GIT_DIR}/  ${PIBOT_DIR}/
  sleep 1
done
