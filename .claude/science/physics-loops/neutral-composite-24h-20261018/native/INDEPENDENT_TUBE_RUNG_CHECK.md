# Independent exact thin-grid rung reduction check

Reviewed `native/TUBE_RUNG_REDUCTION.md` and `neutral_tube_rung_control.py`. The signs, logical ordering and longitudinal channels are correct for the stated all-positive rung parity sector.

## Direct local derivation

Use physical rung order 0=(0,0), 1=(0,1), 2=(1,0), 3=(1,1). In the +1 eigenspace of Z0 Z1 Z2 Z3, independent bits b0,b1,b2 determine b3=b0 xor b1 xor b2. This is an eight-dimensional coordinate chart on an invariant physical subspace.

The two physical x bonds are 0--2 and 1--3. Their −XX operators become respectively −X0 X2 and −X1. The two y bonds are 0--1 and 2--3. Since −Y_i Y_j acts as a double bit flip with coefficient +(−1)^(b_i+b_j), the first becomes +X0 X1 Z0 Z1. The second flips only logical bit 2 and has phase b2+b3=b0+b1, giving +X2 Z0 Z1. This yields exactly

h=−X0 X2−X1+X0 X1 Z0 Z1+X2 Z0 Z1.

The order places X flips to the left of the computational Z phase. X0 X1 Z0 Z1 is Hermitian: reversing it produces two minus signs, hence no net sign change. X2 commutes with Z0 Z1.

Each physical Z becomes one of D=(Z0,Z1,Z2,Z0 Z1 Z2). Therefore the four existing longitudinal −ZZ bonds compress to v=−sum_a D_a tensor D_a on each adjacent rung pair. No transverse coefficient, physical lattice spacing, or extra coupling is introduced.

The longitudinal distance-two neutral column becomes sum_a D_a,z−1 D_a,z+1 with positive coefficients, as stated. This column is the longitudinal component of the relevant composite; it is not a claim that every component of an isotropic three-dimensional observable survives unchanged in a 2x2 cross section.

## Exact invariant-sector scope

Each rung parity commutes with every physical transverse bond (two flips) and every longitudinal bond (Z type). Thus the selected subspace is exactly invariant under H: there is no projection leakage. This differs fundamentally from the earlier unprotected even-X-dimer variational compression.

Selecting positive parities is nevertheless a sector choice, not a derivation that this sector is physically prepared or globally lowest. Other parity patterns can change signs in their corresponding compressed operators and must not be silently discarded. The eight-state rung basis uses three logical coordinates for four existing physical qubits subject to a conserved constraint; no new microscopic qubits or interaction are supplied.

The resulting 2x2xL family is a thin quasi-one-dimensional benchmark. Increasing L at fixed cross section does not establish the three-dimensional thermodynamic limit, bulk isotropy, scalar propagation, or physical coupling. Later variational approximations to this exact chain still need state/residual and convergence checks; exactness of the coordinate map does not make an approximate chain state stationary.

## Independent L=3 control

`/private/tmp/neutral-rung-independent-control.py` explicitly enumerates all 512 reduced computational states and maps each to its physical 12-bit even-rung-parity string. It applies each of the 20 original native bonds directly as physical bit flips and phases, building the 512x512 compressed integer matrix without constructing a full 4096x4096 matrix. This matrix equals the analytic three-rung sum of h and v exactly, entry by entry.

The same independent control applies all four physical distance-two longitudinal ZZ pairs and verifies exact equality with sum_a D_a tensor I tensor D_a. Integer arithmetic gives zero error in both comparisons. These checks extend the root's L=1,2 matrix controls and validate the rung ordering, −YY phases, boundary bond counting, and longitudinal composite simultaneously.
