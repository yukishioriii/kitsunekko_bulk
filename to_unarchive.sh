#!/bin/bash
echo "moving zzz"
mv "test/*.ass" unarchived/
mv "test/*.srt" unarchived/
echo "unrar-ing"
unrar e -r -o- "test/*.rar" "unarchived/"
echo "unzip-ing"
unzip -B "test/*.zip" -d "unarchived/"
echo "7zip-ing"
7za -y -aou x test/*.7z -ounarchived/
echo "done !"