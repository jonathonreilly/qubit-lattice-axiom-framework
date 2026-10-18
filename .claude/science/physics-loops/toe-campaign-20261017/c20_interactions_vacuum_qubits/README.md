# C20 (in progress): spontaneous mass, clean Dirac vacuum, qubit build

## Qubit build (`qbuild.py`, `qbuild.log`)
- **The images.** Each one-fermion term c+_q c_r of the corner model has an explicit Pauli image in the 48-qubit-per-site corner code (flux 1011): G_P (1+B_q)(1-B_r)/4, where G_P = i^n (product of code hops along a path) / (gauge phase).
- **The logical sector.** It is fixed by the three noncontractible Wilson loops, using the gauge's holonomies.
- **Checks:**
  - gauge invariance;
  - the fermionic algebra mod stabilizers (25/25 triples);
  - disjoint commutation;
  - [n, c+c] = c+c;
  - covariance under the code's rotation operators with the fermion-level PSG signs (36/36).

## Spontaneous mass, metallic model (`chi2.py`, `chi_metallic_model.log`)
- **The interaction.** Site-charge repulsion U N_v^2/2, treated in Fock mean field: the attraction is equal in all 143 traceless on-site channels.
- **The leading instability** is the uniform imaginary A1 channel (chi 1.197), a spontaneous chiral T-breaking term of the C18 lambda type.
- **The Dirac mass channel** (staggered imaginary A2) has chi = 0.588, so it is subleading.
- **Caveat.** The model is metallic at the node, so Fermi pockets contribute.

## Clean vacuum
- **Bases (`basis2.py`).** Range |shift|_inf <= 1 gives 43 conjugation-odd and 43 conjugation-even invariant terms.
- **First optimization (`clean1.log`).** It was grid-gamed: off-grid, band 0 rises 0.035 above the node (`verify_clean_v1.log`).
- **Refinement (`clean2.py`).** Running.
