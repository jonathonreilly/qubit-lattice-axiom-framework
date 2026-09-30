import numpy as np, json
from numpy.polynomial.legendre import leggauss
from scipy.special import eval_legendre
from scipy.integrate import quad
import importlib.util, sys
spec = importlib.util.spec_from_file_location("ht", __file__.replace("hemi_test_E.py","hemi_test.py"))
# reuse hemi_axisym without re-running the script: copy the small routines
X, W = leggauss(400)
def gl(f,a,b):
    if b<=a: return 0.0
    x=0.5*(b-a)*X+0.5*(b+a); return 0.5*(b-a)*np.sum(W*f(x))
def hemi_axisym(f, theta):
    ct, st = np.cos(theta), np.sin(theta)
    def integrand(s):
        A = ct*np.cos(s); B = st*np.sin(s)
        with np.errstate(divide='ignore', invalid='ignore'):
            r = np.where(B>1e-300, -A/B, np.where(A>0, -np.inf, np.inf))
        return f(np.cos(s))*np.arccos(np.clip(r,-1,1))/np.pi*np.sin(s)/2
    s1=np.arctan(abs(ct)/st); pts=sorted(set([0.0,s1,np.pi/2,np.pi-s1,np.pi]))
    return sum(gl(integrand,pts[i],pts[i+1]) for i in range(len(pts)-1))
def c_l(l): return 0.5*quad(lambda t: eval_legendre(l,t),0,1)[0]
# polynomial odd g-1/2 in t -> Legendre coefficients -> f_odd
def leg_of_poly(coefs):  # coefs: dict power->coeff for odd polynomial in t
    from numpy.polynomial import legendre as L, polynomial as Pn
    deg=max(coefs); c=np.zeros(deg+1)
    for p,v in coefs.items(): c[p]=v
    return L.poly2leg(c)
from numpy.polynomial import legendre as L
def f_odd_from_g(gpoly):  # gpoly: odd poly of (g-1/2)
    lc = leg_of_poly(gpoly)
    a = np.array([lc[l]/c_l(l) if (l%2==1 and abs(c_l(l))>0) else 0.0 for l in range(len(lc))])
    return a
def mean_abs(a):
    f=lambda t: np.abs(L.legval(t,a))
    return 0.5*(gl(f,-1,0)+gl(f,0,1))  # dmu -> dt/2
res={}
for name,poly in [("Born lam=0.6",{1:0.3}),("Born lam=1",{1:0.5}),("Born lam=0.3",{1:0.15}),
                  ("witness (1+t^3)/2",{3:0.5}),("witness (1+t)/2+t(1-t^2)/8",{1:0.5+0.125,3:-0.125})]:
    a=f_odd_from_g(poly); m=mean_abs(a)
    print(f"{name:34s} f_odd Legendre a_l={np.round(a,6).tolist()}  mean|f_odd|={m:.6f}  realisable={m<=1+1e-12}")
    res[name]=(a.tolist(),float(m))
# E3 direct check of density 2t+4t^3 on t>0
f=lambda t: np.where(t>0,2*t+4*t**3,0.0)
mass=gl(lambda t: f(t)/2,0,1)
err=0
for th in np.linspace(0.05,np.pi-0.05,30):
    t=np.cos(th); g=(1+t)/2+t*(1-t**2)/8
    err=max(err,abs(hemi_axisym(f,th)-g))
print(f"E3: density 2t+4t^3 on t>0: mass={mass:.10f}, max|H f - g_witness2|={err:.2e}")
res['E3_mass']=float(mass); res['E3_err']=float(err)
E1=abs(res['Born lam=0.6'][1]-0.6)<1e-9 and abs(res['Born lam=1'][1]-1)<1e-9 and abs(res['Born lam=0.3'][1]-0.3)<1e-9
E2=res['witness (1+t^3)/2'][1]>1
E3=abs(res['witness (1+t)/2+t(1-t^2)/8'][1]-1.0)<1e-9 and err<1e-8 and abs(mass-1)<1e-9
print("E1",E1,"E2",E2,"E3",E3)
res['E1_pass']=bool(E1); res['E2_pass']=bool(E2); res['E3_pass']=bool(E3)
json.dump(res,open(__file__.replace("hemi_test_E.py","hemi_result_E.json"),"w"),indent=1)
