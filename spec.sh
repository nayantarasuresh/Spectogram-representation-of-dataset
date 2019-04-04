for file in *.wav
do
    outfile="${file%.*}.png"
    sox "$file" -n spectrogram -o "$outfile"
done
