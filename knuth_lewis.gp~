set grid

xmax=2**32
xmin=0
ymin=0

set xrange [xmin:xmax]
set yrange [ymin:*]

binwidth=xmax/100
bin(x,width)=width*floor(x/width)

plot 'prng_knuth_lewis_histo.data' using (($1)+0.5*binwidth):($3)\
     notitle with histeps lt 3 lw 2
pause -1 "Hit [Enter]..."

set terminal pdfcairo
set output "prng_knuth_lewis.pdf"
replot
set output
set terminal wxt

## end