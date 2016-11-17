open.png = function(name, width=3.05, height=2.8, units='in', resolution=300, points=9, xmin=0.15,xmax=0.99,ymin=0.17,ymax=0.99,plt=c(xmin,xmax,ymin,ymax), mgp=c(2.2,1,0), pch=".", ...) {
 png(name, width=width, height=height, pointsize=points, units=units, res=resolution)
 par(plt=plt, mgp=mgp, pch=pch, ...)
}

open.png('bayes_poissoneg_likelihood.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98)
par(yaxs='i')
xx = 0:15
plot(xx, dpois(xx, 0.5), col=2, pch=1, ylim=c(0,0.65), xlab='N', ylab=expression(P(N*group("|",mu,""))))
points(xx, dpois(xx, 2), col='forestgreen', pch=2)
points(xx, dpois(xx, 7), col=4, pch=3)
legend('topright', c(expression(mu==0.5), expression(mu==2), expression(mu==7)), inset=0.02, col=c(2,'forestgreen',4), pch=1:3)
dev.off()

open.png('bayes_poissoneg_prior.png', resolution=200, height=2.5, xmin=0.175, ymin=0.19, xmax=0.98)
par(xaxs='i', yaxs='i')
curve(0*x+1, col=2, xlim=c(0,50), ylim=c(0,2), xlab=expression(mu), ylab=expression(P(mu)), axes=F)
axis(1, at=c(0,50), lab=c(0, expression(infinity)))
axis(2, at=1, lab=expression(epsilon))
box()
dev.off()

curve(dgamma(x, shape=1, rate=0.00), 0, 10)
