# Kill round 1: F1 (price lemma) and F2 (strong coupling / incompressible)

Read: MINIMAL_AXIOMS_2026-06-29 (four axioms; Admissibility is not dynamics), PRIMITIVE_REGISTRY_CHECK (three primitives), neutral brief, routes list, agents 1 and 3; landed 09-14 tensor, 09-24 oscillator and 05-02 CCR notes; probes 10, 11, 15, 17, 18, 20 (PR branch). Checks run: `exercise/kill1/snf_torsion.py`, `exercise/kill1/bogoliubov_check.py`.

## F1 — WOUNDED

**What holds.** For spin-type slots (E diagonal, unit-step, no wrap) and an abelian integer rule the lemma is correct, and the Haar average is redundant: a diagonal linear rule grades every local term by its shift pattern m; components with Gm ≠ 0 annihilate a fixed sector, so on that sector H = Σ_{Gm=0} H_m and probe 10 T3 holds in every eigenstate lying in a sector. This is the Fable remark recorded in probe 15 ("term-by-term preservation is automatic"): already on the branch. Agent 3's mod-N step is safe for local terms: the open-box stencils G and S have Smith invariant factors all 1 (torsion only on periodic tori, order L, i.e. global sectors), so every local mod-N-invariant character equals a lifted kernel character as an operator.

**Gaps.**
1. *Not the price of the wall.* The lemma gives the sum rule m₁(E_TT) ≤ C q⁴. The wall needs also χ_TT bounded below (probe 10 W_a, marked unresolved in its N2). "Only exits: non-compact or O(1) violation" omits the in-domain exit, the incompressible channel, which is F2. So "wall ⇔ one premise" has terminal obligation "no incompressible linear mode" = the target: blocked-equivalent. The price is three premises, not one.
2. *"In any state" covers spin-type slots only.* On Z_N clocks E is not a linear observable: [T_m, O_q] = −w(m) T_m fails at the wrap, so no state-independent T3 exists; only the harmonic 09-14 bound remains, which N-scaling harmonics evade (its own N7). Lemma P's "finite cyclic group" clause yields Gm ≡ 0 mod N; torsion-freeness repairs it, but only into that harmonic bound.
3. *Schrieffer–Wolff "to all orders".* 09-14 explicitly declines to import BDL's linked-cluster theorem (product low-energy subspace fails for this stabilizer sector). Per finite order only, and only for U ≫ J, the regime Route 2 must leave anyway.
4. Non-abelian rules and non-commuting composite E (one qubit per site) are outside; probe 17's phase-rotation form is the real hypothesis.
5. "CCR not load-bearing": correct, but already the CCR note's own N6/N7 and probe 17's spectrum lemma. The quantum CLT supplies kinematics with a state-dependent symplectic form, nothing about dynamics. Not new.

## F2 — WOUNDED

1. *The obligation is a restatement.* T4 makes χ_TT ≤ C q² and S ≤ C q³ automatic for any linear lowest E-weighted mode. Nothing to engineer; "emergent 1/q² TT-electric interaction" is not a mechanism.
2. *Corollary of T2 (state-independent).* For any local B and any state in one sector, |⟨[B_q, E_q]⟩| ≤ (Σ_m ‖B_m‖ μ₂(m)/2) q²: only Gm = 0 components have expectation, and those have zero zeroth and first moments. E_TT is a dipole-conserved (fracton) density with no local conjugate. Hence a linear TT mode with a local Einstein-normalised metric (S_h ~ 1/q) has E_TT = O(q)·π + O(q²)·h on the mode: the stored electric variable is a derivative of the momentum, exactly probe 11 T1's composite E = curl Ã. Probe 11's open question ("does a non-composite incompressible graviton need partners") is moot: non-composite is impossible in the exact-rule domain with a local metric. F2 collapses onto probes 11/16/20/21 (composite; helicity ±1 partners at harmonic order), leaving "gap the constituents' partners non-perturbatively", with no mechanism named. Cross-check (Cauchy–Schwarz, verified numerically): χ_h ≥ |⟨[h,E]⟩|²/(C_H q⁴), so an O(1) conjugate would force a static TT response ≥ 1/q⁴, tidal field ∝ 1/r: anti-Newtonian.
3. Agent 1's version leaves the domain (both rules soft): the 09-14 scalar block is indefinite, probe 18 D gives everything gapped at harmonic order, and his own (ii) says the N-type expansion point is not a ground state. No positive evidence; cost unbounded.
4. The proposed tests do not decide: E–E tails by ED on 20 slots cannot separate r⁻⁶ from exponential at r ≤ 3, and item 2 makes the clustering falsifier moot (E decouples at O(q) regardless of clustering).

Not DEAD: no theorem excludes non-perturbative gapping of the composite's partners. That is F2's only live content, and it is probe 20/21's question beyond harmonic order, not either agent's artifact.
