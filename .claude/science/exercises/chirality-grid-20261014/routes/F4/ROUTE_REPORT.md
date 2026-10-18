# F4 route report: boundary / defect / extra coordinate (anomaly inflow)

**Agent and timing:** Claude Opus 5.5 route agent, 13:19–14:10Z on 2026-10-14. It is the same model family as the supervisor and the other route agents, so it is not independent of them.

**Refresher read:**
- In full: `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- Skimmed: `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`.
- Read: the exercise SKILL steps 4 and 6 and the proof-search governance file, both from origin/main.
- Packet files read: WALL.md, ASSUMPTIONS.md, APPROACH_REGISTRY.md and step0/PRIOR_ART.md.
- Read at the cited lines: `docs/SPIN10_…_2026-09-14.md` §§1–9.

**Deliberately not read:** OUTSIDE_VIEW.md and any other route folder, to keep this route independent.

**Folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/routes/F4/`. It contains:
- `TEST_PREREG.md`: the readings, each fixed before its run;
- `scripts/`: every script, with its output beside it.

**Labels:**
- **proved**: an exact argument, given here or cited.
- **checked**: a finite numerical run in this folder.
- **suggested**: an argument that has not been checked.
- **reading**: an interpretation.
- **comparator**: a supplied model used only for comparison.

## Plain summary

Putting our world on the edge of a thicker qubit slab does make one-handed particles. The trouble is always the mirror partner on the far edge, together with the forces that reach it. This route found four things.

1. **The geometry alone can remove the mirror (checked).** If the slab's far side is glued back onto our own world, the slab has only one edge. The gluing must use a mirror-reversing half-turn of a closed world, and must pair each place with a far-away place. Done this way, the free slab carries exactly one handed particle and no mirror, at a cost of only a few layers per site.
2. **The forces then break it (suggested, with one scaling checked).** The force fields must either connect the glued places, which makes the forces see a mirror-symmetric world again, or be stretched across the universe, which makes the slab's own matter penalize ordinary magnetic and electric fields at Planck strength. The same dichotomy kills every no-interaction variant of the slab idea: smoothed forces ("fluffy mirrors"), a Higgs on the far edge, confining barriers, and growing record-depth ladders. Each fails unless the slab is at least about 10⁴⁶ layers deep, or unless world-sized nonlocal couplings are accepted.
3. **The only local version needs interactions (proved skeleton).** The far edge must be gapped by interactions that keep the symmetry. Any such success must leave a protected "zero" in the far-edge propagator. That is exactly what a 2025–26 theorem by Golterman and Shamir conjectures cannot happen. The slab is therefore the cleanest place to settle that dispute, and the test is named below.
4. **What is new against the repo's prior art.** The repo's Spin(10) slab (SPIN10) already showed that freezing the far edge fails. What is new here:
   - the single-edge geometry;
   - the gauge-locality dichotomy with its numbers;
   - the forced-zero reduction.

## Prior art engaged (not repeated)

- **Staggered-mass walls in 3D are vector-like** (`PRIOR_ART.md:80`). This route never uses 3D walls; it uses a 4+1D bulk.
- **Record-time wall, partner at the end** (`:79`). This route's two-wall case (Route A) has the same partner. Route C removes the end by gluing.
- **Vortex strings carry only local handedness** (`:82`). Not used.
- **Spin(10) slab in the atomic limit** (`docs/SPIN10_…:190-221`, Feshbach bound `:225-243`, zeros `:134-164`, Golterman–Shamir guard `:373-378`).
  - Lemma L1 below generalizes its two projections to *every* momentum-independent far-wall self-energy.
  - Lemma L2 is new: it makes the zero forced and topological in a slab, which SPIN10 does not claim. SPIN10's atom zero is kinematical (`:153`).
- **DOMAIN_WALL_EDGE_CONTENT mismatch** (`PRIOR_ART.md:77`). This route does not try to derive the 16 from tastes. The 16-flavour index is supplied and named as a price.
- **LATTICE_HANDEDNESS exit 3** (branch, `…_2026-09-27.md:342`) says "the Lattice axiom supplies Z³ only". Here the extra coordinate is read as an internal ladder inside a coarse site, and that reading is itself a price.

## Lemmas

**L1. Local self-energies relocate the mirror; they never remove it.** [proved, elementary; checked by T-F4-1]

Setting:
- a finite-range Hermitian slab Hamiltonian H(k) on Z³ × {1..L};
- a far-wall self-energy Σ(ω) on finitely many layers that is independent of k, has any frequency dependence, and is Hermitian at ω = 0. Infinite eigenvalues are allowed and act as projections.

Argument:
- After removing the infinite directions, h(k) = H(k) + Σ(0) is a smooth Hermitian matrix field on T³ of finite dimension.
- In each U(1) charge sector, its zero-eigenvalue points (poles of G(0,k), i.e. gapless states) have total index 0 (Stokes on T³).
- So the near Weyl's index χ is always matched by a gapless index −χ somewhere.

Scope:
- This covers atomic freezing (SPIN10's whole-layer and mirror-slot cases), DMFT- or SYK-type local self-energies, and any on-site far term.
- Any working far-wall mechanism must therefore produce a self-energy that depends on k and is singular at the mirror node.

**L2. A successful far-wall gapping forces a non-kinematical zero.** [proved skeleton]

Setting:
- the slab with a finite-range Hamiltonian, translation invariant along Z³, with an on-site U(1) (any U(1) ⊂ G_SM);
- a unique ground state;
- a near-wall Weyl with index χ ≠ 0 in charge sector q;
- no other gapless states of charge q (far wall and bulk gapped).

Claim: for every finite-support interpolator set whose zero-frequency matrix G_q(0,k) is smooth and invertible away from isolated points or surfaces, G_q has zeros of total index −χ.

Proof skeleton:
1. G(0,k) is Hermitian at T = 0 by the Lehmann representation.
2. The negative-eigenvalue bundle of −G⁻¹ is smooth on T³ minus small balls, so the indices around the singular points sum to zero (Stokes).
3. Since the only pole is the near Weyl, some zero must carry −χ.
4. Enlarging the interpolator set cannot remove the zero, because a removed zero would need a new gapless pole, which is excluded.

Open steps:
- Luttinger surfaces instead of isolated points (handle by flux through enclosing surfaces);
- that the near Weyl shows up as a pole in the elementary near-wall field (true at weak near-wall coupling).

Consequences:
- Condition 4 of Golterman–Shamir's generalized no-go (arXiv:2505.20436 §III: "a complete set of interpolating fields exists so that R(p) has no zeros") must fail in any successful slab gapping.
- Hence: the slab works ⇔ their "zeros are kinematical" conjecture is false for that model (they state the conjecture in arXiv:2505.20436 and its consequence in arXiv:2603.15985).
- With interactions at any strength, the slab is therefore exactly the place where the two camps make opposite predictions:
  - SMG camp: a protected zero;
  - Golterman–Shamir camp: a massless composite of index −χ appears, and the result is vector-like.

**L3. Gauge-locality dichotomy for every inflow geometry without symmetric gapping.**

Setting: the world is the boundary of a 4D region W carrying a C2 ≠ 0 insulator; on-site gauge invariance is exact; there is a light gauge field on the world. Three cases cover the bulk gauge links.

- **(a) Dynamical, deconfined bulk links in a thin bulk (depth D).** [proved skeleton]
  - The light mode is constant along each fibre of W. It is a gauge field on the core M obtained by collapsing the fibres.
  - Each fibre's two boundary ends carry opposite chirality relative to M (Stokes along the fibre).
  - So the content is vector-like at gauge resolution. For the slab, M = world (near + far). For the folded slab, M = world/τ.
  - A thick bulk with deconfined links makes the photon 4+1D, giving Coulomb 1/r². That is excluded.
- **(b) Confining or Higgsed bulk links.** [suggested]
  - Moving a charged fermion through W costs a flux excitation.
  - Below that cost, the C2 band structure is gone, and each layer is a local 3D system, so NN applies.
  - Single-barrier toy: m_mirror ≲ (t/g)² m_γ²/M_Pl ≈ 10⁻⁶³ eV, against more than 10¹² eV needed (T-F4-2).
- **(c) Slaved bulk links** (gradient flow, harmonic extension, coarse-grained Wilson lines).
  - There are no bulk gauge degrees of freedom. But the bulk fermions are physical and have positive electric polarizability, so the bulk energy carries c ∫_W F_B² with c > 0.
  - This gives nonlocal photon terms:
    - flow: a mass-like plateau c/(2δt) for wavelengths shorter than √(Lδt);
    - harmonic extension into a deep bulk: a |k| kinetic term, i.e. Coulomb 1/r² beyond a few Planck lengths;
    - folded slab: a penalty of about c Φ²_strip/(2L) per site on the flux through world-sized strips.
  - The 1/L scaling is checked (T-F4-4b). The rest is suggested.
  - Euclidean domain-wall, Grabowska–Kaplan and Kaplan constructions avoid (c) with Pauli–Villars bulk subtraction. A unitary qubit Hamiltonian has no Pauli–Villars fields (reading).
- **Two-wall slab with Grabowska–Kaplan flow** (arXiv:1511.03649).
  - The mirror's Gauss-law charge is exact at every k, and its coupling is unsuppressed for k ≲ 1/ℓ_flow.
  - Required depth: L ≥ M_Pl/m_γ = 1.2 × 10⁴⁶ layers (light-cone recursion) or about 10⁹³ (diffusive flow) (T-F4-2, arithmetic checked).

**L4. A thin single-boundary bulk must pair distant places.** [proved, using Smith theory, cited from memory and unverified this session]

A thin W with connected boundary equal to the world is an I-bundle whose end-pairing τ is a free involution of the world. Every involution of R³ has a fixed point (Smith theory), and so does every finite-order lattice automorphism (by orbit averaging). Hence:
- the world must be compact, for example T³ with the glide (x, y, z) → (x + N/2, −y, z);
- τ moves some points by about half the world.

**Dimension remark.** [reading] Lower-dimensional boundary-gapping successes are not evidence for 3+1D:
- in Fidkowski–Kitaev 0+1D end modes, the induced interactions are relevant;
- in 3-4-5-0 (1+1D), they are marginal;
- at d_surface ≥ 2+1, the order-t⁴/g³ terms that the strong-coupling expansion generates are irrelevant.

Golterman–Shamir 2505 §V makes the same 2D/4D caution. Decisive tests therefore need surfaces of dimension 2+1 or higher.

## Routes

| Route | Family (object, mechanism, terminal obligation) | Premise dropped/changed | What you would have to believe | First artifact | Cost | What it would change if it worked |
|---|---|---|---|---|---|---|
| **A. Inflow slab, far wall gapped by interactions** | Z³ × ladder(L) per site; tuned 4+1D Wilson C2 = 1 insulator × 16 flavours per generation; G_SM ⊂ Spin(10) links shared across layers. Mechanism: inflow plus far-wall symmetric mass generation. Terminal obligation L_A: a symmetric, local far-wall interaction gaps the far wall (unique ground state) at intermediate coupling while the near 16 stays gapless. | A6 (no extra coordinate); A5 (free) at the far wall only; A2 (a site is a block of about 10³ qubits) | Far-wall symmetric mass generation exists with a *protected* zero (L2), i.e. Golterman–Shamir's kinematical-zero conjecture fails here | L1 and L2 (done); a pre-registered DQMC slab test (below) | Weeks of sign-free QMC for the 2+1D-surface version; months for the 3+1D 16 | The only local F4 construction: a full SM generation with no light mirrors, exact on-site gauge invariance, nearest-neighbour range, about 10³ qubits per site |
| **B. No-go for every F4 variant without interactions** | Any inflow geometry. Mechanism: Gauss law, collapse along fibres, positive polarizability. Terminal obligation: L3 | None (it is a no-go/price) | — | L3 plus T-F4-2 arithmetic (done) | Hours for the flow-plateau check (below) | Removes the flow/fluff, far-Higgs, layer-phase, record-depth ladder, folded-slab and disk variants under locality, so F4 reduces to A |
| **C. Folded slab (orientable twisted I-bundle, one connected boundary)** | T³ × [−L, L] / Φ, with Φ = (x + N/2, −y, z, −t) and spinor S = Γ2Γ4. Mechanism: topology (single edge) and evading NN by breaking one translation through the gluing. Terminal obligation: a gauge sector on W with no identification along fibres and no penalty from bulk polarization | A6; Lattice translation covariance and NN locality (one O(1) bond per site to the site τx half a world away); compact world | The owner accepts world-range nonlocal gluing **and** nonlocal photon terms, or a non-unitary bulk subtraction | T-F4-3 (PASS) and T-F4-4b (penalty ∝ 1/L), both done | Done | Shows that removing the mirror from the spectrum is cheap (2L layers per site). The wall in this family is gauging, not the spectrum |

### Theorem-strength gap test

**A, terminal lemma L_A.**
- L_A ⇒ T, given shared links, the anomaly-free 16 and three copies. The open steps are the gauge dynamics and whether the zero is harmless once gauged. A gapped far wall clusters exponentially, so its current response is analytic at q ≪ Δ and produces no ghost-like running (suggested). Golterman–Shamir (arXiv:2311.12790) argue the opposite, and this is unresolved.
- T ⇒ L_A. Any local chiral 16 can be stacked, as its conjugate, onto the far wall and paired with the mirror by symmetric bilinears.
- So L_A is **target-equivalent: blocked-equivalent.** The genuinely new mechanism over F1 (symmetric mass generation in 3D) has two parts:
  - mirrors are separated in real space rather than in momentum, so links cannot leak them (Eichten–Preskill);
  - L2 turns the existence question into a single observable: a protected zero, or a massless composite.

**B.** Weaker than the target: a no-go for a class of constructions. It is an exact price, namely that F4 without interactions requires world-range nonlocality or at least 10⁴⁶ layers.

**C.** By L3, the gauge obligation is equivalent to accepting nonlocality. It is priced, not open.

### Price in framework terms

**Route A** (per Z³ site, three generations):
- 3 × 16 × 4 × L fermion qubits (Jordan–Wigner) with L ≈ 4–6. At the tuned μ = 3, the near zero mode sits exactly on the boundary layer at k = 0 (layer centroid 1.0 in T-F4-1 and 6.0 in T-F4-3). That gives about 10³ qubits;
- plus the far-wall interaction sector: a Spin(10)-singlet quartic, or a Yukawa to a 10-vector rotor of about 4 qubits per generation;
- plus G_SM link registers, one set per Z³ link, shared across layers.

Supplied structure that is not derived:
- fermion statistics;
- the internal ladder (a reading of what a "site" is; it is not the parked M₄(C) of DEFERRED #4);
- the Wilson Γ-structure and the μ ∈ (2, 4) tuning;
- the 16-flavour index and the G_SM embedding;
- which end carries the far-wall term, i.e. which hand is light (a sign bit);
- the far-wall interaction itself.

Anomaly edge cases [reading; García-Etxebarria–Montero arXiv:1808.00009, Wang–Wen–Witten arXiv:1810.00844; not re-verified this session]:
- Per generation the 16 cancels the perturbative anomalies, the Witten SU(2) anomaly (4 doublets), and the Z₁₆ anomaly with Z₄^X (16 ≡ 0).
- Without ν_R and with Z₄^X kept, the anomaly is 15 ≢ 0 mod 16, so the far wall *cannot* be gapped symmetrically. The interaction must then break Z₄^X, or ν_R must exist.

There is no range price: everything is nearest-neighbour or inside a site.

**Route C:**
- a compact world with an orientation-reversing free involution;
- an O(1) bond pairing every site with one half a world away;
- y-translation broken by the gluing;
- slaved gauge connections built from world-length Wilson lines;
- even then, the photon penalty needs L of roughly 10⁸⁹ (suggested, from c ≈ 5×10⁻³ and the photon-mass scale).

**Owner decision touched.** The range question (`WALL.md:35`; `PRIOR_ART.md:232`). Inside F4:
- accepting world-range nonlocality is what buys chirality without interactions;
- keeping nearest-neighbour locality leaves only Route A.

### Cheapest decisive tests (pre-registrable)

**A.** A sign-free DQMC (Majorana QMC) of the 2+1D *surfaces* of a 3+1D topological-insulator slab, with interactions only on the far surface.
- Setup: surface content anomaly-free under the kept symmetry, e.g. 8 Dirac (16 Majorana) cones with a Slagle–You–Xu-type SO(4)/SU(4) interaction. Measure:
  - layer-resolved spectral weight;
  - the far-surface elementary G(0,k);
  - the far-surface composite (three-fermion) channel.
- Readings:
  - **PASS-SMG:** the far surface opens single-particle and composite gaps at finite U_c with no long-range order; the elementary G has a zero carrying the near cone's index; the near cones stay gapless (finite-size gap ∝ 1/L_x).
  - **FAIL-GS:** a gapless far-surface composite appears, or the near cones gap.
  - **FAIL-SSB:** a gap opens only together with long-range order.
  - **FAIL-RELOCATE:** gapless cones reappear one layer inward.
- This tests the mechanism one dimension below the target. It is the first dimension where the induced interactions are irrelevant.

**B.** A free slab with flow-slaved links.
- Measure the bulk ground-state energy ΔE(k)/|A_k|² against the boundary field's wavevector k.
- Readings: **PLATEAU** if it tends to a k-independent constant for 1/√(Lδt) ≪ k ≪ 1 (this would confirm L3(c) for the flow); **NO-PLATEAU** otherwise. Cost: hours.

**C.** Already run; see below.

## Tests run

All readings were fixed in `TEST_PREREG.md` before each run.

**T-F4-1** (`scripts/t_f4_1_slab_index.py`, outputs `t_f4_1_*`) — **LEMMA-CONSISTENT** (checked; an instrument check, forced by NN, as pre-registered).
- Free slab: near and far projected Chern numbers are −1 and +1, total 0.
- Far-layer Γ5 or Γ4 at λ ≥ 3: the mirror relocates to layer L−1 (centroid 3.0), still at zero energy.
- Random Hermitian far term: at λ = 0.3, a small pocket with total 0 inside ρ = 0.35. At λ = 3, the far layer becomes metallic, and its Fermi surface carries the index.
- Dispersive partner layer: the mirror gaps at k = 0, and the index moves to the partner's 7 corner doublers. Corner Chern numbers are (−1, +1, +1, −1, +1, −1, −1, +1), summing to 0.
- Flat on-site partner: it acquires an induced slow dispersion with nodes at the same 7 corners (min |E| 10⁻³–10⁻¹). This matches SPIN10 §7.

**T-F4-2** (arithmetic) — **PRICE-PROHIBITIVE** (checked).
- 1/m_γ = 1.97×10¹¹ m = 1.22×10⁴⁶ l_P.
- L_min is 1.2×10⁴⁶ (z = 1) and 0.6–1.5×10⁹³ (z = 2).
- Even 1 m gives 6×10³⁴ (z = 1).

**T-F4-3** (`scripts/t_f4_3_folded_slab.py`) — **PASS at the free level** (checked).

| | Unglued slab | Folded slab | One-Weyl reference |
|---|---|---|---|
| Zero modes at k = 0 | 4 | 2 | — |
| States with \|E\| < δ, N = 16, L = 4 | 76 | 38 | 38 |
| States with \|E\| < δ, N = 24, L = 6 | 76 | 38 | 38 |

- In the folded slab, every low-energy state sits on the single face (centroid > L−0.02), and none sits at the midplane.
- The y ↔ −y mixing of the boundary branch at k_y ≈ 1.18 falls by about 7× per layer (energy deviation 5×10⁻³ at L = 2 → 10⁻⁶ at L = 6).

*Bug note:* the 13:52Z run used a gluing bond twice the correct strength. That output is kept as `t_f4_3_output_doubled_gluing.txt`. The 14:00Z rerun at the correct strength gives the same verdict.

**T-F4-4** (`t_f4_4_gluing_flux.py`) — **SLOW** (checked).
- A holonomy step concentrated on the gluing bond costs 5.78×10⁻² per bond (π/2 step), independent of L for L = 2…8.
- Interpretation: this is a flux sheet in the bulk, i.e. a bulk response, not tunnelling. The doubled-bond run gave 0.207, also flat.

**T-F4-4b** (`t_f4_4b_spread.py`; a dated follow-up with its own reading) — **INVERSE-L** (checked).
- With the holonomy spread over the 2L−1 bonds of each fibre, ΔE·(2L−1) = 4.40, 4.49, 4.57 and 4.60 ×10⁻³ for L = 3, 4, 6 and 8 (within 5%).
- The concentrated version stays flat at 3.37×10⁻³.
- So the slaved-gauge penalty decays only as 1/L, never exponentially.

**Review status:** no referee has seen these results. Before any of them is used as a negative conclusion, the supervisor's other-vendor referee should check T-F4-3, T-F4-4b and lemmas L2/L3.

## Literature

Fetched and read this session (abstract or key sections only):
- Golterman–Shamir, arXiv:2505.20436 (theorem conditions §III), arXiv:2603.15985 and arXiv:2311.12790;
- Kaplan, PRL 132, 141603 (arXiv:2312.01494): disk geometry, flowed/EOM bulk field, no mirror, locality only for mR ≫ 1;
- Kaplan–Sen, PRL 132, 141604 (arXiv:2312.04012);
- Grabowska–Kaplan, PRL 116, 211602 (arXiv:1511.03649).

Cited from memory and unverified: Wang–Wen arXiv:1809.11171; García-Etxebarria–Montero; Wang–Wen–Witten; Gurarie PRB 83, 085426; Volovik's momentum-space topology; Smith theory; Fu–Nielsen's layer phase; Dvali–Shifman; Slagle–You–Xu PRB 91, 115121.

## What not to do

- Do not run 0+1D or 1+1D gapping toys as evidence for this route (dimension remark).
- Do not pursue flowed or "fluffy" mirrors, a far-wall Higgs, layer-phase barriers or a growing record-depth ladder as local constructions. L3 and T-F4-2 price each of them at L ≥ 10⁴⁶, or at world-range nonlocality.
- Do not re-freeze far-wall slots. L1 covers every momentum-independent version.
