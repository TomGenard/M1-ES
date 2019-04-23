set title "Segment OM"
set grid

set xlabel "x"
set ylabel "y"
xmax=20.0
xmin=-20.0
ymin=-20.0
ymax=20.0

set xrange [xmin:xmax]
set yrange [ymin:ymax]
set size ratio -1

plot 'prng_circle.data' using 1:2 with points pt 6 ps 0.5
pause -1 "Hit [Enter]..."

set terminal pdfcairo
set output "prng_rectangle.pdf"
replot
set output
set terminal wxt

## end