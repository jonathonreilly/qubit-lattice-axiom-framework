import sympy as sp, time
from fourier_core import *
phi, pi = Fn("phi"), Fn("pi")
xi = [Fn(f"xi{k}") for k in range(3)]; eta = [Fn(f"eta{k}") for k in range(3)]
D = lambda f, k: sp.diff(f, X[k])
Gm = lambda x: pi * sum(x[k] * D(phi, k) for k in range(3))
lie = [sum(xi[l] * D(eta[k], l) - eta[l] * D(xi[k], l) for l in range(3)) for k in range(3)]
t=time.time()
br = pb(Gm(xi), Gm(eta), [(phi, pi)])
slots = [Slot("xi", xi), Slot("eta", eta), Slot("phi", [phi]), Slot("pi", [pi])]
print(is_zero(br - Gm(lie), slots), is_zero(br + Gm(lie), slots), time.time()-t)
