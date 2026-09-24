#!/usr/bin/env python3
"""Record dynamics: finished-record correlators against propagation kernels,
with no tick supplied anywhere, exact and finite.

Wave D (record-dynamics reframing) of the TOE derivation campaign by
underdetermination witnesses.  Exact rational arithmetic; no floating point.
Every quantity is a finished-window record statistic; no clock, rate,
Hamiltonian or evolution law enters any computation.

Declared objects
  * the 8-site path window with nearest-neighbour edges, and the 3x3
    parity-role plane of the landed support-rule note with its Gauss set;
  * pair measures on the binary alphabet {+1, -1}: the nearest-neighbour
    measure mu_NN proportional to 2^(agreeing NN pairs) and the supplied
    long-range measure mu_LR proportional to 2^(agreeing pairs over ALL
    site pairs); their chain rules condition on every formed site and are
    order-blind;
  * the Admissibility nearest-neighbour sentence checked under two
    readings: static (each single-site conditional given all other sites)
    and formation (each sequential conditional given the formed sites);
  * connected record correlators c(i, j) = E[v_i v_j] - E[v_i] E[v_j] of
    the finished-window law, exact;
  * the lattice-Laplacian comparison kernel: the Dirichlet Green function
    of the path Laplacian (grounded beyond both ends), an exact rational
    matrix, the scalar stand-in named by the design note; the transverse
    vector kernel is a named boundary, not computed here;
  * the uniform law on the plane Gauss set (the completed-record law of
    the hard-support rule for value-blind processes, per the clock-and-rate
    and formation-unit blocks) and its parity observables (-1)^(x_i).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
from fractions import Fraction as Fr
from itertools import product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


N = 8
NN_EDGES = [(i, i + 1) for i in range(N - 1)]
ALL_PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]


def make_mu(pairs):
    w = {v: Fr(2) ** sum(1 for i, j in pairs if v[i] == v[j]) for v in product((1, -1), repeat=N)}
    z = sum(w.values())
    return w, {v: x / z for v, x in w.items()}


MUW_NN, MU_NN = make_mu(NN_EDGES)
MUW_LR, MU_LR = make_mu(ALL_PAIRS)


def mean(mu, i):
    return sum(m * v[i] for v, m in mu.items())


def corr(mu, i, j):
    return sum(m * v[i] * v[j] for v, m in mu.items()) - mean(mu, i) * mean(mu, j)


def W_marg(muw, part):
    unk = [i for i in range(N) if part[i] is None]
    tot = Fr(0)
    for fill in product((1, -1), repeat=len(unk)):
        v = list(part)
        for i, b in zip(unk, fill):
            v[i] = b
        tot += muw[tuple(v)]
    return tot


def law_by_order(muw, order):
    """Chain rule of the measure along one formation order (conditions on all formed)."""
    layer = {tuple([None] * N): Fr(1)}
    for s in order:
        nxt = {}
        for part, mass in layer.items():
            base = W_marg(muw, part)
            for a in (1, -1):
                q = part[:s] + (a,) + part[s + 1:]
                p = mass * W_marg(muw, q) / base
                if p != 0:
                    nxt[q] = nxt.get(q, Fr(0)) + p
        layer = nxt
    return layer


# ---------------------------------------------------------------- section 1
print("== 1. Short-range law: exact geometric record correlator ==")
check("mu_NN: normalised, flip-invariant, reflection-covariant; every one-point mean is exactly 0",
      sum(MU_NN.values()) == 1 and all(MU_NN[v] == MU_NN[tuple(-x for x in v)] for v in MU_NN)
      and all(MU_NN[v] == MU_NN[tuple(reversed(v))] for v in MU_NN)
      and all(mean(MU_NN, i) == 0 for i in range(N)))
check("connected correlator is exactly geometric: c(i, j) = 3^-(j-i) for every pair of the path",
      all(corr(MU_NN, i, j) == Fr(1, 3 ** (j - i)) for i, j in ALL_PAIRS),
      "an order-blind covariant formation law whose record correlator decays geometrically, tick-free")
check("the chain rule of mu_NN is order-blind: two explicit formation orders reproduce mu_NN exactly",
      law_by_order(MUW_NN, tuple(range(N))) == MU_NN
      and law_by_order(MUW_NN, (5, 0, 7, 2, 6, 1, 4, 3)) == MU_NN)

# ---------------------------------------------------------------- section 2
print()
print("== 2. The lattice-Laplacian kernel decays differently, exactly ==")


def dirichlet_green(n):
    """Exact inverse of the path Laplacian with Dirichlet ends (grounded beyond both ends)."""
    A = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = Fr(2)
        if i > 0:
            A[i][i - 1] = Fr(-1)
        if i + 1 < n:
            A[i][i + 1] = Fr(-1)
    G = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        G[col], G[piv] = G[piv], G[col]
        inv = A[col][col]
        A[col] = [x / inv for x in A[col]]
        G[col] = [x / inv for x in G[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
                G[r] = [x - f * y for x, y in zip(G[r], G[col])]
    return G


GREEN = dirichlet_green(N)
check("Dirichlet Green function of the path Laplacian: exact closed form G(i, j) = (i+1)(8-j)/9 for i <= j",
      all(GREEN[i][j] == Fr((min(i, j) + 1) * (8 - max(i, j)), 9) for i in range(N) for j in range(N)))
check("the kernel decays linearly along the row: G(0, d) = (8-d)/9, with non-constant successive ratios",
      all(GREEN[0][d] == Fr(8 - d, 9) for d in range(N))
      and len({GREEN[0][d + 1] / GREEN[0][d] for d in range(1, N - 1)}) > 1
      and len({corr(MU_NN, 0, d + 1) / corr(MU_NN, 0, d) for d in range(1, N - 1)}) == 1)
ALPHA = corr(MU_NN, 0, 1) / GREEN[0][1]
check("no scaling matches the kernels: alpha fixed at distance 1 already fails at distance 2, exactly",
      ALPHA * GREEN[0][2] != corr(MU_NN, 0, 2),
      "geometric against linear decay: the record correlator of mu_NN is not a Laplacian Green kernel")

# ---------------------------------------------------------------- section 3
print()
print("== 3. A supplied long-range law, excluded by the nearest-neighbour sentence ==")
check("mu_LR: normalised, flip-invariant, reflection-covariant; every one-point mean is exactly 0",
      sum(MU_LR.values()) == 1 and all(MU_LR[v] == MU_LR[tuple(-x for x in v)] for v in MU_LR)
      and all(MU_LR[v] == MU_LR[tuple(reversed(v))] for v in MU_LR)
      and all(mean(MU_LR, i) == 0 for i in range(N)))
C_LR = corr(MU_LR, 0, N - 1)
check("mu_LR record correlator is distance-blind: one exact value on every pair, far above the geometric tail",
      len({corr(MU_LR, i, j) for i, j in ALL_PAIRS}) == 1 and C_LR == Fr(835,867),
      f"c_LR = {C_LR} on every pair against c_NN(0,7) = 1/2187")
check("the chain rule of mu_LR is order-blind: two explicit formation orders reproduce mu_LR exactly",
      law_by_order(MUW_LR, tuple(range(N))) == MU_LR
      and law_by_order(MUW_LR, (3, 6, 0, 5, 1, 7, 2, 4)) == MU_LR,
      "order-blind, yet not an admissible rule: see the two reading checks below")


NBR = {i: {j for j in (i - 1, i + 1) if 0 <= j < N} for i in range(N)}


def static_conditional(muw, i, v):
    """P(v_i = v[i] | all other sites): the static reading of the sentence."""
    flip = list(v)
    flip[i] = -v[i]
    return muw[tuple(v)] / (muw[tuple(v)] + muw[tuple(flip)])


def static_nn_only(muw):
    """True iff every single-site conditional ignores every non-neighbour flip."""
    for v in product((1, -1), repeat=N):
        for i in range(N):
            base = static_conditional(muw, i, v)
            for j in range(N):
                if j != i and j not in NBR[i]:
                    w = list(v)
                    w[j] = -v[j]
                    if static_conditional(muw, i, tuple(w)) != base:
                        return False
    return True


ALLP = tuple([1] * N)
FAR7 = tuple([1] * (N - 1) + [-1])
check("static reading: mu_NN conditionals depend on neighbours alone (all 256 configurations, 8 sites)",
      static_nn_only(MUW_NN))
check("static reading has teeth at distance two: one supplied next-nearest bond (0,2) is excluded",
      not static_nn_only(make_mu(NN_EDGES + [(0, 2)])[0]))
check("static reading: mu_LR is excluded, its site-0 conditional moves when the far site 7 flips",
      not static_nn_only(MUW_LR)
      and static_conditional(MUW_LR, 0, ALLP) != static_conditional(MUW_LR, 0, FAR7),
      f"{static_conditional(MUW_LR, 0, ALLP)} against {static_conditional(MUW_LR, 0, FAR7)}")
P0 = tuple([1] + [None] * (N - 1))
M0 = tuple([-1] + [None] * (N - 1))
F_PP = W_marg(MUW_NN, P0[:2] + (1,) + P0[3:]) / W_marg(MUW_NN, P0)
F_MP = W_marg(MUW_NN, M0[:2] + (1,) + M0[3:]) / W_marg(MUW_NN, M0)
check("formation reading: mu_NN's chain rule conditions on a formed non-neighbour (site 2 given site 0)",
      F_PP == Fr(5, 9) and F_MP == Fr(4, 9),
      "5/9 against 4/9 with site 1 unformed: as a formation rule it is outside the sentence")

LR_PP = W_marg(MUW_LR, P0[:2]+(1,)+P0[3:]) / W_marg(MUW_LR,P0)
LR_MP = W_marg(MUW_LR, M0[:2]+(1,)+M0[3:]) / W_marg(MUW_LR,M0)
check("formation reading: all-pairs chain conditional depends on the non-neighbour at site 0",
      LR_PP == Fr(851,867) and LR_MP == Fr(16,867))

MUW_END, MU_END = make_mu(NN_EDGES + [(0, N - 1)])
check("one supplied long bond changes direct and indirect correlations",
      corr(MU_END, 0, N - 1) == Fr(1095,3281)
      and corr(MU_END, 0, 4) < 2 * Fr(1, 3 ** 4),
      f"c_END(0,7) = {corr(MU_END, 0, N - 1)}, c_END(0,4) = {corr(MU_END, 0, 4)}")

# ---------------------------------------------------------------- section 4
print()
print("== 4. Glued-support rigidity: exact long-range order with blind two-points ==")
S33 = [(r, c) for r in range(3) for c in range(3)]
I33 = {s: i for i, s in enumerate(S33)}
NB33 = {i: [I33[(r + dr, c + dc)] for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (r + dr, c + dc) in I33]
        for (r, c), i in ((s, I33[s]) for s in S33)}
ROLE = ["VLPC"[(r % 2) + (c % 2)] for (r, c) in S33]
VS = [i for i, x in enumerate(ROLE) if x == "V"]
CHECKS = {v: tuple([v] + [u for u in NB33[v] if ROLE[u] == "L"]) for v in VS}
S_GAUSS = [p for p in product((0, 1), repeat=9) if all(sum(p[m] for m in CHECKS[v]) % 2 == 0 for v in VS)]


def par(sample, sites):
    tot = Fr(0)
    for p in sample:
        tot += Fr((-1) ** (sum(p[s] for s in sites) % 2), 1)
    return tot / len(sample)


ALL9 = list(product((0, 1), repeat=9))
check("uniform Gauss-set law: every one-point and every two-point parity expectation is exactly 0",
      len(S_GAUSS) == 32 and all(par(S_GAUSS, (i,)) == 0 for i in range(9))
      and all(par(S_GAUSS, (i, j)) == 0 for i in range(9) for j in range(i + 1, 9)))
C1, C2, C3 = CHECKS[VS[0]], CHECKS[VS[1]], CHECKS[VS[2]]
SUM12 = tuple(s for s in range(9) if (s in C1) != (s in C2))
SUM13 = tuple(s for s in range(9) if (s in C1) != (s in C3))
check("every check parity is exactly 1, and check sums give exact 4-point order across the window",
      all(par(S_GAUSS, CHECKS[v]) == 1 for v in VS)
      and par(S_GAUSS, SUM12) == 1 and par(S_GAUSS, SUM13) == 1
      and len(SUM12) == 4 and len(SUM13) == 4,
      "multi-point record observables locked at 1 at full window span, with no tick and no dynamics")
NON_DUAL = (VS[0], C2[1], C2[2])
check("a non-dual triple has parity exactly 0: the rigidity sits precisely on the dual code",
      par(S_GAUSS, NON_DUAL) == 0)
check("free-alphabet contrast: under fair coins every listed parity is exactly 0 (empty-set parity 1 guards the normaliser)",
      all(par(ALL9, CHECKS[v]) == 0 for v in VS) and par(ALL9, SUM12) == 0 and par(ALL9, NON_DUAL) == 0
      and par(ALL9, ()) == 1 and par(S_GAUSS, ()) == 1,
      "the long-range order is a support property: it matches neither the geometric nor the Laplacian kernel")

print()

check_words = [sum(1 << i for i in CHECKS[v]) for v in VS]
dual = {0}
for w in check_words:
    dual |= {x ^ w for x in list(dual)}
check("complete character census: all 512 parities are one on the 16-word dual and zero elsewhere",
      len(dual)==16 and all(par(S_GAUSS,tuple(i for i in range(9) if mask>>i&1)) == (1 if mask in dual else 0) for mask in range(512)))

print('per_element: Exact finite arithmetic verifies the declared algebraic identities and explicit model comparisons; it does not select physical axioms.')
print('per_site: The supplied finite windows, alphabets and conditional rules fix the scope; other local laws and representations remain unclassified.')
print('per_mode: Analytic statements require the explicit assumptions and proofs in the note; finite sample checks alone do not establish a universal theorem.')
print('per_block: The fresh runner output certifies the implemented finite controls; historical author mutation tables are provenance rather than fresh review evidence.')
print('lattice_wide: No continuum limit, physical field identification, universal law selection or retained audit status is established by this finite certificate.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
