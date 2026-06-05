# Koide det_C-vs-det_R Fork: the Gaussian / Berezin Mechanism, and What det_C Needs Beyond First-Order

**Date:** 2026-06-04
**Type:** mechanism + narrow no-go (a posit is surfaced)
**Scope:** READ-ONLY probe deliverable. Constructs the explicit second-order
(Gaussian, bosonic) and first-order (Berezin, Grassmann) actions for the
generation coefficient on `R[Z_3] = R (+) C`, computes each partition
function / mass-weight, verifies the claimed `det_R` vs `det_C` fork, and pins
exactly what the `det_C` step requires. This source note approves no axiom, no
import, and no audit verdict; it is a `/tmp` working artifact, not a `main`
landing.
**Runner:** `/tmp/berezin_detc_detr_fork_2026_06_04.py`
(venv `/private/tmp/cl3-review-venv/bin/python3`), **SCORECARD: PASS=38 FAIL=0**.

```yaml
actual_current_surface_status: mechanism-established; det_C-step requires an extra posit
target_claim_type: mechanism + no_go
trace_class: mechanism_plus_negative_route_pruning
reachability_to_target: establishes mechanism; prunes "first-order alone forces det_C"
conditional_surface_status: "IF a holomorphic polarization (complex structure J) is chosen, THEN first-order -> det_C -> r=1/2 -> Q=2/3"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Documents a mechanism + a single negative fact (det_C is not a consequence of first-order-ness alone). Approves no axiom, no import, no audit verdict."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

---

## 0. The lever (retained)

The charged-lepton Koide value reduces, by the retained pure-algebra identity
`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`
(ledger `effective_status = retained`), to a single real ratio. With the
Hermitian circulant generation operator

```text
H = a I + b C + bbar C^2,   C^3 = I,   lam_k = a + 2|b| cos(arg b + 2 pi k/3),
Q = (sum_k lam_k^2) / (sum_k lam_k)^2 = (1 + 2 r)/3,    r = |b|^2 / a^2.
```

So `r = 1/2 <=> Q = 2/3` (observed charged-lepton value) and `r = 1 <=> Q = 1`
(the framework's dimension/trace default). The ONE undetermined object is the
measure that fixes `r`: the **block-count** weighting `(1,1)` gives `r = 1/2`;
the **dimension / per-real-DOF** weighting `(1,2)` gives `r = 1`. The retained
`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`
(`retained_no_go`) and `ACTION_NORMALIZATION_NOTE.md` (`retained_no_go`)
both decline to rank these two weightings. This note asks whether a FIRST-ORDER
(Berezin/Grassmann) action for the generation coefficient `b` forces the
block-count `(1,1)` weighting natively. (Runner Section B verifies the lever:
`Q = (1+2r)/3` for 200 random `(a,b)`, `delta`-independent, plus the symbolic
`sum cos = 0`, `sum cos^2 = 3/2` reductions.)

## 1. `R[Z_3]`: real and complex Wedderburn decompositions

`Z_3 = <C | C^3 = I>` (the cyclic generator; `C` is the framework's `Z^3`
lattice shift restricted to a single generation triple). Its group algebra has
two Wedderburn forms (runner Section A, all checks PASS):

- **Complex:** `C[Z_3] ~= C (+) C (+) C`, three 1-dim complex irreps with
  characters `chi_k(C) = w^k`, `w = e^{2 pi i/3}`, `k = 0,1,2`. Central
  idempotents `e_k = (1/3) sum_j w^{-kj} C^j`, each `tr e_k = 1` (complex-dim
  `(1,1,1)`).
- **Real:** `R[Z_3] ~= R (+) C`. The trivial character `k=0` gives a REAL
  1-dim block `R` (projector `P_s = e_0`, **1 real DOF**). The conjugate pair
  `{w, wbar} = {e_1, e_2}` is NOT realizable over `R` separately; the two
  complex idempotents **fuse** into a single REAL 2-dim block `C` (projector
  `P_d = e_1 + e_2`, real, `tr = 2`, **2 real DOF**).

This is the whole asymmetry: **the singlet block is `R` (1 real DOF); the
doublet block is `C` (1 complex = 2 real DOF).** `det_R` counts real DOF and
sees `(1,2)`; a measure that counts the complex block once sees `(1,1)`.

The real form of the conjugate pair is a **complex structure** `J = -i(e_1 -
e_2)` on the doublet plane: `J` is real, `J^2 = -P_d`, and `det(J|doublet) =
+1` (an orientation-preserving rotation, runner A6-A8). This `J` is the object
that "reduces the doublet's 2 real DOF to 1 complex slot." It is exactly the
irreducible pin named by
`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md` (ledger
`effective_status = unaudited`; cited here for its **argument**, not as a
retained authority): the `(1,1)`-vs-`(1,2)` choice is whether the doublet's
real dimension 2 is reduced to one slot before readout, i.e. a continuous
`SO(2)/U(1)_b` quotient implemented by a complex structure `J` with `det = +1`.

## 2. Second-order (Gaussian, bosonic) action -> `det_R` -> `(1,2)` -> `r = 1`

Write the generation coefficient as a real vector `x in R[Z_3] = R^3` with a
quadratic (second-order) action `S_2 = (1/2) x^T G x`, `G` the `C_3`-invariant
weighting Gram. On the real carrier (runner Sections C, D):

```text
det_R( alpha P_s + beta P_d ) = alpha * beta^2          [ (1,2) ]
```

The doublet eigenvalue `beta` appears with **multiplicity 2** (real rank of
`P_d`). The bosonic partition function over the real doublet plane (action
`(g/2)(x_1^2 + x_2^2)`) is

```text
Z_B,real = int d^2 x exp(-(1/2) x^T G_2 x) = 2 pi / sqrt(det_R G_2) = 2 pi / g,
det_R(G_2) = g^2   =>   doublet log-weight = 2 log g   [ (1,2) ].
```

(Runner D1, D4 confirm `Z = 2 pi/g` symbolically and by direct 2D quadrature.)
The real Gaussian counts the doublet as **two real DOF**. Mapping through the
weight ratio (Section 5): `(1,2) -> r = 1 -> Q = 1`. **The second-order real
bosonic integral gives `det_R`, the dimension/per-real-DOF weighting, `r = 1`,
`Q = 1`.** This matches the framework's dimension/trace default (the memory's
"trace-type -> Q=1" family).

## 3. First-order (Berezin, Grassmann) action

A first-order action for the generation coefficient is `S_1 = psibar D psi`
(holomorphic) or `S_1 = (1/2) theta^T M theta` (Majorana/real), `psi, theta`
Grassmann. The two Berezin integrals are computed **from the anticommuting
algebra directly** (runner Sections E; signed-permutation sum and
perfect-matching sum, derived not asserted, checked at `n = 2,3,4`):

- **Holomorphic Berezin** (one complex Grassmann pair `(psi, psibar)` per
  complex mode):

  ```text
  int Dpsibar Dpsi exp(-psibar A psi) = det_C(A).
  ```

  A single complex doublet mode with eigenvalue `z` contributes
  `int dpsibar dpsi e^{-z psibar psi} = z` — **the eigenvalue ONCE**. The
  doublet `C` is ONE holomorphic mode, counted once: **block-count `(1,1)`**.

- **Majorana / real Berezin** (real Grassmann `theta_i`):

  ```text
  int Dtheta exp(-(1/2) theta^T M theta) = Pf(M),    Pf(M)^2 = det_R(M).
  ```

  The real doublet kinetic `M = [[0,p],[-p,0]]` gives `Pf = p`, and over the
  full real structure `Pf ~ sqrt(det_R)` — **real-DOF flavored, NOT `det_C`.**
  The SAME 2 real DOF that a holomorphic pairing reads as ONE complex mode are
  read by the Majorana action as 2 real Majoranas with a Pfaffian.

So **first-order-ness alone yields a determinant-or-Pfaffian, but whether it is
`det_C` (block-count, `(1,1)`, `r=1/2`, `Q=2/3`) or `Pf ~ det_R` (real-DOF,
`(1,2)`, `r=1`, `Q=1`) is NOT decided by first-order-ness.** It is decided by
whether the doublet's two real DOF are paired into one complex Grassmann mode —
i.e. by a chosen complex structure `J`.

## 4. The decision matrix: polarization, not statistics

Cross `{statistics} x {polarization}` (runner Sections D-G):

```text
                       real polarization              holomorphic polarization
  2nd-order boson  ->  det_R          (1,2) r=1 Q=1   |z|^2 per complex -> block (1,1) r=1/2 Q=2/3
  1st-order ferm   ->  Pf = sqrt det_R(1,2) r=1 Q=1   det_C            -> block (1,1) r=1/2 Q=2/3
```

Reading the **columns** is the result:

- The `det_C` / `(1,1)` / `r=1/2` / `Q=2/3` answer is exactly the
  **holomorphic column**, for BOTH boson and fermion (a holomorphic boson — the
  complex Gaussian `int d^2 z e^{-g|z|^2} = pi/g`, runner D2, D5 — already
  counts the doublet once and gives `r=1/2`).
- The `det_R` / `(1,2)` / `r=1` / `Q=1` answer is the **real column**, for BOTH
  statistics.

Reading the **rows**: the first-order (fermion) row contains BOTH `r`-values
(Majorana `r=1`, holomorphic `r=1/2`). Therefore:

> **The discriminating choice is the POLARIZATION (real vs holomorphic), NOT
> the statistics (boson vs fermion). First-order-ness is neither necessary nor
> sufficient for `det_C`; the holomorphic polarization is what gives the
> block-count `(1,1)` weighting, and it does so for the bosonic action too.**

## 5. The fork end to end: weights -> `r` -> `Q`

Encode each measure by the singlet:doublet weight ratio `rho = w_d / w_s` it
assigns in the quadratic free-energy on the operator span `{I, J-I}`. The
retained Frobenius surface gives `E_+ = 3 a^2` (singlet) and `E_perp = 6 |b|^2`
(doublet); the readout fixes `r = 1/(2 rho)` (runner Section F):

```text
block-count   rho = 1    ->  r = 1/2  ->  Q = 2/3     (doublet = 1 complex slot)
dimension     rho = 1/2  ->  r = 1    ->  Q = 1       (doublet weight split over 2 real DOF)
```

Each measure lands as derived (runner F3, all OK):

| measure | polarization | `rho` | `r` | `Q` |
|---|---|---|---|---|
| real Gaussian (2nd-order boson) | real | 1/2 | 1 | 1 |
| Majorana Berezin (1st-order, real Grassmann) | real | 1/2 | 1 | 1 |
| holomorphic Gaussian (2nd-order boson) | holomorphic | 1 | 1/2 | 2/3 |
| holomorphic Berezin (1st-order, holo Grassmann) | holomorphic | 1 | 1/2 | 2/3 |

This is the explicit, verified fork. **2nd-order real Gaussian -> `r = 1`;
1st-order holomorphic Berezin -> `r = 1/2` — but the second equality holds only
because the holomorphic pairing was chosen, and the same choice on the bosonic
side ALSO gives `r = 1/2`.**

## 6. The sharp sub-question, answered

**Q: Is the Berezin -> `det_C` step a genuine consequence of first-order-ness,
or does it require an extra holomorphic/complex-polarization choice?**

**A: It requires the extra choice. `det_C` is NOT a consequence of
first-order-ness alone.** Precisely:

- A first-order action WITH a chosen **holomorphic polarization** (complex
  structure `J`, `J^2 = -P_d`, `det(J|doublet) = +1`, pairing the 2 real
  doublet DOF into one complex Grassmann mode `(psi, psibar)`) gives `det_C` ->
  `(1,1)` -> `r = 1/2` -> `Q = 2/3`.
- A first-order action that is **Majorana / real** (no complex structure; real
  Grassmann modes) gives `Pf ~ sqrt(det_R)` -> `(1,2)` -> `r = 1` -> `Q = 1`.

The exact thing `det_C` needs **beyond first-order** is the **complex structure
`J` on the doublet plane** = the holomorphic polarization = the
`SO(2)/U(1)_b` doublet-frame reduction. Runner G5 confirms this `J` is
numerically identical to the Section-A doublet complex structure, and G6 shows
a real reflection (CPT / real-structure map, `det = -1`) satisfies
`kappa J kappa = -J`: the holomorphic pairing is **not invariant under, hence
not fixed by, the real structure**. Choosing it is a separate posit.

This is the **same pin** named by
`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md` (the
`SO(2)/U(1)_b` quotient / complex structure `J` with `det = +1`), reached now
from the action side. It is also the **same pattern** as the retained-adjacent
Majorana sector: the framework already distinguishes a determinant/Gaussian
surface from a Pfaffian/Grassmann pairing surface, and
`NEUTRINO_MAJORANA_PFAFFIAN_AXIOM_BOUNDARY_NOTE.md` records the Pfaffian sector
as **admitted, not forced** (ledger `unaudited`; cited for pattern, not
authority). The present note's verdict is the Koide-side analog: the
holomorphic/Berezin route to `det_C` is **constructible but not forced** — the
complex structure is an admitted extension, not a consequence of going
first-order.

## 7. Import flags

- **NO PDG values, NO fitted parameters, NO literature comparators consumed.**
  No `sqrt(m)` readout law, no `delta`, no `v_0`, no charged-lepton mass.
- **RETAINED used (load-bearing):** `KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC`
  (`Q = (1+2r)/3`), ledger `retained`. Pure representation theory of `R[Z_3]`
  (Wedderburn, idempotents) and elementary Gaussian/Berezin/Pfaffian integral
  identities are non-load-bearing calculation machinery.
- **POSIT (flagged, NOT derived):** the **holomorphic polarization / complex
  structure `J`** that turns the first-order action into `det_C`. It is the
  `SO(2)/U(1)_b` doublet-frame reduction. It is **not** on A1+A2+retained; it
  is not established by first-order-ness, by the real structure, by CPT, or by
  Hermiticity (all of which leave it free, per the block-count note's five
  tested mechanisms). Promoting it as background requires explicit user
  approval per `feedback_no_imports_without_user_approval`.
- **DEFAULT (no extra posit):** the Majorana / real first-order action and the
  real Gaussian both give `det_R`-flavored `(1,2)` -> `r=1` -> `Q=1`. This is
  the framework's dimension/trace default; the observed `Q=2/3` is NOT the
  default and remains gated on the complex-structure posit.
- **Cited-for-argument-only (NOT retained, flagged):**
  `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED` (`unaudited`),
  `CPT_EXACT_REAL_ANTI_HERMITIAN_D` (`unaudited`),
  `NEUTRINO_MAJORANA_PFAFFIAN_AXIOM_BOUNDARY` (`unaudited`). Used for their
  arguments/patterns, never as load-bearing retained authority.

## 8. No-go discipline gate (a posit is surfaced)

The negative content is: **`det_C` is not a consequence of first-order-ness
alone; it requires the holomorphic-polarization posit.** Template
`docs/CL3_CHIRAL_CUBE_WILSON_HOP_DOUBLING_FORECLOSED_NARROW_NO_GO_NOTE_2026-05-27.md`.

**N1 - Alternative route enumeration.** Four routes by which first-order-ness
might force `det_C` were checked: (1) holomorphic Berezin with `J` chosen —
gives `det_C` but ONLY because `J` is supplied (runner E1, E2, G1); (2)
Majorana/real first-order — gives `Pf ~ sqrt(det_R)`, NOT `det_C` (E3, E4, G3);
(3) the claim "fermion statistics alone fixes block-count" — falsified, since
the holomorphic BOSON also gives block-count `(1,1)` (D2, D3, G1), so the
distinction is polarization not statistics; (4) real structure / CPT fixing the
pairing — falsified, `kappa J kappa = -J`, the real structure leaves `J` free
(G6), consistent with the block-count note's five-mechanism survey.

**N2 - Wall-independence audit.** The collapsed wall set is one wall: the
complex structure `J` (holomorphic polarization / `SO(2)/U(1)_b` reduction) is
not supplied by going first-order. The four routes above are not independent
walls; they are alternative ways to try to source that one `J`. This is the
SAME wall the block-count note reaches from the operator side.

**N3 - Hidden-wall scan.** "Retained" inputs are explicitly named in Section 7;
the only retained load-bearing input is the algebraic `Q=(1+2r)/3`. The
holomorphic polarization is explicitly NOT imported or approved. Textbook
Wedderburn / Gaussian / Berezin / Pfaffian facts are non-load-bearing
calculation machinery, all re-derived in the runner.

**N4 - Residual matching.** `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS`
(`retained_no_go`) and `ACTION_NORMALIZATION` (`retained_no_go`) decline to
rank `(1,1)`/`(1,2)` — residual matches (this note adds WHICH action realizes
each). `KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED` (`unaudited`) names
the SAME `SO(2)/U(1)_b`/`J` pin — residual matches; used as same-pin corroboration
from a different surface, not as retained authority.
`NEUTRINO_MAJORANA_PFAFFIAN_AXIOM_BOUNDARY` (`unaudited`) supplies the
Gaussian-vs-Pfaffian "admitted not forced" PATTERN — residual matches at the
pattern level only.

**N5 - Rhetoric audit.** The verdict is scoped: it states only that the
particular `Berezin -> det_C` step needs a holomorphic polarization beyond
first-order-ness. It does NOT claim `Q=2/3` is unreachable, that the complex
structure is underivable, or that any future polarization-selecting principle
(a derivable `U(1)_b`, a readout-functional factorization, a separately
approved import) is foreclosed.

**N6 - Partial-closure path scan.** A polarization-selecting principle could
close the wall WITHOUT a new axiom — e.g. a derivation that the framework's
generation sector carries a native complex structure (a `J` already present in
A1+A2+retained), or a readout functional that factors through the `SO(2)`
quotient. This note leaves those paths open and does not assert a new axiom is
required.

**N7 - Steelman.** A hostile reviewer argues: "a first-order Dirac action is
inherently complex (it has `psi` and `psibar` as independent fields), so
first-order DOES carry a complex structure, hence `det_C` is automatic." Reply:
the independence of `psi, psibar` is the holomorphic polarization itself — it
IS the choice. The Majorana action `(1/2) theta^T M theta` is an equally valid
first-order action with `theta` real (`psibar = psi` up to charge conjugation),
and it gives `Pf ~ det_R`. Which first-order action (Dirac/holomorphic vs
Majorana/real) the generation coefficient takes is precisely the unfixed
posit; the steelman assumes the Dirac choice rather than deriving it. (This is
the same complex-vs-real first-order distinction as the Majorana sector's
`det` vs `Pf`.)

**N8 - Cross-cycle echo.** Prior cycles repeatedly converged on this `r=1/2`
pin from kinematic, dynamical, quantum, chiral, and records lenses (memory:
"five A1+A2-internal lenses all reduce to the single unforced `r=1/2`"). This
note adds the **action/measure lens** and lands on the SAME pin (`J` /
holomorphic polarization / `SO(2)/U(1)_b`), now sharpened to: the pin is a
**polarization choice**, not a statistics choice, and it sits identically on the
bosonic and fermionic sides.

## 9. Verdict

- **The fork HOLDS, exactly as a fork between POLARIZATIONS:** real polarization
  (real Gaussian OR Majorana Berezin) -> `det_R` / `Pf` -> `(1,2)` -> `r = 1` ->
  `Q = 1`; holomorphic polarization (holomorphic Gaussian OR holomorphic
  Berezin) -> `det_C` -> `(1,1)` -> `r = 1/2` -> `Q = 2/3`. All four corners
  verified (PASS=38).
- **What `det_C` needs beyond first-order:** a **holomorphic polarization** =
  the **complex structure `J`** on the doublet plane (`J^2 = -P_d`,
  `det(J|doublet) = +1`), equivalently the `SO(2)/U(1)_b` doublet-frame
  reduction. First-order-ness alone gives only a determinant-or-Pfaffian; the
  Majorana (no-extra-posit) first-order default gives `Pf ~ det_R` -> `Q = 1`.
- **Mechanism established; nativity NOT claimed** (that is the sibling probe).
  The `det_C` route is constructible but, on A1+A2+retained, the complex
  structure is an admitted extension, not forced.
- **The next path this opens:** whether the generation sector carries a NATIVE
  complex structure `J` derivable from A1+A2+retained (A1 = each site `= C^2 =`
  Cl(3,0) spinor already supplies an `i`; does its action descend to a
  `det(=+1)` complex structure on the `R[Z_3]` doublet, distinct from the
  `det=-1` CPT/real-structure reflections?), or whether the Koide readout
  functional factors through the `SO(2)/U(1)_b` quotient without `J` being an
  algebra symmetry. Both are sibling-probe questions; this note supplies the
  mechanism they would feed.

## 10. Validation

```bash
/private/tmp/cl3-review-venv/bin/python3 /tmp/berezin_detc_detr_fork_2026_06_04.py
# SCORECARD: PASS=38 FAIL=0
```

Sections: A (Wedderburn real/complex, complex structure `J`), B (retained
`Q=(1+2r)/3` lever, numeric + symbolic), C (`det_R = alpha beta^2` vs
block-count `alpha beta`), D (real vs holomorphic Gaussian, symbolic + 2D
quadrature), E (Berezin `det_C` and Majorana `Pf` DERIVED from the Grassmann
algebra at `n=2,3,4`), F (weights -> `r` -> `Q` for all four measures), G (the
polarization-not-statistics decision matrix and the verdict; `J` identified
with Section A's `J`; `kappa J kappa = -J`), H (import-flag self-audit).
