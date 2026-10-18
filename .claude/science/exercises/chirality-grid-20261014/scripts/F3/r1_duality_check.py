"""R1 check: time-doubler duality for two-band free ticks U = a - i b.sigma in SU(2) on Z^3.

For each tick: W3 (degree of n=(a,b): T^3 -> S^3), all nodes (zeros of b), tick chirality
chi = sign(a0) * sign det(db/dk) (LATTICE_HANDEDNESS T2 convention), and the chirality of the same
point as a Weyl point of the conserved local operator E = (i/2)(U - U^dag) = b.sigma, chi_E = sign det(db/dk).
Also: U_g identity b == g * sin k (E = g * walker) and a == +-1 on even/odd corners; Fock-vacuum inversion.
Pre-registration: ../PREREG.md (Test R1).  Memory: < 100 MB.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
import itertools
import numpy as np

TAU = 2 * np.pi


# ---------------------------------------------------------------- ticks: return n = (a, b1, b2, b3), unnormalized ok
def n_Ug(k):
    kx, ky, kz = k
    c = np.cos(k); s = np.sin(k)
    a = c[0] * c[1] * c[2]
    s2 = (s ** 2).sum(axis=0)
    num = 1.0 - a ** 2
    with np.errstate(invalid="ignore", divide="ignore"):
        g = np.sqrt(np.where(s2 > 1e-300, num / np.where(s2 > 1e-300, s2, 1.0), 1.0))
    g = np.where(s2 > 1e-24, g, 1.0)
    return np.stack([a, g * s[0], g * s[1], g * s[2]]), g


def make_qtr(nf=2, Nfft=64):
    """Fourier truncation |n_j| <= nf of q_g = (a, g s) (the T4 'range-2' example)."""
    ks = TAU * np.arange(Nfft) / Nfft
    K = np.stack(np.meshgrid(ks, ks, ks, indexing="ij"))
    q, _ = n_Ug(K)
    coef = {}
    F = np.fft.fftn(q, axes=(1, 2, 3)) / Nfft ** 3   # q(k) = sum_n F[n] e^{i n.k}
    for n in itertools.product(range(-nf, nf + 1), repeat=3):
        c = F[(slice(None),) + tuple(ni % Nfft for ni in n)]
        if np.max(np.abs(c)) > 1e-14:
            coef[n] = c.real if np.max(np.abs(c.imag)) < 1e-12 else c
    return coef


QTR = make_qtr()


def n_qtr(k):
    acc = np.zeros((4,) + k.shape[1:], dtype=complex)
    for n, c in QTR.items():
        acc += np.asarray(c, dtype=complex).reshape((4,) + (1,) * (k.ndim - 1)) * np.exp(1j * (n[0] * k[0] + n[1] * k[1] + n[2] * k[2]))
    return acc.real


def n_wilson(M):
    def f(k):
        c = np.cos(k); s = np.sin(k)
        m = M - c.sum(axis=0)
        return np.stack([m, s[0], s[1], s[2]])
    return f


TICKS = {
    "U_g (T4 exact)": lambda k: n_Ug(k)[0],
    "V = q_tr/|q_tr| (T4 range-2)": n_qtr,
    "Wilson-normalized M=2": n_wilson(2.0),
    "Wilson-normalized M=-2": n_wilson(-2.0),
    "Wilson-normalized M=0.5": n_wilson(0.5),
}


def normalize(n):
    return n / np.linalg.norm(n, axis=0, keepdims=True)


# ---------------------------------------------------------------- W3 = degree of T^3 -> S^3
def W3(nfun, N=40):
    h = TAU / N
    ks = h * np.arange(N)
    K = np.stack(np.meshgrid(ks, ks, ks, indexing="ij"))
    n = normalize(nfun(K))
    d = []
    for ax in range(3):
        d.append((np.roll(n, -1, axis=ax + 1) - np.roll(n, 1, axis=ax + 1)) / (2 * h))
    M = np.stack([n, d[0], d[1], d[2]])  # (4 rows, 4 comps, grid)
    M = np.moveaxis(M, (0, 1), (-2, -1))
    det = np.linalg.det(M)
    return det.sum() * h ** 3 / (2 * np.pi ** 2)


# ---------------------------------------------------------------- nodes: zeros of b
def jac_b(nfun, k, e=1e-6):
    J = np.zeros((3, 3))
    for j in range(3):
        dk = np.zeros(3); dk[j] = e
        bp = normalize(nfun((k + dk).reshape(3, 1)))[1:, 0]
        bm = normalize(nfun((k - dk).reshape(3, 1)))[1:, 0]
        J[:, j] = (bp - bm) / (2 * e)
    return J


def find_nodes(nfun, Nstart=12, iters=60):
    starts = (TAU / Nstart) * (np.array(list(itertools.product(range(Nstart), repeat=3))) + 0.37)
    found = []
    for k in starts:
        k = k.copy()
        ok = False
        for _ in range(iters):
            b = normalize(nfun(k.reshape(3, 1)))[1:, 0]
            if np.linalg.norm(b) < 1e-12:
                ok = True; break
            J = jac_b(nfun, k)
            try:
                step = np.linalg.solve(J, b)
            except np.linalg.LinAlgError:
                break
            if np.linalg.norm(step) > 0.5:
                step *= 0.5 / np.linalg.norm(step)
            k = k - step
        if not ok:
            b = normalize(nfun(k.reshape(3, 1)))[1:, 0]
            ok = np.linalg.norm(b) < 1e-9
        if ok:
            k = np.mod(k, TAU)
            if not any(np.linalg.norm(np.angle(np.exp(1j * (k - f)))) < 1e-5 for f in found):
                found.append(k)
    return found


def classify(nfun, nodes):
    rows = []
    for k in nodes:
        a0 = normalize(nfun(k.reshape(3, 1)))[0, 0]
        J = jac_b(nfun, k)
        dJ = np.linalg.det(J)
        chiE = int(np.sign(dJ))
        chi = int(np.sign(a0)) * chiE          # T2: sign det(+-J) in 3D
        rows.append((k, a0, chi, chiE, dJ))
    return rows


def vacuum_inversion(nfun, k0, r=0.05, ntry=20, seed=0):
    """Fock vacuum: fill the band with quasi-energy -eps(k) in (-pi,0]. Pair = particle (+eps(k1)) + hole (-eps(k2))."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(ntry):
        k1 = k0 + r * rng.normal(size=3); k2 = k0 + r * rng.normal(size=3)
        n1 = normalize(nfun(k1.reshape(3, 1)))[:, 0]; n2 = normalize(nfun(k2.reshape(3, 1)))[:, 0]
        e1 = np.arccos(np.clip(n1[0], -1, 1)); e2 = np.arccos(np.clip(n2[0], -1, 1))
        dq = np.angle(np.exp(1j * (e1 + e2)))              # pair quasi-energy, mod 2pi in (-pi, pi]
        dE = np.linalg.norm(n1[1:]) + np.linalg.norm(n2[1:])  # pair cost measured by E = b.sigma (= sin eps)
        out.append((dq, dE))
    out = np.array(out)
    return out[:, 0].min(), out[:, 0].max(), out[:, 1].min()


def main():
    print("=== R1 time-doubler duality check ===")
    # identity checks for U_g
    rng = np.random.default_rng(1)
    K = rng.uniform(0, TAU, size=(3, 2000))
    nq, g = n_Ug(K)
    s = np.sin(K)
    print("U_g: |n|-1 max =", np.abs(np.linalg.norm(nq, axis=0) - 1).max())
    print("U_g: b - g*sin k max =", np.abs(nq[1:] - g * s).max(), "(E = (i/2)(U-U^dag) = b.sigma = g * H_walker)")
    print("U_g: g>0 everywhere sampled:", bool((g > 0).all()), " min g =", g.min())
    for cor in itertools.product([0, np.pi], repeat=3):
        a = np.prod(np.cos(cor))
        print("   corner", tuple(int(round(c / np.pi)) for c in cor), "a = c_x c_y c_z =", int(round(a)),
              " walker chirality (-1)^#pi =", (-1) ** int(round(sum(cor) / np.pi)))
    print("U_g: a(k) = c_x c_y c_z = (1/4)[cos(kx+ky+kz)+cos(kx+ky-kz)+cos(kx-ky+kz)+cos(-kx+ky+kz)] (body-diagonal hops), check:",
          np.abs(np.prod(np.cos(K), axis=0) - 0.25 * (np.cos(K[0] + K[1] + K[2]) + np.cos(K[0] + K[1] - K[2]) + np.cos(K[0] - K[1] + K[2]) + np.cos(-K[0] + K[1] + K[2]))).max())
    print("q_tr: number of Fourier modes kept =", len(QTR))
    kk = rng.uniform(0, TAU, size=(3, 4000))
    print("q_tr: min |q_tr| on 4000 random k =", np.linalg.norm(n_qtr(kk), axis=0).min())

    allpass = True
    for name, f in TICKS.items():
        w = W3(f)
        nodes = find_nodes(f)
        rows = classify(f, nodes)
        s0 = sum(r[2] for r in rows if r[1] > 0); sp = sum(r[2] for r in rows if r[1] < 0)
        sE = sum(r[3] for r in rows)
        n0 = sum(1 for r in rows if r[1] > 0); npi = sum(1 for r in rows if r[1] < 0)
        idok = all((r[3] == r[2]) if r[1] > 0 else (r[3] == -r[2]) for r in rows)
        aok = all(abs(abs(r[1]) - 1) < 1e-6 for r in rows)
        ok = (abs(w - round(w)) < 0.05) and s0 == sp == round(w) and sE == 0 and idok and aok
        allpass &= ok
        print(f"\n--- {name}: W3 = {w:+.4f}; nodes: {n0} at eps=0, {npi} at eps=pi; "
              f"sum chi(eps=0) = {s0:+d}, sum chi(eps=pi) = {sp:+d}; sum chi_E (as Weyl points of E) = {sE:+d}; "
              f"|a|=1 at nodes: {aok}; chi_E = +chi (0) / -chi (pi): {idok}  -> {'PASS' if ok else 'FAIL'}")
        for (k, a0, chi, chiE, dJ) in rows:
            print(f"     k/pi = {np.round(k / np.pi, 4)}  a = {a0:+.6f}  chi_tick = {chi:+d}  chi_E = {chiE:+d}  detJ = {dJ:+.4g}")
        # vacuum inversion at one 0-node and one pi-node
        for sel, lab in ((lambda r: r[1] > 0, "eps=0 node"), (lambda r: r[1] < 0, "eps=pi node")):
            rr = [r for r in rows if sel(r)]
            if rr:
                lo, hi, emin = vacuum_inversion(f, rr[0][0])
                print(f"     Fock vacuum, pair at {lab}: pair quasi-energy (mod 2pi) in [{lo:+.4f}, {hi:+.4f}];  min E-cost = {emin:.4f}")
    print("\nOVERALL R1:", "PASS" if allpass else "FAIL")


if __name__ == "__main__":
    main()
