> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# C1 findings: can the six D4 doublers be gapped while ±k* stay gapless, symmetrically?



`run_all.sh` gives TOTAL: PASS=29 FAIL=0 (about 3 min):
- `c1_reps.py`: 13;
- `c1_bdg_step.py` (N=32): 9;
- `c1_anomaly.py`: 7.

Two first-run FAILs were the worker's own wrong expectations.

**Full-O pair-channel calculation with its stated dressed-symmetry and isolated-doublet premises.**
- **Pairing:** the symmetric Majorana mass is all-or-nothing (exact). Gapping only the doublers needs an unprotected tuned zero at ±k*.
- **Number-conserving route:** the six doublers carry a mixed U(1)–translation anomaly (Weyl dipole π(1,1,1)). The proposed SRE exclusion additionally imports anomaly matching and a Hamiltonian/Floquet bridge; it remains a separately deferred terminal promotion, not a native lattice conclusion.
- B7 does not forbid the target state.

## 1. Pairing (free BdG)

- **Representations.** The dressed rotations act as signed permutations, and the axis-C2 lifts anticommute. So every 2-fold node level is a spin-½ irrep: E1/2 or E5/2 of O at ±k*, and E1/2 or E3/2 of D4 at the doublers.
- **Determinant lemma (proved; numerical on 4 + 36 doublets).** det(U_g|_V) is the same character for every 2-fold level. For the real signed-permutation lift it is A2, because that lift is not the SU(2) lift; at the doublers it is B1. "A2" is a lift label: rephasing the lifts turns it into A1, and the selection rule below is lift-independent (check).
- **Pair channels.** One rotation-fixed momentum Q ∈ {0, R = π(1,1,1)} and one 1-dimensional character χ ∈ {A1, A2}.
- **Selection rule (exact).**
  - At Q = R every node pairs with itself, since 2K ≡ R.
  - The singlet mass at K is allowed iff χ|_{little group} = det_K.
  - A1 and A2 restrict to different D4 characters, so it is allowed at a doubler ⇔ χ = A2 ⇔ it is allowed at ±k*.
  - **No selective channel preserving full O exists,** for any PSG-symmetric Hamiltonian or step with 2-fold node levels.
  - **Check addition:** once O is broken, selective channels exist. For example, T with χ(C3) = ω forbids the singlet at ±k* and allows it at all six doublers. But the node doublet then couples to G3/2, and a τ² level shift turns ±k* into a small Bogoliubov shell. So ±k* is still not protected.
  - Inversion: A2g and A2u allow the singlet at all eight, with |m_K| = |m_−K|; A1g and A1u forbid it at all eight.
- **Exact decoupling at ±k*.** An A2-channel Δ pairs the node doublet only with itself, at all orders. This relies on E1/2 and E5/2 each occurring once at ±k*. For the Hamiltonian pairing block [[0,m],[m*,0]], the energies are ±|m|, so its zero-energy gap closes iff m=0. For the corresponding Floquet pairing step exp(−iτ[[0,m],[m*,0]]) with τ>0, the eigenphases are ±τ|m| modulo 2π: zero quasienergy occurs when τ|m|∈2πZ, including nonzero wrapping values; the π quasienergy occurs at odd multiples of π. Thus the zero-quasienergy iff m=0 criterion is restricted to 0≤τ|m|<2π (a small-strength interval such as τ|m|<π also suffices). Exact invariant-subspace decoupling does not remove quasienergy wrapping.
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
- **Interacting:** gapping only the doublers into a symmetric SRE state is excluded. This is conditional on anomaly matching and on a Hamiltonian reading of the Floquet sector (or a C2-symmetric driving loop). B17_check found no local Floquet Hamiltonian.
  - **Cleaner form (check):** O forces the Hall vector to zero, and {±k*} contributes half a quantum per layer. So a compensating sector with b ≡ R is required. This is a Z2-valued obstruction, since b is pinned to {0, R}, and an exact free-level slice version exists. The doublers are one such sector; topologically ordered, gapless or symmetry-breaking sectors are others.
  - The U(1)²–Z2 counts in the table equal b/π mod 2, so they are not independent. b = π(1,1,1) is half a Hall quantum per layer, while an SRE state's Hall vector lies in the reciprocal lattice. This is the field-theory "unquantized anomaly" argument, not a lattice theorem.
- **Not excluded:** a topologically ordered gapped doubler sector with half-quantized Hall response per layer (no construction given), or breaking translations or U(1).
- **B7:**
  - It forbids an SRE gapped state of all eight at odd ν (conditional).
  - It does not forbid "doublers gapped, ±k* gapless", which is gapless.
  - Its twisted tori see only ±k* (L odd, 1–11).

## 3. Against the selection rule

- **Pairing cases B4 and B5b pass the cone test numerically:** only ±k*, isotropic at √2/3.
- **What that costs:**
  - U(1) is broken (a new supplied term), and the species become Majorana.
  - Translations survive only dressed by U(1). (The earlier remark about strictly undressed PSG is a lift convention, not a physical restriction; check.)
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
- **New here:** the all-or-nothing rule for full O, the decoupling, the anomaly table (a Z2 obstruction), and that B7 sees only ±k*.
- **Confirmed by the check's search:** Gioia–Wang–Burkov 2021; Wang–Gioia–Burkov PRL 124, 096603 (2020).
