# Axiom-First Reflection Positivity: Single-Step Spin-Basis No-Go (Staggered-Only)

**Date:** 2026-04-29 (original); 2026-05-26 (staggered-only narrowing);
2026-05-27 (single-step spin-basis no-go acknowledgment + 2-step
narrowing); 2026-05-28 (retyped to no_go per audit verdict; 2-step
positivity demoted to non-load-bearing literature context).
**Type:** no_go
**Loop:** `axiom-first-foundations`
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (retype to no_go)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The primary runner closes the narrow single-step counterexample,
> and the retained one-hop dependencies close determinant positivity
> plus an abstract norm-square lemma. They do not construct the 2-step
> blocked staggered-KS transfer matrix or prove its positivity from
> the repo packet."*

Repair instruction: *"create or wire an audit-clean 2-step blocked
staggered-KS transfer-matrix theorem that derives positivity of
T_hat^2 = S_hat^2 ... keep the single-step no-go as a separate bounded
negative witness."*

Deriving the 2-step blocked positivity in-repo is substantive new work
(the STW 1981 / Palumbo 2002 construction is a real research target,
not a one-line wiring) and is out of scope for a review-loop PR. This
repair takes the auditor's offered alternative — **keep the single-step
no-go as the load-bearing negative witness** — and retypes the row
accordingly:

- `claim_type`: `bounded_theorem` -> `no_go`. The load-bearing content
  of this row is the **proven negative result** that direct single-step
  spin-basis Lagrangian RP for staggered KS under Sharatchandra Theta
  alone is non-PSD (runner-verified, free U=1 min eigenvalue -0.80).
- The **2-step `T_hat^2` positivity is demoted to non-load-bearing
  literature context** (STW 1981 / Palumbo 2002 / Smit §6 /
  Caracciolo-Palumbo 2013). This note does **not** derive it; it is
  recorded only as the standard published resolution surface. A future
  PR that constructs the 2-step positivity in-repo can re-promote a
  positive companion row.

### Convention note (settled 2026-05-28)

A 2026-05-27 attempt (PR #2084) tried to retract this no-go by claiming
the Berezin contraction convention was wrong. That retraction was
**itself incorrect** and was rejected by review-loop. The settled
convention, verified from a first-principles brute-force Berezin
integral (measure normalization cancels in the ratio): for
`S = bar(chi) M chi` with `exp(-S)`,

```text
<chi_b bar(chi)_a>  =  (M^{-1})[b, a],
<bar(chi)_a chi_b>  =  -(M^{-1})[b, a].
```

The on-main no-go runner uses this correct convention and reproduces
the non-PSD Gram. The single-step no-go is genuine, not a convention
artifact.
**Primary runner:** [`scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py`](../scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py)
(no-go demonstration: single-step Lagrangian RP for staggered KS in
spin basis is verifiably non-PSD; this is the load-bearing exhibit for
the 2026-05-27 narrowing).
**Cached runner output:** [`logs/runner-cache/axiom_first_rp_spin_basis_single_step_psd_failure.txt`](../logs/runner-cache/axiom_first_rp_spin_basis_single_step_psd_failure.txt)
**Secondary runner:** [`scripts/axiom_first_reflection_positivity_check.py`](../scripts/axiom_first_reflection_positivity_check.py)
(Hamiltonian-level positivity exhibits E1-E6; these are structural
finite-block checks for a chosen `H_lat`, not Lagrangian RP exhibits).

## 2026-05-27 Audit Repair

The prior version of this note claimed a single-step Lagrangian
reflection-positivity theorem for staggered Kogut-Susskind fermions in
the spin basis under the Sharatchandra link-reflection convention. An
independent verification (the load-bearing no-go runner above) shows
that this claim cannot be derived in that surface:

- The Gram matrix `G_{IJ} = <Theta(F_I) . F_J>_S` constructed directly
  from the Berezin path integral with propagator `M[U]^{-1}` is **not
  PSD even in the free U=1 case**. Diagonal entries for the simplest
  degree-1 monomials `chi_x` and `bar(chi)_x` at positive-time sites
  come out at `-0.4`, and the minimum eigenvalue is `-0.80`. Across 5
  random U(1) gauge configurations PSD fails in 5/5 cases.
- This matches the published literature's warning that the standard
  constructive route in the spin basis is not a direct positive
  one-lattice-spacing transfer matrix. Caracciolo-Palumbo, Phys. Rev.
  D 87 (2013) 014507 (arXiv:1210.1786), report failed attempts at a
  positive single-spacing transfer matrix and then construct the
  spin-basis result through block variables.
- The standard recipe in the lattice literature avoids this no-go by
  working with a **2-step blocked** transfer matrix `T_hat^2 = S_hat^2`
  over two lattice spacings, either in the flavour basis (Palumbo,
  Phys. Rev. D 66 (2002) 077503 = hep-lat/0208005) or via the
  Sharatchandra-Thun-Weisz spin-diagonal construction (Nucl. Phys. B
  192 (1981) 205). Smit's *Introduction to QFT on a Lattice*, §6,
  documents this as the standard treatment.

This 2026-05-27 revision took a "2-step narrowing" framing in which the
2-step positivity was treated as the load-bearing positive claim. The
**2026-05-28 retype above supersedes that framing**: the load-bearing
content of this row is now the single-step no_go (runner-verified), and
the 2-step positivity is non-load-bearing literature context (the
audit verdict correctly flagged that the 2-step positivity was claimed
but not derived in-repo). The bullets below are kept for provenance but
read under the 2026-05-28 retype:

- the load-bearing claim is the **single-step no_go** (Gram non-PSD),
  not the 2-step positivity;
- the direct single-step spin-basis Lagrangian RP surface under
  Sharatchandra Theta alone is the proven negative result per the
  cached runner;
- the 2-step blocked positivity is literature context (STW 1981 /
  Palumbo 2002 / Smit), not derived here, not load-bearing;
- Hamiltonian-level positivity exhibits in the secondary runner are
  kept as structural finite-block consistency checks, not as a
  proof of any Lagrangian RP claim.

The Wilson-fermion subsurface remains out of scope per the 2026-05-26
narrowing. This note continues to address only the staggered-only
fermion sector.

This source note does not set or predict an audit outcome; later
status is generated by the audit pipeline after independent review.

## Scope

In scope (load-bearing — the no_go):

- finite lattice blocks with the parent temporal-link reflection map
  `theta(t, x_vec) = (-1 - t, x_vec)`;
- compact `SU(3)` Wilson plaquette gauge links with Haar measure;
- Kogut-Susskind staggered fermions with positive real mass
  `M = M_KS + m I`, `m > 0`;
- the **negative result** that the direct single-step spin-basis
  Lagrangian RP Gram matrix on this surface is non-PSD (runner-verified);
- polynomial observables supported in the positive-time half (the
  Gram-matrix test surface).

Literature context (NOT load-bearing on this row):

- the **2-step blocked transfer matrix** `T_hat^2` positivity as in
  Palumbo 2002 / Sharatchandra-Thun-Weisz 1981 / Smit — cited as the
  published resolution surface, not derived in this repo.

Out of scope (removed from this row's claim surface):

- a **positive** single-step spin-basis Lagrangian RP theorem for
  staggered KS under Sharatchandra Theta alone (this row proves the
  opposite — the no_go);
- Wilson-fermion operators `M_KS + M_W + m I`;
- symmetric-canonical Wilson determinant bridges;
- configuration-by-configuration Wilson-fermion determinant positivity;
- continuum OS reconstruction in the Wightman sense;
- any publication or ledger status promotion.

## Dependencies

The narrowed proof uses two local authorities plus the new no-go
runner:

- [STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  proves the configuration-by-configuration determinant positivity
  `det(M_KS + m I) > 0` for `m > 0`. This input is necessary for the
  positive U-weighted measure but is not by itself sufficient for the
  Lagrangian Gram-matrix positivity (per the load-bearing no-go
  runner above).
- [REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies an abstract finite Cauchy-Schwarz norm-square identity
  under explicit symmetry hypotheses. That note explicitly disclaims
  the Wilson-plaquette boundary application; this row therefore cites
  it only for the abstract identity, not for a Wilson-plaquette
  boundary closure.

Both are cited only for their stated narrow surfaces. This note does
not import any fitted value, observed target value, literature
numerical comparator, same-surface family selector, or admitted unit
convention.

## Load-bearing statement (no_go)

On the staggered-only action surface

```text
    S = S_G[U] + bar(chi) (M_KS[U] + m I) chi,        m > 0,
```

with the temporal link-reflection `theta(t, x) = (-1-t, x)` and the
Sharatchandra fermion reflection convention, the **direct single-step
spin-basis Lagrangian reflection-positivity Gram matrix**

```text
    G_{IJ} = <Theta(F_I) F_J>_S,    F_I in A_+ (positive-time half),
```

computed with the correct Berezin contraction
`<bar(chi)_a chi_b> = -(M^{-1})[b,a]`, is **not positive semidefinite**.
The primary runner exhibits a free-configuration counterexample with
minimum eigenvalue `-0.80` and PSD failure in 5/5 sampled U(1)
configurations. This is the load-bearing negative result of this row.

The mechanism is structural (see §"Single-step no-go" below): the
staggered spatial phase `eta_1(x) = (-1)^{t_x}` flips sign across the
reflection plane and the Sharatchandra Theta carries no compensating
phase, so the single-step spin-basis action is not reflection-positive
under Theta alone.

## Literature context (NOT load-bearing on this row)

The standard lattice-QFT resolution of single-step staggered RP
failure is the **2-step blocked transfer matrix** `T_hat^2 = S_hat^2`
over two lattice spacings, on which a positive Hermitian transfer
operator and a non-negative subtracted energy spectrum are obtained.
This is the result of Sharatchandra-Thun-Weisz (Nucl. Phys. B 192
(1981) 205) and Palumbo (Phys. Rev. D 66 (2002) 077503), summarised in
Smit, *Intro. to QFT on a Lattice*, §6 as `T_hat_4 = S_hat_4^2`, with
the single-step spin-basis difficulty noted in Caracciolo-Palumbo
(Phys. Rev. D 87 (2013) 014507, arXiv:1210.1786).

**This row does not derive the 2-step positivity.** The 2-step result
is recorded here only as the published resolution surface, explicitly
**non-load-bearing** for this no_go row. Constructing and proving the
2-step `T_hat^2` positivity in-repo (per the 2026-05-28 audit
instruction) is a separate future-work target; a positive companion
row can be promoted when that construction lands. Downstream consumers
that need positive staggered RP should treat the 2-step positivity as
literature-cited, not as a retained in-repo theorem, until that
companion row exists.

## Single-step no-go (load-bearing on the runner)

The primary runner builds the staggered KS Dirac matrix
`M = M_KS + m I` on `L_t = 4`, `L_s = 2`, `m = 0.5`, with U(1)
Abelian gauge links and link-reflection `theta(t, x) = (-1-t, x)`. It
computes the Gram matrix

```text
    G_{IJ} = <Theta(F_I) . F_J>_S
```

via Berezin/Wick contraction with propagator `M^{-1}` for a basis of
monomials in `A_+` up to degree 2 (37 basis elements), and reports the
minimum eigenvalue of the Hermitised Gram matrix.

Results from the cached run:

- Free `U = 1` case: Gram minimum eigenvalue `= -0.80`. Diagonal
  entries for degree-1 monomials `chi_x` and `bar(chi)_x` are all
  `-0.4`.
- 5 random U(1) gauge configurations: 5/5 PSD violations with
  minimum eigenvalues in `[-2.10, -1.08]`.

The mechanism behind the no-go is structural: under temporal
reflection `theta(t, x) = (-1-t, x)`, the staggered spatial phase
`eta_1(x) = (-1)^{t_x}` flips sign across the reflection plane,
because parity of the temporal index is exchanged. The simple
Sharatchandra Theta (chi swap chi-bar with site relabel) does not
include a phase compensator for this asymmetry, so the action is not
reflection-invariant under Theta alone in the spin basis. The result
matches Caracciolo-Palumbo (arXiv:1210.1786).

The 2-step blocked formulation works around this by using a 2-step
temporal interval; this is the standard route used in STW 1981,
Palumbo 2002, Smit, and the Golterman 2024 staggered review
(arXiv:2406.02906).

This no-go is deliberately narrow. It rules out the direct
single-step spin-basis Lagrangian Gram matrix under Sharatchandra
Theta alone, as tested by the runner. It does not rule out a
phase-compensated reflection, a square-root construction, a flavour-
basis construction, or the 2-step blocked transfer matrix; those are
separate surfaces, and the 2-step blocked surface is kept as the
positive scope of this note.

## Hamiltonian-level secondary exhibits

The secondary runner
[`scripts/axiom_first_reflection_positivity_check.py`](../scripts/axiom_first_reflection_positivity_check.py)
provides structural finite-block checks for the chosen lattice
Hamiltonian `H_lat` (built from KS hop matrix plus mass):

- `E1`: `T = exp(-a_tau H_lat)` is Hermitian and positive (trivially,
  because `H_lat` is Hermitian by construction);
- `E2`: U(1) Wilson plaquette transfer matrix is Hermitian and
  positive (trivial, for the same reason);
- `E3`: `<vac| F^dagger T^tau F |vac>` is non-negative for a finite
  list of `F` monomials acting on the chosen `H_lat`;
- `E4`: the Gram matrix on the Fock basis is PSD (which equals `T`
  itself, again trivial);
- `E5`: the staggered chirality anticommutation `{epsilon, M_KS} = 0`
  (a structural algebraic identity);
- `E6`: a Wilson-fermion determinant diagnostic (non-load-bearing).

`E1`-`E4` are not Lagrangian RP exhibits. They demonstrate
**Hamiltonian-level positivity** for a chosen `H_lat` via the trivial
fact that `exp(-a_tau H)` is positive if `H` is Hermitian. The
load-bearing Lagrangian RP claim is governed by the primary no-go
runner, not by these structural exhibits.

`E5` is a genuine algebraic identity that supports the determinant
positivity input (it is the source of the +/- lambda paired-eigenvalue
identity used in the Case A determinant note).

## What this note does NOT claim

- single-step Lagrangian RP for staggered KS in the spin basis;
- a universal impossibility theorem for every conceivable one-step
  staggered transfer-matrix construction;
- a full staggered + Wilson fermion RP theorem;
- an unconditional Wilson-sector determinant positivity statement;
- continuum-limit / OS-reconstruction RP from this lattice setup
  alone;
- a global claim that every historical citation to this row is safe
  without checking whether the downstream consumer uses single-step
  or 2-step RP (downstream consumers that depend on single-step RP
  specifically need to be re-audited; consumers that only need
  "RP holds for staggered KS lattice in the standard sense" are
  compatible with the 2-step formulation).

## No-Go Discipline Gate

This gate applies only to the narrow negative claim:

```text
Direct single-step spin-basis Lagrangian RP for staggered KS under
Sharatchandra Theta alone is non-PSD on the tested finite surface.
```

The gate does not assert a universal no-go over all possible one-step
or phase-compensated constructions.

- **N1 Alternative routes.**
  1. Direct Sharatchandra single-step Gram matrix: ATTEMPTED; the
     primary runner gives a free-configuration counterexample with
     minimum eigenvalue `-0.80`.
  2. Same direct surface under random U(1) links: ATTEMPTED; the
     primary runner finds PSD failure in 5/5 sampled configurations.
  3. Pure Hamiltonian positivity `T = exp(-aH)`: ATTEMPTED by the
     secondary runner, but it proves only Hamiltonian positivity for a
     chosen `H_lat`; it does not prove Lagrangian RP.
  4. 2-step blocked / flavour-basis transfer matrix: KNOWN VIABLE
     BY LITERATURE; this is the adopted positive scope, not a counter
     to the narrow no-go.
  5. Phase-compensated or square-root one-step construction:
     UNTESTED AND OUT OF SCOPE; the note does not claim this route is
     impossible.
- **N2 Wall independence.** The narrow no-go has one collapsed wall:
  the direct single-step Sharatchandra-Theta spin-basis Lagrangian
  Gram matrix is non-PSD. Basis choice, single-step timing, and
  missing phase compensation are not independent walls; they are the
  defining components of the tested surface.
- **N3 Hidden-wall scan.** "Published literature" is context for the
  2-step narrowing, not proof of the finite counterexample. "Standard"
  means the 2-step blocked construction in the cited papers. "Hamiltonian"
  is explicitly non-load-bearing for Lagrangian RP.
- **N4 Residual matching.** The runner attacks exactly the residual
  from the prior overclaim: direct single-step `G_{IJ} =
  <Theta(F_I) F_J>_S` positivity for staggered KS in the spin basis.
  The literature citations support the 2-step replacement surface and
  are not used as finite counterexample evidence.
- **N5 Rhetoric audit.** The negative phrase is restricted to this
  per-finite-block, per-tested-Gram-surface construction. It is not
  stated as a lattice-wide impossibility theorem or as a no-go for
  all one-step transfer matrices.
- **N6 Partial-closure path.** The partial closure path is the 2-step
  blocked formulation; it is adopted here and does not require a new
  axiom.
- **N7 Steelman.** A hostile reviewer could argue that a modified
  reflection with compensating staggered phases, a square root of a
  2-step transfer matrix on a different Fock space, or a flavour-basis
  construction might define a positive one-step object. This note does
  not deny that possibility; it narrows the claim to the directly
  tested Sharatchandra-Theta spin-basis Lagrangian surface.
- **N8 Cross-cycle echo.** The 2026-05-26 Wilson-subsurface repair
  already showed that this row must not absorb unsupported stronger
  fermion-sector claims. The same mechanism applies here: preserve
  the durable positive scope, remove the unsupported stronger surface,
  and queue the source row for independent re-audit.

Gate outcome: **PASS for the narrow no-go; FAIL for any broader
universal single-step impossibility claim.** This note ships only the
narrow no-go.

## Honest Status

Branch-local source-surface repair. The load-bearing claim is a
**no_go**: the direct single-step spin-basis Lagrangian RP Gram matrix
for staggered KS under Sharatchandra Theta is non-PSD (runner-verified,
correct Berezin convention). It is not an author-applied audit
promotion.

What this row supports:

- a terminal negative witness: downstream claims must NOT assume
  single-step spin-basis Lagrangian RP for staggered KS holds;
- a pointer to the literature 2-step resolution (non-load-bearing).

What this row does NOT support:

- a positive single-step staggered RP theorem (this row proves the
  no_go);
- an in-repo-derived 2-step `T_hat^2` positivity (literature-cited
  only; a future companion row can derive and promote it);
- a full staggered + Wilson-fermion RP theorem;
- an unconditional Wilson-sector determinant positivity statement.

Downstream consumers that previously cited this row for *positive*
staggered RP must re-audit: the positive content is now literature-
context only, pending a derived 2-step companion row.
