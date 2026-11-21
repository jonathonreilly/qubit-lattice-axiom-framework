import torch, v6_charged as v
from ex_core import Chain, rss_gb, qmul, qexp, wilson
c = Chain(4, 3, 4, 1)
U = qmul(qexp(v.perturbation(12, 0.02, 0.02, 1)), v.const_flux(12, 1, 1))
P = v.LightProblem(c, c.top(U))
H = 0.01 * torch.randn(P.shape, dtype=torch.float64)
g1 = P._wilson_grad(H, U)
H2 = H.clone().requires_grad_(True)
g2, = torch.autograd.grad(wilson(qmul(qexp(H2), U)), H2)
print("wilson grad, chunked vs full", float((g1 - g2).abs().max()), "rss", rss_gb())
