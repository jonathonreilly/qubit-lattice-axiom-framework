# Block05 Section — R-DICHOTOMY-N5 (clause N5, integrability reframe)

**Route:** R-DICHOTOMY-N5 (exercise `baxis-wall-break`, literature vector L2)
**Clause:** N5 / B-AXIS.3 — "no independent commuting transfer factor is admitted
as a second physical clock."
**Posture:** honest verification of an exercise-surfaced reframe. NOT a defense of
the existing no_go; NOT a closure. Outcome: **shrinks the wall + corrects a
block02 overclaim**, conditional on the (open) dynamics gate.
**Runner:** `scripts/single_clock_n5_integrability_dichotomy_2026_06_20.py`
**Runner cache:**
`logs/runner-cache/single_clock_n5_integrability_dichotomy_2026_06_20.txt`
**Runner result:** `TOTAL: PASS=37 FAIL=0` (deterministic, runtime < 3 s).

- **proposal_allowed:** false · **bare_retained_allowed:** false
- **B_AXIS_DERIVED:** false · **SECOND_PHYSICAL_CLOCK_EXCLUDED:** false ·
  **AUDIT_LEDGER_WRITTEN:** false · **NEW_AXIOM_ADDED:** false
- Independent audit lane is the sole status authority.

---

## 1. The exact thing tested

Block02 (`block02_section_N5.md` §1; unified no_go §6, lines 369–394) anchors the
N5 wall on:

> `T̂² = ⊗_p diag(1,e^{−2E(p)}) = exp(−2a_τ Ĥ)`, `Ĥ = Σ_p E(p) n_p`, with the
> claim that the generator tangent span `{n_p}` has **dimension `L_s`, not 1**, so
> "no commutant/center forces a single one-parameter orbit," and N5 closure needs
> an unsupplied **`(L_s−1)`-parameter physical-clock-admission ray**.

This route tests a precise reframe: **`Ĥ = Σ_p E(p) n_p` is a free (Gaussian)
fermion Hamiltonian, and `{n_p}` is its textbook free-fermion conserved-charge
tower.** The `L_s`-fold commuting span is therefore the *signature of
integrability* (the free/quadratic surface), not a generic feature of "A_min +
locality." The test: add a **minimal A_min-admissible local interaction**
`V = g Σ_x n_x n_{x+1}` (Quantum supplies `M_2(C)` per site; nothing forbids
interacting dynamics) and recompute the conserved-charge span. If it collapses
toward 1 (single conserved `H`), the corrected N5 is *conditional on
non-integrability* — far weaker than the `(L_s−1)`-param admission ray.

## 2. Method (native, recomputed, exact on finite blocks)

All load-bearing facts recomputed in-tree from the supplied dispersion
`E(p)=arcsinh(√(m²+sin²p))` and finite linear algebra (Jordan–Wigner second
quantization on a chain of `L` spinless-fermion sites). No load-bearing edge to
the conditional parent keystone, the unaudited cone, or the downstream consumer.

- **[LABEL]** Recompute `Ĥ` in real space: `Ĥ = Σ_xy h_xy c_x†c_y` is **quadratic**
  (resid 8.9e-16), `spec(h) = E(p)` (resid 2.8e-16); the block02 mode tower
  `{n_p}` all commute with `Ĥ` (max `‖[Ĥ,n_p]‖ ≈ 2e-16`), span dim `= L_s`. This
  *recovers block02's own fact* and names the object: free-fermion `H`, free
  charge tower.
- **[TOWER]** Add `V = g Σ_x n_x n_{x+1}` (periodic, `g=0.37`). Every block02 mode
  charge `n_p` **stops** commuting with `Ĥ_int` (min `‖[Ĥ_int,n_p]‖` = 0.185 at
  `L_s=4`, 0.165 at `L_s=5`; free value ~0). The **bilinear conserved-charge span
  collapses**: `L_s=4` free 8 → interacting 4; `L_s=5` free 9 → interacting **1**.
  Total number `N` survives (`[Ĥ_int,N]=0`) — the trivial on-site symmetry, not
  the tower.
- **[LOCAL]** The rigorous dichotomy computation: dimension of the space of
  **local** conserved charges = real span of Hermitian Pauli strings of bounded
  support (diameter ≤ `kmax`) that commute with `H` (commutant null space).
  - Supplied staggered surface, `L=6, kmax=3`: free local tower dim **8 → 2**.
  - Supplied staggered surface, `L=4, kmax=3`: free **8 → 6** (soft; the
    staggered `h` is even-range-4 so `Ĥ` itself leaks past `kmax=3`).
  - Clean nearest-neighbour free chain (`L=5, kmax=3`, where "local" is
    unambiguous): free **4 → 1** (cleanest collapse to the trivial survivor).
- **[ADMIN]** `V` is A_min-admissible: Hermitian (resid 0); `n_x=(I−Z_x)/2` is an
  on-site `M_2(C)` operator Quantum supplies (resid 0); number-preserving
  (`[V,N]=0`); `g` is a dimensionless dynamical coupling — **NOT** a
  `scale_reference` (no units), **NOT** a `kinetic_isotropy` datum (no `c_t=c_s`
  form), **NOT** a `realized_state` value (operator-level), **NOT** a selector.
  The tower breaks for every tested `g ∈ {0.01,0.1,1.0}` — generic, not
  fine-tuned.

## 3. The L_s=3 finite-size degeneracy (documented caveat, not a counterexample)

On a **3-site ring** the periodic NN sum `Σ_{x mod 3} n_x n_{x+1}` runs over every
pair (the ring *is* the complete graph `K₃`), so `V = (g/2)(N²−N)` is a function
of total number `N` alone (runner block `[L3DEGEN]`, resid 0) and therefore
trivially preserves the whole mode tower. A 3-site ring has no genuine
nearest-neighbour local interaction distinct from a number-only term. The
dichotomy requires `L_s ≥ 4`; the runner records this explicitly and uses
`L_s ∈ {4,5}` for the primary `[TOWER]`/`[ADMIN]` surfaces. (An *open* 3-site
chain already breaks the tower: min `‖[Ĥ_int,n_p]‖ = 0.247`.)

## 4. Honest OUTCOME — `shrinks_wall` + `corrects_overclaim`, NOT closure

**N5 is NOT closed.** A_min supplies **no dynamics** (the emergent-dynamics OPEN
GATE of `MINIMAL_AXIOMS_2026-06-05`), so we cannot assert the emergent dynamics
*is* non-integrable. What the route establishes, runner-backed:

1. **The `(L_s−1)`-param "admission ray" is the free-fermion charge tower of the
   SPECIAL (integrable, measure-zero) free surface — not a generic A_min
   obstruction.** `Ĥ` is provably a free-fermion `H` and `{n_p}` is its standard
   charge tower (block `[LABEL]`).
2. **A generic A_min-admissible local interaction collapses the tower.** The
   block02 mode tower is destroyed (no `n_p` survives) and the local / bilinear
   conserved-charge span drops toward the trivial survivors `{I, N, H}` (blocks
   `[TOWER]`,`[LOCAL]`). The interaction is genuine A_min-admissible dynamics, no
   new axiom/primitive (block `[ADMIN]`).
3. **Corrected N5:** *the multi-clock freedom is the free/integrable signature; a
   generic (non-integrable) A_min-admissible dynamics collapses the tower to a
   single clock. N5 holds **conditional on non-integrability** of the emergent
   dynamics — which is far weaker than the `(L_s−1)`-parameter admission ray
   block02 implied.* Non-integrability is a one-bit generic-position premise, not
   an `(L_s−1)`-dimensional bespoke datum.

This **shrinks the wall** (the residual freedom is one open bit — "is the emergent
dynamics integrable?" — not `L_s−1` free parameters) and **corrects the block02
overclaim** that the `L_s`-fold factorization is the *generic* obstruction. It is
a **conditional shrinkage, not a closure**: dynamics is an open gate.

**Realized-state / counterfactual discipline.** The collapse is an
operator-algebra statement about the conserved-charge **span**, NOT evaluated at
any realized state; it is invariant over the law-admissible dynamics family (the
free surface is one law-admissible dynamics; a generic interacting dynamics is
another). No averaging, no "generic state" specialization predicate — "generic"
here qualifies the *dynamics (the law)*, which is exactly the open gate, not a
state. Counterfactual-safe.

## 5. Correction to the unified no_go (block02 amendment)

`corrects_block02 = yes`. The unified no_go §6 (lines 369–394) and
`block02_section_N5.md` §1/§5 should carry the sharpened statement:

> The supplied `T̂² = ⊗_p diag(1,e^{−2E(p)})` is a **free-fermion** transfer
> matrix and `{n_p}` is its **free-fermion conserved-charge tower**; the
> `L_s`-fold commuting span is the **signature of the free/integrable surface**,
> not a generic A_min obstruction. A minimal A_min-admissible local interaction
> `V = g Σ_x n_x n_{x+1}` destroys the tower (every `n_p` ceases to commute; the
> local/bilinear conserved-charge span collapses toward `{I,N,H}`). The corrected
> N5 wall is therefore: **N5 holds conditional on non-integrability of the
> emergent dynamics** — a one-bit generic-position premise, *not* an
> `(L_s−1)`-parameter physical-clock-admission ray. The residual relocates to the
> SAME emergent-dynamics OPEN GATE, but the missing supplier shrinks from an
> `(L_s−1)`-parameter ray to a single non-integrability bit. N5 stays a LIVE wall
> (dynamics unsupplied); no closure, no new axiom.

The block02 "`(L_s−1)` undetermined parameters" wording is the **overclaim**: that
count is the dimension of the *free* tower; under any generic A_min-admissible
dynamics it is not the residual freedom. Keep the relocation-to-open-gate
conclusion; replace the `(L_s−1)`-param framing with the non-integrability-bit
framing.

## 6. Scope caveats this section must carry

- **Dynamics gate is open.** The collapse holds *for a generic A_min-admissible
  interacting dynamics*; A_min supplies none, so this is conditional, not a
  derivation of N5. The honest residual is "is the emergent dynamics
  integrable?" — unresolved.
- **Finite-block scope.** Computations are exact on small finite chains
  (`L ∈ {4,5,6}`, `kmax ≤ 3`). The free tower is *extensive* (grows with `L` and
  `kmax`); the collapse is monotone but the interacting residual at small
  `kmax`/`L` includes lattice-symmetry survivors (`I,N,H`-type), not a continuum
  claim. `L_s=3` ring is degenerate (§3).
- **`L_s=3` is excluded** from the primary surfaces (complete-graph degeneracy).
- **Literature is precedent, not authority.** The dichotomy
  (arXiv:2504.14315 / 2302.12804 / 2402.08924) is cited as the *precedent* that
  this collapse is generic; the load-bearing fact is the in-tree runner, not an
  imported theorem.
- **Conditional parent unchanged.** The keystone 2026-05-03 stays
  audited_conditional with B-AXIS.3 live; this section sharpens the obstruction
  shape, it does not change status. Independent audit lane is sole authority.

**One line:** `Ĥ = Σ_p E(p) n_p` is a free-fermion `H` whose `L_s`-fold commuting
tower `{n_p}` is the integrable free-fermion charge tower (not a generic A_min
obstruction); a minimal A_min-admissible local interaction `g Σ_x n_x n_{x+1}`
destroys the tower (every `n_p` decommutes; local/bilinear conserved-charge span
collapses toward `{I,N,H}`, e.g. `L_s=5` bilinear 9→1, `L=6/kmax=3` local 8→2,
clean NN 4→1), so the corrected N5 holds **conditional on non-integrability** — a
one-bit premise far weaker than block02's `(L_s−1)`-param admission ray — which
**shrinks the wall and corrects the block02 overclaim** without closing N5 (the
dynamics gate stays open); runner PASS=37 FAIL=0.
