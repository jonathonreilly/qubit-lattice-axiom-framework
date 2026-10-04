"""A51 fwd51: forward tests of a rule (dual frame; classes + four-spin) on the L torus.
(1) Luttinger-Tisza: J(k) of the two-spin part on the L-grid; lowest q-orbits and gaps.
(2) Linear spin waves (S = 1/2, sigma units) for collinear Q in {0, (pi,0,0), (pi,pi,0), (pi,pi,pi)} with the four-spin
    terms in Hartree form (exact at quadratic order for collinear states), and for the LT planar spiral of the two-spin part.
(3) VMC energy contest from stored samples: <H>/site with binning errors.
Usage: fwd51.py L rules_key spec1,spec2,...   (rules from rules51_<L>.npz, key B or B4; or 'file:key' for another L's rule
mapped by class key)."""
import sys, signal, glob, numpy as np
signal.alarm(280)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from anal51 import *
from a46lib import binerr


def lswt(Jk, JQ, Jkp, Jkm, S=0.5):
    """Single-Q planar spiral / collinear LSWT for H = (1/2) sum_ij J_S(i-j) S_i.S_j.  Jk = J_S(k), Jkp/Jkm = J_S(k +- Q)
    on a k-grid.  Returns (mean_k (omega_k - A_k)/2 ... per site correction, min omega^2, min A)."""
    Jp = 0.5 * (Jkp + Jkm)
    A = S * (0.5 * (Jk + Jp) - JQ); B = S * 0.5 * (Jk - Jp)
    w2 = A ** 2 - B ** 2
    om = np.sqrt(np.maximum(w2, 0.))
    return 0.5 * (om - A).mean(), w2.min(), A.min()


def lt_fine(ks, Jc, nk=40):
    """Infinite-lattice LT for a finite-reach rule (classes as Z^3 orbits): J(q) = sum_c J_c sum_{d in orbit} cos(q.d) on an
    nk^3 grid.  Returns (Jmin, qmin (units of pi), fraction of the BZ within 1% / 5% of the span above Jmin)."""
    q = 2 * np.pi * np.array(list(itertools.product(range(nk), repeat=3))) / nk
    J = np.zeros(len(q))
    for k, c in zip(ks, Jc):
        if c == 0: continue
        orb = set()
        for perm in itertools.permutations(k):
            for sg in itertools.product((1, -1), repeat=3):
                orb.add(tuple(int(sg[i] * perm[i]) for i in range(3)))
        D = np.array(sorted(orb)); J += c * np.cos(q @ D.T).sum(1)
    i0 = int(np.argmin(J)); span = J.max() - J.min()
    return J[i0], q[i0] / np.pi, float((J - J.min() < 0.01 * span).mean()), float((J - J.min() < 0.05 * span).mean())


def grid_tools(L):
    g = np.array(list(itertools.product(range(L), repeat=3)))
    idx = lambda v: (np.mod(v, L) @ np.array([L * L, L, 1]))
    return g, idx


def contest(L, v, specs):
    N = L ** 3; out = {}
    for sp in specs:
        S, nf = load(L, sp)
        if S is None: continue
        e = (S @ v).real / N; mu, er = binerr(e); out[sp] = (mu, er, len(e))
    return out


if __name__ == "__main__":
    L = int(sys.argv[1]); key = sys.argv[2]; specs = sys.argv[3].split(",") if len(sys.argv) > 3 else []
    ks, m, F4, G, Gm = metrics(L); nc = len(ks); N = L ** 3
    if ":" in key:
        fn, kk_ = key.split(":"); R = np.load(fn); src = {tuple(k): R[kk_][c] for c, k in enumerate(R["ks"])}
        v = np.zeros(nc + 10); v[nc:nc + 8] = R[kk_][len(R["ks"]):len(R["ks"]) + 8]
        for c, k in enumerate(ks):
            v[c] = src.get(tuple(k), 0.)
        print(f"rule {key} mapped onto L={L} by class key ({sum(tuple(k) in src for k in ks)} of {nc} classes present)")
    else:
        v = np.load(f"rules51_{L}.npz")[key]; print(f"rule rules51_{L}.npz[{key}]")
    g, idx = grid_tools(L); ng = len(g)
    lab = {k: n for n, k in enumerate(ks)}
    cls = np.array([lab[tuple(r)] if r.any() else -1 for r in np.sort(fold(g, L), axis=1)])
    Jd = np.where(cls >= 0, v[np.maximum(cls, 0)], 0.)                 # J(d) per torus vector (sigma units, per pair)
    ph = 2 * np.pi * (g @ g.T) / L
    J2k = np.cos(ph) @ Jd                                                # J(k) = sum_{d != 0} J(d) cos(k.d)
    ql = np.array([lab.get(tuple(r), -1) for r in np.sort(fold(g, L), axis=1)])
    # (1) LT
    order = np.argsort(J2k); seen = []; rows = []
    for i in order:
        o = tuple(np.sort(fold(g[i], L)))
        if o in seen: continue
        seen.append(o); rows.append((J2k[i], o, int((np.sort(fold(g, L), axis=1) == np.array(o)).all(1).sum())))
        if len(rows) == 6: break
    span = J2k.max() - J2k.min()
    print("[LT] lowest q-orbits of J(k) (two-spin part; Q in units of 2pi/L; span max-min = %.3f):" % span)
    for Jv, o, mult in rows:
        print(f"  Q {o}: J(Q) = {Jv:+.4f}  (J - Jmin)/span = {(Jv - rows[0][0]) / span:.4f}  orbit size {mult}")
    nlow = int((J2k - J2k.min() < 0.02 * span).sum())
    print(f"  k-points within 2% of span above the minimum: {nlow} of {ng}")
    inner = [c for c, k in enumerate(ks) if max(k) < L / 2]
    if np.abs(v[[c for c in range(nc) if c not in inner]]).max(initial=0) == 0:
        Jm, qm, f1, f5 = lt_fine([ks[c] for c in inner], v[inner])
        print(f"[LT fine grid 40^3, infinite lattice] J_min {Jm:+.4f} at q/pi = {np.round(qm, 3)}; BZ fraction within 1%: {f1:.4f}, within 5%: {f5:.4f}")
    # (2) LSWT; four-spin Hartree for collinear Q
    cand = {"ferro (0,0,0)": (0, 0, 0), "layer (pi,0,0)": (L // 2, 0, 0), "col (pi,pi,0)": (L // 2, L // 2, 0), "Neel (pi,pi,pi)": (L // 2,) * 3}
    print("[LSWT] collinear candidates, four-spin terms in Hartree form (E per site, sigma units):")
    for nm, Qn in cand.items():
        Qv = 2 * np.pi * np.array(Qn) / L
        JH = np.zeros(ng); E4 = 0.
        for k4 in range(8 if len(v) > nc else 0):
            ck = v[nc + k4]
            if ck == 0: continue
            for (Ps, pi_), w in F4[k4][2].items():
                (i, j), (k, l) = PAIRINGS[pi_]; P = np.array(Ps)
                eij = np.cos(Qv @ (P[j] - P[i])); ekl = np.cos(Qv @ (P[l] - P[k]))
                E4 += ck * w * eij * ekl
                for (a, b, e) in ((i, j, ekl), (k, l, eij)):
                    JH[idx(P[b] - P[a])] += ck * w * e; JH[idx(P[a] - P[b])] += ck * w * e
        Jk = 4 * (J2k + np.cos(ph) @ JH)
        Qi = idx(np.array(Qn)); kp = idx(g + np.array(Qn)); km = idx(g - np.array(Qn))
        corr, w2min, Amin = lswt(Jk, Jk[Qi], Jk[kp], Jk[km])
        Ecl = 0.5 * J2k[Qi] + E4
        stab = "stable" if (w2min > -1e-9 and Amin > -1e-9) else f"UNSTABLE (min w^2 {w2min:.2e})"
        print(f"  {nm:16s}: E_cl {Ecl:+.5f}  E_LSWT {Ecl + corr:+.5f}  {stab}")
    if len(v) == nc or np.allclose(v[nc:], 0):
        Qn = g[order[0]]; Qi = order[0]; kp = idx(g + Qn); km = idx(g - Qn)
        corr, w2min, Amin = lswt(4 * J2k, 4 * J2k[Qi], 4 * J2k[kp], 4 * J2k[km])
        print(f"  LT spiral Q={tuple(Qn)}: E_cl {0.5*J2k[Qi]:+.5f}  E_LSWT {0.5*J2k[Qi]+corr:+.5f}  (min w^2 {w2min:.1e})")
    # (3) VMC contest
    if specs:
        nrm = np.sqrt(v @ Gm @ v)
        res = contest(L, v, specs); print(f"[VMC] <H>/site (binning error), same rule (J_NN = 1; per-site HS norm mod Casimir = {nrm:.3f}; "
                                          f"divide energies by it for unit-norm units):")
        p0 = res.get(specs[0])
        for sp, (mu, er, ns) in res.items():
            dl = "" if sp == specs[0] or p0 is None else f"   ref - parton = {mu - p0[0]:+.5f} +- {np.hypot(er, p0[1]):.5f} ({(mu - p0[0]) / np.hypot(er, p0[1]):+.1f} sigma)"
            print(f"  {sp:14s} {mu:+.5f} +- {er:.5f} ({ns} samples){dl}")
