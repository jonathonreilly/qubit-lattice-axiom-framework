# AC_phi_lambda Sub-Admission (ii) Value Face: Registered-Angle Functional, Law-Freeness, and Exactness Relocation

**Date:** 2026-07-05
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict, and it does not edit the Tier-A
registry, ledger, queue, or publication-status surface. The registry-level
consequence named below is available only to a future gated, owner-approved
lane and is not executed here.
**Primary runner:**
[`scripts/frontier_acphilambda_r_eta_value_face_registered_angle_2026_07_05.py`](../scripts/frontier_acphilambda_r_eta_value_face_registered_angle_2026_07_05.py)
**Cached runner output:**
[`logs/runner-cache/frontier_acphilambda_r_eta_value_face_registered_angle_2026_07_05.txt`](../logs/runner-cache/frontier_acphilambda_r_eta_value_face_registered_angle_2026_07_05.txt)
(`TOTAL: PASS=27 FAIL=0`)

> **Not claimed:** any interior `Phi` derivation, forcing, or preference; mass prediction; local-density derivation; registry edit; or change to the formal `H(delta)` layer.
>
> **Claimed:** `Phi` is an already-defined functional of the unordered registered signed-root multiset. The value face reduces to realized-state registration; the survivor is the delta-side exactness residual.

## FIREWALL (binding on every line below)

Nothing here derives, forces, or prefers any interior `Phi`. The admissible
family spans `[0, pi/3]`: S2.1 constructs states at `Phi = 0.05`, `2/9`,
`0.5`, and `pi/3 - 0.05`, and S2.2 checks that no unique interior `Phi` is
output.

`Phi = 2/9` appears only as the charged-lepton lane's registered comparator.
The local density `2/9` is cited only as a retained-bounded pure number,
scoped to local density with physical readout excluded.

This is delta-side work only. S1.12 verifies `e1,e2` are delta-blind, and
S1.13-S1.14 verify the `r` coordinate is a function of `e1,e2` only while
`Phi` changes through `e3`. No special `r` value is assumed or consumed.

## Statement

Take the formal Hermitian circulant class consumed exactly as in the
2026-06-11 R-eta narrowing note's formal layer:

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,
```

with `a` real, `B >= 0`, and `C` the cyclic 3-shift. The retained one-hop form
authority is the
[Tier-A K-orbit determinant/orientation note](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md);
the physical carrier identification is not imported as retained-grade content.

For the unordered registered signed-root triple

```text
lambda_k = a + 2 B cos(delta + 2 pi k/3),  k = 0,1,2,
```

runner S1.0-S1.7 derives, rather than asserts, the elementary symmetric
functions:

```text
e1 = 3a
e2 = 3a^2 - 3B^2
e3 = a^3 - 3aB^2 + 2B^3 cos(3 delta).
```

On the nondegenerate stratum `B > 0`,

```text
a = e1/3
B = sqrt(e1^2 - 3 e2)/3
cos(3 delta) = (e3 - a^3 + 3aB^2)/(2B^3)
Phi = (1/3) arccos(cos(3 delta)) in [0, pi/3].
```

Therefore `Phi` is a single-valued functional of the unordered multiset
`{lambda_k}` on the registrable folded surface: the delta-magnitude content
of the signed-root multiset.

Under the realized-state primitive, this makes the value face of
sub-admission (ii) state registration, not a derivation-output admission. What
survives is the exactness residual: why the registered charged-lepton value
sits on the retained fixed-locus local density `2/9`.

Net decomposition:

```text
sub-admission (ii) = (ii-value) + (ii-exactness).
```

`(ii-value)` is the registered `Phi` carried by the realized charged-lepton
state. `(ii-exactness)` asks why that registered value lands on the
distinguished fixed-locus number. The physical carrier identification remains
routed through the unaudited context separated by the R-eta narrowing note's
2026-06-20 dependency-status split.

## Derivation

- **S1 (registered-angle functional).** The runner constructs `H(delta)`,
  verifies Hermiticity, computes `det H(delta)`, and derives `e1`, `e2`, and
  `e3` exactly from the three eigenvalues (S1.0-S1.4); the characteristic
  polynomial of `H(delta)` is verified equal to `prod(t - lambda_k)`, so the
  constructed `lambda_k` are the spectrum of `H`, not an assumed form
  (S1.1b). The inversions for `a`, `B`, and `cos(3 delta)` are exact on
  `B > 0` (S1.5-S1.7). A 200-draw shuffled-multiset round trip recovers the
  functional to `1e-12` (S1.8).

- **S1 boundary and independence checks.** `B = 0` is rejected as undefined
  and gives a uniform spectrum (S1.9). The endpoints `cos(3 delta)=+1` and
  `cos(3 delta)=-1` have degenerate pairs and land at `Phi=0` and
  `Phi=pi/3` (S1.10-S1.11). `e1,e2` are delta-blind, while the modulus-side
  coordinate is blind to `e3/Phi` (S1.12-S1.14).

- **S2 (counterfactual/state test).** The runner constructs law-admissible
  Hermitian circulant states with `B > 0` at `Phi = 0.05`, `2/9`, `0.5`, and
  `pi/3 - 0.05`; they register different `Phi` values (S2.1-S2.2). The
  realized-state primitive says, verbatim: "The laws do not pick the state;
  the world does, among the states the laws permit." It also says:
  "Derivations may evaluate at the realized state, pointwise." Its
  counterfactual test is explicit: "A value that would change under a
  different law-admissible realized state is registered data, not derivation
  output." (All three sentences are checked verbatim against the primitive
  note, S2.0.) `Phi` passes that test.

- **S2 comparator, labeled only.** The charged-lepton comparator uses
  `m_e = 0.51099895 MeV`, `m_mu = 105.6583755 MeV`, `m_tau = 1776.86 MeV`,
  the repo's PDG-2024 charged-lepton comparator baseline recorded in
  `docs/CLOSURE_T2_DF_PHYSICAL_CONSEQUENCES_NOTE_2026-05-10_t2df.md`,
  and positive roots `lambda_k = sqrt(m_k)` under the existing charged-lepton
  signed-root/cone convention as a labeled comparator only. It prints
  `Phi_PDG = 0.222229631489716`
  and `|Phi_PDG - 2/9| = 7.409267493568850e-06` as `COMPARATOR S2.PDG`. S2.3
  asserts only that the computation runs in `[0, pi/3]`.

- **S3 (law-freeness).** Reproducing the clean-modulus no-go, `d(e3)/d(delta)
  = -6 B^3 sin(3 delta)` exactly (S3.1), so for `B > 0` stationarity is
  `sin(3 delta)=0` (S3.2). Every `delta = k pi/3` stationary point is
  degenerate (S3.3). The clean laws select only fold-boundary points and leave
  the interior unselected. The no-gos are not obstacles to this reduction;
  they are context guardrails whose relevant finite computation is reproduced
  by S3 rather than imported as an additional dependency.

- **S4 (unit-face dissolution at the value face).** `Phi` is a pure number:
  `arccos` is the standard real inverse function and no unit choice appears
  in T1. The retained fixed-locus row supplies `2/9` as a pure number in its
  scoped class. S4.1 checks that `Phi=(1/3) arccos(x)` contains only `x`, and
  S4.2 checks that `2/9` lies inside `[0, pi/3]`. The value-face comparison is
  number-to-number; "read as an angle in radians" adds no further value-face
  content.

- **S5 (exactness residual, named only).** Runner S5.1 computes the PDG
  comparator gap as a finite number and deliberately does not threshold it
  as a theorem. The geometry supplies the distinguished point; registration
  supplies the sitting. Why the registered value sits there is the
  **delta-side exactness residual**. This is parallel to the sibling
  exactness-residual pattern, "registered pattern sits on a derived
  distinguished cell." No coincidences are silently dismissed.

## Hostile-guard

**(a) "This is just renaming the admission."** No. It changes demand shape:
the value chain evaluates a defined state functional instead of demanding a
law-level selector. It changes audit class: registered realized-state data
have the masses' standing under the primitive, while exactness remains a
frontier. It relocates the frontier to the delta-side exactness question plus
the standing physical carrier identification already routed through unaudited
context.

**(b) "The comparator is too close to `2/9`; registration is inadequate."**
The closeness is exactly why this note names an exactness residual. The
retained fixed-locus row supplies a distinguished number; the charged-lepton
state registers a value close to it. Why it is exact or nearly exact remains
open.

**(c) "The clean-modulus no-go says delta remains an admission."** It says
the clean modulus route selects only degenerate stationary points. That is
precisely the law-freeness hypothesis used here. The reduction is not that
the laws now pick the interior value; it is that the laws do not pick it, and
the primitive tells us how to treat state-varying values that the laws permit.

**(d) "The unit/radian problem is still live."** The retained radian-bridge
no-go remains respected. This note does not derive the literal bridge from
periodic or lattice phase sources. It only observes that the value-face
comparison is between two dimensionless numbers.

**(e) "The R-eta narrowing note says `A_R-eta` remains genuinely admitted, so
this contradicts a landed note."** No contradiction. That assessment predates
applying the realized-state primitive to the delta-side value face. This note
moves only the value face and leaves F1-F5 untouched: F2's fold is S1's
domain, and F4's no-value-selected result is S3's law-freeness input. The two
notes compose.

## No-go compliance

- `koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24`
  (`retained_no_go`): not contradicted. This note does not derive the literal
  radian bridge; it consumes the no-go as law-freeness and unit-bridge
  discipline.
- `koide_delta_lattice_wilson_selected_eigenline_no_go_note_2026-04-24`
  (`retained_no_go`): not contradicted. This note does not derive or select a
  Wilson eigenline; it uses only the unordered signed-root spectrum of the
  supplied circulant class.
- `koide_delta_marked_relative_cobordism_no_go_note_2026-04-24`
  (`retained_no_go`): not contradicted. This note does not close a marked
  relative cobordism route; the fixed-locus density is consumed only within
  its retained local-density scope.

## Boundary

- No derivation of `Phi = 2/9`, no mass prediction, and no global Koide
  solution claim. The comparator is labeled and non-load-bearing.
- No derivation of the fixed-locus density is attempted here. The retained
  fixed-locus row is cited for a local density only; physical readout is
  excluded from that row's scoped content.
- No registry file, ledger, queue, or status surface is edited. The
  independent audit lane remains the only status authority.
- The physical identification of the formal `H(delta)` surface with the
  charged-lepton carrier remains the open/contextual part already named by
  the R-eta narrowing note's 2026-06-20 dependency-status split.
- The minimal-axioms grounding is the 2026-06-29 qualification discipline:
  "These axioms state only their named primitive content..." and "A law
  privileges no states..." (full sentences checked verbatim against the live
  memo, S7.0). This note does not use the superseded occupancy-rule wording
  from the earlier memo as live axiom text.
- The realized-state primitive supplies no state, typicality claim, measure,
  weighting, or value. It permits pointwise evaluation at the supplied
  realized state and classifies counterfactually varying values as registered
  data.
- The result is bounded to the nondegenerate `B > 0` stratum for the
  functional. At `B = 0`, the spectrum is uniform and `Phi` is undefined
  (S1.9).

## Consequence (named, not executed)

The registry-level consequence available to a future gated, owner-approved
lane is: decompose AC_phi_lambda sub-admission (ii) into a realized-state
value face and a surviving exactness frontier. The value chain may consume
the registered `Phi` functional the way it consumes the registered masses.
The remaining open content is the delta-side exactness residual plus the
standing physical carrier identification context. This note executes no
registry edit.

## Honest-auditor-read

An auditor should read this as a bounded reclassification theorem, not a
value theorem. The runner handles the finite 3x3 algebra: derive the
symmetric functions, invert the folded angle, reject the degenerate boundary,
exhibit multiple law-admissible values, and reproduce the clean-modulus
stationary-point no-go.

Weak points to press: whether formal `H(delta)` is the right physical carrier;
whether the realized-state primitive applies to this delta-side functional;
and whether the exactness residual is too sharp to leave as registration. The
note names those points rather than resolving them.

## Dependencies (ids + live effective_status, supervisor-verified 2026-07-05)

| dependency | role | effective_status |
|---|---|---|
| [`tier_a_korbit_determinant_and_orientation_invariance_bounded_note_2026-06-09`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md) | the one retained one-hop authority for the supplied Hermitian circulant form and unordered sign/orientation fold discipline | retained_bounded |
| [`koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md) | derived fixed-locus local density `2/9`; Parts A/B scope is local density only, physical readout excluded | retained_bounded |
| [`koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md) | retained periodic/lattice phase sources do not derive the literal `2/9`-radian bridge; consumed here as law-freeness/unit-bridge discipline | retained_no_go |
| [`registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md) | even/phase-free registrable surface; supports reading the registrable delta-content as the folded magnitude | retained_bounded |
| [`realized_state_primitive`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) | approved primitive; pointwise evaluation and counterfactual test for registered data (quotes checked verbatim, S2.0) | meta |
| [`minimal_axioms`](MINIMAL_AXIOMS_2026-06-29.md) | 2026-06-29 memo qualification: named primitive content only; law privileges no states (quotes checked verbatim, S7.0) | meta |
| `koide_phase_delta_is_also_an_admission_clean_modulus_has_only_degenerate_stationary_points_narrow_no_go_note_2026-06-04` | clean-modulus law-freeness computation reproduced by runner S3 | retained_no_go (context; reproduced in runner) |
| `ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11` | context for the A_R-eta statement and formal F1-F5 layer; consumed facts re-verified here by runner S1-S4 | unaudited (context; reproduced in runner) |

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency, and does not modify any registry. The
independent audit lane is the only status authority.
