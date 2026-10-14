# Chirality on the grid: exercise report (2026-10-14)

Jon's request: "run the exercise on chirality and the grid … what new approaches or combined disparate approaches could crack this open?"

**Provenance.**
- Supervisor: Claude Opus 5.5.
- Agents: 18 Opus 5.5 agents at xhigh — step 0, literature, a blind check, six routes, three combinations, three kill agents, and the K2b/K2c tests. All are the same model family, so they are **not independent of each other**.
- Other-vendor referee: codex gpt-5.6-sol at xhigh. It refereed F2-R and K2 here, and TW-1/2/3 in the gravity packet.

**Labels.** **proved** (with path) / **checked** (finite or numerical test) / **suggested** / **reading**.

**Where things are.** Details live in `WALL.md`, `ASSUMPTIONS.md`, `ROUTES.md` (all tables, kill verdicts and referee records), `APPROACH_REGISTRY.md`, `OUTSIDE_VIEW.md`, `step0/`, `routes/`, `combos/`, `kills/`, `TESTS.md` and `scripts/`.

---

## 1. The wall, in plain words

Matter in nature is handed: the weak force acts only on left-handed electrons and quarks, and the right-handed versions carry different charges. A theorem (Nielsen–Ninomiya) says that if a grid's rules are local, the same everywhere, free (no interactions), and conserve charge in the usual way, then every handed particle comes with a mirror partner of the opposite hand and the same charges. So the grid makes a mirror-symmetric set of particles, and ours is not one.

Getting past the wall means a grid construction whose particles, below the grid's own energy, are exactly the observed handed ones. Any mirrors must be too heavy to have been seen, and the forces must act as observed. The problem has been open, in this form, for over 40 years.

## 2. What the exercise found

1. **The repo had already hit this wall from about twenty directions.** Every attempt sat inside the theorem's class: free, finite-range rules on one-qubit sites, with Hamiltonian or ticking time. None got through.
   - A one-line lemma explains why the mass-term attempts had to fail: no mass term that respects the gauge group can change the net hand count (F6, proved; the kill round narrowed how widely it applies).
2. **Six independent routes and three combinations all end at one of two frontier questions.** Both are open across the whole field, not just here:
   - **(I) Symmetric mass generation.** Can interactions give an anomaly-free set of mirror particles a mass without breaking the protecting symmetry, and without leaving a massless bound state behind? This is Golterman–Shamir's open "propagator zeros" dispute; X1 shows the same question as "lattice completeness". Symmetric gapping, discrete time, extra coordinates, dissipation and the framework's own three-generation package all lead here.
   - **(II) Lüscher's non-abelian measure locality, plus reflection positivity with forces present.** The Euclidean-time "overlap" route reduces to this.
3. **Hard prices on the dead ends, several checked:**
   - **Exact modified chirality from any finite rule is impossible.** Any rule built from finitely many neighbours and finitely many hidden helper fields has zero net chirality, regardless of site size (Lemma R, proved; **confirmed by the codex referee**). The three-way price list that came with it is not exhaustive (referee).
   - **A one-handed ticking rule hides its mirror at half a tick.** The mirror is upside-down with the same charges, so the vacuum radiates (F3-A, proved and checked; strengthened in the kill round).
   - **Dissipation and record sinks move the mirror's topological twist into the vacuum.** Every place it can sit fails observation (F5, proved and checked).
   - **No-interaction extra-coordinate slabs fail on the force fields.** They need a slab at least 10⁴⁶ layers deep, or couplings that span the world (F4-B).
   - **Mirrors that get mass from electroweak breaking are excluded by data:** S at 4–6σ, and Higgs production at least 9× too large (F6, checked).
4. **Constructive gains:**
   - **A framework-native three-generation package** (X2, checked).
     - The three generations are the walker's three left-handed cube corners; the other corners are mirrors made heavy by a cubic-invariant interaction.
     - The light corners are exactly decoupled from that interaction.
     - No anomaly forbids gapping the mirrors: the K1 kill test failed.
     - Its known danger is the 1993 Golterman–Petcher–Rivas symmetry-breaking phase, which mean-field shows is not removed by the filter (K1, wounded).
   - **A Euclidean-time package (set B)** that ties chirality to the gravity campaign's best gravity bill.
     - Its free real-time spectrum is clean: one light handed particle per hand, mirrors heavy and harmless. This was independently rebuilt by K2 and confirmed by the referee.
     - Its strain-protection fixes two gravity-campaign problems (no twins, no strain mass).
     - Its open issue is reflection positivity once forces are included. A counterexample was first found for one gauge measure (Fejér-weighted, open-time lattices; referee-confirmed). **K2c then found the same failure for the hard-cutoff measure the package actually uses**, on open-time lattices *and the torus*, once a masking effect is removed (**codex-confirmed** for the finite 2D U(1) proxy; not shown for 4D, non-abelian or chiral measures). If that holds, reflection positivity with forces fails for the overlap in this 2D proxy, and set B's real-time version needs a price (Π-W, or 5D fermions without Pauli–Villars fields).
5. **Framework facts settled along the way:**
   - one qubit per site is not the obstacle for slab or Euclidean constructions (X1, X3);
   - the right-handed neutrino is forced in every count;
   - **cross-lane theorem:** non-trivial quark mixing (CKM) forces a preferred strain direction in the flavour sector (X2-L8, proved; checked over 1120 subgroups). Its size goes back to the gravity/strain lane.

**Did the exercise crack the 40-year wall? No.** It converted the repo's diffuse wall into the field's two sharpest open questions, attached checked prices to every dead end, and produced two concrete framework-native candidates, each with a known decisive test.

## 3. Routes worth doing (at most three)

| # | Route | What you must believe | Cost | First test | What it would change |
|---|---|---|---|---|---|
| 1 | **Set-B Euclidean package**: overlap fermions plus Euclidean hypercubic time plus spatial-TT gravity (X3/F2-H) | Reflection positivity holds for the hard-cutoff gauge measure on the torus or in infinite time; Lüscher's non-abelian measure is local for the SM 16 | K2c done: gauged RP fails in the 2D proxy (codex-confirmed) → test whether a 2D anomaly-free *chiral* U(1) measure or a 4D slice behaves the same (a day) → if so, price Π-W / 5D-without-PV | the chiral-measure RP test | A single package carrying both chirality and the best gravity bill. Prices: Z⁴ time, and a non-rational kernel (with an infinite real-time fibre) |
| 2 | **Framework-native three-generation corner package** (X2) | The filtered mirror interaction has a symmetric strong-coupling phase, with no 10-vector condensation and no massless composite (GS condition 3 fails) | T-G1 exact diagonalisation (hours–day) → 2+1D QMC (weeks; needs compute) | T-G1: does the filter's overlap destroy the symmetric gapped phase? | Three handed generations from the grid's own corners; prices: 16 modes per site plus fermion number mod 4 |
| 3 | **Inflow slab with far-wall symmetric gapping** (F4-A, X1) | A slab's far wall can be gapped symmetrically, leaving a protected propagator zero | Sign-free 2+1D-surface QMC (weeks; needs compute or collaborators) | F4's DQMC test (pre-registered) | Exact on-site gauge invariance, nearest-neighbour range, no Eichten–Preskill leakage; price ~10³ qubits per site |

## 4. What not to do next

- **No more one-body or mass-term blocks aimed at net handedness.** The index lemma kills them.
- **Do not enlarge the site algebra to M₄(C) "for γ5".** Lemma R holds for any fibre size.
- **Do not pursue one-handed ticks, record or dissipative sinks, or heavy mirrors from electroweak breaking.** Each is priced out.
- **Do not treat 0+1D or 1+1D symmetric-gapping toys as 4D evidence.**
- **Do not use plain staggered twins as generations with the minimal splitting term.** The first-order clock hazard is ×4.7–17.8 on that branch (TW-2, refereed: branch-dependent).

## 5. The exact price

There is no single price for the whole wall. The family-level prices:
- **(a) Lemma R (referee-confirmed).** Exact Ginsparg–Wilson chirality needs a kernel outside the rational, finitely-generated class. That touches Admissibility's "one fixed nearest-neighbor rule" (AX:57), or the site's finiteness (AX:47).
- **(b) Interacting routes** need **16 to about 1000 fermion modes per site**. That is the parked site-size decision #4, whose wake condition has literally fired (K3).
- **(c) The set-B route** needs Euclidean hypercubic time (Z⁴): the gravity campaign's B1–B4 prices.

**Owner decisions surfaced by this exercise:**
1. **Matter per site** (#4): yes/no, and how much. Every surviving route needs more than one qubit's worth.
2. **Range:** whether a non-finitely-generated quasi-local kernel is acceptable (route 1).
3. **Time:** continuous (set C) or Euclidean hypercubic (set B) — the same choice as in the gravity campaign.
4. **Compute:** whether to fund the weeks-scale QMC tests for routes 2 and 3, or seek collaborators (Catterall, Hasenfratz, Fukaya/Onogi, Kikukawa).

## 6. Appendix

**Assumptions most likely wrong:**
- A5, "free carriers": the wall dissolves only with interactions.
- A3, "Hamiltonian or finite tick".
- A2's reading of "one qubit per site".

**Most expensive if wrong:**
- **A2:** forces #4.
- **A9:** time choice (set B vs set C) changes which routes exist.
- **A4:** range.

**PR or ledger candidates:**
- Lemma R as a price note, with the referee's corrections.
- F3-A as a bounded no-go/price for ticks.
- The index lemma (F6).
- The X2 flavour–strain theorem (X2-L8), routed to the gravity/strain lane.
- Corrections to T22 :19 and R2-4 :204.

**Literature worth translating:**
- Lüscher 1999/2000.
- Kikukawa–Usui (free overlap reflection positivity).
- Thorngren–Preskill–Fidkowski 2026 (symmetry disentanglers).
- Golterman–Shamir 2023–26.
- Catterall et al. on reduced Kähler–Dirac and SMG.
- Gioia–Thorngren 2025.
- Read 2017 (algebraic K-theory of local bands).
