#!/usr/bin/env python3
"""Check of the long-distance formula (3.13) of Text 3.14 on the actual Wilson lattice, with real far fields.

Torus T. A cell of side L at the origin, a far plaquette b at distance R, another plaquette q at distance D, both in generic planes. E_b := G J_b, E_q := G J_q in Feynman gauge.
On the cell let A := E_b + d t_extra, with t_extra chosen below. Let t_tot be the least-squares solution of d t_tot = A - e_F on the cell, F the flux of E_b at the cell centre. For J in NN := {J in Z(cell): rho(J, A) = 0, J perp PP_h},

    LHS(J) := VV(G J, E_q, E_b) - <J, tbar_extra E_q>,   the exact torus sum,
    RHS(J) := m_J(F') = <J, P[e_F', F] - tbar_tot e_F'>,   F' the flux of E_q at the cell centre.

(3.13) says LHS = RHS (1 + O(L / D) + O(L / R)). LHS does not see the gauge of E_q on NN.

First run, T = 28: C3 failed, because Moment.kernel used one rank tolerance for density rows of size 1e-5 and moment rows of size 10, so the kernel was not a kernel. Fixed by normalising A in the kernel. Second run, T = 36: C3 still failed. Tolerance tightened to 1e-13, with no change. Debug: rho was 1e-15 relative, but H G J - J was 7e-9, because the momenta were in single precision. So the failure of C3 was in the Green's function of this script. Now double precision. Criteria unchanged.

PRE-REGISTERED CRITERIA (written before the first run).
 C1: on the J of largest |RHS| among a basis of NN, for the worst case of the listed geometries at the largest D, R on the torus: 0.5 < LHS / RHS < 1.5. FAIL means (3.13) is wrong as stated or the corrections are larger than estimated.
 C2: the deviation |LHS / RHS - 1| decreases when D and R grow by a factor at least 1.5 at fixed T. If it does not, report; torus effects may compete.
 RESULT at L = 5, T = 36 with double precision: C1 FAILS (ratios -0.47, -0.73, 1.02; 0.78, -1.21, 1.57; 2.78, 3.36, 7.05; 3.22, -0.76, 1.14 at |z| = 13, 9, 13, 9). C2 not seen. C3 holds to 4e-9, above its stated 1e-10, on LHS of size 1e-12, which I take as round-off of cancelling terms of size 1e-6.
    Reading: the dipole field has |grad F| / |F| = 4 / |z|, so on a box of half-size 2.5 the expansion parameter is 0.8 at |z| = 13. This test cannot reach the regime at L = 5 on a torus of this size. Not a confirmation of (3.13).
 C1', C2' (written before the run at L = 3, where the parameter is 0.3 at |z| = 13): same criteria at L = 3, T = 36. If C1' fails too, (3.13) is in doubt and must be re-derived term by term.
 NOTE after re-deriving (3.13) term by term: the test above is not the statement. It takes J' = a plaquette, which is not in N_j, so VV(G J, E_q, E_b) has a term from the charge rho(J_q, E_b) at q, larger than the main term by R / L. That is what (3.12) removes by J' in N_j. The charge at the far plaquette, rho(J_b, E_J'), also adds a term of rank at most 4 in (J, J'), of the same type as Far_b; it does not harm the rank argument but it must be removed in a test.
 C1'' (written before its run), mode "matrix": J in NN on cell 1, J' in N on cell 2 at distance D, combinations of J' with no field on the far plaquette. Matrix Mat := VV(G J, G J', E_b) against Pred := m_J(F'(J')). Pass: |Mat - Pred| / |Pred| < 0.5 in the Frobenius norm at L = 3 for all listed geometries on T = 36. Fail means (3.13) must be re-derived.
 C3: gauge independence on NN: LHS changes by less than 1e-10 relative under E_q -> E_q + d X with X random on the cell.
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import itertools
import resource
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_rank_moment import Moment, PLANES  # noqa: E402


def check_rss(limit_gb=2.0):
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3
    if r > limit_gb:
        raise MemoryError(f"rss {r:.2f} GB")
    return r


class TorusField:
    def __init__(self, T):
        self.T = T
        self.shape = (T,) * 4
        idx = np.indices(self.shape, dtype=np.float64)
        k2 = sum(4 * np.sin(np.pi * idx[m] / T) ** 2 for m in range(4))
        k2[0, 0, 0, 0] = 1.0
        self.inv = 1.0 / k2
        self.inv[0, 0, 0, 0] = 0.0

    def G(self, J):
        return np.fft.ifftn(np.fft.fftn(J, axes=(1, 2, 3, 4)) * self.inv, axes=(1, 2, 3, 4)).real

    def plaquette(self, x, mu, nu):
        J = np.zeros((4,) + self.shape)
        xm = list(x)
        xm[mu] = (xm[mu] + 1) % self.T
        xn = list(x)
        xn[nu] = (xn[nu] + 1) % self.T
        J[(mu,) + tuple(x)] += 1
        J[(nu,) + tuple(xm)] += 1
        J[(mu,) + tuple(xn)] -= 1
        J[(nu,) + tuple(x)] -= 1
        return J

    def flux_at(self, E, c):
        """Mean flux over the unit cells around the real point c, in the order of PLANES, with the sign of a_nu = x_mu: flux of (mu, nu) plaquette = E_mu(x) + E_nu(x + mu) - E_mu(x + nu) - E_nu(x)."""
        out = np.zeros(6)
        base = [int(np.floor(v)) for v in c]
        corners = list(itertools.product(*[(b, b + 1) if abs(v - b) > 1e-9 else (b,) for b, v in zip(base, c)]))
        for k, (mu, nu) in enumerate(PLANES):
            val = 0.0
            cnt = 0
            for x in corners:
                x = [v % self.T for v in x]
                xm = list(x)
                xm[mu] = (xm[mu] + 1) % self.T
                xn = list(x)
                xn[nu] = (xn[nu] + 1) % self.T
                val += E[(mu,) + tuple(x)] + E[(nu,) + tuple(xm)] - E[(mu,) + tuple(xn)] - E[(nu,) + tuple(x)]
                cnt += 1
            out[k] = val / cnt
        return out

    def VV(self, a, b, c):
        tot = 0.0
        for mu in range(4):
            for nu in range(mu + 1, 4):
                vals = []
                for f in (a, b, c):
                    fm, fn = f[mu], f[nu]
                    fnu = np.roll(fn, -1, axis=mu)
                    fmu = np.roll(fm, -1, axis=nu)
                    vals.append((fm + fnu - fmu - fn, 0.5 * (fm + fmu), 0.5 * (fn + fnu)))
                (p1, m1, n1), (p2, m2, n2), (p3, m3, n3) = vals
                tot += float(np.sum(p1 * (m2 * n3 - n2 * m3) - m1 * (p2 * n3 - n2 * p3) + n1 * (p2 * m3 - m2 * p3)))
        return tot


def on_cell(box, E):
    return np.array([E[(mu,) + x] for (x, mu) in box.links])


def to_torus(box, values, shape):
    out = np.zeros((4,) + shape)
    for v, (x, mu) in zip(values, box.links):
        out[(mu,) + x] = v
    return out


def run(T, L, geom, seed):
    rng = np.random.default_rng(seed)
    Mo = Moment(L)
    b = Mo.box
    tf = TorusField(T)
    zb, pb, zq, pq = geom
    t0 = time.time()
    Eb = tf.G(tf.plaquette(zb, *pb))
    Eq = tf.G(tf.plaquette(zq, *pq))
    c = Mo.c
    F = tf.flux_at(Eb, c)
    Fq = tf.flux_at(Eq, c)
    Ab = on_cell(b, Eb)
    # t_tot on the cell
    e_F = F @ Mo.e
    Pinv = np.linalg.pinv(b.D0, rcond=1e-10)
    ttot = Pinv @ (Ab - e_F)
    mism = np.abs(Ab - e_F - b.D0 @ ttot).max() / np.abs(Ab - e_F).max()
    coef, worst = Mo.particular(F / np.linalg.norm(F))
    coef = coef * np.linalg.norm(F)
    tbar_tot = 0.5 * (ttot[Mo.ends[:, 0]] + ttot[Mo.ends[:, 1]])
    g = (Mo.poly.M @ coef.T).T - Mo.e * tbar_tot[None, :]  # 6 x W, for the unit fluxes
    Nz, rk = Mo.kernel(Ab, tol=1e-13)
    Jn = Nz @ Mo.Zb  # dim NN x W, orthonormal in Z basis
    mvals = Jn @ g.T  # dim NN x 6
    rhs = mvals @ Fq
    order = np.argsort(-np.abs(rhs))[:3]
    print(f"T={T} L={L} |z_b|={np.linalg.norm(np.array(zb)-c):.1f} |z_q|={np.linalg.norm(np.array(zq)-c):.1f} planes {pb} {pq}: |F|={np.linalg.norm(F):.2e} |F'|={np.linalg.norm(Fq):.2e} max|t_tot|={np.abs(ttot).max():.2e} mismatch of uniform flux {mism:.1e} dim NN={Nz.shape[0]} setup {time.time()-t0:.0f}s rss={check_rss():.2f}GB", flush=True)
    ratios = []
    for i in order:
        Jt = to_torus(b, Jn[i], tf.shape)
        EJ = tf.G(Jt)
        lhs = tf.VV(EJ, Eq, Eb)
        # gauge independence: add d X on the cell to E_q, X random, zero outside
        X = np.zeros(tf.shape)
        for x in b.sites:
            X[x] = rng.normal()
        dX = np.array([np.roll(X, -1, axis=m) - X for m in range(4)])
        lhs2 = tf.VV(EJ, Eq + 0.1 * dX, Eb)
        ratios.append(lhs / rhs[i])
        print(f"   J {i}: LHS={lhs:.4e} RHS={rhs[i]:.4e} ratio={lhs/rhs[i]:.3f}; change of LHS under a gauge of E_q: {abs(lhs2-lhs)/max(abs(lhs),1e-300):.1e} rss={check_rss():.2f}GB", flush=True)
    return ratios


def main():
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 28
    L = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    H = T // 2
    geoms = [
        ((H - 3, 2, 2, 0), (2, 3), (2, H - 3, 0, 2), (0, 2)),
        ((H // 2 + 2, 2, 2, 0), (2, 3), (2, H // 2 + 2, 0, 2), (0, 2)),
        ((H - 3, 2, 0, 2), (1, 2), (2, H - 3, 2, 0), (0, 3)),
        ((H // 2 + 2, 2, 0, 2), (1, 2), (2, H // 2 + 2, 2, 0), (0, 3)),
    ]
    for k, g in enumerate(geoms):
        run(T, L, g, 10 + k)




def run_matrix(T, L, zc2, zb, pb, nrows, ncols, seed):
    """The statement itself: J in NN on cell 1, J' in N on cell 2 with no charge on b; matrix VV(G J, G J', E_b) against m_J(F'(J'))."""
    rng = np.random.default_rng(seed)
    Mo = Moment(L)
    b = Mo.box
    tf = TorusField(T)
    t0 = time.time()
    Jb = tf.plaquette(zb, *pb)
    Eb = tf.G(Jb)
    c = Mo.c
    F = tf.flux_at(Eb, c)
    Ab = on_cell(b, Eb)
    e_F = F @ Mo.e
    Pinv = np.linalg.pinv(b.D0, rcond=1e-10)
    ttot = Pinv @ (Ab - e_F)
    coef, worst = Mo.particular(F / np.linalg.norm(F))
    coef = coef * np.linalg.norm(F)
    tbar_tot = 0.5 * (ttot[Mo.ends[:, 0]] + ttot[Mo.ends[:, 1]])
    g = (Mo.poly.M @ coef.T).T - Mo.e * tbar_tot[None, :]
    Nz, rk = Mo.kernel(Ab, tol=1e-13)
    Jn = Nz @ Mo.Zb
    mvals = Jn @ g.T  # dim NN x 6
    U, s, Vt = np.linalg.svd(mvals, full_matrices=False)
    rows = (U[:, :nrows].T @ Jn)  # combinations of NN carrying the largest m
    rows_m = rows @ g.T
    # cell 2: N only, from the densities of E_b there
    shift = tuple(zc2)
    Eb2 = np.array([np.roll(Eb[m], tuple(-v for v in shift), axis=(0, 1, 2, 3)) for m in range(4)])
    A2 = on_cell(b, Eb2)
    A2n = A2 / np.abs(A2).max()
    prod = Mo.Zb * A2n[None, :]
    R = np.zeros((b.V, Mo.n))
    for i in range(b.W):
        xa, xb = Mo.ends[i]
        R[xa] += 0.5 * prod[:, i]
        R[xb] += 0.5 * prod[:, i]
    U2, s2, Vt2 = np.linalg.svd(R, full_matrices=True)
    rk2 = int(np.sum(s2 > 1e-13 * s2[0]))
    N2 = Vt2[rk2:] @ Mo.Zb
    dip2 = N2 @ Mo.e.T
    Ud, sd, Vd = np.linalg.svd(dip2, full_matrices=False)
    cols0 = Ud[:, :ncols].T @ N2
    print(f"T={T} L={L}: z_2={zc2} z_b={zb} plane {pb}: |F|={np.linalg.norm(F):.2e} max|t_tot|={np.abs(ttot).max():.1e}; dim NN={Nz.shape[0]}, sv of m on NN " + " ".join(f"{v:.1e}" for v in s[:6]) + f"; dim N_2={N2.shape[0]}, sv of dip " + " ".join(f"{v:.1e}" for v in sd[:6]) + f"; setup {time.time()-t0:.0f}s", flush=True)
    Fields = []
    charges = []
    fluxes = []
    for j in range(cols0.shape[0]):
        Jt = to_torus(b, cols0[j], tf.shape)
        Jt = np.array([np.roll(Jt[m], shift, axis=(0, 1, 2, 3)) for m in range(4)])
        E = tf.G(Jt)
        Fields.append(E)
        # densities of E on the far plaquette: three independent numbers matter; use its four links
        vals = []
        x = list(zb)
        mu, nu = pb
        xm = list(x)
        xm[mu] += 1
        xn = list(x)
        xn[nu] += 1
        for m_, y in ((mu, x), (nu, xm), (mu, xn), (nu, x)):
            vals.append(E[(m_,) + tuple(v % T for v in y)])
        charges.append(vals)
        fluxes.append(tf.flux_at(E, c))
        check_rss()
    charges = np.array(charges)
    fluxes = np.array(fluxes)
    # combinations of the columns with no density on the far plaquette
    Uc, sc, Vc = np.linalg.svd(charges, full_matrices=True)
    rc = int(np.sum(sc > 1e-10 * sc[0]))
    combo = Uc[:, rc:].T  # (ncols - rc) x ncols
    if combo.shape[0] == 0:
        print("   no columns left", flush=True)
        return None
    Flc = combo @ fluxes
    Mat = np.zeros((rows.shape[0], combo.shape[0]))
    Pred = rows_m @ Flc.T
    for i in range(rows.shape[0]):
        Jt = to_torus(b, rows[i], tf.shape)
        EJ = tf.G(Jt)
        vals = np.array([tf.VV(EJ, Fields[j], Eb) for j in range(len(Fields))])
        Mat[i] = combo @ vals
        check_rss()
    err = np.linalg.norm(Mat - Pred) / np.linalg.norm(Pred)
    sM = np.linalg.svd(Mat, compute_uv=False)
    sP = np.linalg.svd(Pred, compute_uv=False)
    print(f"   columns kept {combo.shape[0]} of {cols0.shape[0]}; |Mat - Pred| / |Pred| = {err:.3f}; sv Mat " + " ".join(f"{v:.2e}" for v in sM[:5]) + "; sv Pred " + " ".join(f"{v:.2e}" for v in sP[:5]) + f"; time {time.time()-t0:.0f}s rss={check_rss():.2f}GB", flush=True)
    return err


def main_matrix():
    T = int(sys.argv[2])
    L = int(sys.argv[3])
    H = T // 2
    for k, (z2, zb, pb) in enumerate([
        ((2, H - 1, 0, 2), (H - 2, 2, 2, 0), (2, 3)),
        ((2, H - 1, 2, 0), (H - 2, 2, 0, 2), (1, 2)),
        ((2, H // 2 + 2, 0, 2), (H - 2, 2, 2, 0), (2, 3)),
    ]):
        run_matrix(T, L, z2, zb, pb, 4, 9, 20 + k)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "matrix":
        main_matrix()
    else:
        main()
