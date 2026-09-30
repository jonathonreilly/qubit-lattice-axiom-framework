#!/usr/bin/env python3
"""Coupled scalar diagnostic; author reuse of exact gravity adjoint implementation.

Transverse reflections make the x-dependent diagonal canonical subspace
invariant. The code compares the original Christoffel Hamiltonian gradient
with a separately integrated-by-parts local variation, then evolves it.
"""
import json
import os
import resource
import signal
import time
from pathlib import Path

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
RUNTIME = Path("/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929")
assert not (RUNTIME / "STOP_REQUESTED.json").exists()
assert time.time() < json.loads((RUNTIME / "DEADLINE.json").read_text())["deadline_epoch"]
signal.alarm(45)
started = time.monotonic()
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

A, B, C = gs = sp.symbols("A B C", positive=True)
pa, pb, pc = ps = sp.symbols("pa pb pc")
qa, qb, qc = qs = sp.symbols("qa qb qc")
ra, rb, rc = rs = sp.symbols("ra rb rc")
S = sp.sqrt(A * B * C)
W = [S / x for x in gs]
u, b, c, v, w = qa / (2*A), qb / (2*B), qc / (2*C), -qb / (2*A), -qc / (2*A)
potential = (-ra*(b+c) + rb*v + rc*w
             - W[0]*(u*(b+c)-b*b-c*c)
             - W[1]*v*(u-b+c) - W[2]*w*(u+b-c))
trace = sum(x*y for x, y in zip(gs, ps))
kinetic = (sum((x*y)**2 for x, y in zip(gs, ps)) - trace**2/2)/S
arguments = (*gs, *ps, *qs, *rs)
exprs = ([sp.diff(kinetic, x) for x in ps]
         + [-sp.diff(kinetic+potential, x) for x in gs]
         + [sp.diff(potential, x) for x in qs]
         + [sp.diff(potential, x) for x in rs]
         + [sp.diff(x, y) for x in W for y in gs])
local = sp.lambdify(arguments, exprs, "numpy", cse=True)


def derivative(n):
    assert n % 2 == 1
    k = np.arange(n)[:, None] - np.arange(n)[None, :]
    out = np.zeros((n, n))
    mask = k != 0
    out[mask] = (-1.0)**k[mask] / (2*np.sin(np.pi*k[mask]/n))
    return out


def original(g, p, D):
    """Literal scalar curvature with spectral derivatives left unexpanded."""
    aa, bb, cc = g
    qa_, qb_, qc_ = g @ D.T
    u_, b_, c_ = qa_/(2*aa), qb_/(2*bb), qc_/(2*cc)
    v_, w_ = -qb_/(2*aa), -qc_/(2*aa)
    rxx = -D @ (b_+c_) + u_*(b_+c_)-b_*b_-c_*c_
    ryy = D @ v_ + v_*(u_-b_+c_)
    rzz = D @ w_ + w_*(u_+b_-c_)
    sqrtg = np.sqrt(aa*bb*cc)
    gp = g*p
    td = (np.sum(gp*gp, axis=0)-np.sum(gp, axis=0)**2/2)/sqrtg
    cd = td - sqrtg*(rxx/aa+ryy/bb+rzz/cc)
    jd = np.sum(p*(g @ D.T), axis=0)-2*(D @ (aa*p[0]))
    return np.mean(cd), cd, jd


def rhs(t, state, D):
    n = D.shape[0]
    g, p = state.reshape(2, 3, n)
    q = g @ D.T
    sqrtg = np.sqrt(np.prod(g, axis=0))
    ww = sqrtg/g
    r = ww @ D.T
    values = local(*g, *p, *q, *r)
    z = np.asarray([np.broadcast_to(x, (n,)) for x in values])
    dg = z[:3]
    dp = z[3:6]+z[6:9] @ D.T
    dw = z[9:12] @ D.T
    wgrad = z[12:].reshape(3, 3, n)
    dp += np.einsum("ijn,in->jn", wgrad, dw)
    return np.stack([dg, dp]).reshape(-1)



# Price:45 CPU/wall alarm,200MB; dense spatial derivative at most257^2.
# This intentionally reuses the author vacuum engine; it is not independent.
from fractions import Fraction as Fr

def centered(n):
    eps=2*np.pi/n
    D=np.zeros((n,n))
    for i in range(n):
        D[i,(i+1)%n]=1/(2*eps);D[i,(i-1)%n]=-1/(2*eps)
    return D

def unpack(y,n):
    return y[:3*n].reshape(3,n), y[3*n:6*n].reshape(3,n), y[6*n:7*n], y[7*n:]

def original_total(y,D):
    g,p,phi,w=unpack(y,len(D))
    energy,cd,jd=original(g,p,D)
    sqrtg=np.sqrt(np.prod(g,axis=0));z=D@phi
    matter=w*w/(2*sqrtg)+sqrtg*z*z/(2*g[0])
    return energy+np.mean(matter),cd+matter,jd+w*z

def rhs_total(t,y,D):
    n=len(D);g,p,phi,w=unpack(y,n)
    base=rhs(t,np.stack([g,p]).reshape(-1),D).reshape(2,3,n)
    sqrtg=np.sqrt(np.prod(g,axis=0));z=D@phi
    metric_derivative=-w*w/(4*sqrtg*g)+sqrtg*z*z/(4*g[0]*g)
    metric_derivative[0]-=sqrtg*z*z/(2*g[0]*g[0])
    base[1]-=metric_derivative
    return np.concatenate([base.reshape(-1),w/sqrtg,D@(sqrtg*z/g[0])])

# All canonical directions in a generic truly aliased diagonal fixture.
controls=[]
for label,operator in [('spectral',derivative),('centered',centered)]:
    n=7;x=np.arange(n)*2*np.pi/n;D=operator(n)
    g=np.array([1+.04*np.cos(x)+.01*np.sin(2*x),1+.03*np.sin(x),1-.02*np.cos(2*x)])
    p=np.array([.08+.03*np.sin(x),.04+.02*np.cos(x),-.03+.01*np.sin(2*x)])
    phi=.06*np.cos(x)+.03*np.sin(2*x);w=.2+.01*np.cos(2*x)
    y=np.concatenate([g.reshape(-1),p.reshape(-1),phi,w]);gradient=np.empty_like(y)
    for j in range(len(y)):
        trial=y.astype(complex);trial[j]+=1e-24j
        gradient[j]=n*original_total(trial,D)[0].imag/1e-24
    expected=np.concatenate([gradient[3*n:6*n],-gradient[:3*n],gradient[7*n:],-gradient[6*n:7*n]])
    error=float(np.max(abs(rhs_total(0,y,D)-expected)))
    assert error<1e-11
    controls.append({'derivative':label,'n':n,'directions':len(y),'gradient_error':error})

# General symmetric metric variation of the scalar local source; all six slots.
rng=np.random.default_rng(19030);matrix_error=0.
for case in range(17):
    perturb=.02*rng.normal(size=(3,3));g=np.eye(3)+(perturb+perturb.T)/2
    z=rng.normal(size=3);w=float(rng.normal());s=1.7
    inv=np.linalg.inv(g);sqrtg=np.sqrt(np.linalg.det(g));v=inv@z
    S=-w*w*inv/(4*sqrtg)+s*sqrtg*(z@v)*inv/4-s*sqrtg*np.outer(v,v)/2
    def scalar_local(gg):
        ss=np.sqrt(np.linalg.det(gg))
        return w*w/(2*ss)+s*ss*(z@np.linalg.solve(gg,z))/2
    for i in range(3):
      for j in range(i,3):
        gg=g.astype(complex);gg[i,j]+=1e-24j
        if i!=j:gg[j,i]+=1e-24j
        expected=S[i,j]*(1 if i==j else 2)
        matrix_error=max(matrix_error,float(abs(scalar_local(gg).imag/1e-24-expected)))
assert matrix_error<1e-11

# Exact rational majorant hypothesis for f=cos x, sigma0=1/20, amplitude1/10.
# q=sin^2 x has norm(1+exp(1/5))/2 <=(1+5/4)/2=9/8.
r=Fr(1,128);R=1+r;d=2-R**5;A=R+R**6/d;L=1+6*R**5/d+5*R**10/d**2
lam=Fr(1,1600);Bbound=Fr(9,8)
assert d>0 and lam*Bbound<=min(r/(2*A),1/(2*L))
assert 3*(R**4-1)<Fr(1,8)
# Floating discretization of the continuum iteration, explicitly not its proof.
nref=257;x=np.arange(nref)*2*np.pi/nref;k=np.fft.fftfreq(nref,d=1/nref)
u=np.zeros(nref);q=np.sin(x)**2
changes=[]
for iteration in range(16):
    psi=1+u;c=np.mean(q*psi)/np.mean(psi**5)
    force=q*psi-c*psi**5
    coeff=np.fft.fft(force)/nref;coeff[0]=0
    inverse=np.zeros_like(coeff);mask=k!=0;inverse[mask]=-coeff[mask]/(k[mask]**2)
    new=(-float(lam)*np.fft.ifft(inverse*nref)).real
    changes.append(float(np.max(abs(new-u))));u=new
psi=1+u;c=float(np.mean(q*psi)/np.mean(psi**5));H2=.1**2*c/12;H=np.sqrt(H2)
psihat=np.fft.fft(psi)/nref
lap=np.fft.ifft(-(k*k)*psihat*nref).real
residual=float(np.max(abs(lap+float(lam)*(q*psi-c*psi**5))))
rows=[]
for label,operator,grids in [('spectral',derivative,(5,7,9,13,17)),('centered',centered,(17,33,65,129))]:
 for n in grids:
    xx=np.arange(n)*2*np.pi/n
    sampled=(np.exp(1j*np.outer(xx,k))@psihat).real
    g=np.array([sampled**4]*3);p=np.array([-2*H*sampled**2]*3)
    phi=.1*np.cos(xx);w=np.zeros(n);y=np.concatenate([g.reshape(-1),p.reshape(-1),phi,w])
    en,cd,jd=original_total(y,operator(n))
    rows.append({'derivative':label,'n':n,'C_sup':float(np.max(abs(cd))),
                 'Jx_sup':float(np.max(abs(jd))),'energy':float(en)})

# Exact massless-scalar Kasner continuum solution, pulled back by X=x+eta sin x.
# pi_i=1/3, scalar coefficient2/sqrt3; constraint sum pi_i^2=1-c_scalar^2/2.
trajectory=[];eta=.05;cc=2/np.sqrt(3);duration=.01;power=np.array([1/3]*3)
for label,operator,grids in [('spectral',derivative,(5,7,9,13,17)),('centered',centered,(17,33,65,129))]:
 for n in grids:
    xx=np.arange(n)*2*np.pi/n;f=1+eta*np.cos(xx);D=operator(n)
    def exact(t):
        scales=t**(2*power)
        g=np.array([scales[0]*f*f,scales[1]+0*f,scales[2]+0*f])
        sqrtg=t*f
        p=np.array([(power[i]-1)*sqrtg/(t*g[i]) for i in range(3)])
        phi=cc*np.log(t)+0*f;w=cc*f
        return np.concatenate([g.reshape(-1),p.reshape(-1),phi,w])
    initial=exact(1);e0,c0,j0=original_total(initial,D)
    solution=solve_ivp(lambda t,y:rhs_total(t,y,D),(0,duration),initial,method='DOP853',rtol=2e-12,atol=2e-14)
    assert solution.success
    final=solution.y[:,-1];ef,cf,jf=original_total(final,D)
    trajectory.append({'derivative':label,'n':n,'rhs_evaluations':solution.nfev,
                       'initial_C_sup':float(np.max(abs(c0))),'initial_Jx_sup':float(np.max(abs(j0))),
                       'state_error_sup':float(np.max(abs(final-exact(1+duration)))),
                       'final_C_sup':float(np.max(abs(cf))),'final_Jx_sup':float(np.max(abs(jf))),
                       'energy_drift':float(abs(ef-e0))})
result={'scope':'Author floating diagnostics and exact rational hypothesis checks; no interval/continuum solve certification, independent computation, or theorem from samples. Duration not certified by majorant T.',
        'canonical_gradient_controls':controls,'general_symmetric_scalar_metric_derivatives':{'cases':17,'directions_each':6,'max_error':matrix_error},
        'contraction_rational_hypotheses':{'radius':str(r),'q_norm_upper':str(Bbound),'lambda':str(lam),'mapping_bound':str(lam*Bbound*A),'contraction_bound':str(lam*Bbound*L),'metric_bound':str(3*(R**4-1))},
        'conformal_iteration':{'reference_n':nref,'amplitude':.1,'sigma0':.05,'iterations':16,'iterate_changes_sup':changes,'H_squared':float(H2),'H':float(H),'reference_equation_residual':residual,'finite_constraint_rows':rows},
        'scalar_Kasner':{'duration':duration,'scalar_log_coefficient':float(cc),'rows':trajectory},
        'seconds':time.monotonic()-started,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_name('scalar_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
