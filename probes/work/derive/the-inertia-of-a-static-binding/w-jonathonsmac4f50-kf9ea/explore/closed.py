import mpmath as mp
mp.mp.dps=40
def E0_of(m,V,guess=None):
    m=mp.mpf(m);V=mp.mpf(V)
    def zE(E):
        s=E*E-4*m*m   # (1+z)^2/z = s ; s<0 ; z=((s-2)-sqrt((s-2)^2-4))/2 choose |z|<1
        x=s-2
        r=mp.sqrt(x*x-4)
        z1=(x+r)/2; z2=(x-r)/2
        return z1 if abs(z1)<abs(z2) else z2
    def f(E):
        z=zE(E); t=E-V
        return (2+z)/E-(t-4*m*m/t)
    return f,zE
def W_closed(m,V,E0=None):
    m=mp.mpf(m);V=mp.mpf(V)
    f,zE=E0_of(m,V)
    if E0 is None:
        # scan
        import numpy as np
        lo=mp.mpf(1e-6); hi=2*m-mp.mpf(10)**-12
        grid=[lo+(hi-lo)*i/4000 for i in range(4001)]
        vals=[f(g) for g in grid]
        roots=[]
        for i in range(4000):
            if vals[i]*vals[i+1]<0:
                roots.append(mp.findroot(f,(grid[i],grid[i+1]),solver='anderson'))
        E0=roots[-1]
    z=zE(E0); E=E0; t=E-V
    a=mp.mpf(1)
    c=-(1+z)*a/E
    w1=-a/E
    N=(w1**2)+(a*a+c*c)/(1-z*z)+4*m*m*a*a*(1/t**2+z*z/(E*E*(1-z*z)))
    S1=-a*a/E+a*c/(1-z)
    Q=(2*m*a/t)**2+(2*m*a)**2*(z/E-1/t)**2+(2*m*a/E)**2*z*z*(1-z)/(1+z)
    return E0,z,(E0*S1+Q)/(2*N)
if __name__=="__main__":
    for (m,V) in [(4,-0.5),(4,-0.3),(4,-0.15),(4,-0.115),(0.8,-0.9)]:
        E0,z,Wv=W_closed(m,V)
        print(m,V,mp.nstr(E0,12),mp.nstr(z,8),mp.nstr(Wv,10))
