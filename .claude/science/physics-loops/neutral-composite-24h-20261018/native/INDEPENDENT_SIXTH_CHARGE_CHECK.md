# Focused sixth-order analytic-charge obstruction check

Disposition: PASS for the recursion, numerical sixth-order evidence, and conditional obstruction proof. The exact nonzero coefficient certification is still required before promoting the final obstruction to an exact theorem. No formal audit or pack edits; root retains authorship.

## Bloch recursion and canonical normalization

Write Ω=W+sum_(n>=1)lambda^n a_n with PΩ=W, and b=sum lambda^n b_n for the Bloch effective Hamiltonian relative to E0. Projecting (H0+lambda V)Ω=Ω(E0+b) gives b_n=W†V a_(n-1) and

a_n=R[V a_(n-1)-sum_(j=1)^(n-1) a_(n-j)b_j].

This is exactly the script's recursion; a_n lies in Q. M=Ω†Ω has M0=I. The recursive S²=M and T=S^-1 handle noncommuting coefficient multiplication correctly. Canonical orthonormalization is ΩT and therefore K=S b T, equivalently T Ω†(H-E0)Ω T. No missing symmetrization or sign was found.

An independent control constructs local matrices without importing the MPS package, evaluates the coefficient intertwining equation through order6, and computes M^-1/2 by the noncommuting binomial power series. It then compresses Ω†(H-E0)Ω directly and normalizes on both sides, rather than using the root square-root similarity. Intertwining residuals are below6.4e-16; canonical coefficient discrepancy at order6 is4.9e-15. This independently checks normalization and coefficient extraction, although it uses the inspected Bloch recurrence rather than claiming a completely unrelated perturbative derivation.

The resulting absolute up/down matrix element is .3480291188652526, agreeing with63/(128sqrt(2)) within1.3e-15. The K6 charge commutator Frobenius norm is3.937499999999987, consistent with63/16. These floating agreements do not alone certify exact rational-radical values or nonzero exact coefficients.

## Obstruction proof

Let Q(lambda)=Q0+lambda Q1+lambda²Q2+... be ANY analytic matrix-valued conserved charge in the finite canonical band, with Q0=sum_i tau3_i. H_eff=E0 I+lambda²K2+lambda⁴K4+lambda⁶K6+... is even by the staggered rung parity and canonical gauge covariance. The order6 equation is

[K6,Q0]+[K4,Q2]+[K2,Q4]=0.

All odd Q terms drop out because the matching odd K coefficients vanish; [E0I,Q6]=0. No assumption Q is even is needed. It is not necessary to solve the lower-order equations to establish the contradiction below.

For |u>=|up>^4 and |d>=|down>^4, Q0 eigenvalues are+4,-4. Reviewed exact K2/K4 linked expressions give BOTH states the SAME respective eigenvalues:

K2: -3/sqrt(2),
K4: -13/(16sqrt(2)).

Each XY term annihilates a fully polarized state, and every tau3_i tau3_j equals+1. Thus for arbitrary Q2,Q4, <u|[K4,Q2]|d>=<u|[K2,Q4]|d>=0, while

<u|[K6,Q0]|d>=-8 <u|K6|d>.

A nonzero exact latter element contradicts conservation. The numerical lower-eigenvector residuals are below2.3e-15 and agree with these exact lower-order formulas. Once root certifies nonzero K6, this is a valid finite perturbative exclusion of an analytic conserved deformation anchored at the specified Q0. It is stronger than merely finding [H_eff,Q0] nonzero.

## Scope and gauge

The statement concerns the specified four-rung low band, the small-longitudinal-coupling analytic expansion, and charge limit Q(0)=sum tau3. It does not exclude conserved charges with different zeroth-order limits, nonanalytic families, arbitrary finite spectral projectors, charged operators outside the band, other states/geometries, bulk emergent symmetries, or criticality. It does not prove a global physical no-go.

An analytic within-band gauge transformation with U(0)=I carries an analytic charge and its conservation equation between gauges. Thus nonexistence with this anchored Q0 is not evaded by a regular near-identity reparametrization; however changing the zeroth-order charge is a different question. The obstruction is local in parameter near zero, not a validity claim at equal couplings or for a uniform thermodynamic perturbation series.

## Controls and SHA256 snapshot

Control: /private/tmp/neutral-sixth-independent.py and JSON. No expensive full4096-dimensional exact diagonalization was required.

- `/private/tmp/rung_sixth_probe.py`: `9925b675e301d202abf6f44b3c9476aa6e576f4d3c113c9261b4c8da67e43655`
- `/private/tmp/rung_sixth_probe.json`: `0294af9ef9fc72f598f56ce7253a76e1d221f9afc3d10abde1f9d4c1f0537466`
- `/private/tmp/rung_sixth_probe.npz`: `7f977de8f72e09fb7164202cc3fac3f5f3be94c5f40a4b49bc75caa59675af71`
- `/private/tmp/neutral-sixth-independent.py`: `557a8620e900fe8a0580c43971d6b277e6039f0adbf3614fb5bb22d4f72d6c10`
- `/private/tmp/neutral-sixth-independent.json`: `5aa061dd262dd18550028fb7cc691b89a393f352aba5818e3e0e9d68fc6dad1a`

## Exact-certificate follow-up — prior condition discharged

Final disposition: PASS, now including the exact finite analytic-charge obstruction. Independently executed the exact certificate with its JSON destination redirected to /private/tmp, leaving the pack untouched. It returns -63sqrt(2)/256 exactly in QQ(sqrt(2),i); lower scalar coefficients are 0, -3sqrt(2)/2, 0, -13sqrt(2)/32, 0. The previous pending exact-nonzero condition is therefore discharged for the specified matrix element and model.

Checked the nonorthonormal coordinate convention explicitly. S diagonalizes the integer-valued local h and S†S=diag(8,4,2,2,2,2,8,4). The code uses S^-1 D S for ket action and the Gram-weighted conjugate up vector for the bra; this is the correct dual contraction. Independent exact assertions verify that the local up/down vectors each have norm squared8, have zero mutual Gram inner product, and have tau3 eigenvalues+1/-1. Four-rung normalized bra/ket contraction divides by8^4, so the coefficient has no missing norm factor. All root projected down columns below order6 are asserted proportional before their scalar coefficients are used; real matrices give the conjugate up result.

The canonical-equality argument is valid. A single V on P excites two zero-energy rungs, so RVP=-(1/(4sqrt(2)))VP and M2=PVR²VP=-K2/(4sqrt(2)). Thus S2=M2/2 commutes with b2=K2. At order4, K4=b4+[S2,b2]=b4. At order6 the general similarity expansion reduces to K6-b6=[S2,b4]+[S4,b2]; the possible additional product term is zero because [S2,b2]=0. Between up/down, both commutators vanish by their common b4 and b2 eigenvalues. Hence the certified Bloch element equals the canonical element exactly. Odd coefficients vanish by the same staggered parity covariance already verified, including the metric and its analytic square root.

The resulting exact nonzero order6 obstruction proves no analytic conserved charge with Q(0)=sum tau3 in this finite four-rung canonical low band. All earlier restrictions remain: it excludes neither differently anchored/nonanalytic charges nor bulk emergent infrared symmetry, equal-coupling behavior or a three-dimensional scalar. The all-entry K6 Frobenius commutator value63/16 remains a floating corroboration, not part of this exact single-element certificate.

The new pure-numpy neutral_rung_model.py has the same displayed h, Ds and kron construction as the previously reviewed MPS module. Its integer-valued matrices justify the exact certificate's integer conversion; it adds no rounding approximation. Removing the unnecessary quimb import does not change these finite model inputs. This review did not alter or rerun the live MPS workflow.

Exact follow-up hashes:

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_sixth_exact.py`: `c6731fddbcbbbcfe91d8c2a9e87786de99dae3d1f571a92c6ea28bc0944daba2`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_sixth_exact.json`: `16de066993fc90edc94c09c8bfa637488844e3384a5d859f349b600aaed3faa6`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIXTH_ORDER_COLLECTIVE_PROCESS.md`: `38f16a0d607c22baf9eed5cd4175fd190e6efd9bda26db38f487a681aecd30dd`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_model.py`: `c14c817d4067501b136a9818d436550af99f8445f220129152b0e37eebdd095d`
- `/private/tmp/neutral_rung_sixth_exact.json`: `5bb5bc68280783c8f7ab065bda21ff4183945ea63f88d6f0d9fb8fff00c5b5df`
