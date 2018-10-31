#!/bin/bash

python main.py -r 79 -s /home/tamutamu/ -d /tmp/backups/ \
  -e "\/home\/tamutamu\/\.m2.*$" \
  -e "\/home\/tamutamu\/\.pyenv.*$" \
  -e "\/home\/tamutamu\/\.rbenv.*$" \
  -e "\/home\/tamutamu\/\.cache.*$" \
  -e "\/home\/tamutamu\/\.gem.*$" \
