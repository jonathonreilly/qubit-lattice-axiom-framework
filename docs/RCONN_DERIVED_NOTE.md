# R_conn Diagnostic from the SU(N_c) Fierz Channel-Count Identity

**Date:** 2026-04-14 (originally); 2026-05-10 (audit-narrowing refresh);
2026-05-18 (claim_scope formalized as exact imported Fierz channel-count
fraction plus conditional MC consistency framing only per audit verdict
boundary instruction; physics-loop Tier B attempt logged as NARROWED —
matching rule (M) closure from retained primitives shown obstructed by
already-recorded no-go authority); 2026-05-25 (prior audit-repair
narrow-rescope recorded matching rule (M) as open); 2026-05-25
(parameterized-diagnostic repair: matching rule (M)
and `kappa_EW = 0` are no longer admitted by this row; the theorem surface is
only the exact SU(3) channel-fraction arithmetic plus a diagnostic MC check).
**Claim type:** bounded_theorem
**Formal parameter boundary.** The repaired note does not admit matching rule
(M), does not admit `kappa_EW = 0`, and does not identify the physical lattice
connected trace with the adjoint dimension fraction. The exact theorem is the
SU(3) channel fraction `F_adj = (N_c^2 − 1)/N_c^2 = 8/9`. The old MC result
`R_conn(MC) = 0.887 ± 0.008` is retained only as a diagnostic consistency
check against that target, not as a derivation of the physical readout.
**Parallel rescope.** The companion note `YT_EW_COLOR_PROJECTION_THEOREM.md`
uses the same formal-parameter boundary for `kappa_EW`.
**Claim scope (post-2026-05-25 parameterized-diagnostic repair):** the
load-bearing content of this note is exactly two pieces: (i) the exact
SU(3) representation-dimension fraction `(N_c^2 − 1) / N_c^2`, checked
directly by the primary runner, and (ii) a diagnostic MC consistency record
showing that the old MC measurement is compatible with `8/9` within its
reported uncertainty. The promotion of the channel-count fraction to the
lattice connected-trace dynamical observable is explicitly out of scope.
**Status:** bounded parameterized/diagnostic support note. The exact
`(N_c^2 − 1)/N_c^2` fraction is finite-dimensional SU(3) arithmetic; the
MC result is diagnostic only. No physical-readout selector is claimed.
**Type:** bounded_theorem (exact channel fraction + diagnostic MC check)
**Status authority:** independent audit lane only.
**Authority role:** records exact channel-fraction arithmetic and a diagnostic
MC consistency check; it does not close the dynamical bridge from channel
fraction to lattice connected-trace ratio.
**Depends on:** baseline `Cl(3)` framework setting (`N_c = 3`), SU(N_c) gauge theory.

**Context authority for the exact `(N_c^2 − 1)/N_c^2` ratio (not a
load-bearing one-hop dep in this repaired row):**

- `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`
  (`claim_type: bounded_theorem`, `audit_status: audited_clean`,
  `effective_status: retained_bounded`) — exact group-theory derivation
  of the q-qbar Hilbert-space adjoint-channel dimension fraction
  `(N_c^2 − 1)/N_c^2` from the SU(N_c) Fierz completeness identity
  applied to the q-qbar two-point function, valid at every gauge
  configuration and at any finite N_c (no expansion). This is context for
  the same arithmetic. The repaired primary runner checks the channel-count
  fraction directly; this context note is not a load-bearing dependency edge.

**Other cross-refs (cited as related, not as authority closure):**
`YT_EW_COLOR_PROJECTION_THEOREM.md` (plain text),
`YUKAWA_COLOR_PROJECTION_THEOREM.md`
(`claim_type: decoration` under the Fierz authority),
`EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md`
(plain text).

**Primary runner:** `scripts/frontier_rconn_parameterized_diagnostic.py`.
The old `scripts/frontier_color_projection_mc.py` remains historical MC
support only; it is not the primary theorem runner for this repaired row.

---

## Audit boundary

The 2026-05-10 audit verdict was `audited_renaming`: the load-bearing
in-note step "the connected/adjoint propagator fraction equals the
representation-dimension fraction" was classified as a definitional
substitution from group-theory channel counts to a dynamical observable.
That substitution is the **dynamical-population bridge** between the
exact Fierz channel-count and the lattice connected-trace ratio.

This repaired note does **not** derive or admit that bridge. It does the
following four things:

1. **Checks** the exact `(N_c^2 − 1)/N_c^2` adjoint-channel
   representation-dimension fraction directly in the primary runner.
2. **Records** a standard 't Hooft-1974 1/N_c topological argument for
   why planar diagrams dominate non-planar diagrams by `1/N_c^2` at
   leading order. This argument is a textbook large-N_c structural
   estimate cited as context ('t Hooft 1974, Witten 1979, Coleman 1985,
   Manohar 1998); it is **not** an in-atlas
   theorem.
3. **Names** the matching-rule wall without accepting it as a premise:
   the lattice connected-trace observable is not identified here with the
   adjoint-channel projection coefficient.
4. **Reports** an MC cross-check on a 4^4 lattice that the measured
   `R_conn(MC) = 0.887 ± 0.008` agrees with the analytic target 8/9 to
   0.2%. The MC is a numerical consistency test, not an independent
   derivation.

**Open derivation gap (real, not import-redirect):**

The promotion from the imported Fierz channel-count fraction
`(N_c^2 − 1)/N_c^2` to the lattice connected-trace ratio `R_conn`
requires a structural matching rule: that the lattice connected color
trace `<Tr_color[G(0,x) G(x,0)]_connected>` projects onto the adjoint
channel `C(x,y)` of the Fierz decomposition rather than onto the total
`Tr_color[G(x,y) G(y,x)]`. The cited Fierz note records this matching
rule as a named structural input from the framework's lattice gauge
surface, not derived in that note. This repaired row does not inherit the
input as a theorem premise; it records the gap and leaves the physical
readout out of scope. In short, the physical readout out of scope boundary is
load-bearing for this repaired row.

This is a **real derivation gap**, not a dependency-citation issue.

## Statement (scope-bounded)

**Representation-theoretic fact (checked by the primary runner).** In
SU(N_c) gauge theory, the adjoint-channel dimension fraction of the q-qbar
Hilbert space is exactly:

    dim(adj) / dim(N_c ⊗ N_c-bar) = (N_c^2 − 1) / N_c^2,

which equals 8/9 at N_c = 3 (fixed by Cl(3)). This is a pure group-
theory invariant; it carries no expansion correction.

**Diagnostic 1/N_c estimate (not theorem scope).**
If a separate matching theorem supplies the statement that the lattice
connected color trace projects onto the adjoint channel, the leading-order
't Hooft topological dominance of planar over non-planar diagrams gives the
diagnostic estimate

    R_conn = (N_c^2 − 1) / N_c^2 + O(1/N_c^4),

with the `O(1/N_c^4) ~ 1.2%` correction at `N_c = 3` bounded by genus-2
contributions in the standard topological expansion. This diagnostic estimate
is not a physical-readout theorem of this row.

For `N_c = 3`:

    R_conn ~ 8/9 + O(1/81)  [diagnostic if a separate matching theorem supplies M]

with the MC cross-check `R_conn(MC) = 0.887 ± 0.008` agreeing to 0.2%
under that diagnostic reading.

---

## Part 1: The 1/N_c Expansion -- Setup

### 1.1 Origin of N_c = 3

The framework begins with Cl(3), the rank-3 Clifford algebra over Z^3.
The gauge group SU(3) arises from the Z_3 clock-shift symmetry of the
lattice. The number of colors N_c = 3 is not a parameter -- it is fixed
by the spatial dimension d = 3 of the Z^3 lattice. This is the single
axiom from which N_c descends.

### 1.2 The 't Hooft expansion

For SU(N_c) gauge theory with quarks in the fundamental representation,
't Hooft (1974) showed that Feynman diagrams can be organized by their
topology. The key insight: rewrite the gauge coupling as

    g^2 = lambda / N_c

where lambda = g^2 N_c is the 't Hooft coupling, held fixed as N_c
varies. Each Feynman diagram can be drawn on a compact orientable
surface of genus g (number of handles). The amplitude of a diagram
drawn on a genus-g surface scales as:

    A_g ~ N_c^{chi}  where  chi = 2 - 2g - B

Here chi is the Euler characteristic of the surface, and B is the
number of quark-loop boundaries.

For the quark-antiquark propagator (B = 1 external quark boundary):

    chi = 2 - 2g - 1 = 1 - 2g

Therefore:
- Planar diagrams (g = 0): A_0 ~ N_c^{1}
- First non-planar correction (g = 1): A_1 ~ N_c^{1-2} = N_c^{-1}
- Higher genus (g >= 2): A_g ~ N_c^{1-2g}

The ratio of non-planar to planar contributions is suppressed by
1/N_c^{2g}, with the leading correction at g = 1 suppressed by
1/N_c^2.

### 1.3 Standard references

This topological classification of diagrams is a textbook result:

- 't Hooft, Nucl. Phys. B72, 461 (1974): original large-N_c paper
- Witten, Nucl. Phys. B160, 57 (1979): baryons in large N_c
- Coleman, "Aspects of Symmetry" (1985), Ch. 8: pedagogical treatment
- Manohar, "Large N QCD" (1998), hep-ph/9802419: modern review

The expansion is exact as a topological classification. No approximation
is involved in assigning genus g to a diagram. The approximation enters
only when truncating the sum over genera.

---

## Part 2: Diagnostic R_conn Heuristic (not theorem scope)

### 2.1 Color decomposition of the q-qbar propagator

The quark-antiquark bilinear psi-bar_a psi_b transforms under
SU(N_c) as:

    N_c (x) N_c-bar = 1 (singlet) + (N_c^2 - 1) (adjoint)

The full q-qbar propagator Pi(p) receives contributions from both
channels:

    Pi(p) = Pi_singlet(p) + Pi_adjoint(p)

In the diagnostic matching picture, the connected color trace ratio would be
defined as:

    R_conn = Pi_adjoint / Pi_total = Pi_adjoint / (Pi_singlet + Pi_adjoint)

### 2.2 Topological channel heuristic

The open step is to identify singlet and adjoint channel weights with distinct
diagram topologies in the lattice connected-trace observable. This repaired
row does not use that identification as theorem scope.

**Adjoint channel (connected, planar).**
Diagrams where the quark and antiquark exchange gluons without their
color lines crossing. These are PLANAR diagrams: they can be drawn
on a sphere (genus 0) with the quark boundary on one side. The color
quantum numbers flow continuously between the quark and antiquark
lines via gluon exchange.

In the standard large-N_c diagnostic picture, planar diagrams dominate at
leading order in 1/N_c. Each planar
diagram carries an implicit factor of N_c from the color trace around
the quark loop, plus factors of lambda (the 't Hooft coupling) from
each vertex pair. The total planar contribution scales as:

    Pi_planar ~ N_c * f(lambda)

where f(lambda) is a function of the 't Hooft coupling that encodes
all planar dynamics.

**Singlet channel (disconnected, non-planar).**
Diagrams where the quark and antiquark annihilate into a pure-glue
intermediate state (the quark lines form a closed loop, connected to
the rest only through gluons). These correspond to the singlet channel:
the q-qbar pair has total color charge zero, and the intermediate state
is a colorless glueball.

Such diagrams are NON-PLANAR: the quark loop is a separate boundary
from the external operator insertion, requiring the surface to have
at least one handle (genus >= 1). The leading non-planar contribution
scales as:

    Pi_non-planar ~ N_c^{-1} * h(lambda)

The diagnostic topological picture says that cutting open a planar diagram along the
quark boundary, the quark and antiquark color indices are connected
by gluon lines -- this is the adjoint (connected) channel. Cutting
open a non-planar diagram, the quark color index is traced internally
-- this is the singlet (disconnected) channel.

### 2.3 The diagnostic ratio at leading order

The total propagator is:

    Pi_total = Pi_planar + Pi_non-planar + O(N_c^{-3})
             = N_c f(lambda) + N_c^{-1} h(lambda) + O(N_c^{-3})

The connected (adjoint) fraction is:

    R_conn = Pi_planar / Pi_total
           = N_c f / (N_c f + N_c^{-1} h + ...)
           = 1 / (1 + h/(N_c^2 f) + ...)
           = 1 - h/(N_c^2 f) + O(1/N_c^4)

Now invoke the completeness relation. The singlet and adjoint channels
span the full N_c x N_c-bar space. By the Fierz identity (proved in
YUKAWA_COLOR_PROJECTION_THEOREM.md, Section 1.3), the N_c^2-dimensional
bilinear space decomposes into:

    dim(singlet) = 1
    dim(adjoint) = N_c^2 - 1

If a separate matching theorem supplies that the dynamics populates the color
channels according to their dimensionality, then:

    Pi_singlet / Pi_total = 1/N_c^2
    Pi_adjoint / Pi_total = (N_c^2 - 1)/N_c^2

This gives:

    h/(N_c^2 f) = 1/N_c^2

    R_conn = 1 - 1/N_c^2 + O(1/N_c^4) = (N_c^2 - 1)/N_c^2 + O(1/N_c^4)

### 2.4 What is exact and what is diagnostic (audit-narrowed 2026-05-25)

The exact-at-finite-N_c content is the **representation-dimension
fraction** `(N_c^2 − 1)/N_c^2`, checked directly by the primary runner.
That fraction is a pure SU(N_c) group-theory invariant; it carries no
expansion correction and no physical-readout selector.

The leading-order **dynamical** statement that the lattice connected-
trace observable saturates that fraction is **conditional**:

1. The Fierz identity is an algebraic identity of SU(N_c) — that part
   is exact arithmetic; this repaired note checks the fraction directly.

2. The assertion that *planar dynamics populates all `N_c^2 − 1` adjoint
   generators uniformly* at leading order in 1/N_c is **not derived in
   this note**. It is the standard textbook large-N_c heuristic
   ('t Hooft 1974) and remains context rather than in-atlas theorem
   authority. It is also the renaming step flagged by the audit verdict.

3. The assertion that *the singlet channel receives contributions ONLY
   from non-planar diagrams (genus >= 1)* uses the same 't Hooft
   topological classification under the same heuristic.

4. Under (2)-(3), the leading-order channel decomposition matches the
   imported representation-dimension fraction with corrections of
   `O(1/N_c^4)` from genus-2 surfaces.

The leading-order match is therefore diagnostic unless a separate matching
theorem supplies (M). Calling it "exact" overstates the in-atlas derivation
status; the previous version of this section did exactly that and is corrected
here.

---

## Part 3: Diagnostic Beta = 6 Context

### 3.1 The topological classification is beta-independent

The 1/N_c expansion classifies diagrams by their TOPOLOGY (genus of
the surface on which they can be drawn). This classification is
independent of:

- The bare coupling g^2 (or equivalently beta = 2N_c/g^2)
- The lattice spacing a
- The quark mass m
- The lattice volume L

The genus of a Feynman diagram is a combinatorial property of its
graph structure. It does not depend on the numerical values of the
propagators or vertices. A planar diagram remains planar at any beta.

Therefore, the standard statement "planar diagrams dominate over non-planar
diagrams by a factor of N_c^2" is beta-independent as a large-N_c topology
classification. Its use as a physical `R_conn` readout remains diagnostic
until a separate matching theorem supplies (M).

### 3.2 What DOES depend on beta

The 't Hooft coupling lambda = g^2 N_c determines the WEIGHT of each
diagram within a given genus class. At beta = 6 (g^2 = 1), the
't Hooft coupling is lambda = 3. This is O(1), meaning:

- Individual diagrams are not perturbatively small
- The full non-perturbative sum over planar diagrams gives f(lambda=3)
- The full non-perturbative sum over genus-1 diagrams gives h(lambda=3)

In the diagnostic picture, the ratio h/(N_c^2 f) is treated as 1/N_c^2 = 1/9
because:

1. Both f and h receive contributions from all orders in lambda
2. The relative suppression factor N_c^{-2} between genus 0 and
   genus 1 is a property of the COLOR TRACE, not the coupling
3. At strong coupling, each genus class is resummed non-perturbatively,
   but the genus-dependent N_c scaling is preserved

This is the diagnostic value of the topological expansion: it separates the
N_c-counting from the dynamical content, but it does not by itself derive the
lattice connected-trace selector.

### 3.3 Higher-genus corrections at N_c = 3

For N_c = 3, the formal expansion parameter is 1/N_c^2 = 1/9 ~ 11%.
In the diagnostic matching picture, the next correction would be:

    delta R_conn^{(g=2)} ~ c_2 / N_c^4 = c_2 / 81

where c_2 is an O(1) coefficient. Even if c_2 ~ 1, the correction
is ~1.2%.

The old MC measurement is consistent with this: R_conn(MC) agrees with 8/9 to
0.2% (see Part 5), consistent with c_2 being O(1) or smaller. This is not a
proof of the physical readout.

### 3.4 Strong coupling and the topological expansion

One might worry that at strong coupling (g^2 = 1), the 1/N_c expansion
breaks down. This does NOT happen. The reason:

The 1/N_c expansion is not a weak-coupling expansion. It is a
TOPOLOGICAL expansion that works at ANY coupling. 't Hooft's original
proof holds for arbitrary lambda. The expansion parameter is 1/N_c^2,
not g^2 or alpha_s.

At strong coupling, the individual diagrams are large, but the
topological suppression of non-planar diagrams is maintained because
it arises from COLOR COMBINATORICS (the number of independent color
traces), not from the magnitude of individual diagrams.

This is supported as context by lattice Monte Carlo studies of large-N_c gauge
theories, which verify the 1/N_c^2 scaling of non-planar observables at strong
coupling (see Lucini, Teper, Wenger, JHEP 0401:061, 2004). That literature
support is not a load-bearing in-atlas theorem in this repaired row.

---

## Part 4: Diagnostic Correction Bound

### 4.1 Genus-2 bound

If a separate matching theorem supplied the physical `R_conn` readout, the
diagnostic leading correction would come from genus-2 diagrams:

    R_conn = (N_c^2 - 1)/N_c^2 + c_2/N_c^4 + O(1/N_c^6)

For N_c = 3:

    R_conn = 8/9 + c_2/81 + O(1/729)

The coefficient c_2 depends on the full non-perturbative dynamics.
From the MC measurement (Part 5):

    R_conn(MC) = 0.887 +/- 0.008
    8/9 = 0.88889

    Residual: |R_conn(MC) - 8/9| = 0.002 +/- 0.008

This gives |c_2| < 0.8 (2-sigma), consistent with c_2 = O(1).

### 4.2 Parametric bound from large-N_c scaling

In general, the 1/N_c expansion coefficients satisfy:

    c_g ~ (lambda/4pi)^{n_g}

where n_g is the number of vertices in the minimal genus-g diagram.
For genus 2, the minimal diagram has n_2 >= 4 vertices, giving
c_2 ~ (3/4pi)^4 ~ 0.03 if perturbative counting applies.

However, at strong coupling (lambda = 3), this perturbative estimate
is unreliable. The MC bound |c_2| < 0.8 is the reliable constraint.

### 4.3 Diagnostic impact on observables

If a later theorem supplies the physical readout, the O(1/N_c^4) diagnostic
correction would propagate to observables as:

    delta(y_t) / y_t = (1/2) * delta(R_conn) / R_conn
                     ~ c_2 / (2 * 81 * 8/9) ~ c_2 * 0.007

For |c_2| < 0.8: delta(y_t)/y_t < 0.5% in that diagnostic picture. This is
context only and does not update a retained prediction.

    delta(g_EW) / g_EW = (1/2) * delta(R_conn) / R_conn ~ 0.5%

This is similarly small compared to the old 0.17% EW-coupling comparison, but
that comparison remains diagnostic and does not prove the selector.

---

## Part 5: MC Diagnostic Check

### 5.1 Setup

The historical script `scripts/frontier_color_projection_mc.py` measures an
R_conn-style diagnostic on SU(3) gauge configurations at beta = 6 (g^2 = 1)
using the color-decomposed quark propagator. It is not the primary theorem
runner for this repaired row.

Framework inputs (zero imports):
- SU(3) gauge group from Cl(3)
- Lattice Z^4 (d+1 = 4 from anomaly-forced time)
- beta = 6 from g^2 = 1 (Cl(3) canonical)
- Staggered fermion operator from Cl(3) taste structure

### 5.2 Measurement

The MC computes:

    R_conn = <Tr_color[G(0,x) G(x,0)]_adj> / <Tr_color[G(0,x) G(x,0)]_total>

where G_{ab}(x,y) is the staggered quark propagator in the SU(3)
gauge background, and the subscripts denote the Fierz decomposition
into adjoint and total channels.

Result (4^4 lattice, 100 configurations, Cabibbo-Marinari heat bath):

    R_conn(MC) = 0.887 +/- 0.008

### 5.3 Comparison with diagnostic target

    R_conn(diagnostic target) = 8/9 = 0.88889
    R_conn(MC) = 0.887 +/- 0.008
    Deviation: |0.887 - 0.889| / 0.889 = 0.2%

The MC value agrees with the diagnostic target to 0.2%, well
within the statistical error (0.9%) and consistent with the
O(1/N_c^4 ~ 1.2%) correction being small. This agreement is not a derivation
of the physical connected-trace theorem.

### 5.4 Cross-check: observable predictions

The Fierz/channel result `R_conn = 8/9` enters one direct observable
prediction and one matching-rule conditional EW package:

1. **EW couplings:** g_1(v), g_2(v) match observed values to 0.17%
   average deviation only on the connected-trace specialization
   `kappa_EW=0`, where `sqrt(K_EW(0)) = sqrt(9/8)`. The exact Fierz
   fraction alone does not derive that physical readout coefficient.

2. **Top mass:** m_t(pole) = 172.57 GeV vs observed 172.69 GeV
   (-0.07%) in the historical package where y_t is corrected by
   sqrt(8/9) = sqrt(R_conn). This comparison is diagnostic unless a separate
   selector theorem supplies the physical readout.

The observed agreements are diagnostics only. They must not be used as
load-bearing derivations of the physical readout.

---

## Part 6: Axiom and Authority Trace

The dependency chain has two parts: an axiom trace for `N_c = 3`, and a
mixed in-atlas / diagnostic-context literature trace for the
`(N_c^2 − 1)/N_c^2` channel-count value:

    Cl(3) --> Z_3 clock-shift --> SU(3) gauge group --> N_c = 3       (in-atlas axiom trace)
          |
          +--> SU(N_c) gauge theory on Z^4 lattice                    (in-atlas axiom trace)

    SU(N_c) gauge theory                                              (in-atlas)
          |
          +--> Fierz completeness identity                            (context authority, retained_bounded)
          |
          +--> Hilbert-space dimension fraction (N_c^2 - 1)/N_c^2     (checked directly here)
          |
          +--> matching rule (M): connected-trace projects on adjoint (open structural input
          |                                                            inherited from Fierz note;
          |                                                            not derived on `main`)
          |
          +--> conditional 8/9 R_conn estimate at N_c = 3              (this note, conditional on (M))

    't Hooft 1/N_c topological classification                         (diagnostic-context literature input)
          |
          +--> O(1/N_c^4) correction estimate                          (diagnostic-context literature input)

This repaired note's in-note theorem content is a class-A read of the SU(N_c)
dimension fraction checked by the primary runner. The 1/N_c discussion and MC
measurement are diagnostic context unless a separate matching theorem supplies
(M).

---

## Part 7: Status Assessment (audit-narrowed 2026-05-10)

### 7.1 Scope of the in-note claim

This repaired note's in-note content is restricted to:

1. an exact check of the `(N_c^2 − 1)/N_c^2` adjoint-channel dimension
   fraction;
2. a diagnostic 1/N_c-expansion estimate that gives
   `R_conn = (N_c^2 − 1)/N_c^2 + O(1/N_c^4)` only if a separate matching
   theorem supplies (M);
3. an MC cross-check on a 4^4 lattice that agrees with the target 8/9 to
   0.2%, recorded as diagnostic context.

### 7.2 What is **not** derived in this note

The dynamical-population bridge — i.e. the structural assertion that the
lattice connected color trace projects onto the adjoint channel of the
Fierz decomposition — is **not** derived or inherited as a premise in this
repaired note. This is the renaming step flagged by the
2026-05-10 audit verdict.

The 't Hooft 1974 topological dominance argument is literature context; it is
**not** an in-atlas theorem on `main`.

### 7.3 Status table for downstream consumers

The downstream observables that depend on `R_conn = 8/9` (`sqrt(Z_phi)`,
`y_t(phys)`, `g_EW(phys)`, `m_t(pole)`) must not cite this repaired row as a
theorem for that physical readout. They require a separate matching-rule
selector theorem.

---

## Import Status Table (audit-narrowed 2026-05-10)

| Element                          | Value      | Status      | Source                                                                                              |
|----------------------------------|------------|-------------|-----------------------------------------------------------------------------------------------------|
| N_c = 3                          | 3          | framework setting | Cl(3) Z_3 clock-shift |
| SU(N_c) gauge theory             | --         | framework setting | Cl(3) framework |
| 1/N_c topological classification | --         | literature context | 't Hooft 1974; not in-atlas theorem |
| Planar dominance (genus 0)       | N_c^{chi}  | literature context | topological classification |
| Fierz identity                   | exact      | context | `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md` |
| `(N_c^2-1)/N_c^2`                | 8/9        | exact algebra | checked by `scripts/frontier_rconn_parameterized_diagnostic.py` |
| Matching rule (M)                | --         | open | not derived or admitted here |
| R_conn estimate                  | 8/9 + O(1/81) | diagnostic | only if a separate matching theorem supplies (M) |
| R_conn(MC) = 0.887 +/- 0.008     | 0.887(8)   | diagnostic | old `scripts/frontier_color_projection_mc.py`; uses 8/9 as explicit target |

---

## 8. 2026-05-18 Tier B bridge-theorem attempt (NARROWED — no closure)

### 8.1 What was attempted

Per the audit verdict's repair sub-target, the 2026-05-18 physics-loop
dispatched a Tier B algebraic bridge attempt: derive the matching rule
(M) — the framework's lattice connected color trace projects onto the
adjoint channel of the Fierz decomposition — as a one-step Fierz
channel-count projection identity from retained Cl(3) primitives. The
target derivation would identify the lattice connected-trace observable
with the SU(N_c) adjoint trace fraction `(N_c^2 − 1)/N_c^2 = 8/9` at
N_c = 3, closing the dynamical-population bridge.

### 8.2 Verdict: NARROWED (closure refused)

The bridge **does not close** from retained primitives. The attempt is
recorded here as a narrowing because the framework already contains
two named-obstruction artifacts that prove the bridge requires non-
retained, non-perturbative inputs. The 2026-05-18 attempt did not find a
route around either obstruction; forcing a closure would silently
elevate the named obstruction to retained status.

### 8.3 Named obstructions blocking the Tier B route

**(O-OPEN-GATE)** `EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`
records the matching-rule underdetermination as a **no-go theorem** on
the retained packet `{ N_c = 3, Fierz identity, CMT mean-field
factorization, OZI bounded suppression }`. Concretely, parametrize the
post-CMT channel sum as

```text
Pi_EW^phys(kappa_EW) = F_adj + kappa_EW (1 − F_adj)
                     = (N_c^2 − 1)/N_c^2 + kappa_EW / N_c^2
```

The retained primitives normalize the total channel sum but **do not
fix** the disconnected/singlet readout coefficient `kappa_EW`. The
package-level 9/8 factor is the special case `K_EW(0) = 9/8` (connected-
trace selector), but the full-trace readout `K_EW(1) = 1` is equally
compatible with the retained Fierz arithmetic and identical CMT
scaling. Distinct completions exist with the **same Fierz channel
counts**, demonstrating that the channel-count identity alone cannot
determine the physical observable. Therefore no one-step Fierz
projection from retained primitives selects `kappa_EW = 0`.

**(O-STRETCH)** `YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md`
enumerates the three structural routes that would close (M) exactly
and demonstrates each fails on the retained packet:

- **(O1)** Disconnected-piece identical vanishing: **false** —
  glueball intermediate states exist at any N_c ≥ 2 with non-zero
  amplitude.
- **(O2)** Disconnected piece contributes only to v: **scheme choice,
  not derivation** — the decomposition `Σ^full = Σ^conn + Σ^disc` is
  algebraic; the assignment of `Σ^disc` exclusively to v is a
  renormalization-scheme choice, not a derived statement of the
  retained primitives.
- **(O3)** Exact OZI-vanishing theorem at all genus orders: **not
  available** — standard OZI is phenomenological and the rule has
  corrections even at N_c = ∞.

The sharpest honest statement kept by this repaired row is exact
channel-fraction arithmetic plus diagnostic support. A physical
`R_conn^phys = (N_c^2 − 1)/N_c^2 + O(1/N_c^4)` theorem still requires a
separate matching-rule selector.

### 8.4 Why a one-step Fierz projection cannot close (M)

Both the cited Fierz authority and this note's Hilbert-space dimension
count derive the **representation-dimension fraction** of the q-qbar
tensor product. That fraction is a pure SU(N_c) group-theory invariant.
The matching rule (M), by contrast, asserts that the **lattice
connected color trace** `<Tr_color[G(0,x) G(x,0)]_connected>` projects
onto the same adjoint channel after the framework's specific Wilson-
line construction of the EW current and after CMT mean-field
factorization. This is a statement about a dynamical observable, not a
statement about a Hilbert-space dimension count. The two coincide only
when an additional structural premise selects the disconnected readout
coefficient `kappa_EW = 0`. The retained primitives do not supply that
premise. Per the hostile-review semantics policy, the arithmetic
identification `dim(adj)/dim(N_c ⊗ N_c-bar) = (N_c^2 − 1)/N_c^2 = 8/9`
cannot mask the action-level admission that the lattice connected-
trace observable is identified with this fraction by convention.

### 8.5 Yang-Mills exclusion boundary check (caveat)

A potential one-step closure route would invoke the Wilson-line
structure of the EW current at the lattice level to **mechanically**
project onto the adjoint channel after CMT factorization absorbs the
singlet piece into `u_0`. This route is **not available** to a retained-
primitive derivation: the Wilson-line construction of the gauge
connection is an admitted import from continuum Yang-Mills, not a
retained theorem (cf. `project_bridge_gap_resolution_c_locked` — the 10-agent attack
established Wilson is an admitted import, not derived from Cl(3)/Z^3).
Forcing a Wilson-line projection here would re-import a known open
admission and silently elevate it under a different label. The Tier B
attempt therefore stops short of invoking Wilson-line structure beyond
what the cited Fierz authority already records as a named open
primitive.

### 8.6 Outcome of the 2026-05-18 attempt

- **Bridge derivation:** NOT complete; NARROWED.
- **Admissions used (counterfactual to closure):** retained Cl(3)
  (N_c = 3) + SU(N_c) Fierz identity context
  alone are **insufficient**; closure additionally requires either
  (O1) an exact disconnected-piece-vanishing theorem, (O2) a scheme-
  level assignment of `Σ^disc` to v (not derived), or (O3) an exact
  all-genus OZI theorem.
- **Honest tier:** the repaired note remains a `bounded_theorem` whose live
  scope is exact channel-count arithmetic plus diagnostic MC context; the
  matching rule (M) is not admitted as a premise and the dynamical-population
  bridge remains open.
- **No promotion of `kappa_EW = 0` is performed** by this narrowing.
  The connected-trace selector remains an extra premise outside the
  retained packet, as established by the open-gate no-go authority.

### 8.7 What this narrowing changes vs the 2026-05-10 audit-refresh

The 2026-05-10 refresh already documented that the matching rule (M)
is not derived in this note. The 2026-05-18 narrowing adds:

1. An explicit cross-reference to the
   `EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`
   no-go theorem, which proves that the retained packet admits at
   least two `kappa_EW` completions (the `K_EW(0) = 9/8` connected-
   trace selector and the `K_EW(1) = 1` full-trace selector) with
   identical Fierz arithmetic and identical CMT scaling.
2. An explicit cross-reference to the
   `YT_EW_MATCHING_RULE_M_NOTE_2026-05-02.md`
   named-obstruction packet, which enumerates the three failure modes
   (O1, O2, O3) blocking a retained-primitive derivation of (M).
3. A documented Tier B bridge-theorem attempt verdict (NARROWED) for
   audit-trail integrity: future re-audits do not need to re-discover
   that the one-step Fierz channel-count projection from retained
   Cl(3) primitives does not close the dynamical-population bridge.

The 2026-05-25 repair changes the live load-bearing claim: this row now
preserves only exact channel-fraction arithmetic plus diagnostic MC context.
It does not carry matching-rule promotion in downstream consumers.
