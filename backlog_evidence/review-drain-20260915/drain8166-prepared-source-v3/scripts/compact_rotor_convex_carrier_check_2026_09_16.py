#!/usr/bin/env python3
"""Check the explicit extension and the actual interpolated time carrier.

This checks algebra, derivative matching, Fourier normalization and selected
finite-grid bridge Hessians. It does not certify a compact-measure comparison.
"""
AUDIT_TIMEOUT_SEC=120
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np
from scipy.integrate import quad
from compact_rotor_bridge_cubic_check_2026_09_16 import two_face_quantities


AUDIT_INPUT_PATHS = ['docs/COMPACT_ROTOR_CONVEX_CARRIER_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/COMPACT_ROTOR_BRIDGE_CUBIC_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'scripts/compact_rotor_bridge_cubic_check_2026_09_16.py']
EXPECTED_INPUT_SHA256 = {'docs/COMPACT_ROTOR_CONVEX_CARRIER_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'e85b065930317f53efaa22c7d322406dcf3072a3e6df52c11eec579e5a633d9e', 'docs/COMPACT_ROTOR_BRIDGE_CUBIC_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'ecfd4f9b82f264e95509653b62424d259a1e7ddb2e7fd9fca766f018ce8ac68c', 'scripts/compact_rotor_bridge_cubic_check_2026_09_16.py': '3b3f41b0e78883c901e15a63c9c47751cd117a81f115465854553dc9a22e307b'}
AUDIT_RSS_LIMIT_MIB = 384
_REPO = Path(__file__).resolve().parents[1]
for _input in AUDIT_INPUT_PATHS:
    assert hashlib.sha256((_REPO / _input).read_bytes()).hexdigest() == EXPECTED_INPUT_SHA256[_input], _input

def _emit_completed(result):
    expected = ['extension', 'carrier', 'bridge']
    assert all(key in result for key in expected)
    result["completed_families"] = expected
    result["TOTAL"] = len(expected)
    destination = _REPO / "logs/runner-cache" / (Path(__file__).stem + ".json")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n")
    for label, scope in [('per_element', 'finite scalar clipped-extension derivative and matching checks'), ('per_site', 'declared finite adjacent-face bridge fixtures only'), ('per_mode', 'finite time Fourier carrier identities on the declared slice counts'), ('per_block', 'three completed finite diagnostic families; no exhaustive theorem execution'), ('lattice_wide', 'not executed; global comparison estimates are written proofs')]:
        print(label + ": " + scope)
    print("TOTAL: PASS=" + str(len(expected)) + " FAIL=0")


def chi(x,alpha):
    y=abs(x);sgn=1 if x>=0 else -1
    if y<=alpha:return (x,1.,0.)
    if y>=2*alpha:return (sgn*1.5*alpha,0.,0.)
    u=(y-alpha)/alpha
    return (sgn*alpha*(1+u-u**3+u**4/2),1-3*u*u+2*u**3,
            sgn*(-6*u+6*u*u)/alpha)


def extension(x,alpha):
    y=abs(x)
    return quad(lambda s:(y-s)*math.cos(chi(s,alpha)[0]),0,y,
                points=[a for a in (alpha,2*alpha) if a<y],epsabs=2e-12)[0]


def extension_checks():
    rows=[]
    for alpha in (.05,.2,.6):
        for x in np.linspace(-3*alpha,3*alpha,121):
            c,d,dd=chi(x,alpha)
            assert abs(c)<=1.5*alpha+1e-15 and -1e-15<=d<=1+1e-15
            assert math.cos(1.5*alpha)-1e-14<=math.cos(c)<=1+1e-14
            assert abs(math.sin(c)*d)<=math.sin(1.5*alpha)+1e-14
            step=alpha*1e-4
            cp,dp,_=chi(x+step,alpha);cm,dm,_=chi(x-step,alpha)
            assert abs((cp-cm)/(2*step)-d)<2e-7
            assert abs((dp-dm)/(2*step)-dd)<4e-3
            if abs(x)<=alpha+1e-14:
                assert abs(extension(x,alpha)-(1-math.cos(x)))<2e-12
        rows.append(dict(alpha=alpha,minimum_curvature=math.cos(1.5*alpha),
                         cubic_upper=math.sin(1.5*alpha),sample_count=121))
    return rows


def carrier_checks():
    rows=[]
    rng=np.random.default_rng(81716)
    for N in (3,4,7,12):
        for T in (.08,.25):
            a=rng.normal(size=(N,5));nxt=np.roll(a,-1,axis=0)
            # Integrate affine interpolants independently by Gauss-Legendre.
            nodes,w=np.polynomial.legendre.leggauss(3)
            integral=0.
            for node,weight in zip((nodes+1)/2,w/2):
                integral+=T*weight*np.sum(((1-node)*a+node*nxt)**2)/2
            algebra=T*np.sum(a*a+a*nxt+nxt*nxt)/6
            fourier=np.fft.fft(a,axis=0,norm='ortho')
            omega=2*np.pi*np.arange(N)/N
            b=(2+np.cos(omega))/3
            spectral=T*np.sum(b[:,None]*abs(fourier)**2)/2
            assert abs(integral-algebra)<1e-12 and abs(spectral-algebra)<1e-12
            kinetic=np.sum((nxt-a)**2)/(2*T)
            kinetic_spectral=np.sum((4*np.sin(omega/2)**2)[:,None]*abs(fourier)**2)/(2*T)
            assert abs(kinetic-kinetic_spectral)<2e-12
            # Wrong one-slice magnetic carrier must actually be distinguishable.
            wrong=T*np.sum(a*a)/2
            assert abs(wrong-algebra)>1e-3
            rows.append(dict(slices=N,T=T,integrated=integral,algebra=algebra,
                             spectral=float(spectral),wrong_one_slice=wrong,
                             kinetic=kinetic,kinetic_spectral=float(kinetic_spectral)))
    return rows


def bridge_hessian_checks():
    rows=[]
    g,T=.45,.2
    end=np.array([[.6,-.25],[.9,.4]])
    h=np.array([[1.,.2],[-.1,.4]]);k=np.array([[.3,-.5],[.7,.1]])
    l=np.array([[.2,.6],[-.2,.3]])
    r=2*T*T;d0=r+g*g*T/(2*(1-r));d2=d0+r/(1-r)
    for shift in (0.,1.,3.):
        f=end+shift
        result=two_face_quantities(g,T,f,h,k,l,16)
        blend=lambda a:np.array([(2*a[0]+a[1])/3,(a[0]+2*a[1])/3])
        ff,hh,kk=map(blend,(f,h,k))
        p2=T/3*np.sum(np.cos(ff)*hh*kk)
        qh=T/3*np.sum(hh*hh);qk=T/3*np.sum(kk*kk)
        error=result['hessian']-p2
        bound=d2*math.sqrt(qh*qk)
        assert abs(error)<=bound+1e-12
        rows.append(dict(shift=shift,hessian=result['hessian'],straight=p2,
                         correction=error,correction_bound=bound))
    constants=[]
    for alpha,T,g in ((.1,.1,.003),(.2,.1,.003),(.1,.05,.01)):
        r=2*T*T;d0=r+g*g*T/(2*(1-r));d2=d0+r/(1-r)
        d3=d0+(1-r)**(-3)-1
        contrast=1-math.cos(1.5*alpha)+d2
        cubic=g*(math.sin(1.5*alpha)+d3)
        assert contrast<1
        constants.append(dict(alpha=alpha,T=T,g=g,relative_contrast=contrast,
                              cubic_chain_coefficient=cubic))
    return dict(hessian=rows,examples=constants)


def main():
    start=time.monotonic()
    files=[Path(__file__),Path(__file__).with_name('compact_rotor_bridge_cubic_check_2026_09_16.py')]
    out=dict(status='PERSONAL_CHECKS_COMPLETED',scope=__doc__,
             input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
             extension=extension_checks(),carrier=carrier_checks(),
             bridge=bridge_hessian_checks())
    out['elapsed_seconds']=time.monotonic()-start
    _emit_completed(out)


if __name__=='__main__':main()
