#!/usr/bin/env python3
"""Author checks of conditional primitive-observation and finite-bin bounds.

No empirical inputs. The analytic source proves the general bounds; these
computations check field-equation pullback, exact examples and controlled faults.
"""
from pathlib import Path
import hashlib
import json
import platform
import sys
import sympy as s
import mpmath as mp

HERE = Path(__file__).resolve().parent
checks = []
mutations = []


def zero(name, expr):
    value = s.factor(s.cancel(s.simplify(expr)))
    checks.append({"name": name, "kind": "symbolic_identity", "ok": value == 0,
                   "residual": str(value)})


def mutant(name, expr):
    value = s.factor(s.cancel(s.simplify(expr)))
    mutations.append({"name": name, "detected": value != 0,
                      "residual": str(value)})


# Derive the label-map slope from the metric angular-minus-time equation.
# These computations do not insert a prescribed scalar profile or potential.
z = s.symbols("z", positive=True)
r, R, B = [s.Function(n)(z) for n in ("r", "R", "B")]
q = s.diff(r, z)
dr = lambda expr: s.diff(expr, z) / q
ellr = dr(R) / R
gt = (B - 1) / r**2 + dr(B) / r
ga = B * (dr(ellr) + ellr**2 + ellr / r) + dr(B) * (ellr + 1 / r) / 2
u = (ga - gt) / (B * (1 / r - ellr))
P = q / (R * s.sqrt(B))
D = R**2 - r * R * dr(R)  # circular geodesic fixes Omega^2 = R*dr(R)/r
endpoint_slope = s.diff(P, z)/P - s.diff(q,z)/q - q/r - s.diff(D,z)/D + 2*s.diff(R,z)/R
integrand = R**4 * P**2 / (q*r*D)
zero("general observation-label formula from metric angular equation", endpoint_slope + integrand - q*u)

# Relabel z by a new label with dz/dnew = h>0.
RR, PP, qq, rr, DD, h = s.symbols("RR PP qq rr DD h", positive=True)
J = RR**4 * PP**2/(qq*rr*DD)
zero("increasing relabeling preserves endpoint P/q", (PP*h)/(qq*h) - PP/qq)
zero("increasing relabeling preserves integral density", J.subs({PP:PP*h,qq:qq*h}, simultaneous=True) - h*J)

# A power-law metric in a nonlinear radius label gives an independent exact profile.
p,b,k = s.symbols("p b k", positive=True)
rp = s.exp(k*z); Rp = rp**p; qp = s.diff(rp,z)
Pp = qp/(Rp*s.sqrt(b)); Dp = Rp**2*(1-p)
Ep = s.diff(Pp,z)/Pp-s.diff(qp,z)/qp-qp/rp-s.diff(Dp,z)/Dp+2*s.diff(Rp,z)/Rp
Jp = Rp**4*Pp**2/(qp*rp*Dp)
c = (b*p*p-b+1)/(b*(1-p))
zero("nonlinear-label power metric reproduces field exponent", Ep+Jp-c*k)
mutant("extra radius Jacobian in integrand", (Ep+Jp/qp-c*k).subs({p:s.Rational(1,5),b:s.Rational(1,2),k:2}))
mutant("inverted endpoint radar slowness", (Ep-2*(s.diff(Pp,z)/Pp-s.diff(qp,z)/qp)+Jp-c*k).subs({p:s.Rational(1,5),b:s.Rational(1,2),k:2}))
mutant("drop shared clock contribution to D slope", (Ep+s.diff(Dp,z)/Dp+Jp-c*k).subs({p:s.Rational(1,5),b:s.Rational(1,2),k:2}))

x,y,H,K = s.symbols("x y H K", positive=True)
zero("exact bin refinement surplus", x*x/H+y*y/K-(x+y)**2/(H+K)-(K*x-H*y)**2/(H*K*(H+K)))
a,bb,coef,t = s.symbols("a bb coef t", positive=True)
width_H=(bb**2-a**2)/2
radar_increment=coef*width_H
quadratic_integral=coef**2*width_H
zero("finite-bin equality profile S=coef*r", quadratic_integral-radar_increment**2/width_H)
zero("uncertain D product split", (RR+x)**2-(rr+y)**2*(PP+h)**2-(RR**2-rr**2*PP**2)
     - ((RR+x)**2-RR**2) + ((rr+y)**2-rr**2)*(PP+h)**2 + rr**2*((PP+h)**2-PP**2))

mp.mp.dps=60
fmt=lambda x:mp.nstr(x,32)
numeric=[]


def channels(ar,aratio,ao,ap):
    return {
        "r":lambda t:1+t+ar*t*(1-t),
        "q":lambda t:1+ar*(1-2*t),
        "R":lambda t:1+(mp.mpf('0.1')+aratio)*t,
        "O":lambda t:mp.mpf('0.12')+ao*mp.sin(mp.pi*t),
        "P":lambda t:1+mp.mpf('0.2')*t+ap*mp.cos(2*mp.pi*t),
    }


def log_profile(f):
    def E(t):
        r,q,R,O,P=[f[n](t) for n in ('r','q','R','O','P')]
        D=R*R-r*r*O*O
        return mp.log(P)-mp.log(q)-mp.log(r)-mp.log(D)+2*mp.log(R)
    def j(t):
        r,q,R,O,P=[f[n](t) for n in ('r','q','R','O','P')]
        return R**4*P**2/(q*r*(R*R-r*r*O*O))
    return E(1)-E(0)+mp.quad(j,[0,mp.mpf('0.5'),1])


base=log_profile(channels(0,0,0,0))
for ar in map(mp.mpf,('0.002','-0.003')):
    for aratio in map(mp.mpf,('0.002','-0.004')):
        for ao in map(mp.mpf,('0.003','-0.002')):
            for ap in map(mp.mpf,('0.004','-0.006')):
                # Certified via |sin|, |cos|<=1 and 0<=t(1-t)<=1/4.
                er,eq,eR,eO,eP=abs(ar)/4,abs(ar),abs(aratio),abs(ao),abs(ap)
                rlo=Rlo=mp.mpf(1)
                qlo=1-abs(ar); Plo=1-abs(ap)
                rhi=2+abs(ar)/4; Rhi=mp.mpf('1.1')+abs(aratio)
                Ohi=mp.mpf('0.12')+abs(ao); Phi=mp.mpf('1.2')+abs(ap)
                Dlo=Rlo**2-rhi**2*Ohi**2
                assert min(rlo,Rlo,qlo,Plo,Dlo)>0
                eD=2*Rhi*eR+2*rhi*Ohi**2*er+2*rhi**2*Ohi*eO
                KR=4*Rhi**3*Phi**2/(qlo*rlo*Dlo)
                KP=2*Rhi**4*Phi/(qlo*rlo*Dlo)
                Kq=Rhi**4*Phi**2/(qlo**2*rlo*Dlo)
                Kr=Rhi**4*Phi**2/(qlo*rlo**2*Dlo)
                KD=Rhi**4*Phi**2/(qlo*rlo*Dlo**2)
                bound=2*eP/Plo+2*eq/qlo+2*er/rlo+2*eD/Dlo+4*eR/Rlo+KR*eR+KP*eP+Kq*eq+Kr*er+KD*eD
                actual=abs(log_profile(channels(ar,aratio,ao,ap))-base)
                numeric.append({'name':'joint primitive perturbation','parameters':list(map(fmt,(ar,aratio,ao,ap))),
                                'actual':fmt(actual),'bound':fmt(bound),'inside':actual<=bound,
                                'bounds_from':'analytic envelopes, not a grid maximum',
                                'scope':'functional perturbations, not asserted field-equation solutions'})

I=mp.log(2); coarse=mp.mpf(2)/3
fine=mp.mpf(2)/5+mp.mpf(2)/7
numeric.append({'name':'constant slowness strict/refined bin bound','actual':fmt(I),'coarse':fmt(coarse),
                'fine':fmt(fine),'inside':coarse<fine<I})
mutations.append({'name':'reverse finite-bin lower inequality','detected':not(I<=coarse),
                  'residual':fmt(I-coarse)})

# Smooth radar curves with identical endpoint increment and endpoint slowness.
raw=lambda t:mp.exp(-1/(1-4*t*t)) if abs(t)<mp.mpf('.5') else mp.mpf(0)
norm=mp.quad(raw,[-mp.mpf('.5'),0,mp.mpf('.5')])
psi=lambda t:raw(t)/norm
psi2=mp.quad(lambda t:psi(t)**2,[-mp.mpf('.5'),0,mp.mpf('.5')])
amp=mp.mpf('.05'); wide=mp.mpf('.5'); center=mp.mpf('1.5')
baseline_lower=1-amp/wide*psi(0)
assert baseline_lower>0
spikes=[]
for eps in (mp.mpf(1)/8,mp.mpf(1)/32,mp.mpf(1)/128):
    S=lambda r:1-amp/wide*psi((r-center)/wide)+amp/eps*psi((r-center)/eps)
    points=[1,center-wide/2,center-eps/2,center,center+eps/2,center+wide/2,2]
    delta=mp.quad(S,points)
    value=mp.quad(lambda r:S(r)**2/r,points)
    lower=amp**2*psi2/(2*eps)
    spikes.append({'epsilon':fmt(eps),'radar_increment':fmt(delta),'quadratic_integral':fmt(value),
                   'proved_lower_bound':fmt(lower),'endpoint_slowness':[fmt(S(1)),fmt(S(2))],
                   'ok':abs(delta-1)<mp.mpf('1e-45') and value>=lower and S(1)==S(2)==1})

out={'kind':'author conditional mathematical controls; no empirical data',
     'python':platform.python_version(),'sympy':s.__version__,'mpmath':mp.__version__,
     'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'source_sha256':hashlib.sha256((HERE/'BLOCK02_DERIVATION_v1.md').read_bytes()).hexdigest(),
     'symbolic_checks':checks,'mutations':mutations,'numerical_controls':numeric,
     'finite_sample_witness':spikes,'baseline_lower_bound':fmt(baseline_lower)}
out['pass']=all(c['ok'] for c in checks) and all(m['detected'] for m in mutations) and all(n['inside'] for n in numeric) and all(c['ok'] for c in spikes)
outpath=HERE/'BLOCK02_CONTROLS_v1.json'
outpath.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'symbolic_checks':len(checks),'mutations':len(mutations),'numeric_controls':len(numeric),
                  'spike_controls':len(spikes),'pass':out['pass'],'output':str(outpath)},indent=2))
sys.exit(0 if out['pass'] else 1)
