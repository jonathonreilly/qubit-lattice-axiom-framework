# T-LANDAU pre-registration (written 2026-10-18T22:57Z, before any run)

Item: T-LANDAU in `masswall/TESTS.md` (readings fixed there, copied below unchanged in meaning).
Background read: `masswall/K/REPORT.md` + `K/scripts/k1_eg_landau.py`; `masswall/R1/REPORT.md`;
GEN-2 `campaign/GEN2/{PREREG,REPORT}.md` + `scripts/gen2_symm.py` on `claude/chirality-grid-exercise-20261014`.

## The gap this test must fill, and the premise I add (named)

GEN-2 fixes only the symmetry content (generation rep P = A1g + Eg on rod axes; Eg order forced for CKM;
first-order strain channel allowed at tree level). It builds no three-orientation rod Hamiltonian
("a three-orientation cell law has not been built", GEN-2 c1). So I must supply the smallest model
that has exactly GEN-2's content. Named premises (conditional, not derived):

- **P1 (fermions).** Three rod species a in {x,y,z} (rod axis = generation). Each is a free lattice
  fermion on Z^3 whose Bloch Hamiltonian is linear in nearest-neighbour hopping amplitudes.
- **P2 (order parameter enters linearly).** The Eg order Phi = rho (cos t, sin t), strains
  e_i = sqrt(2/3) rho cos(t - 2 pi i/3), couples linearly to fermion bilinears (Hubbard-Stratonovich /
  mean-field form). Its own tree potential is the isotropic HS term rho^2/(2G) only. So **every
  angular (cos3t, cos6t, ...) coefficient comes from the fermion determinant**; G is the one radial knob.
  A tree-level b3 or c6 for a fundamental Phi would be a free supplied number: outside this test.

## Models (fixed now)

**Channel A, kinetic/strain (primary; the lattice-scale channel GEN-2 c3/c4 force).**
Rod a has velocities v_{a,i} (i = direction): v0_{a,a} = eta (along its axis), v0_{a,b} = 1 (across), and
the general linear Eg coupling allowed by O_h on P (x) P (three E's in P(x)P, so three couplings):
    v_{a,i} = v0_{a,i} + l1 e_i + l2 e_a + l3 delta_{ai} e_a.
- Variant A-N (naive Weyl, all 8 nodes per rod): E_a(k) = sqrt(sum_i v_{a,i}^2 sin^2 k_i).
- Variant A-W (Wilson-Dirac, doublers gapped, strain scales every hop in direction i):
  E_a(k) = sqrt(sum_i v_{a,i}^2 sin^2 k_i + (sum_i v_{a,i}(1 - cos k_i))^2).
- Sea energy E_sea = -sum_a <E_a(k)>_BZ (common positive species factor dropped; it rescales G only).
- Grid: (l1,l2,l3) direction on a 120-point Fibonacci sphere (overall size absorbed in rho);
  eta in {1/3, 1/2, 1, 2, 3}. BZ midpoint grid N^3, N = 32 (convergence check N = 48 on a subset).

**Channel B, Yukawa/mass (secondary; exists only below EWSB).** Dirac fermions, isotropic kinetic
term, mass matrix linear in Phi: M = m0 1 + mJ (J - 1) + mu1 diag(e) + mu2 Off(e), Off(e)_{bc} = e_a
({a,b,c} distinct) (the A1 and the two E structures of End(P) that are real symmetric).
E_sea = -sum_n <sqrt(sum_i sin^2 k_i + s_n^2)>, s_n singular values of M.
Grid: m0 in {0.02, 0.2}, (mJ/m0) in {0, +-0.5}, (mu1, mu2) direction on 24 points of the circle.

**Admissibility (fixed now).** A: every v_{a,i} >= 0.05 min(1, eta) at the vacuum (no velocity sign
flip: node set and each rod's chirality unchanged). B: no constraint beyond M finite. Couplings and rho
up to the admissibility edge are all "admissible".

## Computation

1. For each coupling point, rho on a grid (40 values, 0 < rho <= rho_edge, rho_edge = largest rho at
   which the whole circle is admissible, capped at 1.5): V(rho, t) on 121 points of t in [0, pi/3]
   (fundamental domain; t = 0 and pi/3 are the two tetragonal lines), then golden-section refinement.
2. Angular class at each rho: **D2h** if the minimising t is >= 0.5 deg from 0 and pi/3; **TET** otherwise.
3. Realised vacua: rho is realisable for some G > 0 iff (rho^2, min_t V) lies on the lower convex hull of
   that curve with negative slope (then 1/(2G) = -slope). Classify the realised vacua.
4. Landau coefficients from the fermion determinant: Fourier modes V(rho,t) = V0 + V3 cos3t + V6 cos6t + ...
   (72-point projection); fit V3 = b3 rho^3 + b5 rho^5 + b7 rho^7, V6 = c6 rho^6 + c8 rho^8,
   V0 = const + a2 rho^2 + q4 rho^4 + ... on small rho. Check K's criterion (c6 > 0 and |b3| < 4 c6 rho^3)
   against the exact angular minimum.
5. Mean-field = one-loop here (P2), so "one-loop determinant and/or mean field" is one computation.

## Readings (from TESTS.md, fixed)

- **LANDAU-D2H:** some admissible coupling gives a D2h minimum (a realised vacuum, step 3). State the
  range, and whether it is generic or tuned. Pre-registered meaning: **generic** if D2h realised vacua
  occur for >= 5% of the coupling directions in a channel and survive +-10% changes of every coupling;
  **tuned** otherwise (e.g. only where b3 nearly cancels, or only at the admissibility edge).
- **LANDAU-TETRAGONAL:** every admissible coupling gives a tetragonal (or trigonal) minimum.
- **OPEN:** otherwise (e.g. D2h only at rho where the linear model is not trustworthy, or N-unconverged).
- Reading per channel; overall = D2H if channel A or B gives D2H (TESTS: "some admissible coupling").

## Also reported (do not enter the reading)

- **Lorentz-violation cost.** Channel A: the fermion speed anisotropy max_{a,i,j}|v_{a,i}-v_{a,j}|/v at the
  vacuum, per unit rho (first order by construction). Channel B: none at tree level in the fermions; the
  cost moves to whatever field carries Phi (GEN-2 c4).
- **Mass levels.** At realised D2h vacua, unit strain direction e-hat(t*). Sector mass matrices
  M_f = a_f 1 + b_f J + c_f diag(e-hat), real, free per sector (K's form; GEN-2 End(P) structures).
  Score = R1/T score (max over sectors of half-spread of log(model/obs) + CKM |log|V|| for us, cb, ub).
  Search: (b/a, c/a) per sector on a 2D grid (signed, log-spaced 1e-4..1e3), t* over the realised D2h set.
  Data: HIER-2's three mass sets (as T/PREREG.md) and CKM 0.225, 0.041, 0.0037.
  Control: 200 random spectra, R1 generator (per sector r21, r32 log-uniform [1e-4,1]; |V| log-uniform
  [1e-3, 0.5]); same search. Also the tetragonal case (t* = 0): check that one generation is CKM-unmixed.

## My prediction (before running)

Channel A: b3 generic and nonzero (no symmetry forbids E x E x E for a uniform, T-even strain), so near the
transition the minimum is tetragonal; c6 sign not known to me. I expect D2h to occur only in a minority
of directions and mostly at large rho (strain ~ 0.3+), i.e. where Lorentz violation is O(1). Proved fact I
will use: E_sea is concave in Phi (ground-state energy of H0 + Phi.V is a minimum of affine functions),
which does not by itself decide the angular minimum.
