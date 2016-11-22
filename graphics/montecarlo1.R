open.png = function(name, width=3.05, height=2.8, units='in', resolution=300, points=9, xmin=0.15,xmax=0.99,ymin=0.17,ymax=0.99,plt=c(xmin,xmax,ymin,ymax), mgp=c(2.2,1,0), pch=".", ...) {
 png(name, width=width, height=height, pointsize=points, units=units, res=resolution)
 par(plt=plt, mgp=mgp, pch=pch, ...)
}
blue.shading = c("#89BAF5", "#DEEBFA")


open.png('mc1_rejection.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98)
par(xaxs='i', yaxs='i')
plot(1, 1, type='n', axes=F, xlim=c(0, 17), ylim=c(0, 0.265), xlab='x', ylab='')
xx = seq(0, 20, len=1000)
polygon(xx, dchisq(xx,3), col=blue.shading[2], border=4)
curve(pi*dnorm(x,0,5), add=T, col=2)
segments(4, 0, y1=dchisq(4,3))
segments(4, dchisq(4,3), y1=pi*dnorm(4,0,5), lty=2)
points(4, 0.08, pch=19)
axis(1)
axis(2)
box()
legend('topright', c(expression(p(x)), expression(A~g(x))), inset=0.02, lty=1, col=c(4,2))
arrows(3.25, 0, y1=0.08, code=3, length=0.1)
text(2.8, 0.04, 'u')
mtext(expression(phantom(minute)*x*minute), 1, at=4, line=0)
dev.off()


N = 50
x = exp(1.0) + rnorm(N)
y = pi + 1.6818*x + rnorm(N)
plot(x,y)
write.table(data.frame(x, y), '../code/mc1_sandbox.dat', row.na=F, col.na=F)


## NB the chain files used here will not be repo'd
ch = lapply(1:4, function(i) read.table(paste0('../code/mc1_sandbox_', i, '.txt'), head=F))
open.png('mc1_sandbox_ab.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98)
plot(1, 1, type='n', xlim=c(-3,5), ylim=c(-3,5), xlab='a', ylab='b')
for (i in 1:4) points(ch[[i]], type='l', col=i+1)
dev.off()
open.png('mc1_sandbox_a.png', resolution=200, height=2.5, width=5, xmin=0.1, ymin=0.2, xmax=0.98)
plot(1, 1, type='n', xlim=c(1,10000), ylim=c(-3,5), xlab='step', ylab='a')
for (i in 1:4) points(ch[[i]][,1], pch='.', col=i+1)
dev.off()
open.png('mc1_sandbox_b.png', resolution=200, height=2.5, width=5, xmin=0.1, ymin=0.2, xmax=0.98)
plot(1, 1, type='n', xlim=c(1,10000), ylim=c(-3,5), xlab='step', ylab='b')
for (i in 1:4) points(ch[[i]][,2], pch='.', col=i+1)
dev.off()
open.png('mc1_sandbox_acf-a.png', resolution=200, height=2.5, width=5, xmin=0.1, ymin=0.2, xmax=0.98)
acf(ch[[1]][-(1:2000),1], lag.max=1000, main='', ylab='autocorrelation of a')
dev.off()
open.png('mc1_sandbox_acf-b.png', resolution=200, height=2.5, width=5, xmin=0.1, ymin=0.2, xmax=0.98)
acf(ch[[1]][-(1:2000),2], lag.max=1000, main='', ylab='autocorrelation of b')
dev.off()
