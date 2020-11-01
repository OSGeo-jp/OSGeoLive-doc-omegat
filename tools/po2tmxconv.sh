#!/bin/sh
for i in source/*.po; do
 po2tmx -l ja $i tm/`basename -s .po $i`.tmx
done

for i in source/overview/*.po; do
 po2tmx -l ja $i tm/overview--`basename -s .po $i`.tmx
done

for i in source/quickstart/*.po; do
 po2tmx -l ja $i tm/quickstart--`basename -s .po $i`.tmx
done
