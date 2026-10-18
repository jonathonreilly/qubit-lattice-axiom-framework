# C1 check: gapping the doublers

Provenance: a fresh-context checker of the same model family. All code is its own: `ckmodel.py` on a copy of `B7_check/chk_core.py`, which has its own GF(2) gauge and brute-force PSG. Pairing was built in real space; chiralities come from Berry flux. Saved by the supervisor from the hand-back.

**Totals: PASS=29 FAIL=0.**

| Script | Result |
|---|---|
| chk1_det_selection | 10/0 |
| chk2_subgroup_channels | 6/0 |
| chk3_anomaly_bdg | 10/0 |
| chk4_slice_inversion | 3/0 |

Two first-run FAILs were the checker's own expectations. A complex-conjugation bug was fixed before the final run.

## Verdicts

1. **Determinant lemma: confirmed.** The lemma holds at every 2-fold level, for five PSG-symmetric models.
   - **Fix:** "A2" labels the real signed-permutation lift. Rephasing by c with c² = A2 turns it into A1. The rule "allowed iff χ|_{G_K} = det_K" is lift-independent.
   - So "under strictly undressed PSG only Q = 0, A1" is a lift convention, not a physical restriction.
2. **Selection rule: confirmed for full O.**
   - At Q = R, A2 gives the singlet at all eight nodes and A1 at none (≤ 6e−15). The O_h version is confirmed.
   - The classification Q ∈ {0, R} is complete for one condensate with U(1)-dressed symmetry. Multi-dimensional pair irreps break O.
   - **New: subgroup channels.**
     - Once O is broken, selective channels exist. Example: T with χ(C3) = ω forbids the singlet at ±k* and allows it at all six doublers.
     - None protects ±k*. In T-ω the node doublet couples to G3/2, and a level shift δ ∝ τ² (slopes 1.98 and 2.00) turns ±k* into a tiny Bogoliubov shell.
     - So "no selective symmetric channel" needs the scope "full O". "±k* masslessness is a tuning" survives.
3. **Decoupling: confirmed.** A2 couples the node doublet to no other level (≤ 1e−14), and the node 4-space is invariant under the BdG step.
   - **Caveat:** this relies on E1/2 and E5/2 each occurring once at ±k*. D′ means the other irrep.
4. **Anomaly table: numbers confirmed.**
   - (i) The U(1)²–Z2 counts equal b/π mod 2, so they are not independent.
   - (ii) **Cleaner form.** O forces the Hall vector to zero. {±k*} contributes half a quantum per layer, so the rest must supply a half-integer, which an SRE insulator cannot. b is pinned to {0, R}, so this is a Z2-valued obstruction. An exact free-level slice version is check L1.
   - (iii) **Missing premise:** the step is Floquet. Anomaly matching and a Hall response need a Hamiltonian reading, or a C2-symmetric driving loop.
   - (iv) "The doublers are anomaly-required" overstates it. What is required is *some* compensating b ≡ R sector: gapless, topologically ordered, or symmetry-breaking.
5. **BdG cases: confirmed qualitatively** (B1, B2, B4, B5b, B5c). B4's Δ(k) has strictly finite range; only the exponentiated layer is quasi-local.

## Prior art (confirmed by search)

- Gioia–Wang–Burkov, PRR 3, 043067 (2021).
- Wang–Gioia–Burkov, PRL 124, 096603 (2020): FQH in Weyl semimetals, which supports the topological-order route.
- Sehayek–Thakurathi–Burkov: named only.
