# T54 pre-registration (written before t54_test.py was run)

Question: can one state of the taste cube C^8 = (C^2)^3 be the dark candidate
that all three notes need (colour-charged for the mass step, SU(2)-charged for
the annihilation weight, gauge-neutral for darkness), and does the choice of
embedding (which qubit is the weak fibre) change the answer?

## Predictions (Sonnet 5.5, same-family)
P1  Embedding, fibre axis f in {1,2,3}: C^8 = (3,2)_{1/3} (6 states) + (1,2)_{-1} (2 states);
    zero gauge singlets; S0=|000> and S3=|111> have (C_F, j(j+1), Y) = (4/3, 3/4, +1/3) for EVERY f.
    PASS = all three axes give the same triple for S0,S3 and zero singlets.
    FAIL (a route exists) = some axis gives S0 or S3 a zero Casimir.
P2  The three axis-conjugate gauge algebras generate a Lie algebra that acts irreducibly on C^8
    (commutant = scalars). PASS = irreducible. FAIL = an invariant subspace containing S0,S3
    exists (then a covariant reading of "gauge-neutral" could isolate them).
P3  Traceless Y with two Y-neutral states forces Y = 0 on the other six. (algebra, no run needed;
    printed as a check).
P4  Many-body census, 8 modes, N_g=1: gauge-neutral states exist only at k=0 and k=8 (counts 1,1).
    N_g=2,3: neutral states at k = 4*n_L (B=L composites), first at k=4. Character-integral method
    must reproduce the brute-force N_g=1 result exactly.
    PASS = as stated. FAIL (neutral composite inside one generation) = a dark-composite route opens.
P5  Stability of N1 (5.323e10 GeV) with the seesaw Yukawa that reproduces m_atm ~ 0.05 eV:
    tau ~ 1e-30 s (lane figure 3.5e-30 s); Yukawa would need to be ~1e-24 times smaller for
    tau > age of the universe. PASS = within a factor 10 of the lane's 3.5e-30 s.

## Reading rules
- P1 and P2 pass  => the "which embedding" choice cannot rescue dark = gauge singlet; the wall is
  a wrong-candidate-list problem, not a charge-reconciliation problem (MISFRAMED).
- P1 or P2 fail  => STANDS or a route (report the axis / invariant subspace).
- P4 fail        => new route (neutral composite).
No outcome here is allowed to be called "solved": it only prices or reframes the wall.

## Addendum (written before adding Parts D2 and F, after Parts A-E had been run)
P6 (kills the Minimal-DM route inside the cube): at k=3 of the N_g=1 Fock space there is exactly one
    colour-singlet, SU(2) j=3/2, Y=+1 multiplet (4 states, a three-quark composite, B=1) containing a
    Q = T3 + Y/2 = 0 member. PASS = found with multiplicity 1. If found, the only neutral-component-of-a-
    multiplet object in the cube is an ordinary baryon-type composite, not a dark state.
P7 (look-elsewhere for the role-split route): the ladder M_k = alpha_LM^k M_Pl has ratio 1/alpha_LM = 11.0
    between nodes, so a factor-50 window (1-50 keV) contains 1 or 2 nodes for any placement; a keV node
    therefore is not evidence. PASS = 1 or 2 nodes in [1,50] keV.
