"""Static ring trace and actual nodal/pairing matrix challenges."""
from pathlib import Path
import json,math
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad

def ring(phi):
    h=np.zeros((4,4),complex)
    for i in range(4):
        j=(i+1)%4;z=np.exp(1j*phi) if i==3 else 1
        h[i,j]=z;h[j,i]=z.conjugate() if hasattr(z,'conjugate') else z
    return h

def analytic(phi,x):
    return 4*(1+np.cosh(2*x*np.cos(phi/4)))*(1+np.cosh(2*x*np.sin(phi/4)))

out={'ring':[],'nodes':[]}
for x in [.05,.1,.4,1.,2.]:
    errs=[]
    for phi in np.linspace(0,2*np.pi,37):
        d=np.linalg.det(np.eye(4)+expm(-x*ring(phi)))
        errs.append(abs(d-analytic(phi,x)));assert abs(d-analytic(phi,x))<1e-8
    c1,qe=quad(lambda phi:analytic(phi,x)**2*np.cos(phi)/(2*np.pi),0,2*np.pi,epsabs=1e-10)
    assert analytic(np.pi,x)>analytic(0,x)
    assert c1<0
    out['ring'].append({'beta_t':x,'max_matrix_formula_error':max(errs),'F0':analytic(0,x)**2,'Fpi':analytic(np.pi,x)**2,'first_Fourier_coefficient':c1,'quadrature_error_estimate':qe,'small_x_coefficient_ratio':c1/x**4})

sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1.,-1.]);zeta=.6;b=.7

def hp(k):
    x,y,z=np.array(k)-np.array([b,0,0])
    return np.sin(x)*sx+np.sin(y)*sy+(2+zeta-np.cos(x)-np.cos(y)-np.cos(z))*sz

for sgx in [-1,1]:
    for sgz in [-1,1]:
        k=np.array([sgx*b,0,sgz*np.arccos(zeta)])
        f=hp if sgx==1 else lambda q:hp(-np.array(q)).conjugate()
        assert np.linalg.norm(f(k))<1e-14
        jac=np.stack([np.array([np.trace(s@((f(k+np.eye(3)[i]*1e-5)-f(k-np.eye(3)[i]*1e-5))/2e-5))/2 for s in [sx,sy,sz]]).real for i in range(3)],axis=1)
        assert np.linalg.norm(jac.T@jac-np.diag([1,1,1-zeta*zeta]))<2e-9
        out['nodes'].append({'k':k.tolist(),'charge':sgx,'chirality':int(np.sign(np.linalg.det(jac))),'metric':(jac.T@jac).tolist()})
assert sum(v['chirality']*v['charge']**3 for v in out['nodes'])==0
for k in [np.array([b,0,np.arccos(zeta)]),np.array([.1,.2,.3]),np.array([2.,1.,-1.])]:
    h=hp(k);delta=.23;bdg=np.block([[h,delta*np.eye(2)],[delta*np.eye(2),-h]])
    assert np.linalg.norm(bdg@bdg-np.kron(np.eye(2),h@h+delta*delta*np.eye(2)))<1e-12
    assert min(abs(np.linalg.eigvalsh(bdg)))>=delta-1e-12
out['pairing_gap']=.23
Path(__file__).with_name('BLOCK1_FOURIER_PAIRING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
for v in out['ring']:print(v)
print('nodes',out['nodes']);print('pairing lower gap',out['pairing_gap'])
