#!/usr/bin/env python3
"""Fluctuation forms on a shell with holonomy, Text 3.5. d = 2, the charged component of the adjoint, one fine level.

The target lead's test field in d = 2: two removed blocks (the closed 0-sheet), the region around them with a flat field, Z_2 or U(1), with holonomy
exp(i phi) around each removed block. The charged component of the adjoint sees phase 2 phi, so phi = pi is the centre sheet, for which the adjoint sees nothing.
A flat field on a region that is not simply connected, so this tests the two statements that have to survive such a shell. It is flat, abelian and one step,
and it says nothing about a non-flat field or about 4D.

PRE-STATED CRITERIA, written before the first run. Region: torus of Nb x Nb blocks of side L minus the two blocks. Links with both ends in kept blocks.
  Cut: the crossing links of a straight line of bonds between the two removed blocks carry the transport exp(i theta), theta := 2 phi for the charged component.
  CENTRE.  PASS-CENTRE if at phi = pi the spectra of A below agree with those at phi = 0 to 1e-9. It is the exact twist symmetry of Text 3.5.
  COER.    A := ||D_V b||^2 + tau ||Pi_0 D_V^* b||^2, on X_V := ker Q^V, restricted to the region, with Pi_0 removing the block average. lambda := its least eigenvalue.
           PASS-COER if min over phi of lambda(phi) L^2 >= 0.5 lambda(0) L^2 at L = 3, 5. FAIL-COER otherwise. That is (COER-G) with holonomy around a hole.
  JENSEN.  For coarse data v on the bonds of the coarse region, q(v) := min{ ||D_V a||^2 : Q^V a = v }. D_W the coarse covariant curl on coarse plaquettes with all four blocks kept.
           PASS-JENSEN if the least eigenvalue of q - D_W^* D_W is >= -1e-9, at every phi. FAIL-JENSEN otherwise. This is the positivity of Delta_q at a twisted flat field, with no patch.
  Numerics are dense, complex Hermitian; at most a few thousand links.

  RESULT OF THE FIRST RUN: VOID, by two errors of mine, both found on reading the output. PASS-CENTRE, FAIL-COER, FAIL-JENSEN as registered. (1) The dip at theta = pi / 2 and none at theta = pi
  was a wrong conjugate in the curl and in Q: with D g = conj(t) g(l+) - g(l-), the transport from l+ to l- is conj(t), and I used t. Real phases hid it. (2) JENSEN was false as registered,
  also at phi = 0: Lemma 7.1 is the statement of d = 4. In d = 2 the Jensen step gives |F'|^2 <= L^2 sum_q w_q F_q^2, with sum over coarse plaquettes of w_q equal to one, so the statement is q >= L^-2 D_W^* D_W.
  ADDED BEFORE THE SECOND RUN. CONTROL-FLAT: ||C D|| <= 1e-12 at every phi. CONTROL-COV: ||Q D g - D_W avg(g)|| <= 1e-12 at every phi, for random g, avg the block average over the frames of a block.
  COER as before, with these conventions. JENSEN2: PASS-JENSEN2 if the least eigenvalue of q - L^-2 D_W^* D_W is >= -1e-9 at every phi. FAIL-JENSEN2 otherwise.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import json, resource, sys
import numpy as np


def check_rss():
    gb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3
    if gb > 2.0:
        sys.exit(f"RSS {gb:.2f} GB above limit")


class Shell:
    def __init__(self, L, Nb, holes, theta):
        self.L, self.Nb, self.S, self.theta = L, Nb, L * Nb, theta
        self.holes = set(holes)
        S = self.S
        self.keep_site = np.zeros((S, S), dtype=bool)
        for x in range(S):
            for y in range(S):
                self.keep_site[x, y] = (x // L, y // L) not in self.holes
        self.links, self.index = [], {}
        for x in range(S):
            for y in range(S):
                for mu in range(2):
                    xx, yy = ((x + 1) % S, y) if mu == 0 else (x, (y + 1) % S)
                    if self.keep_site[x, y] and self.keep_site[xx, yy]:
                        self.index[(x, y, mu)] = len(self.links)
                        self.links.append((x, y, mu))
        self.nl = len(self.links)
        self.sites = [(x, y) for x in range(S) for y in range(S) if self.keep_site[x, y]]
        self.sindex = {s: i for i, s in enumerate(self.sites)}
        # the cut: a line of bonds in direction 1 at block row between the holes. holes share a block column index in x: holes (hx1, hy), (hx2, hy)
        (hx1, hy), (hx2, _) = sorted(self.holes)
        self.cut = set()
        for bx in range(hx1 + 1, hx2):
            for t in range(L):
                # crossing links, direction 1, from block (bx, hy) to block (bx, hy + 1)
                self.cut.add((bx * L + t, (hy + 1) * L - 1, 1))
        self.build()

    def phase(self, link):
        return np.exp(1j * self.theta) if link in self.cut else 1.0

    def build(self):
        L, Nb, S = self.L, self.Nb, self.S
        # covariant gradient D: sites -> links, (D g)_l = phase^* g(l+) - g(l-), l = (l-, l+); in the frame at l-
        D = np.zeros((self.nl, len(self.sites)), dtype=complex)
        for i, (x, y, mu) in enumerate(self.links):
            xx, yy = ((x + 1) % S, y) if mu == 0 else (x, (y + 1) % S)
            D[i, self.sindex[(xx, yy)]] = np.conj(self.phase((x, y, mu)))
            D[i, self.sindex[(x, y)]] = -1.0
        self.D = D
        # covariant curl on plaquettes with all four sites kept
        plaqs = []
        for x in range(S):
            for y in range(S):
                c = [(x, y), ((x + 1) % S, y), ((x + 1) % S, (y + 1) % S), (x, (y + 1) % S)]
                if all(self.keep_site[a, b] for a, b in c):
                    plaqs.append((x, y))
        self.plaqs = plaqs
        C = np.zeros((len(plaqs), self.nl), dtype=complex)
        for p, (x, y) in enumerate(plaqs):
            # all fields in the frame at (x, y), transported along the two axial sides
            l1 = (x, y, 0); l2 = ((x + 1) % S, y, 1); l3 = (x, (y + 1) % S, 0); l4 = (x, y, 1)
            t1 = np.conj(self.phase(l1)); t4 = np.conj(self.phase(l4))
            C[p, self.index[l1]] += 1.0
            C[p, self.index[l2]] += t1
            C[p, self.index[l3]] -= t4
            C[p, self.index[l4]] -= 1.0
        self.C = C
        # block bonds of the region
        self.bonds, self.Qrows = [], []
        for bx in range(Nb):
            for by in range(Nb):
                if (bx, by) in self.holes:
                    continue
                for mu in range(2):
                    nx, ny = ((bx + 1) % Nb, by) if mu == 0 else (bx, (by + 1) % Nb)
                    if (nx, ny) in self.holes:
                        continue
                    row = np.zeros(self.nl, dtype=complex)
                    x0, y0 = bx * L, by * L
                    for t in range(L):
                        # one line of the tube, transported to the frame of the left end. The only nontrivial transport is at a cut crossing link.
                        trans = 1.0 + 0j
                        for i in range(2 * L - 1):
                            w = (i + 1) / L if i < L - 1 else (1.0 if i == L - 1 else (2 * L - 1 - i) / L)
                            link = ((x0 + i) % S, y0 + t, 0) if mu == 0 else (x0 + t, (y0 + i) % S, 1)
                            row[self.index[link]] += trans * w / L
                            trans = trans * np.conj(self.phase(link))
                    self.bonds.append((bx, by, mu))
                    self.Qrows.append(row)
        self.Q = np.array(self.Qrows)
        self.bindex = {b: i for i, b in enumerate(self.bonds)}
        # Pi_0 on sites of a block: remove the block average in the frames of the region. Blocks contain no cut interior link, so frames are the same in a block.
        n = len(self.sites)
        Pi = np.eye(n, dtype=complex)
        for bx in range(Nb):
            for by in range(Nb):
                if (bx, by) in self.holes:
                    continue
                idx = [self.sindex[(bx * L + a, by * L + b)] for a in range(L) for b in range(L)]
                for i in idx:
                    for j in idx:
                        Pi[i, j] -= 1.0 / L ** 2
        self.Pi = Pi

    def coer(self, tau=1.0):
        H = self.C.conj().T @ self.C + tau * self.D @ self.Pi @ self.D.conj().T
        u, s, vh = np.linalg.svd(self.Q, full_matrices=True)
        rank = int((s > 1e-10).sum())
        X = vh.conj().T[:, rank:]
        A = X.conj().T @ H @ X
        A = 0.5 * (A + A.conj().T)
        ev = np.linalg.eigvalsh(A)
        return ev, rank, len(self.bonds)

    def coarse_curl(self):
        L, Nb = self.L, self.Nb
        rows, plist = [], []
        for bx in range(Nb):
            for by in range(Nb):
                cs = [(bx, by), ((bx + 1) % Nb, by), ((bx + 1) % Nb, (by + 1) % Nb), (bx, (by + 1) % Nb)]
                if any(c in self.holes for c in cs):
                    continue
                row = np.zeros(len(self.bonds), dtype=complex)
                b1 = (bx, by, 0); b2 = ((bx + 1) % Nb, by, 1); b3 = (bx, (by + 1) % Nb, 0); b4 = (bx, by, 1)
                t1 = self.coarse_phase(b1); t4 = self.coarse_phase(b4)
                row[self.bindex[b1]] += 1.0
                row[self.bindex[b2]] += t1
                row[self.bindex[b3]] -= t4
                row[self.bindex[b4]] -= 1.0
                rows.append(row)
        return np.array(rows)

    def coarse_phase(self, b):
        # the coarse link of a bond with cut crossing links carries the phase
        (bx, by, mu) = b
        (hx1, hy), (hx2, _) = sorted(self.holes)
        if mu == 1 and by == hy and hx1 < bx < hx2:
            return np.exp(-1j * self.theta)
        return 1.0

    def controls(self, seed=7):
        rng = np.random.default_rng(seed)
        flat = np.abs(self.C @ self.D).max() if self.C.size else 0.0
        n = len(self.sites)
        g = rng.normal(size=n) + 1j * rng.normal(size=n)
        L, Nb = self.L, self.Nb
        avg = {}
        for bx in range(Nb):
            for by in range(Nb):
                if (bx, by) in self.holes:
                    continue
                idx = [self.sindex[(bx * L + a, by * L + b)] for a in range(L) for b in range(L)]
                avg[(bx, by)] = g[idx].mean()
        coarse = np.zeros(len(self.bonds), dtype=complex)
        for i, (bx, by, mu) in enumerate(self.bonds):
            nx, ny = ((bx + 1) % Nb, by) if mu == 0 else (bx, (by + 1) % Nb)
            coarse[i] = self.coarse_phase((bx, by, mu)) * avg[(nx, ny)] - avg[(bx, by)]
        cov = np.abs(self.Q @ (self.D @ g) - coarse).max()
        return float(flat), float(cov)

    def jensen(self):
        # q(v) = min ||C a||^2 subject to Q a = v
        Q = self.Q
        u, s, vh = np.linalg.svd(Q, full_matrices=True)
        rank = int((s > 1e-10).sum())
        V = vh.conj().T
        X = V[:, rank:]
        Qp = V[:, :rank] @ np.diag(1.0 / s[:rank]) @ u[:, :rank].conj().T  # right inverse on the range of Q
        CX = self.C @ X
        CQp = self.C @ Qp
        # residual of C a_p against the range of C X
        uu, ss, _ = np.linalg.svd(CX, full_matrices=False)
        kk = int((ss > 1e-10).sum())
        B = uu[:, :kk]
        R = CQp - B @ (B.conj().T @ CQp)
        qform = R.conj().T @ R
        Dw = self.coarse_curl()
        diff = qform - Dw.conj().T @ Dw / self.L ** 2
        diff = 0.5 * (diff + diff.conj().T)
        return np.linalg.eigvalsh(diff), rank, len(self.bonds)


def main():
    print("blas threads", os.environ.get("VECLIB_MAXIMUM_THREADS"), flush=True)
    out = {"runs": []}
    verdicts = {}
    phis = [0.0, 0.25, 0.5, 0.75, 1.0]  # in units of pi
    for L, Nb in ((3, 6), (5, 6)):
        holes = [(1, 2), (4, 2)]
        lam = {}
        spec = {}
        for ph in phis:
            theta = 2 * np.pi * ph
            sh = Shell(L, Nb, holes, theta)
            ev, rank, nb = sh.coer()
            lam[ph] = float(ev[0])
            spec[ph] = ev
            jev, jr, jn = sh.jensen()
            flat, cov = sh.controls()
            verdicts.setdefault("flat", []).append(flat)
            verdicts.setdefault("cov", []).append(cov)
            print(f"L={L} Nb={Nb} links={sh.nl} bonds={nb} rank Q={rank} phi={ph:.2f} pi: lambda L^2 = {ev[0] * L ** 2:.4f}, "
                  f"second {ev[1] * L ** 2:.4f}; Jensen least eigenvalue {jev[0]:.3e}; controls flat {flat:.1e} cov {cov:.1e}", flush=True)
            out["runs"].append({"L": L, "phi": ph, "lambda_L2": float(ev[0] * L ** 2), "jensen_min": float(jev[0])})
            verdicts.setdefault("jensen", []).append(float(jev[0]))
            check_rss()
        cen = float(np.max(np.abs(spec[1.0] - spec[0.0])))
        low = min(lam.values()) / lam[0.0]
        print(f"L={L}: CENTRE max spectral difference {cen:.2e}, COER ratio min/lambda(0) = {low:.3f}", flush=True)
        verdicts.setdefault("centre", []).append(cen)
        verdicts.setdefault("coer", []).append(low)
    v_centre = "PASS-CENTRE" if max(verdicts["centre"]) <= 1e-9 else "FAIL-CENTRE"
    v_coer = "PASS-COER" if min(verdicts["coer"]) >= 0.5 else "FAIL-COER"
    v_jensen = "PASS-JENSEN2" if min(verdicts["jensen"]) >= -1e-9 else "FAIL-JENSEN2"
    v_ctrl = "CONTROLS-OK" if max(verdicts["flat"]) <= 1e-12 and max(verdicts["cov"]) <= 1e-12 else "CONTROLS-FAIL"
    print(v_ctrl, v_centre, v_coer, v_jensen, flush=True)
    out.update(v_ctrl=v_ctrl, v_centre=v_centre, v_coer=v_coer, v_jensen=v_jensen)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hard-core--independent_shell_form_results.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", path, "rss GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3, flush=True)


if __name__ == "__main__":
    main()
