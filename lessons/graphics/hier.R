open.png = function(name, width=3.05, height=2.8, units='in', resolution=300, points=9, xmin=0.15,xmax=0.99,ymin=0.17,ymax=0.99,plt=c(xmin,xmax,ymin,ymax), mgp=c(2.2,1,0), pch=".", ...) {
 png(name, width=width, height=height, pointsize=points, units=units, res=resolution)
 par(plt=plt, mgp=mgp, pch=pch, ...)
}
shading = c("#41AA41", "#82E682") #c("#89BAF5", "#DEEBFA")

lfn = function(L, L.star=1, phi.star=1, alpha=-1.25) phi.star * (L/L.star)^alpha * exp(-L/L.star)

open.png('hier_lumfcn.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98)
curve(lfn(x), 0.1, 10, log='xy', xlab=expression(L/L*"*"), ylab='n(L)  (arbitrary units)', axes=F, col='darkblue')
axis(1)
axis(2, at=10^seq(-5,1,2), lab=c(expression(10^-5), expression(10^-3), expression(10^-1), expression(10^1)))
box()
dev.off()
