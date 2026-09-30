# T24 pre-registration (written BEFORE any T24 script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor Opus 5.5; same-family checks).
Wall: T24 = L05-W9, doublers (8 or 16 copies, no rule to keep or remove them).

## Conjecture (route R1, "the count is a symmetry-class theorem, not a missing rule")
For a local, translation-invariant, Hermitian two-band symbol H(k)=d0(k)+d(k).sigma on Z^3
with the qubit as coin:
 (P) if the proper cubic group acts on the coin as a spinor (full soldering, T20) then every corner
     k=pi*n, n in {0,1}^3, has d=0, for EVERY range. Reason: each corner's stabiliser in O contains two
     perpendicular 2-fold rotations, whose spinor lifts anticommute, so H(pi n) is a scalar.
     Even a tetragonal D4 alone pins all 8 corners; an abelian (C4z-only) covariance does not.
 (K) if instead only Theta=sigma2 K (Theta^2=-1) is imposed, d is odd, so d=0 at the 8 TRIMs (same corners).
 (M) dropping both gives a 2-node symbol (Nielsen-Ninomiya floor): the price of removal.
 (L) a period-2 covariant term eps(x)*G (G even-displacement covariant convolution) has spectrum
     E^2=|sin k|^2+m(k)^2 exactly; its corner values take only two numbers (singlet pair, triplet pairs),
     so the reachable light sets are {none, singlets, triplet pair hw1+hw2, all}: never hw1 alone.

## Test A (pinning, any range)  A_pin.py
 A1: 200 random covariant symbols (full soldering) for each range r in {1,2,3} by group-averaging random real
     trigonometric polynomials over the 24 rotations with spinor lifts. PASS: max over samples and corners of
     |d(pi n)| < 1e-10. FAIL: any sample above 1e-8. Controls that must NOT pass (else the test is vacuous):
     random non-covariant Hermitian symbols (median max|d(corner)| > 0.1), trivial-coin covariant symbols
     (d scalar-invariant), C4z-only covariant symbols (corner (pi,0,0) NOT pinned in >90% of samples).
 A2: node census with multi-start Newton on d=0 over the torus, chirality = sign det J. PASS: sum of
     chiralities over ALL found nodes = 0 in every sample (validates the finder and Nielsen-Ninomiya), the
     8 corners are always among the zeros, and corner chirality patterns are reported.
 A3: Kramers-only symbols (d odd, no rotation): d(TRIM)=0 (PASS).
 A4: explicit 2-node symbol d=(sin kx, sin ky, -cos kz +2 -cos kx-cos ky... ) : exactly 2 nodes, chirality +1/-1,
     Theta broken, C2x broken, C4z kept. PASS: exactly those. FAIL: other counts.

## Test B (exact diagonalisation, period-2 term)  B_lift.py
 Torus L=8 (1024 states). H=sigma.S + eps(x)(s*Gs + t*Gt), Gs=2(1+sig2), Gt=3-sig2, sig2=cxcy+cycz+czcx,
 eps=(-1)^(x+y+z). PASS: zero-mode counts 16 (s=t=0), 12 (s!=0,t=0), 4 (s=0,t!=0), 0 (both), the spectrum
 equals +-sqrt(|sin k|^2+m^2) to 1e-10, and for random covariant even G (rank<=3, projected to vanish on
 singlets, or on triplets, or neither) the counts are only in {0,4,12,16}. FAIL: any count in {2,6,8,10,14}
 (which would be an unpaired chirality or a hw1-only light set).

## Test C (count census, units)  C_census.py
 Zero-mode counts of: walker sigma.S (L=4), Kawamoto-Smit one-mode staggered (L=4), naive 4-comp alpha.S (L=4),
 ordered tick S_xS_yS_z (L=12, states with U=+-1). Report in Weyl-equivalents (2 states per Weyl node).
 PASS (wall is unit-mixed): the four counts are not all equal, i.e. "8 or 16" compares unlike objects.
 FAIL: all four agree in Weyl-equivalents.

## What each outcome would mean
 If A1 passes and controls fail as required, and A4 gives 2 nodes: T24's count is equivalent to the symmetry
 premise (non-abelian corner stabiliser: SOLDER-T1 or Kramers), i.e. PRICED. If A1 fails for any covariant
 sample, route R1 is dead and T24 STANDS. If B finds a hw1-only light set, the mirror-lift claim is dead.
