import gc, resource, sys, time
sys.path.insert(0, '../gate_ex')
import torch, numpy as np
import v6_charged as v
from ex_core import Chain, rss_gb, qmul, qexp, wilson
st = torch.load('/tmp/excess_v6e/a.pt'); U = st['U']; lam = st['lam']
print('load', rss_gb(), flush=True)
n = 24; Np = 8
chain = Chain(Np, 3, 4, 1)
U0 = qmul(qexp(v.perturbation(n, 0.01, 0.0, 1)), v.const_flux(n, 1, 1))
V = chain.top(U0); print('top', rss_gb(), flush=True)
P = v.LightProblem(chain, V); print('problem', rss_gb(), flush=True)
H = torch.zeros(P.shape, dtype=torch.float64)
t = time.time(); r = P.resid(qmul(qexp(H), U)); print('resid', rss_gb(), time.time() - t, flush=True)
t = time.time(); s = wilson(qmul(qexp(H), U)); print('wilson', rss_gb(), time.time() - t, flush=True)
t = time.time(); g = P._wilson_grad(H, U); print('wgrad', rss_gb(), time.time() - t, flush=True)
t = time.time(); g = P._constraint_grad(H, U, lam + 10 * r, chunk=128); print('cgrad', rss_gb(), time.time() - t, flush=True)
