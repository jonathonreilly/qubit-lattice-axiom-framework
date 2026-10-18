# Independent native rung effective-Hamiltonian and observable check

Disposition: PASS for the finite three-rung weak-longitudinal-coupling expansion in the declared rung-parity sector. No formal audit, repository edit, new route, or equal-coupling/bulk extrapolation was performed. Root retains authorship.

## Perturbation formula and gauge

Let P project onto the tensor product of the isolated rung low doublets, E0=-6sqrt(2), Q=1-P and R=Q(E0-H0)^(-1)Q. Here PVP=0 and POP=0. In the canonical orthonormal (polar/direct-rotation) gauge, the low-band isometry through order two is

U=P+lambda RVP+lambda²[RVRVP-(1/2)PVR²VP]+O(lambda³),

where terms proportional to PVP vanish. Expanding U†OU gives the order-two coefficient

P[V R O R V+O R V R V+V R V R O]P

plus normalization anticommutator -(1/2){PVR²VP,POP}. The latter is zero here. Thus the script's expression is correct for this gauge and model; it would not be the generic formula when POP or PVP is nonzero. The first-order observable term P(ORV+VRO)P also vanishes here. Effective H has coefficient PVRVP with the negative-denominator convention used in the code.

The script's low@polar(low.T@W) is the canonical aligned isometry. Equivalently it is P_lambda W (W†P_lambda W)^(-1/2); this identity makes its gauge independent of arbitrary eigensolver rotations within the low band. It requires a separated band and invertible overlap, checked numerically on the displayed interval. The common polar gauge matters when comparing operator coefficients.

## Exact local algebra and coefficient checks

Built h and D independently from the displayed three-bit Pauli formula, without importing the source module. Exact SymPy algebra verifies the low projector

p=(h²-2sqrt(2)h)/16,

p²=p, p D_a p=0, and h D_a p=0 for all four longitudinal D operators. Therefore a longitudinal D takes the low doublet into the zero-energy rung subspace. The two projected generators t1=sqrt(2)pD0D1p and t2=sqrt(2)pD0D2p obey t1²=t2²=p and {t1,t2}=0 exactly.

A separate full512-dimensional calculation uses the bordered inverse R=(E0I-H0+P)^(-1)-P, rather than the source's tensor spectral-denominator construction. In an independently chosen low-doublet basis it reproduces:

K=-(1/sqrt(2)) sum_(bonds12,23)[I+(tau1_i tau1_j+tau2_i tau2_j)/2],

O2=(3/4)I+(3/8) sum_(all pairs12,13,23) sum_(a=1,2) tau_a,i tau_a,j.

Maximum entry errors are 8.0e-15 and 8.7e-15 respectively. First-order O error is 6.3e-16. These global coefficient checks are floating independent matrix controls supported by exact local identities; they are not a full symbolic512-dimensional certificate.

## Even powers and direct low-band control

The local G=X0X1X2 commutes with h, anticommutes with every D_a and acts as +I on p, all verified exactly. Acting with G on the MIDDLE rung sends V to -V, leaves endpoint O fixed, and is identity on the unperturbed band. Hence the canonical polar effective H and O are even analytic functions of lambda near zero while the isolated spectral band persists. Their errors after the quadratic terms are therefore O(lambda^4), not merely a numerically fitted exponent.

Independently used the spectral-projector isometry P_lambda W(W†P_lambda W)^(-1/2), without the source polar routine. At lambda=.02,.04,.08 the O errors divided by lambda^4 are 1.312043565,1.312907664,1.316373556. This confirms the reported asymptotic behavior. It does not provide an outward-rounded error bound over the whole interval or a radius of analyticity for larger volumes.

## Scope

The eight-dimensional local rung matrix is already a selected parity representation of four original qubits. The effective Pauli doublet is an encoding of its low band, not a new physical qubit or a claim that the unrestricted four-qubit rung has only two low states. Existing longitudinal bond strengths are scaled by explicit lambda; the expansion needs small |Jz/Jperp|. At general positive Jperp, effective interaction scales Jz²/Jperp and this dimensionless composite correction scales (Jz/Jperp)². No validity at equal couplings, infinite-chain uniform error, bulk3D scalar, physical source coupling, or emergent clock is established. Those limits remain open as stated.

Independent control files: /private/tmp/native-rung-independent.py and /private/tmp/native-rung-independent.json. Source imports quimb through neutral_tube_mps, but this review's local/matrix computation does not require quimb or its MPS optimizer.

## SHA256 snapshot

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_effective.py`: `60b2d6a7ddf33c8dabce577e858eba4d29b55d6b82b55a6231372c9becc23e8d`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_rung_effective.json`: `2823bd7c80d4c325947a115c34ddd374c77a7b45a0f61e14177f2288a33d26e4`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_tube_mps.py`: `57e33fa3c4fe6fcc3ccced0ed5c68bc8e782de9982c3ef483f83ff56b2896942`
- `/private/tmp/native-rung-independent.py`: `587d11fdf7fe7826a15c4164622f14ec3406aa8db6e1d48119751acaf07699f0`
- `/private/tmp/native-rung-independent.json`: `fedd784ad6449635c76bdd89839db6aa8ff45afc86687c292fcb937094af8804`
