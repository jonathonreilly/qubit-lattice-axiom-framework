# C3 lane M-D: worker report (Claude Opus 5.5, max effort; 2026-10-10)

Verbatim. Adversarial check (Opus 5.5 xhigh) below the report. Codex sol referee: pending if the verdict is a FAIL or no-go.

**Verdict (worker):** INCONCLUSIVE

**Plain summary:** A composite's noise on the event substrate does not follow its total mass. Each constituent's path sum makes its own noise at its own mass vertices. The part of the noise that grows exponentially is the only part that can destroy interference. It is set constituent by constituent, at a rate k0 m_i m_j l per pair of constituents and never k0 M^2 l. So the heaviest constituent that carries Johnston mass vertices sets the coherence time. Many identical constituents shift that threshold by only a few percent.

The small part that does not grow follows the total mass density, as an elementary particle of mass M would. It is negligible: about 1e-79 for Rb-87 at 70 s.

For two separated interferometer arms, the visibility is exactly 1/(1+R), where R is one arm's relative variance, because separated arms use independent parts of the sprinkling.

A 1+1 toy confirms the structure. At equal total mass, an elementary particle's noise exceeds the composite's by a factor that grows with time: 3, then 20, then 77 over trip lengths 22 to 65. Cross-species noise channels do not grow.

Under the M-A chain law, which is not controlled, the outcome depends on what carries the mass:
- If nucleons are the Johnston particles, Rb-87 decoheres in about 10 ms, against the observed 2.3 s and 70 s. A neutron treated as elementary decoheres in 10 ms, against qBounce's 42.5 ms.
- If ~313 MeV constituent quarks are the Johnston particles, Rb-87 decoheres in about 90 ms.
- If only current quarks (2 to 5 MeV) and electrons carry mass vertices, with binding carried by massless fields, both experiments pass at about 440 s.

Read the other way, the 70 s experiment requires every Johnston mass scale in the atom to be below about 12 MeV.

Two things keep this from a PASS or FAIL. The chain exponent is not controlled. The substrate does not say what carries hadron mass, and the noise from binding vertices was not computed in 4D. The fixed reading is therefore INCONCLUSIVE.

# C3 lane M-D: composite centre-of-mass coherence on links (worker report; Claude Opus 5.5, max effort; 2026-10-10)

**Verdict under the fixed reading: INCONCLUSIVE.**
- **Pre-registration:** `PREREG.md`, stamped Sat Oct 10 02:06:20 UTC 2026, before any computation.
- **Test setting only.** The E1/E1' axiom conflicts apply: Lattice is replaced, and the causal order is supplied.

## Answer to the question: (b) for the part that decides coherence, (a) only for a negligible part, binding vertices open

1. **The exponential (chain) noise follows the constituent masses, not the total mass.** This is the only part that can decohere.
   - Each pair channel is a tachyon of mass **k0 m_i m_j l**, with k0 = 0.2549. A pair channel means constituent i in one replica runs on exactly the same links as constituent j in the other.
   - No channel carries k0 M^2 l.
   - Simultaneous channels add. The largest total rate is k0 l Sum m_i^2 = k0 M^2 l / N_eff, with N_eff = (Sum m)^2 / Sum m^2.
   - So the coherence time is set by the heaviest constituent that carries Johnston mass vertices.
   - N identical constituents give N^2 channel multiplicity. That shifts the threshold by only ln(2N^2) e-folds, a few percent.
   - The bundle algebra is EXACT. Additivity and multiplicity are ARGUED.
2. **The single-regeneration (first-chaos) noise follows the total mass density.**
   - When the composite is smaller than its packet, it equals the noise of an elementary scalar of mass M.
   - EXACT at leading order for a product composite; ARGUED for bound states.
   - Negligible: R_FC = 1.2e-79 for Rb-87 at 70 s, and 9.8e-87 for the neutron at 42.5 ms (s = 1 um).
3. **Binding carried by substrate vertices** adds its own pair channels. They were not computed in 4D, so (c) stays open for them. A 1+1 contact-ladder toy (exploratory) shows no rise toward the elementary-M noise.

**Consequence for the M-A conditional tension.** The total-mass mapping (Rb-87 at 1.2 us) is not what the substrate gives for a composite of Johnston constituents. The tension survives only if heavy constituents carry Johnston mass vertices (Section 5).

## Plain summary

Each constituent's path sum makes noise only at its own mass vertices, whose weight is b_i = -m_i^2/rho.
- When the two copies of the amplitude in E|F|^2 run along the same links, they build a positive-weight chain that grows as e^{k0 m_i m_j l tau}.
- Constituents ride separate chains. So the growth rates are set by constituent masses and only add up; they never combine into (Sum m)^2.
- The small non-growing part is coherent over the mass density, so it does follow M, but it is about 1e-79.
- Separated interferometer arms use independent parts of the sprinkling, so the visibility is 1/(1+R) of one arm.

At l = l_P, using the M-A chain law (conditional), the 70 s Rb-87 experiment needs every Johnston mass-vertex scale in the atom below about 12 MeV. The 2.3 s experiment needs it below about 63 MeV, and qBounce needs it below about 460 MeV.

| What carries the mass vertices | Rb-87 | neutron |
|---|---|---|
| nucleons | ~10 ms | ~10 ms |
| 313 MeV constituent quarks | ~90 ms | ~90 ms |
| current quarks plus electrons, with massless binding | ~440 s | ~450 s |

The chain exponent is not controlled, the substrate does not fix what carries hadron mass, and binding-vertex noise is not computed. Hence INCONCLUSIVE.

## What I read (in full)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. No primitive is used beyond scale_reference, for l = l_P units.
- From the packet:
  - TESTS.md: the rules; E1', E1'-b, and Campaign C3 including lanes M and **M-D** (fixed readings);
  - `agents/C3_M-A_report.md`, `agents/C3_M-A_referee.md`, `agents/C3_M-C_referee.md`.
- Code reused: the packet's `scripts/E1p/E1p_4_massive2d.py` (exact_W structure) and `E1p_4c` (1+1 conventions). The M-A chain formula and P_tr structure come from M-A/verify.

## Setting

- **Substrate:** a Poisson sprinkling of M^{1,3}, with rho = l^-4.
- **Kernel:** K_m = aL(I - abL)^-1, with a = sqrt(rho)/(2 pi sqrt6) and b = -m^2/rho.
- **1+1 control:** K = aC(I - abC)^-1, with a = 1/2 and the causal matrix C.
- **Composite:** N constituents of masses m_i, each a Johnston path sum on the **same** sprinkling. F_c = <psi_d | prod_i K_{m_i} (+ binding) | psi_s>.
- **Observable:** the two-arm visibility V = 2|E[F_1 F_2^*]| / (E|F_1|^2 + E|F_2|^2).

## 1. Pair channels of E|F_c|^2 (EXACT algebra, pure shared-link sector)

Expand E[F_c F_c^*] by Mecke over the 2N chains: N in replica A and N in replica B.
- Every link indicator obeys L^2 = L. A set of k chains on one link therefore gets a^k P1, with one presence probability, not one per chain.
- A shared link forces shared endpoints, so shared links come with shared vertices.
- With E[aL] -> G0, a run of a k-bundle has per link a^k P1 = a^{k-1} G0 and per vertex (prod_chains b) rho.
- So the bundle propagates as a^{k-1} times a propagator of mass^2 = -a^{k-1} (prod b) rho.

Consequences:
- **k = 2, chains (A_i, B_j):** M_ij^2 = a b_i b_j rho = (k0 m_i m_j l)^2. For i = j and one species this is M-A's k0 m^2 l, the part the referee confirmed exact for the pure shared-link sector.
- **k >= 3:** rate proportional to l^{k-1} prod m. This is suppressed by (m l)^{k-2} relative to the pair channels.
- **In-replica bundles (A_i with A_j):** they change the mean (an induced contact term of order b_i b_j rho) and cost (l/r_b)-type factors when r_b >> l (ARGUED).
- **No bundle carries the vertex weight b_M = -M^2/rho.** The elementary-M rate k0 M^2 l does not occur in a composite of Johnston constituents (EXACT within this sector).
- **Disjoint simultaneous pair channels add their rates** (ARGUED: needle overlap between chains of different constituents is O((l/r_b)^4)).
  - The maximum over matchings is k0 l Sum_i m_i m_sigma(i) <= k0 l Sum m_i^2, by the rearrangement inequality.
- **Same-species pairs** in an (anti)symmetric state: relabelling shows each of the N_s^2 channels (i, j) equals the direct one (ARGUED).
- **Cross-species pairs (m_i != m_j):** the shared chain carries no phase, but its end factors carry e^{-+i(m_i - m_j)t}. Integrating over the start and end times suppresses them by about M_ij^2 / (M_ij^2 + (m_i - m_j)^2) (ARGUED; CHECKED in 1+1, Table A).

**Composite law, conditional on the M-A closure per channel:**
1 + R_c = prod_s Sum_k C(N_s,k)^2 k! r_s^k, where r_s = R_chain(m_s, tau) = C k0^2 (m_s l)^6 x h(x) / (16 pi P_tr), and x = k0 m_s^2 l tau.

The M-A caveats carry over unchanged: E_2, signed cross terms and the end factor C are not controlled.

## 2. First chaos: single regeneration

- **Product rule (EXACT identity).** For F_c = prod F_i: D_z F_c = Sum_i D_z F_i prod_{j != i} F_j + (terms with two or more D_z).
- **Leading order (ARGUED: drops first-chaos correlations of D_z F_i with F_j).** With M-A's bulk kernel E D_z F_i = (b_i/2) phibar_a,i phibar_s,i:

  E D_z F_c / Fbar_c = -(1/(4 rho)) Sum_i m_i p_i(z)   (rest frame; p_i is the normalised one-body density)

  This is the **mass density**.
- Hence R_FC,c = (l^4/16) int (Sum_i m_i p_i)^2 d^4z. For a composite smaller than its packet this is M^2 l^4 tau / (16 V_eff), the elementary-M value. A larger composite gives less.
- **At l = l_P** (`out/translate_md.out`, s = 1 um, V_eff = 126 s^3):
  - Rb-87 at 70 s: 1.2e-79;
  - neutron at 42.5 ms: 9.8e-87.

## 3. The interferometric observable

V = |1 + C_12| / (1 + R) for balanced arms, with F_k = Fbar_k (1 + eps_k) and C_12 = E[eps_1 eps_2^*].
- **EXACT.** A chain from y to x lies in the Alexandrov interval I(y,x). If the arms' regions (from source support to detector support) are disjoint, F_1 and F_2 depend on the Poisson process on disjoint sets. They are therefore independent, C_12 = 0, and **V = 1/(1+R)**. The coherence time V = 1/2 corresponds to R = 1.
- **ARGUED, common segments.** Real arms share the splitter and recombiner. Noise accrued there is common-mode, so V ~ (1 + R_common)/(1 + R_total); only the separated proper time costs visibility.
- **ARGUED, overlapping orthogonal states** (qBounce gravitational states).
  - The shared chain's tachyon propagator ~ e^{M_t sqrt(dt^2 - dx^2)} spreads its endpoints over sqrt(2 tau/M_t) ~ 4e5 m (nucleon scale, 30 ms). That is much larger than the apparatus.
  - So C_12 is proportional to |<psi_2|psi_1>|^2 ~ 0, and V = 1/(1+R) again.
- **CHECKED in 1+1** (Table B): V estimated from pairs of independent arms matches 1/(1+R) within Monte Carlo error for R <~ 3, e.g. 0.799 against 0.804 and 0.443 against 0.422. For R >~ 3 the pair estimator has a floor of about 0.07-0.1.

## 4. 1+1 checks

**Table A: EXACT 1+1 cross-channel law** (`scripts/exact2d_cross.py`, `out/exact2d_cross.out`).
- The law: W_ij = Kbar_i Kbar_j + b_i b_j rho int Kbar_i Kbar_j W_ij. It is Mecke-exact because 1+1 chains have no emptiness condition.
- The table gives the connected part at tau = 60 (rho = 1).

| (m_i, m_j) | connected part, tau = 60 | growth |
|---|---|---|
| (0.5, 0.5) | 0.030 | slow |
| (0.7, 0.7) | 0.93 | rate 0.0955 (the m^3/4 rule gives 0.0857) |
| (1.0, 1.0) = elementary M = 1 | 1.85e4 | rate 0.258 (rule: 0.25) |
| (0.4, 0.6) | 2.7e-4, oscillating about 1e-3 | none |
| (0.3, 0.7) | -1.3e-4, oscillating about 1e-3 | none |

- At the same total mass 1.0, the elementary connected part exceeds the constituent channels by 6e5 or more.
- Cross-species channels do not grow.

**Table B: Monte Carlo, product composites against an elementary scalar of total mass** (`scripts/t2d_product.py`, `out/analyse_t2d.out`).
- Diamonds U = 30, 45, 60 (N about 900, 2000, 3600).
- 1200, 600 and 400 realizations; bootstrap medians.
- Gaussian blobs with sigma_t = 3 and sigma_x = 2.5, modulated on shell.
- Trip lengths T = 22.4, 43.6, 64.9.

| composite (M) | R_c at T = 22 / 44 / 65 | R_M (elementary) at T = 22 / 44 / 65 | R_M/R_c |
|---|---|---|---|
| (0.3,0.3) (0.6) | 0.245 / 0.565 / 0.866 | 0.360 / 1.37 / 5.93 | 1.5 / 2.4 / 6.8 |
| (0.4,0.4) (0.8) | 0.512 / 1.41 / 3.23 | 1.65 / 27.9 / 248 | 3.2 / 19.9 / 76.6 |
| (0.3,0.45) (0.75) | 0.409 / 1.04 / 1.78 | 1.03 / 12.4 / 96.7 | 2.5 / 12.0 / 54.5 |
| (0.3,0.3,0.3) (0.9) | 0.624 / 1.64 / 2.77 | 4.86 / 473 / 447 (*) | 7.8 / 288 / 161 (*) |
| (0.3,0.6) (0.9) | 0.719 / 2.44 / 10.8 | 4.90 / 435 / 444 (*) | 6.8 / 178 / 41 (*) |

(*) R_M is heavy-tailed and estimator-limited at R >~ 100; the 16-84% intervals are [180, 1800].

Readings from Table B:
- R_c sits between the independent-constituent prediction prod(1+R_i) - 1 and the coherent first-order N^2 R_m (identical constituents: 0.245 against 0.229).
- (0.3, 0.6) is dominated by its heavier constituent (R_0.6 = 5.9 at T = 65).
- R_M/R_c grows with T: about 0.075 per unit for (0.4,0.4) against 0.8, approaching the asymptotic difference (0.8^3 - 0.4^3)/4 = 0.112 (pre-asymptotic, as in E1p_4b).
- The same-sprinkling cross-species noise correlation E[eps_1 eps_2^*] is positive and of the size of the lighter constituent's R. It does not grow like the elementary-M channel.
- Status: CHECKED structure. 1+1 has no link-indicator variance, so its rates are m^3 l^2/4, not k0 m^2 l. The toy checks the channel structure, not the 4D rate.

**Table C: bound-composite contact ladder (exploratory)** (`scripts/t2d_bound2.py`, `out/analyse_t2dB2_U30_m06.out`).
- The model: A = D(I - gD)^-1 with D = K o K, two identical m = 0.6 constituents, T = 22.4, and a real-time contact vertex g = i*gamma.
- Near threshold (w = 1.0-1.2, 2m = 1.2), g = -0.5i enhances |E F_A| by 2-2.5x over g = 0.
- At the same w:

| case | R |
|---|---|
| g = -0.5i (attraction) | 1.67-1.95 |
| free pair (g = 0) | 2.4-3.0 |
| elementary of mass M = w | 16-100 |

- **Not resolved:** there is no isolated sub-threshold pole at this T. The resolution sigma_t^-1 is about 0.33, and the low-w rise is the particle-antiparticle part of K o K, present at g = 0.
- A first scan (m = 0.45, w >= 0.6) did not resolve a pole either. A U = 42 run was stopped for time, and its log is empty.
- **Weak evidence only** that substrate-carried attraction does not push the noise to the M scale in 1+1.

## 5. Translation at l = l_P: CONDITIONAL on the M-A chain closure

Inputs:
- k = k0 and C = 1; C is scanned from 1/16 to 100, which moves tau_coh by at most 2%.
- P_tr = 1, the matched output port of an interferometer (ARGUED). P_tr < 1 would only shorten tau_coh.
- V = 1/(1+R_sep). Cross-species channels are dropped.
- Masses (COMPARATOR):
  - current quarks: u 2.16 MeV, d 4.67 MeV;
  - constituent quarks: about 313 MeV;
  - Rb-87 = 37p + 50n + 37e.
- Outputs: `out/translate_md.out`, `out/kmargin_md.out`, `out/mmax_md.out`.
- **Check:** the script reproduces M-A's 10.0 ms (nucleon) and 1.2 us (elementary Rb-87).

| model: what carries Johnston mass vertices | neutron tau_coh (qBounce 42.5 ms) | Rb-87 tau_coh (2.3 s; 70 s) | k_crit/k0 |
|---|---|---|---|
| (iv) total mass, elementary (M-A mapping) | 10.0 ms: conflict | 1.2 us: conflict | n: 0.24; Rb: < 1e-6 |
| (i) nucleons (+ e) as elementary scalars | 10.0 ms: conflict | 9.7 ms: conflict | n: 0.24; Rb: 4.4e-3 / 1.5e-4 |
| (ii) constituent quarks, 313 MeV | 91 ms: ok | 89 ms: conflict | n: 2.1; Rb: 0.039 / 1.3e-3 |
| (iii) current quarks + e, massless binding (b = 0) | 449 s: ok | 436 s: ok | n: 9.9e3; Rb: 183 / 6.2 |

k_crit/k0 is the rate coefficient (in the exponent and the prefactor) at which tau_coh equals the observed time.

- **Thresholds** (same conditions; N = 1 to 261 changes them by < 2%): the heaviest Johnston-vertex mass scale must be below
  - **11.6 MeV** for Rb-87 at 70 s;
  - **63 MeV** for Rb-87 at 2.3 s;
  - **459 MeV** for qBounce.
- Electrons are irrelevant: their rate is 2.8e-11 per metre.

## 6. Verdict against the fixed reading

The fixed reading requires a controlled law.
- **PASS** needs coherence longer than 70 s (Rb-87-like) and longer than 42.5 ms (neutron-like).
- **FAIL** needs decoherence below either time.

Neither is met:
1. **The chain exponent is not controlled.** Every tau_coh above uses the M-A closure: k0 for the full variance, E_2, signed cross terms, and the end factor C. The M-A referee left all of these open.
2. **The rigorous parts are far from the bars.** The rigorous lower bound (first chaos) gives R ~ 1e-79, far from V = 1/2. No controlled upper bound exists.
3. **The outcome depends on the constituent model.** Models (i), (ii) and (iv) conflict with experiment, and (iii) passes. The substrate does not fix which particles carry Johnston mass vertices.
4. **Binding-vertex pair channels in 4D were not computed.** They could reintroduce a hadronic-scale rate even in (iii). By dimensional analysis only (ARGUED, unverified), substrate-carried QCD-like binding with an O(1) coupling could give rates near the 300 MeV scale. That would put Rb-87 near 0.1 s, which conflicts.

**INCONCLUSIVE.** The firm deliverable is the scaling result.
- The decoherence-setting noise is per-constituent: k0 m_i m_j l per channel, at most k0 l Sum m_i^2.
- It is never k0 M^2 l.
- Only the negligible single-regeneration part follows the total mass.

## 7. What this does to the M-A conditional tension

- **Removed:** the total-mass mapping (1.2 us for Rb-87). It is not how a composite of Johnston constituents propagates.
- **Replaced by a sharper conditional requirement.** If the chain law holds, the 70 s Rb-87 experiment requires all Johnston mass vertices inside the atom to sit below about 12 MeV.
  - Nucleon mass must then not be carried by Johnston mass vertices.
  - It must be carried by massless (b = 0) fields whose interaction vertices do not generate hadronic-scale pair channels.
  - That is a price-type condition on how hadrons are built on the substrate, not a derived result.

## 8. Scope and caveats

- **Constituents are scalars.** Quarks and electrons are spin-1/2; lane D says chiral matter needs an extra primitive.
- **P_tr = 1 and the end factor C are ARGUED.**
- **The visibility identity is EXACT only for disjoint arm regions.**
- **The 1+1 toy checks structure, not the 4D rate.**
- **The bound toy did not resolve a pole.**
- **Comparator numbers** (qBounce 42.5 ms; Rb-87 2.3 s and 70 s; quark masses) are taken from the M-A referee and memory, and were not re-verified here.

## What a referee should check

1. **The bundle algebra.**
   - a^{k-1} G0 per shared link and (prod b) rho per shared vertex;
   - M_ij = k0 m_i m_j l;
   - shared links force shared vertices;
   - no bundle carries b_M;
   - the k >= 3 suppression.
2. **Composite combinatorics.**
   - the additivity of simultaneous pair channels;
   - the matching count C(N,k)^2 k!;
   - the identical-particle relabelling;
   - the cross-species end-factor suppression.
3. **First chaos.** The product D_z identity and the mass-density law, including the dropped correlations.
4. **Visibility.** The disjoint-region independence lemma; the common-segment and orthogonal-state arguments, including the sqrt(2 tau/M_t) endpoint spread.
5. **1+1 results.** The exact cross-channel Volterra and the Monte Carlo tables, including the heavy tails in R_M.
6. **Translation inputs.** P_tr = 1 for an interferometer port, the C scan, the mass choices, and the thresholds 11.6, 63 and 459 MeV.

## Labels

- **EXACT:** the bundle algebra and channel rates (pure shared-link sector); the absence of a b_M channel; the product D_z identity; the visibility lemma for disjoint regions; the 1+1 Mecke cross-channel law.
- **CHECKED:** the 1+1 tables A and B; V = 1/(1+R) in 1+1; the translation reproducing M-A's 10 ms and 1.2 us.
- **ARGUED:** channel additivity and combinatorics; the cross-species suppression; the first chaos for bound states; the common-segment and orthogonal visibility arguments; P_tr = 1; the bound-toy reading; the binding-vertex estimate.
- **CONDITIONAL** (M-A closure): every l = l_P coherence time and threshold.
- **COMPARATOR:** the experimental times and the quark masses.

## Files

All files are under `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-D/`.

- **Top level:** `PREREG.md`, stamped 02:06:20Z before any computation.
- **scripts/:**
  - `exact2d_cross.py`: the exact 1+1 cross-channel law;
  - `t2d_product.py`: the 1+1 product composites and elementary runs;
  - `analyse_t2d.py`: R, V and bootstrap;
  - `t2d_bound.py`, `t2d_bound2.py`: the bound ladder toy;
  - `analyse_t2dB.py`;
  - `translate_md.py`: the l_P coherence times;
  - `kmargin_md.py`: k_crit;
  - `mmax_md.py`: the mass thresholds.
- **out/:**
  - `exact2d_cross.out`;
  - `out_t2d_U30_s11.npz`, `out_t2d_U45_s12.npz`, `out_t2d_U60_s13.npz`, `run_U30.log`, `run_U45.log`, `run_U60.log`, `analyse_t2d.out`;
  - `out_t2dB_U30_s21.npz`, `runB_U30.log`, `analyse_t2dB_U30.out`;
  - `runB_U42.log`: empty, the run was stopped;
  - `out_t2dB2_U30_s31_m0.6.npz`, `runB2_U30_m06.log`, `analyse_t2dB2_U30_m06.out`;
  - `translate_md.out`, `kmargin_md.out`, `mmax_md.out`.

No repository file was edited; `git status` is clean. All runs used at most 2 threads and finished in under 4 minutes each.

---

## Adversarial check (Opus 5.5 xhigh)

**Supported:** True

**Corrected verdict:** INCONCLUSIVE, supported, with corrections to the scope and the checks. The fixed reading needs a controlled law, and none exists here. Every l_P coherence time rests on the M-A chain closure (k0, E_2, signed cross terms, end factor C), which the M-A referee left uncontrolled. The only rigorous piece, first chaos, is about 1e-79. The outcome also flips with the constituent model, which the substrate does not fix: models (i), (ii) and (iv) conflict with experiment and (iii) passes. Binding-vertex channels are not computed. So neither PASS nor FAIL can be reached. The scaling answer needs a narrower statement. Inside the pure shared-link sector, the exponential noise is per-constituent: k0 m_i m_j l per pair channel, at most k0 l Sum m_i^2, never k0 M^2 l. First chaos follows the total mass density and is negligible. Outside that sector (E_2-type correlated-emptiness terms and signed cross terms) nothing is established for composites. So the total-mass mapping is 'not produced by the shared-link sector', not 'removed'.

**Issues:** 1. Table B is misread, and the 1+1 toy contradicts the report's own composite law.
- The report says R_c 'sits between' the independent prediction and N^2 R_m. In fact R_c is above N^2 R_m in every row and at every T, including the report's own example (0.245 > 0.229).
- R_c also exceeds the composite law 1+R_c = Sum_k C(N,k)^2 k! r^k (with r = R_m) by a factor that grows with T. On the worker's data, with paired-bootstrap 95% intervals:
  - (0.4,0.4): 1.10, 1.19, then 1.38 [1.21, 1.56];
  - (0.45,0.45): 1.13, 1.26, then 1.57 [1.27, 1.96];
  - (0.3,0.3,0.3): 1.09, 1.22, 1.22 [1.11, 1.36].
- A fresh seed at U=60 confirms the excess: 1.06 to 1.34.
- So the toy does not check channel additivity or the matching count. Sectors outside the matched pair channels contribute in 1+1. Only the qualitative result holds: R_M/R_c of 5 to 290, growing with T.

2. The 1+1 visibility check is circular. vis() in analyse_t2d.py uses independent realizations as the two arms, so V = 1/(1+R) holds by construction. It tests the estimator, not the physics, so the 'CHECKED' label is wrong.

3. Table A's cross-species non-growth does not test the 4D mechanism.
- In 1+1 it comes from beating in the J0(m_i tau)J0(m_j tau) kernel; 1+1 has no link sector.
- The 4D claim is a non-oscillating tachyonic bundle with phases only in the end factors.
- So the 4D cross-species suppression stays ARGUED, not CHECKED.

4. The 'firm deliverable' is stated too broadly.
- 'Never k0 M^2 l' and Section 7's 'Removed: the total-mass mapping' hold only in the pure shared-link sector.
- The M-A referee flagged E_2 (shared empty-interval correlations, possibly exponentially enhanced) and signed cross terms as uncontrolled. They are not analysed for composites.

5. The disjoint-region visibility lemma is EXACT but never applies to these experiments.
- Real arms share the source and detector.
- For slow atoms over milliseconds to seconds, the Alexandrov intervals are light-ms to light-s wide and contain both arms.
- So V = 1/(1+R_sep) in Section 5 is ARGUED throughout.

6. Labels are inconsistent on first chaos.
- The answer calls the mass-density law 'EXACT at leading order'; Section 2 calls it ARGUED.
- The '1e-79 rigorous lower bound' is computed from the approximate kernel with correlations dropped. It is an estimate of the rigorous bound, not the bound itself. The verdict is unaffected because the number is negligible.

7. Minor: the 'asymptotic difference (0.8^3 - 0.4^3)/4 = 0.112' ignores the composite's second simultaneous channel. Under the report's own law it is 0.128 - 0.032 = 0.096.

None of these moves the verdict away from INCONCLUSIVE.

**Re-runs:** All checks are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/M-D/verify/. All runs used OMP_NUM_THREADS=2. No repository file was edited.

1. Translation and thresholds: re-ran translate_md.py and mmax_md.py. Both outputs match the worker's byte for byte.
   - Coherence times: neutron 10.0 ms; Rb-87 1.2 us (total mass), 9.7 ms (nucleons), 89 ms (313 MeV quarks), 436 to 449 s (current quarks).
   - Mass thresholds: 459, 63 and 11.6 MeV.
   - Scanning C from 1/16 to 100 moves the times by at most 2%.

2. Hand checks:
   - First chaos: R_FC = 9.78e-87 for the neutron at 42.5 ms and 1.20e-79 for Rb-87 at 70 s.
   - Rb-87 constituent counts: 124 u + 137 d = 261 quarks, 37 e.
   - Endpoint spread sqrt(2 tau/M_t) = 4.4e5 m.

3. Table A: re-ran exact_Wij on two grids, (300,100) and (500,160). Results at tau = 60, converged:
   - (1,1): 1.85e4;
   - (0.7,0.7): 0.933;
   - (0.4,0.6): 2.66e-4.

4. Composite law against Monte Carlo (law_vs_mc.py): compared Sum_k C(N,k)^2 k! R_m^k with the worker's npz data at U = 30, 45 and 60, using a paired bootstrap. R_c exceeds the law by 4% to 57%, and the gap grows with T.

5. Fresh 1+1 Monte Carlo: U = 60, seed 977, n = 300, 127 s.
   - R_c/law = 1.06 to 1.34.
   - R_c is above N^2 R_m in every case.
   - R_M/R_c = 5.4, 173, 150 and 114 for (0.3,0.3), (0.4,0.4), (0.45,0.45) and (0.3,0.6).
   - So the qualitative claim (composite noise far below the elementary-M noise) reproduces. The quantitative composite combinatorics do not.
