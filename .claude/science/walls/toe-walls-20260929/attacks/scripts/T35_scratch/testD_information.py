import numpy as np, math
from scipy.optimize import brentq
import repo_compression_copy as R   # repo's own 1-loop compression code (copy)
gM = R.run_gauge_up()
def mt(y): return R.mt_from_yt_MPl(gM,y)
y0=(math.sqrt(4*math.pi*0.09067))/math.sqrt(6)
m0=mt(y0)
lo_prior,hi_prior=0.22,0.65
span=math.log(hi_prior/lo_prior)
print(f"y_t(M_Pl)={y0:.4f} -> m_t(1-loop, MSbar-like at 173)={m0:.1f}")
for tol in (0.03,0.01,0.005):
    ylo=brentq(lambda y: mt(y)-m0*(1-tol),0.05,y0)
    yhi=brentq(lambda y: mt(y)-m0*(1+tol),y0,1.5)
    yl=max(ylo,lo_prior); yh=min(yhi,hi_prior)
    p=math.log(yh/yl)/span
    print(f"window +-{tol*100:.1f}% in m_t: y_t(M_Pl) in [{ylo:.4f},{yhi:.4f}] (+-{(yhi/y0-1)*100:.1f}%/{(ylo/y0-1)*100:.1f}%)  prior prob (log-uniform) = {p:.3f}  bits = {-math.log2(p):.2f}")
# alternative flat prior in y
for tol in (0.03,):
    ylo=brentq(lambda y: mt(y)-m0*(1-tol),0.05,y0); yhi=brentq(lambda y: mt(y)-m0*(1+tol),y0,1.5)
    p=(min(yhi,hi_prior)-max(ylo,lo_prior))/(hi_prior-lo_prior)
    print(f"flat prior, +-3%: p={p:.3f} bits={-math.log2(p):.2f}")
# 'top-like' fraction: m_t in [150,200] GeV pole-proxy (x1.019 as in repo) 
ylo=brentq(lambda y: mt(y)*1.019-150,0.05,0.6); 
try:
    yhi=brentq(lambda y: mt(y)*1.019-200,0.3,3.0)
except Exception as e:
    yhi=float('inf')
print("y_t(M_Pl) giving pole-proxy in [150,200]: [%.3f, %s]"%(ylo,yhi))
