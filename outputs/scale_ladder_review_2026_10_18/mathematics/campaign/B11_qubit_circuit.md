> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# B11 findings: the parameter-free Weyl step as a qubit circuit



- **Exact finite-depth circuit.** W = S·R_L·U_H·U_L is an exact, finite-depth, range-1 fermionic circuit on the corner code.
  - **R_L.** The link graph splits into disjoint π-flux 4-cycles, three per site. Each block is H = A + B with A² = B² = 1 and {A,B} = 0, so R_L = A·exp((π/4)AB): plaquette-diagonal π/4 rotations plus signed swaps.
  - **S.** S = D·S_B·S_A, where:
    - S_A swaps plaquette diagonals, {d,e}@v ↔ {−d,−e}@v+d+e;
    - S_B swaps on-site antipodes;
    - D is a sign layer.

    The flow index is zero on every axis.
  - **On-site factor.** A Givens elimination gives 60 two-mode rotations.
  - **Depth.** This elimination order gives 25 two-mode layers (38 counting phase gates). The check finds a Clements mesh gives 2-mode depth 12+2+2 = 16 (17 with the phase layer). So the 2-mode depth is ≤ 16; the minimal depth is not determined. (An earlier claim about a 5³ block embedding was unsupported and is withdrawn.)
- **Qubit mapping (C20 dictionary).** Every generator maps to c1·P1 + c2·P2 with commuting Paulis, |c| = 1/2. All 5248 Paulis commute with every stabilizer.
- **Clifford status.**
  - These are statements about the many-body Gaussian unitary Γ(U) and its corner-code image, not about the single-particle matrix itself.
  - Γ(S) is Clifford (a signed permutation with phases in {±1, ±i}).
  - Γ(R_L) is an exact product of Clifford gates and π/8 Pauli rotations, with T-count ≤ 12 per site.
  - The on-site factors are not exact Clifford+T (exact, measurement-free, clean ancillas), and neither is W:
    - U_H has entries (±√3 ± i)/6, and U_L has entries (1+2i)/3 and ±(1−i)/6;
    - a product of W entries equals (1+√3)/36, which lies outside Q(ζ₈).
  - Approximate synthesis is always possible, since Clifford+T is universal.
  - W is a supplied Gaussian free-fermion circuit; the standard efficient simulation applies to Gaussian states/observables and the usual accessible free-fermion setting, not arbitrary encoded interacting input/output tasks. These claims concern exact gate-set synthesis only.
- **Verification.**
  - At the fermion level the circuit equals W to 3.4e−15.
  - At the qubit level, Heisenberg checks modulo stabilizers pass for S (15/15), one R_L block (5/5), one on-site layer (4/4) and the full W (2/2).
  - Control: deleting one rotation gives a residual.
- **Supervisor follow-up** (`B1_parameter_free_corner_step/clifford_family.py`).
  - The only symmetric on-site signed permutation is the identity.
  - Words of length up to 4 in S, S⁻¹, R_L and i-phases give no Weyl doublet at k*.
  - So no on-site Clifford choice in this search gives a Weyl doublet. Exact Clifford+T on-site factors remain open (check correction). The script execs a scratchpad file, so it is not reproducible from the repo alone.
