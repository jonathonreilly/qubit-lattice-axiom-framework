#!/usr/bin/env python3
"""J:falsifier:PR8032 - finite-PW static-source energy note (PR #8032), a stated theorem's finite check: the volume-independent upper
bound (8) (and its explicit form (9)) on the excess energy Delta_R of the projected charged path trial C Omega, C = P W P, over the full
neutral ground Omega of H_R = P(K + V)P, together with its ingredients (1) E_e <= 8v and 1 - q <= theta, and the exact v = 0 value 4d/a.

The note executes one fixture: one plaquette, R = 1, a path of d = 1 link, a single coupling (t = 1/100); its runner computes Haar
contractions of explicit polynomials.  Here, with disjoint machinery, the same single plaquette is solved in the Peter-Weyl basis for
R = 1, 2, 3, paths of d = 1, 2, 3 links and a sweep of v:
  * SU(3) irreps (p, q), p + q <= R, are built as traceless symmetric tensors in (C^3)^p (x) (C^3*)^q (orthonormal bases by SVD; the
    generators T_A = Gell-Mann/sqrt2, Tr(T_A T_B) = delta_AB, Casimir 2c(p,q)/3, link energy e(p,q) = c(p,q)/a = (p^2+pq+q^2+3p+3q)/a);
  * the Clebsch-Gordan isometries fund (x) mu -> mu' and antifund (x) mu -> mu' are Casimir eigenspaces of the product representation,
    matched to the standard bases by solving the intertwining equations (checked on random SU(3) elements);
  * gauge covariance makes all links of the path carry one irrep mu and all complement links one irrep nu (every internal vertex is
    bivalent and unsourced), so a state is a set of Peter-Weyl blocks F^{mu nu}[a,b,k,l,m,n] of two effective links U (path, kinetic
    weight d) and M (complement, weight 4 - d); multiplication by U_ab, by the Wilson loop Tr(UM) and by its conjugate act through the
    CG isometries; inner products by Schur orthogonality with the normalized colour trace Tr/3;
  * Omega = the lowest vector of H_R on the class functions chi_lambda(UM), |lambda| <= R (the neutral sector; it is the full-carrier
    ground when E_0 < 4/a, since any non-invariant state has a nontrivial link), q = ||P U Omega||^2, the trial energy exactly.
Validation: the R = 1 fixture's numbers (norms 1, 1/3, 1/9; J matrix [[0,1/18,1/54],[1/18,0,1/54],[1/54,1/54,0]]; the excess in (4, 4.01));
the loop-multiplication matrix on class functions against the Pieri rule.
HIT if Delta_R exceeds bound (8) (theta < 1) or bound (9) (theta_0 < 1) beyond 1e-9 relative, if E_e > 8v, if 1 - q > theta, or if the
v = 0 excess differs from 4d; a failed validation marks the run unreliable (printed, not a HIT on the note).
"""
import itertools
import math
import sys
import time

import numpy as np

rng = np.random.default_rng(8032)
TOL = 1e-9

# ---------------------------------------------------------------------------------------------------------------- SU(3) data
GM = [np.array(m, dtype=complex) for m in (
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], [[1 / math.sqrt(3), 0, 0], [0, 1 / math.sqrt(3), 0], [0, 0, -2 / math.sqrt(3)]])]
T = [m / math.sqrt(2) for m in GM]


def c_lab(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def dim_lab(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def rand_su3():
    z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2)
    Q, Rm = np.linalg.qr(z)
    Q = Q * (np.diag(Rm) / np.abs(np.diag(Rm)))
    return Q / np.linalg.det(Q) ** (1 / 3)


def slot_op(X, slot, n):
    mats = [np.eye(3)] * n
    mats = list(mats)
    mats[slot] = X
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


class Irrep:
    def __init__(self, p, q):
        self.p, self.q = p, q
        n = p + q
        N = 3 ** n
        if n == 0:
            self.E = np.ones((1, 1), dtype=complex)
        else:
            # symmetrizer over the upper slots and over the lower slots
            S = np.zeros((N, N))
            perms = [(pu, pl) for pu in itertools.permutations(range(p)) for pl in itertools.permutations(range(p, n))]
            I = np.eye(N).reshape((N,) + (3,) * n)
            for pu, pl in perms:
                S += I.transpose((0,) + tuple(1 + x for x in pu + pl)).reshape(N, N)
            S /= len(perms)
            w, V = np.linalg.eigh(S)
            Bs = V[:, w > 0.5]
            # contractions of an upper slot with a lower slot must vanish
            rows = []
            for i in range(p):
                for j in range(p, n):
                    Cm = np.zeros((3 ** (n - 2), N))
                    for idx in itertools.product(range(3), repeat=n):
                        if idx[i] == idx[j]:
                            rest = tuple(x for s, x in enumerate(idx) if s not in (i, j))
                            r = int(np.ravel_multi_index(rest, (3,) * (n - 2))) if n > 2 else 0
                            Cm[r, int(np.ravel_multi_index(idx, (3,) * n))] += 1
                    rows.append(Cm)
            if rows:
                Cst = np.vstack(rows) @ Bs
                u, s, vh = np.linalg.svd(Cst)
                null = vh[np.sum(s > 1e-10):].conj().T
                self.E = (Bs @ null).astype(complex)
            else:
                self.E = Bs.astype(complex)
        self.d = self.E.shape[1]
        assert self.d == dim_lab(p, q), (p, q, self.d)
        self.gen = [self.E.conj().T @ self.tensor_gen(X) @ self.E for X in T]

    def tensor_gen(self, X):
        n = self.p + self.q
        if n == 0:
            return np.zeros((1, 1), dtype=complex)
        return sum(slot_op(X, s, n) for s in range(self.p)) + sum(slot_op(-X.T, s, n) for s in range(self.p, n))

    def D(self, g):
        n = self.p + self.q
        out = np.array([[1.0 + 0j]])
        for s in range(n):
            out = np.kron(out, g if s < self.p else g.conj())
        return self.E.conj().T @ out @ self.E


def cg(irr, target, anti):
    """Isometry W (3, d_mu, d_mu') with (fund or antifund (x) D^mu)(g) W = W D^mu'(g)."""
    d = irr.d
    Xs = [np.kron(-X.T if anti else X, np.eye(d)) + np.kron(np.eye(3), G) for X, G in zip(T, irr.gen)]
    cas = sum(x @ x for x in Xs)
    w, V = np.linalg.eigh(cas)
    lam = 2 * c_lab(target.p, target.q) / 3
    B = V[:, np.abs(w - lam) < 1e-8]
    assert B.shape[1] == target.d, (irr.p, irr.q, target.p, target.q, B.shape)
    dt = target.d
    blocks = [np.kron(np.eye(dt), B.conj().T @ x @ B) - np.kron(G.T, np.eye(dt)) for x, G in zip(Xs, target.gen)]
    u, s, vh = np.linalg.svd(np.vstack(blocks))
    Rm = vh[-1].conj().reshape(dt, dt, order="F")
    assert s[-1] < 1e-8 and (len(s) < 2 or s[-2] > 1e-6)
    Rm = Rm * math.sqrt(dt / np.real(np.trace(Rm.conj().T @ Rm)))
    W = B @ Rm
    return W.reshape(3, d, dt)


# ---------------------------------------------------------------------------------------------------------------- the model
class Model:
    def __init__(self, R):
        self.R = R
        self.labs = [(p, q) for p in range(R + 1) for q in range(R + 1 - p)]
        self.irr = {l: Irrep(*l) for l in self.labs}
        self.CG = {}
        for l in self.labs:
            p, q = l
            for anti, outs in ((False, [(p + 1, q), (p - 1, q + 1), (p, q - 1)]), (True, [(p, q + 1), (p + 1, q - 1), (p - 1, q)])):
                for o in outs:
                    if min(o) >= 0 and sum(o) <= R:
                        self.CG[(l, o, anti)] = cg(self.irr[l], self.irr[o], anti)

    def check_cg(self):
        worst = 0.0
        for (l, o, anti), W in self.CG.items():
            g = rand_su3()
            Wm = W.reshape(3 * self.irr[l].d, self.irr[o].d)
            lhs = np.kron(g.conj() if anti else g, self.irr[l].D(g)) @ Wm
            worst = max(worst, np.abs(lhs - Wm @ self.irr[o].D(g)).max(), np.abs(Wm.conj().T @ Wm - np.eye(self.irr[o].d)).max())
        return worst

    def classfn(self, lab):
        d = self.irr[lab].d
        F = np.zeros((1, 1, d, d, d, d), dtype=complex)
        for k in range(d):
            for l in range(d):
                F[0, 0, k, l, l, k] = 1.0
        return {(lab, lab): F}

    def mulU(self, F):
        out = {}
        for (mu, nu), A in F.items():
            for (l, o, anti), W in self.CG.items():
                if l != mu or anti:
                    continue
                # colour indices: A is scalar (1,1); the product carries the path transporter's indices (a, b)
                new = np.einsum("akK,blL,klmn->abKLmn", W, W.conj(), A[0, 0])
                out[(o, nu)] = out.get((o, nu), 0) + new
        return out

    def mulLoop(self, F, anti):
        out = {}
        for (mu, nu), A in F.items():
            for (l1, o1, a1), WU in self.CG.items():
                if l1 != mu or a1 != anti:
                    continue
                X = np.einsum("ckK,dlL,abklmn->abcdKLmn", WU, WU.conj(), A)
                for (l2, o2, a2), WM in self.CG.items():
                    if l2 != nu or a2 != anti:
                        continue
                    new = np.einsum("abcdKLmn,dmM,cnN->abKLMN", X, WM, WM.conj())
                    out[(o1, o2)] = out.get((o1, o2), 0) + new
        return out

    def inner(self, F, G):
        s = 0.0
        for key, A in F.items():
            if key in G:
                B = G[key]
                s += np.vdot(A, B) / (self.irr[key[0]].d * self.irr[key[1]].d)
        cdim = next(iter(F.values())).shape[0]
        return s / cdim

    def kin(self, F, d):
        return {k: (d * c_lab(*k[0]) + (4 - d) * c_lab(*k[1])) * A for k, A in F.items()}

    @staticmethod
    def lin(a, F, b, G):
        out = {k: a * A for k, A in F.items()}
        for k, B in G.items():
            out[k] = out.get(k, 0) + b * B
        return out

    def neutral(self, v):
        basis = [self.classfn(l) for l in self.labs]
        n = len(basis)
        J = np.zeros((n, n))
        for j in range(n):
            chi = self.lin(1, self.mulLoop(basis[j], False), 1, self.mulLoop(basis[j], True))
            for i in range(n):
                J[i, j] = np.real(self.inner(basis[i], chi)) / 6
        H = np.diag([4.0 * c_lab(*l) for l in self.labs]) + v * (np.eye(n) - J)
        w, V = np.linalg.eigh(H)
        c = V[:, 0] * np.sign(V[0, 0])
        Om = {}
        for ci, b in zip(c, basis):
            Om = self.lin(1, Om, ci, b)
        return w[0], c, Om, J


def pieri_ok(model, J):
    """<chi_l'|(chi + chibar)/6|chi_l> = 1/6 iff l' in l (x) fund or l (x) antifund (Pieri), else 0."""
    ok = True
    for i, li in enumerate(model.labs):
        for j, lj in enumerate(model.labs):
            p, q = lj
            nb = {(p + 1, q), (p - 1, q + 1), (p, q - 1), (p, q + 1), (p + 1, q - 1), (p - 1, q)}
            ok = ok and abs(J[i, j] - (1 / 6 if li in nb else 0)) < 1e-12
    return ok


def main():
    t0 = time.time()
    hits, unreliable = [], []
    models = {R: Model(R) for R in (1, 2, 3)}
    cgerr = max(m.check_cg() for m in models.values())
    print(f"[setup] irreps p+q <= 3 as traceless symmetric tensors, {sum(len(m.CG) for m in models.values())} CG isometries; worst intertwining/"
          f"isometry defect on random SU(3) elements {cgerr:.1e}  ({time.time() - t0:.0f}s)")
    if cgerr > 1e-10:
        unreliable.append(f"CG defect {cgerr:.1e}")
    # ---------------------------------------------------------------- validation: the note's R = 1 fixture
    M1 = models[1]
    tt = 1 / 100
    v_fix = 96 * tt / (1 + tt - 2 * tt ** 2)
    E0, c, Om, J = M1.neutral(v_fix)
    Nn = 1 + 2 * tt ** 2
    fix_dev = max(abs(E0 - (v_fix - v_fix * tt / 3)), np.abs(c - np.array([1, tt, tt]) / math.sqrt(Nn)).max() if len(c) == 3 else 1.0)
    one = M1.classfn((0, 0))
    UA = M1.mulU(one)
    A = {((1, 0), (0, 0)): UA[((1, 0), (0, 0))]}
    Bf = M1.mulU(M1.classfn((1, 0)))
    B = {((0, 1), (1, 0)): Bf[((0, 1), (1, 0))]}
    Cf = M1.mulU(M1.classfn((0, 1)))
    C = {((0, 0), (0, 1)): Cf[((0, 0), (0, 1))]}
    vecs = [A, B, C]
    norms = [np.real(M1.inner(x, x)) for x in vecs]
    Jm = np.zeros((3, 3))
    for j, y in enumerate(vecs):
        ly = M1.lin(1, M1.mulLoop(y, False), 1, M1.mulLoop(y, True))
        for i, x in enumerate(vecs):
            Jm[i, j] = np.real(M1.inner(x, ly)) / 6
    Jref = np.array([[0, 1 / 18, 1 / 54], [1 / 18, 0, 1 / 54], [1 / 54, 1 / 54, 0]])
    Qn = 1 + 4 * tt ** 2 / 9
    Etr_formula = (4 + (20 / 3) * tt ** 2 + v_fix * (Qn - (4 * tt + tt ** 2) / 27)) / Qn
    trial = M1.mulU(Om)
    trial = {k: A_ for k, A_ in trial.items() if sum(k[0]) <= 1 and sum(k[1]) <= 1}
    qf = np.real(M1.inner(trial, trial))
    Hf = M1.lin(1, M1.kin(trial, 1), v_fix, trial)
    Hf = M1.lin(1, Hf, -v_fix / 6, M1.lin(1, M1.mulLoop(trial, False), 1, M1.mulLoop(trial, True)))
    Etr = np.real(M1.inner(trial, Hf)) / qf
    exc = Etr - E0
    val_ok = (fix_dev < 1e-12 and np.allclose(norms, [1, 1 / 3, 1 / 9], atol=1e-12) and np.allclose(Jm, Jref, atol=1e-12)
              and abs(Etr - Etr_formula) < 1e-12 and 4 < exc < 4.01 and pieri_ok(M1, J))
    print(f"[validation] R = 1 fixture (t = 1/100, v = {v_fix:.10f}): Omega = (1, t, t)/sqrt(N) and E_0 = v - vt/3 to {fix_dev:.1e}; "
          f"norms {', '.join(f'{x:.12f}' for x in norms)}; J matrix max deviation from [[0,1/18,1/54],...] {np.abs(Jm - Jref).max():.1e}; "
          f"trial energy {Etr:.12f} vs the note's formula {Etr_formula:.12f}; excess {exc:.9f} in (4, 4.01): {4 < exc < 4.01}; Pieri: {pieri_ok(M1, J)}")
    if not val_ok:
        unreliable.append("the R = 1 fixture is not reproduced")
    # ---------------------------------------------------------------- the sweep
    vs = [0.0, 0.01, 0.03, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0]
    rows = []
    worst8 = (0.0, None)
    worst9 = (0.0, None)
    worst1 = (0.0, None)
    worst8p = (0.0, None)
    worst9p = (0.0, None)
    n8 = n9 = nprem = 0
    for R, Mo in models.items():
        eR = R * R - (R * R) // 4 + 3 * R
        for v in vs:
            E0, c, Om, J = Mo.neutral(v)
            if not pieri_ok(Mo, J):
                unreliable.append(f"Pieri check fails at R = {R}")
            Ee = sum(ci ** 2 * c_lab(*l) for ci, l in zip(c, Mo.labs))
            premise = E0 < 4 - 1e-12
            if not premise:
                continue
            nprem += 1
            if Ee > 8 * v * (1 + TOL) + 1e-12:
                hits.append(f"(1) fails: R = {R}, v = {v}: E_e = {Ee:.6e} > 8v = {8 * v:.6e}")
            if v > 0:
                r1 = Ee / (8 * v)
                if r1 > worst1[0]:
                    worst1 = (r1, (R, v))
            UO = Mo.mulU(Om)
            trial = {k: A_ for k, A_ in UO.items() if sum(k[0]) <= R and sum(k[1]) <= R}
            q = np.real(Mo.inner(trial, trial))
            lp = Mo.lin(1, Mo.mulLoop(trial, False), 1, Mo.mulLoop(trial, True))
            for d in (1, 2, 3):
                Hq = Mo.lin(1, Mo.kin(trial, d), v, trial)
                Hq = Mo.lin(1, Hq, -v / 6, lp)
                Etr = np.real(Mo.inner(trial, Hq)) / q
                E0d = E0          # the neutral ground does not depend on how the four links are split into path and complement
                Delta = Etr - E0d
                Epath, Eface = d * Ee, 4 * Ee
                theta = Epath / eR
                if 1 - q > theta + 1e-12:
                    hits.append(f"1 - q > theta: R = {R}, d = {d}, v = {v}: {1 - q:.6e} > {theta:.6e}")
                if v == 0 and abs(Delta - 4 * d) > 1e-9:
                    hits.append(f"v = 0: Delta = {Delta:.12f} != 4d = {4 * d}")
                b8 = None
                if theta < 1:
                    n8 += 1
                    b8 = (4 * d + math.sqrt(theta) * (4 * d + 4 * math.sqrt(d * Epath)) + 2 * v * (math.sqrt(Eface / eR) + math.sqrt(theta))) / (1 - theta)
                    if Delta / b8 > worst8[0]:
                        worst8 = (Delta / b8, (R, d, v, Delta, b8))
                    if v > 0 and Delta / b8 > worst8p[0]:
                        worst8p = (Delta / b8, (R, d, v, Delta, b8))
                    if Delta > b8 * (1 + TOL):
                        hits.append(f"bound (8) fails: R = {R}, d = {d}, v = {v}: Delta = {Delta:.9f} > {b8:.9f}")
                th0 = 8 * v * d / eR
                b9 = None
                if th0 < 1:
                    n9 += 1
                    b9 = (4 * d + math.sqrt(th0) * (4 * d + 4 * d * math.sqrt(8 * v)) + 8 * v * d * (math.sqrt(32 * v / eR) + math.sqrt(th0))) / (1 - th0)
                    if Delta / b9 > worst9[0]:
                        worst9 = (Delta / b9, (R, d, v, Delta, b9))
                    if v > 0 and Delta / b9 > worst9p[0]:
                        worst9p = (Delta / b9, (R, d, v, Delta, b9))
                    if Delta > b9 * (1 + TOL):
                        hits.append(f"bound (9) fails: R = {R}, d = {d}, v = {v}: Delta = {Delta:.9f} > {b9:.9f}")
                rows.append((R, d, v, E0, Ee, q, Delta, b8, b9))
        print(f"[sweep] R = {R} (e_R = {eR}): {sum(1 for r in rows if r[0] == R)} (d, v) cases with the full-carrier premise E_0 < 4  ({time.time() - t0:.0f}s)")
    for R in (1, 2, 3):
        sel = [r for r in rows if r[0] == R and r[1] == 1]
        print(f"[table R={R}, d=1] " + "; ".join(f"v={r[2]:g}: E0={r[3]:.4f} E_e={r[4]:.4f} q={r[5]:.6f} Delta={r[6]:.6f} (8)={'%.4f' % r[7] if r[7] else '-'}"
                                                   f" (9)={'%.4f' % r[8] if r[8] else '-'}" for r in sel))
    print(f"[bounds] {nprem} (R, v) neutral grounds with E_0 < 4; bound (8) applicable (theta < 1) in {n8} (R, d, v) cases: largest Delta/bound = "
          f"{worst8[0]:.6f} at R = {worst8[1][0]}, d = {worst8[1][1]}, v = {worst8[1][2]} (Delta {worst8[1][3]:.6f}, bound {worst8[1][4]:.6f}); bound (9) "
          f"(theta_0 < 1) in {n9}: largest ratio {worst9[0]:.6f} at R = {worst9[1][0]}, d = {worst9[1][1]}, v = {worst9[1][2]}; (1): largest E_e/(8v) = "
          f"{worst1[0]:.6f} at R = {worst1[1][0]}, v = {worst1[1][1]}")
    print(f"[bounds] v > 0 only (v = 0 is the equality Delta = 4d = bound): largest Delta/(8) = {worst8p[0]:.6f} at R = {worst8p[1][0]}, d = "
          f"{worst8p[1][1]}, v = {worst8p[1][2]} (Delta {worst8p[1][3]:.6f}, bound {worst8p[1][4]:.6f}); largest Delta/(9) = {worst9p[0]:.6f} at "
          f"R = {worst9p[1][0]}, d = {worst9p[1][1]}, v = {worst9p[1][2]}")
    print(f"[time] {time.time() - t0:.0f}s")
    for u in unreliable:
        print(f"UNRELIABLE: {u}")
    for h in hits[:10]:
        print("HIT: " + h)
    print(f"SUMMARY: single plaquette in the Peter-Weyl basis (explicit SU(3) irreps and CG isometries; R = 1 fixture reproduced: "
          f"{'yes' if val_ok else 'NO'}): R = 1, 2, 3, paths d = 1, 2, 3, {len(vs)} couplings; bound (8) at {n8} cases, largest Delta_R/bound "
          f"{worst8[0]:.4f} (the v = 0 equality; {worst8p[0]:.6f} at v > 0); bound (9) at {n9} cases, largest ratio {worst9[0]:.4f} ({worst9p[0]:.6f} at v > 0); (1) largest E_e/(8v) {worst1[0]:.4f}; v = 0 excess = 4d; "
          f"{len(hits)} violations; falsifier {'FIRES' if hits else 'does not fire'}{' (UNRELIABLE run)' if unreliable else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
