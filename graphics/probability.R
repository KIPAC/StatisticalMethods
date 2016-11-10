require(ellipse)

open.png = function(name, width=3.05, height=2.8, units='in', resolution=300, points=9, xmin=0.15,xmax=0.99,ymin=0.17,ymax=0.99,plt=c(xmin,xmax,ymin,ymax), mgp=c(2.2,1,0), pch=".", ...) {
 png(name, width=width, height=height, pointsize=points, units=units, res=resolution)
 par(plt=plt, mgp=mgp, pch=pch, ...)
}

cr = 0.5
open.png('prob_joint_correlated.png', resolution=200)
plot(ellipse(cr, lev=pchisq(9,1)), type='l', col='darkblue', xlab='x', ylab='y')
points(ellipse(cr, lev=pchisq(4,1)), type='l', col='darkblue')
points(ellipse(cr, lev=pchisq(1,1)), type='l', col='darkblue')
dev.off()

cr = 0
open.png('prob_joint_independent.png', resolution=200)
plot(ellipse(cr, lev=pchisq(9,1)), type='l', col='darkblue', xlab='x', ylab='y')
points(ellipse(cr, lev=pchisq(4,1)), type='l', col='darkblue')
points(ellipse(cr, lev=pchisq(1,1)), type='l', col='darkblue')
dev.off()

open.png('prob_joint_marginal.png', resolution=200)
par(yaxs='i')
curve(dnorm(x), -4, 4, col='darkblue', xlab='y', ylab='P(y)', ylim=c(0,0.45))
dev.off()

cr=0.5
open.png('prob_joint_conditional.png', resolution=200)
par(yaxs='i')
curve(dnorm(x, cr*2, sqrt(1-cr^2)), -4, 4, col='darkblue', xlab='y', ylab='P(y | x=2)', ylim=c(0,0.5))
dev.off()
