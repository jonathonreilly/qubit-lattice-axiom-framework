"""K1: smallest non-common per-entry excursion (log-space L2, and L_inf) taking each quark sector to r=1/2.
Common-scale MSbar masses from the repo runner (as the attack). Also: where in the 3 masses does the cheapest excursion sit?"""
from common import *
from scipy.optimize import minimize, brentq
g = load_runner(); PARS, _RG = g["PARS"], g["_RG"]
R = _RG(PARS['aS'], PARS['mc'], PARS['mb'], PARS['mt'])
up = np.array([PARS['mu']*R.factor(2.0,162.5), PARS['mc']*R.factor(PARS['mc'],162.5), PARS['mt']*R.factor(PARS['mt'],162.5)])
dn = np.array([PARS['md']*R.factor(2.0,162.5), PARS['ms']*R.factor(2.0,162.5), PARS['mb']*R.factor(PARS['mb'],162.5)])
for name, m0 in (("down", dn), ("up", up)):
    # L2 minimal: minimise |l|^2 s.t. r(m0*exp(l)) = 0.5; l defined mod common shift (drop that dof by setting sum l = 0 is not needed, r invariant)
    cons = {'type':'eq','fun':lambda l: rf(m0*np.exp(l))-0.5}
    best=None
    for s in range(20):
        x0=np.random.default_rng(s).normal(0,0.3,3)
        res=minimize(lambda l:(l-l.mean())@(l-l.mean()), x0, constraints=[cons], method='SLSQP', options=dict(maxiter=500, ftol=1e-14))
        if res.success and (best is None or res.fun<best.fun): best=res
    l=best.x-best.x.mean()
    print("%s: min centred-L2 excursion to r=1/2: |l|=%.3f ; factors (centred) = %s" % (name, np.sqrt(best.fun), np.round(np.exp(l),3)))
    # Linf via continuous minimisation of t s.t. |l_i|<=t (common shift is free, so also allow l0 offset)
    bestt=None
    for sd in range(30):
        x0=np.concatenate([np.random.default_rng(sd).normal(0,0.3,3),[1.0]])
        cons=[{'type':'eq','fun':lambda z: rf(m0*np.exp(z[:3]))-0.5}]+[{'type':'ineq','fun':(lambda z,i=i: z[3]-z[i])} for i in range(3)]+[{'type':'ineq','fun':(lambda z,i=i: z[3]+z[i])} for i in range(3)]
        res=minimize(lambda z:z[3], x0, constraints=cons, method='SLSQP', options=dict(maxiter=800, ftol=1e-14))
        if res.success and (bestt is None or res.fun<bestt.fun): bestt=res
    print("   Linf: independent factors within [e^-t,e^t] (common shift free) reach r=1/2 at t=%.3f -> factors %s" % (bestt.fun, np.round(np.exp(bestt.x[:3]),3)))
    for keep in (0,1,2):
        # freeze entry `keep`, move the other two only
        bb=None
        for sd in range(20):
            x0=np.random.default_rng(sd).normal(0,0.5,2)
            def full(z): 
                l=np.zeros(3); idx=[i for i in range(3) if i!=keep]; l[idx]=z; return l
            res=minimize(lambda z:z@z, x0, constraints=[{'type':'eq','fun':lambda z: rf(m0*np.exp(full(z)))-0.5}], method='SLSQP', options=dict(maxiter=500, ftol=1e-14))
            if res.success and (bb is None or res.fun<bb.fun): bb=res
        if bb is not None: print("   entry %d frozen, other two moved: min L2=%.3f, factors %s" % (keep, np.sqrt(bb.fun), np.round(np.exp(full(bb.x)),3)))
print("\nreference: repo one-loop c-vs-t pole-factor spread ~12%% (attack) -> log 0.11 ; attack envelope 15%% -> log 0.14")
