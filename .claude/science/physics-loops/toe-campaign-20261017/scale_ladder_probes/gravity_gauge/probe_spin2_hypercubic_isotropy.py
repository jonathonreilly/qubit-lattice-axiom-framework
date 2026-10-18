#!/usr/bin/env python3
"""Scale-ladder probe G1 (gravity lane): does lattice point-group symmetry plus
linearised gauge invariance protect a common, isotropic light cone at leading
(two-derivative) order, spin by spin?

Counts the independent local quadratic two-derivative forms
    Q(k, f) = f . K(k) . f,   K(k) quadratic in k,
that are invariant under (a) the continuum group SO(d) and (b) the hyperoctahedral
group B_d (signed permutations; B_3 = O_h cubic, B_4 = hypercubic Z^3 x Z_tau with
the kinetic-isotropy primitive c_t = c_s), and that are exactly gauge invariant:
  spin 1:  delta A_mu    = k_mu chi
  spin 2:  delta h_munu  = k_mu xi_nu + k_nu xi_mu   (linearised diffeos)
If #B_d = #SO(d) the leading-order operator is fixed by the lattice symmetry and
anisotropy is pushed to (a k)^2-suppressed irrelevant operators (EFT direction 3).
If #B_d > #SO(d) the extra forms are MARGINAL: an anisotropic / birefringent cone is
allowed at leading order and must be tuned or forbidden by something else.

Then, for spin 2 in d=4 (Euclidean, continued k_4 = i omega in temporal gauge
h_{4mu}=0), it computes the TT dispersion omega^2(n, pol) for a generic B_4
combination near linearised Einstein-Hilbert and reports anisotropy/birefringence.
Pure numpy; deterministic seed.
"""
import itertools
import numpy as np

rng = np.random.default_rng(20261018)


def act_slots(X, n, d, mats):
    """Apply per-slot matrices to a stack X of shape (d**n, m). mats: list of n (d,d)."""
    m = X.shape[1]
    T = X.reshape((d,) * n + (m,))
    for s in range(n):
        T = np.moveaxis(np.tensordot(mats[s], T, axes=([1], [s])), 0, s)
    return T.reshape(d ** n, m)


def group_action(X, n, d, R):
    return act_slots(X, n, d, [R] * n)


def lie_action(X, n, d, L):
    I = np.eye(d)
    return sum(act_slots(X, n, d, [L if t == s else I for t in range(n)]) for s in range(n))


def permute_axes(X, n, d, perm):
    m = X.shape[1]
    T = X.reshape((d,) * n + (m,))
    return np.transpose(T, tuple(perm) + (n,)).reshape(d ** n, m)


def nullspace(A, tol=1e-9):
    """Null space via eigen-decomposition of A^T A (memory-light)."""
    G = A.T @ A
    w, v = np.linalg.eigh(G)
    top = max(w[-1], 1e-300)
    return v[:, w < (tol ** 2) * top * 1e4]


def closure(perms, n):
    elems = {tuple(range(n))}
    frontier = [tuple(range(n))]
    while frontier:
        new = []
        for g in frontier:
            for h in perms:
                x = tuple(g[h[i]] for i in range(n))
                if x not in elems:
                    elems.add(x)
                    new.append(x)
        frontier = new
    return sorted(elems)


def sym_basis(d, n, swaps):
    grp = closure(swaps, n)
    N = d ** n
    seen = {}
    cols = []
    for flat in range(N):
        idx = np.unravel_index(flat, (d,) * n)
        orbit = sorted({tuple(idx[p[i]] for i in range(n)) for p in grp})
        key = orbit[0]
        if key in seen:
            continue
        seen[key] = True
        v = np.zeros(N)
        for o in orbit:
            v[np.ravel_multi_index(o, (d,) * n)] = 1.0
        cols.append(v / np.linalg.norm(v))
    return np.array(cols).T


def signed_perm_generators(d):
    gens = []
    for i in range(d - 1):
        R = np.eye(d)
        R[[i, i + 1]] = R[[i + 1, i]]
        gens.append(R)
    F = np.eye(d)
    F[0, 0] = -1.0
    gens.append(F)
    return gens


def so_generators(d):
    gens = []
    for a, b in itertools.combinations(range(d), 2):
        L = np.zeros((d, d))
        L[a, b], L[b, a] = 1.0, -1.0
        gens.append(L)
    return gens


def count_forms(d, spin, group):
    if spin == 1:
        n = 4
        swaps = [(1, 0, 2, 3), (0, 1, 3, 2)]
        gauge_slots = (1, 2, 3)
    else:
        n = 6
        swaps = [(1, 0, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5), (2, 3, 0, 1, 4, 5), (0, 1, 2, 3, 5, 4)]
        gauge_slots = (2, 4, 5)
    S = sym_basis(d, n, swaps)
    if group == "hyperoctahedral":
        rows = [group_action(S, n, d, R) - S for R in signed_perm_generators(d)]
    else:
        rows = [lie_action(S, n, d, L) for L in so_generators(d)]
    Ginv = nullspace(np.vstack(rows))
    Binv = S @ Ginv
    acc = np.zeros_like(Binv)
    cnt = 0
    for p in itertools.permutations(gauge_slots):
        full = list(range(n))
        for a, b in zip(gauge_slots, p):
            full[a] = b
        acc += permute_axes(Binv, n, d, full)
        cnt += 1
    K = nullspace(acc / cnt)
    return Binv.shape[1], K.shape[1], Binv @ K


def report_counts():
    out = {}
    for d in (3, 4):
        for spin in (1, 2):
            for grp in ("SO", "hyperoctahedral"):
                ninv, ngauge, _ = count_forms(d, spin, grp)
                out[(d, spin, grp)] = (ninv, ngauge)
                print(f"d={d} spin={spin} group={grp:15s} invariant forms={ninv:3d}  gauge-invariant={ngauge}")
    return out


# ---------------- spin-2 dispersion in d=4 ----------------
SYM_PAIRS4 = [(i, j) for i in range(4) for j in range(i, 4)]


def Kmat(Tflat, k):
    T = Tflat.reshape((4,) * 6)
    return np.einsum("abcdef,e,f->abcd", T, k, k)


def dispersion(Tflat, nhat, kmag=1e-3):
    """Return omega^2/|k|^2 roots of physical (temporal gauge h_4mu=0) modes."""
    sp = [(i, j) for i in range(3) for j in range(i, 3)]

    def M(s):
        # k4^2 = -s ; build real matrix by evaluating at k4 = sqrt(-s) analytically:
        # entries are polynomials in k4 with parity fixed by # of index-4's.
        k_s = kmag * np.asarray(nhat) / np.linalg.norm(nhat)
        # evaluate Kmat at k4 = t for t real and extract even/odd parts
        def Kt(t):
            return Kmat(Tflat, np.array([*k_s, t]))
        t = 1.0
        Kp, Km = Kt(t), Kt(-t)
        K0 = Kmat(Tflat, np.array([*k_s, 0.0]))
        even2 = (Kp + Km) / 2 - K0          # coefficient of k4^2 (times t^2=1)
        odd1 = (Kp - Km) / 2                # coefficient of k4 (times t=1)
        rows = []
        for (a, b) in SYM_PAIRS4:
            nf = (a == 3) + (b == 3)
            row = []
            for (i, j) in sp:
                e0, e2, o1 = K0[a, b, i, j], even2[a, b, i, j], odd1[a, b, i, j]
                w = 1.0 if i == j else 2.0  # h_ij = h_ji both counted
                if nf == 1:
                    row.append(w * o1)          # divided by k4
                else:
                    row.append(w * (e0 - s * e2))
            rows.append(row)
        return np.array(rows)

    k2 = kmag ** 2
    grid = np.linspace(0.05, 3.0, 3000) * k2
    sv = np.array([np.linalg.svd(M(s), compute_uv=False) for s in grid])
    smin = sv[:, -1] / sv[:, 0]
    roots = []
    for i in range(1, len(grid) - 1):
        if smin[i] < smin[i - 1] and smin[i] < smin[i + 1] and smin[i] < 1e-2:
            lo, hi = grid[i - 1], grid[i + 1]
            for _ in range(60):
                m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
                f1 = np.linalg.svd(M(m1), compute_uv=False)
                f2 = np.linalg.svd(M(m2), compute_uv=False)
                if f1[-1] / f1[0] < f2[-1] / f2[0]:
                    hi = m2
                else:
                    lo = m1
            s = (lo + hi) / 2
            f = np.linalg.svd(M(s), compute_uv=False)
            mult = int((f / f[0] < 1e-6).sum())
            roots.append((round(s / k2, 6), mult, f[-1] / f[0]))
    return roots


def main():
    print("== Leading-order (two-derivative) quadratic forms: SO(d) vs signed-permutation group ==")
    report_counts()
    print()
    _, n_so, B_so = count_forms(4, 2, "SO")
    _, n_b4, B_b4 = count_forms(4, 2, "hyperoctahedral")
    # Linearised EH = the SO(4) form; express it and orthogonal B4 extras
    eh = B_so[:, 0]
    # sign / normalisation: choose so that the TT root is +1 along x
    extras = B_b4 - np.outer(eh, eh @ B_b4) / (eh @ eh)
    u, s, vt = np.linalg.svd(extras, full_matrices=False)
    extras = u[:, s > 1e-8]
    print(f"spin-2 d=4: SO(4) gauge-invariant forms={n_so}; B_4 forms={n_b4}; extra marginal directions={extras.shape[1]}")
    dirs = {"[100]": (1, 0, 0), "[110]": (1, 1, 0), "[111]": (1, 1, 1), "[210]": (2, 1, 0)}
    print("\nEH reference (should be omega^2/k^2 = 1, multiplicity 2 in every direction):")
    for name, nv in dirs.items():
        r = dispersion(eh, nv)
        print(f"  {name}: {r}")
    # fix overall sign so root is positive
    for eps in (0.05, 0.2):
        c = rng.normal(size=extras.shape[1])
        c = eps * c / np.linalg.norm(c) * np.linalg.norm(eh)
        T = eh + extras @ c
        print(f"\nGeneric B_4 form, relative admixture eps={eps} of extra hypercubic invariants:")
        for name, nv in dirs.items():
            r = dispersion(T, nv)
            print(f"  {name}: omega^2/k^2 roots (value, multiplicity, rel. sigma_min) = {r}")


if __name__ == "__main__":
    main()
