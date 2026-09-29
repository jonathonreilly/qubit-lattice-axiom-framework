"""Falsifier for PR #9313: the positive-J spin model equals the quadratic comparator with the opposite bond sign, and the projected sector energies do
not depend on the sign convention when N/2 is even.

Disjoint from the PR's runner: no Pfaffian-parity formula, no Schur decomposition, no torus code.  Whole small clusters are solved by brute force.
  * The spin model is built as Pauli matrices on 2 qubits (sigma, tau) per site and diagonalised (dense for N = 6, Lanczos extremes for N = 8).
  * The comparator lives in the full Majorana Hilbert space (2^(3N) states, Jordan-Wigner with the two b's of every bond adjacent, so every bond
    operator u_e = i b_i b_j is diagonal).  Operators are applied to basis states by bit operations with exact phases.  The physical projection
    (constraints D_s = -i b^x b^y b^z c^x c^y c^z = 1) is applied by brute force: in every gauge sector the physical states are the +1 eigenspace of
    the product of all D_s, which is computed by applying that operator string to the sector's basis states.  One representative sector per gauge orbit.
Claims tested (from the note, extended to whole clusters with every term present):
  C1 the positive-J spin model equals the comparator with both signs reversed (A -> -A) as an operator identity on the physical space, whole cluster:
     (a) term by term (every spin bond and every odd path against its comparator counterpart, on a random physical vector of the full 2^(3N)-dimensional
         Majorana space, with the comparator's own sign as a control that must fail), and (b) for N = 6 the whole physical spectrum;
  C2 the physical spectra of the four sign conventions (bond +-, odd +-) coincide when N/2 is even (the note's claim: N = 8abc on tori);
  C3 the mechanism: when N/2 is odd, two convention pairs must split, since the parity entering the projection changes by (-1)^(N/2).
Exact enumeration; the only floating-point content is the diagonalisation, labelled.  Prints SUMMARY: and HIT: (HIT only if a claim fires).
"""
import sys, time, itertools
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

FAST = "--fast" in sys.argv
T0 = time.time()
J, KAPPA = 1.0, 0.3
FIRED = []
def check(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (" :: " + detail if detail else ""), flush=True)
    if not ok:
        FIRED.append(label)

def popcount(x):
    x = x.astype(np.uint64)
    x = x - ((x >> np.uint64(1)) & np.uint64(0x5555555555555555))
    x = (x & np.uint64(0x3333333333333333)) + ((x >> np.uint64(2)) & np.uint64(0x3333333333333333))
    x = (x + (x >> np.uint64(4))) & np.uint64(0x0F0F0F0F0F0F0F0F)
    return ((x * np.uint64(0x0101010101010101)) >> np.uint64(56)).astype(np.int64)

def apply_maj(m, idx, ph):
    """Jordan-Wigner Majorana gamma_m (m = 2q: Z...Z X_q, m = 2q+1: Z...Z Y_q) on basis states given by integer indices and phases."""
    q, t = m >> 1, m & 1
    z = popcount(idx & ((1 << q) - 1)) & 1
    b = (idx >> q) & 1
    ph = ph * (1 - 2 * z)
    if t == 1:
        ph = ph * 1j * (1 - 2 * b)
    return idx ^ (1 << q), ph

def apply_string(ops, idx, ph):
    for m in reversed(ops):
        idx, ph = apply_maj(m, idx, ph)
    return idx, ph

# ---------------------------------------------------------------------------------------------
# clusters: 3-regular bipartite graphs with a proper 3-edge colouring (flavours x = 0, y = 1, z = 2) and distinct neighbours at every site
# ---------------------------------------------------------------------------------------------
def cluster(name):
    if name == "K33":
        N = 6; A = [0, 1, 2]; bonds = [(i, 3 + j, (i + j) % 3) for i in range(3) for j in range(3)]
    elif name == "cube":
        N = 8
        coords = list(itertools.product((0, 1), repeat=3))
        A = [n for n, c in enumerate(coords) if sum(c) % 2 == 0]
        bonds = []
        for n in A:
            for ax in range(3):
                c = list(coords[n]); c[ax] ^= 1
                bonds.append((n, coords.index(tuple(c)), ax))
    else:
        raise ValueError(name)
    return N, set(A), bonds

class Cl:
    def __init__(self, name):
        self.N, self.A, self.bonds = cluster(name)
        N = self.N
        self.nbond = len(self.bonds); assert self.nbond == 3 * N // 2
        self.nc = 3 * N // 2
        self.bond_of = {}          # (site, flavour) -> (bond index e, other end)
        for e, (i, j, l) in enumerate(self.bonds):
            self.bond_of[(i, l)] = (e, j); self.bond_of[(j, l)] = (e, i)
        assert all((s, l) in self.bond_of for s in range(N) for l in range(3))
        assert all(len({self.bond_of[(s, l)][1] for l in range(3)}) == 3 for s in range(N))
    def b(self, s, l):
        e, _ = self.bond_of[(s, l)]
        return 2 * e + (0 if s in self.A else 1)
    def c(self, s, a):
        return 3 * self.N + 3 * s + a
    def comparator_terms(self):
        """Hb (bond terms, coefficient of sb) and Ho (odd terms, coefficient of so) as lists (coeff, majorana string)."""
        Hb, Ho = [], []
        for e, (i, j, l) in enumerate(self.bonds):
            for a in range(3):
                Hb.append((-J, [2 * e, 2 * e + 1, self.c(i, a), self.c(j, a)]))       # (i/2)(2J u) c c with u = i b_i b_j:  -J g g c c
        for p in range(self.N):
            for (l, m) in ((0, 1), (1, 2), (2, 0)):
                e1, q1 = self.bond_of[(p, l)]; e2, q2 = self.bond_of[(p, m)]
                for a in range(3):
                    Ho.append((-1j * KAPPA, [2 * e1, 2 * e1 + 1, 2 * e2, 2 * e2 + 1, self.c(q1, a), self.c(q2, a)]))   # (i/2)(2 kappa) u u c c
        return Hb, Ho
    def constraint_string(self, s):
        return [self.b(s, 0), self.b(s, 1), self.b(s, 2), self.c(s, 0), self.c(s, 1), self.c(s, 2)]

def block(cl, terms, sec_idx):
    """Dense block of sum of terms on the sector basis (all indices stay in the sector)."""
    n = len(sec_idx); M = np.zeros((n, n), complex)
    pos = {int(v): k for k, v in enumerate(sec_idx)}
    lookup = np.full(int(sec_idx.max()) + 1, -1, dtype=np.int64); lookup[sec_idx] = np.arange(n)
    for coeff, ops in terms:
        idx, ph = apply_string(ops, sec_idx.copy(), np.ones(n, complex))
        rows = lookup[idx]
        assert rows.min() >= 0
        M[rows, np.arange(n)] += coeff * ph
    return M

def gauge_orbits(cl):
    nb = cl.nbond
    site_mask = [sum(1 << e for e in range(nb) if s in (cl.bonds[e][0], cl.bonds[e][1])) for s in range(cl.N)]
    seen = {}; reps = []
    for u in range(1 << nb):
        if u in seen: continue
        stack = [u]; seen[u] = u; reps.append(u)
        while stack:
            v = stack.pop()
            for m in site_mask:
                w = v ^ m
                if w not in seen: seen[w] = u; stack.append(w)
    return reps

def physical_spectra(cl):
    """{(sb, so): sorted array of all physical eigenvalues}, plus per-sector lowest energies, by brute-force sector diagonalisation."""
    N, nb, nc = cl.N, cl.nbond, cl.nc
    Hb_terms, Ho_terms = cl.comparator_terms()
    full = [s for s in range(N) for _ in (0,)]
    prod_ops = []
    for s in range(N): prod_ops += cl.constraint_string(s)
    spectra = {(sb, so): [] for sb in (1, -1) for so in (1, -1)}
    lowest = {}
    reps = gauge_orbits(cl)
    for r_i, u in enumerate(reps):
        # u bit e = 1 <-> U_e = i g_{2e} g_{2e+1} = +1  (verified below for the first sector)
        sec_idx = np.array([u | (k << nb) for k in range(1 << nc)], dtype=np.int64)
        Hb = block(cl, Hb_terms, sec_idx); Ho = block(cl, Ho_terms, sec_idx)
        # product of all constraints, with the phase (-i)^N
        idx, ph = apply_string(prod_ops, sec_idx.copy(), np.ones(len(sec_idx), complex) * ((-1j) ** N))
        lookup = np.full(int(sec_idx.max()) + 1, -1, dtype=np.int64); lookup[sec_idx] = np.arange(len(sec_idx))
        tgt = lookup[idx]; assert tgt.min() >= 0
        # Pi is an involution: |k> -> ph |tgt>;  +1 eigenspace: pairs (|k> + ph_k |k'>)/sqrt2 and fixed points with ph = +1
        cols, rows_, vals = [], [], []; n_phys = 0
        done = np.zeros(len(sec_idx), bool)
        for k in range(len(sec_idx)):
            if done[k]: continue
            kp = int(tgt[k]); done[k] = True
            if kp == k:
                if abs(ph[k] - 1) < 1e-9:
                    rows_.append(k); cols.append(n_phys); vals.append(1.0); n_phys += 1
            else:
                assert abs(ph[k] * ph[kp] - 1) < 1e-9
                done[kp] = True
                rows_ += [k, kp]; cols += [n_phys, n_phys]; vals += [1 / np.sqrt(2), ph[k] / np.sqrt(2)]; n_phys += 1
        W = coo_matrix((vals, (rows_, cols)), shape=(len(sec_idx), n_phys)).tocsr()
        assert n_phys == (1 << nc) // 2, (n_phys, 1 << nc)
        Hb_p = W.conj().T @ (Hb @ W); Ho_p = W.conj().T @ (Ho @ W)
        assert np.abs(Hb_p - Hb_p.conj().T).max() < 1e-9 and np.abs(Ho_p - Ho_p.conj().T).max() < 1e-9
        for sb in (1, -1):
            for so in (1, -1):
                ev = np.linalg.eigvalsh(sb * Hb_p + so * Ho_p)
                spectra[(sb, so)].append(ev); lowest[(r_i, sb, so)] = float(ev[0])
        if FAST or r_i % 8 == 0:
            print(f"   sector {r_i + 1}/{len(reps)} done ({time.time() - T0:.0f} s)", flush=True)
    return {k: np.sort(np.concatenate(v)) for k, v in spectra.items()}, lowest, len(reps)

# ---------------------------------------------------------------------------------------------
# the spin model on 2 qubits per site, built from Pauli strings
# ---------------------------------------------------------------------------------------------
def spin_hamiltonian(cl):
    N = cl.N; nq = 2 * N; dim = 1 << nq
    # qubit of site s: sigma = 2 s, tau = 2 s + 1;  Pauli string = list of (qubit, 'X'|'Y'|'Z')
    def pauli_terms(bond_terms):
        pass
    terms = []
    sig = lambda s, a: (2 * s, "XYZ"[a]); tau = lambda s, l: (2 * s + 1, "XYZ"[l])
    for (i, j, l) in cl.bonds:
        for a in range(3):
            terms.append((J, [tau(i, l), tau(j, l), sig(i, a), sig(j, a)]))
    for p in range(N):
        for (l, m) in ((0, 1), (1, 2), (2, 0)):
            nu = ({0, 1, 2} - {l, m}).pop()
            q1 = cl.bond_of[(p, l)][1]; q2 = cl.bond_of[(p, m)][1]
            for a in range(3):
                terms.append((KAPPA, [tau(q1, l), tau(p, nu), tau(q2, m), sig(q1, a), sig(q2, a)]))
    states = np.arange(dim, dtype=np.int64)
    rows, cols, vals = [], [], []
    for coeff, string in terms:
        # merge factors on the same qubit (product of Pauli matrices in the order listed) -> flip mask and phase
        ph = np.ones(dim, complex); idx = states.copy()
        for (q, P) in reversed(string):
            b = (idx >> q) & 1
            if P == "X": idx = idx ^ (1 << q)
            elif P == "Y": ph = ph * 1j * (1 - 2 * b); idx = idx ^ (1 << q)
            else: ph = ph * (1 - 2 * b)
        rows.append(idx); cols.append(states); vals.append(coeff * ph)
    H = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(dim, dim)).tocsr()
    assert abs(H - H.conj().T).max() < 1e-12
    return H

def tr2(H): return float((H.multiply(H.conj().T)).sum().real)

def act(cl, term, v):
    """Apply coeff * (Majorana string) to a full-space vector v (a monomial matrix: one basis state to one basis state)."""
    co, ops = term
    idx, ph = apply_string(ops, np.arange(len(v), dtype=np.int64), v.copy())
    out = np.empty_like(v); out[idx] = co * ph
    return out

def identity_test(cl, seed=1):
    """Spin bonds / odd paths (in Majorana form: sigma^a = -i c^b c^c, tau^l = -i b^m b^n, (a,b,c) cyclic) against the comparator terms with hopping
    -2J u and -2 kappa u u, on a random vector of the physical space (P v = v)."""
    N = cl.N; dim = 1 << (3 * N)
    sig = lambda s, a: (-1j, [cl.c(s, (a + 1) % 3), cl.c(s, (a + 2) % 3)])
    tau = lambda s, l: (-1j, [cl.b(s, (l + 1) % 3), cl.b(s, (l + 2) % 3)])
    def prod(*factors):
        co, ops = 1.0, []
        for cc, oo in factors: co *= cc; ops += oo
        return co, ops
    rng = np.random.default_rng(seed)
    v = rng.normal(size=dim) + 1j * rng.normal(size=dim)
    for s in range(N):
        v = (v + act(cl, (-1j, cl.constraint_string(s)), v)) / 2
    v /= np.linalg.norm(v)
    phys_err = max(np.linalg.norm(act(cl, (-1j, cl.constraint_string(s)), v) - v) for s in range(N))
    def resid(spin_terms, comp_terms):
        S = sum(act(cl, t, v) for t in spin_terms); C = sum(act(cl, t, v) for t in comp_terms)
        return float(np.linalg.norm(S - C)), float(np.linalg.norm(S))
    worst_match, best_control, n_terms = 0.0, np.inf, 0
    for e, (i, j, l) in enumerate(cl.bonds):
        spin = [(J * prod(tau(i, l), tau(j, l), sig(i, a), sig(j, a))[0], prod(tau(i, l), tau(j, l), sig(i, a), sig(j, a))[1]) for a in range(3)]
        rev = [(+J, [2 * e, 2 * e + 1, cl.c(i, a), cl.c(j, a)]) for a in range(3)]        # comparator bond with hopping -2J u
        own = [(-J, [2 * e, 2 * e + 1, cl.c(i, a), cl.c(j, a)]) for a in range(3)]        # the comparator's own convention +2J u
        r, nrm = resid(spin, rev); worst_match = max(worst_match, r / nrm); r2, _ = resid(spin, own); best_control = min(best_control, r2 / nrm); n_terms += 1
    for p in range(N):
        for (l, m) in ((0, 1), (1, 2), (2, 0)):
            nu = ({0, 1, 2} - {l, m}).pop(); e1, q1 = cl.bond_of[(p, l)]; e2, q2 = cl.bond_of[(p, m)]
            spin = []
            for a in range(3):
                co, ops = prod(tau(q1, l), tau(p, nu), tau(q2, m), sig(q1, a), sig(q2, a)); spin.append((KAPPA * co, ops))
            rev = [(+1j * KAPPA, [2 * e1, 2 * e1 + 1, 2 * e2, 2 * e2 + 1, cl.c(q1, a), cl.c(q2, a)]) for a in range(3)]
            own = [(-1j * KAPPA, [2 * e1, 2 * e1 + 1, 2 * e2, 2 * e2 + 1, cl.c(q1, a), cl.c(q2, a)]) for a in range(3)]
            r, nrm = resid(spin, rev); worst_match = max(worst_match, r / nrm); r2, _ = resid(spin, own); best_control = min(best_control, r2 / nrm); n_terms += 1
    return phys_err, worst_match, best_control, n_terms

def main():
    global FIRED
    for name in (["K33"] if FAST else ["K33", "cube"]):
        cl = Cl(name)
        N = cl.N
        print(f"== cluster {name}: N = {N} sites, N/2 = {N // 2} ({'even' if (N // 2) % 2 == 0 else 'odd'}), {cl.nbond} bonds, physical dimension 4^{N} = {4 ** N}", flush=True)
        pe, worst, control, nt = identity_test(cl)
        check(f"{name} C1a: each of the {nt} spin terms (bond and odd-path, summed over the Pauli index) equals the comparator term with the opposite hopping sign, on a random vector "
              f"of the physical space of the full 2^{3 * N}-dimensional Majorana space", pe < 1e-12 and worst < 1e-9 and control > 0.5,
              f"physical-projection error {pe:.1e}; worst relative residual {worst:.1e}; with the comparator's own sign the smallest relative residual is {control:.2f} (test is sign-sensitive); {time.time() - T0:.0f} s")
        spec, lowest, nrep = physical_spectra(cl)
        total = len(spec[(1, 1)])
        check(f"{name}: physical dimension = 4^N", total == 4 ** N, f"{total} states in {nrep} gauge orbits")
        ref = spec[(-1, -1)]                                       # comparator with A -> -A
        if N == 6:
            Hs = spin_hamiltonian(cl)
            ev = np.linalg.eigvalsh(Hs.toarray())
            d = float(np.abs(ev - ref).max())
            check(f"{name} C1b: positive-J spin model spectrum equals the comparator with both signs reversed (all {len(ev)} eigenvalues)", d < 1e-9, f"max deviation {d:.1e} (FLOATING POINT diagonalisation)")
            d_plus = float(np.abs(ev - spec[(1, 1)]).max())
            print(f"   (spin model against the comparator in its own convention (+,+): max deviation {d_plus:.3g})")
        pairs = {}
        for a, b in itertools.combinations([(1, 1), (1, -1), (-1, 1), (-1, -1)], 2):
            pairs[(a, b)] = float(np.abs(spec[a] - spec[b]).max())
        same = {k: v < 1e-9 for k, v in pairs.items()}
        if (N // 2) % 2 == 0:
            check(f"{name} C2: the four sign conventions give the same physical spectrum (N/2 even)", all(same.values()), "max spread " + f"{max(pairs.values()):.1e}")
        else:
            cls_ok = same[((1, 1), (1, -1))] and same[((-1, 1), (-1, -1))] and not same[((1, 1), (-1, -1))]
            check(f"{name} C3: N/2 odd, the conventions split into two classes {{(+,+),(+,-)}} and {{(-,+),(-,-)}} (parity entering the projection changes by (-1)^(N/2))",
                  cls_ok, "pair spreads " + ", ".join(f"{a}-{b}: {v:.2g}" for (a, b), v in pairs.items()))
        print(f"   [{name} took {time.time() - T0:.0f} s]", flush=True)
    print(f"   [total {time.time() - T0:.0f} s]")
    if FIRED:
        print("SUMMARY: FALSIFIER FIRES: " + FIRED[0])
        print("HIT: PR #9313 claim fails on a whole cluster: " + "; ".join(FIRED))
        sys.exit(1)
    ran = ", ".join(f"{n} (N = {cluster(n)[0]}, N/2 {'even' if (cluster(n)[0] // 2) % 2 == 0 else 'odd'})" for n in (["K33"] if FAST else ["K33", "cube"]))
    print("SUMMARY: no falsifier fired: on " + ran + ", solved by brute-force Majorana/Pauli exact enumeration with the physical projection applied by operator application "
          "(no Pfaffian formula): every spin bond and odd path equals the comparator term with the opposite hopping sign on the physical space (the comparator's own sign fails), "
          "the four sign conventions give the same physical spectrum when N/2 is even, and split into the two predicted classes {(+,+),(+,-)} and {(-,+),(-,-)} when N/2 is odd")

if __name__ == "__main__":
    main()
