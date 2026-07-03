# The 3+1 Constraint/Multiplier Structure of the Linearized EH Target Operator: the Derived Non-Degenerate (Lambda-One) Fiber Metric Exists, the Comparator Signs Are Derived, and the Trace Channel Is Constrained, Not Glued

**Date:** 2026-06-09
**Claim type:** bounded_theorem / target-operator structure certificate
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_3plus1_constraint_fiber_metric_2026_06_09.py`](../scripts/frontier_universal_gr_3plus1_constraint_fiber_metric_2026_06_09.py) (PASS=9 FAIL=0, exact sympy)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_3plus1_constraint_fiber_metric_2026_06_09.txt`](../logs/runner-cache/frontier_universal_gr_3plus1_constraint_fiber_metric_2026_06_09.txt)

## Scope (engages the actual no-go texts at their stated boundaries)

The degenerate-supermetric sign no-go
([`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO...`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md))
proves: degenerate trace=shear fiber signs + the derived gluing law `ω²=V/G` + **supplied**
opposite-signed comparator potentials ⟹ one channel unhealthy. Its own N1/N6 name the open bypass:
*"a derived non-degenerate fiber metric"* (its λ=1 control passes its T3 inside the same law). The
gluing derivation
([`UNIVERSAL_GR_QUADRATIC_MODE_GLUING_DERIVATION...`](UNIVERSAL_GR_QUADRATIC_MODE_GLUING_DERIVATION_NARROW_THEOREM_NOTE_2026-06-09.md))
states its hypothesis: *"a diagonal bounded channel with quadratic Lagrangian `L = ½G q̇² − ½V q²`"*.
The retained records-route supermetric
([`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md`](UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md))
is all-negative and trace=shear degenerate. The landed R3 row
([`R3_GEOMETRIC_REGGE_LINEARIZATION...`](R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md))
is a target-operator certificate that explicitly does **not** supply the 3+1 kinetic/multiplier split.
This note supplies exactly that split, for the same target operator, and answers the no-go's bypass
question. The 3+1 lapse/shift channel-weight probe is the TT-kernel row's named next probe
([`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING...`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md)).

## Results (all derived in-runner from the metric/curvature definitions; exact sympy)

1. **Anchor (A1).** The linearized Einstein operator built from the curvature definitions reproduces
   the landed R3 facts identically in `(ω,k)`: gauge modes `h = p⊗ξ + ξ⊗p` are exact zero modes
   (symbolically, all ξ), and `G(h_TT) = ½(k²−ω²) h_TT` — at `ω=0` the landed `+k²/2`.
2. **Multiplier structure, scheme-independent (A2).** Writing every second derivative as a formal
   symbol `S(μ,ν)`: the constraint rows `G^{00}`, `G^{0i}` have **zero coefficient on `S(0,0)`** (no
   `q̈` in any constraint row — the trace-reversal cancels them), and `G^{00}` contains **no**
   time-derivative symbol at all. A zero polynomial stays zero under **any** stencil substitution: the
   lapse/shift multiplier structure is **discretization-robust** (structural).
3. **The derived non-degenerate fiber metric (A3) — the no-go's named bypass.** The kinetic
   coefficient `c₂ = +coeff(G^{ij}, S(0,0))` in the tensor pairing has the λ=1 DeWitt pattern:
   `K_trace : K_TT = −1 : +½ = −2 : +1` (indefinite, non-degenerate; both TT channels equal), with
   **zero** lapse/shift kinetic weights. This is a *different object* from the retained records-route
   supermetric (all-negative, degenerate).
4. **The derived comparator potential signs (A4).** At `ω=0` the same operator gives `V_TT = +k²/2`
   and `V_trace(transverse) = −k²/2` — the no-go's **supplied** pair, now derived.
5. **Gluing with both halves derived (A5).** `ω²_TT = V/K = +k²` and `ω²_trace = (−k²/2)/(−½) = +k²`
   — the no-go's λ=1 control (its T3) reproduced with derived inputs: the obstruction is **bypassed
   exactly through the route its N1/N6 left open**.
6. **The constraint content (A6).** `G^{00} = +(k²/2)(h_yy+h_zz)` **exactly** (k‖x; every other
   component absent): the linearized Hamiltonian constraint is `k² ×` (transverse trace). In vacuum at
   `k≠0` it forces that channel to zero — the trace is **not** a free *"diagonal bounded channel"*, so
   the gluing law's hypothesis does not apply to it in the constrained 3+1 system (the channel is
   **eliminated, not glued**).
7. **DOF count (A7, exact rank algebra).** At generic `ω²≠k²` the kernel of the full 10×10 operator is
   exactly the 4-parameter gauge family; at `ω²=k²` it is 4+2: precisely **two propagating physical
   modes, both TT**, healthy dispersion.
8. **Discrete transcription (A8;** [`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
   `c_t=c_s`; **declared symmetrized stencils).** The multiplier structure holds verbatim on the
   lattice (`G^{00}` row ω-free entirely; constraint rows have no even-ω kinetic term); the discrete TT
   dispersion is `4sin²(ω/2) = 4sin²(k/2)`, i.e. `ω = ±k` **exactly** across the BZ (healthy, no extra
   branch); the continuum-form gauge mode has a nonzero lattice residual at finite `k` — the measured
   lattice diffeomorphism-breaking, `|G(h_gauge)| ~ p⁵` (order `2^{4.99}` per halving).
9. **Tie-in (A9, both landed rows respected).** Gluing the derived potentials with the **retained
   records-route supermetric** weights reproduces the no-go's negative product (the no-go **binds that
   gluing** — correct at its scope); gluing with the **derived geometric fiber metric** gives a positive
   product. The no-go is a correct boundary on the records-Hessian gluing specifically; the geometric
   target operator carries its own healthy non-degenerate gluing.

## What is and is not claimed

- **Is:** for the linearized EH **target operator** (the same object as the landed R3 certificate),
  the 3+1 kinetic fiber metric is derived and is the indefinite λ=1 DeWitt form; the comparator
  potential signs are derived; the gluing with both halves derived is healthy in both channels; the
  trace channel is constrained (eliminated, not glued — the gluing theorem's hypothesis does not reach
  it); the multiplier structure is scheme-independent and survives the symmetric `Z³×Z_τ` transcription
  verbatim; the exact physical content is 2 TT modes with healthy dispersion, discrete included.
- **Is not:** this note does **not** derive the geometric **action** from the framework (the
  Einstein/Regge glue, the edge-length degrees of freedom, and the action selection remain open — the
  retained supermetric note's own frontier and the R3 row's guardrails); does **not** compute the
  cubic-Coxeter Regge second variation
  ([`CUBIC_COXETER_REGGE_DEFICIT_VANISHING...`](CUBIC_COXETER_REGGE_DEFICIT_VANISHING_NARROW_THEOREM_NOTE_2026-05-10.md)
  cited as context); does **not** overturn the degenerate-supermetric no-go (it **confirms** it at its
  stated scope and exhibits the bypass its own gate names); does **not** address the source-coupling
  sign (`sign(G_Newton)` — a separate located residual per the arrow/stability/spectral no-go row);
  adds no axiom, no primitive, no fitted value.

## Boundaries (honest)

- **Linearized / abelian-gauge scope only.** Nonlinear constraint closure on discrete time is a known
  hard problem in discrete gravity (consistent-discretization literature, cited as context only) and is
  not addressed; the framework's nonlinear completion remains separately open.
- **The discrete part is a declared-stencil transcription** of the target operator (symmetrized
  stencils stated in-runner), not a derivation of a discrete action; the measured `~p⁵` gauge residual
  quantifies the transcription's diffeomorphism-breaking at finite `k`.
- **Target-operator status.** Everything here is structure *of the target operator* a geometric route
  must reproduce — the framework-native derivation of that operator is the open item, unchanged.
- The matter-route comparison is not used as an input here. The in-review full-channel-table row
  (PR #3435) is context only and is not a load-bearing dependency of any check in this note.

## Load-bearing inputs

- [`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md) — the no-go whose named bypass (N1/N6) this note exhibits; its negative product is reproduced (A9).
- [`UNIVERSAL_GR_QUADRATIC_MODE_GLUING_DERIVATION_NARROW_THEOREM_NOTE_2026-06-09.md`](UNIVERSAL_GR_QUADRATIC_MODE_GLUING_DERIVATION_NARROW_THEOREM_NOTE_2026-06-09.md) — the derived gluing law used in A5/A9; its stated hypothesis is what A6 shows the trace channel fails.
- [`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md`](UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md) — the retained records-route supermetric weights used in A9 (the bound gluing).
- [`R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md`](R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md) — the landed target-operator anchor (A1 reproduces its facts identically in `(ω,k)`).
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md) — names the 3+1 lapse/shift channel-weight probe this note performs.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — grants `c_t=c_s` for the symmetric discrete transcription (A8); nothing beyond its declared structural grant is used.

## Forbidden-imports check

No PDG / fitted / literature value is consumed. The linearized Einstein operator is derived in-runner
from the metric/curvature definitions (standard differential geometry, reproven symbolically); the
DeWitt λ=1 pattern, the comparator signs, and the constraint content are outputs, not inputs. The
ADM/constraint vocabulary and the consistent-discretization caveat are cited as context only; no
formula from them enters any check.
