# KCPT corner-carrier antilinear and non-Hermitian K-real readout classification: every explicitly K-real functional face registers the conjugate doublet pair degenerately (bounded theorem)

Registry id: `kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_bounded_theorem_note_2026-07-18`
Date: 2026-07-18
**Type:** bounded_theorem
Paired runner: [kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py](../scripts/kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py)
Runner cache: `logs/runner-cache/kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.txt`

## Abstract

The landed corner-carrier work supplies a real cyclic carrier `C` with `C^3 = I_3`
and `C^T = C^2`, entrywise conjugation `K`, and the shared conjugate doublet lines
`vw` and `vwb = conj(vw)` on which `C vw = w vw` and `C vwb = conj(w) vwb`, with
`w = -1/2 + (sqrt(3)/2)*i`. The parent delivery note classified Hermitian linear
readouts and left antilinear and non-Hermitian functionals open. This note answers
that stated opening as a bounded theorem: it classifies the explicitly `K`-real
readout faces and shows that each one registers the two conjugate doublet lines
degenerately, while every named sharp separator carries an explicitly `K`-odd or
non-`K`-real ingredient.

Three faces are treated on one carrier. A linear non-Hermitian but `K`-real
functional splits by the Hermitian bridge into a `K`-even symmetric part and a
`K`-odd skew part, and always returns complex-conjugate values on `vw` and `vwb`,
so their real parts coincide. An antilinear equivariant functional built from the
commutant span of `C` vanishes identically on both doublet lines. An
antilinear `K`-real functional (equivariance dropped) is a bilinear form whose two
doublet values are complex conjugates, so the two doublet rays carry equal moduli.
Every degeneracy is register-not-read: it is a property of the explicitly `K`-real
face, not a bound on the carrier, and named non-`K`-real or `K`-odd separators
split the pair sharply. The same statements are delivered to the landed `4^3`
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
carried entirely by the skew part. The sharpest separating witness is the real
non-Hermitian `A = C - C^2`, with `E(vw) = 3*i*sqrt(3)` and
`E(vwb) = -3*i*sqrt(3)`, encoded by the polarization identity
`i*(C - C^2) = -sqrt(3)*(P_w - P_wb)`.

**T3 (antilinear equivariant face).** The commutant of `C` is the span of
`{I, C, C^2}`, of complex dimension `3`. For `A` in this span the antilinear `B`
is `C`-equivariant, sends `vw` to `conj(a + b*w + c*w^2) vwb`, and gives
`F_B(vw) = F_B(vwb) = 0`: the equivariant antilinear face is identically null on
both doublet lines, while the singlet value `F_B(v0) = 3*conj(a + b + c)` stays
free.

**T4 (antilinear `K`-real face, equivariance dropped).** `K B K = B` holds iff
`A` is entrywise real. Then `F_B(vw) = vwb^T A vwb`, only the symmetric part
contributes, `F_B(vwb) = conj(F_B(vw))`, and the two doublet rays carry equal
moduli `|F_B(vw)| = |F_B(vwb)|`. Antilinear phase covariance is
`F_B(c*psi) = conj(c)^2 * F_B(psi)`. The degeneracy is register-not-read: the
non-`K`-real `A = vwb vwb^T` returns `(F_B(vw), F_B(vwb)) = (9, 0)`, its
conjugate mirror `A = vw vw^T` returns `(0, 9)`, and the `K`-real but
non-equivariant rejector `E_11` returns `F_B(vw) = 1`.

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
class, so the equal-moduli degeneracy and its named separators transport
unchanged to the staggered surface.

## Unified bounded reading

| Face | Operator class | Doublet values `(vw, vwb)` | Degeneracy registered |
| --- | --- | --- | --- |
| Hermitian linear | `A = A^dag` | equal real, equal imaginary | equal expectation values |
| linear non-Hermitian `K`-real | `A` real, `A != A^dag` | complex conjugates | equal real parts |
| antilinear equivariant | `A` in span `{I, C, C^2}` | `(0, 0)` | identically null |
| antilinear `K`-real | `A` real | complex conjugates | equal moduli |

Each explicitly `K`-real row registers the two conjugate doublet lines
degenerately; each degeneracy is broken only by leaving the row, either by a
`K`-odd Hermitian imaginary part (linear) or by a non-`K`-real seed (antilinear).

## Boundary

This is a classification of explicitly K-real readout functionals on the supplied
corner carrier and its landed lattice delivery, not a nonderivability claim: K-odd
and non-K-real separators remain derivable and registrable.

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
that no other readout convention exists. The independent audit lane sets status.

## Dependency roles

- [KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md](KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md)
  supplies the carrier, the `hw=1` lift `V64`, the staggered operator `2D` with
  exact rank `56`, the rotation intertwiner, and the Hermitian-linear
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
