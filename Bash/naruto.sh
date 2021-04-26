cd ~/Movies/Naruto/to_convert
for f in *.mkv
do
  filename="${f%%.*}";
  echo "<START  ----  $filename  ----  START>";
  ffmpeg -i "${filename}.mkv" -i "a_2x2_1_220/${filename}.mka" -i "a_eng_1_220/${filename}.mka" -i "s_2ndlife_1_101/${filename}.ass" -i "s_alexjulia_1_220/${filename}.ass" -c copy -map 0:v:0 -map 1:a:0 -map 2:a:0 -map 0:a:0 -map 3:s:0 -map 4:s:0 "../${filename}.mkv";
  rm "./${filename}.mkv";
done
echo "<COMPLETE  ----  +*+*+*+* *+*+*+*+  ----  COMPLETE>"
read exit_var
