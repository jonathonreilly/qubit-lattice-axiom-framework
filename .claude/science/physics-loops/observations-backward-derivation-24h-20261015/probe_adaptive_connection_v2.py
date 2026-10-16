#!/usr/bin/env python3
"""An explicit adaptive-connection candidate; no empirical verification."""
from pathlib import Path
import json,hashlib
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp

def main():
    rows=[]
    def ck(name,value,**kw):
        assert bool(value),name
        rows.append(dict(name=name,passed=True,**kw))
    q,w,g=s.symbols('q w g',real=True);m,tau,k,C,lam,t,om,A=s.symbols('m tau k C lambda4 t omega A',positive=True,real=True)
    V=k*q*q/2+C*w*w/2+g*w*q*q/2+lam*q**4
    square=C*(w+g*q*q/(2*C))**2/2+k*q*q/2+(lam-g*g/(8*C))*q**4
    ck('completion of square and unstable direction',s.expand(V-square)==0 and s.expand(V.subs(w,-g*q*q/(2*C))-(k*q*q/2+(lam-g*g/(8*C))*q**4))==0)
    ck('adaptive force equations',s.diff(V,q)==k*q+g*w*q+4*lam*q**3 and s.diff(V,w)==C*w+g*q*q/2)
    Omega=s.sqrt(C/tau);drive=-g*t*t/(2*C)+g*tau/C**2*(1-s.cos(Omega*t))
    ck('ramp memory solution and zero forced preparation',s.simplify(tau*s.diff(drive,t,2)+C*drive+g*t*t/2)==0 and drive.subs(t,0)==0 and s.diff(drive,t).subs(t,0)==0)
    cubic=4*lam*t**3+g*drive*t
    series=s.series(cubic,t,0,9).removeO()
    ck('delayed cubic Taylor order',s.expand(series-(4*lam*t**3-g*g*t**5/(24*tau)+g*g*C*t**7/(720*tau*tau)))==0)
    a1,a2,L,Q=s.symbols('a1 a2 L Q');f1=a1*L+a1**3*Q;f2=a2*L+a2**3*Q
    ck('amplitude separation of unknown initial-state term',s.factor((f2/a2-f1/a1)/(a2*a2-a1*a1)-Q)==0)
    D=C-4*tau*om*om;wp=-g*A*A/(4*C)-g*A*A*s.cos(2*om*t)/(4*D);qp=A*s.cos(om*t)
    ck('periodic particular response',s.simplify(tau*s.diff(wp,t,2)+C*wp+g*qp*qp/2)==0)
    force=m*s.diff(qp,t,2)+k*qp+4*lam*qp**3+g*wp*qp
    expected=((k-m*om*om)*A+(3*lam-g*g/(4*C)-g*g/(8*D))*A**3)*s.cos(om*t)+(lam-g*g/(8*D))*A**3*s.cos(3*om*t)
    ck('fundamental and third harmonic force',s.trigsimp(s.expand_trig(force-expected))==0)
    x1,x2=s.symbols('x1 x2');B=lambda x:lam-g*g/(8*(C-4*tau*x))
    ck('bare quartic removed by frequency difference; B at zero is rational continuation',s.diff(s.simplify(B(x1)-B(x2)),lam)==0 and s.simplify(B(0).subs(lam,g*g/(8*C)))==0)
    ck('zero frequency static cubic merges both harmonics',s.simplify((3*lam-g*g/(4*C)-g*g/(8*C))+B(0)-(4*lam-g*g/(2*C)))==0)
    xs=s.symbols('x1:5');ys=[B(x) for x in xs]
    poly=(xs[0]-xs[3])*(xs[1]-xs[2])*(ys[0]-ys[2])*(ys[1]-ys[3])-(xs[0]-xs[2])*(xs[1]-xs[3])*(ys[0]-ys[3])*(ys[1]-ys[2])
    ck('common adaptive susceptibility cross ratio',s.factor(poly)==0)
    scale=s.symbols('scale',nonzero=True,real=True)
    ck('unobserved coordinate scaling preserves response',s.simplify(B(x1).subs({g:g/scale,C:C/scale**2,tau:tau/scale**2},simultaneous=True)-B(x1))==0)
    # Independent numerical w ODE, same unknown preparation across amplitudes.
    gn=.7;Cn=2.;tn=1.3;ln=.12;kn=1.1;amps=[.3,.8];grid=np.linspace(0,2,101);forces=[]
    for amp in amps:
        def rhs(time,y):return [y[1],(-Cn*y[0]-.5*gn*(amp*time)**2)/tn]
        sol=solve_ivp(rhs,[0,2],[.4,-.2],t_eval=grid,rtol=1e-11,atol=1e-13)
        assert sol.success
        forces.append(kn*amp*grid+4*ln*(amp*grid)**3+gn*sol.y[0]*amp*grid)
    recovered=(forces[1]/amps[1]-forces[0]/amps[0])/(amps[1]**2-amps[0]**2)
    reference=4*ln*grid**3+gn*grid*(-gn*grid**2/(2*Cn)+gn*tn/Cn**2*(1-np.cos(np.sqrt(Cn/tn)*grid)))
    error=np.max(np.abs(recovered-reference));ck('unknown-preparation amplitude subtraction from numerical ODE',error<1e-9,maximum_error=float(error))
    # Autonomous conservative dynamics with a permitted stable completion.
    mn=1.;stable_lam=gn*gn/(8*Cn)
    def rhs(time,y):
        q,v,w,dw=y;return [v,(-kn*q-4*stable_lam*q**3-gn*w*q)/mn,dw,(-Cn*w-.5*gn*q*q)/tn]
    sol=solve_ivp(rhs,[0,30],[.8,0.,-.1,.2],rtol=1e-10,atol=1e-12,t_eval=np.linspace(0,30,1001));assert sol.success
    qn,vn,wn,dwn=sol.y;energy=.5*mn*vn**2+.5*tn*dwn**2+.5*kn*qn**2+.5*Cn*wn**2+.5*gn*wn*qn**2+stable_lam*qn**4
    drift=np.max(np.abs(energy-energy[0]));ck('stable-completion conserved-energy numerical control',drift<1e-8,maximum_energy_drift=float(drift))
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK15_v2.md')
    print(json.dumps({'summary':{'passed':len(rows),'failed':0},'checks':rows,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'empirical_validation':False,'scope':'Chosen passive adaptive-connection polynomial action, explicitly conditional preparation and force/readout. Stability constrains a family; it does not select a physical potential.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
