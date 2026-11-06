# LW1. The cube law and its consistency

## 0. Status

**FINISH: FROZEN 2026-11-04 after pass 3, with the open statements below named. The LW1 target is not established.** Pass 1 by Claude (`LW1_DRAFT.md`), pass 2 by Codex (this text), pass 3 by a fresh Claude Opus 5.5 session at max effort (`LW1_REFEREE.md`: 92 items, 85 correct, 3 errors and 4 incomplete, none changing a theorem's content). The referee's eight required edits are applied. Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment.

**Proved here.** Free-tick cell covariance and site transitivity (A2), event geometry (A3), the scalar-walk obstruction (B2), the one-site frame classification (B3, B5(a)), exact Gauss conservation (B4), exact finite gate factorization, finite transport existence and uniqueness (B6–B7), the quasi-free copy criterion and record witnesses (B8), record permanence, the free sea (B10), the countable-list consistency result (B11), the free dispersion expansion (C1), infinite-volume dynamics, stationary states, formation, supported histories, and existence of invariant transport optimizers (E1–E6). Claims concerning an unspecified plaquette update are conditional on its stated hypotheses.

**Open by name.** LW1-U as stated is false for non-factor states (`LW1U_DRAFT.md` Theorem 4.3); open are LW1-U_f (factor states) and its case LW1-U_sea (the vacuum), plus the owner's rule for non-factor states; owner readings are needed for LW1-i/B9 ("nearest-neighbor conditions"; the shell-only reading is false), LW1-ii/F (target item 3; the closed-box reading is false) and LW1-R (the domain on which "Records form." is required; the tracial state never forms one); B5(b) (cell frame claim); B12(ii–iii) (the imported scalar and fermion transfer assertions); LW1-N (selection for non-invariant states); GA1-P (plaquette gate class); VC1 (the gauged vacuum). The draft's full edge-triple universality assertion fails as stated; the factorization actually needed here is closed below. These gaps prevent a complete proof of the assembly target.

**Amendment 1, 2026-11-04 (owner decisions after the freeze; `TOE_ASSEMBLY.md` section 3.3).** No proved result changes.
- LW1-i is settled under PS-Ar: the nearest-neighbor conditions of a site are the state of its one-tick neighbourhood of influence, which contains the site and its six neighbours. The formation test (PS-3c) and the locked-value law (B9's established clauses) use only the site and its six neighbours, so Admissibility holds for \(L_{\rm cube}\). The shell-only GAP LW1-i/B9 is kept below as the record of why the reading was needed.
- LW1-ii/F is settled: target item 3 is restated as existence on \(\mathbb Z^3\times\mathbb N\) with finite-box laws as restrictions of one history, which E1-E5 prove. The closed-box identity stays false, as shown below.
- Non-factor states: no rule is adopted. LW1's uniqueness question is LW1-U_f, at factor states only.
- LW1-R moves to part TM1 as TM1-i.
- Open after this amendment: LW1-U_f, with LW1-U_sea first; LW1-N; B5(b); B12(ii-iii); GA1-P; VC1.

**Amendment 2, 2026-11-05 (B5(b); frozen part `B5B.md`).** No proved result of this file changes.
- B5(b) is settled under split register changes. `B5B.md` (Claude draft `B5B_DRAFT.md`, Codex distillation, referee `B5B_REFEREE.md`, frozen) proves: if a frame on an even cell leaves each odd gate unchanged after register changes split at the cell, it acts on the cell's modes by independent site phases (Theorem 3.1). The same holds if only the whole base tick, or its odd half-step, is unchanged (Theorem 3.3). Many-body frames, frames of either parity and frames that mix modes with internal links are included. The mode image is exactly \(U(1)^8\). So the GAP B5(b) below is closed in that reading, and the scalar claim stays false.
- Under register changes that entangle internal and outside links (reading R-E), the compatible frames are operator-valued phases and are not closed under composition (`B5B.md`, RC5). That case with the even gate, and the plaquette layer, stay open as B5b-E′ and with GA1-P.
- `LW1-U_sea` has a pass-1 proof off the segment \(2\varepsilon+\mu=\pi\) (`LW1U_SEA_DRAFT.md`, not yet distilled); the free sea's actual configuration never moves there.
- Open after this amendment: LW1-U_f (LW1-U_sea on the segment, as LW1-U_hop); LW1-N; B5b-E′; B12(ii-iii); GA1-P; VC1.

**Premises and readings.** Under PS-1 read by PS-1c, PS-3 read by PS-3h and PS-3c, PS-6 read by PS-6r, PS-7 read by PS-7r, and PS-11 read by PS-11c (final texts in `TOE_ASSEMBLY.md`, lines 167–185), and PS-4; with the CAR reading of one site mode and parity superselection. PS-2 is not used: no proof here needs it. Two further inputs lie outside the working-set text and are listed as such: the joint Born identification (inferred definition 26) and the record-memory reading of "locks" (inferred definition 25). The time/space graining in A3 uses `kinetic_isotropy_primitive`. A realized history is supplied subject to PS-11c; this is LW1's only use of `realized_state_primitive`; probability-one claims are not pointwise claims about every history. No theorem here derives the CAR product, the Born rule, the law choice, or a physical gauge sector from the four axioms alone.

**Free data.** Angles \(\varepsilon,\mu\) satisfy \(0\leq\mu<2\varepsilon<\pi\). The link spin is \(S\in\{\tfrac12,1,\tfrac32,\ldots\}\). The electric angle is \(\tau_E\in\mathbb R\), including zero. The initial state \(\omega_0\) is supplied data, not a numerical constant. The plaquette class and its constants are unspecified. Readers: LZ1 uses \(\varepsilon\); MT1/VC1 use \(\mu\); GA1/GA2 use \(S,\tau_E\) and any plaquette data; TM1 uses \(\omega_0\).

**Provenance.** Read only `LW1_DRAFT.md` in full and `TOE_ASSEMBLY.md`, lines 167–227. Draft SHA-256: `f35997463e2ee9ceadb1e5e734737e173da24fcfadfee4a17563deaad7cf22a9`. SHA-256 of the assembly excerpt, with its file newlines: `8ff6b3629a7d5d519027f88dc587dfd84abc3cc38381b0cd13b2530e8d94bbb4`. Draft line references below refer to this revision. No numerical checks serve as proofs.

**Pass 2 distilled by Codex (`gpt-6-astra`, reasoning effort high, codex-cli 0.165.0, session `01a1a8f8-b07f-7c21-9221-d1d76d0a6713`; recorded by the lead session from the run log), not yet refereed.**

## 1. Definitions

**Sites and symmetry.** Sites are \(x\in\mathbb Z^3\); \(e_i\) are coordinate vectors. The shell is \(N(x)=\{x\pm e_i:1\leq i\leq3\}\). Put \(\mathbf1=(1,1,1)\) and \(c_0=\mathbf1/2\). The even and odd tilings are
\[
\mathcal T_e=\{b+\{0,1\}^3:b\in2\mathbb Z^3\},\qquad
\mathcal T_o=\{b+\mathbf1+\{0,1\}^3:b\in2\mathbb Z^3\}.
\]
The group \(O\) consists of determinant-one signed coordinate permutations. Its action about \(c_0\) is \(x\mapsto Q(x-c_0)+c_0\). Write \(\mathscr G=2\mathbb Z^3\rtimes O_{c_0}\) for these spatial transformations, with the sign lifts constructed in A2. Statements about the exact spatial symmetry group refer to orientation-preserving lattice isometries lifted by diagonal phases. They do not classify arbitrary unitaries commuting with the update. Set \(T_t|x\rangle=|x+t\rangle\).

**Matter and links.** The operators \(c_x,c_x^\dagger\) satisfy the canonical anticommutation relations (CAR): \(\{c_x,c_y\}=0\), \(\{c_x,c_y^\dagger\}=\delta_{xy}\). Put \(n_x=c_x^\dagger c_x\) and \(N_F=\sum_{x\in F}n_x\). On a finite set, fermion parity is \(\mathcal P_F=(-1)^{N_F}\). An even operator commutes with parity; an even state is invariant under parity conjugation. An odd-parity vector can define an even state. The matter algebra is the CAR algebra, a graded tensor product of the one-site algebras \(M_2(\mathbb C)\).

Each positively oriented link \(\ell=(x,x+e_i)\) has the spin-\(S\) Hilbert space with basis \(|m\rangle\), \(m=-S,-S+1,\ldots,S\). Define
\[
 E_\ell|m\rangle=m|m\rangle,\qquad
 J_\ell|m\rangle=\sqrt{S(S+1)-m(m+1)}\,|m+1\rangle,
\]
with the last expression zero at \(m=S\), and put \(S^x_\ell=(J_\ell+J_\ell^\dagger)/2\). Thus \([E_\ell,J_\ell]=J_\ell\). Link algebras are ordinary tensor factors and commute with matter. A cube and its links have Hilbert space \(\mathcal H_C=(\bigwedge\mathbb C^C)\otimes\bigotimes_{\ell\subset C}\mathbb C^{2S+1}\). The quasi-local algebra \(\mathfrak A\) is the norm completion of the finite matter-and-link algebras. Its states are positive normalized linear functionals. Gauge transformations are conjugations by
\[
 e^{it\mathcal G_x},\qquad
 \mathcal G_x=n_x+\sum_{\ell\text{ out of }x}E_\ell-\sum_{\ell\text{ into }x}E_\ell.
\]
Gauge invariance of a state means invariance under these conjugations, not support in the sector \(\mathcal G_x=0\). Global number invariance means invariance under \(c_x\mapsto e^{it}c_x\). In the phrase “gauge-invariant quasi-free state” below, “gauge” means this global number symmetry, not local link gauge symmetry.

**Free tick.** Put \(\eta_i(x)=(-1)^{\sum_{j<i}x_j}\), \(a_e=\varepsilon-\mu/2\), and \(a_o=\varepsilon+\mu/2\). On \(\ell^2(\mathbb Z^3)\), define
\[
 R_T=\frac1{\sqrt3}\sum_{(x,x+e_i)\text{ in cubes of }\mathcal T_T}
 \eta_i(x)(|x+e_i\rangle\langle x|+|x\rangle\langle x+e_i|),
 \quad T\in\{e,o\}.
\]
Let \(R_C\) be the restriction to a cube. Set \(V_e=e^{-ia_eR_e}\), \(V_o=e^{ia_oR_o}\), and \(V=V_oV_e\). On finite Fock spaces \(\Gamma(W)=\bigoplus_k\bigwedge^k W\); it fixes the empty vector. This normalization removes the arbitrary scalar phase in an implementer. The free update is \(\Gamma(V)\). At infinite volume it means its CAR automorphism, not an asserted unitary in the sea representation.

**Dressed tick.** For a cube define the even Hermitian operator
\[
 H_C=\frac1{\sqrt3}\sum_{\ell=(x,y)\text{ in }C}\eta_i(x)
 (c_y^\dagger J_\ell c_x+c_x^\dagger J_\ell^\dagger c_y),\quad y=x+e_i.
\]
The matter layers are \(M_e=\prod_{C\in\mathcal T_e}e^{-ia_eH_C}\) and \(M_o=\prod_{C\in\mathcal T_o}e^{ia_oH_C}\). The electric layer is \(W_E=\prod_\ell e^{-i\tau_E E_\ell^2}\). Products at infinite volume mean the local automorphisms of E1. The specified base tick is \(U_0=W_EM_oM_e\). A possible added plaquette update is denoted \(W_B\); it is not specified here. If supplied, put \(U_B=W_BW_EM_oM_e\). A plaquette monomial \(J_p\) is the oriented product of \(J_\ell\) or \(J_\ell^\dagger\) around its four edges; its Hermitian term is \(B_p=J_p+J_p^\dagger\).

**Time and states.** A half-tick has index \(h\in\mathbb N_0\); tick \(n\) ends at \(h=2n\). For the base law the Schrödinger half-step operators are \(W_{2n}=M_e\) and \(W_{2n+1}=W_EM_o\). Define the Heisenberg automorphism \(\beta_h(A)=W_h^*AW_h\), \(\omega_{h+1}=\omega_h\circ\beta_h\), and the tick automorphism \(\alpha(A)=U_0^*AU_0\). Thus \(\varrho_n=\omega_{2n}=\omega_0\circ\alpha^n\). On a finite system this convention gives \(\rho' = W_h\rho W_h^*\). For a supplied \(W_B\), insert it on the left of the odd half-step. Results depending on a support radius of two cubes concern \(U_0\).

**Occupations, odds and records.** Configurations are \(\xi\in\Omega=\{0,1\}^{\mathbb Z^3}\). On finite \(F\), let
\[
 P_{F,\sigma}=\prod_{x\in F}n_x^{\sigma_x}(1-n_x)^{1-\sigma_x},\qquad
 \nu_\omega(\xi_F=\sigma)=\omega(P_{F,\sigma}).
\]
Projectors include the identity on links. Commutativity of the \(n_x\) gives consistent finite probabilities; Kolmogorov's extension theorem defines \(\nu_\omega\). Write \(\nu_h=\nu_{\omega_h}\). The copy test is \(D_{xy}=(n_x-n_y)^2\). Define
\[
 F_n=\{x:\exists y\ne z\in N(x),\ \varrho_n(D_{xy}+D_{xz})=0\},\quad
 \mathcal R_0=\varnothing,\quad \mathcal R_n=\mathcal R_{n-1}\cup F_n.
\]
The first-record time is \(t_x=\inf\{n\geq1:x\in F_n\}\), with \(\inf\varnothing=\infty\). If finite, the record content is \(r_x=\xi_{2t_x}(x)\). It never changes. Readout at a recorded site returns \(r_x\); other sites have no readout. Histories are sequences \((\xi_h)_{h\geq0}\); their probability measure is \(\mathbb Q\).

**Transport.** For a finite union \(\Lambda\) of active cubes, use its reduced density matrix \(\rho\) and active cube update \(W_\Lambda\). Set \(p(\xi)=\operatorname{tr}(P_{\Lambda,\xi}\rho)\), \(p'(\zeta)=\operatorname{tr}(P_{\Lambda,\zeta}W_\Lambda\rho W_\Lambda^*)\), and
\[
 \mathscr S_\Lambda=\{(\xi,\zeta):P_{\Lambda,\zeta}W_\Lambda P_{\Lambda,\xi}\ne0\}.
\]
The single-cube version is \(\mathscr S_C\). A coupling \(\gamma\) is a probability measure with the specified first and second marginals. Let \(\Pi(p,p';\mathscr S_\Lambda)\) contain those supported on \(\mathscr S_\Lambda\). Its cost and entropy are
\[
 d_\Lambda(\gamma)=\sum_{\xi,\zeta}\gamma(\xi,\zeta)\sum_{x\in\Lambda}\mathbf1_{\xi_x\ne\zeta_x},\qquad
 \mathsf H_\Lambda(\gamma)=-\sum_{\xi,\zeta}\gamma(\xi,\zeta)\log\gamma(\xi,\zeta),
\]
where \(0\log0=0\). The selected coupling minimizes cost and then maximizes entropy. Its transition kernel is \(\mathsf K(\xi,d\zeta)\). Values on zero-probability inputs are arbitrary measurable probability kernels.

For cell-invariant \(\omega_h\), let \(\mathcal C_h\) be the cell-translation-invariant couplings of \(\nu_h,\nu_{h+1}\) obeying every active-cube support. With \(C_0=\{0,1\}^3\), put
\[
 \bar d(\gamma)=\tfrac18\mathbb E_\gamma\sum_{x\in C_0}\mathbf1_{\xi_x\ne\zeta_x},\qquad
 s(\gamma)=\lim_{m\to\infty}\frac{\mathsf H_{Q_m}(\gamma)}{|Q_m|},\qquad
 \mathcal O_h=\mathop{\rm argmax}_{\mathop{\rm argmin}_{\mathcal C_h}\bar d}s.
\]
Here \(Q_m=\{0,\ldots,2^m-1\}^3\) is a box of cells; each cell has the pair alphabet \(\{0,1\}^{16}\). Entropy is per cell and cost per site. E6 proves the entropy limit. Weak convergence of measures means convergence against continuous functions; weak-* convergence of states means convergence on every algebra element. Tori have even site side length \(L\), periodic signs and tilings. Local convergence means convergence of every fixed finite marginal after identifying a neighbourhood with the lattice.

**Sea and momentum.** Bloch momentum for cells is \(K\in\mathbb T^3=(-\pi,\pi]^3\). Write a site as \(x=2b+r\), \(r\in\{0,1\}^3\), and Fourier transform the cell index \(b\); the eight residue components give periodic fibre matrices. Define \(\chi(K)=\tfrac13\sum_i\cos K_i\), \(a_{\rm band}=(\cos\mu-\cos2\varepsilon)/2\), and \(b_{\rm band}=(-\cos2\varepsilon-\cos\mu)/2\). Quasi-energy is defined by the eigenvalue \(e^{-iw}\), with \(w\in(-\pi,\pi]\). The negative-arc projection is \(P=\mathbf1_{(-\pi,0)}(w(V))\). The gauge-invariant quasi-free state with covariance \(G\), \(0\leq G\leq1\), is specified by \(\omega_G(c_y^\dagger c_x)=G_{xy}\), vanishing unequal-creation/annihilation moments, and Wick's determinant rule for the remaining moments. In particular, the free sea is \(\omega_P\). Put \(D_s|x\rangle=(-1)^{x_1+x_2+x_3}|x\rangle\), let \(\mathcal K\) be site-basis complex conjugation, and set \(\Theta=D_s\mathcal K\). In C1, \(K=k\widehat n\), \(|\widehat n|=1\), \(k\geq0\), \(s_\varepsilon=\sin\varepsilon\), \(T_4(\widehat n)=\sum_i\widehat n_i^4\), and site momentum is \(q=K/2\).

For a finite site set \(F\), \(G_F=(G_{xy})_{x,y\in F}\) denotes the principal covariance matrix; \(P_F\) and \((I-P)_F\) use the same convention.

**Events.** An event is an active cube at half-tick \(h\), located at \((X,h)\), where \(X\) is its centre minus \(c_0\). The two-sided geometric extension allows \(h\in\mathbb Z\); actual histories use \(h\geq0\). Denote the set of two-sided event positions by \(\mathcal E\). Equal spatial and temporal units mean \(c\Delta=a\), with site spacing \(a\), half-tick duration \(\Delta\), and conversion constant \(c\). Define \(D_4=\{z\in\mathbb Z^4:\sum_jz_j\in2\mathbb Z\}\) and \(D_4^*=\mathbb Z^4\cup(\mathbb Z^4+\tfrac12(1,1,1,1))\). The draft's D4 candidate is a Euclidean nearest-event weight with all 24 root directions equivalent and a proposed Osterwalder–Schrader (OS) transfer along a chosen time root. Its Euclidean symmetry group is denoted \(W(F_4)\). It supplies no cube gate formula.

### Definitions inferred by the distiller

These are interpretive conventions, not additional axioms. Unjustified readings are explicitly left open.

1. **Implementer normalization:** \(\Gamma(W)\) fixes the empty vector; otherwise the draft's uniqueness claim has a scalar ambiguity (A1(5), lines 137–146).
2. **Heisenberg direction:** use \(A\mapsto U^*AU\) when states evolve by \(\rho\mapsto U\rho U^*\). The opposite conjugation in E1 does not match the subsequent state formulas (sections 5.4, 9.1–9.4).
3. **Two time indices:** \(\omega_h\) denotes half-time and \(\varrho_n\) tick-time; the draft uses \(\omega_n\) in both roles (sections 4, 9.3–9.4).
4. **Electric placement:** put the electric layer at the end of the odd half-step. It has no separate occupation move because it commutes with every occupation projector (sections 4, 5.4).
5. **Spin range:** spin \(S\) is a positive integer or half-integer, not an arbitrary real number \(\geq1/2\) (section 4(2)).
6. **Link orientation reversal:** a geometric reversal uses \(E\mapsto-E\), \(J\mapsto J^\dagger\), implemented by a spin rotation. Gauged covariance needs this convention (sections 5.3, 9.2).
7. **Covariance lifts:** geometric symmetries may carry site sign gauges; their lifts may differ by a scalar phase. The claimed spatial group is not the entire operator commutant (A2 and A2a).
8. **Local gauge invariance:** it means invariance of a state under conjugations, not a prescribed zero-charge Gauss sector (B4, E2b).
9. **Quasi-free conventions:** in B8/B10 gauge invariance means global particle-number symmetry, distinct from the local symmetry in B4/E2b. The finite covariance matrices in B11 are principal compressions, not occupation-pattern projectors.
10. **Infinite-volume update:** infinite gate products denote automorphisms. No global Fock-space implementer for an infinite sea is assumed (A1(5), E1).
11. **First record:** retain the value at the first formation time; subsequent \(F_n\) membership cannot overwrite it (E3, E5(v)).
12. **Formation schedule:** the unrecorded condition depends on previous formation sets, not previous realized values (B9, E3).
13. **Null inputs:** kernels are specified arbitrarily on zero-marginal inputs; they do not alter the history measure (B7, E5).
14. **Cube subsystem:** a finite active region includes the links used by its gates; unused factors can be traced out (section 5.4, E4).
15. **Boundary convention:** closed finite evolutions are distinct from restrictions of an infinite history. No boundary condition or compatible closed-box family was specified (section 9 opening, section 10).
16. **Periodic approximants:** tori have even side length and periodic hop signs. Translation invariance of their states is an additional hypothesis when asserting invariant optimizers (B7, LW1-U Attack 2); it is not automatic from local convergence.
17. **Entropy units and windows:** use the cell pair alphabet and dyadic cell boxes for specific entropy, and divide cost by eight for a site average (E6).
18. **Phase cut and zero modes:** the strict negative interval excludes zero modes. The massless zero fibre is null in infinite volume; this does not assign half of a finite torus zero eigenspace (B10, LW1-U).
19. **Even state versus vector:** B8b's three-particle vector has odd parity; its density matrix is even (B8b(ii)).
20. **Two-sided event geometry:** the full D4 lattice requires integer times of both signs; the first-tick law occupies its future half (A3 versus C4/PS-4).
21. **Time direction:** the time axis is parallel to the shortest vector \(2e_4\); \(e_4\) itself is not an event-lattice vector. An oriented root stabilizer and its unoriented line stabilizer are distinct (A3, B12(i)).
22. **Finite events and frequencies:** PS-11c's finite events are subsets of the finite site/tick occupation-and-record alphabet. Translates use cell translations and full ticks. No frequency convergence or time stationarity is assumed (FINAL PS-11c; draft section 5.7).
23. **Shell data:** the draft implicitly treats the identity of copy neighbours as supplied by the shell state. This is unjustified and remains GAP LW1-i/B9 (B9(i)–(iii)).
24. **Optional plaquette extension:** \(W_B\) is separate, unspecified law data. Statements extended to it require a gauge-invariant, cell-covariant finite circuit on links; this is a conditional hypothesis, not an adopted gate class (draft section 5.3; FINAL PS-6r).
25. **Record memory:** the permanent content is the value at formation, not a constraint that all later actual occupations at that site remain equal to it (B9(iv), E3, E5(v)). The draft's permanence proof uses this reading.
26. **Joint Born identification:** the draft applies the state expectation rule to joint occupation projectors, although its PS-2 quotation states a one-site trace rule. This manuscript takes that joint identification as a premise, not a derivation from the one-site quotation (C3, B6–B11, E4–E6).
27. **Quantifier on record formation:** the draft's witnesses establish formation for some supplied states, while its law domain permits arbitrary initial states. Reading this as satisfaction of the axiom on the entire domain is unjustified; see GAP LW1-R (B8a–B8b, section 9 opening).
28. **Bloch convention:** Fourier transform the cell index while retaining eight site residues; fibre symbols are periodic on the cell momentum torus (B10, C1, E2a).

## 2. Statement of \(L_{\rm cube}\)

The adopted refinements are the following exact texts from `TOE_ASSEMBLY.md`, section 3.2.

**PS-1c.**
> In PS-1 and in Admissibility, covariance under lattice translations and proper cubic rotations is read on cells: the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre, and its symmetry group acts transitively on sites.

**PS-3h.**
> The actual configuration is a configuration of site occupations. It exists at every half-tick and moves once per half-tick, using only the nonzero matrix elements of that half-tick between occupation configurations.

**PS-3c.**
> The actual value of a site has been copied into a neighbouring site at a tick when the law gives probability one that their actual values agree at that tick. A record forms at the end of a tick at each site that carries no record and whose actual value has then been copied into at least two of its neighbours; it locks the site's actual value.

**PS-6r.**
> Each link register is a finite quantum link: a finite-dimensional register on which the frame group of the site content acts, with the raising and lowering structure the Gauss law needs. Link registers carry odds but no actual configuration and no records.

**PS-7r.**
> In PS-7, the half-filled sea of a tick is the quasi-free state that fills every one-body mode with quasi-energy in `(-pi, 0)`, quasi-energy read in `(-pi, pi]`. It is defined when `pi` lies in a gap. For the gauged law, the vacuum is the state VC1 builds from this sea; PS-7 does not name it by itself.

**PS-11c.**
> A statement that the law gives probability one holds in the realized history, for each statement in this fixed list: (1) every event that names finitely many sites and ticks; (2) for every such event `E` and every pair of rationals `a < b`, the statement that the frequency of the translates of `E`, under the law's translations and ticks, over the windows `[-n, n]^3 x [0, n]` converges as `n -> infinity` to a limit in `[a, b]`.

**Law specification.** The proposed law is \(L_{\rm cube}=(U,\omega_0,\mathrm{Act})\), with the matter, spin links and parameter window of section 1. Its gate classes are:

1. The dressed matter cube gates \(M_e,M_o\), required.
2. The on-link electric layer \(W_E\), with independent free constant \(\tau_E\); zero is allowed.
3. A plaquette gate class, **OPEN as law data for GA1**. The draft found noncommuting shared-link plaquette terms and supplied no rotation-covariant ordering. This does not prohibit a plaquette update.

The specified base update is \(U=U_0\). Choosing a plaquette class would specify \(U=U_B\) and its additional constants. The results below state which version they cover. PS-6r alone supplies neither these gates nor their coefficients.

The initial state \(\omega_0\) is supplied. Initially there are no records. Odds evolve by the prescribed automorphisms and never depend on records. On a closed finite system (an even torus, or a closed box with a stated boundary prescription), \(\mathrm{Act}\) uses B7's least-change, greatest-entropy coupling. B7 couplings of nested regions of one infinite system are not shown to be restrictions of one another, so on \(\mathbb Z^3\) the actual configuration comes from \(\mathcal O_h\) only, on the cell-invariant domain. For non-invariant infinite states no rule is given (LW1-N). A unique such element is not yet proved. Formation and readout use \(F_n,t_x,r_x\) from section 1. Links carry neither actual occupations nor records. PS-11c applies precisely to its fixed list.

For the **free tick**, PS-7r selects \(\omega_P\), whose properties are proved in B10. It is the free vacuum in this manuscript. The dressed tick is not a one-body update, so this free state is not named as its vacuum. E2b proves existence of stationary, gauge-invariant, half-filled states of the gauged base law. Selecting and constructing the gauged vacuum is VC1's task.

**LW1 target.** Under these premises, the assembly asks for shell-determined conditional record odds, covariance, single permanent records, inclusion-consistent finite-box laws with an infinite history limit, and uniqueness after fixing the named free data. Record permanence and the existence statements below are established. Shell-only odds, closed-box inclusion consistency, infinite transport uniqueness, and the remaining law choices are open. No amendment of the assembly target is presumed.

## 3. Theorems and proofs

### 3.1 Geometry and finite gates

**Lemma A1 (ownership, flux and involutions).** Each positive edge belongs to exactly one cube in exactly one of the two tilings. Every unit face has sign product \(-1\). Both \(R_e^2\) and \(R_o^2\) equal the identity.

*Proof.* For an edge \((x,x+e_i)\), a tiling with offset \(o\in\{0,\mathbf1\}\) contains both endpoints in one cube exactly when \(x_i\equiv o_i\pmod2\). Each other coordinate belongs to a unique length-two interval of that tiling. Exactly one offset satisfies the condition. For \(i<j\), moving the base point by \(e_i\) reverses \(\eta_j\), whereas moving it by \(e_j\) leaves \(\eta_i\) fixed. The face product is therefore \(-1\). In a cube let \(A_i\) be its signed axis matching. Then \(A_i^2=I\). The two orders of traversing an \(i,j\) face have opposite signs, so \(A_iA_j=-A_jA_i\). Consequently \((A_1+A_2+A_3)^2=3I\). Cubes in each tiling are disjoint, proving the asserted involutions. ∎

**Lemma A1a (free nearest-neighbour factorization).** Each free half-tick is exactly a finite product of nearest-neighbour gate layers repeated over its cell lattice.

*Proof.* Order a cube's corners as
\(000,001,011,010,110,111,101,100\).
Successive corners share an edge. Adjacent-row Givens elimination reduces any \(8\times8\) unitary to a diagonal matrix: in column one eliminate from the last row upward; then do the same below the diagonal in each remaining column. Previously eliminated entries remain zero because both mixed rows have zero entries in those earlier columns. The final upper triangular unitary is diagonal, as successive column orthogonality shows. Reversing these operations factors the cube unitary into adjacent Givens rotations and one-site phases. This is the standard Givens QR factorization. Exterior powers give \(\Gamma(W_1W_2)=\Gamma(W_1)\Gamma(W_2)\). Each lifted two-mode factor is even and supported on the corresponding edge. Repeating the finite ordered list in every cube produces disjoint gates at each stage. Even operators on disjoint supports commute. ∎

**Dressed factorization (the required step of draft section 5.3; closed by the distiller).** Each dressed cube gate is an exact finite product of even gates on individual edge triples. These factors can be chosen gauge invariant. Hence the base tick has finite depth in nearest-neighbour edge-triple gates.

*Proof.* Work on the finite-dimensional Hilbert space of one cube and its twelve links. Write \(-iH_C=\sum_{j=1}^{12}X_j\), where each \(X_j\) is its skew-Hermitian dressed edge term. Let \(\mathfrak g\) be the real Lie algebra generated by these matrices, and let \(\mathsf L\) be the connected analytic matrix subgroup with Lie algebra \(\mathfrak g\), supplied by the analytic subgroup theorem. Let \(\mathsf H\) be the subgroup of finite words in \(\exp(tX_j)\), \(t\in\mathbb R\). Then \(\mathsf H\subseteq\mathsf L\).

The span \(\mathfrak v\) of all \(\operatorname{Ad}_hX_j\), \(h\in\mathsf H\), is invariant under \(\operatorname{Ad}_{\exp(tX_j)}\). Differentiating gives \([X_j,\mathfrak v]\subseteq\mathfrak v\). Hence it contains all iterated brackets of generators and contains \(\mathfrak g\). Conversely \(\mathfrak g\) is invariant under every \(\exp(t\operatorname{ad}_{X_j})\), so \(\mathfrak v\subseteq\mathfrak g\). Choose a basis \(Y_k=\operatorname{Ad}_{h_k}X_{j_k}\), \(1\leq k\leq\dim\mathfrak g\). The map
\[
 (t_1,\ldots,t_{\dim\mathfrak g})\longmapsto
 \prod_k h_k\exp(t_kX_{j_k})h_k^{-1}
\]
has derivative \((t_k)\mapsto\sum_k t_kY_k\) at zero. The inverse function theorem on the analytic group \(\mathsf L\) gives a neighbourhood of its identity contained in \(\mathsf H\). Thus \(\mathsf H\) is an open subgroup of connected \(\mathsf L\), and \(\mathsf H=\mathsf L\). In particular \(\exp(-i\theta H_C)\in\mathsf H\). Membership in \(\mathsf H\) means an exact finite word, not a Trotter limit. Every factor acts on one edge triple and is even. B4's edge calculation shows that each also commutes with every local gauge generator. Repeating the word on translated cubes produces finitely many layers. \(W_E\) already consists of disjoint link gates. ∎

**GAP: UALL (the stronger universality assertion is false as written).** The draft says edge-triple even operators generate *all* even cube operators as a Lie algebra. For cube parity \(\mathcal P_C\), every such local skew-Hermitian generator \(X\) satisfies \(\operatorname{tr}(\mathcal P_CX)=0\): at least one unused matter mode contributes \(\operatorname{tr}((-1)^n)=0\). Also \(\operatorname{tr}(\mathcal P_C[X,Y])=0\) for even \(X,Y\), by cyclicity of trace. But \(\operatorname{tr}(\mathcal P_C\,i\mathcal P_C)=i\dim\mathcal H_C\ne0\). Thus the claimed full Lie algebra is not generated. The preceding proof closes the needed factorization without that assertion or an unproved extension of Bravyi–Kitaev universality.

**Theorem A2 (free spatial covariance).** The orientation-preserving lattice isometries preserving \(V\), up to site phases, are exactly \(\mathscr G\). Even translations preserve its phases exactly. Every proper cube-centred rotation preserves each half-tick up to a common site sign gauge. The action on sites is transitive; a site's stabilizer has three elements. A diagonal translation by \(\mathbf1\), with a sublattice sign and a sign gauge, exchanges the two half-steps when \(\mu=0\). This last operation is a symmetry of the half-step schedule after shifting its time origin, not an extra commuting spatial translation of \(V\).

*Proof.* Even translations preserve both tilings and every \(\eta_i\). For \(Q\in O\), the map \(x\mapsto Qx+c_0-Qc_0\) preserves integer sites. It sends even cube centres to even cube centres. It sends an odd centre \(c_0+\mathbf1+b\) to \(c_0+Q\mathbf1+Qb\), again an odd centre since \(Q\mathbf1-\mathbf1\in2\mathbb Z^3\).

The transformed edge signs and original signs have the same face products. Their ratio has product one on every face. Fix its value at one site and define a site sign by multiplying the ratios along an edge path to that site. This is path independent: commuting adjacent coordinate steps and cancelling backtracks reduces any closed lattice path to elementary face loops. Therefore the ratio on an edge \((x,y)\) is \(d(x)d(y)\). The signed permutation \(D_dP_Q\) consequently fixes both \(R_e,R_o\), and hence both half-ticks. Rotations about other even or odd cube centres differ from these by even translations.

For exclusion, expand \(V=(\cos a_o+i\sin a_oR_o)(\cos a_e-i\sin a_eR_e)\). From \(0\) to \(2e_i\), the sole two-step path uses an even edge then an odd edge, giving modulus \(\sin a_e\sin a_o/3>0\). From a site \(t\) with \(t_i\) odd to \(t+2e_i\), this order is impossible, so the entry is zero. Diagonal conjugations cannot change these moduli. Thus no translation with an odd coordinate is a symmetry. Every orientation-preserving lattice isometry is a cube-centred rotation followed by an integer translation, so the listed group is exact within the declared class. A rotation about a site must fix the centre of its even cube; its stabilizer consists of the identity and the two turns about that body diagonal. Cube rotations move one corner to all eight corners, and even translations move those corners to all sites, proving transitivity.

Finally translation by \(\mathbf1\) swaps the tilings, with a sign correction obtained by the same face argument. Conjugation by \(D_s\) reverses both hop operators. The resulting operation sends \(V_e\) to \(e^{ia_eR_o}\) and \(V_o\) to \(e^{-ia_oR_e}\). These equal \(V_o,V_e\), respectively, exactly when \(a_e=a_o\), since \(0<a_e\leq a_o<\pi\). This is \(\mu=0\). Swapping the temporal origin exchanges the order of the layers. ∎

**Theorem A3 (event lattice).** The two-sided event set is
\[
 \mathcal E=\{(X,h)\in\mathbb Z^4:X_1\equiv X_2\equiv X_3\equiv h\pmod2\}=2D_4^*.
\]
With \(c\Delta=a\), it is similar to \(D_4\). Its shortest vectors are the sixteen \((\pm1,\pm1,\pm1,\pm1)\) and the eight \(\pm2e_j\). The time axis is parallel to the root \(2e_4\). Actual events have \(h\geq0\).

*Proof (geometric identification closed by the distiller).* The alternating centres give the parity condition. A nonzero all-even vector has squared length at least four, with equality exactly for \(\pm2e_j\). An all-odd vector has squared length at least four, with equality exactly for the sixteen sign vectors. The linear map
\[
 \Phi(v)=\tfrac12(v_1+v_2,v_1-v_2,v_3+v_4,v_3-v_4)
\]
scales squared lengths by \(1/2\). It maps \(\mathcal E\) into \(D_4\): its coordinates are integers and their sum is \(v_1+v_3\), which is even. Its inverse is \(z\mapsto(z_1+z_2,z_1-z_2,z_3+z_4,z_3-z_4)\). If \(\sum_jz_j\) is even, these four coordinates have one parity, so the inverse lies in \(\mathcal E\). This proves the similarity and the time-direction statement. The draft's literal identification of \(e_4\) as a shortest lattice vector, and of a first-tick event set with a full lattice, require these stated corrections. ∎

### 3.2 Local frames and Gauss laws

**Theorem B2 (scalar finite-range walks).** A finite-range unitary on \(\ell^2(\mathbb Z^d)\) commuting with all translations is a phase times a translation. If it also commutes up to diagonal conjugation with site rotations having no common nonzero fixed vector, it is a scalar phase.

*Proof.* Translation invariance makes the matrix a finite convolution \(W_{yx}=w_{y-x}\). Its Fourier multiplier is a Laurent polynomial \(w(z)=\sum_a w_a z^a\). Unitarity gives \(|w(z)|=1\) on the torus. Set \(w^*(z)=\sum_a\overline{w_a}z^{-a}\). Uniqueness of Fourier coefficients gives the Laurent-polynomial identity \(ww^*=1\). Order exponents lexicographically. The greatest exponent of a product of nonzero Laurent polynomials is the sum of their greatest exponents, because that extreme term cannot cancel. The greatest exponent of \(w^*\) is minus the least exponent of \(w\). Therefore the identity gives \(\max\operatorname{supp}w-\min\operatorname{supp}w=0\). There is one monomial, of coefficient modulus one. Thus \(W=e^{i\phi}T_a\). A rotation changes its support displacement to \(Qa\), while a diagonal conjugation leaves that displacement unchanged. Equality requires \(Qa=a\) for every rotation, so \(a=0\). This proves the scalar-walk result directly, without importing Meyer's classification. ∎

**Lemma B3 (one-site fermion frames).** A CAR automorphism fixing every other mode and preserving the algebra at \(x\) sends \(c_x\) to \(u c_x\) or \(v c_x^\dagger\), where the nonzero coefficient has modulus one. These transformations form \(U(1)\rtimes\mathbb Z_2\). The number-preserving subgroup is \(U(1)\).

*Proof.* Write its image as \(d=aI+b n_x+u c_x+v c_x^\dagger\). It must anticommute with both \(c_y,c_y^\dagger\) for \(y\ne x\). Its even part commutes with them, so \((aI+b n_x)c_y=(aI+b n_x)c_y^\dagger=0\). Multiplying these equalities by \(c_y^\dagger,c_y\) and adding gives \(aI+b n_x=0\). Thus \(d=u c_x+v c_x^\dagger\). Now \(d^2=uvI=0\), and \(dd^\dagger+d^\dagger d=(|u|^2+|v|^2)I=I\). Exactly one coefficient is nonzero and has modulus one. Conjugation \(c_x\leftrightarrow c_x^\dagger\) reverses a phase, giving the semidirect product. It sends \(n_x\) to \(1-n_x\), so only the phase subgroup preserves number. ∎

**Theorem B4 (Gauss conservation).** Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\). So does each oriented quantum-link plaquette monomial. Consequently the base update conserves every local gauge transformation; any product of gauge-invariant plaquette gates does also.

*Proof.* For \(\ell=(x,y)\), let \(A_\ell=c_y^\dagger J_\ell c_x\). At its source, \([n_x,A_\ell]=-A_\ell\) and \([E_\ell,A_\ell]=A_\ell\), which cancel in \([\mathcal G_x,A_\ell]\). At its target, \([n_y,A_\ell]=A_\ell\) and \([-E_\ell,A_\ell]=-A_\ell\). All other vertex generators commute. Taking adjoints proves the same for \(A_\ell^\dagger\). Linear combinations and exponentials preserve commutation. Electric squares commute with every matter number and every electric operator. In an oriented plaquette, the two incident link factors at each corner have opposite gauge weights, so their weights cancel. This argument uses \([E,J]=J\), not unitarity or mutual commutativity of the link raising operators. ∎

**Gauged covariance and B1/B1q.** Under PS-1c the base update is cell covariant, acts transitively on sites, is unitary locally, has the finite nearest-neighbour form proved above, and retains the one-site algebra \(M_2(\mathbb C)\).

*Proof.* A geometric symmetry permutes site factors and link factors. If it reverses an oriented link, conjugation by the spin rotation \(e^{-i\pi S^x}\) sends \(E\) to \(-E\) and \(J\) to \(J^\dagger\). A hopping monomial then becomes its correctly oriented monomial or its adjoint. Apply A2's site sign correction to restore the \(\eta_i\). Thus each cube Hamiltonian is sent to the Hamiltonian of the image cube. Its angle is unchanged because each tiling is preserved. The electric squares are preserved by link reversal. This proves covariance of \(U_0\). A2 supplies transitivity. Exponentials of finite Hermitian even operators are unitaries; the factorization above supplies the required gate layers. Finally \(I,c_x,c_x^\dagger,n_x\) span \(M_2(\mathbb C)\). The same covariance conclusion holds for an additional \(W_B\) if that entire layer is cell covariant. ∎

**Theorem B5(a) (site-local mode-linear frames).** The image of a compact group acting by number-preserving one-body transformations independently at each one-mode site is abelian, a subgroup of a product of \(U(1)\)'s.

*Proof.* Each one-dimensional one-body space admits only multiplication by a phase. Such transformations commute. B3 gives the same conclusion from the CAR algebra. ∎

**B5(b), retained as an unproved draft statement.** If a compact group acts on the eight modes of each even cell and each dressed half-tick gate is invariant after changing the registers on its own cube, the draft claims that the mode image is scalar \(U(1)\) per cell.

**GAP: B5(b).** A dressed gate is not \(\Gamma(u_C)\) times independent link factors. Its generator contains operator-valued hops, so the draft's one-body support argument does not apply. Its final step also assumes there are no links inside an even cell, contrary to the specified twelve internal links. Indeed the eight independent site phases, grouped as \(U(1)^8\) on a cell and compensated on their incident links as in B4, satisfy the stated gate invariance and are not scalar on the cell. Thus the scalar conclusion is false under the stated hypotheses. The draft's weaker exclusion of non-abelian cell-mixing actions still needs a proof. No such exclusion is used here. The established microscopic frame conclusion for GA1 is B5(a), namely the site-local \(U(1)\) action.

### 3.3 Transport and records

**Lemma B6 (supported couplings).** For a finite-dimensional unitary \(W\), any orthogonal resolution \((P_\xi)\) of the identity, and any density matrix, \(\Pi(p,p';\mathscr S)\) is nonempty. The projectors may have rank greater than one.

*Proof.* For a set \(A\) of outputs, let \(N^t(A)\) be the inputs having a nonzero block to an output in \(A\). Let \(P_A\) and \(P_N\) be the corresponding sums of projectors. Then \(P_AW=P_AWP_N\). For \(X=P_N\rho P_N\geq0\),
\[
 p'(A)=\operatorname{tr}((P_AW)X(P_AW)^*)
 \leq\|P_AW\|^2\operatorname{tr}X\leq p(N^t(A)).
\]
For an input set \(B\), let \(N(B)\) be its neighbouring outputs and take \(A=\Omega_\Lambda\setminus N(B)\). Then \(N^t(A)\subseteq\Omega_\Lambda\setminus B\), so the preceding inequality gives \(p(B)\leq p'(N(B))\).

Build the finite network with source-to-input capacities \(p(\xi)\), allowed input-to-output capacities two, and output-to-sink capacities \(p'(\zeta)\). A cut crossing an allowed middle edge has capacity at least two. Every other cut with input set \(B\) and output set \(D\) on the source side has \(N(B)\subseteq D\) and capacity
\(1-p(B)+p'(D)\geq1\).
The source cut has capacity one. The finite real-capacity max-flow min-cut theorem therefore gives a flow of value one. Every source and sink edge is saturated; its middle flows define the required coupling. This is the supply-demand argument of Gale/Ford–Fulkerson. ∎

**Theorem B7 (finite PS-3 selection).** On a finite union of active cubes, and on an even torus, there is exactly one least-change, greatest-entropy coupling. Its kernel carries \(p\) to \(p'\) and uses only allowed blocks.

*Proof.* B6 gives a nonempty finite-dimensional polytope of couplings. It is closed and bounded, hence compact. Cost is linear, so its minimizers form a nonempty compact convex face. Entropy is continuous, with \(0\log0=0\), and strictly concave on probability vectors because \(-t\log t\) is strictly concave on \([0,1]\). It attains its maximum on that face. Two distinct maximizers would have a midpoint of strictly greater entropy, so the maximizer is unique. Dividing its \(\xi\)-row by \(p(\xi)>0\) gives the kernel; its second marginal is \(p'\). Null rows do not affect that identity. ∎

**Support factorization.** The support for a half-layer is \(\prod_C\mathscr S_C\). For a union of active cubes its output Born marginal equals that obtained from its reduced state and its internal active gates.

*Proof.* Order the fermion modes cube by cube. Even gates and occupation projectors then give a tensor product of the cube block operators, with identity factors for unused links. A tensor product of finite matrices is nonzero exactly when every factor is nonzero. External active gates commute with every observable in the region and cancel from its evolved expectation. Finally a subsequent link-only unitary \(W_L\) commutes with every matter projector, giving
\(P_\zeta W_LM_oP_\xi=W_LP_\zeta M_oP_\xi\).
It preserves whether this block is zero and leaves the matter marginal unchanged. This justifies the electric placement in PS-3h. The same observation applies to a supplied link-only \(W_B\); no occupation move is inserted for that layer. ∎

**Theorem B8 (perfect copies in a quasi-free state).** For distinct sites in a globally number-invariant quasi-free state with covariance \(G\),
\[
 \omega_G(D_{xy})=0
 \quad\Longleftrightarrow\quad
 G_{xy}=0\ \text{ and }\ (G_{xx},G_{yy})\in\{(0,0),(1,1)\}.
\]

*Proof.* Wick's determinant rule gives \(\omega_G(n_xn_y)=G_{xx}G_{yy}-|G_{xy}|^2\). Since \(n_x,n_y\) are commuting projections,
\[
 \omega_G(D_{xy})=G_{xx}(1-G_{yy})+G_{yy}(1-G_{xx})+2|G_{xy}|^2.
\]
Each summand is nonnegative because \(0\leq G\leq I\). Vanishing forces the off-diagonal entry to vanish. The first two summands vanish together exactly for the two stated diagonal pairs. Conversely those conditions give zero. ∎

**Corollary B8a.** Under the free tick and PS-3c, starting from the free sea, no record forms.

*Proof.* B10 proves stationarity and \(P_{xx}=1/2\). B8 then excludes every perfect copy at every full tick. Hence every \(F_n\) is empty. ∎

**Theorem B8b (record witnesses for the base law; under PS-3c and PS-4).** Let \(\mathbb Q\) be any history measure whose one-time marginals are the \(\nu_h\) (B7 on closed finite systems; E5 at infinite volume). (i) If an even product initial state has empty matter throughout the side-seven cube centred at \(x\), then tick one has perfect empty copies at \(x\) and its six neighbours. (ii) Supplied initial states can give a tick-one record at \(x\) with the two values equally likely.

*Proof (the locality and parity steps are closed by the distiller).* For (i), trace the seven output occupations backwards through the odd and even cube layers. Each layer expands each coordinate of their support by at most one; the union lies within supremum distance three of \(x\). In the earliest layer, every ancestor cube relevant to these outputs has empty matter on all its sites. Its dressed hops annihilate that matter subspace, independently of its links. Those sites remain empty. The same argument on the next layer keeps the output sites empty. The electric layer commutes with occupations. Thus all seven output occupations vanish with probability one, so the required copy expectations vanish. This uses the backward gate cone, not conservation of the number in an arbitrary region with boundary.

For (ii), choose six distinct sites with \(y,z\in N(x)\), and the vector
\[
 |\psi\rangle=2^{-1/2}(|111\rangle_{xyz}|000\rangle_{abc}
                       +|000\rangle_{xyz}|111\rangle_{abc}).
\]
Both branches have three particles. The vector has odd parity; its rank-one density matrix is parity invariant and hence an even state. Extend it by even states on the remaining factors. In this output state \(n_x=n_y=n_z\) with probability one and \(\omega_\psi(n_x)=1/2\). Supply \(\omega_0=\omega_\psi\circ\alpha^{-1}\); E1 makes this a state whose tick-one image is \(\omega_\psi\). Initialize no records. The copy test then forms a record at \(x\). Its value is \(r_x=\xi_2(x)\), and \(\mathbb Q(\xi_2(x)=1)=\nu_2(\xi_x=1)=\omega_\psi(n_x)=1/2\) because the one-time marginals of \(\mathbb Q\) are the \(\nu_h\) (referee closure, pass 3). ∎

**Theorem B9, established clauses (under PS-3c).** Let \(\mathbb Q\) be any history measure whose one-time marginals are the \(\nu_h\) (B7; E5, which builds \(\mathbb Q\) before citing B9, so the citation is not circular). Given a copy neighbour \(y\) at a formation time, the locked value has distribution
\[
 \mathbb Q(r_x=v)=\varrho_n\bigl(n_y^v(1-n_y)^{1-v}\bigr),\qquad v\in\{0,1\}.
\]
All copy neighbours give the same distribution. This distribution varies between the all-empty and all-occupied states. The copy test is equivariant under shell-preserving lattice maps. Records are single and permanent, and their values have positive one-site Born weight almost surely.

*Proof.* \(D_{xy}\) is the occupation-disagreement projector. Then \(\mathbb Q(\xi_{2n}(x)\neq\xi_{2n}(y))=\nu_{2n}(\xi_x\neq\xi_y)=\varrho_n(D_{xy})=0\), so \(\xi_{2n}(x)=\xi_{2n}(y)\) almost surely. This proves the displayed identity and agreement between copy neighbours. Formation times, including prior non-formation, are deterministic functions of the state sequence, so conditioning on formation at such a site adds no random constraint on \(\xi\). Empty and occupied states give different probabilities and satisfy the copy condition. The definition quantifies over all unordered pairs of neighbours, so commutes with geometric permutations. Each site is assigned a value once, at \(t_x\), and that stored value is never overwritten. A zero-weight one-site value occurs with probability zero by the Born marginal. There are countably many sites and times, so these assertions hold simultaneously almost surely. Readout is the stored value by definition. ∎

**GAP: LW1-i/B9 (shell-only Admissibility).** The asserted dependence on the *unannotated six-site reduced state alone* does not follow and is false on the supplied domain. To see the exact defect, label four shell sites \(y_1,\ldots,y_4\). Take a diagonal shell state with \((y_1,y_2)=(b,b)\), \((y_3,y_4)=(1-b,1-b)\), the last two shell sites fixed empty, and \(\mathbb P(b=1)=1/3\). Extend this same shell state in one case by \(\xi_x=b\), and in a second by \(\xi_x=1-b\). Both extensions are even diagonal states. Both pass the two-copy test, using different neighbour pairs. Their centre probabilities are \(1/3\) and \(2/3\). They have identical shell density matrices. Each can be supplied as a tick-one state by pulling it back through \(\alpha^{-1}\), as in B8b. Thus no function of that shell density matrix alone gives both locked-value laws. The draft's argument supplies a copy neighbour from the centre–shell joint state and then treats it as shell data. The established clauses above do not settle LW1-i.

### 3.4 The free sea, probability-one statements and dispersion

**Theorem B10 (free sea).** For \(0\leq\mu<2\varepsilon<\pi\):

1. The Bloch eigenvalues are \(e^{\pm iw(K)}\), with
   \(\cos w(K)=a_{\rm band}\chi(K)-b_{\rm band}\) and \(\mu\leq w(K)\leq2\varepsilon\).
   Each sign has multiplicity four away from a coincident eigenvalue.
2. The negative-arc projection obeys \(\Theta P\Theta^{-1}=I-P\) and \(P_{xx}=1/2\).
3. \(\omega_P\) is a pure, stationary, \(\mathscr G\)-invariant, half-filled state of the infinite CAR algebra.
4. If \(\mu>0\), \(|P_{xy}|\leq C e^{-\kappa_{\rm dec}|x-y|}\) for some \(C,\kappa_{\rm dec}>0\).

*Proof.* First,
\[
 R_eR_o+R_oR_e=\tfrac13\sum_{i=1}^3(T_{2e_i}+T_{-2e_i}).
\]
To verify the identity, expand each matrix entry as two-step paths. A return path would use the same edge in both tilings, which A1 excludes. For two different axes, either neither path around the corresponding face has the required opposite-tiling order, or both orders occur. Their amplitudes cancel because the face sign product is \(-1\). This applies with either sign of either coordinate step. For a straight displacement \(\pm2e_i\), the edges have opposite ownership and exactly one ordering occurs. Its sign product is one, since \(\eta_i\) is independent of \(x_i\). Its amplitude is \(1/3\). These are all two-step possibilities. On a Bloch fibre the identity becomes \(\{R_e(K),R_o(K)\}=2\chi(K)I\).

Using the involutions of A1, expand the tick and its adjoint to obtain
\[
 V(K)+V(K)^*=2\cos a_e\cos a_o\,I
             +\sin a_e\sin a_o\{R_e(K),R_o(K)\}.
\]
Thus every eigenvalue has real part
\(\cos a_e\cos a_o+\sin a_e\sin a_o\,\chi=a_{\rm band}\chi-b_{\rm band}\).
Here \(a_{\rm band}>0\), and \(\chi\) ranges over \([-1,1]\). The extreme real parts are \(\cos2\varepsilon\) and \(\cos\mu\), proving the energy interval. There is a gap at \(\pi\); there is also one at zero when \(\mu>0\). When \(\mu=0\), zero occurs only at \(K=0\).

Both fibre hop matrices have trace zero, so \(\det V(K)=1\). For a point where \(w(K)/\pi\) is irrational, this forces equal multiplicities of \(e^{iw}\) and \(e^{-iw}\), hence four each. Such a point exists because the energy is a nonconstant continuous function of \(K\). Multiplicities are locally constant where the eigenvalues are distinct. The torus is connected for \(\mu>0\), and its complement of \(K=0\) is connected for \(\mu=0\). The multiplicities follow everywhere they are distinct. At the massless zero fibre \(V(K)=I\); its single point has zero Lebesgue measure in the infinite-volume Bloch integral. It therefore contributes no spectral projection on \(\ell^2(\mathbb Z^3)\).

Each \(R_T\) is real and satisfies \(D_sR_TD_s=-R_T\). Complex conjugation reverses the signs in its exponential, and \(D_s\) reverses them back. Hence \(\Theta V\Theta^{-1}=V\). Because \(\Theta\) is antiunitary, it exchanges the two quasi-energy signs. There is no spectral subspace at the cuts, by the preceding paragraph. Thus \(\Theta P\Theta^{-1}=I-P\). Taking a diagonal entry gives \(P_{xx}=1-P_{xx}\).

The standard CAR quasi-free-state theorem (Powers–Størmer/Araki) supplies the state for \(0\leq P\leq I\), and its purity criterion says it is pure exactly when its covariance is a projection. Here \(P^2=P=P^*\). Since \(P\) commutes with \(V\), its evolved covariance is \(VPV^*=P\). Wick's determinant rule then proves stationarity of every moment, and density of local polynomials proves stationarity of the state. A2's lifted symmetries commute with \(V\) and hence with its spectral projection; the same moment argument proves their invariance. Half filling is the diagonal identity above.

For the last clause, choose a finite contour enclosing the negative spectral arc and excluding the positive arc. When \(\mu>0\), its Euclidean distance \(\delta\) from the spectrum is strictly positive. Normality gives \(\|(z-V)^{-1}\|\leq\delta^{-1}\) there. Here is the finite-range Combes–Thomas argument with its hypotheses explicit. Fix \(y\), set \(f_N(x)=\min(|x-y|,N)\), and conjugate by the bounded invertible diagonal operator \(e^{t f_N}\). The matrix \(V\) has fixed finite range and uniformly bounded row and column sums. Since \(f_N\) is one-Lipschitz, the Schur bound gives
\[
 \|e^{t f_N}Ve^{-t f_N}-V\|\leq c_{\rm range}(e^{tr}-1)
\]
for a fixed range \(r\) and a constant \(c_{\rm range}\), uniformly in \(N,y\). Choose \(t>0\) to make this less than \(\delta/2\). The resolvent identity and Neumann series give norm at most \(2/\delta\) for the conjugated resolvent. Its \((x,y)\) entry is \(e^{t f_N(x)}(z-V)^{-1}_{xy}\), so letting \(N\to\infty\) gives exponential decay uniformly on the contour. The Riesz formula
\(P=(2\pi i)^{-1}\oint(z-V)^{-1}\,dz\)
gives the claimed bound. This closes the draft's unsupported conversion of an angular gap into a resolvent-distance bound. ∎

**Theorem B11 (probability-one consistency).** No atomless history law admits a realized history satisfying every measurable probability-one statement. The free sea's Born measure is atomless, as is the tracial state's Born measure. The fixed list in FINAL PS-11c is countable and is consistent with any supplied history law.

*Proof.* If every singleton history has probability zero, each complement of a singleton has probability one. Their intersection is empty. For the free sea, take any fixed configuration. It has infinitely many occupied sites or infinitely many empty sites. For a finite set \(F\) chosen from the former, Wick's rule and Hadamard's determinant inequality give
\[
 \nu_{\omega_P}(\xi_x=1\ \forall x\in F)=\det P_F
 \leq\prod_{x\in F}P_{xx}=2^{-|F|}.
\]
For a set of empty sites the same computation uses \(I-P\). Letting \(|F|\) grow proves that every singleton has probability zero. The normalized trace on the finite local matter-and-link algebras is compatible under inclusions and yields the infinite tracial state. On matter its occupation measure is the independent fair-bit measure, also atomless. Each local unitary preserves this trace, so the tracial state is stationary for the base update. A history singleton is contained in its initial-configuration singleton; an atomless initial marginal therefore implies an atomless history measure.

There are countably many finite site/tick sets. Each has a finite occupation-and-record alphabet and finitely many events. Pairing these events with two rational numbers still gives a countable list. The frequency-convergence events are measurable, since convergence of a sequence of finite cylinder averages to a value in a closed interval can be expressed using countable unions and intersections of inequalities. Intersect only those listed statements assigned probability one by the law. Countable subadditivity gives an intersection of probability one, hence a nonempty set of possible realized histories. This proves consistency, not that any listed frequency limit actually exists. ∎

**Theorem C1 (free massless dispersion).** For \(\mu=0\) and \(k\downarrow0\),
\[
 w(k\widehat n)=\frac{s_\varepsilon k}{\sqrt3}
 \left[1+k^2\left(\frac{s_\varepsilon^2}{72}-\frac{T_4(\widehat n)}{24}\right)+O(k^4)\right].
\]
The relative phase-velocity correction contains the direction-dependent term \(-T_4(\widehat n)k^2/24\), or \(-T_4(\widehat n)|q|^2/6\) in site momentum. This is the draft's tree-level dimension-six term.

*Proof.* B10 gives \(1-\cos w=s_\varepsilon^2(1-\chi)\). Taylor's theorem gives
\[
 1-\chi(k\widehat n)=\frac{k^2}{6}-\frac{k^4T_4(\widehat n)}{72}+O(k^6),\quad
 1-\cos w=\frac{w^2}{2}-\frac{w^4}{24}+O(w^6).
\]
The analytic function \(z\mapsto1-\cos\sqrt z\) has derivative \(1/2\) at zero. The inverse function theorem therefore makes \(w^2\) analytic in \(k^2\) near zero and gives \(w^2=s_\varepsilon^2k^2/3+O(k^4)\). Substitution and coefficient comparison yield
\[
 w^2=\frac{s_\varepsilon^2k^2}{3}
       +k^4\left(\frac{s_\varepsilon^4}{108}
                  -\frac{s_\varepsilon^2T_4(\widehat n)}{36}\right)+O(k^6).
\]
Taking the positive square root proves the formula. Since \(s_\varepsilon>0\), this step is valid. \(T_4\) equals one on an axis and \(1/3\) on a body diagonal, so the direction dependence is nonconstant throughout the parameter window. Finally \(K=2q\) gives the site-unit coefficient. ∎

**Theorem B12 (scope of the D4 obstruction).** A symmetry of an ordered PS-1 update that maps each time slice to a time slice cannot move the time root off its line. For an oriented forward time direction it must fix that direction. The event-lattice stabilizer of the oriented root has 48 elements. Thus full \(W(F_4)\), which moves the chosen root to nonparallel roots, is not a symmetry of the ordered tick data.

*Proof.* A slice is the intersection of the event lattice with a hyperplane orthogonal to the time root. Its differences span that three-dimensional hyperplane. If an orthogonal transformation moves the root to a nonparallel vector, it maps that hyperplane to a different one. The image slice then contains events with different original time coordinates and cannot be a single original slice. Preserving forward orientation additionally excludes root reversal. Swapping coordinates one and four preserves the event lattice and its nearest vectors but moves the time root to a nonparallel root, exhibiting the conflict with the full Euclidean symmetry. An orthogonal lattice symmetry fixing \(e_4\) must permute the six shortest vectors orthogonal to it, \(\{\pm2e_i:1\leq i\leq3\}\). It therefore acts as a signed spatial coordinate permutation. All \(2^3\cdot3!=48\) such permutations preserve the lattice and fix \(e_4\). This also corrects the draft's conflation of the root stabilizer with the line stabilizer: allowing time reversal doubles the latter to 96 (closed by the distiller). ∎

**GAP: B12(ii–iii).** The draft supplies no scalar transfer kernel and no fermionic positivity argument. Exponential locality does not imply failure of finite range: a finite-range operator is also exponentially local. To prove the draft's scalar assertion one must exhibit nonzero tails of the relevant reconstructed real-time update, or another obstruction to finite depth. To prove its fermion assertion one must give the stated failure of positive slice reconstruction. Quotations reporting these results do not provide the full proofs required here. A positive OS transfer is itself unitary only if it is the identity, by the spectral theorem, but this alone says nothing about finite depth of a real-time unitary reconstructed from it.

The cube tick is the selected law because it supplies the explicit update and actuality construction above. The D4 candidate as specified is a Euclidean weight, not a specified PS-1 gate update; the proved part of B12 restricts its time-slice symmetry, while the draft's stronger transfer exclusions remain the named gaps. This choice asserts no classification of possible laws.

### 3.5 Infinite volume

**Theorem E1 (quasi-local update).** Each base layer and their tick composition define automorphisms of \(\mathfrak A\). They fix every \(e^{it\mathcal G_x}\). A supplied finite-depth layer of finite-support gauge-invariant plaquette gates has the same properties, provided each of its sublayers consists of pairwise commuting gates (GA1-P shows that quantum-link plaquette terms on a shared link do not commute).

*Proof.* Consider a layer of locally finite, commuting, even gates \(g_j\) with supports \(X_j\). For \(A\) supported on finite \(F\), define
\[
 \beta(A)=\left(\prod_{X_j\cap F\ne\varnothing}g_j^*\right)
              A
           \left(\prod_{X_j\cap F\ne\varnothing}g_j\right).
\]
There are finitely many factors. A further gate disjoint from \(F\) commutes with \(A\), by evenness, and with the listed gates. Including it changes nothing. Given two local observables, use the finite union of their gate lists. Finite-unitary conjugation then proves linearity, multiplicativity, preservation of adjoints, and norm preservation. Using \(g_j^*\) instead of \(g_j\) gives its inverse; any extra gates meeting the enlarged support still cancel by the same commutation argument. Continuity extends this isometric automorphism to the norm completion. Cube layers have disjoint supports by A1; the electric layer has disjoint links. Composition defines \(\alpha\). B4 implies that every relevant gate commutes with each local gauge exponential, so it is fixed. A finite circuit of other local gauge-invariant layers is handled by the same construction layer by layer. ∎

**Theorem E2a (free infinite-volume vacuum).** For \(\mu>0\), the free sea is pure, stationary, cell symmetric, exactly half filled and has exponentially decaying two-point function. For \(\mu=0\), the state properties persist and \(|P_{xy}|\leq C/(1+|x-y|)\) for some \(C\). The last assertion is a power-decay bound, not a claimed sharp asymptotic.

*Proof.* B10 proves the state properties and the positive-mass bound. **GAP: E2a-0, closed by the distiller:** the draft did not prove its massless decay statement. Here is a direct bound. At \(\mu=0\), set \(g(K)=\cos w(K)=1-s_\varepsilon^2(1-\chi(K))\). For \(K\ne0\), spectral calculus gives
\[
 P(K)=\tfrac12\left[I+\frac{V(K)-V(K)^*}{2i\sqrt{1-g(K)^2}}\right].
\]
The numerator is an analytic matrix function vanishing at zero, since \(V(0)=I\). It is \(O(|K|)\), and its first derivatives are bounded. Taylor's theorem gives \(1-g(K)^2\asymp|K|^2\) near zero and first derivatives \(O(|K|)\). Its positive square root is therefore comparable to \(|K|\), with bounded first derivatives off zero. The quotient rule proves \(\|\partial_jP(K)\|\leq C_1/|K|\) near zero. Away from zero all symbols are smooth, because \(w(K)<\pi\). These first derivatives are integrable in three dimensions.

Since \(\|P(K)\|\leq1\), integration by parts on the torus with a radius-\(r\) ball removed has a boundary term bounded by a constant times \(r^2\), which tends to zero. Thus the integrable classical derivatives are also weak derivatives. For any nonzero cell separation \(d\), choose \(j\) with \(|d_j|\geq|d|/\sqrt3\). Integration by parts in the Fourier coefficient then bounds each matrix entry by \((2\pi)^{-3}\|\partial_jP\|_{L^1}/|d_j|\). The finitely many residue pairs convert this to \(|P_{xy}|\leq C/(1+|x-y|)\); bounded matrix entries cover zero cell separation. This establishes the draft's massless power-decay claim as an explicit bound. ∎

**Theorem E2b (stationary gauge-invariant half-filled states of the gauged law).** Suppose \(\omega\) is cell-translation invariant, locally gauge invariant and half filled in cell average. Every weak-* limit point of
\[
 \omega^{(N)}=\frac1N\sum_{j=0}^{N-1}\omega\circ\alpha^j
\]
is stationary, cell-translation invariant, locally gauge invariant and half filled in cell average. Cube-rotation invariance also passes to the limit when present initially. Such initial states and stationary limits exist. With transitive spatial invariance, half filling holds at every site. This holds for \(U_0\), and conditionally for a cell-covariant, gauge-invariant finite circuit \(W_B\) acting only on links.

*Proof.* The state space is weak-* compact by Banach–Alaoglu. This algebra is separable, being generated by countably many finite-dimensional local algebras, so sequences have weak-* convergent subsequences. For any \(A\),
\[
 |\omega^{(N)}(\alpha(A))-\omega^{(N)}(A)|
 =N^{-1}|\omega(\alpha^N(A))-\omega(A)|\leq2\|A\|/N.
\]
Thus every limit is stationary. The covariance proof following B4 shows that the spatial actions commute with \(\alpha\); B4/E1 give the same for local gauge conjugations. These invariances persist in each mean and in its limit.

For half filling, a dressed cube gate conserves the sum of the matter occupations in that cube: each hop removes one particle and adds one. In a cell-translation-invariant state, every translated length-two cube has the same total expected occupation, since it contains one representative of each residue class modulo two. The even half-layer preserves this total on even cubes; the odd half-layer preserves it on odd cubes. Each intermediate state is cell-translation invariant, so the common total, hence the cell density, is preserved through both. The electric layer and any link-only \(W_B\) commute with each \(n_x\). The density is a finite local expectation and passes to limits. Transitive spatial invariance makes all site expectations equal to that density.

For existence, use the compatible normalized traces on all finite matter-and-link algebras. Their state is invariant under local gauge conjugations and spatial permutations and has \(\omega(n_x)=1/2\). The local construction of E1 shows it is already stationary. It is an explicit witness for the asserted nonempty class. Neither this witness nor Cesàro averaging selects VC1's vacuum. ∎

**Theorem E3 (formation at infinite volume; under PS-3c).** For every initial state, \(F_n\), \(\mathcal R_n\) and \(t_x\) are well defined. They depend on the state sequence, not its realized history. Record sets increase and start empty. Any spatial symmetry preserving the initial state and commuting with the tick preserves these sets.

*Proof.* Each \(D_{xy}+D_{xz}\) is a positive observable supported on three sites. Its expectation in \(\varrho_n\) exists by E1. Testing the finitely many neighbour pairs defines whether each site belongs to \(F_n\). The recursion defines an increasing record set; taking the first positive integer with membership defines \(t_x\). Every operation is deterministic in \(\omega_0\). Under a symmetry the copy observable maps to the corresponding observable at the image sites, with the same expectation. Induction on \(n\) proves covariance of the sets. ∎

**Theorem E4 (supported infinite-volume couplings; under PS-3h).** For every state and one half-step there is a coupling of its input and output Born measures satisfying every active-cube support almost surely. If the state is cell-translation invariant, the coupling can be so chosen.

*Proof.* Choose increasing finite unions of active cubes \(\Lambda_m\) exhausting the lattice. The support factorization and local marginal identity after B7 allow B6 to be applied to the reduced state on each union, including its used links. This gives a finite coupling \(\gamma_m\) with the correct marginal restrictions and cube supports. Extend it to the full pair-configuration space by an arbitrary product distribution on the remaining pair coordinates. This extension need not have the full correct marginals; every fixed marginal becomes correct once its support lies in \(\Lambda_m\).

The pair-configuration space is compact metrizable. Probability measures on it are weakly sequentially compact, by the compact-space case of Prokhorov's theorem. Choose a subsequential limit \(\gamma\). Every cylinder indicator is continuous, so each finite marginal constraint passes to the limit. The violation of a given cube support is also a cylinder event; its probability is eventually zero. The limit therefore has the required marginals and has zero probability of any cube-support violation. The countable union over cubes still has probability zero.

For invariance, average the translates of \(\gamma\) over growing cell boxes. Marginals and support constraints persist because both are invariant under cell translations. A fixed translation changes these averages in total variation by at most the relative size of the box's symmetric difference with its translate, which tends to zero. A weak limit point of the averages is therefore invariant and retains all constraints. This is the Følner averaging argument. ∎

**Theorem E5 (supported actual histories).** For every \(\omega_0\), there is a Markov history measure with Born marginal \(\nu_h\) at each half-time and with each step satisfying its active-cube support. Odds never depend on records. The first-record rule gives single permanent records with almost surely admissible one-site values and no records at tick zero. If every state in the sequence is cell invariant, every step may additionally be selected from \(\mathcal O_h\).

*Proof.* Choose a coupling \(\gamma_h\) for each consecutive pair using E4. The configuration space is standard Borel, so the disintegration theorem supplies a measurable probability kernel \(\mathsf K_h\) satisfying
\(\gamma_h(d\xi,d\zeta)=\nu_h(d\xi)\mathsf K_h(\xi,d\zeta)\).
Complete its null-input values arbitrarily. Ionescu–Tulcea's theorem supplies a unique Markov measure for the supplied initial marginal and this sequence of kernels. Inductively, if its time-\(h\) marginal is \(\nu_h\), its next marginal is \(\nu_h\mathsf K_h=\nu_{h+1}\). Thus its pair marginal is \(\gamma_h\), proving the support condition. Countably many steps and cubes permit the conditions to hold simultaneously almost surely.

The quantum state sequence is defined without records. E3 defines the first-record times; the history assigns their contents. B9's established record clauses prove permanence, uniqueness of the stored value and its positive one-site Born weight almost surely. This invokes no shell-only Admissibility claim. PS-4 is the imposed empty initial record set. Finally E6 proves \(\mathcal O_h\ne\varnothing\) for invariant states, so those couplings can be used in the same construction. The uniqueness in Ionescu–Tulcea is conditional on the chosen kernels and is not LW1-U. ∎

**Theorem E6 (invariant PS-3 optimizers exist).** For cell-invariant input state, \(\mathcal O_h\) is a nonempty compact convex set.

*Proof.* E4 gives \(\mathcal C_h\ne\varnothing\). The marginal identities, translation identities and zero probabilities of the clopen support violations are closed conditions on measures on a compact space. Hence \(\mathcal C_h\) is compact; it is convex by linearity of those conditions. Cost is a continuous affine cylinder expectation. Its minimizers form a nonempty compact convex face \(\mathcal M_h\).

Partition the dyadic cell box \(Q_{m+1}\) into eight translates of \(Q_m\). Shannon entropy subadditivity and translation invariance give
\(\mathsf H_{Q_{m+1}}\leq8\mathsf H_{Q_m}\).
Thus the normalized entropies decrease and are bounded below by zero. Their limit is their infimum, which defines \(s\). Each finite entropy is continuous in the cylinder probabilities. An infimum of continuous functions is upper semicontinuous, so \(s\) is upper semicontinuous.

For invariant measures \(\gamma_1,\gamma_2\) and \(0<t<1\), entropy concavity and the entropy chain rule with a binary mixture label give
\[
 t\mathsf H_{Q_m}(\gamma_1)+(1-t)\mathsf H_{Q_m}(\gamma_2)
 \leq \mathsf H_{Q_m}(t\gamma_1+(1-t)\gamma_2)
 \leq t\mathsf H_{Q_m}(\gamma_1)+(1-t)\mathsf H_{Q_m}(\gamma_2)+\log2.
\]
Divide by \(|Q_m|\) and take limits. The result is affinity of \(s\). Upper semicontinuity gives an attained maximum on compact \(\mathcal M_h\), with a closed set of maximizers. Affinity makes that set convex. This is exactly \(\mathcal O_h\). ∎

## 4. Open statements and failed proof steps

**Lemma LW1-U (OPEN).** For the cube tick, PS-3h and a \(2\mathbb Z^3\)-invariant state \(\omega_h\), the set \(\mathcal O_h\) of E6 has exactly one element, and it is the local limit of the unique torus transports of B7 on tori of even side \(L\to\infty\) with states converging locally to \(\omega_h\).

**As stated, LW1-U is false.** `LW1U_DRAFT.md` (pass 1, Theorem 4.3, not yet distilled or refereed) gives an ergodic, non-factor, \(2\mathbb Z^3\)-invariant state of the free cube tick for which \(\mathcal O_h\) is a segment. The open statements are LW1-U_f (the same lemma for invariant factor states) and its case LW1-U_sea (the free sea with \(0<\mu<2\varepsilon<\pi\), both half-ticks; `LW1U_DRAFT.md` section 10). The same draft proves uniqueness when both Born laws are independent across cubes given the shared cube-number field (Theorem 10.2). Choosing a rule for non-factor states (PS-3m, or a set-valued transport there) is an owner decision. The free sea and its half-step images are examples of the invariant state premise for the free tick. They are not declared vacua of the gauged tick. The statement retains both the uniqueness and torus-limit obligations; E6 proves neither.

- **Attack 1 — finite entropy strictness fails:** specific entropy is affine by E6, since the mixture's extra entropy is at most \(\log2\) per box and vanishes per cell.
- **Attack 2 — torus limits fail to establish selection:** no recovery sequence has been constructed that matches the exact torus Born marginals while preserving the allowed cube supports and approaching both variational optima; invariant limit points also require justified invariance of the approximants.
- **Attack 3 — a local Gibbs dual is missing:** the free sea's determinantal marginals have no supplied summable-potential representation for the dual variables, and no uniform Dobrushin-type uniqueness bound is supplied as the change penalty tends to infinity.

**LW1-edge (required factorization, CLOSED).** For each finite-spin cube and real angle \(\theta\), \(e^{-i\theta H_C}\) is a finite product of gauge-invariant even edge-triple gates. Section 3.1 proves this using the analytic subgroup theorem and the inverse function theorem. **GAP: UALL** concerns only the draft's stronger, false assertion that these local operators generate every even cube operator; the parity-trace obstruction there specifies its failure. No universality lemma is assumed in the law's nearest-neighbour proof.

**GA1-P (OPEN plaquette law input).** Specify a quantum-link plaquette gate class, its free constants and its ordering or other construction. Prove that the resulting full layer is gauge invariant, cell covariant and implementable in finitely many allowed nearest-neighbour layers. Nothing here requires that such a class be present or absent.

The obstruction actually available is noncommutation, not nonexistence of a covariant construction. For two plaquettes sharing just one link, choose loop orientations so their monomials are \(J_\ell A\) and \(J_\ell B\); \(A,B\) act on disjoint other links. Their Hermitian terms satisfy
\[
 [B_p,B_q]=2E_\ell(AB^\dagger-A^\dagger B).
\]
This follows by expanding the commutator, using \([J_\ell,J_\ell^\dagger]=2E_\ell\), and commuting all disjoint factors. It is nonzero for \(S\geq1/2\): choose the other links at extremal weights so \(AB^\dagger\) acts nontrivially while \(A^\dagger B\) annihilates, and choose a nonzero \(E_\ell\) eigenvalue. Thus a product over these terms cannot be treated as an unordered commuting layer. The draft supplied no rotation-covariant ordering; it proved no ban on other constructions.

**GAP: LW1-i/B9 (OPEN admissibility input).** Establish a well-defined function of the permitted nearest-neighbour conditions that gives the locked-value law whenever formation occurs. With those conditions defined as the unannotated shell density matrix, the assertion is false by section 3.3. A revised reading or a restricted state domain would be additional supplied data; neither is adopted here.

**GAP: LW1-ii/F (OPEN finite-box consistency).** For each finite \(\Lambda\subseteq\Lambda'\), supply the finite-box dynamics, boundary prescription and history measures \(\mathbb Q_\Lambda\), and prove
\[
 (\operatorname{res}_{\Lambda'\to\Lambda})_*\mathbb Q_{\Lambda'}=\mathbb Q_\Lambda,
\]
with the stated PS-3 selection in each box. **In the closed-box reading this identity is false** (referee closure, pass 3, `LW1_REFEREE.md` section 3.G): a state in which one particle sits at a site of \(\Lambda\) whose odd cube crosses into \(\Lambda'\setminus\Lambda\) leaves \(\Lambda\) with probability \(\sin^2(a_o/\sqrt3)>0\) in \(\Lambda'\), while \(N_\Lambda\) is conserved in the closed box \(\Lambda\). One-time Born marginals do not depend on the transport, so no choice of Act repairs it. In the marginal reading (restrictions of one infinite history) it holds by E5. So target item 3 needs an owner reading, not a proof. The draft specifies no such boundary prescription. A closed finite system omits exterior gates, whereas a restriction of an infinite system includes their incoming effects. E1 gives local dynamical agreement when the full backward gate cone fits inside a finite system. E5 supplies infinite histories whose restrictions are automatically consistent. Neither fact proves the displayed identity for independently evolved and optimized closed boxes. The target is not silently replaced by infinite-volume existence.

**GAP: B5(b) (OPEN cell-frame classification).** Determine the image of compact mode-linear frame groups on an even cell under the stated invariance of every dressed cube gate. The claimed scalar conclusion is false with internal link transformations, by section 3.2. Whether the remaining hypotheses exclude every non-abelian mode image is unproved. B3 and B5(a) establish only the site-local classification used here.

**GAP: B12(ii) (OPEN scalar transfer assertion).** For the D4 weight quoted by the draft, define the scalar real-time update reconstructed along the time root and prove that it cannot be a finite-depth nearest-neighbour circuit. Exponential locality alone does not prove this.

**GAP: B12(iii) (OPEN fermion transfer assertion).** For that weight's stated fermion kernel, prove the claimed absence of a positive slice Hilbert-space reconstruction. The permitted text supplies a reported verdict, not the kernel or the proof. The foliation argument of B12 does not establish this assertion.

**GAP: LW1-N (OPEN non-invariant selection).** Define and prove existence and uniqueness of the infinite-volume least-change, greatest-entropy transport on the law's supplied non-cell-invariant initial states and their images. The per-site cost and specific entropy selection in E6 was defined only on invariant couplings. E5 supplies supported histories for arbitrary states but does not make those histories PS-3 optimizers.

**GAP: LW1-R (OPEN formation domain).** Specify the law-admissible initial-state domain on which the axiom that records form is required, and prove formation on that domain. B8b gives witnesses, not a result for all supplied states. In particular, the gauged tracial state of E2b is stationary and has independent fair occupations, so \(\varrho_n(D_{xy})=1/2\) for distinct sites at every tick. It forms no records under PS-3c. The free sea likewise forms none by B8a. An unrestricted domain therefore cannot guarantee formation for every initial state.

**VC1 (OPEN vacuum input).** Construct and specify the gauged vacuum from the free sea under FINAL PS-7r, for the same chosen gate classes and constants. E2b proves existence of stationary gauge-invariant half-filled states, not their uniqueness, a sea-continuation property, purity, or a vacuum selection.
