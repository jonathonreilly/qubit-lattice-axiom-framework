#!/usr/bin/env python3
"""J:derive:deferred-20260924-assembly:a1  --  arrow ONE_VERTEX_INVARIANTS -> T_GRAVITY.

Reads (read only) the landed assembly-graph runner on origin/main through git,
rebuilds the graph, and then checks, with exact arithmetic where a finite fact is
claimed:

 A. what the Boolean graph does and does not say about the arrow (exact);
 B. the one-vertex lemma and the orbit count of one-vertex invariants (exact);
 C. in the SUPPLIED Gaussian divergence-free comparator (not the ice measure):
    quadratic neutral local statistics induce a like-attractive interaction
    (exact covariance, exact Wick sign, determinant cross-check), while a
    linear 1/r channel is like-repulsive; decay exponent of the quadratic
    channel (numerical);
 D. the other parent of the target, GRAVITY_BOUNDARIES: same constraint complex,
    two Hamiltonians, two different static source kernels (exact, recovered).

Environment: python3 with numpy, sympy, mpmath.  Memory about 0.35 GB for the FFT part.
"""
import os, sys, subprocess, hashlib, itertools, time
from fractions import Fraction
import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
MAIN_WT = os.environ.get(
    "MAIN_WT",
    "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/main_wt",
)
MAIN_SHA = "3e1a2dd2531590dabf85bee8db56175ba9b96e90"      # origin/main when this attempt ran
LANDING_SHA = "1cb2a082bfa4cebc01c0f61b4e366a6daa48a82d"    # landing commit named by the manifest
FROZEN_8648 = "fe1e7a925c5b66b669b69afe57581cac0e60b404"
RUNNER = "scripts/candidate_assembly_source_linked_graph_minimal_decision_sets_2026_09_22.py"
NOTE_G = "docs/CANDIDATE_ASSEMBLY_SOURCE_LINKED_GRAPH_ELEVEN_TARGETS_MINIMAL_DECISION_SETS_BOUNDED_THEOREM_NOTE_2026-09-22.md"
NOTE_OV = "docs/UNIFORM_ICE_CARRIES_THE_LATTICE_GREEN_FUNCTION_IN_ITS_CHARGED_SECTOR_WHILE_NEUTRAL_SCALAR_RECORDS_ARE_SHORT_RANGED_BOUNDED_THEOREM_NOTE_2026-09-23.md"
NOTE_GB = "docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md"

RES = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail else ""))
    return ok


def git_show(rev, path):
    r = subprocess.run(["git", "-C", MAIN_WT, "show", f"{rev}:{path}"], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout


def sha(b):
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------- A. graph
print("== A. the supplied Boolean graph (read from origin/main through git) ==")
raw = git_show(MAIN_SHA, RUNNER)
check("A0 runner bytes readable at pinned origin/main", raw is not None)
if raw is None:
    print("TOTAL: PASS=0 FAIL=1")
    print("SUMMARY: could not read the landed runner; nothing demonstrated")
    sys.exit(1)
src = raw.decode().split("\n")
g = {}
exec("\n".join(src[14:26]), g)          # data lines only: D, L, OP, NODES, CANDIDATES, WITHDRAWN, EDGES, OPEN_EDGES, TARGET_BRIEF, PARENTS
NODES, EDGES, CAND = g["NODES"], g["EDGES"], g["CANDIDATES"]
PAR = {}
for u, v in EDGES:
    PAR.setdefault(v, []).append(u)
kinds = {}
for n, (k, p) in NODES.items():
    kinds.setdefault(k, []).append(n)
check("A1 117 nodes, 40 menu entries, 75 landed + 3 open reference nodes, 11 targets",
      len(NODES) == 117 and sum(len(v) for v in CAND.values()) == 40 and len(kinds["landed"]) == 75
      and len(kinds["open"]) == 3 and len(kinds["target"]) == 11 and len(kinds["decision"]) == 12,
      f"edges={len(EDGES)}")
DEC = sorted(kinds["decision"])
TOPO = []
seen = set()


def visit(n):
    if n in seen:
        return
    seen.add(n)
    for p in PAR.get(n, []):
        visit(p)
    TOPO.append(n)


for n in NODES:
    visit(n)


def truth(assign, par=PAR, false_nodes=()):
    t = {}
    for n in TOPO:
        k = NODES[n][0]
        if n in false_nodes:
            t[n] = False
        elif k == "source":
            t[n] = True
        elif k == "decision":
            t[n] = n in assign
        elif k == "choice":
            t[n] = any(t[p] for p in par.get(n, []))
        else:
            t[n] = all(t[p] for p in par.get(n, []))
    return t


def families(target, par=PAR, false_nodes=()):
    """minimal true decision subsets by brute force over all 4096 subsets (independent of the landed recursion)"""
    good = []
    for m in range(1 << 12):
        A = {DEC[i] for i in range(12) if m >> i & 1}
        if truth(A, par, false_nodes)[target]:
            good.append(frozenset(A))
    gs = set(good)
    return {s for s in gs if not any(t < s for t in gs)}


GRAV = families("T_GRAVITY")
exp = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_ALPHABET", "DEC_READING"},
    {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW", "DEC_ROLES"})}
check("A2 T_GRAVITY minimal decision sets by 4096-assignment brute force = the four landed families", GRAV == exp)
inter = frozenset.intersection(*GRAV)
check("A3 no single decision is common to all four families (nothing is individually necessary for T_GRAVITY)",
      len(inter) == 0)
check("A4 every family has exactly one of {DEC_ORDER_LAW, DEC_READING} (formation reading xor static reading)",
      all(("DEC_ORDER_LAW" in s) != ("DEC_READING" in s) for s in GRAV))

# which parents of T_GRAVITY can change its families if the edge is deleted
gp = PAR["T_GRAVITY"]
changed = {}
for p in gp:
    par2 = {k: [q for q in v if not (k == "T_GRAVITY" and q == p)] for k, v in PAR.items()}
    changed[p] = (families("T_GRAVITY", par2) != GRAV)
check("A5 deleting the edge ONE_VERTEX_INVARIANTS->T_GRAVITY changes no minimal family (Boolean-inert); same for GRAVITY_BOUNDARIES and HOLE_READS_CLOCK; T_RECORD_DYNAMICS and T_GAUGE edges matter",
      (not changed["ONE_VERTEX_INVARIANTS"]) and (not changed["GRAVITY_BOUNDARIES"]) and (not changed["HOLE_READS_CLOCK"])
      and changed["T_RECORD_DYNAMICS"] and changed["T_GAUGE"], str(changed))
AXREF = [(u, v) for u, v in EDGES if u == "AX" and NODES[v][0] in ("landed", "open")]
check("A6 the graph makes each of the 78 reference nodes true by a direct arrow AX->node", len(AXREF) == 78)
par3 = {k: [q for q in v if not (k == "ONE_VERTEX_INVARIANTS" and q == "AX")] for k, v in PAR.items()}
fam3 = families("T_GRAVITY", par3)
check("A7 withdrawing the arrow AX->ONE_VERTEX_INVARIANTS leaves the node parentless, and an empty AND is true: T_GRAVITY's families do not change (the arrow from AX is itself Boolean-vacuous)",
      fam3 == GRAV, f"families={len(fam3)}")
famF = families("T_GRAVITY", PAR, false_nodes=("ONE_VERTEX_INVARIANTS",))
check("A7b the node matters only if its truth is overridden: with ONE_VERTEX_INVARIANTS set false T_GRAVITY has no family. The graph holds no content that could make it false; its truth is a convention of the encoding, not a derived value",
      famF == set(), f"families={len(famF)}")
anc = set()
st = ["T_GRAVITY"]
while st:
    n = st.pop()
    for p in PAR.get(n, []):
        if p not in anc:
            anc.add(p)
            st.append(p)
ref_anc = [n for n in anc if NODES[n][0] in ("landed", "open")]
check("A8 count of reference nodes that T_GRAVITY depends on (ancestors)", len(ref_anc) > 0, f"{len(ref_anc)} of 78")

# frozen original: the stronger sentence that was deferred
orig = git_show(FROZEN_8648, NOTE_G)
check("A9 frozen head of PR 8648 fetched; original note readable", orig is not None,
      f"sha256={sha(orig)[:16] if orig else None}")
needle = "one-vertex scalar invariants for one neutral statistic feed gravity (PR 8918)"
check("A10 the deferred sentence 'one-vertex ... feed gravity' is in the frozen original and absent from the landed note",
      orig is not None and needle in orig.decode() and needle not in (git_show(MAIN_SHA, NOTE_G) or b"").decode())

# the cited source's own scope sentences (verbatim, with line numbers)
ov = (git_show(MAIN_SHA, NOTE_OV) or b"").decode().split("\n")
gb = (git_show(MAIN_SHA, NOTE_GB) or b"").decode().split("\n")


def line_of(lines, frag):
    for i, l in enumerate(lines, 1):
        if frag in l:
            return i
    return None


q1 = line_of(ov, "They are not derived from the repository axioms")
q2 = line_of(ov, "No gravity, Born-weight or statistical-bridge conclusion is asserted")
q3 = line_of(ov, "an unresolved tail is not proved zero or exponentially decaying")
q4 = line_of(gb, "not supply these tensor pairs")
check("A11 cited source ONE_VERTEX says its models are not derived from the axioms and asserts no gravity conclusion", q1 is not None and q2 is not None,
      f"{NOTE_OV}:{q1},{q2}")
check("A12 cited source ONE_VERTEX leaves the tail of the neutral statistic unresolved (so 'short-ranged' is not a theorem)", q3 is not None, f"{NOTE_OV}:{q3}")
check("A13 cited source GRAVITY_BOUNDARIES says the axioms do not supply its tensor pairs, constraints, Hamiltonian, source or phase", q4 is not None, f"{NOTE_GB}:{q4}")

# ------------------------------------------------ B. one-vertex lemma and orbits
print("== B. one-vertex invariants (exact) ==")
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
didx = {d: i for i, d in enumerate(dirs)}
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = sp.zeros(3, 3)
        for r in range(3):
            M[r, perm[r]] = sg[r]
        if M.det() == 1:
            rots.append(M)
check("B1 24 proper cubic rotations", len(rots) == 24)
perms6 = []
for M in rots:
    p = [didx[tuple(int(x) for x in (M * sp.Matrix(d)))] for d in dirs]
    perms6.append(p)
check("B2 rotations act transitively on the six outward directions", len({p[0] for p in perms6}) == 6)
# invariant subspace of the 6-dim permutation representation: dimension = number of orbits = 1 (averaging)
Pav = sp.zeros(6, 6)
for p in perms6:
    for i in range(6):
        Pav[p[i], i] += sp.Rational(1, 24)
check("B3 averaging projector of the permutation representation = J/6, invariant linear statistics = span(sum of outward arrows)",
      Pav == sp.ones(6, 6) / 6 and Pav.rank() == 1)
states = [s for s in itertools.product((1, -1), repeat=6) if sum(s) == 0]
check("B4 ice (3-in 3-out) vertex states: 20", len(states) == 20)
# the sum of outward arrows vanishes on all of them (the invariant linear statistic is constant 0)
check("B5 the only invariant linear statistic vanishes on every ice vertex state", all(sum(s) == 0 for s in states))


def orbits(group_perms):
    seen_, orbs = set(), []
    for s in states:
        if s in seen_:
            continue
        o = set()
        for p in group_perms:
            t = [0] * 6
            for i in range(6):
                t[p[i]] = s[i]
            o.add(tuple(t))
        seen_ |= o
        orbs.append(o)
    return orbs


O24 = orbits(perms6)
# full octahedral group
full = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = sp.zeros(3, 3)
        for r in range(3):
            M[r, perm[r]] = sg[r]
        full.append([didx[tuple(int(x) for x in (M * sp.Matrix(d)))] for d in dirs])
O48 = orbits(full)
print("   orbit sizes under 24 rotations:", sorted(len(o) for o in O24), "; under 48:", sorted(len(o) for o in O48))
# Burnside cross-check
fixed = 0
for p in perms6:
    for s in states:
        t = [0] * 6
        for i in range(6):
            t[p[i]] = s[i]
        fixed += (tuple(t) == s)
check("B6 Burnside: number of orbits of the 24 rotations on the 20 ice vertex states equals the orbit enumeration",
      Fraction(fixed, 24) == len(O24), f"orbits={len(O24)}")
check("B7 more than one orbit: non-constant rotation-invariant one-vertex statistics exist (the lemma is silent on them)",
      len(O24) > 1, f"{len(O24)-1} independent non-constant invariants under rotations, {len(O48)-1} under the full octahedral group")
# alignment statistic f = sum_i E_i(r) E_i(r-e_i) = - sum_i sigma_{+i} sigma_{-i}
fvals = set()
for s in states:
    fvals.add(-sum(s[2 * i] * s[2 * i + 1] for i in range(3)))
forb = {frozenset(o) for o in O24}
lev3 = frozenset(s_ for s_ in states if -sum(s_[2 * i] * s_[2 * i + 1] for i in range(3)) == 3)
check("B8 the landed alignment statistic f (1 or 3 aligned axes, values {-1,3}) has exactly the two rotation orbits (sizes 8 and 12) as its level sets: it is the one non-constant invariant",
      fvals == {-1, 3} and lev3 in forb and sorted(len(o) for o in O24) == [8, 12], str(sorted(fvals)))

# ------------------------------------------------ C. Gaussian comparator on the 4^3 torus, exact
print("== C. supplied Gaussian divergence-free link field, quadratic vs linear coupling ==")
L = 4
N = L ** 3


def sid(x, y, z):
    return ((x % L) * L + (y % L)) * L + (z % L)


# exact mean-zero lattice Green function G0(d), scaled: G0(d) = (1/N) sum_{k!=0} e^{ik.d} / lam(k), lam = sum 2-2cos k_i
# on L=4 the phases are powers of i and lam in {0,2,4,...}: exact in Q.
def cosint(n, L_):
    """cos(2 pi n/L) for L=4 as an integer"""
    return [1, 0, -1, 0][n % 4]


def G0_exact(d):
    tot = Fraction(0)
    for kx in range(L):
        for ky in range(L):
            for kz in range(L):
                if (kx, ky, kz) == (0, 0, 0):
                    continue
                lam = sum(2 - 2 * cosint(k, L) for k in (kx, ky, kz))
                ph = cosint(kx * d[0] + ky * d[1] + kz * d[2], L)          # real part (the sum is real by k -> -k)
                tot += Fraction(ph, lam)
    return tot / N


Gtab = {}
for dx in range(L):
    for dy in range(L):
        for dz in range(L):
            Gtab[(dx, dy, dz)] = G0_exact((dx, dy, dz))


def Gd(d):
    return Gtab[(d[0] % L, d[1] % L, d[2] % L)]


check("C1 mean-zero lattice Green function: sum over the torus = 0 and (-Laplacian G0)(0) = 1 - 1/N exactly",
      sum(Gtab.values()) == 0 and 6 * Gd((0, 0, 0)) - sum(Gd(e) for e in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]) == 1 - Fraction(1, N))

nl = 3 * N
LID = lambda site, i: 3 * site + i


def link(x, y, z, i):
    return LID(sid(x, y, z), i)


# P0 = I - D^T G D - harmonic
def link_pos(a):
    s, i = divmod(a, 3)
    x, r = divmod(s, L * L)
    y, z = divmod(r, L)
    return (x, y, z), i


E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
Sig = np.empty((nl, nl), dtype=object)
for a in range(nl):
    (ux, uy, uz), i = link_pos(a)
    for b in range(nl):
        (vx, vy, vz), j = link_pos(b)
        d0 = (ux - vx, uy - vy, uz - vz)
        val = Gd(d0) - Gd((d0[0] - E[j][0], d0[1] - E[j][1], d0[2] - E[j][2])) \
            - Gd((d0[0] + E[i][0], d0[1] + E[i][1], d0[2] + E[i][2])) \
            + Gd((d0[0] + E[i][0] - E[j][0], d0[1] + E[i][1] - E[j][1], d0[2] + E[i][2] - E[j][2]))
        Sig[a, b] = (Fraction(1) if a == b else Fraction(0)) - val - (Fraction(1, N) if i == j else Fraction(0))
# scale to integers for fast exact projector test
import math
den = 1
for v in Sig.flat:
    den = den * v.denominator // math.gcd(den, v.denominator)
SI = np.empty((nl, nl), dtype=object)
for a in range(nl):
    for b in range(nl):
        SI[a, b] = int(Sig[a, b] * den)
SS = SI.dot(SI)
check("C2 covariance matrix of the zero-flux divergence-free Gaussian (K=1) is an exact orthogonal projector on the 192 links of the 4^3 torus",
      (SS == den * SI).all() and (SI == SI.T).all(), f"common denominator {den}")
# divergence free: D Sigma = 0
Dm = np.zeros((N, nl), dtype=object)
for x in range(L):
    for y in range(L):
        for z in range(L):
            s = sid(x, y, z)
            for i in range(3):
                Dm[s, link(x, y, z, i)] += 1
                Dm[s, link(x - E[i][0], y - E[i][1], z - E[i][2], i)] -= 1
check("C3 Sigma annihilates the lattice divergence and the three uniform-flux directions (zero-flux, divergence-free sector)",
      (Dm.dot(SI) == 0).all() and all(sum(SI[a, b] for b in range(nl) if link_pos(b)[1] == i) == 0 for a in range(nl) for i in range(3)))
rank_ok = sum(Sig[a, a] for a in range(nl)) == nl - (N - 1) - 3
check("C4 trace(Sigma) = 192 - 63 - 3 = 126: the degrees of freedom of the divergence-free zero-flux field", rank_ok, f"trace={sum(Sig[a,a] for a in range(nl))}")


def vlinks(x, y, z):
    out = [link(x, y, z, i) for i in range(3)]
    inc = [link(x - E[i][0], y - E[i][1], z - E[i][2], i) for i in range(3)]
    return out + inc


Lx = vlinks(0, 0, 0)
Cov = {}
for y in range(L):
    for z in range(L):
        for x in range(L):
            Ly = vlinks(x, y, z)
            Cov[(x, y, z)] = 2 * sum(Sig[a, b] ** 2 for a in Lx for b in Ly)
check("C5 exact covariance C(r) = 2 sum Sigma_ab^2 of the vertex statistic s_v = sum over its six incident links of B^2: >= 0 at every separation and > 0 at every separation on 4^3",
      all(c >= 0 for c in Cov.values()) and all(c > 0 for c in Cov.values()), f"min={min(Cov.values())}, C(1,0,0)={Cov[(1,0,0)]}, C(2,0,0)={Cov[(2,0,0)]}")
# determinant (generating function) cross-check of F_int = -lam_x lam_y C + O(lam^3), using mpmath, 50 digits
mp.mp.dps = 50
y0 = (2, 0, 0)
Ly = vlinks(*y0)
S = sorted(set(Lx) | set(Ly))
idx = {a: n for n, a in enumerate(S)}
SigS = mp.matrix(len(S), len(S))
for a in S:
    for b in S:
        v = Sig[a, b]
        SigS[idx[a], idx[b]] = mp.mpf(v.numerator) / mp.mpf(v.denominator)


def Qdiag(links_, lam_):
    q = mp.zeros(len(S), len(S))
    for a in links_:
        q[idx[a], idx[a]] += lam_
    return q


def lndet(Qm):
    return mp.log(mp.det(mp.eye(len(S)) + 2 * Qm * SigS))


def Fint(lx, ly):
    Qx, Qy = Qdiag(Lx, lx), Qdiag(Ly, ly)
    return mp.mpf(1) / 2 * (lndet(Qx + Qy) - lndet(Qx) - lndet(Qy))


Cexact = mp.mpf(Cov[y0].numerator) / mp.mpf(Cov[y0].denominator)
lam = mp.mpf("1e-8")
r_same = Fint(lam, lam) / (-lam * lam * Cexact)
r_opp = Fint(lam, -lam) / (lam * lam * Cexact)
check("C6 exact Gaussian partition functions: F_int(lam,lam) = -lam^2 C(r) (1+O(lam)) -- like inclusions attract; F_int(lam,-lam) = +lam^2 C(r) -- unlike repel",
      abs(r_same - 1) < 1e-6 and abs(r_opp - 1) < 1e-6, f"ratios {mp.nstr(r_same, 12)}, {mp.nstr(r_opp, 12)}")
lam2 = mp.mpf("-1e-8")
check("C7 same sign of F_int for lam of either sign (leading order is quadratic in the coupling)",
      abs(Fint(lam2, lam2) / (-lam2 * lam2 * Cexact) - 1) < 1e-6)

# linear channel: like sources through the mean-zero Green function
def G0_L6_axis():
    # L=6: lam in exact quadratic irrationals avoided: use x-axis profile via exact eigenvalues 2-2cos(2 pi n/6) in {0,1,3,4}
    L6 = 6
    cos6 = [Fraction(1), Fraction(1, 2), Fraction(-1, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2)]
    # real part of e^{i 2pi m/6} is cos6[m % 6]
    out = []
    for r in range(0, 4):
        tot = Fraction(0)
        for kx in range(L6):
            for ky in range(L6):
                for kz in range(L6):
                    if (kx, ky, kz) == (0, 0, 0):
                        continue
                    lam_ = sum(2 - 2 * cos6[k] for k in (kx, ky, kz))
                    tot += cos6[(kx * r) % 6] / lam_
        out.append(tot / L6 ** 3)
    return out


ax4 = [Gd((r, 0, 0)) for r in range(0, 3)]
ax6 = G0_L6_axis()
check("C8 linear channel: the mean-zero Green function is strictly decreasing in separation on 4^3 and 6^3 (cross energy of two like unit sources q^2 G0(r) falls with distance: like sources repel)",
      all(ax4[i] > ax4[i + 1] for i in range(2)) and all(ax6[i] > ax6[i + 1] for i in range(3)),
      f"4^3 axis {[str(x) for x in ax4]}; 6^3 axis {[str(x) for x in ax6]}")

# ------------------------------------------------ C'. decay exponent on a large torus (numerics)
print("== C'. decay exponent of the quadratic channel (floating point, not a proof) ==")


def sigma_fft(Lb, add_back=False):
    k1 = 2 * np.pi * np.fft.fftfreq(Lb)
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    w = [1 - np.exp(-1j * kx), 1 - np.exp(-1j * ky), 1 - np.exp(-1j * kz)]
    w2 = sum(np.abs(c) ** 2 for c in w)
    w2[0, 0, 0] = 1.0
    out = {}
    for i in range(3):
        for j in range(i, 3):
            P = (1.0 if i == j else 0.0) - np.conj(w[i]) * w[j] / w2
            if i == j:
                P[0, 0, 0] = 0.0
            else:
                P[0, 0, 0] = 0.0
            Gij = np.fft.ifftn(P)       # (1/N) sum_k e^{+ik.d} P_ij(k)
            if add_back and i == j:
                Gij = Gij + (2.0 / 3.0) / Lb ** 3
            out[(i, j)] = Gij
    return out


def sig_lookup(G, Lb, i, j, d):
    # <B_i(u) B_j(v)> with d = u - v; G stores (i<=j); symmetry <B_j(v)B_i(u)> at -d
    d = tuple(int(c) % Lb for c in d)
    if i <= j:
        return G[(i, j)][d].conj() if False else G[(i, j)][d]
    dm = tuple((-c) % Lb for c in d)
    return G[(j, i)][dm]


# convention test against the exact rational Sigma on 4^3 (try both conjugation conventions)
G4 = sigma_fft(4)
ok_dir = True
ok_conj = True
for a in range(0, nl, 7):
    (ux, uy, uz), i = link_pos(a)
    for b in range(0, nl, 5):
        (vx, vy, vz), j = link_pos(b)
        ex = float(Sig[a, b])
        v1 = sig_lookup(G4, 4, i, j, (ux - vx, uy - vy, uz - vz))
        ok_dir &= abs(v1.real - ex) < 1e-12 and abs(v1.imag) < 1e-12
check("C9 FFT construction of Sigma (conventions of the large-torus run) reproduces the exact rational Sigma on 4^3 to 1e-12", ok_dir)


def cov_axis(G, Lb, dmax):
    base = [((0, 0, 0), i) for i in range(3)] + [(tuple(-c for c in E[i]), i) for i in range(3)]
    res = []
    for dd in range(1, dmax + 1):
        sh = [((dd, 0, 0), 0)]
        tot = 0.0
        for (pu, i) in base:
            for (pv, j) in base:
                u = pu
                v = (pv[0] + dd, pv[1], pv[2])
                val = sig_lookup(G, Lb, i, j, (u[0] - v[0], u[1] - v[1], u[2] - v[2])).real
                tot += val * val
        res.append(2 * tot)
    return np.array(res)


Lbig = 112
Gb = sigma_fft(Lbig, add_back=True)
Cax = cov_axis(Gb, Lbig, 20)
d_ = np.arange(1, 21)
expo = -np.log(Cax[1:] / Cax[:-1]) / np.log(d_[1:] / d_[:-1])
print("   axis covariance C(d), d=1..20:", " ".join(f"{c:.3e}" for c in Cax))
print("   local exponent -dlnC/dlnd between d and d+1 (d=1..19):", " ".join(f"{e:.2f}" for e in expo))
check("C10 on a 112^3 torus the local decay exponent of the quadratic channel decreases monotonically from d=8 to d=19, stays within 0.45 of 6, and is within 0.05 of 6 at d=19 (r^-6 asymptote from two dipolar r^-3 correlators, approached from above); it is NOT r^-1",
      all(abs(expo[d - 1] - 6.0) < 0.45 for d in range(8, 20)) and all(expo[d] < expo[d - 1] for d in range(8, 19)) and abs(expo[18] - 6.0) < 0.05,
      f"exponents d=8:{expo[7]:.3f} d=14:{expo[13]:.3f} d=19:{expo[18]:.3f}")
check("C11 the covariance is positive at every axis separation 1..20 on the large torus", bool((Cax > 0).all()))
del Gb, G4

# ------------------------------------------------ D. GRAVITY_BOUNDARIES parent: one constraint complex, two kernels
print("== D. the other parent: same constraints, two Hamiltonians, two static source kernels (recovered, exact) ==")
kx, ky, kz = sp.Integer(1), sp.Integer(2), sp.Integer(2)
kv = sp.Matrix([kx, ky, kz])
k2 = (kv.T * kv)[0]
hs = sp.symbols("h0:6")
H = sp.Matrix([[hs[0], hs[3], hs[4]], [hs[3], hs[1], hs[5]], [hs[4], hs[5], hs[2]]])
eps = sp.LeviCivita


def Rmat(h):
    R = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            s = 0
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        for d in range(3):
                            e1, e2 = eps(i, a, b), eps(j, c, d)
                            if e1 and e2:
                                s += e1 * e2 * (-kv[a] * kv[c]) * h[b, d]
            R[i, j] = s
    return R


Rh = Rmat(H)
Sh = sp.simplify(Rh.trace())
Pk = sp.eye(3) - kv * kv.T / k2
check("D1 S(h) = tr R(h) = -k^2 tr h + k^T h k (symbolic, k=(1,2,2))", sp.simplify(Sh - (-k2 * H.trace() + (kv.T * H * kv)[0])) == 0)
# rank of h -> R(h) is 3 (transverse symmetric tensors)
Jac = sp.Matrix([[sp.diff(Rh[i, j], hv) for hv in hs] for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]])
check("D2 the curvature map h -> R(h) has rank 3 = dim of symmetric transverse tensors", Jac.rank() == 3)
rho = sp.symbols("rho")
hsol = -rho * Pk / (2 * k2)
Rs = sp.simplify(Rmat(hsol))
check("D3 the source-fixing field h = -rho P/(2k^2) has S(h) = rho and R(h) = rho P/2", sp.simplify(Rs.trace() - rho) == 0 and sp.simplify(Rs - rho * Pk / 2) == sp.zeros(3, 3))
EL = sp.simplify(sp.Rational(1, 2) * sum(Rs[i, j] ** 2 for i in range(3) for j in range(3)))
EN = sp.simplify(sp.Rational(1, 2) * sum(hsol[i, j] * Rs[i, j] for i in range(3) for j in range(3)))
check("D4 static scalar-source energies in the two quadratic comparators (g=1): H_L = rho^2/4 (k-independent contact), H_N = -rho^2/(4k^2) (attractive inverse-Laplacian kernel)",
      sp.simplify(EL - rho ** 2 / 4) == 0 and sp.simplify(EN + rho ** 2 / (4 * k2)) == 0, f"E_L={EL}, E_N={EN}")
TTproj = sp.simplify(sp.Rational(1, 2) * (Rh.T * Rh).trace() - sp.Rational(1, 2) * (Rh.trace()) ** 2 / 2)
# minimality of the source-fixing configuration inside the constraint surface for H_L: |R|^2 >= (tr R)^2/2 for transverse R
check("D5 for every h: |R(h)|^2 - (tr R(h))^2/2 = |R_TT|^2 (a sum of squares), so rho^2/4 is the minimum of H_L at fixed S = rho",
      sp.simplify(sum(Rh[i, j] ** 2 for i in range(3) for j in range(3)) - Rh.trace() ** 2 / 2 - sum((Rh - Rh.trace() * Pk / 2)[i, j] ** 2 for i in range(3) for j in range(3))) == 0)
J, U = sp.symbols("J U", positive=True)
Kmat = sp.Matrix([[0, -J / sp.sqrt(2)], [-J / sp.sqrt(2), J / 2 + U * k2]])
check("D6 finite derivative penalty cannot repair the scalar block: det K = -J^2/2 < 0 for every U (unconstrained Gaussian scalar form is indefinite)", sp.simplify(Kmat.det() + J ** 2 / 2) == 0)

# -------------------------------------------------------------- summary
tot = sum(RES)
fail = len(RES) - tot
print(f"runtime {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={tot} FAIL={fail}")
print("SUMMARY: PARTIAL -- the arrow ONE_VERTEX_INVARIANTS->T_GRAVITY is Boolean-inert and the node's truth is an encoding convention (empty AND), not a derived value; in the supplied Gaussian comparator the quadratic one-vertex channel is like-attractive but decays as r^-6, the linear 1/r channel is like-repulsive, and the attractive 1/r kernel appears only with the indefinite scalar sector of the other parent; no source->curvature bridge is supplied, so the physical implication is not derived.")
sys.exit(0 if fail == 0 else 1)
