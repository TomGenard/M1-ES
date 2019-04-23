set title "Segment OM"
set grid

set xlabel "x"
set ylabel "y"
xmax=100.0
xmin=0
ymin=0
ymax=40.0

set xrange [xmin:xmax]
set yrange [ymin:ymax]

binwidth=xmax/100
bin(x,width)=width*floor(x/width)

plot 'sim_file.data' using 1:2 with points pt 6 ps 0.5
pause -1 "Hit [Enter]..."

set terminal pdfcairo
set output "sim_file.pdf"
replot
set output
set terminal wxt

## end