# GUIDE arithmetic for gap-finishline-opus (row 837). Decides nothing.
import math
# Athenodorou-Teper Table 1 (as transcribed in library/prior/gap-seed-size.md): beta, a*sqrt(sigma), a*m(0++)
data=[(2.2986,.36778,1.224),(2.3714,.29023,1.025),(2.427,.24013,.8469),(2.509,.18011,.6563),(2.60,.13283,.5001)]
# beta where a m = 1 (linear interpolation in log(a m))
for (b1,s1,m1),(b2,s2,m2) in zip(data,data[1:]):
    if m1>=1>=m2:
        t=(math.log(m1)-0)/(math.log(m1)-math.log(m2)); print("a m(0++) = 1 at beta ~ %.3f"%(b1+t*(b2-b1)))
# two-loop asymptotic scaling for SU(2): a*Lambda = (6 pi^2 b/11)^(51/121) exp(-3 pi^2 b/11)
def aL(b): return (6*math.pi**2*b/11)**(51/121)*math.exp(-3*math.pi**2*b/11)
for b,s,m in data: print("beta %.4f  a m %.4f  (a m)/(a Lambda) %.2f"%(b,m,m/aL(b)))
c=11/(3*math.pi**2); print("x per e-fold (one loop) %.4f"%c)
for thr,name in [(2/9,'seed+gap 2/9'),(1/4,'Langevin 1/4'),(8/27,'Langevin 8/27 (82Z tori)'),(5/11,'SOS 5/11'),(2/3,'area law 2/3')]:
    print("%-26s beta=%.4f  ratio to 2.30: %.2f  to 2.38: %.2f  to 2.60: %.2f  strong-coupling 4log(4/b)=%.2f"%(name,thr,2.30/thr,2.38/thr,2.60/thr,4*math.log(4/thr)))
for x in [4,10,25,100]:
    ef=(x-2.38)/c; print("account unit x=g^-2=%5.1f -> %.1f e-folds (one loop) to beta_eff 2.38, length factor %.3g; two-loop factor %.3g"%(x,ef,math.exp(ef),aL(2.38)/aL(x)))
