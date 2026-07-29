actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "the live ledger remains audited_conditional until the source change lands and an independent re-audit is applied"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The theorem is algebraic under an explicitly fixed coordinate convention; the convention remains a named condition rather than a derived physical fact."
audit_required_before_effective_retained: true
bare_retained_allowed: false
no_go_discipline_status: pass_for_bounded_scope_only
no_go_discipline_reason: N1-N8 stress-test four collapsed scope walls; no route-independent negative is claimed

# Certificate checks

- No open physics import was added.
- The coordinate convention and unit spacing remain explicit.
- The continuum comparison remains non-load-bearing.
- The runner checks dependency classes and the theorem's source boundary.
- Review-loop disposition is `pass`.
- Independent audit is still required before the repository may treat the row
  as retained-grade.

## No-Go Discipline N1-N8 — bounded scope

The positive claim is the three-dimensional identity
`vol([-pi,pi]^3)=(2pi)^3` and its Haar-probability normalization under the
stated `Z^3`, unit-spacing, and Fourier-pairing convention.  The note's
negative-looking sentences are boundaries on what this identity supplies, not
claims that broader derivations are impossible.

### N1 — mechanism-distinct routes

1. **Pontryagin-dual route — `ATTEMPTED`.**  Dualize `Z^3` to `T^3`, invoke
   normalized Haar uniqueness, and read the coordinate density.  This is the
   theorem's analytic proof route.
2. **Finite-character route — `ATTEMPTED`.**  The runner checks one-dimensional
   character orthogonality and direct/product three-dimensional sums at
   several nontrivial momenta.  This independently exercises the dual-group
   normalization at finite cutoff.
3. **Product-volume route — `ATTEMPTED`.**  Exact symbolic integration gives
   `2pi`, `(2pi)^2`, and `(2pi)^3` before any continuum comparison.  This is a
   geometric measure calculation rather than character algebra.
4. **Probability/quadrature route — `ATTEMPTED`.**  Constant-density Riemann
   sums at four grids integrate `1/(2pi)^3` to one.  This is a numerical
   normalization check with a distinct failure mode.
5. **General reciprocal-covolume route — `UNTESTED AND OPEN`.**  For
   `L=A Z^3`, derive the dual fundamental volume `(2pi)^3/|det A|` and recover
   this row at `A=I`.  That would expose lattice scale and basis dependence
   rather than silently fixing unit spacing.
6. **Four-dimensional regulator/Wick route — `UNTESTED AND OPEN`.**  Specify a
   temporal lattice or regulator and prove the corresponding four-dimensional
   measure and continuation.  The present three-dimensional theorem neither
   executes nor forecloses this route.

The routes use group duality, finite sums, product measure, quadrature,
reciprocal-lattice determinants, and regulated dimensional extension.  The
two open routes forbid a route-independent negative conclusion.

### N2 — collapsed walls and pairwise independence

The source boundaries collapse to four walls: `W_U` (unit spacing,
fundamental-domain coordinate, and `exp(i k.x)` convention); `W_H` (the
textbook Pontryagin-duality and Haar-uniqueness suppliers are given rather
than derived from the minimal axioms); `W_4` (four-dimensional measure and
Wick/regulator extension); and `W_B` (downstream composition with the `4pi`
factor, gauge normalization, Wilson matching, or a hierarchy primitive).

| Pair | first does not close second because | second does not close first because |
|---|---|---|
| `W_U`, `W_H` | choosing coordinates does not prove duality/Haar uniqueness | the abstract theorem does not choose unit or exponent convention |
| `W_U`, `W_4` | a 3D convention does not supply temporal continuation | a 4D regulator can retain an independent scale convention |
| `W_U`, `W_B` | fixing `(2pi)^3` does not derive other constants | a downstream bridge does not derive this coordinate normalization |
| `W_H`, `W_4` | compact-group Haar theory does not choose a Wick regulator | a regulator does not derive Pontryagin/Haar facts |
| `W_H`, `W_B` | harmonic analysis alone does not supply gauge/hierarchy inputs | a parameter bridge does not prove the Haar normalization |
| `W_4`, `W_B` | a 4D measure does not derive `g`, `4pi`, or Wilson matching | those parameters do not construct Wick rotation or a regulator |

All six unordered pairs have distinct terminal obligations.  This is an
independence audit of the scoped tasks, not an assertion that the walls are
fundamental.

### N3 — hidden-wall scan

The note and runner were scanned for “standard,” “same,” “unit,” “given,”
“uniquely determined,” “convention,” and “structural coincidence.”  Unit
lattice spacing, `[-pi,pi]^3`, and the no-extra-`2pi` exponential map to
`W_U`; textbook Pontryagin/Haar facts map to `W_H`; every 4D/Wick/regulator
sentence maps to `W_4`; and the `4pi`, `g`, generator, Wilson, and hierarchy
sentences map to `W_B`.  No fifth derivational wall is hidden by rhetoric.

### N4 — exact residual matching

The audit residual is runner evidence transport, not a missing identity.  The
new source-bound runner emits exactly 55 labelled passes, zero failures, and
4,831 characters with no clipping marker; its live stdout equals the fresh
cache byte-for-byte.  The note hash and input fingerprint force a current
rerender.  None of `W_U`-`W_B` is described as repaired.

### N5 — resolution and rhetoric audit

- **Per axis:** the exact interval length is `2pi`.
- **Three-torus:** product measure gives `8pi^3=(2pi)^3`.
- **Finite grids:** `N=16,32,64,128` quadrature checks only the constant
  normalization and is not an asymptotic field-theory theorem.
- **Coordinate resolution:** the density is stated in the named unit-spacing
  `d^3k` coordinate; no dimensionful lattice-scale claim is smuggled in.
- **Dimensional resolution:** three-dimensional BZ normalization is not
  promoted to a four-dimensional loop/Wick statement or hierarchy closure.

### N6 — primitive and convention paths

The framework supplies the `Z^3` substrate through the minimal-axiom surface;
Pontryagin duality and Haar uniqueness remain disclosed textbook inputs.  A
general `A Z^3` covolume theorem is the clean route to exposing scale/basis
dependence.  Existing 4D regulator and hierarchy no-go notes remain context,
not premises that upgrade this positive row or make the open routes
impossible.

### N7 — strongest actionable steelman

Prove one coordinate-explicit theorem for every full-rank lattice
`L=A Z^n`: its dual fundamental cell has volume
`(2pi)^n/|det A|`, and normalized Haar density is
`|det A| d^n k/(2pi)^n` under a declared Fourier pairing.  Test it symbolically
for nonorthogonal integer/rational `A`, with wrong-determinant and altered-
exponent controls.  A separate regulated `n=4` theorem would then be required
before any Wick or loop-measure use.  This route is concrete, cheaper than a
hierarchy calculation, and remains open.

### N8 — cross-cycle echo

The current `origin/main` comparison includes this BZ note, the downstream
Maradudin Green-function context, the hierarchy regulator-dependence no-go,
and the sibling `Z^3` character bridge.  They consistently separate the 3D
Haar factor from the `4pi`, four-dimensional, regulator, and hierarchy tasks.
That repetition supports the bounded positive claim and the N7 generalization;
it does not support a new broad negative.
