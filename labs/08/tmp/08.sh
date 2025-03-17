#!/bin/bash

mkdir -p ./a/b/c/d
touch ./a/foo.txt
touch ./a/b/foo.txt
touch ./a/b/c/foo.txt
touch ./a/b/c/d/foo.txt

chgrp mail ./a/foo.txt

chmod 777 ./a/foo.txt
chmod 077 ./a/b/foo.txt
chmod 660 ./a/b/c/foo.txt
umask

whoami

groups

cat ./a/foo.txt
cat ./a/b/foo.txt

chmod ug-rwx ./a/b/c/d
find ./a -name "*.txt" -exec ls -alF {} \;

chmod u+rwx ./a/b/c/d
find ./a -name "*.txt" -exec ls -alF {} \;

rm -rf ./a
