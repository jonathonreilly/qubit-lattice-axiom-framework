# Microcausality / Lieb-Robinson Bound on the Lattice and Quantum Baseline

**Date:** 2026-05-01 (2026-05-09: bounded action-support/J-bound support added; 2026-06-10: exact-log free-bilinear quasilocal LR repair)
**Type:** bounded_theorem
**Claim scope:** equal-time strict locality `[O_x, O_y] = 0` for `x != y` on the one-site tensor structure (M1); finite-velocity Lieb-Robinson bounds in the overlap-weight convention for (i) the finite-range hopping/action carrier and (ii) the free (`U = 1`) bilinear two-step exact logarithmic Hamiltonian with exponentially decaying kernel (M2); continuum spacelike microcausality only as a sector-scoped scaling corollary when the matching Lorentz scaling bridge is also supplied (M3). Gauged/interacting exact-log locality and full continuum QFT microcausality are outside this row.
**Status authority:** independent audit lane only. This source note does not set or predict audit status.
**Runner:** `scripts/axiom_first_microcausality_check.py`
**Cache:** `logs/runner-cache/axiom_first_microcausality_check.txt`

## Scope

This note packages the lattice microcausality statements that currently close
from the framework baseline and the cited sector bridges. The result has
three parts:

**(M1) Equal-time strict locality.** For any two distinct lattice
sites `x ≠ y` and any operators `O_x, O_y` supported at those sites,
`[O_x, O_y] = 0` strictly. This is a one-line consequence of the Quantum
axiom's tensor product structure.

**(M2) Lieb-Robinson lightcone.** For operators `O_x, O_y` at sites
`x, y`, two sector-scoped finite-velocity statements are now supplied:

- **(M2a) finite-range carrier:** the support-family bridge gives
  a finite-range LR bound with the overlap-weight velocity
  `v_LR = 2 e q W R` on the finite-range hopping/action carrier;
- **(M2b) free exact-log carrier:** the free bilinear two-step
  `H = -log(T_hat^2)/(2 a_tau)` is quasilocal, not finite range, and the
  2026-06-10 bridge gives, for `0 < d mu < eta < arcsinh(m)`,

```text
    ||[alpha_t(O_x), O_y]||
      <= 2 ||O_x|| ||O_y|| exp(-mu d_1(x,y) + 4 W_mu |t|),              (1)
```

where `W_mu` is the finite exponential weighted overlap of the exact-log
hopping kernel. Equivalently `v_mu = 4 W_mu / mu` is finite. In both
readings, the commutator is exponentially small outside the corresponding
effective lightcone. The gauged/interacting exact logarithm is not closed by
this note.

In the continuum-limit identification `t_phys = t · a_tau`,
`d_phys = d · a_s`, and finite LR slope `v · a_s / a_tau -> c` on a
sector-matching Lorentz scaling surface, this gives the usual
spacelike-commutator limit inside the same sector. This is a scaling
corollary, not an interacting Wightman-axiom theorem.

This note therefore closes a bounded lattice lightcone surface and the
free-bilinear exact-log repair, complementing the spatial
cluster-decomposition theorem. It does not close the gauged/interacting
exact-log frontier.

## Framework Baseline And Supplied Inputs

- **Lattice.** Supplies the `Z^3` nearest-neighbor graph metric
  `d(x, y)`.
- **Quantum.** Supplies the finite one-qubit operator algebra at each site,
  equivalently `M_2(C) ~= Cl(3,0)`, and the finite-block tensor product.
  This is the only baseline axiom used in (M1).
- **Record.** Not used. No readout context, central-sector decomposition,
  weighting, normalization, probability rule, measurement dynamics, or
  recorded outcome enters this row.
- **Finite-range hopping/action carrier.** Supplies the sector carrier for
  (M2a): nearest-neighbor staggered hopping/Wilson terms and one-plaquette
  gauge-action support have finite support in the lattice graph metric.
- **Free exact-log carrier.** Supplies the sector carrier for (M2b): the
  free (`U = 1`) two-step exact logarithmic Hamiltonian is exponentially
  quasilocal, not finite range.

## Cited Inputs

- **RP transfer matrix.** From the [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md),
  `T : H_phys → H_phys` is Hermitian, positive, and bounded. The
  Hamiltonian `H = -log(T) / a_τ` is well-defined and bounded below.
- **Spectrum condition.** From the [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md),
  `H` on `H_phys` is bounded operator with finite spectral norm
  (since `H_phys` has finite dimension on any finite block, by RP
  reconstruction).
- **Exact-log free bilinear quasilocality and LR composition.** From
  [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md),
  the free two-step exact logarithm is an exponentially quasilocal bilinear
  support family and is not finite range. From
  [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md),
  that weighted kernel yields a finite-velocity LR envelope in the same free
  sector.

## Statement

Let `Λ` be a finite lattice block with one-site algebra supplied by the
current Quantum axiom. Then:

**(M1) Equal-time strict locality.** For any two distinct lattice
sites `x, y ∈ Λ` with `x ≠ y` and any operators `O_x, O_y` supported
at these sites,

```text
    [O_x, O_y]  =  0  (exactly)                                              (2)
```

**(M2a) Finite-range support-family lightcone.** For any finite-range support
family `H = Σ_Z h_Z` with support size `q`, support diameter `R`, and
per-site overlap weight `W`, the cited bridge gives

```text
    v_LR := 2 e q W R,                                                       (3)
```

and the corresponding exponential commutator envelope. Applied to the
hopping-bilinear/action carrier, this is the finite-range lattice lightcone
this row may cite.

**(M2b) Free exact-log quasilocal lightcone.** In the free bilinear two-step
sector, let `H = -log(T_hat^2)/(2 a_tau)` and let `W_mu` be the finite
weighted overlap from the free-bilinear quasilocal LR bridge. Then for any
`0 < d mu < eta < arcsinh(m)` and one-site observables,

```text
    ||[alpha_t(O_x), O_y]||
      <= 2 ||O_x|| ||O_y|| exp(-mu d_1(x,y) + 4 W_mu |t|).                 (4)
```

Equivalently, `v_mu = 4 W_mu / mu` is a finite sector speed. The exact log is
quasilocal rather than finite range; the strict `R <= 2` exact-log statement
is false on this sector.

**(M3) Sector-scoped continuum-limit microcausality.** In a sector where the
finite LR slope `v · a_s / a_tau -> c < infinity` is tied to a matching
Lorentz scaling surface
([`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
[`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md)),
the lattice bound becomes strict for spacelike-separated continuum points in
that same sector. This does not assert gauged/interacting exact-log locality
or full continuum QFT microcausality.

Statements (M1)–(M3), with these boundaries, constitute the current bounded
framework microcausality surface.

## Proof

### Step 1 — Equal-time strict locality (proves M1)

By the Quantum axiom, each lattice site carries a finite one-site operator
algebra and distinct sites enter the finite-block tensor product as distinct
tensor factors. The full lattice operator algebra on a finite block `Λ` is
the tensor product

```text
    A(Λ)  =  tensor_{z in Λ} A_z
```

Operators `O_x in A_x` and `O_y in A_y` with `x != y` are then
of the form `O_x = (...) ⊗ a ⊗ (...)` and `O_y = (...) ⊗ (...) ⊗ b ⊗ (...)`
where `a` lives in the `x`-th tensor factor and `b` in the `y`-th
tensor factor. They commute trivially:

```text
    O_x · O_y  =  (... a ⊗ b ...)  =  O_y · O_x                             (6)
```

This proves (M1) for ordinary one-site observables. For staggered fermion
generators, the corresponding locality statement is the graded commutator
`[O_x, O_y]_± = O_x O_y - (-1)^{|O_x| |O_y|} O_y O_x = 0`. ∎

### Step 2 — finite-range and quasilocal LR bounds (proves M2)

The previous version of this note used the stale constant `v_LR = 2 e r J`
and asserted that the exact logarithmic Hamiltonian was finite range. Both
parts are superseded.

**M2a.** The finite-range bridge
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
proves the finite-range support-family LR lemma directly. In that convention
the load-bearing inputs are support size `q`, support diameter `R`, and
per-site overlap weight `W`, and the velocity is

```text
    v_LR = 2 e q W R.
```

This closes the finite-range hopping/action-carrier LR bound; the old
`2 e r J` expression should not be used downstream.

**M2b.** The transfer-matrix log-quasilocality theorem proves that the free
two-step exact log Hamiltonian is exponentially quasilocal and not finite
range. The new bridge
[`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
then performs the missing weighted-path composition: for
`0 < d mu < eta < arcsinh(m)`, the exact-log kernel has finite weighted
overlap `W_mu`, and

```text
    ||[alpha_t(O_x), O_y]||
      <= 2 ||O_x|| ||O_y|| exp(-mu d_1(x,y) + 4 W_mu |t|).
```

This is a finite lightcone with `v_mu = 4 W_mu / mu`. It is deliberately
sector-scoped: free (`U = 1`) bilinear two-step exact log only. The
gauged/interacting logarithm remains an open bridge. ∎

### Bounded action-support/J-bound support (added 2026-05-09)

The Step 2 argument above takes the finite-range structure of `H = Σ_z h_z`
and the local-density operator-norm `J = sup_z ‖h_z‖_op` as inputs. A
2026-05-05 audit review flagged that these inputs were **asserted** rather
than **derived**: the cited RP/spectrum authorities supply positivity /
self-adjointness / boundedness of the reconstructed `H`, but not the
locality structure needed for Lieb-Robinson, nor an explicit `v_LR`
derivation.

The companion bridge note
`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
narrows that gap. It proves three bounded statements directly from the
canonical action coefficients (the same coefficients that the parent RP
note's eqs. (1) and (2) record, not from any new spectral input):

**(F1) Leading action-density support.** The action `S = S_F + S_G`
(parent RP note eqs. (1)–(2)) couples either single sites (mass term),
NN sites (staggered hop, Wilson term), or four sites in a single
elementary plaquette (Wilson plaquette). This gives bounded support
`r_action <= 2` in the site `l1` metric for the leading local
action-density pieces. It does not prove that the exact logarithmic
Hamiltonian `H = -log(T)/a_tau` is finite range.

**(F2) Explicit action-density J and overlap-weight budgets.** The
repaired bridge uses the plaquette coefficient `2β`: the `1/N_c`
belongs inside the trace average, not in the exterior coefficient.
Its displayed bound is

```text
    J_action <= (d/2) · 1 + r_W · d + |m| + 2β · q_face,
```

with `q_face = d(d-1)/2`. On the canonical surface
(`d = 4, r_W = 1, β = 6, N_c = 3`) this gives the supplied-surface
budget `J_max = |m| + 78`. The same bridge also brackets the
carrier-faithful Wilson reading and all-direction envelope:
`J_max^carrier = |m| + 78.5` and `J_max^envelope = |m| + 80`.
All three are finite and gauge-background-independent; the older
double division by `N_c` is superseded.

The LR lemma does not consume `J_action` directly. Its local input is
the per-site overlap weight `W = sup_x Σ_{Z ∋ x} ‖h_Z‖_op`. For the
same carrier family the bridge proves

```text
    W_surface = |m| + 296,
    W_carrier = |m| + 298,
    W_envelope = |m| + 300.
```

**(F3) Conditional Lieb-Robinson velocity.** If the exact reconstructed
Hamiltonian has a finite-range/quasilocal decomposition with compatible
support and overlap weight, the in-repo finite-range bridge gives the
overlap-weight velocity `v_LR = 2 e q W R`. The older `2 e r J`
summary is superseded because it omitted the per-site overlap weight;
under the envelope branch the conditional finite-range ceiling is
`v_LR <= 16·e·(|m| + 300)`.

The bridge note's runner `scripts/microcausality_finite_range_h_bridge_2026_05_09.py`
verifies (F1) on a finite-range toy action-density carrier, (F2) by
computing `‖h_z‖_op` on 20 random SU(3) backgrounds and comparing
against the repaired conservative `J_max`, (F2b/F2c) by checking the
`78 <= 78.5 <= 80` branch arithmetic and `296/298/300` overlap
weights, (F3) by verifying the proved Lieb-Robinson bounds on a
finite-range Hamiltonian, and (F4) outside-lightcone exponential decay.

**Consequence for the load-bearing claim.** The action-support and
coefficient/norm pieces are no longer asserted. The finite-range LR constant
is the overlap-weight constant of the finite-range bridge, and the free bilinear
exact-log sector is repaired by the 2026-06-10 quasilocal LR bridge. What
remains open is the gauged/interacting exact-log locality bridge.

### Step 3 — sector-scoped continuum microcausality (proves M3)

In the lattice -> continuum limit `a -> 0` with finite sector LR speed `v`
satisfying `v · a_s / a_tau = c < infinity` on a sector-matching Lorentz
scaling bridge
([`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
[`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md)),
spatial graph distance `d_phys = d · a_s` and time
`t_phys = t · a_tau` satisfy
`v |t| = c |t_phys| / a_s`. The Lieb-Robinson exponent
becomes

```text
    - d(x, y) + v |t|  =  - d_phys / a_s + c |t_phys| / a_s
                       =  (1 / a_s) · (- d_phys + c |t_phys|)
```

For spacelike separation `d_phys > c |t_phys|`, the exponent is
`- (d_phys - c |t_phys|) / a_s -> -infinity` as `a_s -> 0`, so the commutator
vanishes strictly in the same sector. This is the standard relativistic
microcausality limiting form, but it is only as broad as the lattice
lightcone and Lorentz-scaling inputs it consumes. ∎

## Hypothesis Set Used

- Lattice (`Z^3` nearest-neighbor graph metric).
- Quantum (one-site finite operator algebra and finite-block tensor product).
- Record is not used.
- finite-range hopping/action support-family carrier for M2a.
- free bilinear two-step exact-log kernel and weighted-overlap LR bridge for M2b.
- RP transfer matrix (defines H_phys).
- Spectrum condition (H bounded operator with finite J).
No fitted parameters. No observed values used as proof inputs. No
gauged/interacting exact-log locality is consumed.

## Corollaries

C1. **Spatial cluster decomposition refinement.** Combined with
[`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md),
(M1)+(M2) refine the *spacetime* decay rate of connected
correlators on the framework: `<O_x α_t(O_y)>_c → 0` exponentially in
`d(x, y) - v |t|`, in whichever M2 sector supplies the finite velocity.

C2. **Causal asymptotic local algebras.** The local algebras
`A(O) := { observables localized in spacetime region O }`
satisfy `[A(O_1), A(O_2)] = 0` for any two regions `O_1, O_2` with
spacelike separation in the sector-scoped continuum limit.

C3. **No-superluminal-signaling on the framework.** Any signaling
protocol from `x` at `t = 0` to `y` at time `t` requires
`d(x, y) ≤ v · t` for the relevant sector velocity. This is the lattice analogue of the
no-faster-than-light-signaling principle.

C4. **Reeh-Schlieder cyclicity premise.** The local algebras built
from microcausal operators are the inputs to the Reeh-Schlieder
theorem (Block 08), which would prove cyclicity of the vacuum vector
for any nonempty open region.

## Honest status

**Bounded source theorem on current Lattice/Quantum premises plus cited
sector bridges.** (M1)–(M3) are derived from:

- Lattice and Quantum, named explicitly above;
- the finite-range support-family LR bridge for M2a;
- the exact-log quasilocality theorem plus the 2026-06-10
  free-bilinear quasilocal LR bridge for M2b;
- RP (defines H, H_phys);
- spectrum condition (H bounded);
- Lorentz scaling notes for M3 only when the same sector velocity is
  being scaled.

The original runner verifies the finite-range lattice Lieb-Robinson bound on a
small block. The 2026-06-10 bridge runner verifies the exact-log quasilocal
weighted-overlap constants and finite-matrix commutator envelope in the free
bilinear sector.

**Honest claim-status fields:**

```yaml
actual_current_surface_status: support
conditional_surface_status: bounded theorem over finite-range carrier plus free-bilinear exact-log sector
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "No new axiom is proposed; gauged/interacting exact-log locality remains open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Not in scope.**

- Gauged/interacting exact-log locality and full Wightman-style continuum
  microcausality. We prove the finite lattice lightcone surfaces currently
  supported in-repo.
- Promotion to retained / Nature-grade in the canonical paper
  package. Independent audit required.

## Citations

- current minimal axioms: [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- RP support note:
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
- spectrum-condition support note:
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
- cluster-decomposition note:
  [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- 2026-05-09 overlap-weight finite-range LR bridge:
  [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
- exact-log free-bilinear quasilocality:
  [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
- 2026-06-10 exact-log free-bilinear quasilocal LR bridge:
  [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
- emergent Lorentz scaling inputs:
  [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
  [`LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md`](LORENTZ_KERNEL_POSITIVE_CLOSURE_NOTE.md)
- standard references (context only; no constant imported after the
  in-repo bridges):
  Lieb-Robinson (1972) *Comm. Math. Phys.* 28, 251;
  Hastings (2004) *Phys. Rev. B* 69, 104431;
  Nachtergaele-Sims (2010) in *New Trends in Mathematical Physics*,
  Springer, p. 591.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by the
audit verdict so the audit citation graph can track them. It does not promote
this note or change the audited claim scope.

- [microcausality_finite_range_h_and_vlr_bridge_theorem_note_2026-05-09](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  (overlap-weight finite-range LR bridge; supersedes `2 e r J`).
- [TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
  (free-bilinear exact-log quasilocal kernel and strict finite-range failure).
- [FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
  (new one-hop bridge composing the exact-log quasilocal kernel into a finite
  LR envelope in the free bilinear sector).
