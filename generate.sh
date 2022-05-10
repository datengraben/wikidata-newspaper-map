#! /bin/bash

echo "<!DOCTYPE html>" \
     $(cat head.html) \
     "<body>" \
     $(cat header.html) \
     $(cat generated-index.html) \
     $(cat scripts.html) \
     "</body></html>" > show.html
