# Block 171 (B1) — the trilemma, the class map, the K-identities

INERTIA CONVENTION BANNER, first and with teeth. Every triple is in the `(n_+, n_-, n_0)` order
of `b165.real_symmetric_inertia`, stamped inline as `(a,b,c)(n+,n-,n0)[b165]`. The landed
`b163/b164` `congruence_inertia` returns `(n_+, n_0, n_-)`; the literal `(4,0,4)` here means PSD
at rank 4.

SCOPE. Committed antiperiodic Dirac-Kahler fixture, region-pinned at links `{c-1, c}`, `c = 1`,
at **12x4 (T_phys = 6, THE BENCH)** and **8x4 (T_phys = 4, disclosed cross-check, carries no
verdict)**. Exact rationals; no float; no `nsimplify`. Every negative is NON-SUPPLY within this
pairing/quotient formalism (CYCLE913), never necessity. Run: `$S/b171_run.txt`, 50 checks, 50
PASS, 55.3 s.

## 0. PRE-REGISTRATION — written before the leg-(iii) computation

DISCLOSURE, load-bearing: scouting probes (`_b171_probe5.py`, `_b171_probe7.py`) preceded this
registration and fixed the expectations in the `s_x` and connection-off columns at both scopes.
**Registered strictly before any computation:** the holonomy-dial column, the `s_t`-derivative
column, the moment-weight row W8 entirely, every K-identity, F8, and every 12x4 verdict for W2,
W5, W7, W10.

Two scopes, both tested for every W, with `W(a) = tr(G_scope.Pi_a)/tr(G_scope)`: **SC** — the
slice-`c` block, class map = its `L_x` site projectors (the calibrated scope the panel named);
**RS** — the block of the record's own free time level `t*`, class map = its `L_x` site
projectors (THIS BLOCK'S scope, a disclosed premise-class probe).  Registered transport-off
(iii-b) / holonomy (iii-d) expectations, per W: **SAME/SAME** for W1 `herm(Q)=m.quotient(H)` (by
theorem), W2 `herm(Q)^{-1}` (sign-quenched, landed), W3 Schur of `[rQ]_(S,S)`, W4
`B=m.diag(D(c,.))` (b166 induced state); **UNDEFINED (0/0)/differ** for W5 `A^dag A`;
**differ/differ** for W6 `Q^dag Q`, W7 `herm(Q)+A^dag A`, W8 (b170 moment matrix, class map =
the 4 families, leg (i) CONDITIONAL — expect not PSD at small `m`), and the two own designs W9
`herm(Q^{-1})`, W10 `Q^dag herm(Q)^{-1} Q` (leg (i) BY THEOREM). Registered leg (ii): SC fail /
RS pass for W1, W2, W6, W7, W9, W10; fail for W3, W4; unknown for W8. PR-1..PR-5: (1) slice `c`
is a direct summand of `Q` on the region and `Q[c,c]` is record-free, so leg (ii) fails at SC
for the WHOLE class; (2) W5's normalized profile is degree-2 homogeneous in the connection at
`s_t = 0`, hence blind to rescaling `s_x`; (3) the LANDED `graded` carrier is `x`-homogeneous, a
SECOND null fixture; (4) K1 is a theorem for the site class map and fails for the sigma-value
alphabet; (5) F8 does not fire at RS at `T_phys = 6`.

**ALL FIVE CONFIRMED. No pre-registered expectation was refuted.**

## 1. T1 — THE TRILEMMA TABLE. Verdict: **the trilemma has a solution.**

Bench 12x4, region pin, `s_x = 3/5`, `m = 1`, `x`-graded probe carrier `sigma = 3/5`. Leg (iii)
is the five-dial battery `{conn-off, s_x, s_t at 0, holonomy g_t, holonomy g_x}`; pass needs
MOVE on conn-off, `s_x` and both holonomy dials. All RS inertias are `(4,0,0)(n+,n-,n0)[b165]`.

| W | SC (i,ii,iii) | RS (i,ii,iii) | memory depth |
|---|---|---|---|
| W1 `herm(Q)` | P F P | P P **F** | 1 |
| W2 `herm(Q)^{-1}` | P F **F** | P P **F** | full |
| W3 = W4 on region | P F F | — | 0 |
| W4 `m.diag(D(c,.))` | P F F | — | 0 |
| W5 `A^dag A` | F F F | F P F | 1 |
| W6 `Q^dag Q` | P F P | **P P P** | 1 |
| W7 `herm(Q)+A^dag A` | P F P | **P P P** | 1 |
| W8 moment matrix | leg (i) conditional and FAILING on the full matrix (herm-part `(16,0,0)` connected / `(15,1,0)` full `(n+,n-,n0)[b165]`); leg (iii) P | — | — |
| W9 `herm(Q^{-1})` | P F P | **P P P** | **full** |
| W10 `Q^dag herm(Q)^{-1} Q` | P F P | **P P P** | **full** |

**WINNING SET, scoped to this enumeration and no wider: `{W6, W7, W9, W10}` at RS scope, 12x4**
— same at 8x4. **THE CANDIDATE: `W9 = herm(Q^{-1})`.** Selection criterion, stated: full memory
depth (W6 and W7 see only the adjacent level); it is the Hermitian part of the covariance the
committed Gaussian measure actually supplies (`G = Q^{-1}`); and its shim twin `W2 =
herm(Q)^{-1}` differs from it only in the ORDER of `herm()` and inverse and is LANDED
transport-blind (= the connection-off covariance entrywise, re-verified here at both extents;
its profile differs from W9's at both extents). The anti-shim separation is exhibited inside one
formula.

Leg (i) for W9 and W10 is a **theorem**, both identities verified entry for entry at both
extents: `herm(Q) > 0` implies `herm(Q^{-1}) = Q^{-1} herm(Q) Q^{-dag} > 0`, and `Q^dag
herm(Q)^{-1} Q = herm(Q) + A^dag herm(Q)^{-1} A >= herm(Q) > 0` (using `A^dag = -A`). The
hypothesis `herm(Q) > 0` is measured `(24,0,0)` / `(16,0,0)` `(n+,n-,n0)[b165]` at `m in {1,3}`
on the bench carriers — a CENSUS, not a theorem in `m` and the moduli. **Consequence worth
naming: leg (i) does not need the positive region at all** — only `herm(Q) > 0`, a global fact
about the committed action. The region pin's remaining job is to define the alphabet.

**THE OBSTRUCTION, the sharpest thing in this block. S1** (symbolic, all free symbols, both
extents): On the region at `s_t = 0`, slice `c` is a DIRECT SUMMAND of `Q`: `Q[c,k] = Q[k,c] =
0` for every `k != c`. **S2 (symbolic, both extents).** `Q[c,c]` contains NO free-shear symbol —
its symbols are exactly `{m, s_x, n_(0,.), n_(1,.), u_(0,.)}`. **COROLLARY.** `Q = Q_cc (+)
Q_rest`, so `f(Q)_cc = f(Q_cc)` for every `f` built from `Q`, `Q^dag`, inverses, sums and
products, and `Q_cc` is record-free. **Every weight got by compressing such an `f` to slice `c`
is RECORD-BLIND BY THEOREM — leg (ii) fails at SC for the whole class, W9 included, measured 7
of 7.** Exhibited: `herm(Q^{-1})_cc == herm((Q_cc)^{-1})` entry for entry.

This SUPERSEDES the panel's mechanism ("the calibrated `G = m.diag(D(c,.))` carries no shear
symbols"): the calibrated Gram is record-free *because* slice `c` is disconnected and its two
incident links are pinned. The escape is not a different functional but a different SCOPE — at
RS scope `Q` is not block-diagonal and the same constructions become record-sensitive. **The
theorem-shaped statement a follow-up checker could refute:** *for the committed quotient action
on the region at `s_t = 0`, `c = 1`, at 8x4 and 12x4, no function `f` of `(Q, Q^dag)` closed
under sums, products and inverses has a slice-`c` compression depending on any free shear.*
Refute by exhibiting one, or at wider scope by an `f` outside that closure (entrywise,
reflection-mixed).

Three rows carry their own theorems. **W3 == W4 on the region, exactly:** at `s_t = 0` the
corner `C = s_t.C_1` vanishes, so the Schur complement of `[rQ]_(S,S)` IS `B = m.diag(D(c,.))`,
whose symbols are `{a_(0,.), a_(1,.), n_(1,.), u_(0,.)}` — no shear, no connection. That is the
margin law's mechanism written out: `m.kappa_2 = 57/160` with `kappa_2` shear-blind BY FORCE, no
run needed. **W5** fails leg (i) at connection-off (`tr(G) = 0`, ratio `0/0`) and leg (iii) by
homogeneity: at `s_t = 0`, `A = s_x.A_x`, so `A^dag A = s_x^2 . A_x^dag A_x` and the normalized
profile is invariant under rescaling `s_x` — the affine/homogeneity shim signature at the weight
level. **W8** is NOT Hermitian at either extent (`G = Q^{-1}` is not), so it is not a state; its
diagonal is real and positive so the ratio still normalizes, but the full matrix's Hermitian
part is not PSD at the bench.

### Two null fixtures, not one

The flat carrier is exactly uniform, as landed. **NEW: the LANDED `b166.graded_carrier` is
`x`-homogeneous — `(3t + 5x) mod 5 = 3t mod 5` — so on it EVERY site profile is exactly
`(1/4,1/4,1/4,1/4)` at both scopes for every construction in the battery.** A second null
fixture; nothing may be benched there. This block therefore discloses an `x`-inhomogeneous probe
carrier (`(3t + 2x) mod 5`), verified inside the positive region (`[rQ]_(S,S) =
(4,0,4)(n+,n-,n0)[b165]`, both extents).

## 2. T2 — THE CLASS MAP AND THE K-IDENTITIES

**Record alphabet, declared:** the landed `b166.free_shears`, the shears the region leaves free
— **16 at 12x4, 8 at 8x4** (`2 L_x (T_phys - 2)`). Two class maps, both declared and tested.
**CM-SITE** — the `L_x` site projectors of the record slice: Hermitian, idempotent, mutually
orthogonal, `sum_a Pi_a = 1` **EXACTLY at both extents**, `|A| = L_x = 4 >= 3` so the
coarse-graining leg is not vacuous — **it IS a resolution of the identity**. **CM-VALUE** —
`sigma in {0,1/5,2/5,3/5}`, `b = -nu.sigma/(1-sigma^2)`: **NOT a projector partition**, being
cone-membership values of a continuous modulus with no attached orthogonal decomposition and no
landed operator having them as spectrum; DECLARED absent, not measured absent, refutable by
exhibiting such an operator. Two wirings follow. **G-A**: slots = free TIME LEVELS, alphabet =
sites, record implemented as the disconnection pin `sigma_(t,x) -> 0` (N1: the recording rule IS
the disconnection rule). **G-B**: slots = free LINKS (`L_x` per level), alphabet = CM-VALUE.

| identity | verdict | how |
|---|---|---|
| **K1** G-A | **THEOREM** | `sum_a tr(G.Pi_a) = tr(G)` for a FULLY SYMBOLIC Hermitian `G` — an identity in the free symbols, trail-length independent, lifting by induction to every `T`; re-verified numerically-exactly on W9 over every declared trail at BOTH extents |
| **K1** G-B | **FAILS** | exact nonzero defect at both extents (193-digit numerator over 192-digit denominator at 12x4). The four ratios `W(t.a)/W(t)` are each near 1, so the sum is near `\|A_v\| = 4`: structural, not small. Under G-B normalization is an INPUT, by fiat |
| **K2** action | **THEOREM** | appending two records at two links of ONE slice in either order gives the SAME action entry for entry, free symbols still present, both extents — so it holds for every weight at every trail length |
| **K2** weight | **FAILS** | the JOINT weight of the same two records differs between the two slot orders by an exact nonzero rational at BOTH extents |
| **K3** support | **HOLDS** | `W(t) > 0` and every class weight strictly positive on every declared trail, both extents — no `0/0` in the tower for W9 |

**The K2 failure is this block's sharpest negative and it is not a bug.** The substitution
commutes; the chain-rule product of conditionals does not, because `G_t` depends on the trail
NON-LINEARLY. Precisely: the finite-window family is NOT Kolmogorov-consistent under
re-enumeration of the `L_x` links of one slice, so **Kolmogorov's extension theorem does not
apply. Ionescu-Tulcea still does** — it needs only K1 + K3 at a FIXED declared slot order, which
the generator has by theorem and by computation at both sizes. **The slot order is therefore an
INPUT to the generator, not a derived object, and must be declared with it** — a new, named,
owner-visible premise.

## 3. T3 — F8, AND THE BLINDNESS TRANSFER

At **RS scope, bench 12x4: `D5 != 0`** — `P(a|trail)` MOVES between two equal-length trails of
different content, so `W(t.a) != W(t).W(a)`: the law is **NOT trail-blind** and does not
factorize over the record partition. It also fires on the recorded VALUE at fixed record SITES
(`D5' != 0`), so the sensitivity is to the record's content, not only its support. **At SC scope
F8 fires the other way: `D5 = 0` exactly at both extents — the law IS trail-blind there** (the
panel's finding reproduced, now explained by S1+S2). **Blindness transfer (lens R2): `D2 != 0`**
— the profile moves between carrier `sigma = 1/5` and `sigma = 3/5` — so the candidate is not
carrier-blind, hence not count-proportional in disguise, and does not inherit the boundary
note's many-to-one kill. All separations are exact rationals in the run log with their
denominators.

## 4. T4 — THE B2/B3 HOOK

`$S/b171_profile_table.py` carries 32 rows `(extent, trail, weight profile, frequency profile)`
as exact `(numerator, denominator)` literals, plus both null fixtures and the bench carrier,
schema documented in the file. Trails are `(x_1, x_2)`: record sites at the first two free time
levels, each a disconnection pin; every profile sums to 1 exactly. At 12x4: **16 of 16 distinct
weight profiles; 10 of 16 distinct frequency profiles; 0 weight profiles carry two frequency
profiles** (so `W` determines the frequency profile here — the bridge is a function); **6 of the
10 frequency profiles carry TWO distinct weight profiles.**

**PRE-CENSUS DESIGN RESULT FOR B2.** On the site alphabet the census WILL find collisions, for
the combinatorial reason the boundary note already landed: `(x1,x2)` and `(x2,x1)` share a
frequency profile and have different weights. **B2's "zero collisions => theorem candidate"
branch is UNREACHABLE on this alphabet**; B2 must run the REFINEMENT (Gleason-shaped) variant
the synthesis specifies — additivity across refinements of a fixed record.

**What replaces the boundary note's hand-supplied IID `p`.** The note hands in
`binomial_weight(N, k, p)` with `p = 0.7` by hand — no Gram, no carrier, no shear, nothing
lattice-valued. Its replacement at the c679 harness interface is `P(a | trail) =
tr(herm(Q^{-1})_(t*,t*) . Pi_a) / tr(herm(Q^{-1})_(t*,t*))` on the region at the declared
carrier: an exact-rational, slot-dependent, trail-dependent, carrier-dependent,
connection-carrying probability vector derived from the committed action with no free parameter.
It is **not** an IID `p` — slot dependence means no stationary kernel (the Gram-not-moment
result stands) and F8 means trail dependence. B3 must replace the harness's IID sampler with a
forward Ionescu-Tulcea walk over the declared slot order; the open residue is ergodicity —
nothing here supplies convergence of window frequencies.

## 5. WHAT IS NOT CLAIMED

Not an inner product, not a GNS space, not a semigroup, not a transfer operator — the region pin
still costs time-translation invariance (b170 N4) and the block is a Gram, not a moment
sequence. Two extents are not a limit. The RS scope, the `x`-graded probe carrier, W9, W10 and
both generator wirings are PREMISE-CLASS PROBES of this block, not framework objects; nothing is
registered or adopted. The trilemma verdict is scoped to the enumerated battery `{W1..W10}`, the
five declared trails and the five dials; "the winning set is exactly `{W6,W7,W9,W10}`" ranges
over that enumeration and no wider.
