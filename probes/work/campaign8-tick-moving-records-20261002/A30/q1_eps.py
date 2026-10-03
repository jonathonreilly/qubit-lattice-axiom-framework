"""A30 q1_eps: (i) how the records' own field on the surface site (eps) limits blackness;
(ii) catch-first capture (A24 C1 structure) as an energy-dependent surface self-energy.

(i)  Rate model, H = -t hops + (eps - i Gam/2)|1><1| on the half chain (wall at 0).
     Best absorption over Gam at fixed k: A* = 2 t s / (|t + eps e^{ik}| + t s), s = sin k.
     Black somewhere iff |eps| < t.  Heisenberg toy with caught-matter records: eps = +2t.
(ii) Catch-first: surface site 1 couples (g) to the first site of an emission chain C
     (hopping tC, on-site -V: the trap releases V into the emitted excitation).
     Sigma(E) = g^2 gC(E + V), gC = surface Green function of C.  R = -(t + Sigma e^{-ik})/(t + Sigma e^{ik}).
"""
import signal
import numpy as np

signal.alarm(55)
t = 1.0
ks = np.linspace(1e-4, np.pi - 1e-4, 20001)
print("(i) best absorption over Gam, then over k, for surface field eps (hopping -t convention)")
for eps in [0.0, 0.5, 0.9, 1.0, 1.5, 2.0, -2.0]:
    s = np.sin(ks)
    Astar = 2 * t * s / (np.abs(t + eps * np.exp(1j * ks)) + t * s)
    i = np.argmax(Astar)
    Gopt = 2 * np.abs(t + eps * np.exp(1j * ks[i]))
    print(f"  eps={eps:+.1f}: max_k A* = {Astar[i]:.6f} at k={ks[i]:.4f} (Gam_opt={Gopt:.4f}); "
          f"black iff |eps|<t -> {'yes' if abs(eps) < t else 'no'}")
print("  eps=2: closed-form check A*(2pi/3) =", 2 * np.sin(2 * np.pi / 3) / (np.sqrt(3) + np.sin(2 * np.pi / 3)))


def gC(E, tC):
    """Retarded surface Green function of a semi-infinite chain, hopping -tC, band [-2tC, 2tC]."""
    E = np.asarray(E, dtype=float)
    inside = np.abs(E) < 2 * tC
    g_in = (E - 1j * np.sqrt(np.clip(4 * tC * tC - E * E, 0, None))) / (2 * tC * tC)
    g_out = (E - np.sign(E) * np.sqrt(np.clip(E * E - 4 * tC * tC, 0, None))) / (2 * tC * tC)
    return np.where(inside, g_in, g_out)


print("\n(ii) catch-first capture into an emission channel: A(k) at several k; threshold A/k at k->0")
for (g, tC, V) in [(1.0, 1.0, 0.0), (1.0, 1.0, 0.5), (1.0, 1.0, 1.0), (0.7, 1.0, 1.0), (1.0, 2.0, 1.0)]:
    out = []
    for k in [0.01, 0.3, 0.8, np.pi / 2, 2.3, 3.0]:
        E = -2 * t * np.cos(k)
        Sig = g * g * gC(E + V, tC)
        R = -(t + Sig * np.exp(-1j * k)) / (t + Sig * np.exp(1j * k))
        out.append(f"{1-abs(R)**2:.4f}")
    k = 1e-3
    E = -2 * t * np.cos(k)
    Sig = g * g * gC(E + V, tC)
    R = -(t + Sig * np.exp(-1j * k)) / (t + Sig * np.exp(1j * k))
    print(f"  g={g} tC={tC} V={V}: A at k=[0.01,0.3,0.8,pi/2,2.3,3.0] = {out};  A(k=1e-3)/1e-3 = {(1-abs(R)**2)/1e-3:.3f}")
# sanity: surface Green function satisfies g = 1/(E - tC^2 g)
E = np.array([-1.5, 0.3, 1.9, 2.5])
gg = gC(E, 1.0)
print("  gC self-consistency |g(E - g) - 1| max =", np.max(np.abs(gg * (E - gg) - 1)))
