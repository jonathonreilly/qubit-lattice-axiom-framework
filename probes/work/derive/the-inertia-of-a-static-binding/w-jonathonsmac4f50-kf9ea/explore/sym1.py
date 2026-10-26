import sympy as sp
z,m,d=sp.symbols('z m delta',real=True)
E=sp.symbols('E',positive=True)
# parametrize by z,m: E^2=4m^2+(1+z)^2/z ; t from (2+z)/E = t-4m^2/t
Es=sp.sqrt(4*m**2+(1+z)**2/z)
t=sp.symbols('t',positive=True)
# t^2 - ((2+z)/E) t - 4m^2 =0
q=(2+z)/E
tpos=(q+sp.sqrt(q**2+16*m**2))/2
V=E-tpos
a=1
c=-(1+z)/E
w1=-1/E
tt=t
N=w1**2+(1+c**2)/(1-z**2)+4*m**2*(1/tt**2+z**2/(E**2*(1-z**2)))
S1=-1/E+c/(1-z)
Q=(2*m/tt)**2+(2*m)**2*(z/E-1/tt)**2+(2*m/E)**2*z**2*(1-z)/(1+z)
W=(E*S1+Q)/(2*N)
# substitute: t satisfies t^2 = q t + 4 m^2 ; keep t symbolic with that relation
# numeric test of threshold expansion
import mpmath as mp
mp.mp.dps=40
Wf=sp.lambdify((z,m,E,t),W,'mpmath')
def Wzm(zv,mv):
    Ev=mp.sqrt(4*mv**2+(1+zv)**2/zv); qv=(2+zv)/Ev
    tv=(qv+mp.sqrt(qv**2+16*mv**2))/2
    return Wf(zv,mv,Ev,tv),Ev,Ev-tv
for mv in [mp.mpf(4),mp.mpf('0.8'),mp.mpf('0.1')]:
    for dv in [mp.mpf('1e-2'),mp.mpf('1e-3'),mp.mpf('1e-4')]:
        zv=-1+dv
        Wv,Ev,Vv=Wzm(zv,mv)
        print(mv,dv,mp.nstr(Wv,12),mp.nstr((1-Wv)/dv,10),'V',mp.nstr(Vv,10))
