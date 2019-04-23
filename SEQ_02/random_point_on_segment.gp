set title "Segment OM"
set grid

set xlabel "x"
set ylabel "y"
xmax=10.0
xmin=0
ymin=0
ymax=10.0

set xrange [xmin:xmax]
set yrange [ymin:ymax]

plot 'random_segments_data.csv' using 1:2 with points pt 6 ps 0.5
pause -1 "Hit [Enter]..."

set terminal pdfcairo
set output "prng_segment.pdf"
replot
set output
set terminal wxt

## end