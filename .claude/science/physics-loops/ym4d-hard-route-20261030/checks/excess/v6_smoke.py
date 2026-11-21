import time, torch, v6_charged as v
from ex_core import Chain, rss_gb, qmul, qexp
# consistency of the chunked map against Block, and timing, on a small torus
c = Chain(4, 3, 4, 1)
n = 12
U = qmul(qexp(v.perturbation(n, 0.02, 0.02, 1)), v.const_flux(n, 1, 1))
V = c.top(U)
B = c.levels[0]
B._setup()
err = 0
for mu in range(4):
    W = v.parent_links(B, U, B.base, mu)
    err = max(err, float((W - V.reshape(-1, 4, 4)[:, mu]).abs().max()))
print("chunk map vs Block", err)
P = v.LightProblem(c, V)
lam = torch.randn(P.cshape, dtype=torch.float64)
t = time.time(); g1 = P.lag_grad(torch.zeros(P.shape), U, lam); print("lag_grad s", time.time() - t, "rss", rss_gb())
g2 = v.Problem.lag_grad(P, torch.zeros(P.shape), U, lam)
print("chunked grad vs autograd", float((g1 - g2).abs().max()))
