lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-16T02:35Z

# gap-kflow-read-opus: literature reading on the reopened (K-flow) path

Queue row 1002 of `FINISH.md` (pinned commit 25fda615c). Literature reading only; no lemma is attacked here.
Started 2026-11-15T14:35Z.

## Plan (at most eight steps)

1. Read `parts/gap.md`, lead rule W2 and the (K-flow) definition (FINISH row 999); record the exact property a hit must have.
2. Inventory what the repository already holds on these topics (library, prior/, sa-index) so as not to repeat it.
3. Search: monotone quantities under RG flow (c-, a-, F-theorems; Zamolodchikov, Cardy, Komargodski-Schwimmer, Casini-Huerta, Jafferis-Klebanov-Pufu-Safdi; any rigorous/lattice form).
4. Search: entropy / relative-entropy monotones along block-spin or coarse-graining maps (data-processing, Gaudin/Gurau-type, Kadanoff, information-theoretic RG; rigorous forms).
5. Search: rigorous flows through an order-one coupling in models with a gap (2D/3D; e.g. Balaban, Brydges-Yau, Dimock, Bauerschmidt-Brydges-Slade, Bauerschmidt-Bodineau-Dagallier, multiscale log-Sobolev / Polchinski-flow, cluster expansions), and Casimir / free-energy-along-scales bounds.
6. For each hit: statement, rigor, model and coupling range, selectivity (false for a massless factor?), source with short quote. Tabulate.
7. Assess against (K-flow): which hits, if any, could feed the reopened path; what fails for a massless factor.
8. RESULT line.

## Step log

### Step 1 (done 14:45Z). What a hit must have

Sources read: `parts/gap.md` L1-136 (state of attack, obligations); FINISH row 999 with lead rule W2 (FINISH L1078-1079);
`library/gap-crux-exercise3-max.md` (row 998) 1.2 (L111-158), 6b (L515-527), 8.2-8.5 (L724-818).

Objects (row 998 1.2): Wilson SU(2) on a periodic 4-torus; F = log Z; f = inf F(n)/|n|; the Casimir free energy
D(a) = F(a^4) - f a^4 >= 0 of the symmetric torus of side a; m(B) = log(lambda_0/lambda_1) of the transfer operator on a
3-box B; S(k;B) the thermal sum. Along a trajectory (a_j, beta_j): D^+(L) = limsup_j D_j(L/a_j), z^-(L) = liminf_j
(L/a_j) m_j((L/a_j)^3). The wall (W): one physical size L with z^-(L) > 256 D_0 + 30. Theorem ZD-c (lane, unchecked):
(PHYS-SEED) iff (BDD-Delta) and (Z-UNB). Route RA / (CAS) = (CONTR)_theta: D^+(2L) <= theta D^+(L) whenever D^+(L) >=
eps_0 = 6.1e-4, between first passage and the seed size; base D^+ <= C l^4 from (TH).

(K-flow), lead rule W2: a statement that reads the first-passage data of Wilson SU(2) (K_j -> infinity at one fixed
small g) and is carried through the order-one band by a step that fails for compact U(1) at weak coupling, for the
free photon, for frozen Q_8 / 2T (even-sector tools), and for any product with a massless (no-seed) factor (Lemma PT).
Sup-over-tilt forms are false (Theorem D2) and forms uniform over plaquette coupling fields are false (Lemma SHEET).

So a literature hit is useful to the path only if it is (i) a statement about a quantity defined from UV data and
transported across scales, (ii) rigorous or rebuildable by hand (no computer-assisted step, GOAL.md), and (iii)
**selective**: false, or vacuous, when the theory contains a massless factor. The ideal hit is a monotone or contraction
statement for D (or for an equivalent quantity such as a relative entropy of block-spin laws or a finite-size free
energy) that holds only in a gapped model. Test for selectivity used below: does the statement hold verbatim for the
free massless scalar / free photon / a product with one? If yes, it is blind (cannot feed (W) by L1, L5 of row 998).

Note on the target the reading has to meet. For a free massless field in d = 4 on the symmetric torus of side a, D(a)
tends to a nonzero constant (the Casimir / zero-mode term; scale invariance), so any statement "D shrinks by theta < 1
per doubling" is selective by construction. The literature question is therefore whether any theorem gives a
*mechanism* for such a contraction from UV data, not whether contraction is selective.

### Step 2 (done 14:55Z). Repo search: what is already on record

`grep -rliE` over `library/` and `parts/` (pinned commit), counts of files per topic:

- **c-, a-, F-theorems:** never read from source in this lane. Mentions are RECALLED, GUIDE: `library/gap-compress-opus.md`
  L100, L276, L289 ("Monotonicity statements (data processing along the flow, chain rules, entropic c-, F- and
  a-theorems, area laws ...) hold for every group and stay non-strict at the U(1) photon fixed point; their strictness
  is the seed"); `library/gap-ymcons-opus.md` L439-440 (Komargodski-Schwimmer, Casini-Teste-Torroba, recalled);
  `library/gap-skeleton-max.md` L306 (2D c-theorem relates nothing at different s); `library/gap-form-exercise.md` L415
  (a-theorem "orders the two ends and does not exclude a free massless end"); `library/prior/gap-seed-lit.md` L57 ("No
  source in this pass established a lattice a-theorem or a step-scaling inequality that controls Phi(n)").
  **Appelquist-Cohen-Schmaltz (thermal free-energy count): 0 files. Effective central charge from the Casimir energy
  (c_eff(L)): 0 files in the gap lane.** These are the new ground for this row.
- **Data processing / relative entropy along coarse-graining:** `gap-compress-opus.md` 2.1 (L113-137): data processing
  along time and under any slice-wise block kernel is PROVED and group-blind; it bounds the seed from the wrong side.
  `gap-lit-transport.md` (row 915), `gap-lit-hcvac.md`. Not repeated here except for the RG-specific relative-entropy
  papers (Apenko; Beny-Osborne; Gaite-O'Connor), which no file reads.
- **Polchinski flow / multiscale Bakry-Emery / LSI (Bauerschmidt, Bodineau, Dagallier, Shenfeld):** 39 files;
  `gap-lit-bridge-lsi.md`, `gap-lit-transport.md` RESULT (row 915): "conditional tools for Gaussian-based field
  theories". Not repeated; cited in the table by reference only.
- **Goepfert-Mack 3D U(1) all couplings:** `gap-crux-lit-nonab.md` T5 (L135-152), `gap-lit-u1.md` L23-34 (abstract
  read, proof not read). Cited here only for its selectivity (row 7 of the table).
- **Step scaling / Schrodinger functional (Luscher-Weisz-Wolff, Sint-Vilaseca):** `gap-seed-lit.md` L59-61, L113;
  `gap-sepinput-read-opus.md` 4.3. Verdict there: perturbative plus numerical program. The LWW finite-volume coupling
  of the O(N) sigma model, which is literally L m(L), is not tied to the lane's z(L) anywhere; noted below.
- **Sharpness (Duminil-Copin-Tassion, Aizenman-Barsky-Fernandez):** 42 files (`gap-lit-ineq.md`, `gap-lit-marginal.md`).
- **Borgs-Kotecky finite-size, Luscher volume dependence, mirror TBA:** `gap-lit-casimir.md` (row on E0(2L) - 2^d E0(L)),
  RESULT L68: no general rigorous small-defect bound.
- **Large N, Gross-Neveu, Kupiainen, Patrascioiu-Seiler:** `gap-crux-lit-nonab.md`, `gap-crux-lit-cross.md`,
  `gap-crux-lit-2.md`, `gap-skeleton-max.md`.
- `gap-3dmix-read-opus.md` (row 992) RESULT: no volume-free mixing bound for 3D SU(2) outside strong coupling, finite
  groups or abelian U(1).

So the new search goes to: (a) the c/a/F theorems from source, with their selectivity checked; (b) finite-size
c-functions built from the Casimir energy (the 2D analogue of D) and whether they are monotone; (c) the thermal
free-energy count (ACS) and its status; (d) RG-specific relative-entropy monotones; (e) rigorous flows through an
order-one coupling with a gap that the lane has not filed (2D/3D, large N, hierarchical), only to classify
selectivity. Plan steps 3-5 are kept, in that order.
