# Lane consolidation memo — July K-CPT Dirac commutant/census era (D-kcpt)

Destination at GO: `archive/chains/july-kcpt-dirac-era.md`.
Scope: 21 docs/ claim notes (2026-07-17 → 07-25) — the KCPT lane's
operator-algebra program on the periodic staggered qubit lattice: the
L = 4 (N = 64) Dirac operator D2, its complex structure J_full, the
lattice-parity involution S_eps, the extended symmetry group
H = ⟨G_amb, S_eps⟩, and the L = 6 surface-change comparison. All 21
personally read in full (2026-09-04). Ruling: **all 21 ARCHIVE**, released
to the archive tier behind this memo; each note remains the primary claim
surface of its own result (runners, caches, ledger shards never move — G8).

## The era's question and answer

**Question:** what symmetry structure does the staggered lattice Dirac
operator actually carry, and which parts of it are geometry (surface-
dependent bookkeeping) versus candidate physics (surface-stable structure)?

**Answer (as of the era's close):** The full classification exists at L = 4
and the dichotomy is proved at L = 6. Surface-dependent: the ambient
module (End_H 6 → 19, gaining multiplicity-2 constituents and going
non-abelian), the ambient algebra 𝒜 = ⟨D2, J_full, ρ(H)⟩ (dim 992 → 4224),
the separator complement (1 → 9), and the reach-census value set
({0, 1/9, 1/3, 1} at L = 4 vs {0, 1/4, 4/15, 1/3, 1/2, 1} at L = 6, 1/9
absent). Surface-stable: the natural core 𝒜_nat = ⟨D2, J_full, S_eps⟩ ≅
M₂(C)^⊕4 with center C[M], numerically blind to the entire separator space
at both L (overlap² ≲ 1e-30 against a wrong-value control that pulls it to
1). Every note is a bounded theorem with explicit claim-boundary language:
"CP"/"chiral" are geometric labels for S_eps and the split real-12; no
physical CP, chirality, measurement, readout, or Record identification is
asserted anywhere in the lane.

## Arc

**Stage-setting (07-17 → 07-19; 4 notes).** The Berezin count-binary
measure collapse — with its exact theorem content: under the pinned
measure the quadratic Berezin integral is exactly det M (reversed
ordering: (−1)ⁿ det M); horn m uses 6m generators; every active constant
homogeneous odd-linear substitution at fixed count/held measure
multiplies the zero-source output by det S, while the explicitly computed
coupling-dependent substitution A(W) = W converts det₃ to det₃² — the
note that names the FRONT AC occupancy-grain obligation, quotes its live
closure criterion (derive the physical matter action and measure, then
distinguish det_C from |det_C|²) — while itself making NO discharge,
narrowing, or reframing of that obligation (the note's own item 5): its
collapse statement concerns the probe surface's constant-substitution
parameter freedom, its det/reversed-order identities are runner-verified
at n = 1, 2, 3, its substitution class is active constant homogeneous
LINEAR odd-generator substitutions with ordinary central Grassmann-even
scalar coefficients at fixed generator count and held integration
order/normalization, and "horn m uses 6m generators" is a declared
bookkeeping reading; the two corner-carrier notes (four antilinear readout
faces classified; the w ↔ w̄ presentation swap shown to be a proper-rotation
frame choice with K-parity = rotation parity on the Hermitian section
only); and the bulk holomorphic split 28 ⊕ 28 ⊕ 8 with the orientation
involution K exchanging the halves and spectrum ±2i√m.

**The extended group and its module (07-20 → 07-21; 8 notes).** The
holomorphic G_amb representation (32 = 4+4+6+6+12); the CP-completion
C⁶⁴ = 8 ⊕ 8 ⊕ 12 ⊕ 12 ⊕ 12⁺ ⊕ 12⁻ under H (order 1536); the two
Frobenius–Schur censuses (holomorphic (0,0,0,0,+1) with S_eps the
geometric conjugation; extended all +1); the radius grading
P = D2·J_full = −√(−M); the symplectic-leg χ_sgn-covariance
(hᵀωh = χ_sgn(h)·ω) with the pairing census sorting the six constituents
into four self-paired induced blocks plus the isotropic chiral pair
12⁺ ↔ 12⁻ cross-paired at rank 12; the even-algebra reach floor (exactly
C[M]; the two missing directions are character-level Frobenius projectors
of DIFFERENT kinds — one separates the CP-split pair {12⁺,12⁻} on shell
−4, the other separates the two induced-12 constituents on shell −8; only
the first is a CP charge);
and the five-module fusion theorem (Z(𝒜) = C⁵; only the chiral pair fuses;
C[M] ⊊ Z(𝒜) ⊊ End_H at 4 ⊊ 5 ⊊ 6).

**The full algebra (07-24; 2 notes).** The Dirac sign character s = χ_sgn
derived from the D2 conjugation census with the Schur-forced fused-block
superstructure; and the bicommutant theorem
𝒜 = M₈ ⊕ M₈ ⊕ M₁₂ ⊕ M₁₂ ⊕ M₂₄, dim 992, commutative tower 4 ⊊ 7 ⊊ 8 ⊊ 992.

**The commutant of D2 itself (07-25; 4 notes).** The graded
signed-permutation enumeration (|Comm| = 96N); the closed-form translation
lifts ζ_ν with lattice-size independence verified L ∈ {4,6,8,10}; the
abstract identification as a non-split central double cover of T⋊B₃ with
End_Comm = C[D2] dim 7 L-stable; and the extension localization (the point-group side splits and the
translation side is non-split FOR THE TESTED FAMILY {B₃, O, A₄, D₃, T,
T_even, T_even⋊A₄} — not blanket: the cyclic translation subgroup ⟨e_x⟩
SPLITS, its lift of order L giving a −I-free section, and the primary
says non-splitness does not propagate down to every translation
subgroup; β(s,t) = (−1)^((Σs)(Σt)−s·t) is the unique nontrivial
B₃-invariant alternating bimultiplicative COMMUTATOR FORM on T/2T among
the 512 bilinear forms — not a full H² extension-class classification;
q toggles with the parity of (L/2)²).

**The surface comparison (07-25; 3 notes).** The L = 4 quantized reach
census (ω ∈ {0, 1/9, 1/3, 1} over all 768 extensions of 𝒜_nat); the L = 6
reach census (six values, 1/9 absent, translation dial sweeps ω); and the
capstone surface-change/natural-algebra-invariance theorem (PASS=34,
two-seed resolved throughout).

## Deltas this memo carries

- The dichotomy itself — ambient structure (module, algebra dimension,
  separator space, reach labels) is surface-dependent; the natural core
  𝒜_nat ≅ M₂(C)^⊕4 with Z(𝒜_nat) = C[M] is not, and is blind to every
  separator direction at both surfaces.
- The exact objects: |G_amb| = 768/2592, |H| = 1536/5184 (L = 4/6);
  the six-constituent decomposition and both FS censuses; dim 𝒜 = 992
  (= 8²+8²+12²+12²+24²) vs 4224 (13 idempotents, ranks
  [8,8,8,12,12,12,12,24,24,24,24,24,24]); commutative tower 4 ⊊ 5 ⊊ 6
  (C[M] ⊊ Z(𝒜) ⊊ End_H).
- The D2 commutant package: |Comm| = 96N exactly for the exhaustively
  enumerated L ∈ {4, 6, 8, 10} (at L = 12 only |Comm| ≥ 96N = 165,888 is
  proven — equality NOT established; the general even-L results cover the
  translation lifts, commutator, and q formulas), the closed-form lifts,
  the non-split central double cover of T⋊B₃ for the tested subgroup
  family (⟨e_x⟩ splits), β as the unique B₃-invariant alternating
  bimultiplicative commutator form on T/2T (not a full H² class), the
  (L/2)² parity toggle, End_Comm dim 7 stable.
- The symplectic sorting: ω = −J_full sign-covariant under χ_sgn; the
  chiral backbone 12⁺ ↔ 12⁻ canonically and nondegenerately paired while
  each half is ω-isotropic; rank accounting 40 + 24 = 64.
- The reach quantization and its surface-dependence: {0, 1/9, 1/3, 1} at
  L = 4 vs {0, 1/4, 4/15, 1/3, 1/2, 1} at L = 6 — plus the census's
  surface-change structure: the L = 4 set equality {Δχ ≠ 0} = {ω = 1/3}
  FAILS at L = 6, becoming a proper containment (witness: a size-12 orbit
  with ω = 1/3 and Δχ = 0), and the maximal-reach unlock retains
  sep = e_a − e_b while its closure grows from dimension/center 28/7 to
  68/17 with rank-8 minimal idempotents.
- The era's named open paths (recorded, not pursued): the L = 6 reach
  census on the nine-dimensional separator space; classification of the
  multiplicity-2 constituents; the GENERAL-L scaling law and full reach
  census over Comm∖H for the signed-permutation commutant (the
  finite-surface characterization itself is DELIVERED exhaustively at
  L = 4 and 6 — |Comm| = 6144/20736, the Z₂-graded GC of order 2|Comm|,
  H and ⟨H, g_r4⟩ located within it; the dressed r4 rotation sits outside
  H at both L); the liftability obstruction.

## Why this is safe

Nothing is deleted or demoted; every note keeps its runner, cache, and
ledger shard in place with citations resolvable per the archive design.
The lane is NEARLY self-contained: the corner-carrier
two-presentation-swap note names two non-KCPT load-bearing dependencies
on its own surface — MINIMAL_AXIOMS_2026-06-29.md (proper cubic rotation
group, admissibility covariance) and the staggered-Dirac realization gate
note (the operator surface) — both FRONT-resolvable. The rows carry the
notes' explicit geometric-label firewalls (attack-pass verified
2026-09-04; gaps repaired in the MEMO-FIX batch), so the archive never
reads "CP"/"chiral" as Standard-Model claims. The era's open paths are
recorded in the notes and summarized here. One FRONT connection stands:
the Berezin count-binary note names the standing FRONT AC
occupancy-grain obligation, quotes its closure criterion, and supplies
finite-surface controls relevant to it — while expressly making no
discharge, narrowing, or reframing of it (its result and surviving
routes are carried above and on its corrected row), so that active
obligation does not need to rediscover the archived primary.
