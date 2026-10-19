<!-- Original PR9807 source SHA256 131206ec3c5d55ec5273b0cd5c596549c5f97ff3e8d9319211391803cae2a0ce. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native mobile charged whole-column pole

Status: conditional-support. A distinct light charged constituent is derived from the supplied one-qubit Hamiltonian. “Charged” means the exact plane-symmetry character below, not electric charge. No fermionic statistics or empirical particle identification is established.

Inputs: WHOLE_COLUMN_MODE_PROOF.md (native winding coefficient), SIX_LAYER_NEUTRAL_POLE_PROOF.md (diagonal sixth-order coefficients), ISOTROPIC_BOUND_FEATURE_PROOF.md (all-polynomial low-energy embedding), and REFLECTION_GROUND_SECTOR_PROOF.md (existence of a positive-plane global ground). Fix L10, even R and J>0, lambda tending to zero.

## Sector and feature

D_r=product_z X_(r,z) flips all ten spins in one column. It preserves wall count and every physical X/Y plane character, since its Y intersection has even size ten. It reverses every horizontal Z-plane character. Hence it maps the positive-sector global ground to X/Y positive, all Z negative. The original neutral distance-two ZZ observable commutes with those charges and cannot create this particle from the vacuum.

In the column encoding this is odd column parity. No locally flat Q0 pattern has odd parity on an even torus. Its minimum defect count is Q4, whose syndromes are rectangle corners with odd area. The minimum perimeter eight occurs only for the single-column pattern, a filled 2×2 bad-plaquette square. The next odd rectangle has perimeter twelve and costs an additional JDlambda6, D=3L/1024. Larger Q is separated at order lambda4. All-Q positivity excludes a competing extensive-charge low state.

Thus one translate per site supplies the isolated charged branch. Its gap from the positive global ground is

 epsilon_c(0)=J Delta lambda4+J(8a+16b)lambda6+O(Jlambda8),
 Delta=L/16, a=25L/18432, b=3L/8192.

Here the term linear in Q contributes 8a and perimeter eight contributes 16b. Momentum-independent corrections at higher orders are retained in a common energy, not silently set to zero.

## Native motion and microscopic transfer

The existing winding -Jgamma lambda10 Eedge moves a single column to its nearest neighbor. Gamma=12155/33554432. Both directions have the same negative matrix element. In its one-state-per-momentum reduction,

 epsilon_c(q)=e_c(lambda)-2Jgamma lambda10(cos qx+cos qy)+later.

Direct winding corrections begin at lambda12. Excursions into other odd Q4 shapes first produce lambda14 corrections, using their lambda6 separation. Finite-order paths have uniformly bounded displacement moments, so

 epsilon_c(q)-epsilon_c(0)=Jgamma lambda10|q|²
       +O(Jlambda12|q|²+Jlambda10|q|4+JR²lambda^M).

For any fixed R~lambda^-p, p>0, and q=2pi n/R, fixed n≠0, choose final absolute remainder order M>10+4p. The all-polynomial positivity construction isolates this low-energy odd sector from walls without requiring whole-band separation. Within each exact momentum and plane fibre the branch is separated from other odd shapes at order lambda6. The resolved positive quadratic increment transfers to the actual microscopic pole. No continuous derivative theorem or fixed-lambda infinite-volume assertion is made.

## Original charged readout and its dressing

Normalize D_q=R^-1 sum_r exp(iq·r)D_r. Distinct single-column images of the flat orbit vacuum are orthogonal for sufficiently large R, so the leading Bloch source has norm one. A local D_r instead has weight 1/R² at a specified momentum. This normalization is not 1/sqrt(LR²).

For the original, rather than artificially dressed, operator, let S1=A+B be the leading wall-elimination generator, with B odd under D_r conjugation. Only the 2L incident YY bonds occur in B. Each creates four walls, cost8J, with generator magnitude lambda/8. D_r S1 D_r=A-B. Expanding e^S D_r e^-S gives the second-order term [2B²+[A,B]]D_r. Distinct x/y bonds cannot return to N0 in two insertions, so the mixed projected commutator vanishes. Anti-Hermiticity gives

 P0 B² P0=-(2L)(lambda/8)²P0,
 P0 e^S D_r e^-S P0=[1-Llambda²/16]D_r+O(lambda4).

The off-block canonical second-order generator contributes no further P0 commutator. This formula is frame specific; state and operator rotations must remain matched. The transverse checkerboard Z product maps lambda to -lambda and commutes with D_r at even L, excluding odd powers in the physical residue.

Vacuum winding dressing starts at lambda6; charged shape mixing starts at lambda4 and is orthogonal at its first insertion to the one-column source. Neither affects the lambda² result. Every retained Fourier-source correction is a normalized translated finite-pattern sum. Its Gram matrix has bounded overlap multiplicity, uniformly in R, because distinct finite defect patterns are orthogonal unless their supports coincide up to one of finitely many translations. Charge change excludes a scalar-vacuum coherent piece. This controls the retained source corrections without a triangle-inequality area loss.

The Hamiltonian-tail projector error is O(R²lambda^(M-6)); even multiplying by ||D_q||<=R gives O(lambda^(M-6-3p)). Choose M>10+3p for an O(lambda4) source remainder. A sufficiently high operator transformation tail is included as well. The actual original charged-source pole weight is therefore

 1-Llambda²/8+O(lambda4)=1-(5/4)lambda²+O(lambda4).

Some weight leaves the low-wall pole; the microscopic D_r remains unitary. The exact physical-bond coefficient control neutral_charged_column_control.py verifies cancellation of all nonincident terms and the area-independent second-order coefficient on R4,8,12. It is a perturbative sign/control calculation, not a full-grid diagonalization.

## Relation to the neutral modes and remaining physics

This supplies a mobile constituent in the same low-wall space as the neutral modes, unlike the earlier N2 defect of rest energy order J. Two well-separated columns have leading energy2JDelta lambda4. Adjacent columns form the neutral Q4 feature of leading energyJDelta lambda4, while separation two gives the Q8 bound cluster with binding JDlambda6 below the separated-column threshold. These energies and motion follow from the existing plaquette and winding terms; no attraction is supplied.

Distinct microscopic D_r commute. The encoded spin operators admit a hard-core spin/bosonic description but are not canonical bosons, and this construction supplies no fermion exchange sign. A native scalar–constituent vertex or scattering residue still requires a separate calculation; symmetry permission and binding alone are insufficient. No electric charge, universal gravity, Lorentz invariance, scale calibration or detector identification is inferred from this pole.
