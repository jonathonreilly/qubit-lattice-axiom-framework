# Derived weak-longitudinal collective interaction and composite readout

Status: conditional-support. Native term structure is unchanged; the small ratio J_z/J_perp is an explicit diagnostic regime, not derived for the original isotropic J_z=J_perp model. No physical scalar or three-dimensional fermion identification is claimed.

The positive-parity four-site rung has spectrum -2sqrt(2) (twice), zero (four times), +2sqrt(2) (twice), in units J_perp. Write G=X0X1X2 in the exact three-coordinate representation. Its native transverse Hamiltonian is -(1+G)(A+B), for two anticommuting Hermitian involutions A,B. The low doublet has G=+; every longitudinal D_a is G-odd and maps it into the zero-energy G- subspace. The two-state feature is four original physical qubits with a low-energy restriction, not another qubit placed on each site.

Let P_r project onto the low rung doublet. Within it, tau1=sqrt(2) P_r Z0Z1 P_r and tau2=sqrt(2) P_r Z0Z2 P_r square to identity and anticommute, while P_r Z1Z2 P_r=0. Thus the collective Pauli algebra is derived from physical observables. A longitudinal boundary V=-J_z sum_a D_a tensor D_a has PVP=0 and reaches two zero-energy rungs, with energy denominator -4sqrt(2)J_perp. Its square projects to 4I+2(tau1 tensor tau1+tau2 tensor tau2). Different neighboring boundaries cannot return all rung parities to the low sector in two steps. Therefore

H_eff = -2sqrt(2)J_perp L - [J_z²/(sqrt(2)J_perp)] sum_bonds [I+(tau1_i tau1_j+tau2_i tau2_j)/2] + higher orders.

This fixes an XY-chain interaction and its coefficient from the existing microscopic terms. A standard rotation of the effective Pauli axes puts it in the XX+YY convention. This derivation does not certify a gapless phase at equal coupling: higher-order terms and thermodynamic control must be addressed. Finite-chain perturbation theory is controlled sufficiently close to zero longitudinal coupling by the isolated rung band; no volume-uniform error theorem is supplied.

The original neutral longitudinal composite on three rungs is O=sum_a D_a,0 D_a,2. It has POP=0 and no first-order matrix elements in the low band. With R=Q(E0-H0)^(-1)Q, the second-order polar-aligned observable is

O2=P[V R O R V+O R V R V+V R V R O]P.

Root's finite matrix calculation gives O2=(3/4)I+(3/8)sum_(i<j,a=1,2) tau_a,i tau_a,j. Thus the native composite couples to collective bilinears at order (J_z/J_perp)²; neither the collective interaction nor this coefficient was supplied as a scalar coupling. The displayed O2 coefficient identity currently has numerical finite-matrix support and independent canonical-projector checking completed; it should not be promoted to an exact symbolic theorem merely by recognizing rational coefficients.

Root compares these formulas against the exact low-eight-dimensional spectral subspace of the 12-physical-qubit Hamiltonian. Polar alignment removes arbitrary eigenvector/gauge rotations. At ratios .01,.025,.05,.1,.2, the Hamiltonian and observable errors scale approximately as ratio^4; relative error in O2 ranges3.91e-5 to.01599. This is model-development validation on the same Hamiltonian, not independent observational data. The low-band gap remains above2.20 in these finite tests. No equal-coupling extrapolation is claimed.

This gives a constructive, explicitly conditional route: low-energy multi-site features acquire dynamics and a composite readout through existing bonds. It does not yet provide a propagating3Dscalar, universal matter coupling, a cosmological state or physical scales. Those remain the campaign's hard residuals.

## Fourth order and finite symmetry test

For the canonical polar effective Hamiltonian, K4=P V R V R V R V P - {P V R² V P,K2}/2. Root computes this directly and checks the exact finite spectral low band; remaining errors scale as lambda^6. Every boundary V flips its two endpoint rung G parities. Returning to the all-low-rung band on an open chain requires each used edge an even number of times. Four insertions therefore use at most two distinct edges. Disjoint clusters cancel in the additive canonical effective Hamiltonian, leaving single-bond and adjacent-bond contributions. Independent checking confirms this support argument.

Define XY_ij=tau1_i tau1_j+tau2_i tau2_j and ZZ_ij=tau3_i tau3_j. The calculated dimensionless K4 (J_perp=1) has single-bond contribution [-I/32+XY_ij/16-5 ZZ_ij/32]/sqrt(2), plus adjacent-bond triple contribution [-I/8-(XY_ij+XY_jk)/16-3 XY_ik/16]/sqrt(2). Finite2,3,4rung checks agree below5e-15. The coefficients are supported by finite numerical algebra and independent reconstruction; no interval/symbolic certification of every rational coefficient is claimed. Restore dimensions with J_z^4/J_perp^3.

This produces collective interactions beyond the free XY limit from the original bonds. K4 commutes with undeformed total tau3, but the exact four-rung polar effective Hamiltonian does not: its commutator norm divided by lambda^6 approaches about3.94 in the tested weak-coupling range. At .05 the commutator is6.17e-8 against eigenpair residual4.1e-14. This is evidence for higher-order breaking of that specific emergent charge, not exclusion of every possible dressed conserved quantity. An all-up/all-down matrix element also appears, about .34905lambda^6 at .05; no all-orders or thermodynamic symmetry conclusion follows.

The leading collective dynamics and readout are derived, while their simplification to a free conserved scalar would still be an extra assumption. This distinction is why the actual higher-order interaction is retained.

The later exact sixth-order certificate and finite analytic-charge obstruction are in SIXTH_ORDER_COLLECTIVE_PROCESS.md; this supersedes the merely undeformed-charge numerical limitation above for that narrowly specified analytic continuation. It does not supersede the bulk/equal-coupling limits.
