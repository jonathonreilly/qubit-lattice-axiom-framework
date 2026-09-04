"""T127c - the ratio, conditioned properly.  (T127b's 7.12 was my procedure, not physics.)

T127b extrapolated the RATIO; the raw values swung -4.34 -> +4.78 as tau_0 fell,
which is not linear-in-tau_0 convergence at all.  The cause is a log tau_0 term:
in d=4 the a_2 coefficient produces log tau_0 alongside a_1's 1/tau_0, and a
ratio taken at finite tau_0 does not cancel it -- it amplifies it.

Fix the conditioning: extrapolate EACH quantity to tau_0 -> 0 first, exactly as
T126 did (where it reproduced -1/(24 pi) to 0.03%), and take the ratio of the
two limits.  Fit tau_0 I(tau_0) = c0 + c1 tau_0 log tau_0 + c2 tau_0, which is
the form the expansion actually has, instead of a bare straight line."""
import numpy as np, itertools
def K0_sph(s,LMAX=4000):
    l=np.arange(LMAX+1.0); return float(np.sum((2*l+1)*np.exp(-s*l*(l+1))))
def K0_tor(s,W=14):
    t=0.0
    for w in itertools.product(range(-W,W+1),repeat=2): t+=np.exp(-(w[0]**2+w[1]**2)/(4.0*s))
    return t/(4*np.pi*s)
Kscal=lambda s: K0_sph(s)*K0_tor(s)
Kform=lambda s: (4*K0_sph(s)-2.0)*(4*K0_tor(s))
VOL=4*np.pi
def tauI(tau0,m2,Kfun,rank,NQ=4000,SMAX=60.0):
    ss=np.exp(np.linspace(np.log(tau0),np.log(SMAX),NQ))
    f=np.array([(Kfun(s)-rank*VOL/(4*np.pi*s)**2)*np.exp(-s*m2)/s for s in ss])
    tr=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
    return -0.5*tau0*tr(f,ss)
T0=np.array([0.004,0.002,0.001,0.0005,0.00025])
def limit(m2,Kfun,rank):
    y=np.array([tauI(t,m2,Kfun,rank) for t in T0])
    A=np.vstack([np.ones_like(T0),T0*np.log(T0),T0]).T
    return np.linalg.lstsq(A,y,rcond=None)[0][0], y

print("T127c  each limit taken first, then the ratio")
print(f"       a_1 ratio measured directly in T127(2): -8.0000")
print(f"       scalar limit target -1/(24 pi) = {-1/(24*np.pi):.8f}")
print()
print(f"    {'m^2':>7} {'scalar c0':>13} {'% vs target':>12} {'KD-form c0':>14} {'RATIO -c0f/c0s':>16}")
rows=[]
for m2 in (0.4,0.2,0.1,0.05):
    cs,_=limit(m2,Kscal,1); cf,_=limit(m2,Kform,16)
    r=(-cf)/cs; rows.append((m2,r))
    print(f"    {m2:7.3f} {cs:13.7f} {100*(cs+1/(24*np.pi))/(1/(24*np.pi)):12.3f} {cf:14.6f} {r:16.5f}",flush=True)
m2s=np.array([x[0] for x in rows]); rs=np.array([x[1] for x in rows])
c=np.polyfit(m2s,rs,1)
print()
print(f"    linear in m^2 -> 0 :  {c[1]:.5f}      target 8      ({100*(c[1]-8)/8:+.3f}%)")
print()
print("    The scalar column is the control: it must reproduce T126's -1/(24 pi).")
print("    If it does and the ratio lands on 8, the conditioning was the whole issue")
print("    and the induced 1/G is +8x a scalar's -- positive, hence attractive.")
