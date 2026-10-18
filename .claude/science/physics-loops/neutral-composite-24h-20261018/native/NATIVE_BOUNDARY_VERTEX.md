# Neutral coupling derived from the existing native boundary

Status: exact-support and conditional finite numerical support. The source is the supplied native compass Hamiltonian, not an appended scalar interaction. This is a feature/environment partition calculation, not physical identification of a fermion or cosmological scalar.

Split the exact parity-rung chain into left/right regions. Each isolated region has the conserved G=product of X0 X1 X2 over its rungs. Every boundary D_a=(Z0,Z1,Z2,Z0 Z1 Z2)_a is odd under G. The existing boundary term V=-J sum_a D_a,left D_a,right therefore maps (++ ) to (--), and conversely, in the total G=+ sector. It has exactly zero matrix elements within either block. Here neutral means even under this particular region parity; it is weaker than neutrality under every plane symmetry. Do not conflate the two.

Write P=(++), Q=(--). The full native Hamiltonian has blocks H_PP=H_L+H_R restricted to P, H_QQ=H_L+H_R restricted to Q and H_QP=V_QP. Whenever E-H_QQ is invertible,

psi_Q=(E-H_QQ)^(-1) V_QP psi_P,

[H_PP+Sigma(E)]psi_P=E psi_P,

Sigma(E)=V_PQ(E-H_QQ)^(-1)V_QP.

This exact Schur complement derives an energy-dependent neutral-sector interaction from the original boundary bonds. Its coefficients are fixed by the same H and the chosen partition. No new microscopic coupling is supplied. It is not a new scalar particle: retained-state selection, locality of a low-energy reduction and an autonomous field limit still need justification. The projection/elimination identity is standard prior art; the native-sector construction and numerical check are this campaign's application.

For real E below the Q spectrum, Sigma'(E)=-V_PQ(E-H_QQ)^(-2)V_QP is negative semidefinite. If u is the normalized P component, the actual P weight of a normalized full eigenstate is Z_P=1/[1-<u|Sigma'(E)|u>]. This derivative is an exact normalization/memory correction, not a fitted field-strength parameter.

Root checks two two-rung regions, 16 original physical qubits, with positive rung parities and total G=+. Each region's G+ ground energy is -6.928203230276 and its G- threshold lies 1.464101615138 above it. The physical boundary coefficient is fixed at one. An auxiliary multiplier lambda only diagnoses the perturbation series around disconnected regions; it is not an adopted interaction change. Native V has norm4, while its action on the product ground state has squared norm4.

The second-order energy coefficient is -1.058475493514. At lambda=.01 the discrepancy from this expansion is -1.24e-8; at the physical lambda=1 it is -.431464641460. The exact total energy -15.346346595526 agrees with the independent native selected-sector solver. The odd-odd weight is .301934565388, so a weak-admixture truncation is not supported here. The initial product ground-state weight is only .472737268027, distinct from total P weight .698065434612.

The exact eliminated equation has residual2.83e-12, reconstructs Q to2.28e-13, and predicts the P weight from Sigma' to6e-14. The product-ground column of Sigma(E) has diagonal -.735913015211 and off-diagonal norm1.311478301218, demonstrating that the existing boundary induces substantial mixing among region-even product states. This is a derived finite coupling mechanism, not a common scalar charge, static universal potential, or proof of a weakly coupled effective scalar.

Next: retain this exact energy dependence while testing larger regions and operational neutral source response. Region shape, parity sector and supplied H remain explicit. No empirical observations have been fitted or independently tested.

## Derived source vertex

For a region-parity-even existing observable O with O_PQ=0, the effective transition operator is

O_eff(E_f,E_i)=O_PP+V_PQ R(E_f) O_QQ R(E_i) V_QP.

Its matrix element uses the actual P components; if these are normalized separately, multiply by sqrt(Z_f Z_i). This follows by substituting the exact Q components of both full eigenstates, not by fitting an observable. For the original left-region energy H_L, a tested transition at gap1.900055472644 has direct amplitude .329110095492. The P-only part is .795609755575 and the induced Q part -.466499660083; together they reproduce the full native result to1.3e-14. Overall amplitude sign depends on eigenvector phase; the interference and absolute weights do not. Dropping the induced vertex would therefore be quantitatively wrong even with an energy-correct reduced model. No independently chosen scalar-source coupling is involved. This derives an existing energy observable's finite transition vertex, not its cosmological identification.
