# AC_phi_lambda Cycle-Flux Transport-Face Inventory

**Date:** 2026-07-01
**Claim type:** bounded_theorem
**Scope:** exact face inventory plus wall typing.
**Status authority:** independent audit lane only. This note does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement.
**Primary runner:** [`scripts/acphilambda_cycle_flux_transport_face_inventory_2026_07_01.py`](../scripts/acphilambda_cycle_flux_transport_face_inventory_2026_07_01.py)

## Claim

On the retained C3 generation ring, the forced trace-free transverse pair
(1,2), equivalently (2,1), is the unique nontrivial pair whose fixed-point
summands are per-mode real-positive Green weights. For j = 1,2, the conjugate
pair gives 1 / |omega^j - 1|^2 = 1/3, so S_sum(1,2) = 2/3 and the local
average L3(1,2) = 2/9.

The same two numbers are the zero-mode-subtracted return inventory of the
cycle graph Laplacian on the generation 3-ring. For L_N = 2 I - C_N - C_N^T,
Tr L_N+ = (N^2 - 1)/12 and (L_N+)vv = (N^2 - 1)/(12 N); at N = 3 these are
2/3 and 2/9.

```text
W_cycle_holonomy_value, transport-typed presentation:
  the physical charged-lepton readout's cycle flux equals the generation ring's
  zero-mode-subtracted return amplitude:
  Phi = Tr L+ = 2/3,   equivalently   delta = (L+)_vv = 2/9 per site.
```

Thus the fixed-defect density is the generation ring's per-site return amplitude. In this exact sense, the equation itself remains the wall; this note types it. It does not derive the strike-point equation.

## Retained Inputs

- `koide_aps_c3_fixed_locus_weights_bridge_narrow_theorem_note_2026-06-05`: [docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md). Quoted fragment: "the determinant of the transverse action is the C₃ singlet"; boundary fragment: "does **not** supply the physical single-summand readout".
- `brannen_circulant_is_forced_c3_covariant_record_preserving_generation_form_bounded_theorem_note_2026-06-15`: [docs/BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md](BRANNEN_CIRCULANT_IS_FORCED_C3_COVARIANT_RECORD_PRESERVING_GENERATION_FORM_BOUNDED_THEOREM_NOTE_2026-06-15.md). Quoted fragments: "circulant form" and "(a, |b|, delta)".
- `koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24`: [docs/KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md). Quoted fragments: "eta_APS(Z_3; 1,2)" (listed there with value 2/9 in its witness inventory) and "Type-B-to-radian".
- PR #4783 `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`: rescale obstruction; c = 1 is not derivable homogeneously.
- PR #4788 `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01`: registrable content is cos(3 delta); Phi = 3 delta; c = 1 iff Phi = S_sum = 2/3; wall `W_cycle_holonomy_value`.
- PR #4789 `ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01`: K-real equals real-holonomy equals the modulus-stationary locus; the physical member remains off-locus.
- `DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05`: unaudited context; record-preserving local dynamics allows closed-loop Wilson and covariant-path terms, but this note does not lean on it as authority.

## Conjugate-Pair Reduction (T-F1)

Let omega = exp(2 pi i / 3), realized exactly as -1/2 + i sqrt(3)/2. The nontrivial C3 transverse pairs are (1,1), (1,2), (2,1), and (2,2). The fixed-locus row's forcing is the trace-free condition a + b = 0 mod 3, equivalently the determinant of the transverse action is the singlet. That condition selects (1,2) and (2,1).

For the selected pair, omega^(j b) is the conjugate of omega^(j a) for j = 1,2. Each summand is therefore

```text
1 / ((omega^(j a) - 1)(omega^(j b) - 1))
  = 1 / |omega^(j a) - 1|^2
  = 1/3.
```

The per-mode weights are real and positive before summing. Hence S_sum(1,2) = 1/3 + 1/3 = 2/3, and L3(1,2) = S_sum(1,2) / 3 = 2/9.

The non-forced pairs do not have this per-mode property. For (1,1), the summand 1 / (omega - 1)^2 has nonzero imaginary part exactly, and the j = 2 summand has the opposite imaginary part. Their total is real, S_sum(1,1) = 1/3, but the per-mode Green weights are not real-positive modulus-squared weights. The same conjugate failure holds for (2,2).

Thus the fixed-locus "det of transverse action is the singlet" sentence does more than pick the denominator after summation. It picks exactly the pair for which the fixed-point terms are already the transport Green weights mode by mode.

## Transport Faces (T-F2)

Let C_N be the cyclic shift on N vertices and L_N = 2 I - C_N - C_N^T. The
runner constructs L_N as an exact rational SymPy matrix and computes L_N+ by
Matrix.pinv on exact matrices.

The N = 3 ring has spectrum {0, 3, 3}. Its pseudoinverse has trace 2/3, and
each diagonal entry is 2/9. Vertex transitivity is visible directly in the
diagonal equality.

For every N from 2 through 8, the runner verifies

```text
Tr L_N+ = (N^2 - 1)/12.
```

The per-site return amplitude is therefore

```text
(L_N+)vv = (N^2 - 1)/(12 N),
```

and at N = 3 this is 2/9.

The resistance face gives the same closed form with no spectral shorthand.
For vertices v,w on the N-cycle, let d be their cycle distance. The exact
resistance

```text
R(v,w) = (L_N+)vv + (L_N+)ww - 2 (L_N+)vw
```

equals d(N - d)/N for all pairs checked at N = 2 through 6. Summing over
unordered pairs gives Kirchhoff's route:

```text
sum_{v<w} R(v,w) = N Tr L_N+.
```

The runner also checks the finite sum

```text
sum_{d=1}^{N-1} d(N-d) = N(N^2 - 1)/6
```

for the same N range. This is the resistance/Kirchhoff face of the transport
inventory.

The spectral face is verified where SymPy has exact radical trigonometry:
N in {2,3,4,6}. In those cases,

```text
sum_{j=1}^{N-1} 1 / (2 - 2 cos(2 pi j/N)) = (N^2 - 1)/12.
```

The discriminators are load-bearing. Tr L_4+ = 5/4, not 2/3, so the number is
not graph-blind. The wrong closed form (N^2 + 1)/12 fails at N = 3. The
three-vertex path Laplacian has Tr L_path+ = 4/3, not 2/3, so the ring
topology is part of the type.

Thus at N = 3 the fixed-point face and transport face share one exact object:

```text
S_sum(1,2) = Tr L_3+ = 2/3,
L3(1,2) = (L_3+)vv = 2/9.
```

## Typed Presentation Of The Wall (T-F3)

```text
W_cycle_holonomy_value, transport-typed presentation:
  the physical charged-lepton readout's cycle flux equals the generation ring's
  zero-mode-subtracted return amplitude:
  Phi = Tr L+ = 2/3,   equivalently   delta = (L+)_vv = 2/9 per site.
```

Both sides are closed-loop transport quantities on the same retained 3-ring:
the flux threading the cycle and the return amplitude of the cycle's own free
propagation with the zero mode removed. Both are R-valued and off-locus
capable, consistent with PR #4789's parity constraint.

The unaudited context note says record-preserving local dynamics allows
closed-loop Wilson and covariant-path terms; this note marks that sentence as
unaudited context and uses it for no authority.

Under the no-coincidences discipline, `eta_APS(Z_3; 1,2) = 2/9` sat in the
radian-bridge witness inventory as a support coincidence. The Green face
upgrades the fixed-point-vs-return-amplitude pair from coincidence to identity:
the same exact object appears in both presentations. The remaining coincidences
listed there, including hypercharge, Casimir-ratio, and charge-product faces,
are untouched.

The equation itself remains the wall; this note types it.

## What This Moves

| Before | After |
|---|---|
| 2/9 as Lefschetz average | 2/9 as per-site return amplitude: identity, not coincidence |
| strike-point equation untyped | typed closed-loop = closed-loop |
| radian-bridge witness inventory | one entry upgraded from coincidence to identity |
| general-N scaling implicit | general-N scaling explicit: (N^2 - 1)/12 |

## What Does Not Move

- The typed equation is not derived.
- No dynamics theorem is supplied.
- The readout selection stays open.
- Other coincidence-inventory entries remain untouched.
- No additional wall label is introduced.

## Audit Consequence If Retained

Rows citing the strike point may use the transport-typed presentation. That is
the same dependency as `W_cycle_holonomy_value` / `W_defect_identity_unit` /
R-eta sub-admission (ii), not a second dependency and not a replacement
authority.

## Non-Claims

- This note does not derive flux = return amplitude.
- This note does not claim the ring Laplacian is the physical dynamics; it is
  the retained ring's free transport reconstruction, a calculational device
  per the record ontology.
- This note does not import eta or APS machinery. The face arithmetic is
  self-contained finite algebra.
- This note contains no probability, occurrence, or theta content.

## No-Go Discipline Gate

This checklist supports a bounded face inventory; it is not a terminal no-go.

### N1
- Fixed-point face route: ATTEMPTED: exact.
- Transport/Green face route: ATTEMPTED: exact.
- Resistance/Kirchhoff face: ATTEMPTED: exact.
- Identification of flux with return amplitude: OPEN: the typed strike point.
- Rescale-invariant derivation: OUT OF SCOPE HERE; the live rescale wall is not discharged by this face inventory.
- Owner primitive: GOVERNANCE.

### N2
No additional wall label is introduced. One wall is now presented in a fourth form.

### N3
- ring Laplacian: reconstruction on the retained ring, not new physics.
- zero-mode subtraction: the democratic/singlet mode is the C3 fixed line;
  removing it is exact linear algebra, not a physical claim.
- return amplitude: defined as the pseudoinverse diagonal.
- closed-loop typing: both sides' type, not a dynamics claim.

### N4
Residual matching is unchanged against PR #4788: same wall, typed. Against the
radian row, one coincidence is upgraded. Against the fixed-locus row, its
average is the per-site return amplitude.

### N5
The proven sentences are exact finite identities. The typing sentence is a type statement, not a derivation.

### N6
Live paths remain: derive flux = return amplitude from a same-surface record/transport theorem, now that the equation's two sides have one type; prove a K-breaking registration theorem; or settle the owner primitive.

### N7
Steelman: return amplitudes and fixed-point sums coinciding is standard spectral graph theory, so this is decoration.

Reply: standard or not, the identity removes a coincidence-ledger entry, fixes the general-N scaling, and gives the wall equation a single transport type on the retained surface. No value is derived.

### N8
Echo: same-number-multiple-structures events are handled under the
no-coincidences discipline by identity-or-mechanism. This note applies that
pattern to one entry.

## Verification

Run from the worktree root:

```bash
python3 scripts/acphilambda_cycle_flux_transport_face_inventory_2026_07_01.py
```

Expected close after the final runner pass:

```text
TOTAL: PASS=127 FAIL=0
```
