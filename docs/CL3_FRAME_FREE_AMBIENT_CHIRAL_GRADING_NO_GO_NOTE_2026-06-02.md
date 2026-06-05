# Frame-Free Ambient Clifford Operations Do Not Source the Chiral Grading - Narrow No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Claim scope:** on the grade-1 vector subspace of the one-site `Cl(3,0)` / `M_2(C)` carrier, no frame-free Spin(3)/Pin(3)-equivariant ambient Clifford operation induces a grade-1 endomorphism that anticommutes with `Gamma_chi = (2/3)J - I`; the anticommuting L4 family exists, but it requires a chosen singlet axis and a free doublet vector, while frame-broken Lattice, momentum, dynamical, and sector-factorization routes remain open.

**Primary runner:** [`scripts/cl3_frame_free_ambient_chiral_grading_no_go_2026_06_02.py`](../scripts/cl3_frame_free_ambient_chiral_grading_no_go_2026_06_02.py)
(SCORECARD PASS=39 FAIL=0).

This note sets no audit verdict and predicts no downstream status. It proposes
no new axiom, primitive, selector, or carrier bridge.

---

## Setup

The baseline local carrier is the Quantum axiom in
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md): one qubit at
each site, equivalently `M_2(C)` or `Cl(3,0)` as a real algebra. In a Pauli
model write the grade-1 vectors as `e_i = sigma_i`; their span is the real
spin-1 vector representation of Spin(3). The pseudoscalar is
`omega = e_1 e_2 e_3 = i I`, with `omega^2 = -I`.

For the Koide-generation test surface, identify the generation factor with the
grade-1 vector space as in
[`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md).
That identification is used here only to ask whether the ambient one-site
Clifford structure supplies the missing chiral operator. This note does not
claim a physical species bridge.

On the grade-1 space let `J` be the all-ones matrix and
`Gamma_chi = (2/3)J - I`. Then `Gamma_chi^2 = I`, its eigenvalues are
`{+1,-1,-1}`, and it is the rotation `2vv^T - I` around the body-diagonal
`v = (1,1,1)/sqrt(3)`.

## Result

The named frame-free ambient Clifford operations have the following grade-1
actions:

| ambient operation | grade-1 action | anticommutes with `Gamma_chi`? |
|---|---:|:---:|
| grade involution `e_i -> -e_i` | `-I_3` | no |
| reversion | `+I_3` | no |
| Clifford conjugation | `-I_3` | no |
| pseudoscalar conjugation `x -> omega x omega^-1` | `+I_3` | no |
| Hodge map `omega * sigma_k -> b_k` on the `su(2)` index | `+I_3` | no |
| conjugation by the `[1,1,1]` quaternion | `Gamma_chi` itself | no |
| bivector commutator actions | rotation generators | no |

The structural reason is Schur scalarity on the real spin-1 representation. The
runner solves `[M,L_k]=0` for the three `so(3)` generators and obtains
`M = c I_3`. Hence every Spin(3)-equivariant grade-1 endomorphism is a scalar,
and `{c I_3, Gamma_chi} = 2c Gamma_chi`, which vanishes only for `c=0`.

The anticommuting family is not absent. The L4 family

```text
H = (1/3)(1 h^T + h 1^T),    sum(h) = 0
```

does anticommute with `Gamma_chi`, breaks the cyclic-circulant class, and gives
`Q=2/3` on the checked nonzero eigenvectors. But `H` uses two pieces of frame
data: the singlet axis `(1,1,1)` and a free doublet direction `h`. A single-axis
equivariant construction `a I + b vv^T` always commutes with
`Gamma_chi = 2vv^T - I`, so it cannot supply the required doublet datum. The
negative result is therefore narrow: frame-free ambient Clifford structure does
not source the chiral grading; a successful positive route must explain the
frame selection.

## Relation To Nearby Notes

This is the ambient-algebra companion to
[`CL3_CHIRAL_BODY_DIAGONAL_AXIS_FORCED_DOUBLET_H_NOT_SOURCED_NARROW_NO_GO_NOTE_2026-06-04.md`](CL3_CHIRAL_BODY_DIAGONAL_AXIS_FORCED_DOUBLET_H_NOT_SOURCED_NARROW_NO_GO_NOTE_2026-06-04.md).
That note analyzes the Lattice/body-diagonal side and separates the native
singlet axis from the unsourced doublet direction. This note analyzes the
one-site Clifford side and shows that equivariant ambient operations do not
produce the anticommuting grade-1 operator.

The result is also consistent with
[`KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02.md`](KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02.md):
the natural adjoint/Bloch/Hopf map quotients the spinor sign rather than
transporting it to the vector-grade sign partition. Both notes isolate the
same type of missing non-equivariant frame data.

## No-Go Discipline Gate

**Status:** PASS for the scoped claim only. The claim closed here is not
"nothing can ever source the chiral grading" and not "`Q=2/3` is unreachable."
It is only that the frame-free ambient Clifford operation class does not source
an operator anticommuting with `Gamma_chi`.

### N1 - Alternative Route Enumeration

| route | what it would attempt | outcome | marker |
|---|---|---|---|
| Grade-sign operations | Use grade involution, reversion, Clifford conjugation, or pseudoscalar conjugation as the source. | Each is `+I_3` or `-I_3` on grade-1; a nonzero scalar cannot anticommute with `Gamma_chi`. | ATTEMPTED |
| Hodge/pseudoscalar map | Use `omega` to send grade-1 vectors to bivectors and return a non-scalar source. | The map is index-identical on the `su(2)` vector labels, hence scalar for the tested grade-1 endomorphism. | ATTEMPTED |
| Even-subalgebra adjoint | Conjugate grade-1 by the unit quaternion whose adjoint action is `Gamma_chi`. | The result is `Gamma_chi` itself, so it commutes with `Gamma_chi` rather than anticommutes. | ATTEMPTED |
| Bivector commutator route | Use `[b_k,-]` as an ambient source. | These are antisymmetric rotation generators; the checked generators do not anticommute with the symmetric `Gamma_chi`. | ATTEMPTED |
| General equivariant endomorphism | Let any frame-free Spin(3)-equivariant grade-1 endomorphism act. | The exact commutant calculation gives only `c I_3`; no nonzero scalar anticommutes. | ATTEMPTED |
| Single-axis equivariant construction | Build from the body-diagonal projector as `aI + bvv^T`. | Every such operator is a function of `vv^T` and commutes with `Gamma_chi = 2vv^T - I`. | ATTEMPTED |
| Chosen-frame L4 family | Use `H=(1/3)(1h^T+h1^T)`, `sum(h)=0`. | It works, but it requires a chosen singlet axis and free doublet vector; this is outside the frame-free ambient class. | OPEN |
| Lattice/dynamics/sector route | Supply the axis and `h` from lattice geometry, momentum, dynamics, or sector factorization. | Not tested here; these routes explicitly add frame data and are left open. | OPEN |

### N2 - Wall-Independence Audit

There is one collapsed wall: frame-free Spin(3)/Pin(3) equivariance on grade-1.
The individual operations above are examples of that wall, not independent
walls. Once equivariance is dropped, the L4 family supplies anticommuting
operators, so the note does not claim independence from frame choice.

### N3 - Hidden-Wall Scan

The load-bearing inputs are explicit:

1. the Quantum axiom's one-site `Cl(3,0)` / `M_2(C)` carrier;
2. the grade-1 spin-1 representation matrices;
3. the exact matrix `Gamma_chi = (2/3)J - I`;
4. the exact commutant calculation `[M,L_k]=0 -> M=cI_3`;
5. the grade-1 bridge used only as a test surface.

No measured mass, PMNS entry, species identification, source/action bridge,
Born weight, log-det structure, or physical-unit map is consumed.

### N4 - Residual Matching

| cited witness | residual it addresses | residual here | match |
|---|---|---|---|
| [`CL3_CHIRAL_BODY_DIAGONAL_AXIS_FORCED_DOUBLET_H_NOT_SOURCED_NARROW_NO_GO_NOTE_2026-06-04.md`](CL3_CHIRAL_BODY_DIAGONAL_AXIS_FORCED_DOUBLET_H_NOT_SOURCED_NARROW_NO_GO_NOTE_2026-06-04.md) | Lattice/body-diagonal axis is native, doublet `h` is not selected by the tested cube structures. | Ambient Clifford operations also fail to supply the doublet datum. | yes |
| [`KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02.md`](KOIDE_ADJOINT_MAP_QUOTIENTS_SPINOR_Z2_NARROW_NO_GO_NOTE_2026-06-02.md) | Natural adjoint map kills the spinor sign; a non-equivariant frame is still needed. | Frame-free grade-1 Clifford operations are scalar or commuting; a non-equivariant frame is still needed. | yes |
| [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) | Cyclic-circulant operators cannot anticommute with `Gamma_chi`. | Spin(3)-equivariant ambient operations also cannot anticommute. | partial, used only as context |
| [`KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md) | If an anticommuting L4 operator is supplied, its nonzero eigenvectors give `Q=2/3`. | The supplied L4 family exists only after frame data is chosen. | existence check only |

### N5 - Rhetoric Audit

"Do not source the chiral grading" means only "do not source it within the
frame-free ambient Clifford operation class." It is not a claim about all of
`End(R^3)`, all lattice operators, all momentum constructions, or all
dynamical selections. The tested resolution is the grade-1 vector block of the
one-site Clifford carrier; broader lattice-wide and sector-factorized
resolutions are explicitly outside the claim.

### N6 - Partial-Closure Path Scan

The note does not say a new axiom is required. Two non-axiom partial-closure
paths remain open:

1. a Lattice/body-diagonal route that supplies the singlet axis and then still
   needs a doublet direction, as isolated by the body-diagonal companion note;
2. a momentum, dynamics, or sector-factorization route that supplies both the
   singlet axis and `h` without a hand choice.

Either path would bypass the scoped no-go because it would no longer be
frame-free.

### N7 - Steelman

A hostile reviewer could argue that the Lattice axiom already contains a
distinguished cube body-diagonal and that the body-diagonal companion note
therefore makes the "chosen axis" less arbitrary than this note suggests. A
future finite-lattice or momentum-sector theorem might also derive a particular
doublet `h`, making the L4 operator selected rather than posited. That would be
a real positive route, and this note leaves it open. It would not contradict
the scoped statement that the frame-free ambient one-site Clifford operations
listed here are scalar, commuting, or non-anticommuting on grade-1.

### N8 - Cross-Cycle Echo

Earlier Koide chiral-gate work repeatedly found the same residual shape:
equivariant or natural maps preserve/quotient too much symmetry, while the
positive `Q=2/3` route needs frame data. This note avoids turning that pattern
into a universal foreclosure by landing only the ambient-Clifford operation
case and naming the live frame-supplying routes.

## Falsifiers

- An error in the exact commutant solve or in one of the named operation
  matrices.
- A frame-free Spin(3)/Pin(3)-equivariant grade-1 endomorphism that is not a
  scalar and anticommutes with `Gamma_chi`.
- A proof that one of the tested ambient Clifford operations has a different
  grade-1 action from the runner matrix.

## Next Work

The useful next target is not another frame-free ambient operation. It is a
positive source of frame data: a lattice, momentum, dynamics, or sector
factorization theorem that supplies the singlet axis and the doublet `h` without
hand selection.
