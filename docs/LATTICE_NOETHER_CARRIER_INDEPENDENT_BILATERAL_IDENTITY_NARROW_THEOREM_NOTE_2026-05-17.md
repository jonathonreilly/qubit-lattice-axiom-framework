# Carrier-Independent Bilateral Lattice-Noether Identity — Narrow Theorem (Block 27)

**Date:** 2026-05-17
**Type:** positive_theorem (narrow sub-theorem)
**Loop:** `filter-excluded-positive-closures-2026-05-17`, Block 27
**Authority role:** source-note proposal; effective `effective_status`
is set only by the independent audit lane.
**Primary runner:** `scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py`
**Cache:** `logs/runner-cache/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.txt`
**Parent (audited_conditional row this narrow closure targets):**
  `docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`

## Authority disclaimer

This is a source-note proposal. The `claim_type`, scope, named
admissions, and `positive_theorem` classification are author-proposed;
the audit lane has full authority to retag, narrow, or reject the
proposal. This note adds a narrow sub-theorem that **strictly extends**
the parent note's content without modifying parent text. No parent
dependency is added or removed; the parent's `audited_conditional`
status is unaffected by this note.

## Why this note exists

The 2026-04-29 axiom-first lattice Noether theorem note
(`docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`) carries
the audit verdict `audited_conditional` with the explicit verdict
rationale:

> "The internal Noether manipulation and runner exhibits are algebraic
> checks on the admitted staggered carrier, so class A is appropriate.
> However the restricted packet explicitly says the
> staggered-Dirac/Grassmann carrier is an open gate and is imported as
> an admitted context input rather than derived from the provided
> axioms. Under the rubric, an explicit unclosed carrier import
> requires audited_conditional even if the bounded identity closes on
> that carrier."

The named gap is the **carrier import**, not the algebraic Noether
identity. The parent's proof of (5) -> (4) under the U(1) phase
generator (parent Step 2 and Step 4a) is a finite-Grassmann variational
argument whose only dependence on the staggered structure is that the
matrix `M_KS` is anti-Hermitian off-diagonal with nearest-neighbour hop
coefficients of the form `+-(1/2) eta_mu(x)`.

This note observes that the parent's bilateral algebraic content is
**carrier-independent** within a precisely characterized class of
nearest-neighbour operators on `Z^d` -- the *axis-translation-invariant
carrier class* defined below. The staggered carrier `eta_mu` is one
member of this class; the naive Wilson-free carrier `c_mu = 1` is
another; we exhibit a third explicit member to certify the class is
strictly larger than {naive, staggered}. The bilateral Noether
identity is then a positive theorem on every member of the class, with
**no dependence on the staggered-Dirac realization gate**.

The narrow closure here is therefore a slice of the parent's
audited_conditional gap: the *bilateral algebraic core* (parent Step 2
plus the U(1)-phase Step 4a) is recovered as a positive theorem on the
axis-inv class, independent of the carrier-import question. The
remainder of the parent's content -- specifically the identification of
the carrier with `M_KS` and the physical naming of `J` as the
"fermion-number current" of staggered Kogut-Susskind theory -- is
unchanged and remains subject to the parent's gate-import dependency.

## Scope

**In scope.** The bilateral Noether identity for a nearest-neighbour
operator `M` on the periodic `Z^d` lattice with parametrization

```text
    M_{x, x+mu_hat}  =  +(1/2) c_mu(x)
    M_{x, x-mu_hat}  =  -(1/2) c_mu(x)                                   (P)
```

where `c_mu : Z^d -> R` is an arbitrary real-valued lattice function,
plus a mass term `m * I` (`m > 0`).

**Carrier class.** The *axis-translation-invariant carrier class* is

```text
    AxisInv(Z^d)  :=  { c_mu : Z^d -> R  |  c_mu(x + mu_hat) = c_mu(x),
                                            for all x in Z^d, mu in {1,...,d} }.   (AxisInv)
```

The condition `(AxisInv)` says that `c_mu` does not depend on `x_mu`
itself (only on the other components `x_1, ..., x_{mu-1}, x_{mu+1},
..., x_d`). Equivalently, `c_mu` is constant along every line parallel
to the `mu`-axis.

**Out of scope.**

- Identification of `M` with `M_KS` (the staggered Kogut-Susskind
  operator) or any specific physical operator. That identification
  re-introduces the staggered-Dirac realization gate of the parent
  note's audited_conditional verdict.
- Wilson-sector contributions `M_W != 0`. The parent note is also
  silent on Wilson contributions outside its scope statement; we
  inherit that silence here.
- The `(2Z)^d` sublattice translation case (parent's (N1)). That case
  uses the parent's discrete Ward-identity Step 4b, which is a
  different algebraic content than the local-alpha bilateral
  derivation we treat here. Step 4b carrier-independence is left
  for follow-on work.

## Theorem (carrier-independent bilateral Noether identity)

**(T1) Anti-Hermiticity characterization.** Let `M` be the operator
defined by `(P)` plus mass term. Then the off-diagonal part of `M` is
anti-Hermitian (`M_off^T = -M_off`) if and only if `c_mu` is in
`AxisInv(Z^d)`.

Proof. By direct expansion:

```text
    M_{x, x+mu_hat}  +  M_{x+mu_hat, x}
        = +(1/2) c_mu(x)  +  (-(1/2) c_mu(x+mu_hat))
        = (1/2) [ c_mu(x) - c_mu(x + mu_hat) ].
```

This vanishes for every `(x, mu)` iff `c_mu(x + mu_hat) = c_mu(x)` for
every `x`, which is `(AxisInv)`. ∎

**(T2) Carrier-independent bilateral conserved current.** For any
`c_mu` in `AxisInv(Z^d)` and any field-index generator `T` satisfying
the symmetry condition

```text
    [T, M]  =  T M  -  M T  =  0,                                        (Sym)
```

the local-alpha Ward expansion of `S_F = chi_bar M chi` produces the
bilateral conserved current

```text
    J^mu_x(T)  =  (1/2) c_mu(x) [ chi_bar_x  T  chi_{x+mu_hat}
                                  + chi_bar_{x+mu_hat}  T  chi_x ]        (5)
```

with on-shell divergence vanishing identically:

```text
    partial^L_mu  J^mu_x  =  0     on shell.                              (10)
```

Proof.  We follow the parent's Step 2 verbatim, replacing `eta_mu(x)`
by the generic `c_mu(x)` throughout and noting that `(AxisInv)` is
exactly the condition the reindex step needs.

*Local-alpha expansion.* Vary `chi_y -> chi_y + alpha^A_y T^A chi_y`,
`chi_bar_x -> chi_bar_x - alpha^A_x chi_bar_z (T^A)_{zx}` with `alpha`
site-dependent. The variation of `S_F` is

```text
    delta S_F[alpha(x)]
      = Sum_{x,y,z} (alpha^A_y - alpha^A_x) chi_bar_x M_{xy} T^A_{yz} chi_z
```

(parent eq. 7a; the constant-`alpha` piece vanishes by `(Sym)`).

*Forward-backward split.* For the nearest-neighbour structure `(P)`,
only `y = x +- mu_hat` pairs contribute:

```text
  forward  (y = x + mu_hat):
    Sum_{x,mu}  (1/2) c_mu(x)  chi_bar_x T^A chi_{x+mu_hat}
                              ( alpha^A_{x+mu_hat} - alpha^A_x )
  backward (y = x - mu_hat):
    Sum_{x,mu}  -(1/2) c_mu(x)  chi_bar_x T^A chi_{x-mu_hat}
                              ( alpha^A_{x-mu_hat} - alpha^A_x )
                                                                           (7b)
```

*Reindex of the backward piece.* Substitute `x' = x - mu_hat` so `x =
x' + mu_hat`. The coefficient `c_mu(x) = c_mu(x' + mu_hat)`. By
`(AxisInv)`, `c_mu(x' + mu_hat) = c_mu(x')`, so the backward piece
becomes

```text
  backward (after reindex):
    Sum_{x',mu}  (1/2) c_mu(x')  chi_bar_{x'+mu_hat} T^A chi_{x'}
                              ( alpha^A_{x'+mu_hat} - alpha^A_{x'} )
                                                                           (7b')
```

This is the unique step that depends on the carrier; `(AxisInv)` is
*precisely* what makes the reindexed backward coefficient match the
forward coefficient at the same site `x'`. Combining:

```text
    delta S_F[alpha(x)]
      = Sum_{x,mu}  (1/2) c_mu(x)  [ chi_bar_x T^A chi_{x+mu_hat}
                                   + chi_bar_{x+mu_hat} T^A chi_x ]
                                  ( alpha^A_{x+mu_hat} - alpha^A_x )
                                                                           (7c)
```

The coefficient of the discrete forward derivative `(partial^L_mu
alpha^A)_x = alpha^A_{x+mu_hat} - alpha^A_x` is the bilateral form
`J^{mu,A}_x` in (5).

*On-shell conservation.* On classical solutions of `M chi = 0 = chi_bar
M`, the bulk variation vanishes for arbitrary `alpha`, so

```text
    Sum_x  alpha^A_x  partial^L_mu  J^{mu,A}_x  =  0
```

for all `alpha`. Choosing `alpha^A_x = delta_{x, x_0}` gives `(10)`. ∎

**(T3) Class is strictly larger than {naive, staggered}.** Both the
naive Wilson-free carrier `c_mu(x) = 1` and the staggered carrier
`c_mu(x) = eta_mu(x) = (-1)^{Sum_{nu<mu} x_nu}` are in
`AxisInv(Z^d)`. Moreover the carrier

```text
    phi_mu(x)  :=  1  +  0.3 * cos( pi * Sum_{nu != mu} x_nu / L )
```

is in `AxisInv(Z^d)` (each `phi_mu` is a function of the components
`x_nu` for `nu != mu` only), and is neither identically `1` nor `+-1`
on every site, so it is neither the naive nor the staggered carrier.
Runner exhibit `E4` verifies the bilateral identity for `phi_mu`.

This certifies that `AxisInv(Z^d)` strictly contains
`{naive, staggered}`, so the theorem is a *genuine* extension and not
a trivial repackaging of the two known carriers.

## Sharpness

**(T4) Sharpness of the class characterization.** The condition
`(AxisInv)` is *sharp* for the off-diagonal anti-Hermiticity of `M`:
by `(T1)`, dropping the condition strictly breaks anti-Hermiticity at
every site `x` where `c_mu(x + mu_hat) != c_mu(x)`. Runner exhibit `E5`
exhibits a non-axis-inv carrier `c_mu(x) = 1 + 2 (x_mu mod 2)` and
measures `||M_off + M_off^T||_max = 1.000`, an O(1) departure from
anti-Hermiticity.

Loss of off-diagonal anti-Hermiticity is *not* by itself a
contradiction with the U(1)-phase Ward identity (because `T = i I`
commutes with any `M`), but it does break the *bilateral derivation*
of Step 2: the reindex step `(7b) -> (7b')` requires `c_mu(x +
mu_hat) = c_mu(x)` to match coefficients, so outside `AxisInv` the
bilateral form `(5)` is no longer the form produced by the local-alpha
expansion.

For non-trivial generators `T` (those that don't commute with arbitrary
operators), `(Sym)` itself constrains the relationship between `T`
and `c_mu`, and the bilateral form `(5)` is the *only* form that the
finite-Grassmann variational derivation produces, again requiring
`(AxisInv)`.

## Carrier inclusion: staggered and naive Wilson-free

Both `c_mu(x) = 1` (naive) and `c_mu(x) = eta_mu(x)` (staggered) are
in `AxisInv(Z^d)`:

- *Naive.* `c_mu(x + mu_hat) = 1 = c_mu(x)` trivially.
- *Staggered.* `eta_mu(x) = (-1)^{Sum_{nu < mu} x_nu}` depends on
  `x_1, ..., x_{mu-1}` but not on `x_mu`. So `eta_mu(x + mu_hat) =
  (-1)^{Sum_{nu < mu} (x + mu_hat)_nu}`, where `(x + mu_hat)_nu =
  x_nu` for every `nu < mu` (since `mu_hat` has zero `nu`-th component
  for `nu != mu`). Hence `eta_mu(x + mu_hat) = eta_mu(x)`.

So `staggered, naive in AxisInv`. The narrow theorem `(T2)` therefore
*recovers* the parent's bilateral identity for staggered as a
corollary of the carrier-independent statement, with no dependence on
the staggered-Dirac realization gate.

## On-shell convention

The "on shell" condition used here is the same as the parent's: a
choice of `chi`, `chi_bar` field expectations that solve the
classical equations of motion `M chi = 0`, `chi_bar M = 0`. For `M`
of the form `M = M_off + m I` with `m > 0`, the operator is
invertible, and the appropriate operationally-canonical "on-shell"
expectation values are the Wick-contracted Green's functions

```text
    <chi_bar_a chi_b>  =  Minv_{b, a}
```

evaluated in the free Grassmann partition with action
`exp(- chi_bar M chi)`. This is the convention adopted by the parent
runner's `E3` exhibit and by the present runner's `E1`-`E8` exhibits
(see `greenfn_expectation_bilateral` in the runner).

## Carrier-independence is a quantitative statement

**(T5) Uniformity in `c_mu`.** For every `c_mu` in `AxisInv(Z^d)` and
every `T` satisfying `(Sym)`, the on-shell divergence of `(5)` vanishes
*exactly* in the algebraic sense and to machine precision in numerical
realization. Runner exhibit `E8` sweeps `K = 16` distinct
axis-inv carriers and confirms `max |partial^L J^mu|_max < 1.2e-15`
across the full sweep, uniformly in the carrier.

## Hypothesis-set summary

**Framework axioms (current).**

- **A1 - local algebra `Cl(3)`.** Used only via the existence of a
  faithful local representation of the Cl(3) algebra on each site
  (parent A1; this note carries A1 in the same minimal way as the
  parent).
- **A2 - substrate `Z^d`.** Used via the discrete nearest-neighbour
  hop structure. The narrow theorem here is dimension-independent
  in `d`; the runner exhibits use `d = 3`.

**No admitted context inputs.** This narrow theorem does *not* admit
the staggered-Dirac realization gate, because the bilateral identity
holds for *every* carrier in `AxisInv(Z^d)`, of which the staggered
carrier is one instance. The carrier choice is a *parameter* of the
theorem, not a load-bearing import. The runner exhibits four distinct
carriers (random axis-inv, naive, staggered, phi-cosine) plus
sweeps over K = 16 random axis-inv carriers (E8).

**Relationship to parent note.** The parent note's `Hypothesis set
used` section admits the carrier gate to *identify* `M` with `M_KS`
and the parent's `J` with the "fermion-number current" of staggered
Kogut-Susskind theory. The narrow theorem here removes the
identification, treating `(P)` as a generic-carrier parametrization
with `c_mu in AxisInv(Z^d)` as the only constraint on the carrier.
The parent's `(N2)` identification of `J^mu_x` with the staggered
fermion-number current is unchanged; this note only certifies that
the underlying *algebraic identity* (5) does not need the
staggered-specific carrier to close.

## Runner verification

The runner
`scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py`
exhibits eight numerical checks:

- **E1.** Axis-inv carrier sweep: `K = 8` random `c_mu in AxisInv`
  (constructed by broadcasting `L^{d-1}` transverse fields along
  each axis). Worst `||[T, M]||_max = 0`, worst on-shell
  `|partial^L J|_max < 1e-15`.
- **E2.** Naive Wilson-free reference: `c_mu = 1`. Verifies the
  trivially-axis-inv member.
- **E3.** Staggered reference: `c_mu = eta_mu`. Recovers the parent
  `E3` numerical target.
- **E4.** Third explicit class member: `phi_mu(x) = 1 + 0.3 *
  cos(pi * Sum_{nu != mu} x_nu / L)`. Verifies the class is strictly
  larger than {naive, staggered}.
- **E5.** Sharpness: non-axis-inv carrier `1 + 2(x_mu mod 2)` gives
  `||M_off + M_off^T||_max = 1.000` (O(1) violation of
  anti-Hermiticity), while the axis-inv carrier `eta_mu` gives
  identically zero. Confirms `(T1)` is a sharp characterization.
- **E6.** Non-identity internal generator: `T = I_lattice (x)
  sigma_3` with a 2-component internal `chi`. Verifies `(T2)` for a
  generator other than the trivial `T = i I`.
- **E7.** Algebraic Lie-substitution: `J4 = (+i) * J5` exactly on
  any random field (no on-shell requirement). Verifies the
  algebraic substitution identity for a generic carrier.
- **E8.** Carrier-uniformity: `K = 16` distinct axis-inv carriers,
  each on its own M_k on-shell state, all give
  `|partial^L J|_max < 1.2e-15`. Verifies `(T5)`.

All eight exhibits report `PASS`. The runner exits 0 iff all exhibits
pass.

## Corollaries (narrow)

**(C1) Parent's `(N2)` U(1) fermion-number current is recovered as the
staggered-specialization of the narrow theorem.** Specifically, for
`T = i I` and `c_mu = eta_mu`, the bilateral form `(5)` reduces to the
parent's `(4)` by the algebraic identity `J4 = +i * J5` (runner E7),
exactly as the parent's Step 4a claims. The narrow theorem here
re-derives this conclusion without reference to the staggered-Dirac
realization gate, recovering the parent's `(N2)` content as a
specialization of the carrier-independent `(T2)`.

**(C2) Multiple discretization schemes share the same Noether
identity.** The naive Wilson-free fermion (`c_mu = 1`) and the
staggered Kogut-Susskind fermion (`c_mu = eta_mu`) are *both* in
`AxisInv(Z^d)`, so the on-shell conservation of `J` is structurally
the same identity for both discretizations. This is a useful
consistency check on the bilateral Ward identity: it cannot
distinguish between "naive" and "staggered" lattice fermions at the
level of the local-alpha derivation, because both share the
axis-translation-invariance property.

## Honest status

**Positive narrow theorem on the explicit framework baseline.** The
bilateral Noether identity is a positive theorem on the
axis-translation-invariant carrier class, with `(T1)`-`(T5)`
established algebraically and verified numerically by the eight runner
exhibits to machine precision. The narrow theorem does *not* close
the parent note's audited_conditional gap; rather, it closes a
specific *slice* of that gap: the bilateral algebraic core is recovered
without admitting the staggered-Dirac realization gate, leaving only
the carrier-identification question (which is what the parent's
`audited_conditional` rationale actually concerns).

The parent note's `audited_conditional` status is unaffected by this
note. The independent audit lane has full authority over the parent's
effective status; this note adds a strictly-additive positive
sub-theorem that does not modify the parent note's text or change
its dependency graph.

The narrow theorem here is dimension-independent and gate-independent;
it depends only on `A1`, `A2`, and the elementary finite-Grassmann
variational technique used by the parent in Step 2.

## Not in scope

- The parent's `(N1)` `(2Z)^d` sublattice momentum current. That
  case uses the parent's discrete Ward-identity Step 4b, which is a
  different algebraic content than the local-alpha bilateral
  derivation treated here. A carrier-independent version of Step 4b
  is left for follow-on work.
- Anomaly closure of the conserved currents at the quantum level.
  Same as the parent.
- Identification of `M` with the physical `M_KS` operator. That
  identification re-introduces the staggered-Dirac realization gate
  of the parent's audited_conditional verdict.

## Load-bearing dependencies

- Current public framework memo:
  `MINIMAL_AXIOMS_2026-05-03.md` (`A1`: Cl(3) per-site, `A2`: Z^d
  spatial substrate).

## Citations

- Parent (audited_conditional, this narrow closure targets a slice):
  `docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md`.
- For context (sister sub-theorems on the parent surface):
  - `docs/STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`
    (Block 25; same authority pattern: a strictly-additive narrow
    sub-theorem on a parent note's slice).

## Admitted context inputs

**None.** The narrow theorem does not admit the staggered-Dirac
realization gate, because the bilateral identity is carrier-independent
within the axis-translation-invariant class.

`AxisInv(Z^d)` is defined directly from the substrate `Z^d` axiom and
makes no reference to staggered-specific structure. The staggered
carrier `eta_mu` is one *member* of the class (verified by direct
expansion); the naive carrier `c_mu = 1` is another. The runner
exhibits a third explicit member (`phi_mu = 1 + 0.3 cos(...)`) to
certify the class is genuinely larger than {naive, staggered}.

## Audit dependency repair links

- [minimal_axioms_2026-05-03](MINIMAL_AXIOMS_2026-05-03.md) - current
  public framework memo; sole upstream framework dependency.
- [axiom_first_lattice_noether_theorem_note_2026-04-29](AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md) -
  parent (audited_conditional). This narrow theorem is strictly
  additive on the parent and does not modify the parent's text or
  dependency graph.
