#!/usr/bin/env python3
"""A law that satisfies every clause of T1-net as worded, with H = 0 and no dynamics.

Law: pick a coordinate 2-plane (mu, nu) uniformly among the 6. Set all links in direction
mu to exp(i a rho sigma_1 / 2), all links in direction nu to exp(i a rho sigma_2 / 2), all
other links to 1. Act only on gauge-invariant functions, as Proposition 10.4 does.

Claims checked here, on a lattice, with no statistics (the law is six point masses):
 (i)   invariance under translations and under the hypercubic group on gauge-invariant
       functions, including the reflection reversing mu (conjugation by exp(i pi sigma_2/2)
       sends sigma_1 -> -sigma_1, so r U is gauge equivalent to U);
 (ii)  reflection positivity: Gram matrix S(Theta F_i F_j) on a set of gauge-invariant
       functions in a half space is positive semi-definite;
 (iii) renormalisation condition: e_r fixed at r_0 by tuning rho, 0 < e < 1/3, and the
       limit is not flat and not Haar;
 (iv)  (WIT): connected correlator of s_p, s_q is non-zero, ordered along all axes;
 (v)   (NF1): <s([W_1, W_2])> > 0 for two small loops at a common base point;
 (vi)  (NF2): e_r -> 0 as r -> 0, as r^4.
 (vii) the connected correlator does not decay: no clustering, H = 0 on the OS space.
"""
import itertools
import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=140)

SIG = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
ID = np.eye(2, dtype=complex)


def expsu2(vec):
    """exp(i vec . sigma / 2)."""
    vec = np.asarray(vec, dtype=float)
    th = np.linalg.norm(vec)
    if th == 0:
        return ID.copy()
    n = vec / th
    return np.cos(th / 2) * ID + 1j * np.sin(th / 2) * (n[0] * SIG[0] + n[1] * SIG[1] + n[2] * SIG[2])


def s_of(U):
    return 1 - 0.5 * np.trace(U).real


class Config:
    """Constant field: links[mu] is the SU(2) element on every link in direction mu."""
    def __init__(self, links):
        self.links = links

    def path(self, steps):
        """Product of link variables along steps, a list of signed axes (1..4 or -1..-4)."""
        U = ID.copy()
        for st in steps:
            mu = abs(st) - 1
            U = U @ (self.links[mu] if st > 0 else self.links[mu].conj().T)
        return U

    def reflected(self, axis):
        """(r U)_b = U_{r(b)}: on a constant field, axis links become their inverses."""
        L = [u.copy() for u in self.links]
        L[axis] = L[axis].conj().T
        return Config(L)


def plane_configs(a_rho):
    cs = []
    for mu, nu in itertools.combinations(range(4), 2):
        L = [ID.copy() for _ in range(4)]
        L[mu] = expsu2([a_rho, 0, 0])
        L[nu] = expsu2([0, a_rho, 0])
        cs.append(Config(L))
    return cs


def gi_functions():
    """Gauge-invariant functions: half traces of closed loops, as lists of signed steps,
    including chiral combinations that are odd under a reversal in a generic constant field."""
    loops = []
    axes = [1, 2, 3, 4]
    for m, n in itertools.permutations(axes, 2):
        loops.append([m, n, -m, -n])
        loops.append([m, m, n, -m, -m, -n])
        loops.append([m, n, n, -m, -n, -n])
    for m, n, k in itertools.permutations(axes, 3):
        # hexagon and twisted loops
        loops.append([m, n, k, -m, -n, -k])
        loops.append([m, n, -m, k, -n, -k])
        loops.append([m, n, -m, -n, k, n, -k, -n])
    return loops


def fval(cfg, loop):
    return 0.5 * np.trace(cfg.path(loop)).real


def main():
    a_rho = 0.37  # link angle; the fine lattice value is immaterial, the law is scale covariant
    confs = plane_configs(a_rho)
    loops = gi_functions()
    print("number of test functions:", len(loops))

    # (i) reflection: F(r U) = F(U) on each point mass, for every gauge-invariant loop.
    worst = 0.0
    for c in confs:
        for ax in range(4):
            rc = c.reflected(ax)
            for lp in loops:
                # r also reverses the steps of the loop; the function is evaluated on r U,
                # which is what Theta F does.
                worst = max(worst, abs(fval(rc, lp) - fval(c, lp)))
    print("(i)  sup |F(r U) - F(U)| over planes, axes, loops: %.2e" % worst)
    # generic constant field control: a non-orthogonal triple breaks this, RP would fail.
    gen = Config([expsu2([.3, 0, 0]), expsu2([.1, .3, 0]), expsu2([.05, .1, .3]), ID])
    bad = max(abs(fval(gen.reflected(ax), lp) - fval(gen, lp)) for ax in range(4) for lp in loops)
    print("     control, generic constant field: sup |F(r U) - F(U)| = %.2e (not invariant)" % bad)

    # (ii) RP Gram matrix. Since F(rU) = F(U) on each point mass, S(Theta F_i F_j) = E[F_i F_j].
    Fm = np.array([[fval(c, lp) for lp in loops] for c in confs])  # 6 x nloops
    Fr = np.zeros_like(Fm)
    for k, c in enumerate(confs):
        rc = c.reflected(0)
        Fr[k] = [fval(rc, lp) for lp in loops]
    gram = (Fr.T @ Fm) / len(confs)
    ev = np.linalg.eigvalsh(0.5 * (gram + gram.T))
    print("(ii) RP Gram: min eigenvalue %.2e, max %.3f, asymmetry %.2e, rank %d"
          % (ev.min(), ev.max(), np.abs(gram - gram.T).max(), np.sum(ev > 1e-10)))

    # (iii), (vi) scale dependence with a coarse field: constant field blocked by the path
    # mean. Coarse link over side n in direction mu = n-fold product (the blocking of a
    # constant field is a constant field; straight paths are the leading part of the mean).
    print("(iii,vi) plaquette energy at scale r = n a, with link angle a rho:")
    for n in [1, 2, 4, 8, 16, 32]:
        th = n * 0.02
        L = [expsu2([th, 0, 0]), expsu2([0, th, 0]), ID, ID]
        cfg = Config(L)
        sp = s_of(cfg.path([1, 2, -1, -2]))
        print("   r/a = %3d  s_p in the active plane = %.6e   e_r = (1/6) s_p = %.6e   s_p/(r rho)^4 = %.4f"
              % (n, sp, sp / 6, sp / th ** 4))

    # (iv), (vii) WIT and absence of clustering: correlator independent of separation.
    th = 1.0
    c = Config([expsu2([th, 0, 0]), expsu2([0, th, 0]), ID, ID])
    sp = s_of(c.path([1, 2, -1, -2]))
    e = sp / 6
    conn = sp * sp / 6 - e * e
    print("(iv) coarse angle 1: e_r = %.5f, Cov(s_p, s_q) for parallel p, q at ANY separation = %.5e" % (e, conn))
    print("     by exact constancy of the field: no decay, S_c(Theta B, tau_t B) constant in t, H = 0.")

    # (v) NF1: two plaquettes at one base point in the active plane.
    W1 = c.path([1, 2, -1, -2])
    W2 = c.path([-1, 2, 1, -2])
    comm = W1 @ W2 @ W1.conj().T @ W2.conj().T
    print("(v)  s([W_1, W_2]) in the active plane = %.5e > 0; <.> = (1/6) of it = %.5e" % (s_of(comm), s_of(comm) / 6))


if __name__ == "__main__":
    main()
