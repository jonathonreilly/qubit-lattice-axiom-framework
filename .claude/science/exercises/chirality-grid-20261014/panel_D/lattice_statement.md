# Panel D statement: lattice chiral gauge theory lens

**Lens:** lattice chiral gauge theory (Lüscher's construction, overlap and domain-wall fermions, Kaplan, symmetric mass generation, Golterman–Shamir, reflection positivity of lattice actions).

**Provenance.** Claude Opus 5.5. This is the same model family as the supervisor and every exercise agent, so it is not independent. Nothing here is refereed. Jon decides; this statement only advises.

**Read in full:** `docs/MINIMAL_AXIOMS_2026-06-29.md` (AX); the exercise's `SUMMARY.md` (SUM), `ROUTES.md` (RT), `WALL.md`, `ASSUMPTIONS.md` and `OUTSIDE_VIEW.md` (OV).
**Read in part:** `DEFERRED_DECISIONS.md:121-146`; gravity `SUMMARY.md` §26–27 (GS); gravity `TESTS.md` R19-28/R19-33 records (GT); `agents/panel_F/SYNTHESIS.md` (PF); `combos/X2`, `combos/X3` and `kills/K2c` reports; `docs/DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS_…_2026-09-24.md` (LINK).

**Labels:** proved / checked / suggested / reading / comparator.

**Scripts:** `panel_D/lattice/scripts/` (all under 150 MB):
- `corner_orbits.py` with `.out`;
- `pg_weight_rp.py` with `.out`;
- `torus_tri/`: K2c's own code, copied unchanged, run with the triangle weight on the torus.

---

## Plain words first

1. **Matter per site (D1).** The Standard Model does not fit on one qubit per site, and chirality is not the reason.
   - A colour triplet needs three slots at one point.
   - The repo's own link note shows an SU(3) link needs at least 3 qubits' worth of states.
   - The gravity root already needs about 90 fermion modes per site.

   So the real question is how much bigger, not whether. My advice:
   - name a **finite** enlarged site (option b) as an axiom price, with its size set by content;
   - do not hide it in an unstated blocking (a);
   - do not refuse (c), because refusing also refuses colour.
2. **Range (D2).** Do **not** make an infinitely-generated kernel law content.
   - It buys exactly one route, the exact overlap.
   - That route also needs an infinite fibre per site, and it loses reflection positivity once forces are on. That failure comes from the overlap itself, not from the gauge weight (see below).
   - Everything else that exact chirality buys can be had, to better than observational accuracy, from a finite stack of about 50–150 layers. That stack is mirror-symmetric, though, so chirality still has to come from interactions.
3. **Time (D3).** Chirality does not favour either set. Make this decision on the gravity and Lorentz grounds, knowing two chirality facts:
   - **Set B cannot host the framework's own three-generation corner package (X2).** With time–space rotation symmetry, the special momenta come in groups of 1, 4, 6, 4, 1, never 3.
   - **Set B's only extra chirality asset, the exact overlap, is the part that fails reflection positivity.**

   With no gravity tie-break, I lean to set C: it stays inside the axioms, and unitarity is built in.
4. **Compute (D4).** Do not fund weeks of in-house QMC yet.
   - The decisive question is the field's open problem, and 2+1D proxies do not decide 3+1D (the exercise's own rule, SUM:65).
   - Pass two cheap gates first: NT-3, and a sign-problem check of the exact X2 Hamiltonian.
   - Then ask the people who own this question. Golterman–Shamir come first, because they will say fastest whether X2 is already dead.
   - Record the prices either way.

---

## D1. Matter per site

**Recommendation: (b), a finite enlarged site, named as an axiom price, with its size left as a downstream parameter fixed by content. Not (a) as an unstated blocking, and not (c).**

**Reasons.**

1. **The enlargement is forced by the gauge content, not by chirality** (proved in the repo for links; reading for the program).
   - LINK:3 (claim_scope): an SU(N) link needs at least 2N states, and a qubit carries no SU(N) link. Independent U(1)×SU(2)×SU(3) links need 48 states; a joint construction needs 12.
   - PF:52: the gravity root's ~90 fermion modes per site already make a root "site" a ≥90-qubit block.
   - X2's object is C²⊗C¹⁶ per site (X2:55), i.e. 32 complex fermion modes, before any fermion-encoding overhead (Jordan–Wigner or Chen–Kapustin, OV:170-171).
   - So D1 is already decided against "one qubit" by the SM gauge group and by gravity. The chirality exercise only fixes the fermion count at 16 Weyl per generation (the mod-16 condition, RT:9 and :43), not 15.
2. **(a) is not a free relabelling** (reading).
   - Exact lattice gauge invariance (Wilson, Kogut–Susskind, quantum links) needs the gauge group to act on-site, with Gauss's law at each gauge-covariant point.
   - If colour lives across several fine sites, gauge transformations act on blocks. A fine-scale nearest-neighbour rule covariant under fine translations (AX:57) then either moves colour slots into one another, or must privilege block origins.
   - That second option conflicts with "No site is privileged" (AX:40), unless the blocking arises spontaneously.
   - Staggered fermions are the one standard case where fine translations act as internal (taste) transformations. They do this for a finite group, not for continuous SU(3).
   - So (a) is either (b) in disguise, or a spontaneous-superlattice hypothesis that needs its own test.
3. **(c) refuses more than chirality** (reading).
   - With one qubit per site and nothing on links, non-abelian gauge fields would have to emerge from spin models.
   - Parton gauge redundancy gives emergent SU(2) on spin-½ lattices (comparator: Affleck–Zou–Hsu–Anderson; Wen's projective symmetry groups), but no emergent SU(3)×SU(2)×U(1) with chiral matter is known.
   - That is a separate open programme, not an option.
4. **Finiteness is the right line to hold** (proved, from the exercise's results).
   - Every no-go that matters is insensitive to how large a finite site is: Lemma R is fibre-independent (RT:11, :154), and Fidkowski–Xu applies to any finite-dimensional site (OV:56).
   - The only thing an infinite site buys is exact Ginsparg–Wilson chirality, and that is D2.
   - So the axiom price to name is "a finite M_{2^N}(C) per site, with N fixed by content". Do not name a specific N now.
   - The candidates on the table: 16×2 fermion modes (X2), ~64·L_s (slab, X1), plus links.

**On #4 (DEFERRED_DECISIONS.md:139-142).** The wake condition has fired (RT:74, K3). M₄(C) "for γ5" stays dead (SUM:63). The live item is site size, and this lens says it was live before chirality.

---

## D2. Range

**Recommendation: decline. Keep finite range with finitely many local degrees of freedom (AX:57 as written). Record Lemma R as a price note. Use finite-L_s domain-wall stacks for mass protection, and interactions for chirality.**

**Reasons.**

1. **What D2 actually buys** (reading, on refereed parts).
   - Lemma R (RT:146-154, codex-confirmed): exact GW needs a kernel outside the rational class.
   - X3-C (RT:128, :164): for the overlap, the non-rational kernel and an infinite real-time fibre co-occur. The block-Hankel rank keeps growing (X3:134).
   - So **D2 = yes implies D1 = infinite site** after OS reconstruction. That is a bigger break of the Qubit axiom than any finite (b).
   - Comparator: this is Horváth's and Bietenholz's 1998–99 no-ultralocal-GW result, sharpened to rational kernels with auxiliaries (OV:55).
2. **And it does not deliver a real-time theory without a further price** (checked by K2/K2c; scope-limited by the referee).
   - Gauged RP fails for the overlap in the 2D U(1) proxy, on the torus included (RT:190-204).
   - The obvious objection is that the failure might come from the gauge weight: the hard indicator has sign-changing character coefficients, and that alone breaks pure-gauge RP at odd Lx (K2c §2b).
   - **That objection is closed:**
     - The triangle weight (1−|θ|/δ)₊ is strictly admissible (support |θ| < δ). Its coefficients are (sin(nδ/2)/n)²·const ≥ 0, so it is OS–Seiler positive for every number of crossing plaquettes.
       - Proved (Bochner plus Schur).
       - Checked: Lx = 1–5 PSD, while the hard weight reproduces K2c's −8.95e-3 at Lx = 3 (`pg_weight_rp.out`).
     - The non-abelian version holds the same way: f = g ⋆ g̃, with g a class function supported in the ε/2 ball, has character coefficients |ĝ_r|²/d_r ≥ 0 and support in the ε ball, because ‖1−UV‖ ≤ ‖1−U‖ + ‖1−V‖ (proved, elementary).
     - K2's "Fejér" measure **is** this triangle weight (`lat2d.py:93`, `:122`). The overlap is certified negative under it on W-matched open pools (K2c `V2_open_Lt12_wgsearch_tri.out`: −5.6e-5 relative, while the Wilson and pure-gauge controls are PSD). K2c:115 already drew this conclusion.
     - **Torus with the triangle weight (new, checked here):** this is the loophole left by K2c, whose torus runs used only the hard weight.
       - The overlap is certified negative: λ_min −1.43e-4, relative −6.2e-6, error estimate 7.7e-11.
       - On the same pool the Wilson control (+4.5e-13) and the pure-gauge control are PSD.
       - This is the same size as K2c's hard-weight torus value (−6.3e-6).
   - **Reading:** the RP failure is the overlap determinant's own. No choice of admissible, positive gauge weight removes it.
   - So route 1 in real time needs Π-W for matter, which conflicts with AX:60-61 (site-level probability distributions) and WALL:44 (no non-normalizable readout probabilities).
   - In lattice QCD one shrugs at RP violation at the cutoff, because a → 0. Here a is physical, and records live at the cutoff.
3. **What exact GW protects, a finite stack protects well enough** (suggested estimate; comparator: lattice-QCD domain-wall practice).
   - The bare 5D determinant (no Pauli–Villars fields) is RP: Osterwalder–Seiler for a 5D Wilson fermion, checked PSD on all K2c pools (RT:184; K2c:55).
   - Its residual mass is m_res ~ e^{−cL_s}/a.
   - Keeping m_res below m_e at a = ℓ_P needs cL_s ≳ ln(M_Pl/m_e) ≈ 52.
   - The strain-hazard channel of PF §4 is the strain derivative of the same additive mass. Using PF's uncorrected exceedance (2e8), it needs only cL_s ≳ 19.
   - So L_s ≈ 50–150 for c ≈ 0.3–1. That is about 64·L_s ≈ 3–10 × 10³ modes per site per generation, the same order as F4's ~10³.
   - This also removes the 1-in-1e20 critical-mass tuning PF:§1(b) describes, with no Π-W.
   - **But it is vector-like.** The mirror sits on the far wall with the same charges. Chirality then needs far-wall symmetric gapping, which is route 3 / F4-A / X1, frontier question (I).
4. **An option the list omits: the gauge-fixing approach** (comparator: Rome; Bock–Golterman–Shamir 1998; Golterman–Shamir 2004).
   - It keeps finite range and Wilson-type fermions, and drops exact gauge invariance at the cutoff.
   - It needs tuned counterterms, including a gauge-boson mass.
   - The non-abelian case is unfinished: Neuberger's 0/0 needs equivariant BRST.
   - Under the program's number counting it costs tuned numbers. I do not recommend it, but it belongs on the price list.

---

## D3. Time

**Recommendation: chirality is neutral, with two exceptions that Jon should weigh. Absent a gravity tie-break, set C for matter. If set B is chosen for Lorentz reasons, take it only in its reflection-positive form (finite range and finite fibre), not with the overlap.**

**The chirality facts.**

1. **Set B excludes X2's three generations** (proved, elementary; checked by `corner_orbits.out`).
   - With W(B4) symmetry, the 16 Brillouin-zone corners {0,π}⁴ fall into Hamming-weight orbits of size 1, 4, 6, 4, 1, with chirality (−1)^hw.
   - Symmetric single-chirality light sets have sizes {1, 2, 6, 7, 8} (right-handed) or {4, 8} (left-handed). **Never 3.**
   - On Z³ (set C) the orbits are 1, 3, 3, 1, and 3 is natural.
   - The fourth hw1 corner in Z⁴ is the time doubler, which X3:296 shows as a π pole for naive time differences (H1 = −1.00, so not RP). With staggered time it becomes a fourth light copy.
   - Breaking the time–space rotation to remove it gives up set B's Lorentz protection.
   - This is a cleaner form of X2:214 ("continuous time is required").
2. **Set B's extra chirality asset is the non-RP part.**
   - Every RP-safe set-B action is in the Osterwalder–Seiler class: positive-type plaquette weights; Wilson r = 1, staggered (two-step) or bare-5D domain-wall fermions; θ-real on-site multi-fermion terms.
   - Within that class, chirality reduces to the same symmetric-gapping question (I) as in set C. So set B adds nothing for chirality without Π-W.
   - In the free theory, set B's clean real-time spectrum (X3-A) is real (RT:126). It does not survive gauging (above).
3. **Set C keeps the qubit picture whole.**
   - The Hilbert space is primary (AX:47), and unitarity is manifest.
   - Gauss's law is exact with quantum links (LINK).
   - There is no OS-reconstruction record cost (R2-5 is OPEN in set B and is a Record-sector cost; GT:8774).
   - The strongest SMG evidence is Hamiltonian: 2+1D QMC and 1+1D DMRG (OV:93-95).
   - The disentangler programme is Hamiltonian too (OV:98-99).
   - Set B is also an axiom change (Z³ → Z⁴ against AX:37), while set C's continuous time is downstream dynamics (AX:114-123).

**The non-chirality fact that may override this** (comparator: standard lattice field theory).
- Hypercubic symmetry leaves the O(4)-invariant operator as the only dimension-4 kinetic term. That is why set B fixes every matter speed with no tuning, and it is the only symmetry that does (GS:774).
- Set C pays 4 tuned speeds per charge class, reset at every order, or a counting clause (GS:778).
- I rate this as the most robust mechanism on either side. It is gravity's call, and it is a real reason to prefer set B.
- Set B also already pays Π-W or Π-NL for the conserved GR bridge (R19-33 B-RP-FAILS, GT:8909-8913).
- I would **not** count Π-W for matter as "count once" with gravity's constraint sector (suggested). Matter's negative-norm states would be charged, propagating and record-forming, not a constraint sector.

---

## D4. Compute and collaborators

**Recommendation: (b), with a narrow ask, gated by two cheap internal checks, and with (c) as the standing record until then. (a) only after the gates pass, and then for a model the collaborators have vetted.**

**Reasons.**
- **The decisive question (I) is the field's.**
  - The 4D numerics are specialist work: near SMG phase boundaries, intermediate broken phases appear generically (OV:95-96, K1).
  - The program's agents are one model family and unrefereed on QMC.
  - A sign or finite-size misreading after weeks of compute is a real risk.
- **Gate 1: NT-3 (T-G1 exact diagonalisation).** If the filtered quartic shows no unique symmetric ground state on small clusters, X2 should not get compute.
- **Gate 2: is the exact X2 Hamiltonian sign-free?** (suggested; about an hour of algebra.)
  - The filter acts on all four legs of the 16⊗16→10 channel (X2:55-70).
  - Check whether it can be written as a sum of θ-real squares of Majorana bilinears, which gives Majorana-reflection positivity (comparator: Li–Jiang–Yao; Wei et al.).
  - If not, "sign-free weeks of QMC" does not exist for X2 at all.
  - F4's far-wall model is pre-registered as sign-free (SUM:58), so this gate concerns X2 only.
- **Order of asks.**
  - Golterman–Shamir first. They are the adversarial owners of the zeros criterion, and GPR is X2's direct ancestor.
  - Then Catterall/Butt/Hasenfratz, whose 4D staggered SMG codes already see the intermediate phase (OV:96-97), for compute on whatever survives.
  - For the slab: You, Xu or Meng, or Chandrasekharan (fermion bag).
  - Kikukawa and Fukaya/Onogi only if NT-1 reopens route 1.

---

## How the decisions interact

- **D2 = yes ⇒ D1 = an infinite site** (X3-C co-occurrence), **and ⇒ Π-W for matter** to have any real time (K2c). So "accept D2" is really a three-price package: infinite fibre, infinite generation and non-positive measure. It is the most expensive path on the table.
- **D3 = set B does not force D2.**
  - The RP-safe set-B class hosts the slab (bare 5D domain-wall fermions, no PV, with far-wall gapping) and staggered SMG.
  - Set B forces D2 only if route 1 is the chosen route, and route 1 needs Π-W besides.
  - **D3 = set B does kill X2's three-corner generations** (orbit count). Under set B, generations are supplied as three copies.
- **D1 = (a) does not make D2 moot.** Lemma R holds for any finite fibre and any blocking (RT:11, :154). No finite D1 choice rescues exact GW.
- **D1 is forced by gauge content and the gravity root, independent of D2 and D3.** Decide it once, for the whole program.
- **D4 depends on D3.** The model to send differs:
  - X2 is a set-C Hamiltonian;
  - set B's chiral route is a Euclidean bare domain-wall stack with far-wall SMG, which is the Catterall/Hasenfratz home ground.
- **The two surviving chirality routes, and the gauge sector, may share one structure** (comparator plus suggested).
  - D-theory (Brower–Chandrasekharan–Wiese, 1999–2004) gets continuum-like non-abelian gauge fields from finite quantum links by dimensional reduction along an extra ladder. In it, quarks arise naturally as domain-wall fermions on the same ladder.
  - A single "internal ladder of L qubits per site" price could therefore carry finite-dimensional SU(3)×SU(2) links, mass protection, and the inflow slab's light wall.
  - Far-wall gapping is still needed for chirality.

---

## The strongest argument from my tradition, and the steelman against me

**From the tradition.**
- Forty years of lattice chiral gauge theory show one pattern. Every construction that keeps finite range, a finite fibre, exact gauge invariance and a positive Hilbert space either failed or reduced to symmetric mass generation. The record includes Smit–Swift, Eichten–Preskill to GPR, waveguides, and the 345 model (OV:82-84).
- The only nonperturbative success, Lüscher's abelian theory, pays non-ultralocality and lives in Euclidean space.
- Lattice QCD's practical lesson is that exact chirality is a luxury: domain-wall fermions at finite L_s with a tiny residual mass suffice for anything observable.
- So the program should:
  - keep finiteness and positivity;
  - buy mass protection with a finite stack;
  - record chirality as conditional on one named open conjecture, (I);
  - not pay three axiom-level prices (D2 plus an infinite site plus Π-W) for a route that is not even shown to work non-abelian.

**The steelman against me.**
- If Golterman–Shamir are right that symmetric-phase mirror zeros are kinematical, then Shamir's 1993 interacting no-go and their 2025 generalization (OV:54, :58) make every finite, positive, exactly gauge-invariant lattice vector-like.
- My recommendations then lead, by design, to **no chirality at all**.
- The only proven nonperturbative chiral mechanism (GW/Lüscher) would be thrown away in favour of a conjecture the field's sharpest critics think is false.
- On that view, the honest choice is to pay D2 and Π-W now and confine the negative norms to the cutoff. The K2c violations are small (1e-5 to 1e-6 relative).
- Exponential tails are observationally indistinguishable from finite range.
- Against D3 = C: hypercubic Lorentz protection is a mechanism, while 3 = |hw1(Z³)| may be numerology. X2-L8 (X2:126) shows that X2's generations bring a CKM-tied strain channel, a Lorentz-violation hazard of open size.

**My reply.**
- The steelman's escape needs negative-norm states at the cutoff to be harmless.
- In this framework the cutoff is where records form and where AX:60-61 demands probability distributions.
- That is the one place lattice QCD's tolerance does not transfer.

---

## What would change my mind

- **NT-1 (chiral-measure RP; FIXED readings in `next/NT1/PREREG.md:11-14`).**
  - **CHI-RP-PASS-at-power, with the vector-like witness negative on the same pools:** the chiral measure's phase choice repairs RP. I would reopen route 1, and D2 becomes a defensible two-price package (infinite fibre plus non-rational kernel, without Π-W). It would still need a 4D non-abelian check.
  - **CHI-RP-FAIL:** this confirms "decline D2".
  - **OPEN ("measure not built"):** no change.
- **NT-2 (3D plaquette-bound RP): low weight for the decisions.**
  - If the hard bound comes out negative in 3D, it is repairable by the triangle / g⋆g̃ weight (proved above). NT-2's own PREREG:116 says the same.
  - It would matter only if someone showed that **no** admissible positive-type weight exists in 3D/4D, which contradicts the construction above.
- **NT-3 (X2 exact diagonalisation; FIXED readings TG1-SYMMETRIC / TG1-BROKEN / OPEN).**
  - **TG1-SYMMETRIC:** a modest upgrade. X2 deserves the collaborator ask, and later compute if gate 2 passes. Clusters cannot prove 4D SMG.
  - **TG1-BROKEN:** X2 is in GPR territory, and D4 should not fund X2. The slab becomes the only Hamiltonian chirality candidate, and the D3 case for set C loses its chirality-specific asset.
- **The torus triangle-weight run** (§Checks) came out negative. Had it come out PSD, I would have reopened "the failure is the hard weight's" and weakened my D2 reasoning to scope.
- **Outside results.**
  - An RP proof for gauged overlap in infinite volume or 4D non-abelian would revive route 1.
  - A Golterman–Shamir statement that their 2025 theorem covers X2's filtered model would kill X2. If they say it also covers the slab (F4-L2), I would advise Jon to record chirality as unrealized, conditional on (I), rather than pay D2 and Π-W.
  - A number-free counting rule for set-C speeds would make set C dominate outright.

---

## One concrete next action

**Send Golterman and Shamir a two-page, pre-registered X2 packet.** This is Jon's call, since it is a message on his behalf. It should contain:
- the Hamiltonian (X2:55-70);
- the exact light-corner decoupling and its filter zeros;
- K1's mean-field condensation ratios;
- F4-L2's "a working wall ⇒ protected zero".

Ask exactly two questions:
1. Does arXiv:2505.20436's conditional theorem apply to X2 as written, and if not, which hypothesis fails?
2. What single finite-volume diagnostic would you accept as deciding whether X2's mirror zeros are kinematical?

**Why this action.**
- It is cheap and has the highest information per unit cost.
- It decides whether route 2 is worth any compute (D4).
- It decides whether set C keeps its one chirality-specific asset (D3).
- If the answer to question 1 is "yes, it applies", it moves the program to recording chirality as conditional on (I).
- Run gate 2 (sign-freeness) before sending, so the packet can say whether the model is QMC-ready.

---

## Checks

- `scripts/corner_orbits.out`: Z³ orbits (1, 3, 3, 1) give 3 light corners; Z⁴ orbits (1, 4, 6, 4, 1) never give 3. Corner chirality = (−1)^hw, the standard product-of-cosines formula, not re-derived numerically.
- `scripts/pg_weight_rp.out`: the hard weight (δ = 0.6) at Lx = 1–5 gives −2.2e-1, +1.4e-3, **−8.95e-3** (matching K2c), +3.3e-7, −3.9e-4. The triangle weight with the same support is PSD at every Lx.
- `scripts/torus_tri/V2_torus_Lt12_wgsearch_tri.out`: K2c's search code (copied unchanged), W-matched torus, Lt = 12, seed 4412, triangle weight. Result: O λ_min −1.4335e-4 (min/max −6.16e-6; E 7.7e-11; certified negative); W +4.5e-13 (PSD); PG −4.2e-15 (PSD within error). Max bulk plaquette 0.5475 (limit 0.55). 803 s, 135 MB peak. Pool file `pool_K2c_wgsearch_tri_O_torus_Lt12_seed4412.npz`. Same-family run, not refereed. Scope: 2D U(1) vector-like proxy, Lx = 2, β_g = 0, M = 1, m = 0.05.
