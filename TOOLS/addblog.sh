#!/bin/bash
cd addblog
ls -1rt|grep md$ | while read line; do python blog_transform.py $line;done

#find 163md/ -name "*.md"| while read line; do echo "$line" ;./add163md.py "$line";done
