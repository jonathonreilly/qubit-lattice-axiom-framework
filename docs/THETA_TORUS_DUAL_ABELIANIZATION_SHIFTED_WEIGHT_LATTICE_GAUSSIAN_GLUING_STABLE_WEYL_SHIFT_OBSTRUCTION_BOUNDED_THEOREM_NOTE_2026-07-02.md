# Torus-Dual Abelianization of SU(N) Class Weights: the Heat-Kernel Member Is an Exact Signed Gaussian on the Regular Rho-Shifted Weight Lattice, the Structure Is Gluing-Stable, the Block-1 Center Grading Is Its Coset Shadow — and a Continuous Weyl-Consistent Theta Shift-Slot on the Nonabelian Torus Dual Is Obstructed (Bounded Theorem)

**Date:** 2026-07-02
**Claim type:** bounded_theorem (exact finite constructions on witness weight
classes plus a scoped obstruction; not a terminal no-go, not a discharge of
the theta admission).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_torus_dual_abelianization_weight_lattice_gaussian_2026_07_02.py`](../scripts/theta_torus_dual_abelianization_weight_lattice_gaussian_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_torus_dual_abelianization_weight_lattice_gaussian_2026_07_02.txt`](../logs/runner-cache/theta_torus_dual_abelianization_weight_lattice_gaussian_2026_07_02.txt)

## Question

The theta campaign's block 3 (PR #4811, in-flight; companions PRs #4784 and
#4796) sharpened `W_theta_Q_context` to three named residuals, of which the
second is:

```text
(i-b) SU(3) abelianization: derive the torus-dual branch structure of the
      glued 4D SU(3) effective weight (center Z_3 projection provably
      insufficient).
```

Question answered here: does the SU(N) class-weight family carry an exact
abelianized (torus-dual) structure at the finite level — with which integer
lattice, which coefficients, what stability under gluing, and what theta
slot?

## Answer

Four exact finite results (runner-verified; SU(2) fully, SU(3) on an 841-mode
window):

1. **The abelianized dual exists exactly, on the regular ρ-shifted weight
   lattice.** For the heat-kernel member `K_t = sum_R d_R e^{-t C2(R)}
   chi_R`, the Weyl-denominator-dressed weight `Delta · K_t` — a genuine
   function on the maximal torus — has torus-Fourier support exactly on the
   **regular points of the ρ-shifted weight lattice**, with coefficients

   ```text
   coeff(mu) = (sign) · P(mu) · e^{-t |mu|^2}   (one overall normalization),
   ```

   where `P(mu)` is the Weyl dimension polynomial. For `SU(2)`:
   `c_n = A · n · e^{-t n^2/4}` on every nonzero integer `n`, `c_0 = 0`.
   For `SU(3)`: the window modes match the signed `d_R e^{-t C2}` orbit
   table parameter-free; the non-regular lines (`n1 = n2`, `n1 = 0`,
   `n2 = 0`) carry exactly zero; the table is anti-invariant under the
   **full** Weyl group action on the mode lattice (all six elements, signed).
   The integer flux data (i-b) asks for — a `Z^rank` lattice dual — is
   therefore present exactly at the class-weight level: `Z` for `SU(2)`,
   `Z^2` for `SU(3)`, minus the Weyl-singular set, modulo `W`.

2. **The position side is an exact branch/winding image sum.** By the
   full-lattice Poisson identity (machine-precision verified),

   ```text
   sum_(n in Z) n e^{-t n^2/4} e^{i n phi}
     = i sqrt(4 pi / t) sum_(k in Z) (2 (phi + 2 pi k)/t) e^{-(phi+2pik)^2/t},
   ```

   the `SU(2)` class weight is an image sum over the `2 pi k` winding of the
   torus variable — the same branch-summed structure that carried the
   integer in the abelian blocks, now derived inside the nonabelian class
   weight. (Rank-2 version for `SU(3)` follows from the same Poisson
   structure on the lattice Gaussian; only the `SU(2)` instance is
   runner-pinned here.)

3. **Gluing stability.** Two-dimensional gluing multiplies dual coefficients
   pointwise in `R` (block-2 mechanism): the lattice support therefore never
   grows, and the heat-kernel member is the **exact gluing fixed class**:
   `c_R(t1) c_R(t2)/d_R = c_R(t1+t2)` (semigroup, runner-exact). The Wilson
   member is not form-stable — at `beta = 6` its effective exponents give
   `tau_R / C2 = 0.3231, 0.3031, 0.2993` on the tested irreps (fresh Weyl
   quadrature inside the runner), not a constant — while remaining inside
   the same lattice-dual support class. Abelianized integer flux data are
   thus not a per-plaquette accident: they persist under multi-plaquette
   gluing for the whole positive family, exactly for the heat-kernel member.

4. **The theta shift-slot is obstructed on the nonabelian torus dual.** In
   the abelian template (PR #4796) theta acts as a continuous shift of the
   dual label. Here: the Weyl-fixed subspace of the Cartan is exactly zero
   for `su(2)` and `su(3)` (runner-exact linear algebra), and every tested
   nonzero lattice shift of the `SU(3)` dual table — including diagonal
   shifts — breaks full-Weyl anti-invariance. So **no continuous
   Weyl-consistent label-shift theta slot exists on the `SU(N)` torus
   dual**: the `U(1)`-template insertion does not lift. The theta content of
   the carrier must therefore enter not as a per-plaquette label shift but
   as the cross-plane pairing of the abelianized fluxes — exactly the shape
   block 3 derived on the closed-branch surface and named as residual
   (ii'). Two independent directions now converge on that shape.

**Also closed into a circle:** the block-1 center grading is recovered as
the **coset shadow** of the dual lattice. Restricting `SU(2)` to integer
spins (the center-even subalgebra) depopulates exactly one lattice coset;
the `SU(3)` dual support decomposes into the three triality cosets of the
weight lattice mod the root lattice, all populated. The fusion-level
obstruction of PR #4784 is not contradicted: `Delta · w` is Weyl
**anti**-invariant — not a class function — so the lattice dual lives
outside the class-function fusion algebra that the block-1 theorem
classifies; its fusion-visible shadow is precisely the `Z_N` grading.

## Source surface (named authorities)

1. **Record axiom** (approved axiom node `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)) — used
   only as background discipline here; no record-registration claim is made
   for any torus-dual object (see the identification checkpoint).

2. **Retained `SU(3)` character surface**
   ([`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md),
   ledger `effective_status = retained`): supplies the `SU(3)` Wilson weight
   and character basis used for the Wilson-member checks (dual support and
   the `tau_R/C2` form-instability witness at `beta = 6`).

3. **Tier-A theta registry text** (docs/audit/data/tier_a_admissions.json,
   gauge side): the residual is "localized to the multi-plaquette /
   large-gauge-winding account"; this note supplies the abelianized
   structure of that account at the class-weight level.

The heat-kernel member is defined inline by its positive coefficients
`d_R e^{-t C2(R)}` with the internal normalization `|mu|^2 = (2/3)(a^2 + ab
+ b^2)` for `mu = (a, b)` in fundamental-weight coordinates, `C2 = |mu|^2 -
|rho|^2` (all internal; no external comparator). All identities — Fourier
support, coefficient values, Poisson image sums, Weyl-group action, gluing
semigroup — are earned inline by the runner at machine precision on
degeneracy-free offset grids (exact mode extraction for band-limited
character sums). One overall normalization per dual table is fixed on a
single mode; every other mode is then parameter-free.

## Theorem 1 (exact lattice dual)

For the heat-kernel member on `SU(2)` (runner A1-A2) and `SU(3)` (C1-C5):

- `Delta · K_t` has torus-Fourier support exactly on the regular points of
  the ρ-shifted weight lattice: `SU(2)`: all nonzero `n`, with `c_0 = 0`;
  `SU(3)`: the orbit lattice of `mu = (p+1, q+1)` with the non-regular lines
  carrying zero.
- Coefficients are the signed dimension-polynomial Gaussian
  `P(mu) e^{-t |mu|^2}` — `SU(2)`: `A n e^{-t n^2/4}` verified on every
  `n in [1, 28]` after fixing `A` at `n = 1`; `SU(3)`: 841 window modes
  match the signed `d_R e^{-t C2}` table parameter-free.
- The table is anti-invariant under the full Weyl action on the mode lattice
  (`PRED(w m) = sgn(w) PRED(m)` for all six `w`), and the Wilson member has
  the same support-and-antisymmetry structure (`SU(2)` runner A3; its
  coefficients are Bessel-type, no closed form claimed).

## Theorem 2 (branch/winding image sum)

The `SU(2)` dual Gaussian equals its `2 pi`-shift image sum exactly (runner
B1, machine precision at all tested `(t, phi)`): the class weight is a
branch-summed function of the torus variable with integer winding index —
the nonabelian class weight natively carries the shift-sum structure that
the abelian blocks used, dressed by the Weyl denominator and the dimension
polynomial.

## Theorem 3 (gluing stability; heat kernel is the fixed class)

Under two-dimensional gluing (coefficientwise products `c_R c'_R / d_R`,
the block-2 mechanism):

- the lattice-dual support never grows (zero coefficients stay zero,
  runner D2);
- the heat-kernel member reproduces itself exactly with `t1 + t2` (runner
  D1) — the abelianized structure is gluing-form-invariant there;
- the Wilson member is not form-stable: `tau_R / C2` is not constant at
  `beta = 6` (runner D3, fresh quadrature; spread `~ 0.024` across the
  tested irreps), while staying in the same support class.

## Theorem 4 (Weyl-shift obstruction for the theta slot)

- The `W`-fixed subspace of the Cartan is exactly zero for `su(2)` and
  `su(3)` (runner E1-E2).
- Every tested nonzero lattice shift of the `SU(3)` dual table — including
  the diagonal shifts that preserve the single swap reflection — breaks
  anti-invariance under the full Weyl group (runner E3).

Hence there is no continuous Weyl-consistent shift of the nonabelian dual
label, i.e. no `U(1)`-template theta slot on the `SU(N)` torus dual. This is
the second, independent derivation that the carrier's theta content must be
the cross-plane pairing of abelianized fluxes (block 3's exact reduction),
not a per-plaquette label shift. It also coheres with the block-1
obstruction (no additive `Z` on the fusion algebra) and with the
registry-tracked absence of a local per-plaquette cross-plane slot.

## Corollary (wall state for W_theta_Q_context)

Residual (i-b) is refined, not discharged:

```text
(i-b) resolved at the class-weight level: the abelianized torus dual with
      Z^rank integer flux data EXISTS EXACTLY (regular shifted weight
      lattice; Gaussian for the heat-kernel member) and is gluing-stable.

(i-b') what remains: Weyl-frame consistency for glued-SURFACE flux sectors.
       The lattice labels are defined modulo W plaquette by plaquette; a
       sector assignment on a glued surface requires a W-consistent global
       frame (the abelian-projection question), which is not derived here.

(i-a) defect closure and (ii') the F u F-shaped insertion: unchanged from
      block 3, with (ii') now doubly motivated (shift-slot obstructed).
```

## Identification checkpoint (what objects these are)

The torus dual is a **reconstruction surface**: `Delta · w` is a
frame-dependent object (defined on the maximal torus, anti-invariant under
`W`), and the lattice labels `mu` are defined modulo the Weyl group. No
claim is made that a physical record registers `mu`, that the abelianized
fluxes are the physical theta `Q`, or that abelian dominance holds
physically. The class-visible (frame-independent) content is the `W`-orbit
data; the block-1 `Z_N` grading is exactly its fusion-visible shadow. The
headline is a theory of the class weight's abelianized dual and its exact
properties — not a registration claim.

## Relation to the RP-half no-go (route independence)

The retained no-go row
strong_cp_rp_half_cannot_forbid_cp_odd_imaginary_no_go_note_2026-05-16
forecloses only "the RP half-square identity alone cannot derive a
no-bare-theta-slot exclusion." No reflection-positivity identity appears
here, and the shift-slot obstruction of Theorem 4 is a Weyl-symmetry
statement about the torus dual, not a bare-theta-slot exclusion: it
relocates where theta can act (pairing, not label shift); it does not forbid
theta.

## What moves

| Prior state | After this note |
|---|---|
| (i-b) "derive the torus-dual branch structure" — named unknown | derived at the class-weight level: exact signed lattice Gaussian on the regular ρ-shifted weight lattice (HK member), same support class for Wilson |
| branch-summed structure = abelian-only template | the SU(2) class weight natively carries the winding image sum (Poisson-exact); rank-2 analogue structurally supplied by the lattice Gaussian |
| gluing fate of abelianized data unknown | support gluing-stable for the whole positive family; HK member exactly form-invariant (semigroup) |
| theta-slot shape on the nonabelian dual undetermined | continuous label-shift slot obstructed by Weyl symmetry (no fixed direction; shifted tables break full-W anti-invariance) — pairing shape (ii') confirmed independently |
| block-1 `Z_N` grading vs torus dual | unified: the grading is the coset shadow (weight mod root lattice) of the dual support; center-even restriction depopulates cosets exactly |

## What remains

```text
W_theta_Q_context (current decomposition):
  (i-a)  defect closure on the abelianized multi-plaquette dual (block 3);
  (i-b') Weyl-frame consistency for glued-surface flux sectors (the
         abelian-projection question, named here);
  (ii')  derive the F u F-shaped multi-plaquette insertion from the
         framework surface (block 3 supplies its exact sector reduction;
         this note obstructs the alternative shift-slot shape).

W_theta_bar_assembly: unchanged (in-flight PR #4768).
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- that the torus dual or its lattice labels are physically registered
  objects, or that abelian dominance holds;
- a derivation of (i-a), (i-b'), or (ii') — those are the live residuals;
- a closed form for Wilson-member dual coefficients, or any universality /
  scaling-limit statement about the gluing flow beyond the exact semigroup
  and support facts stated;
- rank-2 runner verification of the position-side image sum (the `SU(3)`
  statement rests on the verified lattice Gaussian; only `SU(2)` is
  Poisson-pinned positionally);
- complete coverage of shift maps (the obstruction is verified for the
  listed lattice shifts and derived structurally from the zero fixed
  subspace for continuous shifts; nonlinear relabelings are out of scope);
- any new axiom, import, primitive, or admission (the heat-kernel member is
  defined inline by positive coefficients; all identities runner-earned).

## No-Go Discipline Gate (for the negative boundary)

**Status:** PASS as bounded scoping inside positive constructions. The
negative content is exactly: (a) no continuous Weyl-consistent label-shift
theta slot exists on the `SU(N)` torus dual (zero fixed subspace; shifted
tables break full-W anti-invariance); (b) the Wilson member is not
gluing-form-stable (its `tau_R/C2` is not constant), scoped to the tested
irreps and `beta = 6`.

### N1 — Alternative-route enumeration

| Route to the carrier's theta structure | Standing here |
|---|---|
| per-plaquette label-shift slot on the nonabelian torus dual | OBSTRUCTED (Theorem 4): no W-fixed direction; shifts break anti-invariance |
| cross-plane pairing of abelianized fluxes | SUPPORTED: block 3's exact reduction + this note's flux data; derivation of the insertion itself = (ii'), open |
| center `Z_N` projection as carrier | EXCLUDED for the integer pairing (block 3); here seen as the coset shadow only |
| class-function fusion grading | EXCLUDED (block 1); the lattice dual lives outside the fusion algebra (anti-invariant sector) |
| W-frame (abelian-projection) construction on glued surfaces | OPEN — named residual (i-b') |
| defect closure | OPEN — residual (i-a), unchanged |
| scaling-limit sector functional | OPEN — unchanged live path |
| operational primitive registration | OWNER-GOVERNANCE ROUTE, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

Nothing here binds the mass side or `W_theta_bar_assembly`. The shift-slot
obstruction (a) is scoped to continuous Weyl-consistent shifts and tested
lattice shifts of the dual table; it does not assert that theta cannot act
on the carrier (block 3 exhibits how it does act). The Wilson statement (b)
is a form-stability witness, not a defect of the Wilson surface: support
stability holds for it.

### N3 — Hidden-wall scan

"Regular shifted weight lattice" is verified, not assumed (zero on
non-regular lines). "One normalization, many modes" is the explicit checking
structure — no fitted parameters beyond a single scale per table. The full
Weyl action on the mode lattice is constructed explicitly (all six signed
elements) after an earlier single-reflection check was found insufficient
during development — the runner tests the full group. The internal `C2`
normalization is declared inline; no textbook value is consumed.

### N4 — Residual matching

Block 3's (i-b) named exactly this derivation target; this note supplies the
class-weight-level structure and returns the sharpened frame-consistency
residual (i-b'). The Tier-A registry's multi-plaquette localization is
respected: the gluing-stability theorem is what carries the per-plaquette
structure onto multi-plaquette surfaces. Block 1's grading obstruction and
block 2's matching mechanism are both consumed consistently (coset shadow;
coefficientwise gluing).

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The obstruction is scoped
(continuous W-consistent shifts; tested lattice shifts); live paths are
named; (i-b) is refined into (i-b'), not declared done — the frame question
is stated as the surviving content.

### N6 — Partial-closure path scan

Live paths: derive (i-b') a W-consistent frame rule on glued surfaces (or
show sector data can be defined frame-freely from W-orbit invariants);
derive (i-a) defect closure; derive (ii') the pairing insertion; the
scaling-limit route; and the assembly-side work of PR #4768.

### N7 — Steelman

A hostile reviewer can press: (1) "The lattice Gaussian for heat kernels is
classical harmonic analysis." Correct — the deliverable is the exact finite
statement set in audit format, wired to the named wall decomposition
(support regularity, full-W antisymmetry, gluing stability, shift
obstruction), not a novelty claim. (2) "Modulo-W labels are not sector
labels; you have not produced fluxes on any surface." Agreed and stated —
that is precisely residual (i-b'); what is new is that everything except
the frame choice now exists exactly. (3) "The shift obstruction only rules
out one insertion shape." Correct — and that is its role: it eliminates the
per-plaquette alternative to the cross-plane pairing, converging with block
3 from an independent direction. All three objections are absorbed into
scope.

### N8 — Cross-cycle echo

The campaign's echo risks are tracked cumulatively: no
integer-from-character-grading (block 1), no label-existence-only claims
(block 2), no unrestricted-sum sectors and no center-dual integer charge
(block 3). This block adds: no per-plaquette shift-slot theta insertion on
the nonabelian dual, and no treatment of modulo-W lattice data as
frame-free sector labels. Future cycles citing this chain must supply
(i-a), (i-b'), and (ii') explicitly.

## Verification

Run:

```bash
python3 scripts/theta_torus_dual_abelianization_weight_lattice_gaussian_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=17 FAIL=0
```

Sections: A `SU(2)` dual (support, Gaussian coefficients, anti-invariance,
Wilson member, center-coset shadow); B position-side Poisson image identity;
C `SU(3)` dual (degeneracy-free grid, finiteness, 841-mode parameter-free
match, full-W anti-invariance, regular-line zeros, triality cosets);
D gluing (semigroup, support stability, Wilson `tau_R/C2` non-constancy by
fresh quadrature); E Weyl-shift obstruction (zero fixed subspace for
`su(2)`/`su(3)`; shifted tables break full-W anti-invariance).
