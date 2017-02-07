require(ellipse)
open.png = function(name, width=3.05, height=2.8, units='in', resolution=300, points=9, xmin=0.15,xmax=0.99,ymin=0.17,ymax=0.99,plt=c(xmin,xmax,ymin,ymax), mgp=c(2.2,1,0), pch=".", ...) {
 png(name, width=width, height=height, pointsize=points, units=units, res=resolution)
 par(plt=plt, mgp=mgp, pch=pch, ...)
}
blue.shading = c("#89BAF5", "#DEEBFA")

Rosenbrock.lnP = function(x, y, a=1.0, b=100.0) -( (a-x)^2 + b*(y-x^2)^2 )
ros = expand.grid(x=seq(-2, 3, 0.0025), y=seq(0, 5, 0.0025))
ros$z = Rosenbrock.lnP(ros$x, ros$y)

eggbox.lnP = function(x,y) (2.0 + cos(0.5*x)*cos(0.5*y))^3
egg = expand.grid(x=seq(0, 30, 0.1), y=seq(0, 30, 0.1))
egg$z = eggbox.lnP(egg$x, egg$y)

open.png('mc2_rosenbrock.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98, ymax=0.98)
par(xaxs='i', yaxs='i')
contour(unique(ros$x), unique(ros$y), -2*matrix(ros$z, length(unique(ros$y))), lev=qchisq(pchisq((1:3)^2, 1), 2), col='darkblue', drawlabels=F, xlab='x', ylab='y')
points(ros[which.max(ros$z),1:2], col=2, pch=4, cex=0.5)
dev.off()

open.png('mc2_eggbox.png', resolution=200, height=2.8, xmin=0.175, ymin=0.175, xmax=0.97, ymax=0.97)
par(xaxs='i', yaxs='i')
contour(unique(egg$x), unique(egg$y), -2*matrix(egg$z-max(egg$z), length(unique(egg$y))), lev=qchisq(pchisq((1:3)^2, 1), 2), col='darkblue', drawlabels=F, xlab='x', ylab='y')
dev.off()

open.png('mc2_slice.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98)
par(xaxs='i', yaxs='i')
plot(1, 1, type='n', axes=F, xlim=c(0, 17), ylim=c(0, 0.265), xlab=expression(theta), ylab=expression(P(theta)))
curve(dchisq(x,3), add=T)
xx = seq(0, 5, len=1000)
yy = dchisq(xx,3)
j = which(yy >= 0.11)
points(xx[j], yy[j], type='l', col=4, lwd=1.5)
segments(xx[j][1], 0.11, x1=xx[rev(j)][1], lty=2)
##polygon(xx, dchisq(xx,3), col=blue.shading[2], border=4)
points(2, dchisq(2,3), pch=19)
axis(1)
axis(2)
box()
mtext(expression(theta[0]), 1, at=2.2, line=0.1)
arrows(2, 0, y1=0.11, code=3, length=0.1)
text(2.4, 0.055, 'q')
dev.off()

yy = c(rexp(300000), sqrt(rchisq(600000, 2)/2))
h = hist(yy, breaks=100, plot=F)
open.png('mc2_steplength.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98)
par(xaxs='i', yaxs='i')
plot(1, 1, type='n', xlim=c(0, 3.99), ylim=c(0, 0.9), xlab='|y-x|/s', ylab='Q(|y-x|/s)')
curve(2*dnorm(x), add=T)
points(c(0, h$mids), c(0.33, h$density), type='l', col=4)
dev.off()

open.png('mc2_reparam0.png', resolution=200, xmin=0.16)
plot(ellipse(0.9, lev=pchisq(0.25,1)), type='l', col='darkblue', xlab='x', ylab='y', xlim=c(-2,2), ylim=c(-2,2))
arrows(-1, 0, x1=1, length=0.1, code=3)
arrows(0, -1, y1=1, length=0.1, code=3)
dev.off()

open.png('mc2_reparam1.png', resolution=200, xmin=0.16)
plot(ellipse(0, lev=pchisq(0.25,1)), type='l', col='darkblue', xlab=expression(x*minute), ylab=expression(y*minute), xlim=c(-2,2), ylim=c(-2,2))
arrows(-1, 0, x1=1, length=0.1, code=3)
arrows(0, -1, y1=1, length=0.1, code=3)
dev.off()

open.png('mc2_reparam2.png', resolution=200, xmin=0.16)
plot(ellipse(0.9, lev=pchisq(0.25,1)), type='l', col='darkblue', xlab='x', ylab='y', xlim=c(-2,2), ylim=c(-2,2))
y = 0.96
arrows(-y, -y*0.99, x1=y, y1=y*0.99, length=0.1, code=3)
y = 0.217
arrows(y*0.85, -y*1.05, x1=-y*0.85, y1=y*1.05, length=0.1, code=3)
dev.off()

open.png('mc2_reparam3.png', resolution=200, xmin=0.16)
plot(ellipse(0.9, lev=pchisq(0.25,1)), type='l', col='darkblue', xlab='x (fast)', ylab='y (slow)', xlim=c(-2,2), ylim=c(-2,2))
y = 0.96
arrows(-y, -y*0.99, x1=y, y1=y*0.99, length=0.1, code=3)
y = 0.42
arrows(-y, 0, x1=y, length=0.1, code=3)
dev.off()



post = function(x, y, sx=1, sy=1, r=-0.75) -0.5/(1-r^2)*( (x/sx)^2 + (y/sy)^2 -2*r*(x/sx)*(y/sy) ) 

metro = matrix(NA, 1000, 2)
metro[1,] = c(3,3)
lnp = post(metro[1,1], metro[1,2])
for (i in 2:nrow(metro)) {
    prop = metro[i-1,] + rnorm(ncol(metro), 0, 0.5)
    lnp.prop = post(prop[1], prop[2])
    if (log(runif(1)) <= lnp.prop-lnp) {
        lnp = lnp.prop
        metro[i,] = prop
    } else {
        metro[i,] = metro[i-1,]
    }
}

gibbs = metro
r = -0.75; sx=1; sy=1
for (i in 2:nrow(gibbs)) {
    if (i %% 2 == 0) {
        gibbs[i,] = c(rnorm(1, r*sx/sy*gibbs[i-1,2], sx*sqrt(1-r^2)), gibbs[i-1,2])
    } else {
        gibbs[i,] = c(gibbs[i-1,1], rnorm(1, r*sy/sx*gibbs[i,1], sy*sqrt(1-r^2)))
    }
}

open.png('mc2_metro.png', resolution=200, height=2.5, xmin=0.16, ymin=0.19)
j = 1:26
plot(metro[j,1], metro[j,2], col=cmap.blue.red(stretch(j)), pch=20, xlim=c(-4,4), ylim=c(-4,4), xlab=expression(theta[1]), ylab=expression(theta[2]))
segments(metro[j[-length(j)],1], metro[j[-length(j)],2], x1=metro[j[-1],1], y1=metro[j[-1],2], col=cmap.blue.red(stretch(j)))
points(ellipse(-0.75, lev=pchisq(1,1)), type='l', col=1)
points(ellipse(-0.75, lev=pchisq(4,1)), type='l', col=1)
dev.off()

open.png('mc2_gibbs.png', resolution=200, height=2.5, xmin=0.16, ymin=0.19)
j = seq(1,51,2)
plot(gibbs[j,1], gibbs[j,2], col=cmap.blue.red(stretch(j)), pch=20, xlim=c(-4,4), ylim=c(-4,4), xlab=expression(theta[1]), ylab=expression(theta[2]))
j = 1:51
segments(gibbs[j[-length(j)],1], gibbs[j[-length(j)],2], x1=gibbs[j[-1],1], y1=gibbs[j[-1],2], col=cmap.blue.red(stretch(j)))
points(ellipse(-0.75, lev=pchisq(1,1)), type='l', col=1)
points(ellipse(-0.75, lev=pchisq(4,1)), type='l', col=1)
dev.off()
