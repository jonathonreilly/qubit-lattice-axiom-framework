# B15 check

Provenance: a fresh-context checker of the same model family; not independent in model lineage. Saved by the supervisor from the hand-back.

The checker wrote its own code and used a different method: exact momentum-space lattice symbols (Laurent polynomials in e^{iak}, e^{iaq}, e^{iap}) expanded in a.

| Runner | Result |
|---|---|
| `chk_b15_symbols.py` | PASS=9 FAIL=0 |
| `chk_b15_orders.py` | PASS=13 FAIL=0 (about 80 s) |

First-run logs are kept. Every first-run failure was the checker's own wrong expectation:
- S3a: same-sign diagonal pairs were expected to survive;
- O3/O3b/O4: the t≠½ term was expected to be absorbable;
- O5b: τ = σ at (π,π,π).

**Absorbability test.** Any linear, translation-covariant G_f on ξ̃ has symbol Σ_j (X_j−Y_j) g_j(XY, P). Order by order:
- B_0 and B_1 must be linear in κ;
- B_2 + Σ κ_j³ ∂_{κ_j}B_0/6 must be linear in κ.

One exact rational failure point proves non-absorbability.

## Verdicts

1. **Continuum bracket, v² and sign: confirmed.**
   - [h_N, h_M] = −v² L_w (Kosmann), by three routes. Closure needs v² = −sK/(4α), the scalar's c.
   - The bracket does not depend on statistics or bracket conventions.
   - **Correction:** Hermiticity forces s = −1 only together with the supplied K, α > 0 and a common relabelling orientation. Hermitian Clifford generators square to +1, so v² > 0.
   - The gain over the scalar is that v² > 0 is derived rather than supplied.
2. **No exact lattice closure: confirmed, and stronger.**
   - The range-2 term is exact (S3b).
   - Same-sign diagonal pairs cancel at every timing. Mixed pairs ±(e_j−e_k) survive in proportion to w_a² − w_b² (S3a).
   - T2 and T3 are confirmed (kernel = 3 constant shifts).
   - **No linear G_f of any range closes**, whether or not it is translation-covariant (S3c; K2a/K2b at L = 5, rank 186 vs 3).
   - C(λ) terms and on-site internal constraints do not help.
3. **Orders: exact.**
   - Endpoint-mean timing gives an O(a²) obstruction that no translation-covariant G_f of any range can absorb (O2).
   - At t ≠ ½ there is a genuine O(a) obstruction, cubic in κ (O3).
   - **Mass:** cross terms vanish iff t = ½ (O7). Otherwise they are ξ̃-linear with a Clifford-odd coefficient, so they block only Kosmann-class G_f. The endpoint mean is independently selected by O3.
   - **Wilson: corrected.** The O(a) term is Clifford-odd but linear in κ, so a Clifford-odd O(a)-corrected G_f absorbs it. The obstruction is O(a²) against a general G_f.
4. **Doublers (T7): confirmed.**
   - Every doubler has the same v², with its own spin set τ.
   - **Caveat:** at the 6 doublers with one or two π components, τ ≠ σ. A G_f with the on-site spin term fails there at O(1), so the lattice G_f needs momentum-dependent spin structure.
5. **Prior art: corrected.**
   - Schwinger, Phys. Rev. 130, 800 (1963) already covers the continuum spin-0, ½ and 1 energy-density commutator condition.
   - Nelson–Teitelboim 1978 is confirmed. Henneaux 1983 is unverified.
   - Add Koo–Saleur (1994; lattice Virasoro closing only in the scaling limit), Bonzom–Dittrich (arXiv:1304.5983) and arXiv:2305.10097.
   - New and narrow: the monomial, the no-go for any linear G_f, the timing and order classification, and the doubler spin caveat.
