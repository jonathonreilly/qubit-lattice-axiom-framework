# C13: BKSF half-edge codes under on-site Cliffords

- `onsite.py`: a general linear search for an on-site 12x12 symplectic map. It is inconclusive: the
  solution spaces have dimension 28, too large to enumerate. Superseded.
- `majhalf.py`: the in-site Jordan-Wigner Majoranas (mu_d = X_d Z_<d, nu_d = Y_d Z_<d, in the code's own
  ordering) turn the BKSF operators into Majorana words. A site rotation composed with an on-site signed
  permutation of the 12 Majoranas preserves the signed group for all 24 rotations. Confirmed for all 60 classes x 24 rotations x
  both uniform sectors (`majhalf_all60_L4.log`, about 41 min), and for one code per orbit type in the C11
  runner (PASS=7).
- Consequence: the "minimal orbit four" of C6 holds only for bare permutations.
- `halfpair.py`: clean pair test under the sign-free Majorana permutation (L = 8, a D3 code and an order-4
  code, both sectors, all 9 C2). lambda = -1 everywhere, so eta_f = +1: the trivial class (`halfpair.log`).
  Under the bare action the same codes carry w2.
