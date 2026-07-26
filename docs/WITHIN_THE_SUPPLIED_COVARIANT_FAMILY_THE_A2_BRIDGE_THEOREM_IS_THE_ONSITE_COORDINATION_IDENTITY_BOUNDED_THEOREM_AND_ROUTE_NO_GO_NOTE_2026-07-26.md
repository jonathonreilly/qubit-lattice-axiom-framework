# Within the Supplied Covariant Family, A2's Missing Bridge Theorem Is Exactly "the On-Site Term Equals the Coordination Number" — and As Posed It Carries an Energy Origin That Is Unobservable in the Matter Dynamics into the Observable Force Range (Bounded Theorem + Route No-Go)

**Date:** 2026-07-26
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact rational operator algebra and exact
torus spectra) **+ route_no_go** (the route as posed cannot close; escape
conditions named).
**Status authority:** none. Audit: unset. Constitutional effect: none. This
note edits no axiom, foundation, Qualification, primitive, registry, policy,
queue, audit-status, or PR-control surface. **It does not supply A2's missing
bridge theorem, and does not change the status of
`gravity_full_self_consistency_note`.**
**Primary runner:**
[`scripts/physical_a2_bridge_is_the_onsite_coordination_identity_cycle709_2026_07_26.py`](../scripts/physical_a2_bridge_is_the_onsite_coordination_identity_cycle709_2026_07_26.py)
(8 PASS / 0 FAIL, exit 0).

## The gap

The `critical` root row `gravity_full_self_consistency_note` (`deps: []`,
773 transitive descendants) carries:

> `missing_bridge_theorem: supply a retained derivation of `L^{-1} = G_0` from
> the accepted framework premises`

This note identifies that gap exactly and shows the route as posed cannot
close. It does not close it.

## The identification

Work inside the **supplied** range-1 proper-cubic covariant family (landed
classification: `L = A·I + B·Delta`). Write the matter side generally:

```text
A_adj    nearest-neighbour adjacency on Z^3          (Lattice axiom: adjacency)
Delta    = A_adj - 6I                                (coordination number 6)
H(mu)    = mu*I - A_adj                              (on-site term mu, hopping -A_adj)
G(E)     = (H - E)^{-1}                              (matter resolvent at reference energy E)
```

A2 generalized to the resolvent is `L^{-1} = G(E)`, hence `L = H - E`. Since
`H(mu) = (mu - 6)·I - Delta` **exactly** (row R1), comparing with
`L = A·I + B·Delta` gives

```text
B = -1,        A = mu - 6 - E.
```

**A2 as written** — `G_0 = H^{-1}`, i.e. `E = 0`, with `H` in graph-Laplacian
form, i.e. `mu = 6` — **is exactly the statement `A = 0`** (row R2). One number,
two readings:

| reading | meaning |
|---|---|
| `A = mu - 6` | the on-site term minus the coordination number |
| `A = -E` | minus the reference energy of the matter resolvent |

**So the missing bridge theorem is exactly: derive `mu = 6`** — that the
on-site term equals the coordination number. Equivalently (row R5), that `H`
has vanishing row sums, i.e. that `H` annihilates the uniform state.

That restatement is the main deliverable. The gap has stood as "derive
`L^{-1} = G_0`", which names an operator identity between two supplied objects;
it is the same thing as one arithmetic identity on one diagonal entry.

## Why the route as posed cannot close

**`A` is observable.** `min spec(L) = A` exactly (row R3), and the band is
`[A, A+12]` with both endpoints exact (row R7). `A` is the mass gap of the
field operator: near `k = 0` the Green's function goes as `1/(A + k^2)`, so
`A = 0` gives the `1/r` law and `A > 0` gives a force screened at range
`1/sqrt(A)`. The force range is not a convention.

**`mu` is not observable in the matter dynamics.** A landed note records this
in its own words:

> "For each raw Hamiltonian `H`, the runner removes the energy origin … **The
> shift has no observable effect because it contributes only a global phase**."
> — [`SINGLE_AXIOM_HILBERT_NOTE`](SINGLE_AXIOM_HILBERT_NOTE.md)

Row R4 re-earns it exactly: `H -> H + cI` moves every eigenvalue by exactly
`c`, leaves all 63 spectral gaps identical, commutes with `A_adj` so the
eigenbasis is unchanged for every `mu`, and leaves `H` self-adjoint for every
`mu`, hence the evolution unitary.

**So A2, as posed, makes an observable (the force range) a function of a
quantity that is unobservable everywhere else `H` appears.** A derivation of
A2 from the framework premises would have to derive observable content from
input the framework itself treats as redundant. That is the obstruction, and it
is why five previously-checked mechanisms found nothing: none of them fixes an
energy origin.

**The `H = -Delta_lat` form does not settle it.** The graph-Laplacian form is
the hopping operator *measured from the band bottom*: the bare hopping
Hamiltonian is `-A_adj` (`mu = 0`, giving `A = -6`), and `mu = 6` is precisely
the choice that puts zero at the bottom of the band. Writing `H = -Delta_lat`
therefore assumes the identity that the bridge theorem is supposed to prove.

## The discriminator, and the sharpest escape condition

Row R6 isolates what *would* force `mu = 6`.

- **A continuous-time Markov generator must have zero column sums**, because
  `d/dt sum(p) = sum(Q p) = 0` for every `p` requires it. For
  `Q = A_adj - mu*I` the column sums are `6 - mu`, so probability conservation
  **forces `mu = 6`** — and indeed `Delta` is the standard random-walk
  generator on `Z^3`.
- **A self-adjoint quantum Hamiltonian conserves probability by unitarity**,
  which requires only `H = H^dagger` — true for every real `mu` (verified for
  five values). The quantum reading does **not** force `mu = 6`.

So the on-site coordination identity is a *stochastic* normalization, not a
quantum one, and the Qubit axiom puts the framework on the quantum side.

**Escape conditions, named and not adopted:**

- **(X1) a stochastic or detailed-balance requirement on record formation.**
  This is the strongest route, because R6 shows it *does* force `mu = 6`
  outright. What would be needed is a derivation that the record-formation
  process conserves a probability current on the lattice, not merely that
  amplitudes evolve unitarily.
- **(X2) a vacuum / band-bottom energy convention.** Standard physics, and an
  import here: the axioms supply no dynamics and therefore no ground state.
- **(X3) a shift symmetry `phi -> phi + c`**, which would force `L·1 = 0` and
  hence `A = 0` directly. This *appears* blocked, because the Record axiom
  fixes readouts absolutely (`I(empty) = 0` plus additivity), so the field's
  zero is not free. Establishing or refuting that is a separate question and is
  not settled here.
- **(X4) a background-subtraction convention** making the source a fluctuation
  about its mean. This resolves the corollary below but redefines what "source"
  means.

## Corollary, scoped to finite lattices

Row R8: at `A = 0` on a finite covariant lattice the constant is a genuine
kernel vector, so `L phi = -rho` is solvable only for zero-mean `rho`. Of the
81 non-negative integer sources enumerated, **exactly one** has zero sum — the
empty configuration. So on a finite covariant lattice A2 admits a non-negative
record density only if there are no records, which sits badly with "Records
form."

**This is a finite-volume statement and is labelled as such.** The parent
theorem is formulated on infinite `Z^3`, where a compactly supported
non-negative source is perfectly fine. The corollary constrains regulator
choice; it does not invalidate the parent's conditional implication.

## Claim ledger

Per the inference audit (physics-loop step 11). Hypotheses tagged
`[supplied]` (assumed and unforced) or `[satisfied]` (met by construction).

| ID | Claim | Support | Hypotheses | Shown vs claimed | Falsifier |
|---|---|---|---|---|---|
| N1 | `H(mu) = (mu-6)·I - Delta` exactly, so `A = mu - 6` | row R1, exact matrix identity at four values of `mu` | **[supplied]** `L` lies in the range-1 covariant family (its own classification states these operator hypotheses are supplied, not derived); **[supplied]** `H` is one-body-diagonal plus NN hopping; [satisfied] coordination 6 on `Z^3` | shown: the two matrices are equal entry-by-entry for the tested `mu`, and the identity is linear in `mu` so it holds for all; claimed: the same | a `mu` where the two matrices differ |
| N2 | A2 generalized gives `A = mu - 6 - E`, and A2 as written is `A = 0` | row R2, exact at six `(mu,E)` pairs | **[supplied]** the same operator family as N1; **[supplied]** A2 is read on the resolvent `G(E)` rather than only at `E=0` | shown: `L = H - E` matches `A·I + B·Delta` with `A = mu-6-E` exactly; claimed: the same, **and** that A2 as literally written (`E=0`, `mu=6`) is `A=0` | a pair where the reconstruction fails |
| N3 | `A` is observable: `min spec(L) = A` and the band is `[A, A+12]` | rows R3, R7, exact torus spectra | [satisfied] `L = A·I - Delta` on the `L=4` torus, cosines exactly rational | shown: the minimum attained eigenvalue equals `A` at four values, and both band endpoints are exact; claimed: `A` is the mass gap. **Not** claimed: the `1/sqrt(A)` range, which is the standard continuum reading and is cited, not computed here | a lattice where `min spec(L) != A` |
| N4 | `mu` is unobservable in the matter dynamics | row R4 (rigid shift, identical gaps, shared eigenbasis, self-adjoint for every `mu`) plus the landed `SINGLE_AXIOM_HILBERT_NOTE` sentence | [satisfied] `H(mu)` self-adjoint; [satisfied] the shift is a multiple of the identity | shown: the spectrum shifts rigidly, all 63 gaps are unchanged, `[H(mu), A_adj] = 0`, and `H = H^T` for five values of `mu`; claimed: unobservable **in the matter dynamics** — not that `mu` is unobservable everywhere, since A2 itself is what promotes it | a `mu`-shift that changes a gap, an eigenvector, or self-adjointness |
| N5 | the bridge theorem is exactly "derive `mu = 6`" | N1 + N2 | **[supplied]** the operator family, as in N1 | shown: A2 within that family is the single equation `mu - 6 - E = 0`; claimed: the bridge theorem *reduces to* that equation inside the family — **not** that it reduces to it unconditionally | an A2-satisfying `L` in the family with `mu != 6 + E` |
| N6 | `mu = 6` iff zero row sums iff `H` annihilates the uniform state | row R5, exact at three `mu` | [satisfied] the lattice is regular of degree 6 | shown: row sums equal `mu - 6`, and `H·1 = 0` exactly when `mu = 6`; claimed: the same | a `mu != 6` annihilating the constant |
| N7 | zero row sums are forced for a Markov generator, not for a quantum Hamiltonian | row R6, exact column sums and exact symmetry checks | [satisfied] the Markov conservation law is `sum(Qp) = 0` for all `p`; [satisfied] unitarity requires only self-adjointness | shown: column sums are `6 - mu`, zero only at `mu=6`; and `H = H^T` for every tested `mu`; claimed: the same. **Not** claimed: that the framework's process is or is not stochastic | a self-adjointness failure at some real `mu`, or a Markov generator conserving probability with `mu != 6` |
| N8 | on a finite covariant lattice, A2 admits a non-negative source only if empty | row R8, exhaustive over 81 non-negative sources | [satisfied] finite periodic lattice; [satisfied] `rho >= 0` for a record density | shown: the constant is in `ker(L)` at `A=0`, uniform `rho` is obstructed, and exactly one of 81 non-negative sources has zero sum; claimed: the same, **scoped to finite lattices only** | a non-negative non-zero source with zero sum, or a finite covariant lattice where `L` has no constant kernel vector |

## Scope

- **The operator family is supplied, not derived** — flagged in the title and
  in every ledger row that uses it. Outside the range-1 covariant family, `A2`
  is not a statement about two coefficients and N1/N2/N5 do not apply.
- **`A2` is read on the resolvent.** The row states `G_0 = H^{-1}`; reading it
  as `G(E)` with `E` free is a generalization this note introduces in order to
  exhibit the freedom. At `E = 0` it reduces to the row's own statement.
- **Nothing here derives `mu = 6`, and nothing here refutes it.** The no-go is
  that the route *as posed* — from the accepted premises, with `H`'s energy
  origin free — cannot close. It is not a proof that `mu = 6` is false or
  underivable by other means; X1 in particular is a live route.
- **The `1/sqrt(A)` force range is the standard continuum reading** of a
  screened propagator and is cited, not computed here. What is computed is that
  `A` is the mass gap.
- Torus sizes are `L = 2` and `L = 4`, chosen so every cosine is an exact
  rational; no floating point is used anywhere.
- No lane, row, or obligation status is changed, and no N1–N8 discipline-gate
  verdict is awarded.

## Controls and honesty record

- R7 **exhibits its own counterexample** rather than excluding it: the
  continuum claim "singular for all `A` in `[-12,0]`" is false on a finite
  torus, where only a discrete subset is attained, and `A = -1` at `L = 4` is
  nonsingular. An earlier draft asserted the continuum "iff" and tested only
  `A ∈ {-13,-6,0,1}`, quietly omitting exactly the counterexamples.
- R4 originally "verified" real spectra with `isinstance(..., Fraction)` — a
  type test that cannot fail. Replaced by exact self-adjointness checks, which
  is the actual mathematical content.
- R8 originally tested an equivalence on two hand-picked vectors, both of which
  satisfied it trivially. Replaced by exhaustive enumeration over 81
  non-negative sources.
- All three defects were caught by the author during this cycle, under step 11,
  and are recorded rather than silently fixed.

## Dependency citations

The runner imports nothing from the repository. The gap and the row metadata
are from `docs/audit/data/ledger/gr/gravity_full_self_consistency_note.json`.
A2, its A1/A2 split, and the `L = G_0^{-1} = H` inversion are from
[`GRAVITY_FULL_SELF_CONSISTENCY_NOTE`](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md).
The energy-origin redundancy sentence is quoted from
[`SINGLE_AXIOM_HILBERT_NOTE`](SINGLE_AXIOM_HILBERT_NOTE.md) and re-earned by
row R4. The range-1 covariant classification is
[`PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25`](PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-25.md),
whose own text states that the linearity, finite-range, convolutional and
covariance hypotheses are supplied. The Lattice and Qubit axioms are from
[Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
