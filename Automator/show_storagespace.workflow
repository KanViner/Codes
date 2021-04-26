export PATH=/usr/local/bin:$PATH;
result=$(df -h -l | grep -v '/private/var/\|Filesystem' | tr -s ' ' | cut -d' ' -f1,2,3,4,5);
osascript -e "display alert \"show_storagespace\" message \"$result\""
