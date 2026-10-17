import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'scripts'))
import large_feature_spectral_response as m
import sympy as s
import numpy as np
A,B,C,z=s.symbols('a b c z',real=True)
gauge=m.solve_cell(dict(square=1,triangle=0,plaquette=1,tube=1))
H=s.zeros(12)
for j,(v,w,sh,kind) in enumerate(m.etypes):
    amp=-(A if kind=='onsite' else B)*(-1)**gauge[j]*(-s.I)**(sh[0]-sh[1]+sh[2])
    i,k=m.CI[v],m.CI[w]
    H[k,i]+=amp;H[i,k]+=s.conjugate(amp)
for v,w in m.TRI:
    amp=s.I*C*(-1)**gauge[m.ekey[(v,w,m.Z0)]]
    i,k=m.CI[v],m.CI[w]
    H[k,i]+=amp;H[i,k]+=s.conjugate(amp)
expected=(z*z+2*A*z-2*A*A-2*(B+C)**2)**4*((z-2*A)**2-2*(B-2*C)**2)**2
poly=H.charpoly(z)
actual=poly.as_expr().subs(poly.gen,z)
checks={'exact_charpoly':s.expand(actual-expected)==0,'Hermitian':H==s.conjugate(H.T)}
# Independent random numeric spectrum and inverse check on a preselected connected box.
rng=np.random.default_rng(71072)
maxerr=0
for j in range(100):
    a,b,c=rng.uniform([-1.05,.08,-.52],[-.95,.12,-.48])
    q=np.sqrt(2)*(b-2*c);r=np.sqrt(3*a*a+2*(b+c)**2)
    energies=np.repeat([2*a-q,-a-r,2*a+q,-a+r],[2,4,2,4])
    vals=np.linalg.eigvalsh(m.bloch(gauge,-np.pi/2*np.array([1,-1,1]),a,b,c))
    maxerr=max(maxerr,float(np.max(np.abs(vals-energies))))
    assert np.all(np.diff(energies)>=0)
    d1=-3*a+q-r;d2=2*q;d3=-3*a+q+r
    aa=(d2-d1-d3)/6; qq=d2/2;rr=(d3-d1)/2
    vv=-np.sqrt((rr*rr-3*aa*aa)/2);uu=qq/np.sqrt(2)
    assert np.max(np.abs([aa-a,(uu+2*vv)/3-b,(vv-uu)/3-c]))<1e-12
checks['numeric_100_spectra_and_inverse']=maxerr<1e-12
# Homogeneous positive scaling, including arbitrary k (not only selected valley).
for j in range(30):
    k=rng.uniform(-np.pi,np.pi,3);g=rng.uniform(.1,3)
    base=m.bloch(gauge,k,-1,.1,-.5)
    assert np.max(np.abs(m.bloch(gauge,k,-g,.1*g,-.5*g)-g*base))<1e-12
checks['full_Bloch_positive_scaling_30']=True
# Nonvanishing Jacobian of the three-gap map, algebraically via q,r intermediates.
q=s.sqrt(2)*(B-2*C);r=s.sqrt(3*A*A+2*(B+C)**2)
gaps=s.Matrix([-3*A+q-r,2*q,-3*A+q+r])
det=s.simplify(gaps.jacobian([A,B,C]).det())
checks['gap_Jacobian']=s.simplify(det-(-72*s.sqrt(2)*(B+C)/r))==0
out={'checks':checks,'pass':sum(checks.values()),'fail':len(checks)-sum(checks.values()),'max_spectrum_abs_error':maxerr,'gap_jacobian':str(det)}
print(json.dumps(out,indent=2));open(Path(__file__).resolve().parents[4]/'outputs/large_feature_spectral_response/independent.json','w').write(json.dumps(out,indent=2)+'\n')
assert all(checks.values())
