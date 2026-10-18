# C1 findings: can the six D4 doublers be gapped while ±k* stay gapless, symmetrically?

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back. The model is a verbatim copy of `B18_check/chk_model.py`.

`run_all.sh` gives TOTAL: PASS=29 FAIL=0 (about 3 min):
- `c1_reps.py`: 13;
- `c1_bdg_step.py` (N=32): 9;
- `c1_anomaly.py`: 7.

Two first-run FAILs were the worker's own wrong expectations.

**Answer: no, not by symmetry.**
- **Pairing:** the symmetric Majorana mass is all-or-nothing (exact). Gapping only the doublers needs an unprotected tuned zero at ±k*.
- **Number-conserving route:** the six doublers carry a mixed U(1)–translation anomaly (Weyl dipole π(1,1,1)). So symmetric mass generation of the doublers alone into an SRE state is excluded, conditional on standard anomaly matching.
- B7 does not forbid the target state.

## 1. Pairing (free BdG)

- **Representations.** The dressed rotations act as signed permutations, and the axis-C2 lifts anticommute. So every 2-fold node level is a spin-½ irrep: E1/2 or E5/2 of O at ±k*, and E1/2 or E3/2 of D4 at the doublers.
- **Determinant lemma (proved; numerical on 4 + 36 doublets).** det(U_g|_V) is the same character for every 2-fold level. For this PSG it is A2, because the real signed-permutation lift is not the SU(2) lift. At the doublers, det = B1.
- **Pair channels.** One rotation-fixed momentum Q ∈ {0, R = π(1,1,1)} and one 1-dimensional character χ ∈ {A1, A2}.
- **Selection rule (exact).**
  - At Q = R every node pairs with itself, since 2K ≡ R.
  - The singlet mass at K is allowed iff χ|_{little group} = det_K.
  - A1 and A2 restrict to different D4 characters, so it is allowed at a doubler ⇔ χ = A2 ⇔ it is allowed at ±k*.
  - **No selective symmetric channel exists,** for any PSG-symmetric Hamiltonian or step with 2-fold node levels.
  - Inversion: A2g and A2u allow the singlet at all eight, with |m_K| = |m_−K|; A1g and A1u forbid it at all eight.
- **Exact decoupling at ±k*.** An A2-channel Δ pairs the node doublet only with itself, at all orders. So ±k* is gapless iff one complex number m_{±k*} vanishes.
- **Q = 0** pairs K with −K, which have opposite chirality. Each BdG point then has charge ±2, and no small Q = 0 pairing gaps any node (exact).
- **Explicit BdG steps (numerical, uncertified):**

  | Case | Pairing | Result |
  |---|---|---|
  | B1 | Q = R, A2, on-site | All eight gapped (gap 0.098) |
  | B2 | A1 | Nothing gapped |
  | B3 | Q = 0 | Zeros persist |
  | B4 | Δ(k) = w(k)·A, w O-invariant, w(±k*) = 0 | ±k* gapless with isotropic BdG cones at √2/3; doublers gapped; no other zeros (min 0.11). Quasi-local |
  | B5b | on-site A2 with m_{±k*} tuned to zero | ±k* gapless, doublers gapped (0.039), strictly on-site |
  | B5c | B5b plus η × generic | k* gap ∝ η: tuning, not protection |

## 2. Number-conserving route (SMG)

- **Infrared symmetry.** Translations act as a Z2³ taste: e^{ik*·e}(−1)^{n·e}, composed with U(1).
- **Anomaly table:**

  | Subset | Net chirality | Weyl dipole b mod 2π | U(1)²–Z2 counts mod 2 |
  |---|---|---|---|
  | six doublers | 0 | π(1,1,1) | (1,1,1) |
  | {±k*} | 0 | π(1,1,1) | (1,1,1) |
  | all eight | 0 | 0 | 0 |

  Only the empty set and all eight are anomaly-free among rotation-invariant subsets.
- **Free fermions:** trivially no gap.
- **Interacting:** gapping only the doublers into a symmetric SRE state is excluded, conditional on anomaly matching. b = π(1,1,1) is half a Hall quantum per layer, while an SRE state's Hall vector lies in the reciprocal lattice. This is the field-theory "unquantized anomaly" argument, not a lattice theorem.
- **Not excluded:** a topologically ordered gapped doubler sector with half-quantized Hall response per layer (no construction given), or breaking translations or U(1).
- **B7:**
  - It forbids an SRE gapped state of all eight at odd ν (conditional).
  - It does not forbid "doublers gapped, ±k* gapless", which is gapless.
  - Its twisted tori see only ±k* (L odd, 1–11).

## 3. Against the selection rule

- **Pairing cases B4 and B5b pass the cone test numerically:** only ±k*, isotropic at √2/3.
- **What that costs:**
  - U(1) is broken (a new supplied term), and the species become Majorana.
  - Translations survive only dressed by U(1); under strictly undressed PSG only Q = 0, A1 is allowed, which gaps nothing.
  - Masslessness at ±k* is a tuning, the Wilson-fermion naturalness problem in Majorana form.
  - B22's gap premise is still unmet.

## Status

- **Exact:** the determinant lemma, selection rule, decoupling, the Q = 0 charge, and the anomaly bookkeeping.
- **Numerical:** the BdG spectra.
- **Conditional:** the SMG exclusion.
- **Open:** the topological-order route.

## Prior art (recalled, not verified)

- **SMG:** Wang–You 2022; Tong 2022; Razamat–Tong 2021.
- **Interacting reduction:** Fidkowski–Kitaev 2010.
- **Mirror fermions:** Eichten–Preskill 1986; Golterman–Petcher–Rivas.
- **Staggered and Wilson fermions:** staggered taste, Wilson additive mass, Curci–Veneziano 1987.
- **Weyl superconductivity:** Cho–Bardarson–Kim–Moore 2012; Meng–Balents 2012; Bednik–Zyuzin–Burkov 2015; Li–Haldane 2018.
- **Weyl dipole and translation anomaly:** Burkov–Balents 2011; Zyuzin–Burkov 2012; Wang–Zhang 2013; Gioia–Wang–Burkov 2021; Thakurathi–Burkov 2020.
- **New here:** the A2 all-or-nothing rule, the decoupling, the anomaly table, and that B7 sees only ±k*.
