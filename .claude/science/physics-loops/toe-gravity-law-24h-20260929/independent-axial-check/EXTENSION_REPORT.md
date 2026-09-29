# Independent radius-one cubic-momentum and mixing extensions

This supplements `REPORT.md` on 2026-09-29. It remains a focused mathematical check, with no formal audit, landing verdict, physical identification, or premise adoption. Source revision and the original frozen CC runner remain unchanged.

**Result:** the exact radius-one obstruction survives the addition of every diagonal P³ monomial to G3 and the explicitly enumerated momentum-linear constraint-mixing kernels. Every matrix entry was independently reconstructed with explicit 11-site torus functional derivatives. The supplied dual certificates were then recombined against those independently obtained equations. Both give `0=-1`.

The larger certificate uses **no** continuum restriction on the new P³ or mixing terms. It remains valid when every new-term continuum moment equation is removed. This is a consequence of the verified certificate support, not an assumption that such moments vanish or an extrapolation of the solver's reported outcome.

## New frozen inputs

Exact copies are preserved with `_start` suffixes in this directory; `EXTENSION_INPUTS.json` binds them.

| Input from `nonlinear-evidence/` | SHA256 |
| --- | --- |
| `axial_cubic_momentum.py` | `6087d885109dc37e0f0ddd5f3b760fc209b86407228a2bdf927e301a2a5c9f21` |
| `axial_constraint_mixing.py` | `af7cb28e5d175138d2176e8214f70066c3ae4cf6e0cad1158f1c123e677cf647` |
| `axial_r1_cubic_momentum_system.json` | `35c7e11c7d9cb8986d4d87cb1bc798f8c8d0451b6c83a9909f33168c55c9ed59` |
| `axial_r1_cubic_momentum_rational.json` | `537208374f81b9e076c5f5ae62ee38e11735151437c726aa9accbea68a6aeade` |
| `axial_r1_constraint_mixing_system.json` | `3e988e0ff71d5662ea7f88f651a98fa9f9d572da3f54c25502f4d654cc3fdb34` |
| `axial_r1_constraint_mixing_rational.json` | `8018524496d4cd2195030668b5c6438db3ea359c185a04cec0b8893c767aebaf` |

Both new scripts were read completely. Their assembly functions were not imported or executed. Their serialized system coefficients were read only after independent reconstruction, and their witnesses only after complete matrix comparison. Author findings were disclosed in the coordinator's dispatch; this is mathematical and implementation independence rather than a blind review.

## Equations and support actually tested

Retain the original fixed C1, T2 and G1 and the V2, T3, G2, F1, U0 bases in `REPORT.md`. All coefficients below are independent real unknowns, with no axial symmetry reduction.

1. **Cubic momentum:** G3 gains all 56 unordered degree-three products from the six momentum slots `(P,Q,R)` at edge endpoints x,x+1. Their contribution to the degree-two, momentum-quadratic mixed equation is exactly `{G3(P³)[X],C1[N]}`. The bracket sign is negative for a momentum derivative paired with C1's coordinate derivative. Terms involving B or C momenta can contribute; terms with only A momenta lie in this bracket's kernel. Every repeated factor is differentiated with its full multiplicity.
2. **CC mixing:** add `C1[Z1(P;N,M)]` to the CC degree-two right-hand side. Z1 contains every component P_i(x+p), p in {-1,0,1}, multiplied by every antisymmetric lapse pair with n<m in {-1,0,1}. There are 27 coefficients.
3. **GC mixing:** add `G1[W1(P;X,N)]` to the mixed degree-two, momentum-quadratic right-hand side. W1 contains every P component at endpoints p in {0,1}, X on any of the three nearby edges indexed -1,0,1, and N at either endpoint. There are 36 coefficients.

Thus the tested necessary equations include

`CC2: {C1,T3}+{T3,C1}+{V2,T2}+{T2,V2}=G2[F0]+G1[F1]+C1[Z1]`,

`GC1: {G1,V2}+{G2,C1}=C1[U0]`,

`GC2_P2: {G1,T3}+{G2,T2}+{G3(P³),C1}=T2[U0]+G1[W1]`.

The continuum G2 moments remain fixed to the positive Lie action. The P³-only certificate uses the longitudinal A,P pair (h moment -1 and P moment -2); the full mixing certificate uses the transverse B,Q pair (h moment +1 and P moment 0). Each certificate requires its two listed moments. The cubic-momentum and mixing extensions are the explicit ones above, not all possible redefinitions of phase space or all possible support families.

The independent implementation also reconstructs every imposed new continuum equation. For P³, the zeroth component sum and first moment of each separately differentiated factor vanish; repeated component labels accumulate the expected Taylor multiplicity. For Z1, antisymmetry kills the zeroth lapse moment and the first moment is weighted by m-n. For W1, offsets from its edge anchor are p-1/2 for momentum, xp for shift, and n-1/2 for lapse. These equations match the frozen payload exactly.

Requiring each new kernel itself to vanish through first spatial derivative is a separately supplied stronger condition than merely checking the asymptotics of the full constraint-valued right-hand side: C1 and G1 already contain derivatives. No general necessity claim for those kernel restrictions is made. The verified certificates avoid that issue by using none of those rows.

## Independent certificates

`check_extensions.py` uses the same independently constructed finite-torus functionals and coordinate derivatives as the original check. The additional residuals still have integer slot-position diameter at most 3: differentiating C1 shifts N at most one site from a G3 momentum endpoint; C1[Z1] has all factors within one site of a vertex anchor; G1[W1] has slot positions between -1 and 1. The unique labelled smearing anchor and L=11>6 therefore give the same injective local lift. This is exact comparison of coefficients, with no field samples and no floating-point tolerance.

| Expanded system | Unknowns | Serialized rows | Dual witness rows | Combined left side | Combined RHS |
| --- | ---: | ---: | ---: | --- | --- |
| P³ in G3 | 557 | 940 | 96 | Every coefficient zero | -1 |
| P³ plus Z1,W1 mixing | 620 | 979 | 121 | Every coefficient zero | -1 |

Every coefficient and right-hand side of both serialized systems matched, including the zeroth and first moment rows. All 557 or 620 unknown coefficients were included when recombining the corresponding witness.

The 96-row witness uses only CC2 (68 rows), GC1 (10), GC2_P2 (16), and one each of `continuum_G2_dh(0,0)` and `continuum_G2_dp(0,0)`.

The 121-row witness uses only CC2 (65 rows), GC1 (12), GC2_P2 (42), and one each of `continuum_G2_dh(1,1)` with weight -1 (right-hand side +1) and `continuum_G2_dp(1,1)` with weight +1 (right-hand side 0). It uses no GG1, uniform V2, continuum T3, F1 moment, U0 moment, G2 zeroth moment, P³ continuum moment, or mixing continuum moment row.

Accordingly, the larger certificate proves inconsistency even with arbitrary low continuum moments for the new P³, Z1 and W1 coefficients. It also does not require the other omitted normalization rows. It is stronger than the initial momentum-linear-G result, but only within these exact support and generator definitions.

The complete independently reconstructed witness rows, weights, coefficient arrays and right-hand sides are preserved in `cubic_momentum_independent_certificate.json` and `constraint_mixing_independent_certificate.json`. `extension_results.txt` records the exact comparisons and recombination summaries. No author's rank claim or expected contradiction was treated as proof.

## 3D projection and remaining limits

The omitted-coordinate argument from `REPORT.md` still applies: C1's shear derivatives vanish for axial lapses, so derivatives of P³ with respect to omitted shear momenta cannot contribute. In C1[Z1], axial restriction removes shear momentum factors and aggregates transverse displacement coefficients into the included axial slots. In G1[W1], discarded shear momenta vanish and transverse differences of the x-dependent kernels vanish; the surviving x component lies in the stated W1 basis.

This supplies a necessary restriction for the declared 3D family with those physical radius-one supports. It supplies no 3D sufficiency theorem. No radius-two or larger-support calculation, modified quadratic kinetic stencil, different flat background, altered canonical pairing, new generator family outside the displayed field-degree expansion, full nonlinear Jacobi identity, matter coupling, or record-formation mechanism is covered. Later changes to these input bytes or support hypotheses require separate coverage.

Executed from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/check_extensions.py > .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/extension_results.txt 2>&1
```

Exit 0; elapsed 3.22 seconds. Deadline/stop checks were active. No external compute, unmanaged worker, or heavy job was launched; writes stayed in the assigned independent-check directory.
