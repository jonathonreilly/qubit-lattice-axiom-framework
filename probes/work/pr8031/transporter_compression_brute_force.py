#!/usr/bin/env python3
"""J:attack:PR8031 - finite-transporter note (PR #8031), attack pattern (f) NORMALIZATION: the compressed Haar transporter
U_R = P_R U P_R of (U psi)_i(g) = sum_j g_ij psi_j(g) on L2(SU3) x C^3, recomputed by brute force in an explicit Peter-Weyl basis at
R = 1, 2, 3 (the runner builds R = 1 only: 19 link basis states x 3 colours):
  * D_R = I - U_R* U_R = P_R U* (I - P_R) U P_R from the leaked blocks (p + q = R + 1), with U_R* U_R + D_R = I checked;
    0 <= D_R <= T_R = P_R - P_(R-1) (D_R vanishes on the interior), ||D_R|| = 1 and the witness psi_R = sqrt(d_(R,0)) g_11^R e_1 with
    U_R psi_R = 0; the left defect I - U_R U_R* on the same shell; the spectrum of D_R (for comparison: the projector onto the
    (p+1, q) part of the input's colour x right-index space predicts eigenvalues 0 and 1 with multiplicity sum_(p+q=R) d_(p,q) d_(p+1,q));
  * the energy bound (2): <psi, D_R psi> <= <psi, K psi>/g_(R-1), g_(R-1) = [R^2 - floor(R^2/4) + 3R]/a, on random states and at its
    sharp maximum over each shell irrep;
  * distinct-link paths: W_R (product of compressed link matrices, adjoints by orientation) = P W P and
    ||W psi - W_R psi||^2 <= sum_e <psi, T_(R,e) psi> for random states entangled across links, colour and a reference qubit, at R = 1
    with two and three links;
  * g_(R-1) against the brute-force minimum of the link energy on the shell p + q = R, R <= 60.
HIT if an identity fails beyond 1e-10 or a stated bound is exceeded.
"""
import itertools
import math
import sys
import time

import numpy as np

rng = np.random.default_rng(8031)

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




def labels(R):
    return [(p, q) for p in range(R + 1) for q in range(R + 1 - p)]


class LinkSpace:
    """Ran P_R: orthonormal basis sqrt(d_mu) D^mu_ab(g) e_j, flattened block by block (mu, a, b, j)."""

    def __init__(self, R):
        self.R = R
        self.labs = labels(R + 1)
        self.irr = {l: Irrep(*l) for l in self.labs}
        self.inside = [l for l in self.labs if sum(l) <= R]
        self.leak = [l for l in self.labs if sum(l) == R + 1]
        self.offset, n = {}, 0
        for l in self.inside:
            self.offset[l] = n
            n += self.irr[l].d ** 2 * 3
        self.dim = n
        self.loff, m = {}, 0
        for l in self.leak:
            self.loff[l] = m
            m += self.irr[l].d ** 2 * 3
        self.ldim = m
        self.cg = {}
        for l in self.inside:
            p, q = l
            for anti, outs in ((False, [(p + 1, q), (p - 1, q + 1), (p, q - 1)]), (True, [(p, q + 1), (p + 1, q - 1), (p - 1, q)])):
                for o in outs:
                    if min(o) >= 0 and sum(o) <= R + 1:
                        self.cg[(l, o, anti)] = cg(self.irr[l], self.irr[o], anti)

    def energy(self, l):
        return c_lab(*l)

    def transporter(self, adjoint=False):
        """Matrices of P_R U P_R (dim x dim) and of (I - P_R) U P_R (ldim x dim) in the orthonormal bases; U* when adjoint:
        (U* psi)_i = sum_j conj(g_ji) psi_j, i.e. antifundamental entries with the colour indices transposed."""
        Uin = np.zeros((self.dim, self.dim), dtype=complex)
        Ul = np.zeros((self.ldim, self.dim), dtype=complex)
        for l in self.inside:
            d = self.irr[l].d
            for (l1, o, anti), W in self.cg.items():
                if l1 != l or anti != adjoint:
                    continue
                do = self.irr[o].d
                # input basis vector (a, b, j): c_ab,j -> output c'_KL,i = W[i,a,K] conj(W[j,b,L]) (entry g_ij), or for the adjoint the
                # entry conj(g_ji) = D^anti_(j i): W[j,a,K] conj(W[i,b,L])
                if not adjoint:
                    T = np.einsum("iaK,jbL->KLiabj", W, W.conj())
                else:
                    T = np.einsum("jaK,ibL->KLiabj", W, W.conj())
                T = T * math.sqrt(d) / math.sqrt(do) if False else T
                # orthonormal normalisation: input sqrt(d) D^l, output sqrt(do) D^o => factor sqrt(do/d)^-1 ... computed below
                fac = math.sqrt(d / do)
                block = (T * (1 / fac)).reshape(do * do * 3, d * d * 3) if False else T.reshape(do * do * 3, d * d * 3) * math.sqrt(do / d) ** 0
                block = T.reshape(do * do * 3, d * d * 3) * math.sqrt(d) / math.sqrt(do)
                if sum(o) <= self.R:
                    Uin[self.offset[o]:self.offset[o] + do * do * 3, self.offset[l]:self.offset[l] + d * d * 3] += block
                else:
                    Ul[self.loff[o]:self.loff[o] + do * do * 3, self.offset[l]:self.offset[l] + d * d * 3] += block
        return Uin, Ul

    def shell_mask(self):
        m = np.zeros(self.dim, dtype=bool)
        for l in self.inside:
            if sum(l) == self.R:
                d = self.irr[l].d
                m[self.offset[l]:self.offset[l] + d * d * 3] = True
        return m

    def K_diag(self):
        k = np.zeros(self.dim)
        for l in self.inside:
            d = self.irr[l].d
            k[self.offset[l]:self.offset[l] + d * d * 3] = c_lab(*l)
        return k

    def witness(self):
        R = self.R
        irr = self.irr[(R, 0)]
        e1 = np.zeros(3 ** R, dtype=complex)
        e1[0] = 1.0                                   # e_1 tensor ... tensor e_1
        x = irr.E.conj().T @ e1
        d = irr.d
        c = np.einsum("a,b->ab", x.conj(), x)          # g_11^R = sum_ab conj(x_a) D_ab x_b
        v = np.zeros(self.dim, dtype=complex)
        blk = np.zeros((d, d, 3), dtype=complex)
        blk[:, :, 0] = c * math.sqrt(d)                # psi_R = sqrt(d_(R,0)) g_11^R e_1, coefficient c/sqrt(d) per orthonormal element... see below
        # orthonormal coordinates: psi = sum c_ab D_ab * sqrt(d) e_1 = sum (c_ab) (sqrt(d) D_ab) e_1
        blk[:, :, 0] = c
        v[self.offset[(R, 0)]:self.offset[(R, 0)] + d * d * 3] = blk.reshape(-1)
        return v


def main():
    t0 = time.time()
    hits = []
    worst_unit, worst_int, worst_left = 0.0, 0.0, 0.0
    for R in (1, 2, 3):
        L = LinkSpace(R)
        Uin, Ul = L.transporter()
        unit = np.abs(Uin.conj().T @ Uin + Ul.conj().T @ Ul - np.eye(L.dim)).max()
        D = Ul.conj().T @ Ul                              # D_R = P_R U* (I - P_R) U P_R
        D2 = np.eye(L.dim) - Uin.conj().T @ Uin
        shell = L.shell_mask()
        interior = np.abs(D[~shell][:, ~shell]).max() if (~shell).any() else 0.0
        offd = np.abs(D[~shell][:, shell]).max() if (~shell).any() else 0.0
        ev = np.linalg.eigvalsh((D + D.conj().T) / 2)
        ones = int(np.sum(np.abs(ev - 1) < 1e-9))
        zeros = int(np.sum(np.abs(ev) < 1e-9))
        pred = sum(dim_lab(p, q) * dim_lab(p + 1, q) for (p, q) in labels(R) if p + q == R) * 1
        pred_colour = pred                                   # left index d_(p,q) x the (p+1,q) part of colour x right index
        w = L.witness()
        wn = np.linalg.norm(w)
        Uw = np.linalg.norm(Uin @ w)
        Dw = np.linalg.norm(D @ w - w)
        # left defect I - U_R U_R*
        Uadj_in, Uadj_l = L.transporter(adjoint=True)
        Dl = np.eye(L.dim) - Uin @ Uin.conj().T
        left_int = np.abs(Dl[~shell][:, ~shell]).max() if (~shell).any() else 0.0
        left_norm = np.linalg.eigvalsh((Dl + Dl.conj().T) / 2)[-1]
        adj_ok = np.abs(Uadj_in - Uin.conj().T).max()
        # energy bound (2): max of <D>/<K> times g over the shell, and random states
        g = R * R - (R * R) // 4 + 3 * R
        Kd = L.K_diag()
        gen = np.linalg.eigvalsh(np.diag(1 / np.sqrt(Kd[shell])) @ D[shell][:, shell] @ np.diag(1 / np.sqrt(Kd[shell])))[-1] * g
        rnd = 0.0
        for _ in range(200):
            psi = rng.normal(size=L.dim) + 1j * rng.normal(size=L.dim)
            psi /= np.linalg.norm(psi)
            rnd = max(rnd, np.real(psi.conj() @ D @ psi) / (np.real(psi.conj() @ (Kd * psi)) / g))
        print(f"[R={R}] Ran P_R dimension {L.dim} (= 3 x {L.dim // 3}); |U_R*U_R + D_R - I| = {unit:.1e}; D_R on the interior {interior:.1e}, "
              f"interior-shell {offd:.1e}; spectrum of D_R: {ones} eigenvalues 1, {zeros} eigenvalues 0 (of {L.dim}; predicted {pred} ones); "
              f"witness: |psi_R| = {wn:.12f}, |U_R psi_R| = {Uw:.1e}, |D_R psi_R - psi_R| = {Dw:.1e}; left defect: interior {left_int:.1e}, "
              f"norm {left_norm:.12f}; compressed adjoint = (U_R)* to {adj_ok:.1e}; energy bound (2) with g = {g}: max <D>/(<K>/g) over the shell "
              f"{gen:.12f}, over 200 random states {rnd:.6f}  ({time.time() - t0:.0f}s)")
        ok = (unit < 1e-10 and interior < 1e-10 and offd < 1e-10 and ones + zeros == L.dim and ones == pred and abs(wn - 1) < 1e-10
              and Uw < 1e-10 and Dw < 1e-10 and left_int < 1e-10 and abs(left_norm - 1) < 1e-10 and adj_ok < 1e-10 and gen <= 1 + 1e-10
              and rnd <= 1 + 1e-10)
        if not ok:
            hits.append(f"R = {R}: an identity or bound fails (unitarity {unit:.1e}, interior {interior:.1e}, ones {ones} vs {pred}, witness "
                        f"{Uw:.1e}, left {left_int:.1e}/{left_norm:.6f}, energy {gen:.6f}/{rnd:.6f})")
        worst_unit = max(worst_unit, unit)
    # paths at R = 1: two and three distinct links with a shared colour register and a reference qubit
    L = LinkSpace(1)
    Uin, Ul = L.transporter()
    Uadj_in, Uadj_l = L.transporter(adjoint=True)
    n = L.dim // 3
    shell = L.shell_mask()

    def full_op(Ui, Ulk):
        """(P + leak) basis: the full output space of one link = Ran P_1 plus the leaked blocks; U restricted to inputs in Ran P_1."""
        return np.vstack([Ui, Ulk])

    path_dev, bound_viol = 0.0, 0.0
    for nlinks, orient in ((2, (False, False)), (2, (False, True)), (3, (False, True, False))):
        # state space: links (each n link-states x its own index) x colour 3 x reference 2; the colour is shared: represent each link
        # operator as acting on (link_e, colour)
        dims = [n] * nlinks
        for trial in range(8 if nlinks == 3 else 16):
            shape = dims + [3, 2]
            psi = rng.normal(size=shape) + 1j * rng.normal(size=shape)
            psi /= np.linalg.norm(psi)
            # exact W psi and compressed W_R psi, one link at a time (U_e acts on link e and the colour)
            exact = psi.copy()
            comp = psi.copy()
            leak_dims = [n] * nlinks
            ext = [n + L.ldim // 3 for _ in range(nlinks)]
            # embed exact states in the extended link spaces (Ran P + leaked blocks); input to U_e is always inside Ran P for distinct links
            ex_state = np.zeros(ext + [3, 2], dtype=complex)
            ex_state[tuple(slice(0, n) for _ in range(nlinks))] = psi
            sq_leak_bound = 0.0
            for e in range(nlinks):
                A = (Uadj_in if orient[e] else Uin)
                Al = (Uadj_l if orient[e] else Ul)
                Mfull = np.vstack([A, Al])                     # ((n + nl) * 3) x (n * 3): rows (block, colour) flattened as in L
                # reshape the link-e operator to act on (link_e index, colour): L's flattening is (block..., a, b, j): colour is the last
                # index within each block, so the flattened index = link_state * 3 + colour with link_state running over (block, a, b)
                Mt = Mfull.reshape(-1, 3, n, 3)                # (out link, out colour, in link, in colour)
                Mt_in = A.reshape(n, 3, n, 3)
                # exact: only the Ran P part of link e is an admissible input (distinct links: link e untouched before step e)
                sl = [slice(None)] * (nlinks + 2)
                sl[e] = slice(0, n)
                inp = ex_state[tuple(sl)]
                out = np.einsum("OcIj,...", Mt, np.zeros(1)) if False else None
                inp_m = np.moveaxis(inp, [e, nlinks], [0, 1])
                out_m = np.einsum("OcIj,Ij...->Oc...", Mt, inp_m)
                new = np.zeros_like(ex_state)
                nsl = [slice(None)] * (nlinks + 2)
                new = np.moveaxis(new, [e, nlinks], [0, 1])
                new[:, :] = 0
                new = out_m
                ex_state = np.moveaxis(new, [0, 1], [e, nlinks])
                comp_m = np.moveaxis(comp, [e, nlinks], [0, 1])
                comp = np.moveaxis(np.einsum("OcIj,Ij...->Oc...", Mt_in, comp_m), [0, 1], [e, nlinks])
                # <psi, T_(R,e) psi>: weight of psi on the shell of link e
                mask = shell.reshape(n, 3)[:, 0]
                sq_leak_bound += np.sum(np.abs(np.moveaxis(psi, e, 0)[mask]) ** 2)
            proj = ex_state[tuple(slice(0, n) for _ in range(nlinks))]
            path_dev = max(path_dev, np.abs(proj - comp).max())
            err = np.linalg.norm(ex_state) ** 2 - np.linalg.norm(proj) ** 2           # ||W psi - W_R psi||^2 = ||(I - P) W psi||^2
            bound_viol = max(bound_viol, err - sq_leak_bound)
            if abs(np.linalg.norm(ex_state) - 1) > 1e-10:
                hits.append("the exact path does not preserve the norm")
    print(f"[paths R=1] two and three distinct links (orientations incl. adjoints), 40 random states entangled across links, colour and a "
          f"reference qubit: |W_R psi - P W psi| at most {path_dev:.1e} (identity (3)); ||W psi - W_R psi||^2 - sum_e <psi, T_e psi> at most "
          f"{bound_viol:.1e} (bound (4) needs <= 0)")
    if path_dev > 1e-10 or bound_viol > 1e-10:
        hits.append(f"paths: identity (3) off by {path_dev:.1e} or bound (4) exceeded by {bound_viol:.1e}")
    # g_(R-1) against brute force
    gbad = [R for R in range(1, 61) if min(c_lab(p, R - p) for p in range(R + 1)) != R * R - (R * R) // 4 + 3 * R]
    print(f"[g] min over p + q = R of p^2 + pq + q^2 + 3p + 3q equals R^2 - floor(R^2/4) + 3R for R = 1..60: {not gbad}")
    if gbad:
        hits.append(f"g_(R-1) differs at R = {gbad[:5]}")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (f) NORMALIZATION - the compressed transporter P_R U P_R built by brute force in an explicit Peter-Weyl basis "
          f"at R = 1, 2, 3 (Ran P_R of dimension 57, 465, 2415): U_R*U_R + D_R = I, D_R supported on the top shell with norm 1 and the witness "
          f"psi_R, the left defect on the same shell, the energy bound (2) sharp (maximum ratio 1), g_(R-1) exact to R = 60; the path identity "
          f"W_R = PWP and bound (4) on two- and three-link paths with adjoints and entangled inputs; {len(hits)} failures; attack "
          f"{'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
