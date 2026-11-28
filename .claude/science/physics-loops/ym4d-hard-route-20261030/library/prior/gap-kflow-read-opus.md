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

### Step 3 (done 15:10Z). Monotones under the RG flow: c-, a-, F-theorems and thermal counts

Read level: arXiv abstract pages (and the ar5iv text of ACS for its definitions and status). No full proof read in
this step. Quotes are short and verbatim from the abstract pages unless marked "paraphrase".

**H1. a-theorem, Komargodski-Schwimmer.** Z. Komargodski, A. Schwimmer, "On renormalization group flows in four
dimensions", JHEP 12 (2011) 099, arXiv:1107.3987. Statement: for a unitary 4D QFT flowing between two CFTs,
a_UV > a_IR. Quote: "Unitarity of the S-matrix results in a monotonically decreasing function that interpolates between
the Euler anomalies in the ultraviolet and the infrared, thereby establishing the a-theorem." Rigour: physics proof;
assumes the flow is between conformal fixed points, a local stress tensor and the dilaton effective action; not a
theorem in the sense of the lane. Model and range: any unitary 4D QFT; all couplings (it is a statement about the two
ends). **Selectivity: blind.** Pure SU(2) has a_UV = 3 a_V (three free vectors at the UV end, asymptotic freedom). An
IR end consisting of one or two free photons has a_IR = a_V or 2 a_V < a_UV, so it is allowed; a product of the gapped
theory with a free photon is a unitary flow with a_IR = a_V. The theorem orders the ends; it never forces a_IR = 0.
Agrees with the lane's recalled verdicts (`gap-form-exercise.md` L415, `gap-compress-opus.md` L276), now with the source.

**H2. Entropic a-theorem, Casini-Teste-Torroba.** H. Casini, E. Teste, G. Torroba, "Markov property of the CFT vacuum
and the a-theorem", Phys. Rev. Lett. 118 (2017) 261602, arXiv:1704.01870. Quote: "We use strong sub-additivity of
entanglement entropy, Lorentz invariance, and the Markov property of the vacuum state" (abstract; the remainder
paraphrased: proves a_UV >= a_IR and unifies the entropic c- and F-theorems). Rigour: physics proof; needs Lorentz
invariance (so a continuum, Poincare-invariant vacuum), the Markov property of a CFT vacuum on the null plane and
entanglement entropy regulated by mutual information. Model: any 4D QFT between CFT ends. **Selectivity: blind** for
the same reason as H1 (it is the same inequality). It also needs Lorentz invariance, which the lane does not have at
finite cutoff, and it is a property of one state (the vacuum on R^4), not of finite tori; it says nothing about D(L).

**H3. Thermal degree-of-freedom count, Appelquist-Cohen-Schmaltz (ACS).** T. Appelquist, A. G. Cohen, M. Schmaltz, "A
new constraint on strongly coupled field theories", Phys. Rev. D 60 (1999) 045003, arXiv:hep-th/9901109. Definitions
(ar5iv text, eqs. 2-4): f_IR = -lim_{T->0} (F/T^4)(90/pi^2), f_UV the same at T -> infinity, conjecture
f_IR <= f_UV. Status, quoted: "Although we have not proven this inequality, we have shown that it agrees with a large
number of known results." The paper itself says (Section 2, quoted by the fetch) "the inequality can be violated in
the presence of non-trivial UV fixed points, as we show in section 5.2"; it is proposed for asymptotically free
theories. **Why this is the closest hit to (K-flow) in kind:** it is a statement about a thermal free energy (the
4D analogue of the lane's D on T^3 x S^1 rather than on the symmetric T^4) and it is read from UV data (f_UV = free
count by asymptotic freedom). **Selectivity: blind.** For pure SU(2), f_UV = 2 x 3 = 6; one free photon gives f_IR = 2
<= 6. The inequality allows a Coulomb end. The gapped end f_IR = 0 makes it trivially true, so it carries no force
toward a gap. And it is a conjecture with a stated violation class.

**H4. Thermal C-function, Castro Neto-Fradkin.** A. H. Castro Neto, E. Fradkin, "The thermodynamics of quantum systems
and generalizations of Zamolodchikov's C-theorem", Nucl. Phys. B 400 (1993) 525-546, arXiv:cond-mat/9301009. A function
C(g, T) built from the free energy, monotone in T "in regimes where quantum fluctuations dominate" (paraphrase);
quoted: "In regimes in which the classical fluctuations are important the monotonic behavior is absent." Rigour:
heuristic, checked on a free massive scalar, the 1D quantum Ising chain and the 2D quantum O(3) sigma model. Relevance:
it is the only free-energy-along-scales monotone found, and its own authors record that monotonicity fails in
general. **Selectivity: blind where it holds** (a free massless scalar has C constant, which is allowed).

**H5. Finite-size effective central charge c(r) (2D, TBA).** c(r) := -(6r/pi) E_0(r)/m-scaled ground-state energy on a
circle of circumference R, r = mR (the 2D analogue of the lane's Casimir free energy along sizes). P. Dorey,
C. Dunning, R. Tateo, "New families of flows between two-dimensional conformal field theories", Nucl. Phys. B 578
(2000) 699-727, arXiv:hep-th/0001185: abstract (paraphrase) reports that the finite-volume effective central charge is
non-monotonic in the system size along these flows. These flows are between **non-unitary** minimal models. For unitary
theories I found no theorem that c(r) is monotone in r; the search summary of TBA sources states the c-theorem gives a
monotone c-tilde, "apart from the UV and IR points ... it is not clear if there is any connection with E0(r)" (search
digest, not verified at the source; flagged UNREAD). **Status: no theorem.** Monotonicity of the Casimir-energy
c-function is not known in general even in 2D unitary integrable models; in non-unitary ones it is false.
**Selectivity:** c(r) -> 0 as r -> infinity only in a gapped (massive) flow; c(r) -> c_IR > 0 for a massless flow. So a
statement "c(r) falls below a threshold" is selective, exactly as (CAS) is; but no source supplies a mechanism other
than the exact solution (TBA, which takes the massive S-matrix, i.e. the gap, as input).

**H6. Lattice monotones (spin chains, decimation).** J. I. Latorre, C. A. Lutken, E. Rico, G. Vidal, "Fine-grained
entanglement loss along renormalization group flows", arXiv:quant-ph/0404120 (search digest; heuristic link to the
c-theorem via block entropies of critical chains). T. Tamm, arXiv:0910.2097 (search digest): an entropy-per-site
monotone along real-space RG, provable "only for a certain class of real space lattice RG transformations, namely for
decimations", and invalid on hierarchical lattices. **Selectivity: blind** (data-processing type; equality or
non-strictness at a massless fixed point; cf. `gap-compress-opus.md` 2.1). Not read beyond search digests: UNREAD.

**Step 3 verdict.** Every RG monotone found (H1-H4, H6) orders the UV and IR ends by a count of degrees of freedom and
allows an IR end with a massless factor whose count is below the UV count; none is selective. The one family with
the right selectivity (H5, the finite-size c-function, the 2D analogue of D(L)) has no monotonicity theorem in the
unitary case, is false in non-unitary cases, and its only computations take the gap as input. No rigorous lattice
form of any of H1-H5 was found; H6 is decimation-only and blind.

### Step 4 (done 15:20Z). Entropy and relative-entropy monotones along coarse-graining

**Correction to H6 (step 3).** arXiv:0910.2097 is S. M. Apenko, not "Tamm"; the attribution in step 3 came from a
search digest and was wrong. The abstract page (read) gives the record below as H7. The "decimation only" sentence of
H6 is from the same search digest and is UNREAD at the source; treat it as unverified.

**H7. Apenko.** S. M. Apenko, "Information theory and renormalization group flows", Physica A 391 (2012) 62-77,
arXiv:0910.2097 (abstract read). Statement: the information lost in one Wilsonian step is a conditional entropy of the
fast variables; quoted: "Its positivity results in the monotonic decrease of the informational entropy under
renormalization", with the caveat that this "does not necessarily imply the irreversibility of the RG flow". Rigour:
an identity plus positivity (chain rule); exact for any coarse-graining kernel. **Selectivity: blind** (holds for
every measure; the free massless field satisfies it).

**H8. Gaite-O'Connor.** J. Gaite, D. O'Connor, "Field theory entropy, the H-theorem and the renormalization group",
Phys. Rev. D 54 (1996) 5163, arXiv:hep-th/9511090 (search digest of the abstract; abstract page not opened: UNREAD at
the source). Proposal (digest): Wilsonian flows "induce an increase in entropy", relative entropy "the natural quantity
which increases from one fixed point to another in more than two dimensions"; companion hep-th/9610040: it "ranks the
fixed points in decreasing order of criticality". Rigour: proposal, Gaussian and perturbative examples. **Selectivity:
blind** (it ranks fixed points; a massless end is a fixed point and is ranked, not excluded).

**H9. Cotler-Rezchikov.** J. Cotler, S. Rezchikov, "Renormalization group flow as optimal transport", Phys. Rev. D 108
(2023) 025003, arXiv:2202.11737 (abstract read). Polchinski's exact RG equation is the Wasserstein gradient flow of a
field-theoretic relative entropy; quoted: "A striking consequence is that a regularization of the relative entropy is
in fact an RG monotone." Rigour: formal (Gaussian reference, regularized; not a theorem for gauge fields; the
reference measure is not named on the abstract page). Relation to work on file: it is the same structure as the
Polchinski flow / multiscale Bakry-Emery tools of Bauerschmidt-Bodineau-Dagallier, which `gap-lit-transport.md` (row
915) and `gap-lit-bridge-lsi.md` already classify as "conditional tools for Gaussian-based field theories".
**Selectivity: blind.** Monotone decrease of a relative entropy along a gradient flow holds for every action the flow
is defined for, the free massless field included; the gap enters only through a convexity (Hessian lower bound) of the
renormalized potential along the whole flow, which is the (K-flow) input itself, not a consequence.

**H10. Casini-Teste-Torroba, relative entropy along the RG.** H. Casini, E. Teste, G. Torroba, "Relative entropy and the
RG flow", JHEP 03 (2017) 089, arXiv:1611.00016 (abstract read). The relative entropy between the vacuum of a CFT and
of its relevant perturbation, on a null Cauchy surface, equals a difference of entanglement entropies, and "this
difference has the positivity and monotonicity properties of relative entropy"; it gives "a simple alternative proof of
the c-theorem in d=2" and the decrease of the area-term coefficient for d > 2. Rigour: physics proof, Lorentz-invariant
continuum vacuum. **Selectivity: blind** (orders ends; area-term decrease holds along any flow, massless ends included).

**H11. Beny-Osborne.** C. Beny, T. J. Osborne, "Information geometric approach to the renormalisation group",
arXiv:1206.7004 (and 1402.4949, 1310.3188; search digests only, UNREAD at source). The RG as a family of quantum
channels; relative entropy (Kubo-Mori metric) measures which distinctions survive coarse-graining. **Selectivity:
blind** (data processing for channels).

**Step 4 verdict.** All entropy and relative-entropy monotones found are data-processing or chain-rule statements, or
gradient-flow identities; each holds for every measure and every coarse-graining kernel, so each is blind by L1/L5 of
row 998. This repeats, now with sources, the lane's verdict in `gap-compress-opus.md` 2.1 (L113-137, L276): "their
strictness is the seed". No source gives a strict (contractive) form with a constant that a massless factor violates.

### Step 5 (done 15:40Z). Rigorous flows through an order-one coupling in models with a gap; finite-size data along scales

Row 998 already lists the large-N crossings as I36 ("THM, published, recalled", "not re-read",
`gap-crux-exercise3-max.md` L221). This step reads their abstract pages, adds two hits not on file, and records the
selective step of each.

**H12. Kopper, large-N nonlinear sigma model.** Ch. Kopper, "Mass generation in the large N nonlinear sigma-model",
Commun. Math. Phys. 202 (1999) 89-126, arXiv:math-ph/9902020 (abstract read; `gap-precedent-lit.md` row 161 says it
was read in full there). Quoted: the model is "the two-dimensional Euclidean O(N) nonlinear sigma-Model with a suitable
ultraviolet cutoff"; "for a sufficiently large (but finite!) number N of field components the model is massive"; "The
proof is simpler than that of the corresponding result for the Gross-Neveu-Model." Rigour: THEOREM. Range: N large,
fixed UV cutoff (so it is the infrared problem; the UV is not removed). **Selective step:** the large-N saddle (gap
equation). In d = 2 the massless candidate is inconsistent at the saddle because the massless propagator integral
int d^2k / k^2 diverges logarithmically in the infrared; so the gap is forced by an infrared divergence of the
massless factor, with 1/N as a second small parameter controlling fluctuations across the band.

**H13. Kopper-Magnen-Rivasseau, large-N Gross-Neveu.** C. Kopper, J. Magnen, V. Rivasseau, "Mass generation in the
large N Gross-Neveu model", Commun. Math. Phys. 169 (1995) 121-180 (volume and pages from row 998 I36 and my recall;
not confirmed at the publisher in this run: the search found the IP Paris portal entry, which says it studies "the
infrared behaviour of the Euclidean Gross-Neveu-Model with discrete chiral symmetry", and arXiv:1910.07102, which
credits it with a mass gap via exponential decay of the two-point function using an auxiliary bosonic field and
convergent expansions at successive scales; both search digests). Rigour: THEOREM. Range: large N, d = 2. **Selective
step:** same as H12 (2D large-N gap equation; the massless fermion is inconsistent at the saddle).

**H14. Delgadino-Smith (2026, not on file).** M. G. Delgadino, S. A. Smith, "Mass generation for the two dimensional
O(N) Linear Sigma Model in the large N limit", arXiv:2601.19630 (27 Jan 2026; abstract read; no journal ref). Quoted:
"We show that in the large $N$ limit, correlations decay exponentially fast"; the mass "decays exponentially in the
inverse temperature"; marginals converge to "a massive Gaussian Free Field (GFF) on $\mathbb{R}^{2}$"; "our results
hold without restrictions on the coupling constants". Method (quoted): "the Feyel/Üstünel extension of Talagrand's
inequality with some classical tools in Euclidean Quantum Field Theory". Rigour: claimed theorem, in the N -> infinity
limit (not finite N). Range: all couplings, on R^2. **Selective step:** again the 2D large-N gap equation; a
transport (Talagrand) inequality is the vehicle, the 2D infrared divergence the reason.

**H15. Gawedzki-Kupiainen, hierarchical O(N).** K. Gawedzki, A. Kupiainen, "Continuum limit of the hierarchical O(N)
nonlinear sigma-model", Commun. Math. Phys. 106 (1986) 533-550 (Project Euclid record via search digest; full text not
read). Search digest of a later source (hep-lat/9505012) says the continuum limit was proved rigorously; the search
digest of math-ph/9902020's text says the hierarchical support for a mass gap is "rather self-consistent than rigorous"
(UNREAD at the source; do not quote further). Pordt-Reisz, Ann. IHP A 55 (1991) 545 revisits the RG iteration.
**Status for the lane: no published rigorous mass gap through the band for a hierarchical model at fixed N found.**

**H16. LWW finite-volume mass-gap coupling and its step-scaling function.** M. Luscher, P. Weisz, U. Wolff, "A numerical
method to compute the running coupling in asymptotically free theories", Nucl. Phys. B 359 (1991) 221 (recalled; cited
by the sources below). In the 2D O(N) model the running coupling is defined by the finite-volume mass gap,
gbar^2(L) = 2 L m(L)/(N-1) (recalled), and the step-scaling function sigma(u) = gbar^2(2L) at gbar^2(L) = u carries
the flow from the UV (u small, perturbative) through u of order one. U. Wolff, F. Knechtli, B. Leder, J. Balog,
"Cutoff effects in the O(N) sigma model at large N", PoS LAT2005 (2005) 253, arXiv:hep-lat/0509043 (abstract read):
"The computation of the step scaling function for the finite size mass-gap in the O(N) sigma model at large N is
reviewed"; "Practically exact nonperturbative results become available". J. Balog, A. Hegedus, "TBA equations for the
mass gap in the O(2r) non-linear sigma-models", arXiv:hep-th/0504186, and hep-th/0309009 (search digests): TBA
equations for L m(L) at all L for O(3), O(4), O(2r), solved numerically, matching three-loop perturbation theory at
small L; digest value sigma(2, u0) = 1.261208(1) at u0 = 1.0595. Rigour: numerical / integrability-based, not
theorems. **Why it matters for the lane:** the lane's z(L) = L m(L^3) (row 998 1.2) is the exact 4D analogue of the LWW
coupling (a finite-volume mass gap times the size), and (W) asks that its step-scaling flow cross a threshold. In 2D the
crossing is known only through integrability (the exact massive S-matrix, which presupposes the gap) or large N. This
is the closest structural precedent for (K-flow) and it carries no proof at fixed N. Not on file before this row
(`grep -E "Balog|Hegedus"`: 0 files).

**H17. Goepfert-Mack, 3D U(1) Villain, all couplings (on file).** CMP 82 (1982) 545-606; `gap-crux-lit-nonab.md` T5,
`gap-lit-u1.md` L23-34. Search digest of the abstract: a rigorous block-spin calculation; the continuum limit is a free
scalar of mass m_D, asymptotically equal to the mass gap. Rigour: THEOREM, every beta > 0. **Selective step:** Debye
screening in the 3D monopole (instanton) Coulomb gas; the would-be massless photon is unstable because 3D monopoles are
point-like and their plasma screens at every density. In 4D, monopoles are loops, and at weak coupling U(1) has a
massless phase (Guth; Frohlich-Spencer), so the mechanism is dimension-specific and gives nothing for SU(2) in 4D.
Chatterjee, arXiv:2602.00436 (on file): 3D Wilson, groups with a central U(1), Wilson-loop bound
n exp{-c (1+n beta)^(-1) T log(R+1)} (abstract read); no mass gap claimed.

**Finite-size free energy along scales.** No new hit beyond `gap-lit-casimir.md` (Borgs-Kotecky, Luscher volume
dependence, mirror TBA; RESULT L68: no general rigorous small-defect bound). Every rigorous finite-size statement found
runs from the gap to a small size defect (gap -> D(L) exponentially small), the converse direction to (W).

**Step 5 verdict.** Every rigorous order-one crossing with a gap found uses either (i) a second small parameter (1/N:
H12-H14) or (ii) a dimension-specific infrared instability of the massless candidate (the 2D logarithmic divergence at
the large-N saddle: H12-H14; Debye screening of point monopoles in 3D: H17). In 4D a free photon factor is infrared
stable, so neither selective step is available for SU(2) at N = 2; the step-scaling precedent (H16) is numerical or
integrability-based.

**H18 (on file, for completeness).** M. Unsal, L. G. Yaffe, "Center-stabilized Yang-Mills theory: confinement and large
N volume independence", Phys. Rev. D 78 (2008) 065035, arXiv:0803.0344 (abstract read; 10 lane files already cite
Unsal or adiabatic continuity, e.g. `gap-ac-lat.md`, `gap-skeleton-max.md`). Quoted: on R^3 x S^1 at small L "the
deformed Yang-Mills theory has a mass gap and exhibits linear confinement"; continuity to large L rests on "there are
no order parameters which distinguish the small and large radius regimes". Rigour: semiclassical; continuity argued,
not proved. Selective step at small L: 3D monopole-instanton Debye screening (as H17), in a deformed theory.

### Step 6 (done 15:50Z). Table of hits

"Sel." = selective (false, or not available, for a theory with a massless factor). "Read" = what was read in this
row: abs = arXiv or publisher abstract page; digest = search-engine digest only (UNREAD at the source).

| # | Statement (short) | Rigour | Model, coupling range | Sel. | Source, read level |
|---|---|---|---|---|---|
| H1 | a_UV > a_IR (Euler anomaly), via dilaton 2->2 unitarity | physics proof | unitary 4D QFT between CFTs; ends only | no: 1 photon has a_IR = a_V < a_UV = 3 a_V for SU(2) | Komargodski-Schwimmer, JHEP 12 (2011) 099, 1107.3987; abs |
| H2 | a_UV >= a_IR from SSA + Markov property of null-plane vacuum | physics proof | 4D, needs Lorentz invariance | no (same inequality) | Casini-Teste-Torroba, PRL 118 (2017) 261602, 1704.01870; abs |
| H3 | f_IR <= f_UV, f = -(90/pi^2) lim F/T^4 | conjecture; stated violation with nontrivial UV fixed point | asymptotically free 4D | no: f_UV = 6, 1 photon f_IR = 2 | Appelquist-Cohen-Schmaltz, PRD 60 (1999) 045003, hep-th/9901109; abs + ar5iv eqs 2-4 |
| H4 | thermal C(g,T) from free energy monotone in T where quantum fluctuations dominate; "absent" otherwise | heuristic, examples | any d | no | Castro Neto-Fradkin, NPB 400 (1993) 525, cond-mat/9301009; abs |
| H5 | finite-size c_eff(r) from Casimir energy on a circle | no theorem; non-monotone in non-unitary flows | 2D integrable | yes in kind (-> 0 iff massive), but no mechanism | Dorey-Dunning-Tateo, NPB 578 (2000) 699, hep-th/0001185; abs |
| H6 | block-entropy loss along RG (spin chains) | heuristic | 1D lattice | no | Latorre-Lutken-Rico-Vidal, quant-ph/0404120; digest |
| H7 | informational entropy decreases per Wilsonian step (chain rule) | exact identity | any coarse-graining | no | Apenko, Physica A 391 (2012) 62, 0910.2097; abs |
| H8 | relative entropy ranks fixed points (H-theorem proposal) | proposal | d > 2, Gaussian/perturbative | no | Gaite-O'Connor, PRD 54 (1996) 5163, hep-th/9511090; digest |
| H9 | Polchinski ERG = W2 gradient flow of a relative entropy; regularized relative entropy is an RG monotone | formal | scalar fields, Gaussian reference | no | Cotler-Rezchikov, PRD 108 (2023) 025003, 2202.11737; abs |
| H10 | relative entropy CFT vs perturbed CFT on null surface: c-theorem (2D), area-term decrease (d>2) | physics proof | Lorentz-invariant continuum | no | Casini-Teste-Torroba, JHEP 03 (2017) 089, 1611.00016; abs |
| H11 | RG as quantum channels; relative entropy distinguishability | framework | general | no | Beny-Osborne, 1206.7004; digest |
| H12 | large finite N 2D O(N) sigma model is massive | THEOREM | 2D, fixed UV cutoff, N large | yes, via 1/N and the 2D IR divergence | Kopper, CMP 202 (1999) 89, math-ph/9902020; abs (full read on file) |
| H13 | large-N 2D Gross-Neveu mass generation | THEOREM | 2D, N large | yes, same mechanism | Kopper-Magnen-Rivasseau, CMP 169 (1995) 121 (vol./pp. not confirmed here); digest |
| H14 | N -> infinity 2D linear O(N): exponential decay, massive GFF marginals, all couplings | claimed theorem (2026 preprint) | R^2, N = infinity limit | yes, same mechanism | Delgadino-Smith, 2601.19630; abs; not on file before |
| H15 | hierarchical O(N) continuum limit; gap support "self-consistent" | theorem (limit), gap not rigorous | hierarchical 2D | n/a | Gawedzki-Kupiainen, CMP 106 (1986) 533; digest |
| H16 | step-scaling of LWW coupling L m(L) through order one; TBA for L m(L) | numerical / integrability | 2D O(N), O(3), O(4), large N | yes in kind (this is the 2D (W)) | LWW NPB 359 (1991) 221 (recalled); Wolff et al. PoS LAT2005 253, hep-lat/0509043 abs; Balog-Hegedus hep-th/0504186, hep-th/0309009 digest; not on file before |
| H17 | 3D U(1) Villain: mass gap, confinement, every beta | THEOREM | 3D abelian | yes, via 3D monopole Debye screening (fails in 4D) | Goepfert-Mack, CMP 82 (1982) 545; on file; digest |
| H18 | deformed YM on R^3 x S^1: gap at small L; continuity argued | semiclassical | SU(N), small L | yes at small L (as H17) | Unsal-Yaffe, PRD 78 (2008) 065035, 0803.0344; abs; on file |

### Step 7 (done 16:00Z). Assessment against (K-flow)

1. **No hit is a (K-flow) tool.** None starts from first-passage data of a 4D gauge theory and carries a selective
   statement across the order-one band. ESTABLISHED for the sources listed, at the read levels listed; a search that
   finds nothing does not show that no such statement exists.
2. **Counting monotones (H1-H4, H10) are blind, and the reason is quantitative.** They order the two ends by a count of
   degrees of freedom. For pure SU(2) the UV count is three free vectors (a_UV = 3 a_V, f_UV = 6), so an IR end with
   one or two massless vectors satisfies every one of them; and the product of a gapped theory with a free photon is a
   unitary flow that satisfies them. They are therefore never strict in the direction (W) needs. This confirms, with
   sources, the lane's recalled verdicts (`gap-compress-opus.md` L276, `gap-form-exercise.md` L415).
3. **Data-processing and gradient-flow monotones (H6-H9, H11) are blind** for every measure and kernel. Their strict
   forms are the seed (`gap-compress-opus.md`), and the convexity input of H9-type flows is the (K-flow) input itself.
4. **The only hits with the right selectivity in kind are the finite-size ones (H5, H16).** They are the 2D analogues of
   the lane's objects: c_eff(r) is the 2D Casimir free energy along sizes (the analogue of D(L)), and the LWW coupling
   L m(L) is the analogue of z(L) = L m(L^3). In 2D the step-scaling flow of L m(L) through order one is known only
   numerically or from integrability (TBA built on the exact massive S-matrix, which presupposes the gap), and the
   Casimir c-function is non-monotone in non-unitary flows (H5), so monotonicity of a Casimir c-function is not a
   structural law. No source proves, for any fixed-N asymptotically free model, the 2D analogue of (CAS) or (W).
5. **Every rigorous crossing with a gap (H12-H14, H17) has a selective step that 4D SU(2) lacks:** a second small
   parameter (1/N), or an infrared instability of the massless candidate specific to low dimension (the logarithmic
   divergence of int d^2k/k^2 at the 2D large-N saddle; Debye screening of point monopoles in 3D). A free photon in 4D
   is infrared stable (massless phase of 4D U(1), on file: `gap-lit-u1.md`), so neither selective step transfers.
6. **Consequence for the reopened path (ARGUED, a guide, not a proof).** The fixed-N 2D O(N >= 3) sigma model is the
   nearest solvable-looking test bed with the lane's structure: asymptotically free, gap expected, first-passage data
   perturbative (Balog-Hegedus match three-loop perturbation theory at small L), and a massless comparison case (2D O(2)
   in its Kosterlitz-Thouless phase, rigorous by Frohlich-Spencer, on file). Its rigorous mass gap at fixed N is, to my
   knowledge, open (RECALLED, not re-checked in this run; Patrascioiu-Seiler dissent is on file in
   `gap-crux-lit-2.md`, `gap-crux-lit-cross.md`). Proposal for the fact-test table of lead rule W2 (unproved): a
   (K-flow) tool whose transport step uses no four-dimensional and no gauge-specific input would, read in 2D, prove the
   O(N >= 3) gap at fixed N; so a candidate step should be asked which 4D-gauge fact it uses, and a step that uses none
   should be treated as suspect. This is a test of plausibility, not a theorem-grade test (it binds nothing logically).
7. **What stays open.** The wall (W) and every form of it on record ((CAS), (BDD-Delta) with (Z-UNB), (U1)/(U2)); no
   literature statement was found that supplies or prices them more exactly. Not read at the source in this row: H6,
   H8, H11, H13 (volume and pages), H15, the TBA papers of H16 and H17 (search digests only); the full texts of all hits
   (abstract level only, except the ar5iv definitions of H3).

## Provenance

Claude Opus 5.5 high, Mac mini worker (run of queue row 1002), commit 25fda615c. Literature reading only: no numeric
run, no download to disk (abstract pages read with the web fetch tool; nothing under /tmp), no lemma attacked, no
other file edited. Checked by no one. Times from `date -u`: start 14:35Z, steps 1-7 14:45Z-16:00Z.

RESULT: Row 1002 (literature reading on the (K-flow) path, 18 hits, abstract level): no published statement, rigorous or not, carries ultraviolet or first-passage data of a 4D gauge theory across the order-one band to a selective infrared conclusion. The c-, a-, F- and thermal (ACS) monotones and all relative-entropy or data-processing monotones (Komargodski-Schwimmer, Casini-Teste-Torroba x2, Appelquist-Cohen-Schmaltz, Castro Neto-Fradkin, Apenko, Gaite-O'Connor, Cotler-Rezchikov, Beny-Osborne) are blind: for SU(2), a_UV = 3 a_V and f_UV = 6 allow a free-photon end. The only hits with the right selectivity in kind are the 2D finite-size ones, the Casimir c-function (non-monotone in non-unitary flows, Dorey-Dunning-Tateo) and the Luscher-Weisz-Wolff step scaling of L m(L) (numerical or TBA only; the 2D analogue of z(L) and (W)). Every rigorous crossing with a gap (Kopper, Kopper-Magnen-Rivasseau, Delgadino-Smith 2026 at large N in 2D; Goepfert-Mack 3D U(1)) uses 1/N or a low-dimensional infrared instability that a 4D photon lacks. Proposed (unproved) plausibility test: a (K-flow) step with no 4D or gauge-specific input would prove the open fixed-N 2D O(N >= 3) gap. (W), (CAS) and every form on record stay open; seven sources (H6, H8, H11, H13, H15, the TBA papers of H16, H17) were read only through search digests.
