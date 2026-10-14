"""TW-3 probes (b), (c): lattices of FK sites under anisotropic (strained) hopping.

Each site x carries 8 'mirror' Majoranas gamma_a(x) (Spin(7) spinor) with the onsite FK
quartic W*Omega(x); optionally n_L light Majoranas lambda_l(x) (Spin(7) singlets).
Hopping is bipartite (x in A, y in B):  i t_b sum_a gamma_a(x) gamma_a(y),  t_x = t(1+u), t_y = t(1-u).
Light hopping i tL_b sum_l lambda_l(x) lambda_l(y); light-mirror couplings
  V1 * (i sum_l lambda_l(x)lambda_l(y)) (i sum_a gamma_a(x)gamma_a(y))   on bonds,
  V2 * Omega(x) (i sum_l lambda_l(x)lambda_l(y)) on bonds (x the A end).
Theta: antiunitary, gamma(x) -> eps_x gamma(x), lambda(x) -> eps_x lambda(x).

Matrix-free: H = sum over flip masks f of diag-phase vectors; parity sectors by penalty.
Usage: python3 tw3_lattice.py <cluster> [nL] ; cluster in {dimer, L3, plaqpi, plaq0}
"""
import sys
import time
import numpy as np
import scipy.sparse.linalg as sla
from tw3_lib import Maj, cayley_terms

np.set_printoptions(precision=6, suppress=True, linewidth=160)
CL = sys.argv[1] if len(sys.argv) > 1 else "L3"
NL = int(sys.argv[2]) if len(sys.argv) > 2 else 0
MODE = sys.argv[3] if len(sys.argv) > 3 else "scan"

# cluster geometry: sites, sublattice eps, bonds (x(A), y(B), axis, sign)
if CL == "dimer":
    eps = [1, -1]
    bonds = [(0, 1, "x", 1)]
elif CL == "L3":
    eps = [1, -1, -1]
    bonds = [(0, 1, "x", 1), (0, 2, "y", 1)]
elif CL in ("plaqpi", "plaq0"):
    # sites 0=(0,0)A 1=(1,0)B 2=(0,1)B 3=(1,1)A
    eps = [1, -1, -1, 1]
    s = -1 if CL == "plaqpi" else 1
    bonds = [(0, 1, "x", 1), (3, 2, "x", s), (0, 2, "y", 1), (3, 1, "y", 1)]
else:
    raise SystemExit("unknown cluster")
NS = len(eps)
NM = 8 + NL                     # Majoranas per site
assert NM % 2 == 0
QPS = NM // 2
mj = Maj(NS * QPS)
DIM = mj.dim
TERMS = cayley_terms()


def g(x, a):          # mirror Majorana a at site x
    return x * NM + a


def lam(x, l):        # light Majorana l at site x
    return x * NM + 8 + l


class Op:
    """sum of coeff * Majorana strings, stored grouped by flip mask (column convention)."""

    def __init__(self):
        self.d = {}

    def add(self, idx, c):
        f, ph = mj.string(idx)
        if f in self.d:
            self.d[f] += c * ph
        else:
            self.d[f] = c * ph

    def addop(self, other, c=1.0):
        for f, ph in other.d.items():
            if f in self.d:
                self.d[f] = self.d[f] + c * ph
            else:
                self.d[f] = c * ph

    def matvec(self, v):
        out = np.zeros(DIM, complex)
        s = mj.s
        for f, ph in self.d.items():
            # (O v)[s^f] += ph[s] v[s]
            out[s ^ f] += ph * v
        return out


def onsite_omega(x):
    O = Op()
    for (t, sg) in TERMS:
        O.add([g(x, a) for a in t], float(sg))
    return O


def bond_mirror(x, y):
    O = Op()
    for a in range(8):
        O.add([g(x, a), g(y, a)], 1j)
    return O


def bond_light(x, y):
    O = Op()
    for l in range(NL):
        O.add([lam(x, l), lam(y, l)], 1j)
    return O


def product_op(A, B):
    """A*B for commuting even operators given as Op (column convention)."""
    O = Op()
    s = mj.s
    for fa, pa in A.d.items():
        for fb, pb in B.d.items():
            # (A B v)[s^fb^fa] : B maps s -> s^fb with pb[s]; A maps s^fb -> s^fb^fa with pa[s^fb]
            ph = pa[s ^ fb] * pb
            f = fa ^ fb
            O.d[f] = O.d.get(f, 0) + ph
    return O


OMEGA = [onsite_omega(x) for x in range(NS)]
BM = {(x, y): bond_mirror(x, y) for (x, y, _, _) in bonds}
BL = {(x, y): bond_light(x, y) for (x, y, _, _) in bonds} if NL else {}
PAR = mj.parity().astype(float)


def build_H(W, u, t=1.0, tL=0.0, V1=0.0, V2=0.0, extra=None):
    H = Op()
    for x in range(NS):
        H.addop(OMEGA[x], W)
    for (x, y, ax, sg) in bonds:
        tb = t * (1 + u) if ax == "x" else t * (1 - u)
        H.addop(BM[(x, y)], sg * tb)
        if NL:
            tl = tL * (1 + u) if ax == "x" else tL * (1 - u)
            H.addop(BL[(x, y)], sg * tl)
            if V1:
                H.addop(product_op(BL[(x, y)], BM[(x, y)]), sg * V1)
            if V2:
                H.addop(product_op(OMEGA[x], BL[(x, y)]), sg * V2)
    if extra is not None:
        for (idx, c) in extra:
            H.add(idx, c)
    return H


def lowest(H, sector, k=3, shift=1e3, v0=None):
    """lowest k eigenpairs in parity sector (+1 even / -1 odd) via penalty."""
    pen = shift * (1 - sector * PAR) / 2

    def mv(v):
        return H.matvec(v) + pen * v
    L = sla.LinearOperator((DIM, DIM), matvec=mv, dtype=complex)
    if v0 is None:
        rng = np.random.default_rng(7)
        v0 = (rng.normal(size=DIM) + 0j) * (1 + sector * PAR) / 2
    ev, vec = sla.eigsh(L, k=k, which="SA", v0=v0, tol=1e-12, ncv=max(2 * k + 8, 24))
    o = np.argsort(ev)
    return ev[o], vec[:, o]


def _apply(f, ph, v):
    out = np.zeros(DIM, complex)
    out[mj.s ^ f] = ph * v
    return out


def _apply_dag(f, ph, v):
    return np.conj(ph) * v[mj.s ^ f]


def _site_parity_diag(x):
    pc = np.zeros(DIM, dtype=np.int64)
    for q in range(x * QPS, (x + 1) * QPS):
        pc += (mj.s >> q) & 1
    return 1 - 2 * (pc & 1)


def find_theta():
    """U (flip, phase) with U conj(gamma_m) U^dag = eps_site(m) gamma_m for all m."""
    f0, p0 = mj.string(list(range(0, mj.n_maj, 2)))
    Bdiag = np.ones(DIM)
    for x in range(NS):
        if eps[x] < 0:
            Bdiag = Bdiag * _site_parity_diag(x)
    rng = np.random.default_rng(3)
    v = rng.normal(size=DIM) + 1j * rng.normal(size=DIM)
    for cand in (p0, p0 * PAR[mj.s ^ f0] if False else p0):
        pass
    cands = []
    for usep in (False, True):
        for useb in (False, True):
            ph = p0.copy()
            # left-multiply by diagonal D: (D U)|s> = D[s^f] ph[s] |s^f>
            if usep:
                ph = ph * PAR[mj.s ^ f0]
            if useb:
                ph = ph * Bdiag[mj.s ^ f0]
            cands.append((usep, useb, ph))
    for usep, useb, ph in cands:
        ok = True
        for m in range(mj.n_maj):
            fm, pm = mj.op(m)
            e = eps[m // NM]
            # U conj(gamma) U^dag v
            w = _apply_dag(f0, ph, v)
            w = _apply(fm, np.conj(pm), w)
            w = _apply(f0, ph, w)
            if np.abs(w - e * _apply(fm, pm, v)).max() > 1e-12:
                ok = False
                break
        if ok:
            return f0, ph
    raise RuntimeError("Theta not found")


THETA = None


def theta_check(H):
    """max |Theta H Theta^-1 v - H v| on a random vector."""
    global THETA
    if THETA is None:
        THETA = find_theta()
    f0, ph = THETA
    rng = np.random.default_rng(5)
    v = rng.normal(size=DIM) + 1j * rng.normal(size=DIM)
    w = np.conj(_apply_dag(f0, ph, v))
    w = np.conj(H.matvec(w))
    w = _apply(f0, ph, w)
    return np.abs(w - H.matvec(v)).max()


def sector_gaps(W, u, **kw):
    H = build_H(W, u, **kw)
    ee, ve = lowest(H, +1, k=kw.pop("ke", 3) if False else 3)
    eo, vo = lowest(H, -1, k=2)
    return H, ee, ve, eo, vo


def mass_channel(H, E0, psi0, sites_same=True, gs_par=+1):
    """G_ab(x,y; i w=0) for all same-sublattice pairs (incl. x=y), mirror and light;
    psi0 even.  Returns max |G| over same-sublattice entries and over A-B entries."""
    nmaj = NS * NM
    pen = 1e3 * (1 + gs_par * PAR) / 2      # push ground-parity states up: gamma|0> lies in the other sector

    def mv(v):
        return H.matvec(v) - E0 * v + pen * v
    L = sla.LinearOperator((DIM, DIM), matvec=mv, dtype=complex)
    vs, phis = [], []
    for m in range(nmaj):
        f, ph = mj.op(m)
        v = np.zeros(DIM, complex)
        v[mj.s ^ f] = ph * psi0
        phi, info = sla.cg(L, v, rtol=1e-12, atol=0, maxiter=5000)
        assert info == 0, info
        vs.append(v)
        phis.append(phi)
    Gm = np.zeros((nmaj, nmaj), complex)
    for i in range(nmaj):
        for j in range(nmaj):
            Gm[i, j] = np.vdot(vs[j], phis[i]) - np.vdot(vs[i], phis[j])
    site = np.arange(nmaj) // NM
    e = np.array(eps)[site]
    same = np.equal.outer(e, e)
    return np.abs(Gm[same]).max(), np.abs(Gm[~same]).max(), Gm


if __name__ == "__main__":
    t0 = time.time()
    print(f"cluster {CL}: sites {NS}, eps {eps}, bonds {bonds}, light Majoranas/site {NL}, qubits {mj.nq}, dim {DIM}")
    # free single-particle spectrum of the bipartite hopping (per flavor)
    for u in (0.0, 0.1):
        A = np.zeros((NS, NS))
        for (x, y, ax, sg) in bonds:
            tb = (1 + u) if ax == "x" else (1 - u)
            A[x, y] += sg * tb
            A[y, x] -= sg * tb
        print(f"  u={u}: one-flavor single-particle levels of iA:", np.round(np.linalg.eigvalsh(1j * A), 6))
    if MODE == "scan":
        us = [0.0, 0.02, -0.02, 0.05]
        Ws = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0]
        print("\n W      u      E0_even      deg   gap_even    gap_odd(1-fermion)   ")
        rows = {}
        for W in Ws:
            for u in us:
                H = build_H(W, u)
                ee, ve = lowest(H, +1, k=3)
                eo, vo = lowest(H, -1, k=2)
                E0 = ee[0]
                deg = int(np.sum(np.abs(ee - E0) < 1e-9)) + int(np.sum(np.abs(eo - E0) < 1e-9))
                ge = ee[np.abs(ee - E0) > 1e-9][0] - E0 if np.any(np.abs(ee - E0) > 1e-9) else np.nan
                go = eo[0] - E0
                rows[(W, u)] = (E0, deg, ge, go, ve[:, 0])
                th = theta_check(H) if (u == 0.05 and W in (0.1, 10.0)) else float("nan")
                print(f" {W:<6} {u:+.2f}  {E0:+.10f}  {deg}   {ge:.10f}   {go:.10f}   Theta-res {th:.1e}")
        print("\n strain response at u=0 (finite difference, h=0.02 symmetric; check with 0.05 one-sided):")
        print(" W       Delta_odd(0)   d2_u Delta_odd   d2_u ln Delta_odd   d2_u Delta_even  d2_u ln Delta_even")
        for W in Ws:
            d0, dp, dm = rows[(W, 0.0)][3], rows[(W, 0.02)][3], rows[(W, -0.02)][3]
            e0, ep, em = rows[(W, 0.0)][2], rows[(W, 0.02)][2], rows[(W, -0.02)][2]
            d2 = (dp + dm - 2 * d0) / 0.02 ** 2
            e2 = (ep + em - 2 * e0) / 0.02 ** 2
            print(f" {W:<6}  {d0:.8f}    {d2:+.6e}    {d2 / d0:+.6e}      {e2:+.6e}   {e2 / e0:+.6e}")
        # mass channel at a few points
        print("\n mass channel G(i w=0): max |same-sublattice entries| (Theta forces 0), max |A-B entries|")
        for W in (0.1, 1.0, 10.0):
            for u in (0.0, 0.05):
                H = build_H(W, u)
                E0, deg, ge, go, psi = rows[(W, u)]
                if deg != 1:
                    print(f"  W={W} u={u}: degenerate ground state ({deg}); skipped")
                    continue
                ms, mab, _ = mass_channel(H, E0, psi)
                bil = 0.0
                for x in range(NS):
                    for a in range(8):
                        for b in range(a + 1, 8):
                            O = Op()
                            O.add([g(x, a), g(x, b)], 1j)
                            bil = max(bil, abs(np.vdot(psi, O.matvec(psi))))
                print(f"  W={W:<5} u={u:+.2f}: same-sublattice max|G(0)| = {ms:.2e};  A-B max|G(0)| = {mab:.3e};"
                      f"  max onsite |<i g_a g_b>| = {bil:.1e}")
        # control: Theta-breaking onsite bilinear at site 0
        print("\n control: + m * i gamma_0(0) gamma_1(0) (Theta- and Spin(7)-breaking), W=1:")
        for u in (0.0, 0.05):
            for m in (1e-3, 1e-2):
                H = build_H(1.0, u, extra=[([g(0, 0), g(0, 1)], 1j * m)])
                ee, ve = lowest(H, +1, k=2)
                ms, mab, Gm = mass_channel(H, ee[0], ve[:, 0])
                ii = np.unravel_index(np.argmax(np.abs(Gm) * np.equal.outer(np.array(eps)[np.arange(NS * NM) // NM], np.array(eps)[np.arange(NS * NM) // NM])), Gm.shape); print(f"  u={u:+.2f} m={m:.0e}: same-sublattice max|G(0)| = {ms:.4e} at Majoranas {ii}")
    if MODE == "light":
        assert NL == 2
        print("\n light sector: 2 light Majoranas/site, tL=0.5; light zero modes from the chiral index |B|-|A| =", sum(1 for e in eps if e < 0) - sum(1 for e in eps if e > 0))
        print(" W     V1    V2    u      E0          split(lowest odd - lowest even)  next gap   Theta-res")
        for W in (0.1, 1.0, 10.0):
            for (V1, V2) in ((0.0, 0.0), (0.3, 0.0), (0.3, 0.2)):
                for u in (0.0, 0.05, 0.2):
                    H = build_H(W, u, tL=0.5, V1=V1, V2=V2)
                    ee, ve = lowest(H, +1, k=3)
                    eo, vo = lowest(H, -1, k=3)
                    allv = np.sort(np.concatenate([ee, eo]))
                    th = theta_check(H) if u == 0.2 else float("nan")
                    print(f" {W:<5} {V1:<5} {V2:<5} {u:+.2f}  {allv[0]:+.8f}  {eo[0] - ee[0]:+.3e}   {allv[2] - allv[1]:.6f}   {th:.1e}")
        print("\n control: + m * i lambda_0(1) lambda_1(1) (Theta-odd light mass at B site 1), W=1, V1=0.3, V2=0.2:")
        for u in (0.0, 0.05, 0.2):
            for m in (1e-3, 1e-2):
                H = build_H(1.0, u, tL=0.5, V1=0.3, V2=0.2, extra=[([lam(1, 0), lam(1, 1)], 1j * m)])
                ee, _ = lowest(H, +1, k=2)
                eo, _ = lowest(H, -1, k=2)
                # zero-mode weight on site 1 for one light flavor: |psi0(1)|^2 = t_y^2/(t_x^2+t_y^2)
                w1 = (1 - u) ** 2 / ((1 + u) ** 2 + (1 - u) ** 2)
                print(f"  u={u:+.2f} m={m:.0e}: splitting {abs(eo[0] - ee[0]):.6e};  2*m*|psi0(1)|^2 = {2 * m * w1:.6e}")
    if MODE == "randT":
        # replace the Spin(7) Cayley quartic by a random Theta-even onsite quartic (same at every site):
        # real combination of all 70 four-Majorana strings on the 8 mirror Majoranas (Spin(7) broken).
        import itertools
        rng = np.random.default_rng(11)
        quads = list(itertools.combinations(range(8), 4))
        cq = rng.normal(size=len(quads))
        RAND = []
        for x in range(NS):
            O = Op()
            for q, c in zip(quads, cq):
                O.add([g(x, a) for a in q], float(c))
            RAND.append(O)
        OMEGA[:] = RAND
        print("\n random Theta-even onsite quartic (Spin(7) broken); same scan as above")
        us = [0.0, 0.02, -0.02]
        for W in (0.01, 0.1, 1.0, 10.0):
            res = {}
            for u in us:
                H = build_H(W, u)
                ee, ve = lowest(H, +1, k=3)
                eo, vo = lowest(H, -1, k=2)
                E0 = min(ee[0], eo[0])
                deg = int(np.sum(np.abs(ee - E0) < 1e-9)) + int(np.sum(np.abs(eo - E0) < 1e-9))
                exc = np.sort(np.concatenate([ee, eo]))
                gap = exc[exc > E0 + 1e-9][0] - E0
                res[u] = (E0, deg, gap, ee, ve)
            d2 = (res[0.02][2] + res[-0.02][2] - 2 * res[0.0][2]) / 0.02 ** 2
            E0, deg, gap, ee, ve = res[0.0]
            line = f"  W={W:<5}: deg {deg}, gap {gap:.8f}, d2_u gap {d2:+.5e}, d2_u ln gap {d2 / gap:+.5e}"
            if deg == 1:
                eo0, vo0 = lowest(build_H(W, 0.0), -1, k=1)
                gp = +1 if abs(ee[0] - E0) < 1e-9 else -1
                psi = ve[:, 0] if gp > 0 else vo0[:, 0]
                ms, mab, _ = mass_channel(build_H(W, 0.0), E0, psi, gs_par=gp)
                line += f"; ground parity {gp:+d}"
                line += f"; same-sublattice max|G(0)| {ms:.1e} (A-B {mab:.2e}); Theta-res {theta_check(build_H(W, 0.05)):.1e}"
            print(line)
    print(f"time {time.time() - t0:.1f}s")
