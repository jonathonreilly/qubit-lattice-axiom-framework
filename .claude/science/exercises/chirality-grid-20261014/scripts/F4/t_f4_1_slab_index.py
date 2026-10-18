"""T-F4-1: where does the mirror's index go when a free local far-wall term 'gaps' it?

Tuned Wilson 4+1D slab (mu=3), 4 comps per layer-site, L layers along the extra coordinate,
Z^3 momentum k. Chern number of the occupied (E<0) bundle on small spheres around the 8 corners.
Small, numpy only; OMP threads limited by caller.
"""
import itertools
import numpy as np

s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
G = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0), np.kron(sz, s0)]
G1, G2, G3, G4, G5 = G
for a in range(5):
    for b in range(5):
        ac = G[a] @ G[b] + G[b] @ G[a]
        assert np.allclose(ac, 2 * np.eye(4) * (a == b))

MU = 3.0
u_near = np.array([1, 1]) / np.sqrt(2)   # layer-1 zero-mode spinor (first tensor factor)
u_far = np.array([1, -1]) / np.sqrt(2)   # layer-L zero-mode spinor
R_far = np.kron(u_far.reshape(1, 2), s0)  # 2x4 : projects layer-L 4-spinor onto mirror 2-spinor


def slab_H(k, L, far_term=None, partner=None, g=0.0):
    """Full one-body H(k). far_term: 4x4 Hermitian added on layer L.
    partner: None | 'disp' | 'flat' -- extra 2-comp chi coupled to the mirror spinor of layer L."""
    k1, k2, k3 = k
    onsite = G1 * np.sin(k1) + G2 * np.sin(k2) + G3 * np.sin(k3) + G5 * (MU - np.cos(k1) - np.cos(k2) - np.cos(k3))
    M = (-1j * G4 - G5) / 2.0  # c_s^dag M c_{s+1}
    n = 4 * L + (2 if partner else 0)
    H = np.zeros((n, n), dtype=complex)
    for s in range(L):
        H[4 * s:4 * s + 4, 4 * s:4 * s + 4] = onsite
        if s + 1 < L:
            H[4 * s:4 * s + 4, 4 * s + 4:4 * s + 8] = M
            H[4 * s + 4:4 * s + 8, 4 * s:4 * s + 4] = M.conj().T
    if far_term is not None:
        H[4 * (L - 1):4 * L, 4 * (L - 1):4 * L] += far_term
    if partner:
        hc = (sx * np.sin(k1) + sy * np.sin(k2) + sz * np.sin(k3)) if partner == 'disp' else np.zeros((2, 2))
        H[4 * L:, 4 * L:] = hc
        H[4 * L:, 4 * (L - 1):4 * L] = g * R_far
        H[4 * (L - 1):4 * L, 4 * L:] = g * R_far.conj().T
    return H


def occ_proj_vecs(H):
    w, v = np.linalg.eigh(H)
    return v[:, w < 0], w


def sphere_chern(center, rho, Hfun, nth=28, nph=56, eps=0.02):
    th = np.linspace(eps, np.pi - eps, nth + 1)
    ph = np.linspace(0, 2 * np.pi, nph, endpoint=False)
    V = {}
    nocc = None
    mingap = np.inf
    for i, t in enumerate(th):
        for j, p in enumerate(ph):
            k = np.array(center) + rho * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
            vecs, w = occ_proj_vecs(Hfun(k))
            mingap = min(mingap, np.min(np.abs(w)))
            if nocc is None:
                nocc = vecs.shape[1]
            if vecs.shape[1] != nocc:
                return None, mingap
            V[i, j] = vecs

    def link(a, b):
        d = np.linalg.det(V[a].conj().T @ V[b])
        return d / abs(d)

    F = 0.0
    for i in range(nth):
        for j in range(nph):
            a, b, c, d = (i, j), (i + 1, j), (i + 1, (j + 1) % nph), (i, (j + 1) % nph)
            F += np.angle(link(a, b) * link(b, c) * link(c, d) * link(d, a))
    # polar caps: Berry phase of the small loops at th[0] and th[-1]
    capN = np.angle(np.prod([link((0, (j + 1) % nph), (0, j)) for j in range(nph)]))
    capS = np.angle(np.prod([link((nth, j), (nth, (j + 1) % nph)) for j in range(nph)]))
    C = (F + capN + capS) / (2 * np.pi)
    return C, mingap


CORNERS = [np.array(c) * np.pi for c in itertools.product([0, 1], repeat=3)]


def corner_report(Hfun, rho=0.35, label=""):
    out = []
    for K in CORNERS:
        C, gap = sphere_chern(K, rho, Hfun)
        out.append((tuple(int(x / np.pi) for x in K), None if C is None else round(C, 3), round(gap, 4)))
    tot = sum(c for _, c, _ in out if c is not None)
    print(f"[{label}] corner spheres rho={rho}: " + "; ".join(f"{k}:{c} (min|E| {g})" for k, c, g in out))
    print(f"[{label}] total over corners = {tot:.3f}")
    return out


def k0_states(Hfun, L, ntake=6):
    w, v = np.linalg.eigh(Hfun(np.zeros(3)))
    idx = np.argsort(np.abs(w))[:ntake]
    res = []
    for i in idx:
        wt = np.array([np.sum(np.abs(v[4 * s:4 * s + 4, i]) ** 2) for s in range(L)])
        extra = 1 - wt.sum()
        cen = (np.arange(1, L + 1) @ wt) / max(wt.sum(), 1e-12)
        res.append((round(w[i], 4), round(cen, 2), round(extra, 3)))
    return res


if __name__ == "__main__":
    L = 4
    # sanity: single Weyl sigma.k has Chern +1 or -1 under this convention
    Cw, _ = sphere_chern(np.zeros(3), 0.3, lambda k: sx * k[0] + sy * k[1] + sz * k[2])
    print("convention check: sigma.k sphere Chern =", round(Cw, 3))

    print("\n== (0) free slab, L=4 ==")
    Hf = lambda k: slab_H(k, L)
    print("k=0 lowest |E| states (E, layer centroid, partner weight):", k0_states(Hf, L))
    # separate near/far chirality at k=0 by projecting onto layer-1 / layer-L zero modes
    Pn = np.zeros((4 * L, 2), dtype=complex); Pn[0:4, :] = np.kron(u_near.reshape(2, 1), s0)
    Pf = np.zeros((4 * L, 2), dtype=complex); Pf[4 * (L - 1):, :] = np.kron(u_far.reshape(2, 1), s0)
    for nm, P in (("near", Pn), ("far", Pf)):
        C, _ = sphere_chern(np.zeros(3), 0.3, lambda k, P=P: P.conj().T @ Hf(k) @ P)
        print(f"  projected {nm} 2x2 surface Hamiltonian: sphere Chern = {round(C, 3)}")
    corner_report(Hf, label="free")

    print("\n== (a) local on-site far-layer terms lambda*V ==")
    rng = np.random.default_rng(7)
    A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)); Vr = (A + A.conj().T) / 2; Vr /= np.linalg.norm(Vr, 2)
    for vname, V in (("Gamma5", G5), ("Gamma4", G4), ("random", Vr)):
        for lam in (0.3, 3.0, 30.0, 3000.0):
            Hl = lambda k, V=V, lam=lam: slab_H(k, L, far_term=lam * V)
            st = k0_states(Hl, L, ntake=4)
            C0, g0 = sphere_chern(np.zeros(3), 0.35, Hl)
            print(f"  V={vname:7s} lam={lam:7.1f}: k=0 lowest states {st}; k=0 sphere Chern={None if C0 is None else round(C0,3)} (min|E| on sphere {g0:.3g})")

    print("\n== (b) dispersive partner chi (h=+sigma.sin k), coupled to the mirror spinor ==")
    for g in (0.3, 1.0):
        Hb = lambda k, g=g: slab_H(k, L, partner='disp', g=g)
        print(f"  g={g}: k=0 lowest states {k0_states(Hb, L)}")
        corner_report(Hb, label=f"disp g={g}")

    print("\n== (c) flat on-site partner chi, coupled to the mirror spinor ==")
    for g in (0.3, 1.0):
        Hc = lambda k, g=g: slab_H(k, L, partner='flat', g=g)
        print(f"  g={g}: k=0 lowest states {k0_states(Hc, L)}")
        C0, g0 = sphere_chern(np.zeros(3), 0.15, Hc)
        print(f"  g={g}: small k=0 sphere (rho=0.15) Chern={None if C0 is None else round(C0,3)} min|E|={g0:.3g}")
        # scan radial lines for zero-energy crossings of the flat band (Fermi surface)
        for d in (np.array([1, 0, 0]), np.array([1, 1, 0]) / np.sqrt(2), np.array([1, 1, 1]) / np.sqrt(3)):
            ts = np.linspace(0.01, np.pi * np.sqrt(3), 400)
            nneg = [np.sum(np.linalg.eigvalsh(Hc(t * d)) < 0) for t in ts]
            jumps = [round(ts[i], 3) for i in range(1, len(ts)) if nneg[i] != nneg[i - 1]]
            print(f"    dir {np.round(d,3)}: occupied-count changes at |k| = {jumps}")
        corner_report(Hc, label=f"flat g={g}")
