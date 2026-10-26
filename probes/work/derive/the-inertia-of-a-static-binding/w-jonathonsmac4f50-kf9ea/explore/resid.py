import mpmath as mp
from static_cmp import state
mp.mp.dps=50
def lam0(mv):
    s=mp.sqrt(64*mv**4+1)
    return (-16*mv**2+s-3)/(-64*mv**4+8*mv**2*s+s-1)
for mv in [mp.mpf(4),mp.mpf('0.8'),mp.mpf('0.1')]:
    L=lam0(mv)
    for dv in [mp.mpf('1e-2'),mp.mpf('1e-3'),mp.mpf('1e-4')]:
        Ev,V,W,U,N=state(-1+dv,mv)
        Wt=W+L*Ev*U     # tuned fixed lambda
        eb=2*mv-Ev
        print(mp.nstr(mv,3),mp.nstr(dv,3),'W-1',mp.nstr(Wt-1,8),'/delta^2',mp.nstr((Wt-1)/dv**2,8),' -eb/2m /delta^2',mp.nstr(-eb/(2*mv)/dv**2,8),' lam*(delta)',mp.nstr((1-W)/(Ev*U),8))
