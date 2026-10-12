#!/usr/bin/env python3
"""Independent analytic-envelope spot checks; no imported author functions."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
import datetime, hashlib, json, time
import mpmath as mp

BASE=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=BASE/'galaxy_response'
REPO=Path(__file__).resolve().parents[1]

def guard():
    assert not list(BASE.glob('*STOP_REQUESTED*')), 'Stop requested'
    assert time.time()<json.loads((BASE/'DEADLINE.json').read_text())['deadline_epoch'], 'Deadline'

def main():
    guard(); mp.mp.dps=65; OUT.mkdir(parents=True,exist_ok=True)
    checks=[]
    # Direct integration on two linear legs; Fourier expression derived by
    # elementary exponential integration, not copied from author code.
    for S,b,beta,kx,kz,ky,mu in [(1,.2,.3,.8,.4,.2,.1),(3,.04,-.2,1.1,-2.,.3,0.),(.4,.1,.01,.02,.1,.3,2.),(10,.001,.5,3.,.7,.3,.01)]:
        S,b,beta,kx,kz,ky,mu=map(mp.mpf,map(str,(S,b,beta,kx,kz,ky,mu)))
        om=mp.sqrt(kx*kx+ky*ky+kz*kz+mu*mu)-beta*kz
        def leg(sign,lo,hi,velocity,offset):
            q=om-sign*kx*velocity
            return mp.exp(-1j*sign*kx*offset)*(mp.exp(1j*q*hi)-mp.exp(1j*q*lo))/(1j*q)
        integrated=sum(leg(sig,0,S/2,b,0)-leg(-sig,0,S/2,b,0) for sig in [1])
        integrated+=leg(1,S/2,S,-b,b*S)-leg(-1,S/2,S,-b,b*S)
        direct=mp.quad(lambda u:mp.exp(1j*om*u)*(-2j*mp.sin(kx*b*min(u,S-u))),[0,S/2,S])
        K=b*kx
        closed=-4j*K*mp.exp(1j*om*S/2)*(mp.cos(K*S/2)-mp.cos(om*S/2))/(om*om-K*K)
        A=(1-abs(beta))**2-b*b
        small=abs(K)*S*S/2; large=8*abs(K)/(om*om-K*K)
        assert abs(direct-integrated)<mp.mpf('1e-58')
        assert abs(direct-closed)<mp.mpf('1e-58')
        assert abs(direct)<=min(small,large)
        checks.append({'amplitude_error':str(abs(direct-integrated)),'closed_error':str(abs(direct-closed)),'A':str(A)})
    # Recompute physical coefficient from exact h,c and declared G,mass inputs.
    G=mp.mpf('6.67430e-11'); c=mp.mpf('299792458'); h=mp.mpf('6.62607015e-34')
    hbar=h/(2*mp.pi); amu=mp.mpf('1.66053906892e-27')
    mass=mp.mpf(26777)*amu; L=mp.mpf('.98'); v=mp.mpf(261); d=mp.mpf('266e-9')
    S=2*L*c/v; b=h/(2*mass*c*d); g2=4*mp.pi*G*mass*mass/(hbar*c)
    A=(1-v/c)**2-b*b
    assert abs(g2*b*b-4*mp.pi**3*(hbar*G/c**3)/d**2)<mp.mpf('1e-112')
    widths=[]
    for a in map(mp.mpf,['1e-15','1e-10','1e-9','1e-8']):
        k0=4/(S*mp.sqrt(A)); z=(a*k0)**2
        # Explicit separate low/high integrals, with low Gaussian dropped.
        low=S**4*k0**4/16
        high=32*mp.e1(z)/A**2
        result=g2*b*b*(low+high)/(24*mp.pi**2)
        widths.append({'a_m':str(a),'bound':str(result)})
    targets=[REPO/'neutrino/interference/MOVING_SCALAR_AND_FEIN2019.md',REPO/'neutrino/interference/moving_scalar_check.py']
    result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'independent transform, inequalities, angular normalization and physical envelope; not apparatus fit','author_files':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in targets},'checks':checks,'bounds':widths,'g2_b2':str(g2*b*b),'A':str(A)}
    (OUT/'moving_envelope_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
