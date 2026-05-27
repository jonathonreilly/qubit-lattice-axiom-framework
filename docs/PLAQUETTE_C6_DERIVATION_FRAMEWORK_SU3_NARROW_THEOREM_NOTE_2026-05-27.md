# SU(3) Wilson Plaquette Strong-Coupling c_6 = 24 Framework-Bounded Factorization Note

**Date:** 2026-05-27
**Claim type:** bounded_theorem
**Claim scope:** the standalone algebraic facts that

1. the leading-order coefficient of the SU(3) Wilson plaquette
   strong-coupling character expansion
   `<P>(u) = c_1 u + c_4 u^4 + c_6 u^6 + ...`
   satisfies `c_1 = 1`, derived on framework primitives via single-link
   SU(3) Haar moment evaluation;
2. the number of distinct 3-cubes in d=4 spacetime Z^4 containing a
   chosen marked plaquette `P_0` equals exactly `4`;
3. under the structural factorization `c_6 = (geometric d=4 cube count)
   x (per-cube SU(3) Wigner-Racah weight)`, the published Drouffe-Zuber
   1983 Table 13 value `c_6 = 24` decomposes as `4 x 6`, with the
   geometric factor `4` rigorously derived in (2) above and the per-cube
   SU(3) Wigner-Racah weight `6` made explicit as an admitted external
   coefficient input;
4. the closed-form Padé[3/3] approximant value `3/5` at `u = 1/3` from
   PR #2040 is recovered identically using `c_1 = 1, c_4 = 4, c_6 = 24`
   as Padé linear-system input, demonstrating that the narrowed
   coefficient packet is *sufficient* for the Padé[3/3] value (only
   `c_1, c_4, c_6` enter the [3/3] approximant);
5. the d=4 spacetime dimensionality is **load-bearing** for `c_6 = 24`:
   under the framework's spatial substrate `Z^3` alone (no Wick-rotated
   time axis), the cube count is `2`, giving `c_6^(D=3) = 12`, not `24`.
   The framework's d=4 spacetime inheritance through the P2 Wick-rotation
   chain is what selects the Drouffe-Zuber Table 13 value.

This narrow theorem **does not** independently derive the per-cube SU(3)
Wigner-Racah weight `6` from scratch (that remains a Drouffe-Zuber Table 13
admitted coefficient input); it **does** convert PR #2040's Padé[3/3]
conditional from "entire coefficient table is external" to "only the
SU(3) Wigner-Racah weight per cube is external", with the leading
coefficient `c_1 = 1` and the geometric `d=4` factor `4` (and the
parallel `c_4 = 4` geometric count) closed on framework primitives.

**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; effective status is pipeline-derived
after independent review.
**Type:** bounded_theorem.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent
audit lane.
**Primary runner:** [`scripts/frontier_plaquette_c6_derivation_framework_su3_narrow.py`](./../scripts/frontier_plaquette_c6_derivation_framework_su3_narrow.py)

## Statement

Let `<P>(u)` denote the strong-coupling character expansion of the
single-plaquette expectation for SU(3) Wilson gauge action on a
4-dimensional hypercubic lattice, written as a formal power series in
the single-link fundamental character coefficient `u(beta) := beta/18`.
The Drouffe-Zuber 1983 Table 13 coefficient table is

```text
c_1 = 1,   c_4 = 4,   c_6 = 24,   c_7 = -24,   c_8 = 100, ...           (1)
```

**Conclusion (T1) (c_1 = 1 derivation on framework SU(3) Haar primitives).**
For SU(3) Wilson gauge action `S_W = -(beta/N) sum_P Re Tr U_P` with
`N = 3`, the strong-coupling expansion at leading order in `beta` gives

```text
<P>(beta) = (1/N) (beta/N) <(Re Tr U)^2>_{Haar} + O(beta^2)             (2)
         = (1/N^2) beta . (1/2)
         = beta / (2 N^2) = beta/18                                     (3)
```

at `N = 3`. Defining `u(beta) := beta/(2N^2)` makes
`<P>_leading(u) = u`, i.e. `c_1 = 1`. The single-link Haar moments
that feed this calculation are:

```text
int_{SU(3)} dU = 1,                                                     (4a)
int_{SU(3)} dU Re Tr U = 0,                                             (4b)
int_{SU(3)} dU (Tr U)^2 = 0   (no symmetric singlet in 3 (x) 3 = 6 + 3̄),(4c)
int_{SU(3)} dU |Tr U|^2 = 1   (Schur orthogonality F . F̄),              (4d)
int_{SU(3)} dU <(Re Tr U)^2> = (1/4)(0 + 2.1 + 0) = 1/2,                (4e)
```

each a standard SU(3) Haar single-link integral supported by the
framework's `NATIVE_GAUGE_CLOSURE_NOTE.md` /
`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` SU(3) representation-theoretic
primitives. Their effective statuses are pipeline-derived, not asserted
by this source note.

**Conclusion (T2) (d=4 cube enumeration).** A unit 3-cube in
d=4 hypercubic spacetime Z^4 is identified by its 3 spanning axes
(subset of `{0, 1, 2, 3}` of size 3) plus its base corner position. For
the marked plaquette `P_0` to be one of the cube's 6 faces, the cube's
3-axis subset must contain the 2 axes of `P_0`, namely `{0, 1}`. The
third axis is chosen from `{2, 3}` (2 choices); for each third axis,
the cube can extend in the `+` or `-` direction along that axis
(2 choices). Total:

```text
geometric d=4 cube count through P_0 = 2 x 2 = 4.                       (5)
```

**Conclusion (T3) (c_6 = 4 x 6 = 24 factorization).** Under the
structural factorization

```text
c_6 = (geometric d=4 cube count) x (per-cube SU(3) Wigner-Racah weight)
    = 4 x w_cube^(SU(3))                                                (6)
```

the published value `c_6 = 24` (Drouffe-Zuber 1983 Table 13) is consistent
with `w_cube^(SU(3)) = 6`. The geometric factor 4 is rigorously derived
in (T2). The per-cube weight `w_cube^(SU(3)) = 6` is an **admitted
external coefficient input** from Drouffe-Zuber Table 13; this narrow
theorem does **not** recompute the per-cube SU(3) Wigner-Racah weight
from SU(3) 6j-symbols.

The factor 6 admits a cube-symmetry interpretation that this note records
as supporting structure (not a proof): the cube rotation group `O` has
order `24`, and the stabilizer of one face under cube rotations is the
4-fold rotation group about the face normal, of order `4`. The orbit of
one face under `O` therefore has size `|O|/|Stab(face)| = 24/4 = 6`,
matching the per-cube weight. A full proof that this orbit size is the
Wigner-Racah weight requires the SU(3) 6j-symbol contraction on the
3-cube boundary graph, which remains the textbook citation.

**Conclusion (T4) (c_4 = 4 partial bound).** The same d=4 transverse
enumeration gives 4 candidate single-axis branch extensions of `P_0`
(2 transverse axes x 2 directions = 4), matching Drouffe-Zuber's
published `c_4 = 4`. As with (T3), the per-graph SU(3) weight for each
branch configuration is **not** independently verified here; the
structural enumeration is recorded only.

**Conclusion (T5) (d=4 inheritance is load-bearing for c_6 = 24).**
The framework's spatial substrate is `Z^3` (native cubic taste graph;
see `NATIVE_GAUGE_CLOSURE_NOTE.md` for the Cl(3)/SU(2)
construction). The relevant lattice for the Wilson plaquette in the
strong-coupling character expansion is `Z^4` spacetime, reached by
Wick rotation of Lorentzian `Cl(3,1)` to Euclidean `Cl(4,0)` on
`Z^3 x (a tau Z)` (see `P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md`
for the bounded composition that proposes the P2 sign-`ε` question into
the `ε = -1` Lorentzian / Wick-rotated-Euclidean cell).

Under the framework's `Z^3` spatial substrate **alone** (without the
Wick-rotated time axis), the marked plaquette spans 2 of 3 spatial
axes, leaving 1 transverse axis. Cube count = `1 x 2 = 2`, giving

```text
c_6^(D=3) = 2 x 6 = 12, not 24.                                         (7)
```

Therefore the value `c_6 = 24` published by Drouffe-Zuber Table 13 is
specifically the **d=4 spacetime** value, and matches the framework's
post-Wick-rotation Z^4 lattice. The d=4 selection is load-bearing for
the value `c_6 = 24` used by PR #2040 to land the Padé[3/3] result
`3/5` at `u = 1/3`.

**Conclusion (T6) (composition with PR #2040).** Substituting the
framework-bounded `c_1 = 1, c_4 = 4, c_6 = 24` into the same Padé[3/3]
linear-system solve as PR #2040 reproduces the closed-form rational
result

```text
Pade[3/3](u) = (u - 6 u^3) / (1 - 6 u^2 - 4 u^3),                       (8)
Pade[3/3](u = 1/3) = 3/5.                                               (9)
```

This is a numerical confirmation that the narrowed coefficient packet
(specifically `c_1, c_4, c_6`) is *sufficient* to reproduce PR #2040's
`3/5` value; the higher coefficients
`c_7 = -24, c_8 = 100` from Drouffe-Zuber Table 13 do **not** enter the
Padé[3/3] approximant. Therefore PR #2040's conditional dependency on
`c_7, c_8` is irrelevant for the Padé[3/3] = 3/5 value; the conditional
reduces to the framework-derived `c_1` and d=4 geometry, plus the
explicit Drouffe-Zuber per-cube Wigner-Racah weight admission.

## Proof

**(T1)** Standard SU(3) Wilson lattice strong-coupling result. The
Wilson action gives `exp(-S_W) = prod_P exp((beta/N) Re Tr U_P)`. The
plaquette expectation is

```text
<P> = (1/Z) int DU (1/N) Re Tr U_{P_0} prod_P exp((beta/N) Re Tr U_P).
```

Expanding `exp((beta/N) Re Tr U_P)` in a Taylor series and keeping the
leading nonvanishing contribution: the linear-in-`beta` term comes from
`P = P_0`. The integrand is `(1/N) Re Tr U_{P_0} . (beta/N) Re Tr U_{P_0}
= (beta/N^2) (Re Tr U_{P_0})^2`. The Haar integral over the four links of
`P_0` factorizes; each link integral is independent. Using `<(Re Tr U)^2>
= 1/2` from (4e), and four independent link Haar averages over the
plaquette holonomy give a single non-vanishing combinatorial structure
identified by the lowest-order `chi_F . chi_F̄` Schur orthogonality. The
arithmetic gives `<P>_leading = beta/(2 N^2) = beta/18` at `N = 3`,
i.e. `c_1 = 1`.

**(T2)** Direct combinatorial enumeration. A 3-cube in Z^4 is the
collection of `{(x_0, x_1, x_2, x_3) : a_i <= x_i <= a_i + e_i,
e_i in {0, 1}, sum_i e_i = 3}` for some base corner `(a_0, ..., a_3)`
and axis-mask `(e_0, ..., e_3)` with `sum e_i = 3`. For the cube to
contain `P_0` (axes `{0, 1}`) as one of its 6 faces, the mask must have
`e_0 = e_1 = 1`, leaving `(e_2, e_3) in {(1,0), (0,1)}` (the third axis
must be `2` or `3`). For each such mask choice, the cube extends either
+/-1 along the chosen third axis from the marked plaquette's plane, so
the base corner ranges over 2 positions. Total: `2 x 2 = 4` cubes.

**(T3)** From (T2), the d=4 geometric factor in the strong-coupling
coefficient `c_6` is `4`. The Drouffe-Zuber 1983 published value
`c_6 = 24` factorizes as `4 x 6 = 24`. The per-cube SU(3) Wigner-Racah
weight `6` is the SU(3) tensor contraction of the 3-cube boundary graph
under fundamental-rep alternating face orientations; this evaluation is
cited as an admitted external coefficient input from Drouffe-Zuber
Table 13. The cube-symmetry interpretation (orbit of one face under cube
rotation group `O = 24` modulo face stabilizer `4`, giving orbit size 6)
is supporting structure only.

**(T4)** Same d=4 transverse enumeration as (T2), restricted to single
branch attachments at order `u^4` instead of closed cubes at order `u^6`.

**(T5)** Direct enumeration in D=3 alone: P_0 spans 2 of 3 axes, the
third axis is uniquely determined, and the cube extends +/- along it
(2 positions). So D=3 cube count = 2. With the same per-cube weight 6,
hypothetical `c_6^(D=3) = 12 != 24`. The d=4 selection is load-bearing.

**(T6)** Linear-system solve for Padé[3/3] using the narrowed coefficient
packet `c_1 = 1, c_2 = c_3 = 0, c_4 = 4, c_5 = 0, c_6 = 24`: the Padé
numerator and denominator polynomials evaluate
to `P(u) = u - 6 u^3, Q(u) = 1 - 6 u^2 - 4 u^3`. Substitution at
`u = 1/3` gives `P(1/3)/Q(1/3) = (1/9)/(5/27) = 3/5`. The Padé[3/3]
approximant uses only series data through `u^6` (degree N+M = 6),
so `c_7, c_8` do not enter; the Padé[3/3] = 3/5 value is *independent*
of those coefficients. ∎

## Spacetime vs spatial dimensionality

A separate §addressing the d=4 vs D=3 distinction:

**Framework spatial substrate.** The framework's spatial lattice is `Z^3`
(the native cubic taste graph; see `NATIVE_GAUGE_CLOSURE_NOTE.md`).
On `Z^3` alone, the marked plaquette spans 2 of 3 axes, the third axis is
unique, and the cube count through `P_0` is 2 (cube extends +/- along
the unique third axis).

**Wick rotation to d=4 spacetime.** The framework's accepted Wick rotation
extends `Z^3` to `Z^4 = Z^3 x (a_tau Z)` spacetime (see
`P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md`
for the bounded composition that forces the spacetime Clifford algebra
to be Lorentzian `Cl(3, 1)` with Euclidean continuation via the
Osterwalder-Schrader transfer-matrix correspondence). On `Z^4`, the
marked plaquette spans 2 of 4 axes, and the cube count through `P_0` is
`2 x 2 = 4`.

**Wilson plaquette is d=4 Euclidean.** The Drouffe-Zuber 1983 Table 13
coefficients are tabulated for D=4 lattice gauge theory (the canonical
Euclidean spacetime lattice). The relevant Wilson plaquette in the
strong-coupling expansion for `<P>(beta = 6)` (PR #2040) is the d=4
Euclidean plaquette, matching the framework's post-Wick-rotation Z^4
lattice.

**D=3 alone would give different c_n coefficients.** Under D=3 alone
(no Wick-rotated time axis), the cube count is 2, giving hypothetical
`c_6^(D=3) = 12` (under the same per-cube SU(3) Wigner weight 6).
This does *not* match Drouffe-Zuber Table 13, which gives c_6 = 24.
Therefore the framework's d=4 selection (Z^3 + Wick-rotated time) is
**load-bearing** for the published `c_6 = 24` value used by PR #2040.

This § does NOT close the P2 Wick-rotation chain itself; it records that
the d=4 inheritance is load-bearing and inherits the (P2-closure)
parent's status. As of 2026-05-27, the P2 closure narrow theorem
[`P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md`](P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md)
is a source-note proposal with bounded closure conditional on the
Osterwalder-Schrader accepted-premise packet (the same packet already
feeding the single-clock codimension-1 evolution parent inline).

## What this claims

- **(T1):** the SU(3) Wilson plaquette strong-coupling leading-order
  coefficient `c_1 = 1`, derived on framework SU(3) Haar primitives.
- **(T2):** the d=4 cube count through the marked plaquette `P_0` is 4.
- **(T3):** the structural factorization `c_6 = 4 x 6 = 24`, with the
  geometric factor 4 rigorously derived and the per-cube SU(3) Wigner
  weight 6 cited as external (Drouffe-Zuber Table 13).
- **(T4):** the d=4 transverse enumeration matches `c_4 = 4` (same
  geometric factor, per-graph weight cited).
- **(T5):** the d=4 spacetime inheritance is load-bearing for c_6 = 24
  (D=3 alone would give 12).
- **(T6):** the framework-bounded `c_1 = 1, c_4 = 4, c_6 = 24` reproduce
  PR #2040's Padé[3/3] = 3/5 exactly; higher coefficients `c_7, c_8` do
  not enter the [3/3] approximant.

## What this does NOT claim

- Does **not** independently derive the per-cube SU(3) Wigner-Racah
  weight `6` from SU(3) 6j-symbols; that remains a Drouffe-Zuber Table 13
  external citation. The structural factorization `c_6 = 4 x 6` is the
  bounded content, not an independent recomputation of the per-cube
  weight.
- Does **not** independently derive `c_7 = -24` or `c_8 = 100` from
  framework primitives. Those coefficients also remain Drouffe-Zuber
  Table 13 external citations. Their values do not enter the Padé[3/3]
  approximant used by PR #2040.
- Does **not** close PR #2040's `3/5` numerical value as a true
  `<P>(beta = 6)` derivation. The Padé[3/3] residual gap to MC at
  `<P>_MC = 0.5934` remains `-0.0066` (`-1.1%`), an honest non-zero
  residual that PR #2040 explicitly does not promote to a closure.
- Does **not** close the P2 Wick-rotation chain itself. The d=4
  inheritance is recorded as load-bearing for `c_6 = 24`, conditional
  on the
  [`P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md`](P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md)
  bounded composition (audit-lane verdict pending).
- Does **not** retire the open `g_bare = 1` derivation gate, the
  `alpha_bare = 1/(4 pi)` source, the bounded `alpha_LM`/`alpha_s(v)`
  tadpole improvement chain, or the low-energy running bridge to `M_Z`.
- Does **not** promote any existing plaquette-lane note. The upstream
  `PLAQUETTE_SELF_CONSISTENCY_NOTE.md`,
  `GAUGE_VACUUM_PLAQUETTE_BRIDGE_SUPPORT_NOTE.md`,
  `BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06.md`, and related
  notes are reader-orientation pointers only.

## Cited dependencies

### Framework dependencies (load-bearing for T1 and the geometric factors)

- [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):
  structural SU(3) Cl(3)/SU(2) + graph-first SU(3) closure on Z^3.
  Supplies the SU(3) representation theory used by the single-link
  Haar moment evaluation in (T1).
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md):
  SU(3) closure on the selected-axis graph surface. Verifies SU(3)
  commutant structure used to interpret the per-cube Wigner contraction
  in (T3).

### Spacetime dependency (load-bearing for T5 d=4 inheritance)

- [`P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md`](P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md):
  source-note proposal bounded composition selecting Lorentzian `Cl(3,1)`
  + Wick rotation to Euclidean Z^4. Audit-lane verdict pending; the
  d=4 inheritance here inherits the parent's effective status.

### Admitted external coefficient inputs

- **Drouffe J.-M., Zuber J.-B.** (1983), *Physics Reports* 102, 1, Table 13:
  SU(N) Wilson plaquette strong-coupling cluster-expansion coefficients
  through `O(u^8)` for D = 4. Supplies `c_n` values for n in {4, 6, 7, 8}.
- **Münster G.** (1981), *Nucl. Phys.* B190 [FS3], 439: original
  SU(N) Wilson strong-coupling cluster-expansion graph counting.
- **Itzykson C., Drouffe J.-M.** (1989), *Statistical Field Theory* Vol. 2,
  Ch. 6: textbook account of single-link character integrals on SU(N)
  Haar measure.

These external coefficient inputs are load-bearing exactly where named:
`w_cube = 6` for the `c_6 = 24` factorization and the parallel per-graph
weight for the `c_4 = 4` comparison. The framework-internal content is:

- (T1) c_1 = 1: derived from framework SU(3) Haar primitives (no external
  citation required for the value).
- (T2) cube count 4 in d=4: derived from Z^4 combinatorial enumeration.
- (T3) factorization `c_6 = 4 x w_cube`: the factor 4 is framework-derived;
  the factor `w_cube = 6` is an admitted Drouffe-Zuber Table 13 value.
- (T4) c_4 = 4 partial bound: same d=4 enumeration as (T2); per-graph
  weight cited externally.
- (T5) d=4 vs D=3 distinction: derived from Z^3 vs Z^4 enumeration.
- (T6) Padé[3/3] = 3/5: derived numerically from c_1, c_4, c_6 inputs.

## Forbidden imports check

- No observed or fitted numerical targets are consumed as load-bearing.
  The Drouffe-Zuber Table 13 coefficient table enters only via the
  per-cube weight `w_cube = 6` and the parallel `c_4` per-graph weight,
  both explicitly flagged as admitted external coefficient inputs.
- No fitted selectors consumed.
- No same-surface family arguments load-bearing on retention.
- No unit-convention imports load-bearing on the algebraic value.
- No specific framework numerical inputs (`<P>`, `1/(4 pi)`,
  `alpha_s(M_Z)` etc.) load-bearing on the c_n derivation.
- No new repo vocabulary introduced.

## Validation

Primary runner:
[`scripts/frontier_plaquette_c6_derivation_framework_su3_narrow.py`](./../scripts/frontier_plaquette_c6_derivation_framework_su3_narrow.py)

Verifies all six conclusions via exact sympy rational arithmetic
(no floating-point at the theorem layer). Expected result:

```text
TOTAL: PASS=19 FAIL=0
```

The runner walks through:

```text
(T1) c_1 = 1 derivation on framework SU(3) Haar primitives        : 6 checks
(T2) d=4 cube enumeration through marked plaquette P_0            : 4 checks
(T3) c_6 = 4 (geometric) x 6 (SU(3) Wigner) = 24                  : 2 checks
(T4) c_4 = 4 partial bound via d=4 transverse enumeration         : 1 check
(T5) d=4 vs D=3 inheritance (D=3 gives c_6 = 12, not 24)          : 3 checks
(T6) Composition: c_1=1, c_4=4, c_6=24 implies Pade[3/3] = 3/5    : 3 checks
                                                                  ---------
                                                          TOTAL  :  19 checks
```

## Conditional reduction relative to PR #2040

PR #2040 lands the Padé[3/3] value `3/5` at `u = 1/3` (beta = 6) as a
bounded theorem conditional on the entire Drouffe-Zuber 1983 Table 13
coefficient set `{c_1 = 1, c_4 = 4, c_6 = 24, c_7 = -24, c_8 = 100}`.

This narrow theorem converts the conditionality as follows:

| Coefficient | PR #2040 status         | After this note's reduction        |
|-------------|-------------------------|------------------------------------|
| c_1 = 1     | external (DZ Table 13)  | **framework-derived (T1)**         |
| c_2 = 0     | external/no-surface input | unchanged; not newly closed here |
| c_3 = 0     | external/no-surface input | unchanged; not newly closed here |
| c_4 = 4     | external (DZ Table 13)  | **partial framework bound (T4)**   |
| c_5 = 0     | external/no-surface input | unchanged; not newly closed here |
| c_6 = 24    | external (DZ Table 13)  | **4 x 6: geometric factor 4 framework-derived (T2, T3), per-cube weight 6 remains admitted external input** |
| c_7 = -24   | external (DZ Table 13)  | does not enter Padé[3/3]; irrelevant |
| c_8 = 100   | external (DZ Table 13)  | does not enter Padé[3/3]; irrelevant |

So PR #2040's `3/5` value is now narrowed by:
- Framework-derived: `c_1 = 1` + `c_4` geometric factor 4 + `c_6` geometric
  factor 4 + d=4 spacetime inheritance.
- External Drouffe-Zuber: per-cube SU(3) Wigner weight 6 (and the parallel
  per-graph weight for c_4).
- Unchanged coefficient-packet zeros: `c_2 = c_3 = c_5 = 0`; this note
  does not separately prove those no-surface zeros.
- Inert (don't enter Padé[3/3]): c_7, c_8.

The remaining conditionality is the **single SU(3) 6j-symbol contraction
on the 3-cube boundary graph giving the per-cube weight 6**, plus the
parallel per-graph weight used for the `c_4` comparison. This is a
narrower textbook citation than "entire Drouffe-Zuber table".

The narrow theorem does NOT claim that PR #2040's `3/5` value is the
true continuum or finite-volume Wilson plaquette expectation; the
`-1.1%` residual to the MC value `0.5934` recorded by PR #2040 remains
the honest gap.
