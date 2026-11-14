import time, torch, v6_charged as v
from ex_core import Chain, rss_gb, qmul, qexp
c = Chain(4, 3, 4, 1)
U = qmul(qexp(v.perturbation(12, 0.02, 0.02, 1)), v.const_flux(12, 1, 1))
P = v.LightProblem(c, c.top(U))
lam = torch.randn(P.cshape, dtype=torch.float64)
g1 = P.cgrad_left(U, lam, chunk=32)
g2 = P._constraint_grad(torch.zeros(P.shape), U, lam)
print("left gradient vs H gradient at H = 0:", float((g1 - g2).abs().max()), float(g2.abs().max()))
