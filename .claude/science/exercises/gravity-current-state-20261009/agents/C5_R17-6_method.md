# R17-6 method, fixed 00:52Z 2026-10-13, before any run

## Helicity identification (stated in advance, as TESTS:5981 asks)
On Z^3 with only proper cubic rotations O, "helicity" is defined only through
little-group characters at small k along the three symmetric directions:
- C4 axis (k || z): eigenvalue e^{i pi h/2}: h = +-2 -> (-1,-1); h = +-1 -> (+i,-i); h = 0 -> +1.
- C2' face diagonal (k || 110): e^{i pi h}: h = +-2 -> (+1,+1); +-1 -> (-1,-1); 0 -> +1.
- C3 body diagonal (k || 111): e^{2 pi i h/3}: h = +-2 -> (w, wbar) (same as +-1); 0 -> 1.
A branch pair is "helicity +-2" iff (i) it has (-1,-1) on C4 axes AND (+1,+1) on C2'
face diagonals AND (w,wbar) on C3 diagonals, and (ii) it has nonzero residue in the
TT components of the stated metric readout (a local covariant label carrying E+T2).
Vector channel = C4 eigenvalues +-i (and C2' -1); scalar = C4 eigenvalue +1 created
by the readout's longitudinal/trace components.

## In practice
- (a) Representation theory: compute, for every Wyckoff position of P432 and for
  the natural (pure permutation) action and the shift action, the O-content of
  slot labels at Gamma and R (O-invariant points) and on the stars of X and M.
  T2 present or absent is the output. Frobenius reciprocity is the proof method.
- (b) Any ED: classify lowest levels at each cluster momentum on a C4 axis by the
  cluster's C4 (about k) eigenvalue; report energies per sector; no extrapolation;
  label cluster size. Gaplessness is never inferred from a cluster.
- (c) Z2 analogue of R15-3: attempt an f-sum (Bogoliubov) partner lemma using only
  continuity of m1(k) at k = 0 (quasi-locality) and Schur on E+T2; and the Goldstone
  route. State hypotheses; no Kato/Gaussian continuity is assumed.
- Readings are those of TESTS:5956-5986 (CANDIDATE / OBSTRUCTED / OPEN), unchanged.
