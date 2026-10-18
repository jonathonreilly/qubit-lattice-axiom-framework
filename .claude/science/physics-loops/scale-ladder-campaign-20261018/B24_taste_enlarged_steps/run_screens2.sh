#!/bin/bash
cd "$(dirname "$0")"
while pgrep -f "b24_screen.py mix2:4,5,6" > /dev/null; do sleep 5; done
for tag in taste:A taste:B,C taste:D,E taste:F; do
  f=screen_$(echo $tag | tr ':,' '_-').log
  timeout 1500 python3 b24_screen.py $tag 4 > $f 2>&1
done
