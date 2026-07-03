# Flavor — the Heisenberg-Weyl / Fourier symmetry axis does not force r=1/2

**Date:** 2026-06-02
**Type:** open_gate
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not set, predict, or edit any audit outcome.
**Primary runner:** [`scripts/flavor_hw_clifford_does_not_constrain_r_2026_06_02.py`](../scripts/flavor_hw_clifford_does_not_constrain_r_2026_06_02.py)
**Runner cache:** [`logs/runner-cache/flavor_hw_clifford_does_not_constrain_r_2026_06_02.txt`](../logs/runner-cache/flavor_hw_clifford_does_not_constrain_r_2026_06_02.txt)
**No-promotion statement:** This source note creates no promotion, no registry
edit, no audit verdict, and no downstream status change; status remains owned
by the independent audit lane.

## 2026-06-06 HW/Fourier scope repair

The 2026-06-06 repair narrows this row to the HW/Fourier facts directly
checked by the runner and removes unsupported Clifford-landmark, Wigner/PSD,
full-orbit, and readout-selection value claims from the load-bearing scope:

- pure-shift `H = aI + bX + b*X^2` is not Fourier-fixed at `r=1/2`;
- the true Fourier-self-dual clock-shift family is fixed for all `g`, so `r`
  remains a free dial;
- F-covariance of `G = aI + b(X+X^2) + c(Z+Z^2)` forces `b=c` while leaving
  the diagonal `a` free.
- trace and traceless Hilbert-Schmidt norms make the ratio invariant under
  unitary conjugation, but no HW/Fourier equation selects its value.

Any `r=1` landmark, Wigner/PSD/full-orbit statement, or readout-selection
claim is a separate open route, not a claim of this row.

## Question
The generation factor `ℂ³` carries the qutrit **Heisenberg–Weyl** group — shift `X = C` (the hopping,
coefficient `b`), clock `Z = diag(1,ω,ω²)`, Weyl relation `ZX = ωXZ`, and the Fourier transform `F`
(a Clifford element) with `FXF† = Z`. Since `r=1/2 ⟺ |b|/a = 1/√2` is the equal-superposition
magnitude, does an HW/Fourier **self-duality** or HW-covariance *force* `r=1/2` — a symmetry principle
rather than an imported measure?

## Result — no. The scoped symmetry axis adds no value-forcing principle.
1. **"Self-dual at 1/√2" is a magnitude coincidence, not a fixed point.** The pure-shift operator
   `H = aI + bX + b̄X²` is **not** an `F`-eigenoperator at `r=1/2`: `F` maps it onto the orthogonal
   *clock* line `aI + bZ + b̄Z²`, and `‖FHF† − H‖ = 2.449 ≠ 0`. `H` is `F`-fixed only at `b=0` (`r=0`).
   So `1/√2` satisfies no Fourier-eigen equation — the coincidence is purely verbal.
2. **The genuine F-self-dual family carries a free parameter.** The clock-augmented operator
   `K = aI + g(X + Z + X² + Z²)` is `F`-fixed for **all** `g` (verified at representative values), so
   `r = g²` is a **free dial**; `1/2` is an unmarked member. The determinant landmarks of this enlarged
   family, and Wigner/PSD landmarks, are not used as selection rules here.
3. **HW-covariance forces the off-diagonal balance `b=c`, not r.** For the self-dual clock-enriched
   operator `G = aI + b(X+X²) + c(Z+Z²)`, `F`-invariance forces only `b=c` (equal shift- and
   clock-weight), while leaving the **diagonal `a` completely free** (verified). So even granting clock
   content, `r = |b|²/a²` stays free — the forced quantity is an off-diagonal symmetry, never the
   on-site:hopping ratio.
4. **`r` is invariant under the tested unitary conjugations, but its value is unselected.** `Tr(H)/3`
   and the traceless Hilbert-Schmidt norm are separately conjugation-fixed, so the ratio is meaningful
   on this algebraic surface. The HW/Fourier equations still supply no relation fixing on-site weight
   to hopping weight.

## Consequence
The symmetry axis re-confirms, from an independent direction, that **`r=1/2` is not a
Heisenberg-Weyl/Fourier fixed point**. The clean new derived fact is the **`b=c` off-diagonal
F-covariance constraint** with `a` still free. This row does not claim that the framework-native value
is `r=1`, does not prove a discrete-Wigner/PSD/full-orbit landmark theorem, and does not close the
readout-selection problem.

## 2026-06-13 Downstream Boundary Alignment

The downstream occupancy-independence theorem
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
identifies the shared residual as the occupancy/slot-degree atom. This HW row
therefore contributes one route-local negative: the tested Fourier/HW equations
do not supply that atom. The runner now also checks the downstream facts that:

- the occupancy theorem is the bounded source that names the residual;
- Record declines weighting/occupancy supply;
- sector and orbit occupancy weights differ by the exact factor `2`; and
- the orientation sends sector occupancy to `r = 1` and orbit occupancy to
  `r = 1/2`.

No Clifford, Wigner, or HW equation is promoted to a selector here.

## Dependencies

- [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
  (downstream occupancy/slot-degree boundary; bounded-theorem source, not an
  audit verdict).
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (Record axiom boundary and scope reference).

## The next paths this opens (not closing)
- The `b=c` off-diagonal constraint is a clean derived fact worth testing against the CKM/quark
  sector (does equal shift=clock weight constrain mixing?).
- The genuinely untouched lever is the **readout class**: the signed-eigenvalue (Brannen) readout vs
  the singular-value (Yukawa) readout differ at `r=1/2`; whether a discrete-Wigner **sign** structure
  privileges the signed (comparator-compatible) readout that load-bears `Q=2/3` is unexamined.

## No-Go Discipline Gate

This gate is restricted to one route statement: the qutrit
Heisenberg-Weyl / Clifford symmetry axis tested here does not force the
Koide `r=1/2` value.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Pure-shift Fourier fixed point | Treat `|b|/a=1/sqrt2` as self-dual. | The operator is not Fourier-fixed at that value. |
| True Fourier self-dual family | Add clock terms and impose `F`-invariance. | The family is fixed for all `g`; `r` remains free. |
| Heisenberg-Weyl covariance | Force equal shift and clock weights. | It forces `b=c`, not the on-site/hopping ratio. |
| Clifford invariant ratio | Use invariance of trace and traceless norm. | The ratio is meaningful but unselected. |
| Positivity / Wigner landmarks | Use intrinsic Clifford landmarks. | Out of scope for this row; requires a separate theorem/runner. |
| Readout-sign route | Use the signed Brannen readout. | Open and independent of this symmetry-axis test. |

### N2 - Wall Independence

The collapsed residual is value selection. Off-diagonal symmetry and
on-site/hopping weighting are independent.

### N3 - Hidden-Wall Scan

"Self-dual" is used only for the explicit Fourier-conjugation equations in the
runner. No clock content or signed readout rule is smuggled in as an axiom.

### N4 - Residual Matching

The tested residual is `r=1/2` as a symmetry-fixed value. It is not a claim
about Koide readout class, scale, cross-sector matching, or `r=1` landmarks.

### N5 - Rhetoric Audit

The negative statement is route-local. It does not claim that every possible
symmetry or readout principle fails.

### N6 - Partial-Closure Path Scan

A future sign/readout theorem, block-count principle, or approved admission
could still select `r=1/2`. This note leaves those paths open.

### N7 - Steelman

A hostile reviewer can argue that the right symmetry object is not the
pure-shift operator but a larger clock-shift/readout package. The runner tests
one such self-dual family and finds `r` free, but broader packages remain open.

### N8 - Cross-Cycle Echo

This matches the broader flavor pattern: structural symmetries often make the
ratio well-defined without selecting the Koide value. The note adds the
Heisenberg-Weyl / Fourier instance of that split.

**Gate result:** pass for the narrow symmetry-axis boundary only.

## Provenance (verified 2026-06-02)
- Weyl relation and `FXF†=Z`; `‖FHF†−H‖>0` at r=1/2 (H not F-fixed); pure-shift F-fixed only at r=0;
  `K` F-fixed for all g (r free); `G` F-fixed iff `b=c` with `a` free; trace/traceless-HS ratio invariant
  under Fourier conjugation: verified directly by the runner.
  From the Heisenberg–Weyl symmetry-axis workflow (`wf_9d805980`).
- This note records that the tested HW/Clifford structure does not constrain
  `r` and re-confirms `r=1/2` as the unforced equal-block weight.
