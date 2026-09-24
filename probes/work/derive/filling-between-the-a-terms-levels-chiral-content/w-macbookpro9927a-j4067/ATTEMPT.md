# filling-between-the-a-terms-levels-chiral-content, attempt a2: the a-term's levels sit at one record per site

Worker `w-macbookpro9927a-j4067` (`claude-opus-5-5`), unit `J-derive-filling-between-the-a-terms-levels-chiral-content-a2`.

**Sources.**
- **The fork probe.** `FORK_PROBE_source_link_20260922.md`, on the decision-record branch of PR #8572, head `10cb4567c4`.
- **The PR heads of blocks 76–78**, all closed:
  - block 76 (#8611), `2fc37b9f66`;
  - block 77 (#8612), `a2c138c297`;
  - block 78 (#8613), `88a8e6752e`.
- **As landed on origin/main `0e6ad8285096`**, in narrowed form:
  - block 77 now says "corner energies need not be rest masses";
  - block 78 names its compressed two-record generator a supplied model choice.

**Provenance and independence.**
- **The prior attempt.** `a1` (`w-jonathonsmac4f50-j234b`, claude-opus-5-5, another machine, same model family) has no HIT. It covers:
  - (a)–(b) in the free comparator: Fermi sheets carry `−Σ_{L_n<μ}χ_n` (upper band) and `+Σ` (lower), total zero;
  - (c) exactly: the only gap is `|μ − a₀| < |m|`, and for `a ≠ 0` the zeros stay Weyl points at `a₀ ± √(L_n² + m²)` with sense `sign(L_n)χ_n`;
  - (d) only as a statement resting on an ASSUMED anomaly theorem. Its "what would finish it", item 2, asks for "an exact small-torus count of many-record states under exclusion".
- **How my plan was formed.** At claim time I saw only a1's one-line summary. I read the task and the four sources and formed my plan before opening a1's file. The plan: locate the a-term's levels in record number, then ask what the Record axiom's exclusion does there.
- **Credit.** My treatment of (c) coincides with a1's step 4.3. It is credited, not claimed.
- **What is new here:**
  - Theorem F: the levels' record numbers;
  - Theorem X: exclusion at those fillings;
  - the chiral-moment remark (step 2).
- **Related earlier units of this worker,** disclosed and not used:
  - #8741 (the staggered term pairs opposite senses);
  - #8642 (the exchange sign is not derivable; hard-core symmetric and antisymmetric compositions both satisfy the axioms);
  - #8754 (the scalar hop's squared generator).

## 1. What is attempted

**Setting.** Everything is supplied; nothing is adopted.
- **The one-record generator** (block 77) is the family `H_a = a₀ + A`, with
  - `A = 2aΣ_jC_j + Σ_jσ_jS_j`;
  - `C_j = (T_j + T_j†)/2` and `S_j = (T_j − T_j†)/(2i)`;
  - the torus `Z_L³`, `N = L³` sites, a two-component coin, and `a > 0`.
- **The staggered term** is `mε`, with `ε = (−1)^{x₁+x₂+x₃}`.
- **The free comparator** is the free antisymmetric many-record state filled to `μ`. It is a comparator only: it allows two records on a site with different coins.
- **The supplied hard-core model** (block 78's compression, extended to many records) is the free many-record generator restricted to configurations with at most one record per site. It comes with each composition: antisymmetric, symmetric, or labelled with no sign.

**Answers to (a)–(c), free comparator** (restated; a1 credited).
- **(a)–(b).** Every zero `k = πn` lies at level `L_n = a₀ + 2a(3 − 2|n|)` with sense `χ_n = (−1)^{|n|}`. For every Fermi level `μ` between levels, every zero is enclosed by a Fermi sheet. So all eight species are gapless at the Fermi level, four of each sense, and right minus left is zero. This holds in each of the windows `(2a, 6a)`, `(−2a, 2a)` and `(−6a, −2a)` (with `a₀ = 0`).
- **(c).** The staggered term gaps only `|μ − a₀| < |m|`. It moves each zero to `a₀ ± √(L_n² + m²)` and keeps it gapless with its sense (a1, 4.3).

**The claims of this attempt** (on the part a1 left ASSUMED).
- **Theorem F: record counts of the free comparator.** On `L³` tori with even `L`:
  - (F1) `#(E < a₀) = N − z/2`, where `z = #(E = a₀)`: the middle level is one record per site.
  - (F2) For `μ ∈ (a₀ + 2a, a₀ + 6a)`, the window of task (a), `#(E < μ) ≥ N + 6 + z/2`.
  - (F3) For `μ ∈ (a₀ − 6a, a₀ − 2a)`, `#(E < μ) ≤ N − 6 − z/2`.
  - (F4) With `mε`, `m ≠ 0`: exactly `N` states lie below `a₀`, and none within `|m|` of it.
- **Theorem X: the supplied hard-core model.**
  - (X1) There are at most `N` records. At `N` records (one per site), the generator of every composition is the constant `Σ_x(a₀ + mε(x)) = Na₀` times the identity on the `2^N` coin configurations. With clocks `φH_aφ` it is `a₀Σw_x`. So the generator is flat, with no momentum and no senses.
  - (X2) With `N − N_h` records the generator is `D + T`:
    - `D` is diagonal with `|D − (N − N_h)a₀| ≤ |m|N_h`;
    - `‖T‖ ≤ 6(|a| + ½)N_h`.

    The whole spectrum lies within `N_h(6(|a| + ½) + |m|)` of `(N − N_h)a₀`.
  - (X3) In the window `(a₀ − 6a, a₀ − 2a)`, `N_h ≤ z/2 + #(a₀ − 6a < E < a₀) ≤ z/2 + 2#{k : |sin k| < 12a}`. As `L → ∞` this is at most `16 arcsin(12a)³/π³` per site, for `a < 1/12`.
- **Consequences under exclusion.**
  - The filling of task (a) does not exist.
  - Task (b)'s middle window straddles one record per site. Its upper half does not exist, and its middle is frozen.
  - For small `a`, the lowest window is a lattice nearly full of records, in which only `N_h` holes move.
- **The task's HIT condition** (single-sense gapless content surviving exclusion) **is not met.** The new exact partial result is Theorems F and X.

## 2. Steps

0. **ASSUMED (supplied clauses).**
   - The walk and the `a`-term family (blocks 54 and 77), the staggered term (block 77), and the hard-core compression (block 78) are all supplied; the compression is extended here to many records.
   - The free comparator is a comparator. Nothing is adopted, and the parked decisions (statistical postulate; larger site algebra) are not touched.

1. **PROVED; CHECKED L1 (levels and senses; block 77 T1 restated).**
   - At `k = πn`: `sin k = 0` and `Σcos k = 3 − 2|n|`.
   - The multiplicities are `C(3, |n|)`: `1:3:3:1`.
   - The sense is `sign det ∂(sin k)/∂k = Π cos(πn_j) = (−1)^{|n|}`.

2. **PROVED; CHECKED L2 (chiral moments, a remark).**
   - Write `s_j = (−1)^{n_j}`. Then `χ_n = s₁s₂s₃` and `L_n = a₀ + 2a(s₁ + s₂ + s₃)`.
   - `Σ_n` of a monomial in the `s_j` vanishes unless each `s_j` appears to an even power.
   - So `Σ_nχ_nL_n^p` keeps only the terms containing `s₁s₂s₃`:
     - these vanish for `p = 0, 1, 2`;
     - for `p = 3` the term `(2a)³·3!·s₁s₂s₃` gives `8·6·(2a)³ = 384a³`, for every `a₀`.
   - In particular `Σ_nχ_nL_n = 0`: the energy offsets of the nodes carry no net sense.

3. **PROVED (the answers to (a)–(c) above; a1 credited).**
   - Both bands equal `L_n` at the zero `k_n`.
   - So for `μ ≠ L_n`, `k_n` lies in the upper band's occupied region iff `L_n < μ`, and in the lower band's empty region iff `L_n > μ`.
   - Either way a Fermi sheet encloses it, and every one of the eight zeros is enclosed.
   - a1's Chern bookkeeping gives the same zero total.

4. **PROVED; CHECKED S1, F1, F2 (Theorem F).**
   - **(F1)**
     - `ε` anticommutes with every one-step hop, hence with `A`.
     - So `spec A = −spec A`, and `#(A<0) = #(A>0) = (2N − z)/2`. This needs even `L`, so that `ε` is defined on the torus.
   - **(F2)**
     - The three `|n| = 1` zeros carry six states at `E = a₀ + 2a ∈ (a₀, μ)`.
     - So `#(E < μ) ≥ (N − z/2) + z + 6`.
   - **(F3)**
     - The six states of the `|n| = 2` zeros lie at `a₀ − 2a ∈ [μ, a₀)`.
     - So `#(E < μ) ≤ N − z/2 − 6`.
   - **(F4)**
     - `X = εT_1` anticommutes with `A + mε`: `T_1` commutes with `A` and flips `ε`, and then `ε` flips the rest.
     - `(A + mε)² = A² + m² ≥ m²`, so there are no zero modes, and the spectrum is symmetric.
     - Hence exactly `N` states lie below `a₀`, and none within `|m|`. The free sea at the middle is then a band insulator.
   - **Checks.**
     - S1 and F2: the operator identities on all basis vectors of `4³`.
     - F1: exact counts on `4³` and `6³` for `(a₀, a) = (1/3, 1/10), (0, 1/4), (−2/5, 2/3)`. For `6³` at `a = 1/10`: 216 at the middle, 228 in the upper window, 204 in the lower.
     - On `3³`, with odd sides, the middle count is 26 of 54: the exact statement needs even sides. In infinite volume, the symmetric spectral measure gives exactly one record per site at `a₀`.

5. **PROVED; CHECKED X1 (Theorem X1).**
   - Every term of `A` moves a record by one site; `a₀` and `mε` are site terms.
   - At `N` records every site is occupied. So every hop lands on an occupied site, and the compression removes it.
   - What remains is the site part, `Σ_x(a₀ + mε(x))`. `ε` sums to zero on even tori, so this is `Na₀`, times the identity.
   - No hop survives, so the exchange sign plays no role. With clocks the site part is `a₀w_x`, which again sums to a constant.
   - Check X1 (an illustration of the general argument, on block 78's ring): four records on a ring of four, symmetric and antisymmetric. The generator is exactly `4a₀·1` on all 16 coin configurations.

6. **PROVED; X2 is floating evidence (Theorem X2).**
   - **Row sums.** In the configuration basis, a configuration with `N_h` holes has at most `6N_h` allowed hops.
     - Each hop has coin amplitude `a·1 ± σ_j/(2i)`.
     - The column sums of its moduli are `|a| + ½` for `σ₁` and `σ₂`, and `√(a² + ¼)` for `σ₃`.
     - Exchange signs do not change moduli.
   - **Gershgorin.** For hermitian `T`, `‖T‖ ≤` the maximal row sum `≤ 6(|a| + ½)N_h`.
   - **The diagonal.** `D = (N − N_h)a₀ − mΣ_{holes}ε(x)`.
   - **Evidence** (X2), on a ring of six with the family's one-dimensional member (two hops per hole): the spectral widths are 2.039 ≤ 2.4 at `N_h = 1` and 3.533 ≤ 4.8 at `N_h = 2`. Hermiticity is checked exactly.

7. **PROVED; CHECKED X3 (Theorem X3).**
   - **Why the window is thin.** `|E_± − a₀| = |2aΣcos k ± |sin k|| ≥ |sin k| − 6a`, so `|E − a₀| < 6a` forces `|sin k| < 12a`. Then each `k_j` lies within `θ = arcsin(12a)` of `0` or `π`. That is a zone fraction of at most `(2θ/π)³`; with two bands, at most `16θ³/π³` states per site.
   - **The hole count.** `N_h = N − #(E < μ) ≤ N − #(E ≤ a₀ − 6a) = z/2 + #(a₀ − 6a < E < a₀)`.
   - **Checks.**
     - Exact grid counts: 56 of 1728 points on `12³` at `a = 1/20`.
     - On `6³` the lower window leaves 6 holes, against the bound 16.
     - Floating evidence on `48³`: 0.016 states per site with `|E − a₀| < 6a` at `a = 0.05`, against the bound 0.1375.

8. **(d), honestly.**
   - **Frozen or near-frozen at small `a`.** By Theorems F and X, the a-term's zeros sit at one record per site. Under exclusion that filling is frozen, and the fillings above it do not exist. So no filling of the supplied hard-core model gives mobile records at the zeros with `μ` between the a-term's levels. For small `a` only `N_h ≤ 16θ³N/π³` holes move (X2, X3).
   - **What would be needed to reach the zeros with mobile records.** One of:
     - two records on a site: a larger site algebra, which is parked;
     - a reading of "one record per site at a time" other than the hard-core compression.
   - **Even then.**
     - The free count is four of each sense (a1).
     - For interacting content, a lattice theorem forbids a net sense for an on-site conserved record number: 't Hooft anomaly matching, the interacting form of Nielsen–Ninomiya. This is ASSUMED, as in a1's step 5.
   - **So the HIT condition is not met.** The condition that exclusion not destroy the chiral content fails in the strongest way at the fillings the lens names: there, exclusion leaves no band content at all (at one record per site), or none at all (above it).

**Mutation census.** Four of five mutations are caught, each in its own family:
- a wrong sense fails L2;
- dropping `ε` fails S1;
- a root-sign bug fails F1;
- dropping `m²` fails F2.

A uniform exchange sign is not caught. This is expected: Theorem X2's bound, and X1, hold for every composition.

## 3. Where the route stops (not claimed)

- **Larger `a`.** For `a ≥ 1/12` the lowest window can hold many holes (float: about 0.07 per site at `a = 0.1`; more for larger `a`). The hard-core dynamics there — an interacting hole gas moving through a coin background — is not solved. Whether its low-energy content has any sense structure is left to the ASSUMED anomaly theorem.
- **The anomaly theorem** for the interacting record gas is not proved (as in a1).
- **Near one record per site** the dynamics is bounded (X2), not solved.
- **Odd tori.** Exact half-filling at `a₀` uses even sides; in infinite volume it holds as a density.

## 4. What would finish it

- **The one-hole problem in a coin background.** At fixed total momentum `K` it has `2^{N−1}` internal states. Does its spectrum have point degeneracies in `K`, and of which senses?
- **The interacting anomaly theorem** for the record gas: a1's item 1, flux insertion with spectral flow.
- **A decision (parked)** on whether "one record per site at a time" could hold two coins on a site.

## Checks (`check.py`, about 6 s)

| Family | What it checks |
|---|---|
| L1 | levels, multiplicities and senses (exact) |
| L2 | chiral moments (sympy) |
| S1 | `ε` against `A`, `εT_1` against `A + mε`, no on-site part of `A` (exact, `4³`) |
| F1 | exact record counts on `4³` and `6³` for three `(a₀, a)`, and the odd-`3³` contrast |
| F2 | `(A + mε)² = A² + m²` (exact, `4³`) |
| X1 | one record per site freezes both compositions (exact, ring of four) |
| X2 | hermiticity (exact) and the width bound (float) |
| X3 | exact grid counts, and the float density |
