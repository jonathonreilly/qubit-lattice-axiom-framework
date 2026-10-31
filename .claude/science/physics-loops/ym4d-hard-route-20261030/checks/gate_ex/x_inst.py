#!/usr/bin/env python3
"""Cut singular-gauge instanton on a torus: the sector adversary of gate D4 of theorem-z. Charge one patch, equal to 1 outside a ball.
Args: Np L rho k. Reported: e, I, E, f, e/I, C_eff; tree prediction e ~ (1/5)(1 - L^-2) S0 / rho^2, S0 = 4 pi^2 in this normalisation (Garcia Perez et al., recalled, gap)."""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ex_core import *

Np, L, rho, k = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 1
d = 4
ETA = torch.zeros(3, 4, 4)
for a, (i, j) in enumerate([(1, 2), (2, 3), (3, 1)]):
    ETA[a, i, j] = 1; ETA[a, j, i] = -1
    ETA[a, a + 1, 0] = -1; ETA[a, 0, a + 1] = 1   # eta-bar sign

def field(x, R):
    """A_mu^a at x (..., 4): singular gauge; returns (..., 4, 3), times the cut."""
    r2 = (x * x).sum(-1)
    pref = 2 * rho**2 / (r2 * (r2 + rho**2))
    r = torch.sqrt(r2)
    u = torch.clamp((r - 0.55 * R) / (0.45 * R), 0, 1)
    chi = 1 - u * u * u * (10 - 15 * u + 6 * u * u)
    A = torch.einsum("amn,...n->...ma", ETA, x)
    return (pref * chi)[..., None, None] * A

def links(Np, R, centre, nsub=24):
    g = torch.meshgrid(*[torch.arange(Np, dtype=torch.float64)] * d, indexing="ij")
    x0 = torch.stack(g, -1) - centre
    x0 = (x0 + Np / 2) % Np - Np / 2
    V = ident((Np,) * d + (d,))
    for mu in range(d):
        q = ident((Np,) * d)
        for s in range(nsub):
            xs = x0.clone()
            xs[..., mu] = xs[..., mu] + (s + 0.5) / nsub
            A = field(xs, R)[..., mu, :]
            q = qmul(q, qexp(A / (2 * nsub)))
        V[..., mu, :] = q
    return V

c = torch.tensor([Np / 2 + 0.5] * d, dtype=torch.float64) if Np % 2 == 0 else torch.tensor([(Np - 1) / 2 + 0.5] * d, dtype=torch.float64)
R = Np / 2 - 0.25
V = links(Np, R, c)
f, E = flux_stats(V)
I = float(I_grad(V))
S = float(wilson(V))
print(f"parent: Np={Np} rho={rho} f={f:.4f} S={S:.4f} (4 pi^2={4*np.pi**2:.4f}) E={E:.4f} I={I:.4f} I/(fE)={I/(f*E):.3f}", flush=True)
ch = Chain(Np, L, d, k)
pb = Problem(ch, V)
t0 = time.time()
U, lam, gn, rn = pb.solve(pb.initial(), verbose=True)
fs = ch.fields(U)
Ss = [float(wilson(x)) for x in fs]
c1 = (1 - L**-2) / 18
e = Ss[-2] - Ss[-1]
C = (c1 * I - e) / (f * E)
print(f"RESULT Np={Np} L={L} rho={rho} k={k}: f={f:.4f} E={E:.4f} I={I:.4f} e={e:.6f} e/I={e/I:.5f} C_eff={C:.4f} g,r={gn:.0e},{rn:.0e} S_levels={Ss} f_levels={[flux_stats(x)[0] for x in fs]} pred_tree={(1-L**-2)/5*S/rho**2:.5f} t={time.time()-t0:.0f} rss={rss_gb():.2f}", flush=True)
torch.save(dict(V=V, U=U, lam=lam), f"x_inst_{Np}_{L}_{rho}_{k}.pt")
