# OUTSIDE VIEW: chiral fermions (Standard Model content) on a qubit lattice

Wall: put the SM's chiral gauge content (16 Weyl per generation including nu_R: left doublets, right singlets, hypercharges) on Z^3 with one qubit algebra M_2(C) per site and nearest-neighbour local rules (time continuous or discrete), with no unwanted mirror or doubler partners.

Agent: outside-view literature (exercise step 5). Compiled 2026-10-14, 12:59–13:45 UTC. Web search plus arXiv/journal pages. No repository edits.

Evidence labels (each row says which applies):
- **[V-abs]** checked against the arXiv/journal abstract or listing.
- **[V-text]** checked against the paper body (HTML full text).
- **[SEC]** bibliographic detail or claim checked only through a secondary citation.
- **[UNVERIFIED]** not checked here.
- **[INF]** my own inference, not a literature statement.
- **[CHK]** checked here by a small numerical script in `scripts/`.

---

## 0. Plain summary

1. **Doubling is a theorem about free, local, translation-invariant, Hermitian lattices with a conserved, quantized, on-site charge.** It applies to emergent fermions in qubit models too. In 3D Kitaev spin liquids, the emergent Majorana Weyl nodes still come in pairs.
2. **Every escape found in the literature drops at least one premise.** The premises dropped are: on-site-ness of the chiral symmetry (Ginsparg–Wilson/overlap, Gioia–Thorngren, symmetry disentanglers), ultralocality (overlap tails, quasi-local unitaries), free-ness (symmetric mass generation), a closed d-dimensional lattice (domain wall, single boundary), and Hermiticity or norm positivity (non-Hermitian models, Stacey/MPO norms).
3. **Discrete time does not help a strictly local free lattice.** [INF+CHK] A strictly local, translation-invariant one-particle unitary on Z^3 is an invertible Laurent-polynomial matrix. By Read's algebraic K-theory result (2017), its strong 3D winding W3 vanishes. By Bessho–Sato (2021), net Weyl chirality equals that winding at each quasienergy cut, so the net chirality is zero.
   - The published "single Floquet Weyl" constructions all use band-projected or normalized unitaries, which are quasi-local (exponential tails).
   - The D'Ariano–Perinotti BCC Weyl automaton has an opposite-chirality partner at quasienergy 0. I checked this numerically.
4. **The SM with nu_R passes every known anomaly test:**
   - perturbative gauge anomalies cancel;
   - the Witten SU(2) anomaly cancels (an even number of doublets);
   - the Dai–Freed Z_16 condition for a Z_4 symmetry needs exactly 16 Weyl per generation.

   The conjecture "anomaly-free ⇒ definable as a local lattice Hamiltonian with on-site gauge symmetry" (Wen 2013; Wang–Wen 2018/2020) has the following status:
   - Proven: 1+1D finite symmetries (Seifnashri–Shirley 2025/26), and abelian 4D in Euclidean Ginsparg–Wilson form (Lüscher 1999).
   - Exactly solved: the 1+1D "3450" model (Wang–Wen; Berkowitz–Cherman–Jacobson; Thorngren–Preskill–Fidkowski; Seifnashri).
   - Argued but not built: SM hypercharge in 3+1D (Thorngren–Preskill–Fidkowski 2026).
   - Caveat: there are anomaly-free 2D lattice symmetries that cannot be gauged or made on-site (Shirley–Zhang–Ji–Levin 2025).
   - Open: the full SU(3)×SU(2)×U(1) theory as a 3+1D Hamiltonian lattice model.
5. **Qubit-specific obstacles:**
   - Fidkowski–Xu (2023) forbids a shallow-circuit (on-site-like) chiral U(1) for a single Weyl with finite-dimensional sites.
   - The rigorous disentangler models use infinite-dimensional rotors.
   - Commuting-projector models with finite-dimensional sites cannot carry Hall response (Kapustin–Fidkowski).
   - Wang–Wen claim that 16 Weyl per generation (Spin(10) structure) is what allows a purely bosonic (qubit) lattice, while 15 per generation would need fundamental fermions. This is a proposal, not a proof.

---

## 1. Source table

### 1a. No-go theorems and their premises

| Source | What it shows | Premises | Status / evidence quality | Citation |
|---|---|---|---|---|
| Nielsen–Ninomiya I, II | Free lattice fermions have equal numbers of L and R Weyl species | Bilinear (free); local (smooth Bloch H(k) on BZ torus); translation invariant; Hermitian; exactly conserved, quantized charge with local density | Theorem. Premise list per standard summaries [SEC] | NPB 185, 20 (1981); NPB 193, 173 (1981) [SEC: cited in Gioia–Thorngren refs] |
| Nielsen–Ninomiya, Hamiltonian form | Same for a continuous-time lattice Hamiltonian | As above, with continuous time | Theorem | PLB 105, 219 (1981) [UNVERIFIED bib] |
| Friedan | New differential-geometric proof that fills a gap in N–N; phrased toward interacting generalization | Free | Theorem [V-abs] | CMP 85, 481 (1982) |
| Karsten–Smit | Doublers cancel the triangle anomaly of naive lattice fermions | Euclidean, free | Classic [SEC] | NPB 183, 103 (1981) |
| Ginsparg–Wilson | Remnant chiral relation Dγ5+γ5D = aDγ5D for RG-blocked fermions | Euclidean | Classic [SEC] | PRD 25, 2649 (1982) |
| Shamir (interacting no-go) | An interacting regular-lattice theory is vector-like if: local; relativistic continuum limit with no massless bosons; pole-free current vertex functions; unbroken compact symmetry. Proof applies N–N to the zero-frequency inverse propagator as an effective H | Interacting; relies on poles, not zeros | Theorem with stated assumptions [V-abs] | PRL 71, 2691 (1993), hep-lat/9306023; long form hep-lat/9307002 |
| Horváth; Bietenholz | No ultralocal (finite-range) Ginsparg–Wilson operator gives a single Dirac fermion; GW operators can only be exponentially local | Free, hypercubic symmetry (Horváth); general GW kernels (Bietenholz) | Theorems [V-abs] | hep-lat/9808002 (PRL 81, 4063 (1998) [UNVERIFIED bib]); hep-lat/9901005 |
| Fidkowski–Xu | In a fermionic lattice Hamiltonian with finite-dimensional on-site spaces, the U(1)_A of a single Weyl cannot be implemented by a shallow circuit. Z_2N needs N_f a multiple of 2N | Interacting allowed; quasi-local Q with e^{2πiQ}=1; finite-dim sites | Theorem [V-abs] | PRL 131, 196601 (2023), arXiv:2306.10105 |
| Gioia–Thorngren (Sec. III) | A free-fermion, quantized, exponentially local U(1) with no zero-energy band has a trivial gapped ground state, so no anomaly | Free | Theorem [V-text] | arXiv:2503.07708; PRL 136, 061601 (2026) [SEC] |
| Golterman–Shamir (generalized) | If symmetric-mass-generation (SMG) mirror "zeros" are kinematical and the one-particle effective H is local, N–N applies and the massless spectrum is vector-like. Includes a list of questions any SMG model must answer | Interacting, arbitrary strength | Conditional theorem plus conjecture (mirror zeros paired by bound states) [V-abs] | arXiv:2505.20436 (PRD 113, 014503 (2026) [SEC]); arXiv:2603.15985 (Lattice 2025) |
| Golterman–Shamir (zeros) | Propagator zeros act as ghosts once gauged: opposite-sign one-loop β contribution in 4D. Gauge invariance survives (even for anomalous targets) but unitarity is lost | Effective-Lagrangian analysis | Analysis [V-abs]; contested by Zeng–Xu–Lu–You 2405.05339 (current operator unbounded, response unphysical) [SEC] | arXiv:2311.12790 (journal [UNVERIFIED]) |
| Kapustin–Fidkowski | Local commuting-projector Hamiltonians with on-site U(1) have zero Hall conductance | Finite-range commuting projectors, finite-dim | Theorem [V-abs] | CMP 373, 763 (2019/20), arXiv:1810.07756 |
| Chen–Mazaheri–Seidel–Tang; Read | Strictly local (compactly supported Wannier / flat-band, finite-range) free bands carry only 1D windings along each axis, in all ten classes. No strong invariants | Strict finite range; free | Theorems (algebraic K-theory over Laurent polynomials in e^{±ik}) [V-abs] | arXiv:1311.4956 (2014); Read arXiv:1608.04696 (PRB 95, 115309 (2017) [UNVERIFIED bib]) |
| Mlodinow–Brun | A QCA built from the single-particle walk gives free-fermion QFT in 1D; "no construction with similar properties" in ≥2D | QCA from quantum walk; locality | Theorem [V-abs]. Evaded in PRA 103, 052203 (2021) via antisymmetrized distinguishable particles [V-abs] | PRA 102, 042211 (2020) |
| Gioia–Burkov–Hughes | A time-reversal-invariant 3+1D lattice cannot host one symmetry-protected Dirac node (anomaly matching) | Interacting allowed; EM U(1) a normal subgroup | Theorem [V-abs] | arXiv:2508.19329 |
| Sun, Xiao, Bzdušek, Zhang, Fan | N–N still holds on a 3D Floquet lattice (equal R/L). In the adiabatic limit a low-energy band can be one-handed | Floquet, local | Result [V-abs] | PRL 121, 196401 (2018) |

### 1b. Escapes (Euclidean and Hamiltonian lattice field theory)

| Source | What it shows | Premise dropped | Status / evidence quality | Citation |
|---|---|---|---|---|
| Wilson fermions | Doublers get O(1/a) mass | Chiral symmetry broken explicitly | Standard [UNVERIFIED bib] | Wilson, Erice 1975 lectures (1977) |
| Kogut–Susskind; staggered | Hamiltonian lattice gauge theory with continuous time; staggered fermions spread spinor components over sites | Keeps 2^{d/2}-fold tastes (doubling reduced, not removed) | Standard [V-abs for KS] | PRD 11, 395 (1975); Susskind PRD 16, 3031 (1977) [UNVERIFIED] |
| Sharatchandra–Thun–Weisz; Becher–Joos; van den Doel–Smit | Staggered = lattice Kähler–Dirac; reduced (one-component) staggered | Taste/flavour structure; not chiral | Classic [V-abs; vdD–S role in "reduced" only via citations, SEC] | NPB 192, 205 (1981); Z.Phys.C 15, 343 (1982); NPB 228, 122 (1983) |
| Catterall (staggered to Weyl) | Reduced staggered fermions plus site-parity Fidkowski–Kitaev-type Yukawas gap a subset of fermions. Discrete anomalies fix the count; free Weyl expected in the continuum | Free-ness (interactions); not on-site chiral | Proposal with 2D numerics [V-abs] | PRD 104, 014503 (2021), arXiv:2010.02290 |
| Catterall (reduced KD measure) | Reduced Kähler–Dirac fermions have a measure-phase ambiguity (analog of the chiral measure problem). A doubler-free action with the on-site symmetry exists. Mirrors plus anomaly-consistent Yukawas are conjectured to decouple; the minimal model gives a Pati–Salam light sector | Free-ness; uses Kähler–Dirac rather than Weyl | Conjecture [V-abs] | SciPost Phys. 16, 108 (2024), arXiv:2311.02487 |
| Kaplan domain wall | A (2n+1)-dimensional massive fermion with a mass step has chiral zero modes; anomaly flows into the bulk. Overall vector-like (the anti-wall holds the mirror) | Extra dimension; mirror separated in space | Established for vector theories [V-abs] | PLB 288, 342 (1992), hep-lat/9206013 |
| Narayanan–Neuberger; Neuberger | Infinitely many regulator fields / overlap gives chiral determinants; overlap Dirac operator; no doublers, no fine-tuning | Ultralocality; chiral symmetry modified | Established [V-abs] | PLB 302, 62 (1993); NPB 443, 305 (1995); PLB 417, 141 (1998) |
| Hernández–Jansen–Lüscher | The overlap operator is local with exponential tails for gauge fields smooth at the cutoff | Exponential (not strict) locality | Theorem under smoothness [V-abs] | NPB 552, 363 (1999) |
| Lüscher (exact lattice chiral symmetry) | GW implies an exact, gauge-field-dependent, not-on-site lattice chiral symmetry. Evades N–N because the symmetry is realized differently | On-site symmetry | Theorem [V-abs] | PLB 428, 342 (1998), hep-lat/9802011 |
| Lüscher (abelian) | Anomaly-free U(1) chiral gauge theories on the lattice: exact gauge invariance, nonperturbative, all topological sectors. "Mainly of theoretical interest" | Ultralocality, on-site | Theorem [V-abs] | NPB 549, 295 (1999), hep-lat/9811032 |
| Lüscher (non-abelian) | The non-abelian anomaly is a local topological field. Anomaly-free chiral gauge theories regularized to all orders of perturbation theory, any compact group | Same | All-orders proof; nonperturbative non-abelian not done [V-abs] | NPB 568, 162 (2000); JHEP 06 (2000) 028 |
| Kikukawa–Nakayama(–Suzuki); Kadoh–Kikukawa | SU(2)×U(1) cohomology solved. Gauge-invariant nonperturbative Glashow–Weinberg–Salam construction in SU(2) topological sectors with vanishing U(1) flux | Same | Partial nonperturbative non-abelian [V-abs; journals UNVERIFIED] | hep-lat/0005015; hep-lat/0111036; arXiv:0709.3658 |
| Eichten–Preskill → Golterman–Petcher–Rivas | Mirror decoupling by strong multi-fermion couplings. The EP model shows SSB or Dirac-like fermions everywhere; no undoubled Weyl | Free-ness | Early attempt failed (numerics plus strong/weak coupling) [V-abs] | EP NPB 268, 179 (1986) [SEC]; GPR NPB 395, 596 (1993) |
| Poppitz–Shang; Kikukawa | Review of GW mirror-decoupling difficulties. 345 mirrors failed to decouple; four-flavour axial model works at weak gauge coupling | Free-ness | Review + Monte Carlo [V-abs] | IJMPA 25, 2761 (2010); PTEP 2019 (arXiv:1710.11101) |
| Grabowska–Kaplan | Domain-wall fermions with the gauge field gradient-flowed into the bulk; mirrors couple via an exponentially soft form factor ("fluffy") | Locality of the gauge sector in the bulk | Proposal [V-abs]. Critiques: fluff carries a fermion-number anomaly (Okumura–Suzuki 1608.02217); infinite flow gives a nonlocal measure term (Ago–Kikukawa 1911.10925); superfluous conserved current, extra NG boson (Golterman–Shamir PRD 109, 114519 (2024)) [V-abs] | PRL 116, 211602 (2016) |
| Kaplan (single boundary) | Massive fermion on a (d+1)-dimensional disk with one connected boundary: chiral boundary fermion with no mirror. Local d-dimensional description iff perturbative anomalies cancel. Bulk gauge field fixed by the boundary value (e.g., gradient flow). Exponentially small cross-disk nonlocality is an open question | Closed d-dimensional lattice; needs d+1 dims | Proposal, Euclidean, no lattice gauge sector [V-text] | PRL 132, 141603 (2024), arXiv:2312.01494 |
| Kaplan–Sen | 2+1D Wilson Hamiltonian, continuous time, open boundaries: a single-chirality Weyl edge consistent with N–N | Boundary | Free-fermion result [V-abs] | PRL 132, 141604 (2024), arXiv:2312.04012 |
| Aoki–Fukaya–Kan | Spherical domain wall in a 3D lattice: Weyl on S^2. A monopole background induces an opposite-chirality centre mode | Boundary/curvature | Free numerics [V-abs] | arXiv:2402.09774; 2502.03045 |
| Wen (SO(10) lattice definition) | SO(10) chiral gauge theory (SM embedded) on a 3D spatial lattice with continuous time and finite-dim Hilbert space. Argues any anomaly-free chiral gauge theory is lattice-definable via the anomaly–SPT link | Free-ness (mirror SMG) | Argument/conjecture [V-abs] | CPL 30, 111101 (2013), arXiv:1305.1045 |
| Wang–Wen | 3450 as low-energy theory of a 1+1D local lattice with on-site U(1). SO(10)-GUT SM (16/gen) proposed on a 3+1D lattice of bosons/qubits; SU(5) (15/gen) on a fermion lattice | Free-ness | 1+1D: strong (numerics later); 3+1D: proposal [V-abs] | PRD 99, 111501 (2019); PRR 2, 023356 (2020) |
| You–BenTov–Xu | Interactions reduce a 4+1D TSC class so its 3+1D boundary gaps symmetrically only for multiples of 16 chiral fermions: a possible origin of 16n | Free-ness | Argument [V-abs] | arXiv:1402.4151 |
| Razamat–Tong; Tong | Continuum SMG via confinement without chiral symmetry breaking (SUSY, s-confinement). Gaps an SM generation without breaking EW symmetry; groups of 16 under mod-16 discrete anomaly | n/a (continuum) | Continuum arguments [V-abs] | PRX 11, 011063 (2021); JHEP 07 (2022) 001 |
| Wang–You review | SMG defined; numerics summarized; unifying framework | n/a | Review [V-abs] | Symmetry 14 (2022), arXiv:2204.14271 |
| SMG numerics, 1+1D | DMRG on 3450: mirror sector gaps (BKT) while the light chiral sector stays gapless | — | Numerical, strong for 1+1D [V-abs] | Zeng–Zhu–Wang–You arXiv:2202.12355 |
| SMG numerics, 2+1D | QMC: direct continuous transition from Dirac to symmetric gapped phase | — | Numerical, strong [V-abs] | Slagle–You–Xu PRB 91, 115121 (2015); He et al. PRB 94, 241111 (2016) |
| SMG numerics, 3D/4D four-fermion | 3D: direct second-order transition. 4D: narrow intermediate phase with bilinear condensate | — | Numerical; 4D direct SMG not established [V-abs] | Ayyar–Chandrasekharan PRD 91, 065035 (2015); PRD 93, 081701 (2016); JHEP 10 (2016) 058 |
| SMG numerics, 4D staggered Higgs–Yukawa | Massless symmetric, intermediate antiferromagnetic, and massive symmetric (SMG) phases. Critical lines meet at a possible multicritical point | — | Numerical, 2026 preprint [V-abs] | Butt–Catterall–Hartshaw–Hasenfratz arXiv:2608.18239 |
| SMG in 4D gauge theory | SU(3) with N_f=8 (staggered = Kähler–Dirac): strong-coupling chirally symmetric gapped phase, BKT-like transition. Continuum limit "suggested, needs confirmation" | — | Numerical, suggestive [V-abs] | Hasenfratz PRD 106, 014513 (2022); Hasenfratz–Witzel arXiv:2412.10322, 2511.22678; Hasenfratz–Xu 2604.02424 |
| Thorngren–Preskill–Fidkowski | Symmetry disentanglers (constant-depth circuits) make not-on-site symmetries on-site, then gauge. Rotor models for U(1)s with mixed anomalies in 1+1D and 3+1D; disentanglers exist when anomalies cancel. Exactly solvable 3450. SM U(1)_Y "argued": its step (iii) interface is "plausible but unproven". 3+1D Weyl Hamiltonian not yet built; rotors are infinite-dim | On-site-ness (then restored); keeps a strictly local H | Rigorous in parts; key 3+1D step conjectural [V-text] | arXiv:2601.04304; JHEP 07 (2026) 271 [SEC] |
| Seifnashri–Shirley | Every finite internal anomaly-free symmetry of a 1+1D lattice Hamiltonian becomes on-site after adding ancillas and conjugating by a finite-depth circuit | — | Theorem (1+1D, finite) [V-abs] | PRL 136, 216603 (2026), arXiv:2503.09717 |
| Shirley–Zhang–Ji–Levin | 2D lattice symmetries that are anomaly-free but neither gaugeable nor on-siteable; index in H^2(G, Q_+) (labels of 1D QCA) | — | Counterexamples to "anomaly-free ⇒ on-siteable" [V-abs] | arXiv:2507.21267 |
| Seifnashri | Exactly solvable 1+1D chiral lattice gauge theories (modified Villain); quadratic 34-50 Hamiltonian | Villain (integer-valued fields) | Exact [V-abs] | arXiv:2601.14359 |
| Berkowitz–Cherman–Jacobson | Exact lattice chiral symmetry in 2D via bosonization plus modified Villain: QED_2 and 3450; anomalies exact at finite spacing | Uses 2D bosonization (no 4D analog) | Exact, 2D only [V-abs] | arXiv:2310.17539 |
| Gioia–Thorngren | Cubic-lattice Hamiltonians: single Weyl with exact not-on-site, non-compact, unquantized chiral symmetry (a Hamiltonian GW analog; BdG form, fermion-number U(1) broken). Weyl doublet with on-site U(1) plus not-on-site U(1) generating the Onsager algebra, tied to the Witten anomaly. Hard to gauge | On-site-ness; compactness | Exact free models [V-text] | PRL 136, 061601 (2026) [SEC], arXiv:2503.07708 |
| Chatterjee–Pace–Shao | 1+1D staggered: two integer, individually gaugeable, conserved charges generate the Onsager algebra and match the chiral anomaly; force gaplessness | Commutativity of V and A charges | Exact [V-abs] | PRL 134, 021601 (2025) |
| Lew-Smith–Pace–Shao | The Onsager anomaly has order 2, but infinite order with lattice CPT | — | [V-abs] | arXiv:2606.12510 |
| Aoki–Kikukawa–Takemoto | 3+1D Kogut–Susskind: axial charge from shifts is not on-site and not quantized; commutes with H only in special U(1) backgrounds; anomaly seen numerically | — | [V-abs] | arXiv:2511.06198 |
| Fidkowski–Xu–Zhang | 3+1D non-invertible Z_N chiral symmetry on a rotor lattice (Villain U(1) gauge + scalar) | On-site; invertibility | [V-abs] | arXiv:2510.17969 |
| Lu–Seifnashri–Shao | Exact lattice U(1)_V × U(1)_A from bosons in 3+1D (compact boson + axion-like coupling); anomaly via theta shift | Fermions replaced by bosons | [V-abs]; local dimension not stated | PRD 114, 034518 (2026), arXiv:2604.06307 |
| Dharanikota–Fidkowski | Solvable 1+1D Dirac Hamiltonian with not-on-site V and A U(1)s (rotor plus fermionic Villain) | On-site | [V-abs] | arXiv:2608.02722 |
| Hamiltonian GW family | Overlap-based fermion Hamiltonian with Q5 commuting with H_F. Commuting chiral charge for overlap. Approximate GW Hamiltonian (nonlocal, ghosts). Order-k GW Hamiltonians (charge conserved, quantized only as k→∞). Single-Weyl BdG from minimal doubling (tuning needed) | Ultralocality, quantization | [V-abs] | Creutz–Horváth–Neuberger NPPS 106, 760 (2002); Hayata–Nakayama–Yamamoto PRD 108, 034511 (2023); Clancy 2312.08647; Singh 2505.20419; Misumi PRD 113, 074521 (2026) |

### 1c. Discrete time: QCA, quantum walks, Floquet

| Source | What it shows | Premises | Status / evidence quality | Citation |
|---|---|---|---|---|
| Gross–Nesme–Vogts–Werner (GNVW) | 1D QCA/walks are classified by an index (net information flow). Shifts are the nontrivial examples; trivial index means partitioned unitaries | 1D, strict locality | Theorem [V-abs] | CMP 310, 419 (2012), arXiv:0910.3675 |
| Rudner–Lindner–Berg–Levin | Driven 2D systems have chiral edges even when all Floquet Chern numbers are 0; new invariant | Floquet, free | Theorem [V-abs] | PRX 3, 031005 (2013) |
| Po–Fidkowski–Morimoto–Potter–Vishwanath | Interacting (MBL) bosonic chiral Floquet phases with no symmetry; edge index = pumped entropy | MBL, driven | [V-abs] | PRX 6, 041070 (2016) |
| Bialynicki-Birula | Local unitary automata reduce to Weyl in the continuum; cubic-lattice constraints noted | Linear, unitary, local | [V-abs] | PRD 49, 6920 (1994) |
| Meyer; Arrighi–Nesme–Forets | Dirac QCA/walk; higher-dimensional Dirac walk with O(ε²) convergence | Linear | [V-abs] | J.Stat.Phys. 85, 551 (1996); J.Phys.A 47, 465302 (2014) |
| D'Ariano–Perinotti | Weyl/Dirac automata from unitarity, locality, homogeneity, isotropy on a BCC lattice. Paper notes doubling for the massless Dirac automaton | Linear, strictly local | [V-text]; journal PRA 90, 062106 (2014) [UNVERIFIED]. [CHK] Weyl automaton A+ has U=+I nodes at k≡0 (χ=+1) and k=(√3π/2)(−1,−1,−1) (χ=−1), and U=−I nodes of opposite chirality: net 0 at each quasienergy | arXiv:1306.1934 |
| Bakircioglu–Arnault–Arrighi | QCA suffer doubling (1+1D; 3+1D Dirac walk has 7 extra neighbourhoods). Covering-map "flavouring" gives 2 or 8 flavours, not a single Weyl | Strict locality | [V-text] | arXiv:2505.07900 |
| Gupta–Short | Doublers and pseudo-doublers (quasienergy π) in Dirac walks; "lazy" walks remove most | Linear | [V-abs] | PRA 114, 012208 (2026) |
| Beenakker–Sánchez Férnan–Tworzydło | 2D: strictly finite-range two-band walks get one cone only via non-symmorphic symmetries that disorder breaks. Exponential tails allow one cone with on-site symmetries (uses Chen et al./Read) | Strict vs exponential locality | [V-text] | arXiv:2607.05112 |
| Bessho–Sato | Extended N–N for Floquet and non-Hermitian systems: net chirality = bulk winding. Dynamical systems can host unpaired chiral fermions | Bloch translation invariance; point gap | Theorem [V-text, partial] | PRL 127, 196404 (2021), arXiv:2006.04204 |
| Higashikawa–Nakagawa–Ueda | A Floquet unitary U(k): T^3→SU(2) with W3=1 gives a single Weyl and a Floquet chiral magnetic effect. Built from spin-selective pumps including half-step pumps; lower-band operator | Band-projected, quasi-local | [V-text]; journal [UNVERIFIED] | arXiv:1806.06868 |
| Fidkowski–Hastings | Free unitaries T^3→SU(N) with winding ν pump ν p+ip layers. For number-conserving unitaries the winding is quantized, so the unitary is not a finite-time quasi-local evolution. The pump has tails | Quasi-local | [V-text] | PRB 109, 235142 (2024), arXiv:2309.15903 |
| Haah–Fidkowski–Hastings; Shirley et al. | Nontrivial 3D QCA (three-fermion; chiral semion surfaces). Conjectured QCA group = Witt group | Bosonic, strictly local | Strong evidence plus conjecture [V-abs] | CMP 398, 469 (2023); PRX Quantum 3, 030326 (2022) |
| Iadecola–Sen–Sivertsen | Floquet quasienergy spectra map exactly onto discrete-time lattice fermions (SSH/Wilson–Dirac) in 1+1D and 2+1D | Free | [V-abs] | PRL 132, 136601 (2024); PRR 6, 013098 (2024); arXiv:2410.18226 |
| **This note** | A strictly local translation-invariant one-particle unitary on Z^3 is invertible over the Laurent ring, so W3 = 0 (Read 2017 K-theory; the AIII flat-band off-diagonal block is such a unitary). Hence (Bessho–Sato) net Weyl chirality is 0 at every quasienergy. The same holds for the one-particle sector of any U(1)-conserving strictly local QCA with an invariant product vacuum | Free / one-particle sector | **[INF]**, not found stated in the literature. [CHK] `scripts/w3_check.py`: random depth-9 coin+shift walk W3 = 0.107, 0.049, 0.021 at N = 48, 72, 112 (→0); e^{ikxσx}e^{ikyσy}e^{ikzσz} gives 0.0000; quasi-local normalized Wilson map (M=2) gives −0.998 | — |

### 1d. Non-Hermitian, open-system and norm-modifying escapes

| Source | What it shows | Premise dropped | Status / physical meaning | Citation |
|---|---|---|---|---|
| Chernodub | PT-symmetric non-Hermitian local lattice (1+1D) with unequal L/R and a robust 8-shaped cone; PT spontaneously broken (complex branches) | Hermiticity | Model; non-unitary evolution [V-abs] | J.Phys.A 50, 385001 (2017) |
| Bessho–Sato (non-Hermitian) | 3D point-gapped H(k): w3 = Σ Chern numbers of Re E=0 surfaces. Finite-range example. Predicts a non-Hermitian chiral magnetic skin effect | Hermiticity | Theorem [V-text]. [INF] the strict-locality K-theory obstruction does not apply, because a point-gapped Laurent H is not invertible over the Laurent ring | PRL 127, 196404 (2021) |
| Guo–Ma–Zhang; Ma–Zhang | One-sided (forward-difference) lattice derivative: no doublers, chiral symmetry kept, Hermiticity lost. Hypercubic symmetry broken, so non-renormalizability is cured by averaging | Hermiticity | Proposal and review [V-abs] | arXiv:2105.10977; 2411.09886 |
| Non-Hermitian doubling theorems | Doubling theorems extended to non-Hermitian 2D (Fermi points, exceptional points). An unpaired double Weyl point via band-ordering ambiguity | — | [SEC; authors UNVERIFIED] | arXiv:1912.02788; 1905.04338 |
| Lindbladian chirality | No lattice construction of an unpaired chiral fermion from Lindblad dynamics found. Operator–state map doubles the system (dissipative Majorana slides, 2026) | Unitarity | **Gap**; [UNVERIFIED] slides | — |
| Haegeman–Lootens–Mortier–Stottmeister–Ueda–Verstraete | Fock space with a semi-definite MPO norm (Stacey fermions): a single interacting Weyl on a ring, unitary and local, no doubling | Positive-definite inner product | 1+1D preprint [V-abs] | arXiv:2405.10285 |

### 1e. Anomaly perspective

| Source | What it shows | Status | Citation |
|---|---|---|---|
| Witten SU(2) | An odd number of SU(2) doublets is inconsistent (global anomaly). The SM has 4 doublets per generation | Classic | PLB 117, 324 (1982) [UNVERIFIED bib] |
| Wang–Wen–Witten | New SU(2) anomaly: theories without spin structure need an even number of spin-(4r+3/2) multiplets. Matters for fermions emergent from bosons; SM has none | [V-abs] | arXiv:1810.00844 (J. Math. Phys. 2019) |
| García-Etxebarria–Montero | Dai–Freed anomalies: SM, SU(5), Spin(10) anomaly-free. 16 Weyl per generation (with nu_R) ⇔ Dai–Freed freedom of a Z_4 symmetry (mod 16). Z_9 baryon triality needs generations ≡ 0 mod 3 | [V-abs] | JHEP 08 (2019) 003, arXiv:1808.00009 |
| Fidkowski–Kitaev | Interactions reduce Z to Z_8 in 1D Majorana chains: the prototype of SMG and of mod-8/16 counting | [V-abs] | PRB 81, 134509 (2010) [SEC vol.] |
| Kravec–McGreevy–Swingle (+ Wang–Potter–Senthil) | All-fermion electrodynamics exists only on the boundary of a 4+1D state. A constraint on emergent U(1) gauge theories from bosons | [V-abs] | arXiv:1409.8339; 1306.3238 [SEC] |
| "Anomaly-free ⇔ lattice-regularizable" | Evidence for: Lüscher (U(1), 4D Euclidean); all-orders non-abelian; Kadoh–Kikukawa (EW, restricted sectors); 1+1D exact (3450 by four groups); 1+1D finite-group theorem; TPF U(1) disentanglers. Against / caveats: Shirley–Zhang–Ji–Levin (anomaly-free but not on-siteable, 2D); Golterman–Shamir constraints on SMG. No 3+1D non-abelian Hamiltonian construction | Conjecture, open in 3+1D non-abelian | Wen 2013; Wang–Wen 2020; refs above |

### 1f. Condensed-matter realizations

| Source | What it shows | Status | Citation |
|---|---|---|---|
| Wan–Turner–Vishwanath–Savrasov | Weyl semimetal prediction (pyrochlore iridates) with Fermi arcs. Weyl nodes in pairs | [V-abs] | PRB 83, 205101 (2011) |
| Xu et al. (TaAs) | ARPES: bulk Weyl cones and nodes, surface Fermi arcs ending on nodes. Nodes paired | [V-abs] | Science 349, 613 (2015) |
| Fu–Kane–Mele; Hasan–Kane | Strong 3D TI surface "realizes the 2+1D parity anomaly without fermion doubling" (single Dirac cone per surface); partner on the opposite surface | [V-abs] | PRL 98, 106803 (2007); RMP 82, 3045 (2010) |
| Quantum Hall edges | Chiral edge with anomaly inflow from the 2D bulk | Standard | Halperin PRB 25, 2185 (1982) [UNVERIFIED] |
| Shen (perspective) | Lattice view of single massless Dirac fermions: high-energy sector breaks the symmetry, low-energy sector restores it | [V-abs] | arXiv:2609.06349 |

### 1g. Qubit/spin lattices, emergent fermions

| Source | What it shows | Status | Citation |
|---|---|---|---|
| Levin–Wen | On spin lattices, emergent fermions always come with strings and so couple to a gauge field (exactly solvable 2D/3D examples) | [V-abs] | PRB 67, 245316 (2003) |
| Wen (string-nets) | String-net condensation gives emergent gauge bosons and massless (Dirac, non-chiral) fermions from local bosonic models | [V-abs]; journal [UNVERIFIED] | hep-th/0302201 |
| Verstraete–Cirac | Any local fermion Hamiltonian maps to a local spin Hamiltonian in any dimension using auxiliary Majoranas | [V-abs] | cond-mat/0508353 (J. Stat. Mech. 2005 [SEC]) |
| Chen–Kapustin | Exact 3D bosonization: fermions ↔ Z_2 2-form gauge theory with modified Gauss law; locality preserved; depends on spin structure | [V-abs] | PRB 100, 245127 (2019) |
| Hermanns–O'Brien–Trebst; O'Brien–Hermanns–Trebst | 3D Kitaev qubit models: emergent Majorana Weyl nodes (paired) with a Z_2 gauge field | [V-abs] | arXiv:1411.7379 (2015); PRB 93, 085101 (2016) |
| Wang–Wen | 16/gen SM via Spin(10) mirror gapping: definable on a 3+1D lattice of bosons/qubits (claim); 15/gen needs fermions | Proposal [V-abs] | PRR 2, 023356 (2020) |

---

## 2. Premise ledger: which premise each escape drops

| Premise (N–N / Shamir / Fidkowski–Xu) | Escapes that drop it | Qubit lattice with nearest-neighbour rules |
|---|---|---|
| Free (bilinear) | SMG / mirror gapping (Wen; Wang–Wen; Catterall; You–BenTov–Xu) | Available. Interactions are native |
| On-site chiral symmetry | GW/overlap (Lüscher), Gioia–Thorngren, Onsager charges, TPF disentanglers | Available if not-on-site pieces are finite-depth circuits; exact GW needs tails |
| Ultralocality / strict finite range | Overlap (exponential), quasi-local Floquet unitaries (Higashikawa; Fidkowski–Hastings), Beenakker 2D | **Not available exactly.** Nearest-neighbour rules are ultralocal; only truncations |
| Closed d-dim lattice (no boundary) | Domain wall, Kaplan single boundary, Kaplan–Sen | Needs a 4+1D bulk for 3+1D Weyl; Z^3 gives at most 2+1D bulk / 1+1D edge |
| Static Hamiltonian (continuous time) | Floquet/QCA with bulk winding (Bessho–Sato) | Allowed, but strictly local free walks have W3=0 ([INF+CHK]); interacting case open |
| Hermiticity / norm positivity | Non-Hermitian (Chernodub, Bessho–Sato, Ma–Zhang), Stacey/MPO norms | Non-unitary or nonstandard Hilbert space |
| Compact quantized chiral charge | Gioia–Thorngren single Weyl (non-compact), Singh order-k (unquantized) | Possible, but such charges cannot be gauged as on-site U(1) |
| Translation invariance | Not by itself a known escape: disorder and inhomogeneity keep anomaly constraints (Shamir; Gioia–Burkov–Hughes) | — |

---

## 3. Ranked escape mechanisms for a qubit lattice with local rules

Ranking criteria: compatibility with Z^3, finite-dim sites and strictly local rules; strength of evidence; whether it reaches non-abelian SM content.

### 1. Mirror-sector symmetric mass generation (SMG) with the 16 per generation
- **Premise dropped:** free-ness. The mirror 16 is gapped by multi-fermion interactions with no symmetry breaking. Shamir's interacting theorem is evaded only if mirror poles become zeros that are not "kinematical".
- **Unproven:**
  - A direct, continuous 4D SMG transition for a 16-plet with SM (or Spin(10)) symmetry. 4D four-fermion numerics show intermediate phases.
  - Whether the zeros are kinematical (if so, Golterman–Shamir make it vector-like).
  - Unitarity once gauged (ghost-like zeros).
  - That the light sector stays local and gapless.
- **Strongest evidence:**
  - 1+1D: DMRG on 3450.
  - 2+1D: QMC shows continuous SMG transitions.
  - 4D: SU(3) N_f=8 SMG phase (suggestive).
  - The anomaly arithmetic fits: 16 with nu_R cancels Z_16 (García-Etxebarria–Montero).
- **Small test:**
  - (a) Single-site exact diagonalization in the 2^16 Fock space of 16 complex modes (one mirror generation per site). Search for a site-local interaction invariant under SU(3)×SU(2)×U(1)_Y (and optionally Spin(10)) with a unique, gapped, symmetric ground state. No such interaction means the mirrors need multi-site dynamics, which kills the simplest "local SMG seed".
  - (b) Golterman–Shamir diagnostic on the 1+1D 3450 chain (L≈16–24). Compute the zero-frequency inverse propagator of the light and mirror interpolating fields. Test whether the mirror zero is kinematical, i.e., whether a local one-particle effective H with paired chiralities appears.

### 2. Not-on-site chiral symmetry plus symmetry disentangler, then on-site gauging (TPF 2026)
- **Premise dropped:** on-site-ness, at the intermediate stage. The final Hamiltonian is strictly local with on-site gauge symmetry, which avoids Fidkowski–Xu because the original symmetry is not a shallow circuit of on-site type.
- **Unproven:**
  - A 3+1D Hamiltonian whose IR is the Weyl content.
  - The hypercharge interface step (iii).
  - Non-abelian SU(3)×SU(2).
  - Finite-dim (qubit) versions; rotors are used.
  - Shirley–Zhang–Ji–Levin show anomaly-free does not imply on-siteable in 2D.
- **Strongest evidence:** exactly solvable 1+1D 3450 (TPF; Seifnashri); the 1+1D finite-group theorem (Seifnashri–Shirley, PRL 2026).
- **Small test:**
  - (a) Arithmetic: check that one generation's hypercharges (with nu_R) group into TPF's charge vectors, and list which anomaly-free sets fail.
  - (b) Truncate each rotor to spin-S (2S+1 levels) in the 1+1D 3450 model. Measure how the commutator [H, Q] and the disentangler's light-cone growth scale with S. This decides whether qubit-sized sites can host the construction.

### 3. Hamiltonian Ginsparg–Wilson / overlap with Lüscher-type gauge-invariant measure
- **Premise dropped:** ultralocality and on-site chiral symmetry. The symmetry is exact but gauge-field dependent.
- **Unproven:**
  - A Hamiltonian (continuous-time) chiral gauge theory.
  - The nonperturbative non-abelian measure beyond restricted EW sectors.
  - Exact realization with nearest-neighbour qubit rules, which is impossible: no ultralocal GW operator exists (Horváth; Bietenholz).
- **Strongest evidence:** Lüscher abelian (1999) and all-orders (2000) proofs; Kadoh–Kikukawa EW sectors; overlap locality (Hernández–Jansen–Lüscher).
- **Small test:** free Z^3 Creutz–Horváth–Neuberger overlap Hamiltonian. Measure the hopping decay length, then truncate to radius r = 1, 2, 3 and measure (i) reappearing doubler spectral weight and (ii) ‖[H_r, Q5]‖. This tells you how much nearest-neighbour approximation costs.

### 4. Exact not-on-site lattice chiral charges / Onsager algebra (Gioia–Thorngren; Chatterjee–Pace–Shao)
- **Premise dropped:** on-site-ness and commutativity of the V and A charges (or compactness, for the single Weyl).
- **Unproven:**
  - Gauging the not-on-site U(1) (authors: "difficult").
  - Chiral (rather than doublet) gauge content with on-site gauge charges.
  - Interacting versions.
- **Strongest evidence:** explicit cubic-lattice models (PRL 2026). The Weyl doublet's flavour SU(2) and its Witten-anomaly link are directly relevant to SM SU(2) doublets.
- **Small test:** build the Gioia–Thorngren doublet on an L = 6–8 cubic lattice (free). Verify [H,S0]=[H,S1]=0 and the Onsager relations. Then couple S0 to Z_N link qubits and check, in a monopole/flux background, whether S1 conservation fails in the way the anomaly predicts.

### 5. Single-boundary / domain-wall chirality (Kaplan 2024; Kaplan–Sen 2024)
- **Premise dropped:** a closed d-dimensional lattice. The chiral modes live on the boundary of a (d+1)-dimensional bulk.
- **Unproven:** the gauge sector on the lattice; harmlessness of the exp(−2mR) cross-boundary nonlocality; and for Z^3, a fourth spatial dimension. The 3+1D Weyl needs a 4+1D bulk, which Z^3 can only fake with an internal flavour index (overlap-like, nonlocal in that index).
- **Strongest evidence:** free Hamiltonian 2+1D result with continuous time (Kaplan–Sen); 3D spherical domain walls (Aoki–Fukaya–Kan).
- **Small test:** feasibility accounting. Put the 2+1D Wilson Hamiltonian on a disk inside Z^3 (one direction unused) with Verstraete–Cirac-encoded fermions. Verify one chiral edge and measure the cross-disk splitting against R. Then count what a 3+1D version needs. Expected verdict: geometrically incompatible with Z^3 except as a toy.

### 6. Discrete-time QCA with bulk winding (Bessho–Sato route)
- **Premise dropped:** a static Hamiltonian, since quasienergy is periodic.
- **Unproven:**
  - Any **strictly local** realization. For free walks and for the one-particle sector it is ruled out ([INF] Read + Bessho–Sato; [CHK]), consistent with Beenakker et al. in 2D, Sun et al.'s "N–N holds on a Floquet lattice", and the D'Ariano–Perinotti Weyl QCA having a partner.
  - Interacting, non-circuit QCAs on Z^3 whose low-quasienergy composite excitations carry net chirality. Their effective one-body walk is quasi-local, so the K-theory obstruction does not apply. No theorem found either way.
- **Strongest evidence:** quasi-local W3≠0 unitaries exist (Higashikawa; Fidkowski–Hastings), but they are not generated by any finite-time local evolution.
- **Small test:**
  - (a) Turn the [INF] into a written proof: Suslin stability / SK_1 = 0 for C[x^±, y^±, z^±] gives W3 = 0.
  - (b) Two-particle bound-state band of a U(1)-conserving interacting QCA on Z^3 (brickwork gates plus on-site interaction, with and without a GNVW-type shift layer). Compute W3 of the bound-state band's effective unitary. Nonzero would be a genuine new escape.

### 7. Bosonic (qubit) lattice chiral symmetry with emergent fermions (Lu–Seifnashri–Shao; Levin–Wen; Chen–Kapustin; Wang–Wen qubit claim)
- **Premise dropped:** fundamental fermions. Fermions are emergent with Z_2 gauge or 2-form gauge structure, and the chiral symmetry is realized on bosons.
- **Unproven:** emergent chiral (not Dirac) fermions in 3+1D from a local bosonic model. Every explicit example (string-nets, 3D Kitaev) gives paired or Dirac spectra. The finite-dim version of Lu–Seifnashri–Shao is unclear (it uses compact bosons). The Wang–Wen qubit SM is conjectural.
- **Strongest evidence:** exact bosonization keeps locality (Chen–Kapustin); exact U(1)_V × U(1)_A with anomaly on a bosonic lattice (PRD 2026).
- **Small test:** count. For one generation on Z^3, how many qubits per site does Chen–Kapustin / Verstraete–Cirac encoding need (16 complex modes plus gauge/auxiliary qubits)? Then check whether a 3D Kitaev-type qubit model can have an odd number of emergent Majorana Weyl nodes. Prediction from N–N on the emergent band structure: no.

### 8. Non-Hermitian / open-system dynamics
- **Premise dropped:** Hermiticity or unitarity.
- **Unproven:** a physical, probability-conserving interpretation. Non-Hermitian H is a no-jump or post-selected effective description. No Lindbladian construction of an unpaired chiral fermion was found, and the Liouvillian doubles degrees of freedom.
- **Strongest evidence:** Bessho–Sato theorem and finite-range non-Hermitian w3 ≠ 0 models; Chernodub 1+1D.
- **Small test:** embed the Bessho–Sato 3D model as the no-jump part of a qubit Lindbladian with local jumps. Compute the full Liouvillian band structure (vectorized, doubled) and check whether net chirality survives. Expectation: it cancels.

### 9. Semi-definite (MPO/Stacey) norm
- **Premise dropped:** a positive-definite inner product. The physical space is a quotient.
- **Unproven:** dimensions above 1+1D; whether the quotient keeps a local tensor-product (qubit) structure; gauge coupling.
- **Strongest evidence:** 1+1D interacting single Weyl with DMRG (2024 preprint).
- **Small test:** on L ≤ 12 chains, check whether the null space of the MPO norm is generated by local operators. That decides whether the physical theory is a local qubit model.

(The 1+1D bosonization-based exact chiral symmetry of Berkowitz–Cherman–Jacobson and Seifnashri is not ranked: it relies on 2D bosonization with no 3+1D analog.)

---

## 4. What remains open as of 2026 (literature consensus as far as checked)

1. No complete nonperturbative Hamiltonian lattice construction of a 3+1D non-abelian chiral gauge theory (SM) exists.
   - The best partial results: Lüscher (abelian; all orders), Kadoh–Kikukawa (EW sectors, Euclidean), and TPF (U(1)_Y argued, rotors).
2. 4D SMG of a full 16-plet with the required symmetry is not established numerically. The SMG paradigm is under active theoretical challenge (Golterman–Shamir 2023–2026).
3. Whether finite-dimensional on-site Hilbert spaces (qubits) can host the disentangler constructions is untested. The rigorous models use rotors.
4. Whether strictly local *interacting* QCA on Z^3 can carry net Weyl chirality is open. The free and one-particle versions are closed by K-theory ([INF]).

## Files
- `scripts/w3_check.py`: W3 numerics (Laurent walks → 0; quasi-local normalized map → −1).
- `scripts/dariano_weyl_nodes.py`: node chiralities of the BCC Weyl QCA.
- `downloads_untrusted/`: one PDF (Bessho–Sato), not parsed or executed.
