# Independent hostile review of KN_ADOPT.md

## PRE-STATED — 2026-10-28T21:49:51Z

Scope: review the proposed KN_ADOPT section 8.1 insertion using the owner's restricted source list and at most two additional files. No git operations; only this deliverable may be written. This statement precedes mathematical derivation and inspection of the target.

Targets and pre-stated refutation criteria:

1. **Transport identity / H1-F2.** Reconstruct the indexed averaged transport used in (R1). Refutation: convex weights apply to a different map, contour indices or translations fail to match, or a load-bearing identification is unsupported in the permitted evidence. Unsupported identification receives NOT-VERIFIED / GAP, not a fabricated counterexample.
2. **Degeneracy.** Enumerate the d=4, L=3 index set using plain Python and exact combinatorics. Refutation: the stated 1944 indices, 633 distinct transporters, or multiplicities/weights disagree with the explicitly defined path object. Distinguish formal paths from possible coincidences for special gauge fields.
3. **Side conditions and exponent.** Derive S1–S4 and the identity (L^2 + 5.5 A_d)c_1=1/2 with symbols tied to their definitions. Refutation: an inequality fails on the claimed input range, a minimum is stale, or a changed kernel estimate is disguised as an unchanged exponent.
4. **Reversals and constants.** Rebuild eta_1/eta_q, the route ratio, and 13/512 with exact arithmetic. Refutation: any quoted ratio uses incompatible definitions, an unstated minimum, or a wrong N/epsilon dependence.
5. **Baseline and gain.** Determine whether RS-lin is actually derived and active at the same interface. Refutation: the claimed incremental gain compares against a superseded quadratic route, or the purported existing linear route lacks its required hypotheses.
6. **Decidability / patch safety.** Inspect each accessible gate for circularity, vacuity, frozen inputs, and omitted branches. Give a yes/no append recommendation and the smallest sufficient correction.

Review findings use CONFIRMED / NOT-VERIFIED / REFUTED. Mathematical claim statuses use PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED means independently checked within the stated scope; labels in source files are not proof. Arithmetic will be exact rational/symbolic plain Python only. Decimal decade claims will be tested with rational enclosures if needed.

## Findings (appended during review)

### F1 — CONFIRMED for axial-path labels; REFUTED for distinct transporters

**Attaches to:** KN_ADOPT.md §1.6, string `633 distinct (path, y) pairs`, and §6 row `degeneracy of the index→transporter map`; checks/kn1_criteria.md `DEGENERATE-BUT-CONVEX`.

For k nonzero coordinates of y−c_X, the number of distinct (y, axial-path) labels is binom(4,k)2^k k!, each with multiplicity 24/k!. Summing gives 633 labels. Their multiplicity histogram is **{1:384, 4:192, 12:48, 24:9}**, hence exactly the four listed weights. This restricted combinatorial claim is PROVEN.

But these labels are not distinct T transporters. RLARGE.md:989–991 itself says a μ-directed rectangle is degenerate/backtracking. Take y−c_X∈{−e_μ,0,+e_μ}: all 72 indexed terms give the same straight transporter S_c, regardless of σ. Its merged weight is **72/1944=1/27**, absent from the claimed list. Thus the claim about distinct transporters fails even before choosing a gauge field.

Independent plain-Python enumeration of the full word P·μ^3·P_translated^{-1}, cancelling adjacent inverse edges, gives **475 freely reduced transport paths**, with multiplicity histogram

| multiplicity | number of reduced paths | induced weight |
|---:|---:|---:|
| 1 | 288 | 1/1944 |
| 4 | 96 | 1/486 |
| 6 | 48 | 1/324 |
| 12 | 12 | 1/162 |
| 20 | 24 | 5/486 |
| 48 | 6 | 2/81 |
| 72 | 1 | 1/27 |

Counts sum to 475 and multiplicities sum to 1944. A separate counting derivation: with k nonzero transverse coordinates, there are binom(3,k)2^k k! transverse paths; for each, one class with no surviving μ excursion and 2k classes with a signed μ excursion before the last transverse step. Therefore the count is Σ_{k=0}^3 binom(3,k)2^k k!(1+2k)=475. The no-excursion multiplicities are 24/k!+48/(k+1)!; the excursion multiplicities are 24/(k+1)!. This reproduces the histogram without the enumeration algorithm.

These are formal reduced paths on the local lattice, not a claim that their matrix values differ on every field; at the identity field they all coincide. **Convexity survives every merging.** Minimal correction: call 633 the count of `(y, axial-path)` labels only, or replace the distinct-transporter refinement by the reduced-path count and weights above.

### F2 — REFUTED: the proposed minimum has a stale ε_1 crossover

**Attaches to:** KN_ADOPT.md §8.1, string `it would take ε_1 > 814.587 for the other branch, N = 2`.

After η_1=ε_1/117,

    a_RS = ε_1²/N · min{1/27378, κ/256}.

The branch boundary is **κ=128/13689**, independent of ε_1 and N for ε_1>0. At κ=1 the plaquette entry wins at every positive ε_1 for which the lemma applies; there is no ε_1=814.587 crossover. For κ<128/13689 the kernel entry wins at every positive ε_1. This is a PROVEN algebraic refutation and a direct instance of a stale minimum surviving a substitution.

The cited RLARGE.md:1020 defines a symbolic κ; it does not set κ=1. checks/kn1_criteria.md's `a_RS` input row imports κ=1 without a supporting definition in the permitted RLARGE ranges. Numerical gain rows at κ=1 are conditional evaluations, not a discharge for arbitrary κ.

### F3 — REFUTED: these exponent comparisons are live v3 coupling-ceiling gains

**Attaches to:** KN_ADOPT.md §8.1 item 4, string `l.618 must be edited regardless`, and item 7's `honest ledger line`; REVIEW_ARS_EPS_S1.md §1 item 2 / summary RA-17.

RLARGE.md:433–439 explicitly retires the old case split, the 81 and 5⁴ greedy factors, and a_♯ for unreturned defects. RLARGE.md:832 replaces a_♯/n_♯ by a=min{θa_bad,a_A}; :835 says the frozen §7.3 route is not used by RLF-step v3. The actual :616–618 ceiling uses this a, not a_RS. Therefore replacing a by a_RS/625 and declaring :618 false is a change of object, not a correction of its arithmetic.

The second reviewer is right that an existing joint-route baseline must be considered, but **its own phrase “lane's own best proven route” is not established by the PROVEN-HERE list at RLARGE.md:628**. The permitted text supplies neither the RS-lin proof nor a live v3 use of its joint pricing; :434–437 instead explicitly removes that pricing from the unreturned-defect route. The live gain is **NOT-VERIFIED / GAP**, not automatically either 82.1406 or 2.3033 decades. The latter is a valid comparison of the two displayed historical/bare-level exponents under their branch assumptions, evaluated below.

