# KCPT corner-carrier antilinear and non-Hermitian K-real readout classification: conjugation constraints, equivariant nullity, and exact separation modes (bounded theorem)

Registry id: `kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_bounded_theorem_note_2026-07-18`
Date: 2026-07-18
**Type:** bounded_theorem
Paired runner: [kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py](../scripts/kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py)
Runner cache: `logs/runner-cache/kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.txt`

## Abstract

The landed corner-carrier work supplies a real cyclic carrier `C` with `C^3 = I_3`
and `C^T = C^2`, entrywise conjugation `K`, and the shared conjugate doublet lines
`vw` and `vwb = conj(vw)` on which `C vw = w vw` and `C vwb = conj(w) vwb`, with
`w = -1/2 + (sqrt(3)/2)*i`. The parent delivery note classified Hermitian
`K`-real linear readouts and left antilinear and non-Hermitian functionals open.
This note answers that stated opening as a bounded theorem: it classifies the
explicitly `K`-real faces and the broader equivariant antilinear face. Their exact
relations range from equality and nullity to complex-conjugate values with equal
real parts or equal moduli. This is not a universal degeneracy or
indistinguishability claim.

Three new faces are treated alongside the landed Hermitian `K`-real baseline. A
linear non-Hermitian but `K`-real
functional splits by the Hermitian bridge into a `K`-even symmetric part and a
`K`-odd skew part, and always returns complex-conjugate values on `vw` and `vwb`,
so their real parts coincide while their full complex values can distinguish the
lines. An antilinear equivariant functional built from the
commutant span of `C` vanishes identically on both doublet lines. An
antilinear `K`-real functional (equivariance dropped) is a bilinear form whose two
doublet values are complex conjugates, so equal-normalized representatives of the
two doublet rays carry equal moduli. These are face-specific register-not-read
relations, not a universal indistinguishability claim; exact escapes through
`K`-odd, non-`K`-real, and non-equivariant ingredients remain explicit. The same
statements are delivered to the landed `4^3`
staggered surface through the `hw=1` triplet lift with exact compression scale
`4096 = 64^2`. All results are exact and independently reproduced by the paired
runner.

## Carrier and functionals

The corner carrier is `C = [[0,0,1],[1,0,0],[0,1,0]]`, real, with `C^3 = I_3`,
`C^T = C^2`, and `K C K = C`. The unnormalized channel vectors are the singlet
`v0 = (1,1,1)^T` and the conjugate doublet pair
`vw = (1, conj(w), conj(w)^2)^T`, `vwb = conj(vw)`, with `C vw = w vw` and
`C vwb = conj(w) vwb`. In the Hermitian inner product (conjugate-linear first slot)
`<vw, vwb> = 0` and `<vw, vw> = <v0, v0> = 3`. The cyclotomic bilinear sums,
which drive the antilinear witness values below, are `vw^T vw = 0`,
`vwb^T vwb = 0`, and `vwb^T vw = 3`.

A linear functional is `E_A(psi) = psi^dag A psi`. An antilinear functional is
`F_B(psi) = psi^dag conj(A) conj(psi)` with `B = K` composed with `A`. The
character projector is `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for
`chi in {1, w, conj(w)}`; on the doublet `P_w = vw vw^dag / 3`.

## Claims

**T1 (Hermitian-decomposition bridge).** Every complex `A` decomposes uniquely as
`A = H1 + i*H2` with `H1 = (A + A^dag)/2` and `H2 = (A - A^dag)/(2i)` both
Hermitian. For entrywise-real `A` the symmetric part is `K`-even
(`conj(H1) = H1`) and the skew part is `K`-odd (`conj(H2) = -H2`, with `i*H2`
real). A matrix that is simultaneously Hermitian and anti-Hermitian vanishes, so
the split is rigid.

**T2 (linear non-Hermitian `K`-real face).** For entrywise-real `A`,
`E_A(K psi) = conj(E_A(psi))`. Hence `E_A(vwb) = conj(E_A(vw))` and the two
doublet values share one real part. The symmetric part alone fixes that common
real part; the imaginary separation `E_A(vw) - E_A(vwb) = 2i*Im E_A(vw)` is
carried entirely by the skew part. An exact separating witness is the real
non-Hermitian `A = C - C^2`, with `E(vw) = 3*i*sqrt(3)` and
`E(vwb) = -3*i*sqrt(3)`, encoded by the polarization identity
`i*(C - C^2) = -sqrt(3)*(P_w - P_wb)`. This witness stays inside the row and
separates the full complex values; the theorem supplies only the equal-real-part
constraint and does not posit a real-part-only physical readout.

**T3 (antilinear equivariant face).** The commutant of `C` is the span of
`{I, C, C^2}`, of complex dimension `3`; `K`-reality is not required in this
face. For `A` in this span the antilinear `B` is `C`-equivariant, sends `vw` to
`conj(a + b*w + c*w^2) vwb`, and gives
`F_B(vw) = F_B(vwb) = 0`: the equivariant antilinear face is identically null on
both doublet lines, while the singlet value `F_B(v0) = 3*conj(a + b + c)` stays
free.

**T4 (antilinear `K`-real face, equivariance dropped).** `K B K = B` holds iff
`A` is entrywise real. Then `F_B(vw) = vwb^T A vwb`, only the symmetric part
contributes, and `F_B(vwb) = conj(F_B(vw))` for the displayed conjugate,
equal-normalized representatives. Antilinear phase covariance is
`F_B(c*psi) = conj(c)^2 * F_B(psi)`, so the complex value is not a ray invariant
but its modulus is. The exact separation modes remain explicit: the
non-`K`-real `A = vwb vwb^T` returns `(F_B(vw), F_B(vwb)) = (9, 0)`, its
conjugate mirror `A = vw vw^T` returns `(0, 9)`, and the `K`-real but
non-equivariant rejector `E_11` returns `(1, 1)`, breaking equivariant nullity
without breaking the equal-modulus relation.

**T5 (value freedom and neutrality).** On the equivariant channel family
`A = al*I + be*(C + C^2) + ga*(C - C^2)` the closed forms are
`E(v0) = 3*(al + 2*be)` and `E(vw) = 3*(al - be) + 3*sqrt(3)*ga*i`. The
normalization-invariant channel-value map from `(al, be, ga)` to the singlet
value and the real and imaginary doublet channel values has Jacobian determinant
`-3*sqrt(3)`, so the three real channel values are independently free. Every
class condition is invariant under `A` to `conj(A)` and under `w` to `conj(w)`,
and no channel value forces `r`.

**T6 (lattice delivery).** The landed `hw=1` triplet lift `V64` satisfies
`V64^T V64 = 64*I_3`, lies in the kernel of the integer antisymmetric staggered
operator `2D` (`2D V64 = 0`), and intertwines the carrier with the proper cubic
rotation `UR`: `UR V64 = V64 C`. Every carrier face is delivered to the `4^3`
staggered surface with exact compression scale `4096 = 64^2`. The delivered
linear witness `V64 (C - C^2) V64^T` gives `E(psi_w) = 4096*3*sqrt(3)*i`, and the
delivered non-`K`-real antilinear witness `V64 vwb vwb^T V64^T` gives
`F(psi_w) = 36864 = 4096*9` with `F(psi_wb) = 0`.

**T6-corollary (delivered class identity).** Because `V64^T V64 = 64*I_3`, the
delivered `K`-real antilinear class equals `4096` times the carrier `K`-real
class, so the equal-moduli relation and its named separators transport
unchanged to the staggered surface.

## Unified face-by-face classification

| Face | Operator class | Doublet values `(vw, vwb)` | Exact registered relation |
| --- | --- | --- | --- |
| Hermitian linear `K`-real | `A = A^dag`, `A` real | equal real values | equal expectation values |
| linear non-Hermitian `K`-real | `A` real, `A != A^dag` | complex conjugates, generally distinct | equal real parts; full complex values can differ |
| antilinear equivariant (`K`-reality not required) | `A` in span `{I, C, C^2}` | `(0, 0)` | identically null |
| antilinear `K`-real | `A` real | complex conjugates | equal moduli for equal-normalized representatives |

The four rows impose four different relations. The real non-Hermitian witness
`C - C^2` separates full complex values while remaining inside its row. The real
`E_11` seed leaves equivariance and changes the equivariant antilinear pair from
`(0, 0)` to `(1, 1)` while remaining `K`-real. The non-`K`-real rank-one seeds
break the antilinear equal-modulus relation, while the Hermitian separator
`i*(C - C^2)` leaves the Hermitian `K`-real row through its `K`-odd part.

## Boundary

This is a classification of named readout-functional faces on the supplied corner
carrier and its landed lattice delivery, not a nonderivability,
universal-degeneracy, or indistinguishability claim: the K-real non-Hermitian face
already separates full complex values, and K-odd, non-K-real, or non-equivariant
escapes remain explicit.

No orientation is selected: every statement is invariant under the joint relabeling
`w <-> conj(w)`, and the mechanism note's two-model FLAG and live Qualification stand
unchanged.

Nothing here forces, derives, or prefers any value of `r`: the classified functional
values on the singlet and shared doublet channels remain free.

Lattice-wide readout on non-kernel states, superoperator and completely positive faces,
and interacting extensions are untested here and are the next paths this opens.

## Non-claims

- No dynamics, formation rule, Born weight, or probability is asserted; the
  channel values are static readouts on supplied kernel states.
- No real-part-only physical readout is supplied for the linear non-Hermitian
  face; its full complex values distinguish the displayed conjugate lines.
- No new axiom, import, or primitive is registered. The carrier, the lift `V64`,
  the staggered phases, and the doublet lines are taken from the landed
  dependencies below.
- The staggered realization gate `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03`
  remains an open downstream gate; nothing here discharges or renames it.
- The delivered results concern the `hw=1` kernel triplet only; readout on
  non-kernel lattice states is a separate open path.

## Honest auditor read

The exact content is elementary linear algebra on a `3`-dim carrier plus integer
arithmetic on the `4^3` surface, so every gate is reproducible with exact
arithmetic and none depends on a tuned prefactor. The witness values `9`, `0`,
`3*sqrt(3)`, and `4096` each discriminate: perturbing the carrier eigen-relation,
the polarization sign, the compression scale, or the rotation transpose
convention flips the corresponding gate, and the paired runner carries those
negative controls. The load-bearing modeling choice is the identification of the
antilinear composed functional `F_B` with `B = K` composed with `A`; the
classification is a statement about that supplied functional family, not a claim
that no other readout convention exists. No physical bridge selects only the
common real part of the non-Hermitian linear values. The independent audit lane
sets status.

## Dependency roles

- [KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md)
  supplies the carrier, the `hw=1` lift `V64`, the staggered operator `2D` with
  exact rank `56`, the rotation intertwiner, and the Hermitian `K`-real linear
  classification this note extends to the antilinear and non-Hermitian faces.
- [KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md](KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md)
  supplies the carrier presentation, the character projectors, the entrywise
  conjugation `K`, and the `K`-real derivable-initial-data reading used by the
  `K`-reality faces.
- [KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md](KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md)
  supplies the two-model FLAG and live Qualification that keep the `w` to
  `conj(w)` orientation open.
- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  cubic-lattice sites, nearest-neighbor adjacency, and proper cubic rotations
  under which the staggered delivery is covariant.
