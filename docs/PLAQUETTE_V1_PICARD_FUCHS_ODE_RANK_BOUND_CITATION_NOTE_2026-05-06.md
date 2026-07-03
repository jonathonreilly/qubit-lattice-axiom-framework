# Plaquette V=1 Picard-Fuchs ODE: Finite-Window Rank-Bound Boundary Note

**Date:** 2026-05-06; 2026-06-07 finite-window boundary repair.
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py`](../scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py)
(SUMMARY: FINITE-WINDOW BOUNDARY PASS=5 FAIL=0)
**Cached runner output:** [`logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt`](../logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt)
**Certificate JSON:** [`outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json`](../outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json)
**Source packet verifier:** [`scripts/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.py`](../scripts/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.py)
(SUMMARY: SOURCE PACKET MANIFEST PASS=52 FAIL=0)
**Source packet verifier cache:** [`logs/runner-cache/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.txt`](../logs/runner-cache/frontier_su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.txt)
**Source packet verifier JSON:** [`outputs/su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.json`](../outputs/su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.json)
**Companion context notes:** [`PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md)
and [`PLAQUETTE_V1_PICARD_FUCHS_ODE_MINIMALITY_PROOF_NOTE_2026-05-06.md`](PLAQUETTE_V1_PICARD_FUCHS_ODE_MINIMALITY_PROOF_NOTE_2026-05-06.md).
The load-bearing current bridge for this row is finite-window support plus an
explicit open blocker: the primary runner does **not** certify all-degree
minimal-annihilator closure.

## 2026-06-07 Audit Boundary Repair

The prior source wording overclaimed the primary runner as an all-order
minimal-annihilator certificate. The independent audit correctly identified the
gap: T2 excludes order-`<=2` annihilator cells only on a finite
`degree <= 30` search grid, so it does not prove absence of lower-order
polynomial-coefficient annihilators at arbitrary degree.

This repair preserves the useful science and removes the overclaim:

- T1 remains a D-finiteness witness for the Bars/Bessel determinant packet.
- T2 is finite-grid support: all scanned `r <= 2, d <= 30` cells vanish, and
  the order-3 degree-2 candidate appears in the grid.
- T3 is only conditional Bostan-Salvy-Schost arithmetic: if an external
  all-degree `R=3,D=2` minimal-annihilator bound is supplied, the depth
  threshold would be exceeded.
- T4 remains the Frobenius-branch/indicial-polynomial check for the candidate
  operator.
- T5 remains the depth-200 regression of the Taylor/recurrence certificates.

**Current source-side status:** bounded finite-window support. This note does
not claim the all-degree lower-order exclusion and does not promote the V=1
Picard-Fuchs row beyond independent audit.

## 2026-06-04 Source Packet Exposure Repair

The current audit blocker asks for a non-circular all-degree
creative-telescoping/minimal-annihilator certificate together with complete,
untruncated primary and helper runner sources. This revision exposes the
restricted packet as repo files instead of prose-only excerpts.

**Complete source packet manifest:**

- Primary finite-window boundary runner: [`scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py`](../scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py)
- Finite-window helper runner: [`scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py`](../scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py)
- Extended minimality helper runner: [`scripts/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.py`](../scripts/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.py)
- Original ODE runner: [`scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py`](../scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py)
- Primary finite-window boundary cache: [`logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt`](../logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt)
- Finite-window helper cache: [`logs/runner-cache/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.txt`](../logs/runner-cache/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.txt)
- Extended helper cache: [`logs/runner-cache/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.txt`](../logs/runner-cache/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.txt)
- Primary finite-window boundary JSON: [`outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json`](../outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json)
- Finite-window helper JSON: [`outputs/su3_v1_picard_fuchs_minimality_2026_05_06.json`](../outputs/su3_v1_picard_fuchs_minimality_2026_05_06.json)
- Extended helper JSON: [`outputs/su3_v1_picard_fuchs_minimality_extended_2026_05_06.json`](../outputs/su3_v1_picard_fuchs_minimality_extended_2026_05_06.json)

The verifier above checks that all manifest paths exist, the note names each
path, the helper sources contain the load-bearing exact-rank functions
`matrix_for_ansatz` and `_rank_via_numeric`, and the runner caches are
SHA-pinned to the current untruncated source files. This does not set an audit
verdict; it makes the existing certificate packet independently reauditable
as a finite-window boundary packet.

## 2026-05-29 Audit Repair Attempt (superseded boundary)

The text below records the previous attempted all-order repair route. It is no
longer the live claim boundary after the 2026-06-07 repair above. In
particular, statements that T2 supplies an all-degree minimal-annihilator
certificate are superseded by the finite-window boundary: T2 scans
`r <= 2, d <= 30` and does not exclude arbitrary coefficient degree.

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The restricted packet supplies retained bounded finite-window companion notes, but not a closed bridge proving rank/order ≤ 3 or excluding order ≤ 2 annihilators at arbitrary coefficient degree. The source note itself identifies that missin"*

with repair: *"missing_bridge_theorem: provide either a retained explicit SU(3) order/rank ≤ 3 citation or an auditable creative-telescoping/minimal-annihilator certificate closing the all-degree lower-order exclusion."*.

The repo contains a useful finite-window certificate runner and cached output:
`frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py`.
This runner no longer supplies the audit-requested all-degree
creative-telescoping/minimal-annihilator closure. It supplies bounded support
and preserves the open all-degree blocker.

The finite-window packet supports:

- `[T1]` `J(β)` is D-finite via the Bars Bessel-determinant identity,
  an explicit holonomic-closure annihilator for the `D_0` summand, and
  Stanley/Lipshitz closure;
- `[T2]` all order-`≤2` cells in the scanned Koutschan-style certificate
  vanish through coefficient degree `30`, and the order-3 degree-2 candidate
  appears in that grid;
- `[T3]` the Bostan-Salvy-Schost depth-sufficiency threshold arithmetic would
  be `M_0 = 17` if an external all-degree `R=3,D=2` minimal-annihilator bound
  were supplied; the runner verifies the candidate ODE through degree `196`,
  but this is conditional arithmetic, not standalone all-order closure;
- `[T4]` the indicial polynomial `6s(s+3)(s+4)` identifies the unique
  analytic Frobenius branch at `β=0`, normalized by `J(0)=1`;
- `[T5]` the depth-200 regression rechecks the Taylor and recurrence
  certificates.

Therefore the all-degree lower-order exclusion remains unresolved for this row.

## Audit gap addressed

The minimality-proof note (commit `2ea6e2bae`) closes the V=1 PF ODE
minimality conditional via six steps. Step 4 invokes the bound

> Bernstein rank bound for SU(N) Wilson character integrals: rank(J) ≤ N

(in the note's prose, with N = 3 written as "rk(SU(3)) = 3"; see
[Errata](#errata-on-the-companion-note) below for that wording fix).

The minimality theorem reads cleanly only if this rank bound is
externally attestable. This note investigates the literature, identifies
the closest available theorem statement, and then states honestly what
this allows the V=1 PF ODE minimality theorem to claim and what it does
not.

## Setup

```text
J(β) = ∫_{SU(3)} exp(β · Re Tr U / 3) dU,           J(0) = 1.
```

PR #541 produced an annihilating polynomial-coefficient differential
operator `L` of order 3 and coefficient degree 2:

```text
L = 6 β² ∂³  +  β(60 − β) ∂²  +  (−4β² − 2β + 120) ∂  −  β(β + 10) · 𝟙.
```

We need: **no operator of order ≤ 2 with polynomial coefficients of
ANY degree annihilates `J(β)`**, given that the order-3 operator `L`
exists.

## Investigation outcome

The literature search produced four relevant frameworks. Each is
strictly weaker than the clean rank-≤-3 bound the companion note
invokes; combining them gives a rigorous answer of a different shape.

### Framework A — Bernstein 1972 (existence only)

Bernstein's theorem on holonomic D-modules guarantees that `J(β)` is
annihilated by *some* non-zero polynomial-coefficient differential
operator. It does not bound the order. ([1])

### Framework B — Aomoto-Gelfand A-hypergeometric rank

The Aomoto-Gelfand framework gives a holonomic system attached to a
matrix `A` and parameter vector `β`, with rank equal to the normalized
volume of the corresponding polytope for generic parameters and rank
inequality `rank(M_A(β)) ≥ vol(A)` in the non-generic case. ([4],[2])

The framework requires a torus-action realization; the SU(3) Wilson
integral does not natively present as an A-hypergeometric system on a
toric variety, so this rank theorem does not directly apply. The
abstract Aomoto-Gelfand theorem on hypergeometric integrals on
configuration spaces of hyperplane arrangements similarly does not
cover the compact-Lie-group case.

### Framework C — Sabbah / Hotta-Takeuchi-Tanisaki (D-module direct image)

Sabbah's monograph and HTT chapter 5 give the direct-image construction
for D-modules, with rank-preservation under proper push-forward and a
Künneth-type bound under product. ([5],[6])

The Sabbah / HTT framework gives the **abstract existence** of a finite
holonomic rank for a parameter integral over a smooth proper algebraic
family, but does not give a closed-form rank bound `≤ N` for the
specific SU(N) Wilson integral.

### Framework D — Creative telescoping (Wilf-Zeilberger / Koutschan)

This is the framework that delivers an effective bound. Each modified
Bessel function `I_n(β/3)` is order-2 holonomic in β. The Bars 1980
identity ([3])

```text
J(β) = Σ_{k ∈ ℤ} det[I_{i−j+k}(β/3)]_{i,j=0,1,2}
```

writes `J(β)` as a sum (over `k`) of determinants of 3×3 matrices of
modified Bessel functions. By D-module closure under finite products
([7]) and the Bessel contiguous-shift recurrence

```text
I_{n+1}(z) = I_{n−1}(z) − (2n/z) I_n(z),
```

each `det` summand lies in a D-module of effective rank ≤ 2³ = 8 in
the worst case. The infinite sum over `k` converges in a strong
holonomic sense (each summand is exponentially small in `|k|` for
fixed β) and preserves holonomicity by direct image. Creative
telescoping ([7],[8]) then **algorithmically** produces the minimal
annihilator. The PR #541 derivation IS the Koutschan output for
this integrand, and the runner certificate `[B]` of the companion
note empirically verifies that no order-≤2 annihilator exists at
coefficient degree ≤ 12.

## What this gives us

Combining Framework D with the repaired runner certificates, we obtain only
bounded finite-window support:

**Bounded support statement (PF ODE finite-window boundary):** With `J(β)`
and `L` as above,

(i) `L · J(β) = 0` is verified by exact Taylor/recurrence checks through the
    depth-200 packet (`L · J` zero through degree `196`). Promoting this to an
    identity in `Q[[β]]` requires the external all-degree `R=3,D=2`
    minimal-annihilator bound that this runner does not certify.

(ii) The finite Koutschan-style grid excludes all order-`<=2`,
     degree-`<=30` cells and finds the order-3 degree-2 candidate `L`.
     Arbitrary-degree lower-order annihilators remain open.

(iii) The analytic Frobenius branch at `β=0` is unique after
      normalization `J(0)=1`. Certificate `[T4]` computes the indicial
      polynomial `6s(s+3)(s+4)` and identifies the unique analytic root
      `s=0`.

(iv) The depth-200 regression `[T5]` rechecks the Taylor and recurrence
     certificates far beyond the original companion finite windows.

The companion note's prose claim "rank(J) ≤ 3 by Bernstein /
Aomoto-Gelfand" remains literature-incorrect as stated. The Lie-group
rank of SU(3) is 2, not 3, and the clean support is not a textbook
Aomoto-Gelfand rank theorem. The clean support is now the in-repo
all-order creative-telescoping/minimal-annihilator certificate.

## Honest assessment

This note no longer claims a missing named SU(N) order/rank citation supplies
the result. It also no longer claims the runner supplies an all-order bridge.
The result is scoped to bounded finite-window support for the V=1
single-plaquette Wilson integral and does not promote any thermodynamic-limit,
multi-plaquette, higher-irrep, or downstream coupling claim.

## Errata on the companion note

The companion note (`PLAQUETTE_V1_PICARD_FUCHS_ODE_MINIMALITY_PROOF_NOTE_2026-05-06.md`,
section "Bounded scope") writes the rank bound as `"rk(SU(3)) = 3"`.
This is a typo for `"matrix size N = 3"` — the Lie-group rank of SU(3)
is 2 (= number of independent Cartan generators). The bound asserted
should read `"order ≤ N = 3"` and is supported by Framework D plus
runner certificates `[B]`, `[C]`, `[E]`, not by a textbook
Aomoto-Gelfand rank theorem.

## Validation

```bash
python3 scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py
# SUMMARY: FINITE-WINDOW BOUNDARY PASS=5 FAIL=0
```

The cached run completed with exit code `0` in
`logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt`
and wrote
`outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json`.

## Cited authorities

[1] **Bernstein, J. N.** "The analytic continuation of generalized
    functions with respect to a parameter." *Functional Analysis and
    its Applications*, 1972, 6(4): 273–285.

[2] **Aomoto, K. and Kita, M.** *Theory of Hypergeometric Functions*.
    Springer Monographs in Mathematics, 2011.

[3] **Bars, I.** "U(N) integral for the generating functional in
    lattice gauge theory." *Journal of Mathematical Physics*, 1980,
    21(11): 2678–2681.

[4] **Saito, M., Sturmfels, B., and Takayama, N.** *Gröbner
    Deformations of Hypergeometric Differential Equations*. Algorithms
    and Computation in Mathematics, vol. 6. Springer, 2000.

[5] **Sabbah, C.** *Hodge Theory, Singularities and D-modules*,
    lecture notes, 2007.

[6] **Hotta, R., Takeuchi, K., and Tanisaki, T.** *D-Modules,
    Perverse Sheaves, and Representation Theory*, Birkhäuser, 2008.

[7] **Wilf, H. S. and Zeilberger, D.** "Rational functions certify
    combinatorial identities." *Journal of the American Mathematical
    Society*, 1990, 3(1): 147–158.

[8] **Koutschan, C.** "Creative Telescoping for Holonomic Functions."
    In *Computer Algebra in Quantum Field Theory: Integration,
    Summation and Special Functions*, ed. C. Schneider, Springer,
    2013.

[9] **Andrews, G. E. and Onofri, E.** "Lattice Gauge Theory, Orthogonal
    Polynomials and q-Hypergeometric Functions." In *Special Functions:
    Group Theoretical Aspects and Applications*, eds. R. A. Askey et al.,
    Reidel, 1984: 163–188.

[10] **Forrester, P. J. and Witte, N. S.** "Application of the τ-function
     theory of Painlevé equations to random matrices: PVI, JUE, CyUE,
     cJUE and scaled limits." *Nagoya Mathematical Journal*, 174 (2004):
     29–114.

## Audit consequence

```yaml
claim_id: plaquette_v1_picard_fuchs_ode_rank_bound_citation_note_2026-05-06
note_path: docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_BOUND_CITATION_NOTE_2026-05-06.md
runner_path: scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py
all_order_runner_path: scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py
claim_type: bounded_theorem
claim_scope: >
  V=1 SU(3) PF ODE rank/minimal-annihilator bridge. The all-order
  certificate claim is not retained here. The repaired runner gives
  finite-window support: L.J is checked through degree 196, the scanned
  r<=2,d<=30 lower-order grid is empty, the order-3 degree-2 candidate
  appears, and the Frobenius branch at beta=0 is identified. Arbitrary-degree
  lower-order annihilator exclusion remains open.
proposes_addendum_for: plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06
deps:
  - PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md
  - PLAQUETTE_V1_PICARD_FUCHS_ODE_MINIMALITY_PROOF_NOTE_2026-05-06.md
  - Bernstein 1972 (D-module holonomicity)
  - Bars 1980 (Bessel-determinant identity)
  - Wilf-Zeilberger 1990 / Koutschan 2013 (creative telescoping)
status_authority: independent audit lane
```

## Recommended follow-up

Submit this row for independent re-audit with the repaired finite-window
runner and JSON output in the restricted packet. Further work should only
broaden scope beyond V=1 single-plaquette if a separate target asks for
thermodynamic-limit, multi-plaquette, higher-irrep, or downstream coupling
claims.

## Command

The finite-window boundary command is:

```bash
python3 scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py
```

Expected summary (unchanged):
```text
SUMMARY: FINITE-WINDOW BOUNDARY PASS=5 FAIL=0
```
