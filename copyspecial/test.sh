#!/bin/bash
# test for copyspecial.py

cd ~/workspace/copyspecial
rm -rf ~/workspace/copyspecial/foo
~/workspace/copyspecial/copyspecial.py .
echo
~/workspace/copyspecial/copyspecial.py --todir foo/copy .
tree foo
rm -rf ~/workspace/copyspecial/foo
~/workspace/copyspecial/copyspecial.py --tozip foo/bar/myzip .
tree ~/workspace/copyspecial/foo
echo
cd foo/bar
unzip myzip.zip
echo
tree ~/workspace/copyspecial/foo
cd ~/workspace/copyspecial

