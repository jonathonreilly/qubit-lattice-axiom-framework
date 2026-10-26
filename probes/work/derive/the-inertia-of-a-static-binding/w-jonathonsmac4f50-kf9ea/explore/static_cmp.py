import mpmath as mp
mp.mp.dps=40
def state(zv,mv):
    Ev=mp.sqrt(4*mv**2+(1+zv)**2/zv); qv=(2+zv)/Ev
    t=(qv+mp.sqrt(qv**2+16*mv**2))/2
    V=Ev-t
    a=mp.mpf(1); c=-(1+zv)*a/Ev; w1=-a/Ev
    N=(w1**2)+(a*a+c*c)/(1-zv*zv)+4*mv*mv*a*a*(1/t**2+zv*zv/(Ev*Ev*(1-zv*zv)))
    S1=-a*a/Ev+a*c/(1-zv)
    Q=(2*mv*a/t)**2+(2*mv*a)**2*(zv/Ev-1/t)**2+(2*mv*a/Ev)**2*zv*zv*(1-zv)/(1+zv)
    W=(Ev*S1+Q)/(2*N)
    wr2=(a*a+(2*mv*a/t)**2)/N   # weight at r=2
    U=V*wr2
    return Ev,V,W,U,N
for mv in [mp.mpf(4),mp.mpf('0.8'),mp.mpf('0.1')]:
    for dv in [mp.mpf('1e-2'),mp.mpf('1e-3'),mp.mpf('1e-4')]:
        zv=-1+dv
        Ev,V,W,U,N=state(zv,mv)
        T=Ev-2*mv-U
        stat=-(T-U/2)/mv
        print(mp.nstr(mv,3),mp.nstr(dv,3),'1-W',mp.nstr(1-W,8),'static',mp.nstr(-stat,8),'ratio',mp.nstr((1-W)/(-stat),8),'U',mp.nstr(U,6),'T',mp.nstr(T,6),'eb',mp.nstr(2*mv-Ev,6))
