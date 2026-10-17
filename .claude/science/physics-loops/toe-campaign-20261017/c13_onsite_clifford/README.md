# C13: BKSF half-edge codes under on-site Cliffords

- `onsite.py`: a general linear search for an on-site 12x12 symplectic map. It is inconclusive: the
  solution spaces have dimension 28, too large to enumerate. Superseded.
- `majhalf.py`: the in-site Jordan-Wigner Majoranas (mu_d = X_d Z_<d, nu_d = Y_d Z_<d, in the code's own
  ordering) turn the BKSF operators into Majorana words. A site rotation composed with an on-site signed
  permutation of the 12 Majoranas preserves the signed group for all 24 rotations. Confirmed for the first
  class, and for one code per orbit type in the C11 runner (PASS=7); the run over all 60 classes is in
  progress.
- Consequence: the "minimal orbit four" of C6 holds only for bare permutations.
