# A54 notes: is the sign chi (dressed ring = chi bare ring chi) local?

## 0. Setting (2026-10-04)
- A52 objects, Z2 form. Links l (one qubit), corners v, plaquettes p. Hop t_l = X_l Z^{d_l}
  (d_l = record-conditioned field-factor set at both end stars, never l itself). Dressed ring
  S_p = prod_{l in dp} t_l = s_p X^{dp} Z^{d dp}. Bare ring R_p = X^{dp}. Gauss G_v = Z^{star v}.
- Matrix d (links x links): d[m,l] = 1 iff hop l carries Z on m. Tournament property gives
  d + d^T = D^T D over GF(2), where D = boundary map links -> corners (D^T D [l,m] = #shared corners mod 2).
  (Holds on every torus, also L=2 where two links share both corners: 2 = 0.)
- chi = (-1)^{Q(n)}, Q = sum_{l<m} A_lm n_l n_m + b.n  =>  chi X^x chi = +- X^x Z^{Bx}, B = A + A^T
  (symmetric, zero diagonal). Z4-valued chi (S gates) allows B symmetric with any diagonal.
- Requirement on the charge-free sector: (B + d) dp in im(D^T) (Gauss products) for every p,
  plus a sign condition handled by b.  On the infinite lattice with local B this is
  <dq, (B+d) dp> = 0 for all plaquettes p, q  (M := B + d vanishes on B_1 x B_1).

## 1. Theorem L (EXACT, derivation): no bounded-range quadratic chi exists on Z^3
Claim: for ANY local field-factor hop family with d + d^T = D^T D (all A52 tournaments, any record
background, covariant or not; also A45's y-gauge variants), there is no finite-range symmetric B
(+-1 or +-i valued chi) with (B+d) dp in im D^T for all p.  Same in every dimension >= 2; false in 1D.
Proof (infinite coarse lattice, finite-support chains; H_1 = H_2 = 0, H^1_c = H^2_c = 0):
 1. M = B + d local, M + M^T = D^T D (B symmetric). M dp = D^T g_p, g_p finite, local (complement
    of a ball is connected). g(d cube) = 0, so g descends to g^: Z_1 -> C^0 with M x = D^T g^(x).
 2. For x in Z_1, y in C_1:  x^T M y = y^T M x + (Dy).(Dx) = <Dy, g^(x)>.
 3. phi_v(x) := g^(x)(v) is closed on plaquettes, so phi_v(x) = <x, h_v>, h_v finite near v.
 4. Hence M y = H D y + D^T k_y (H e_v = h_v, k_y local), i.e. M = H D + D^T R.
 5. Then D^T Rt + Rt^T D = D^T D with Rt := R + H^T local.  Read as hops: c_l := Rt e_l gives
    Gauss-parity-dressed hops X_l G_{c_l} that are exactly fermionic (anticommute iff one shared corner).
 6. Lemma G (no local Gauss-dressed fermions, d >= 2): from (5) with y a finite cycle, Rt z is
    constant, hence 0, so s(u,w) := sum_{l in path u->w} c_l is path independent.  In d >= 2 a path can
    detour around any ball, so for far u,w: s(u,w) = alpha_u + alpha_w with alpha_u supported near u and
    independent of w.  Put x = path u->w, y = path u->v (u,v,w pairwise far) into (5):
    LHS = alpha_u(u) + alpha_u(u) = 0, RHS = |{u,w} cap {u,v}| = 1.  Contradiction.
 1D control: c_l = {left end of l} solves (5) (no detours exist; JW is local in 1D).
Translation-invariant shadow: Rt = A.D forced, and A + Abar = 1 is impossible (constant term of
A + Abar vanishes).  Obstruction in one line: a local splitting K + K^T of the corner dot product
has zero diagonal; d >= 2 locality forces K to extend to single corners, where the diagonal is 1.
Also repairs A52 Lemma R's last step ("own link + Gauss parities -> boson"): a single far Gauss factor
CAN flip one junction (t1 = X_l1 G_{x2} gives theta(1,2,3) = -1); Lemma G shows a local family cannot
make all junctions fermionic.

## 2. GF(2) scans (CHECKED), Z2 form, A52 hops (tournament T0)
c1_local_scan: unknown symmetric B with range^2 <= R2 (fine units), equations <dq,(B+d)dp> = 0 (p<q).
 - 2x2x2: solvable already at R2 = 2.  3^3: no solution R2 <= 6, solvable from 8.  4^3: none at 4,8,12;
   solvable at 16.  5^3: none up to 26 (max tested).  6^3: none at 8, 14, 16 (where 4^3, 4x4x6, 4x4x8
   are solvable at 14-16).  Thresholds 4x4x6, 4x4x8: 14; 3x3x5, 3x3x6, 4x4x5: 20.
 - Quasi-1D tori 2x2xL (L = 3..8): solvable at R2 = 2 (even L) or 4 (odd L) for every L: the 1D escape.
 - Random record mixtures: same thresholds/ranks (6^3: identical counts) -- A52 Lemma V: backgrounds
   differ by a local CZ pattern (range^2 4), absorbed into B once R2 >= 4.
c1b_ti_scan (translation-invariant B, uniform records, 4^3): no solution at ANY range up to the full
 torus (R2 = 48).  Control: translation-invariant bosonic hops X_l Z^{B0 e_l} (B0 range^2 4) -> detected
 exactly at R2 >= 4 (none at 2).  So every solution found on a torus is a non-invariant, torus-sized one.
c2_gauss_core (record-free core, Gauss-dressed fermionic hops): smallest admitted range (doubled units^2)
 1D rings L=4..16: 1 (= one endpoint, the local JW).  2D L=3..8: 9,13,25,37,49,65 (distance ~ L/2).
 3D L=3,4,5: 13, 29, 41 (torus max 17, 41, 57).

## 3. The explicit chi (c3_jw_chi, EXACT construction, CHECKED)
- Order corners; K[u,w] = 1 iff pos(u) < pos(w); Lambda = corner sublattice parity (even sizes).
  M = D^T (K^T + Lambda) D, B = M + d. Then M + M^T = D^T D, M dp = 0, B symmetric with zero diagonal,
  B dp = d dp exactly; a linear part b fixing all S_p phases exists. chi = (-1)^{sum_{l<m} B_lm n_l n_m + b.n}.
- chi X^{dp} chi = S_p as exact Pauli strings (every sector, not only charge-free): 0 mismatches on
  2x2x2, 2x2x4 (random), 4^3 (uniform, random), 6^3 (random).
- Spin-1/2 ice BFS (A52 c4 conventions): 0 failing edges (2x2x2 864 states complete; 2x2x4 60k capped;
  4^3 20k capped; 6^3 3k capped); chi equals A52's BFS chi up to one global sign (+1, +1, +1, -1).
- Non-locality grows with the torus: chi = CZ on 108 / 2400 / 14694 link pairs, farthest coupled pair
  distance^2 12 / 36 / 76 (2^3 / 4^3 / 6^3).
- Uniqueness: on each homology sector chi is fixed up to one sign by chi(n+dp)chi(n) = sign_p(n), so
  "non-local" is a property of the function itself, not of this construction.
- Dual description (EXACT): Gamma := D2^T d D2 (plaquette form) is local, symmetric, alternating, so
  chi(n) = (-1)^{sigma^T U sigma + lambda.sigma} with U = upper half of Gamma and any 2-chain sigma with
  d sigma = n.  chi is local in the dual (membrane) potential sigma, not in the field n.

## 4. Q2: what chi does to A52's hops (EXACT identity, CHECKED)
- chi t_l chi = +- X_l Z^{(B+d) e_l} = +- X_l Z^{M e_l} = +- X_l prod_{v in J(l)} G_v,
  J(l) = corners in the half-open order interval (pos a, pos b] of l's ends, xor Lambda at the ends:
  the Jordan-Wigner fermion hop, bare-ring frame.  Statistics unchanged (conjugation): 0 pair-rule
  violations, commutation matrix identical to A52's hops; 0 anticommutations with bare rings.
- String lengths (corners): mean 2.3 / 10.5 / 23.9, max 5 / 49 / 181 on 2^3 / 4^3 / 6^3.
- Consistency with Theorem L: bare rings + fermions needs Gauss strings; Lemma G says they cannot be local.

## 5. Spin-1/2 U(1) version
- Same chi works (EXACT): on ice states the dressed flip L_p has exactly the Z2 matrix element of S_p
  (field factors sigma^axis = Z in the field basis; sequential signs identical; S_p Hermitian), so
  chi X^{dp} chi = S_p restricted to allowed flips.  CHECKED on ice BFS (section 3).
- Locality on the ice manifold (c4_ice_local, CHECKED): ice constraints are weaker (only flippable
  pairs), so Theorem L does not apply verbatim.  Random-walk sample on 4^3 (10 walkers x 3000 steps,
  1200 states): no local quadratic Q for R2 <= 4, 8, 12; solvable on the sample at 16 (same threshold as
  Z2).  Controls: bosonic-conjugated signs solvable exactly from R2 = 4 (none at 2); quasi-1D 2x2x8
  solvable at R2 = 2.  ARGUED in general via COMPARATOR (Wang-Senthil: E_b M_b vs E_f M_b distinct).
- (First BFS-capped sample of 6k states near the start was too shallow: solvable at R2 = 4 -- the
  constraints were not saturated.  Random walks fix this.)

## 6. Q3 flux sector (c5_flux, EXACT in Z2 form)
- One cube, charge-free sector (dim 32), -K sum S_p: K=+1 -> unique ground state, all S_p = +1;
  K=-1 -> unique, all S_p = -1; gap 4|K|; uniform and random records.
- Tori: both uniform assignments consistent with all relations of <S_p, G_v> on 2^3, 2x2x3, 4^3, 3x4x4;
  on 3^3 S_p = -1 violates 9 relations (planes with 9 plaquettes): pi flux frustrated on odd planes.
- eta with |eta cap dp| odd for all p exists iff every torus plane has an even plaquette count;
  Z^eta flips every S_p and multiplies hop t_l by (-1)^{eta_l}: light alone cannot tell K from -K,
  the charges can (0 vs pi flux).  S_p are conserved also with charges hopping (commute with hops), so
  in empty space sign(K) decides: K>0 zero flux (Schroedinger band), K<0 pi flux (Kawamoto-Smit Dirac).

## 7. Q4 helper places (derivation; EXACT for finite-range Pauli helpers, rest ARGUED)
- Hops t_l = X_l G_{c_l} (x) h_l, h_l a finite-range Pauli on helper qubits (faces, cubes, any number);
  ring R_p = X^{dp} bare (touches no helper).  Lemma R still reduces the link part to Gauss parities.
- Lemma G' (EXACT): if the helper loop products H_p := h(dp) are trivial (prop. to 1), fermionic statistics
  is impossible in d >= 2.  Same far-pair argument: both parts are path independent, split as
  alpha_u + alpha_w, and the helper symplectic form is alternating, so <alpha_u, alpha_u> = 0 too:
  LHS 0, RHS 1.  (= no local qubit representation of the even-Majorana commutation form without constraints.)
- If H_p is non-trivial it is central (commutes with every hop and ring) and the charges feel the composite
  flux X^{dp} G_{.} H_p.  Unless H_p is fixed by a helper loop rule, empty space has an extensive
  degeneracy of helper fluxes and the charges see random static flux.  So helpers keep light's ring bare
  only by moving the dressed loop rule onto the helpers (ARGUED).  With the dual potential sigma on faces
  and the local constraint n = d sigma, chi becomes a local CZ circuit (section 3), but a charge must then
  end a string of violated constraints (the JW string made physical): confining unless untensioned.

## 8. Corrections and run log
- Correction to section 2: 4^3 uniform threshold is R2 = 14 (rerun 12 -> none, 14 -> solvable), same as random.
  Z4 chi (S gates) on 4^3: none at 8, 12.  Fermion + local CZ conjugation: identical pattern to fermion.
- c4 random-walk run with 40 walkers x 4000 steps stopped at the 118 s alarm after R2 = 4, 8 (both: no
  solution); reduced to 10 x 3000 for the reported run.
- c5 first version built 4096^2 complex arrays: 0.37 s, peak 302.7 MB (edge of the 300 MB guide);
  rebuilt sector-only (35 MiB), identical numbers.
- Load 3.0-4.7, free memory 33-38% throughout; every job via run_small.sh with alarm <= 118 s.
