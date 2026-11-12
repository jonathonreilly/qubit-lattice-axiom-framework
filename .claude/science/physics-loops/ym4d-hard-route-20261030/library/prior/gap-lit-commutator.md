## Repo search

The lead's row-778 search in library/gap-vortex-astra.md found earlier
soft-route literature on vortex free energies (especially
checks/review_massgap_block_literature.md:112–121, which identifies a missing
common endpoint for twisted and untwisted ratios) and the local Wilson witness
in PR 10114's MASS_GAP_LOCAL_BLOCK_ASTRA.md:89–166. That witness, also used
by library/gap-fusion-astra.md, proves a positive one-step elementary-loop
correlation lower bound from local conditional Haar comparison. It is a
nearby conditional-measure method, but it has no random-commutator averaging,
twist comparison, or bound on the electric parity trace in (16). The
Ito–Seiler discussion is a caution about a proposed decimation interpolation,
not a no-go theorem for other non-Abelian methods. I read and credit these
passages; I do not repeat their proof.

I searched target terms outside this lane on origin/main, pr/10114, pr/10133,
pr/10134, pr/10141, and pr/10144, at respectively a527a6f, f76f6c6,
89faef2, 1e70c72, fb99b4d, and 296c6f2. The only scoped hit was pr/10134's
unrelated use of “(CF)” in gates/field-tier-upper-chain-c3242879df.md:212.
No other ref supplied a commutator-word estimate or a vortex/centre-odd
bound. The lane's row-778 search found no open-registry owner for the
twist-bound target. These are bounded searches, not proofs that no
differently named result exists.


# Literature on random commutators and the vortex comparison

Research reading for FINISH row 781 at repository commit
f0dd509a2f020b98b4b61d389817bde1d5322127. This is not an audit, proof,
or status change. Literature statements are separated from row 778's new
argument. No computer calculation was used; any simulation result below is
GUIDE only.
## Question and answer

**I found no published use of Haar-random commutator averaging to bound
vortex free energies, twisted-to-untwisted partition-function ratios, or
centre-odd observables in three- or four-dimensional lattice gauge theory.**
The exact group-theoretic commutator law is well established for compact
groups. It yields the local spectral contraction used in row 778, and
products of commutators occur in surface-group integrals and two-dimensional
Yang–Mills. Those statements average independent Haar variables or evaluate
a 2D surface measure; they do not identify the normalizers of two 4D Wilson
measures with different centre twists.

The nearest lattice literature uses reflection positivity, twisted boundary
conditions, centre flux, character expansions and Migdal–Kadanoff-type
decimations. It gives implications from an already small vortex free energy
to Wilson-loop area decay, or compares fluxes under specified hypotheses.
It does not use the Haar commutator spectral multiplier to prove that
smallness. Tomboulis's 2007 all-coupling claim is disputed by Ito–Seiler and
is not an established theorem. Reuse and credit the prior reviews
library/prior/gap-lit-grok-paths.md, part D, and library/prior/gap-lit-flux.md.

## Haar commutator and surface-word formulas

**Michael Magee and Doron Puder, “Surface Words are Determined by Word
Measures on Groups,” arXiv:1902.04873, Israel Journal of Mathematics 241
(2021), 749–774, DOI 10.1007/s11856-021-2113-5.**
[arXiv](https://arxiv.org/abs/1902.04873);
[open copy read](https://durham-repository.worktribe.com/OutputFile/1305327).

Theorem 1.1 states that for a compact group G, an irreducible character psi,
and the genus-g surface word

    w_g = [x_1,y_1] ... [x_g,y_g],

with all variables independent Haar, E[psi(w_g)] = 1/psi(1)^(2g-1).
For one commutator this character moment is 1/d. Schur's lemma gives the
matrix Fourier coefficient E[rho([A,B])] = d^(-2) I. This is the
compact-group Frobenius identity behind row 778's (5)–(6). In SU(2), centre
odd irreducibles have even dimension d; the largest nontrivial multiplier is
1/4, attained at d=2. An n-fold convolution has multiplier d^(-2n), hence
norm 4^(-n) on that centre-odd subspace. These are exact symbolic identities,
not numerical estimates.

**Relation to (CF) and (16):** this supplies the Haar local averaging
algebra behind (CF), but not the common representation. It assumes independent
Haar inputs. Row 778 separately proves a conditional finite-beta mixture
estimate for selected links in a twisted Wilson measure; this controls
normalized conditional laws only. It gives no comparison of the twist
normalizers C_k product_x z_{k,x} in (15), no bound on the trace ratio (16),
and no 3D/4D centre-odd lattice observable. The group theorem includes SU(2)
but is not a theorem about a 4D Wilson Gibbs measure. Read status: the
relevant theorem and definition (paper opening and Theorem 1.1) were read;
the full paper was not.

The same paper proves that a word measure equal to [x,y] on every compact
group determines the commutator word up to a free-group automorphism; it
also proves the corresponding statement for surface words. This is about
word measures, not Wilson-loop area decay.

**Shripad Garge and Uday Bhaskar Sharma, “A Frobenius-Type Formula for
Compact Lie Groups,” arXiv:2410.12282 (2024).**
[arXiv record](https://arxiv.org/abs/2410.12282);
[HTML text](https://arxiv.org/html/2410.12282).

Theorem 1.1, for connected compact Lie G, gives the product-Haar measure of
the exact commutator-map fibre at g as a normalized limit of finite character
sums, with normalization exponent dim(G) − rank(G) + 1. This is the measure
of {(A,B): [A,B]=g}. It is **not** the density of the push-forward law of
[A,B] as a random group element; that law is determined by character moments
above. For connected nonabelian compact Lie groups these exact fibres have
measure zero, so this is a limiting character identity, not a twist-sector
probability estimate.

**Relation to (CF)/(16):** this corrects a possible confusion about the word
“commutator probability” but supplies neither statement. Its group scope
includes SU(2); it says nothing about 4D Wilson SU(2) observables. Read
status: theorem, hypotheses and proof discussion read in HTML; not full paper.

**Jason Fulman, “Representation theory and central limit theorems for traces
of commutators for compact Lie groups,” arXiv:2502.09499 (2025), Advances in
Applied Mathematics 172 (January 2026), 102962, DOI
10.1016/j.aam.2025.102962.**
[arXiv](https://arxiv.org/abs/2502.09499);
[publisher page](https://doi.org/10.1016/j.aam.2025.102962).

This studies traces of products of independent Haar commutators in classical
compact Lie groups. For example, at increasing rank, a fixed product's
symplectic-group trace tends to a standard normal; analogous orthogonal and
unitary results are given. It records the compact-Lie character identity
and cites Yang–Mills partition functions as motivation.

**Relation to (CF)/(16):** representation-theoretic context only. Large-rank
trace limits do not estimate finite-rank, finite-volume SU(2) Wilson
expectations or compare twisted normalizers. No implication to (CF) or (16).
Read status: arXiv HTML sections 1–3 and publisher metadata/abstract; not the
full paper. This is a forward-citation-era result, not a lattice theorem.

## Surface groups and 2D Yang–Mills

For a genus-g surface group the relation is a product of commutators equal
to the identity. In two-dimensional Yang–Mills, the heat-kernel lattice
measure has the representation expansion

    Z_g(A) = sum_R (dim R)^(2-2g) exp[-(e^2 A/2) C_2(R)],

up to normalization convention. The representation dimension carries the
Euler-characteristic power; area enters through the quadratic Casimir.
The 2024 source passage also gives the plaquette heat-kernel character
weight and subdivision invariance.

Source: Luca Griguolo, Rodolfo Panerai, Jacopo Papalini, Domenico Seminara
and Itamar Yaakov, “Localization and resummation of unstable instantons in
2d Yang-Mills,” arXiv:2403.00053, JHEP 06 (2024) 188, DOI
[10.1007/JHEP06(2024)188](https://doi.org/10.1007/JHEP06(2024)188).
Relevant equations (2.15)–(2.17), pp. 4–5:
[open full text](https://eprints.soton.ac.uk/492178/1/JHEP06_2024_188.pdf);
partial read. The cited passage gives the formula above and subdivision
invariance; the full article was not read. Classical sources include Edward
Witten, “On quantum gauge theories in two dimensions,” Communications in
Mathematical Physics 141 (1991), 153–209, and “Two Dimensional Gauge Theories Revisited,”
[arXiv:hep-th/9204083](https://arxiv.org/abs/hep-th/9204083). Magee–Puder's
open text gives the surface-word character moment formula.

**Relation to (CF)/(16):** exact products-of-commutators and surface
partition formulas, but in a different setting. The 2D heat-kernel action is
subdivision invariant; that reduction has no 4D Wilson counterpart. Neither
formula gives the finite-beta common-normalizer comparison (CF) or the
centre-odd trace bound (16). No transfer follows from dimension, topology,
or the presence of commutator words alone.

## Lattice gauge theory: close results, different mechanisms

The prior reviews library/prior/gap-lit-flux.md and
library/prior/gap-lit-grok-paths.md part D contain fuller source details and
read status; row 778 read and cited them. I reuse rather than repeat them.

| Result | Exact statement and scope | Relation to (CF)/(16); 4D Wilson SU(2)? |
|---|---|---|
| Tomboulis–Yaffe, DOI 10.1007/BF01206134; Kanazawa, arXiv:0808.3442, DOI 10.1016/j.aop.2009.04.002 | Reflection positivity gives a beta-independent finite-periodic-lattice inequality relating a Wilson loop of nonzero centre charge to the twisted/untwisted partition ratio. In SU(2), small vortex free energy suffices for an area law. | It consumes the small ratio; does not produce it, identify a commutator word with the flux trace, or provide the common C_k product_x z_{k,x} normalizer in (CF). No proof of (16). The inequality applies to finite 4D Wilson SU(2), but its required smallness is open. Relevant theorem read in row 778; see gap-lit-flux.md. |
| Mack–Petkova sufficient vortex criterion, DOI 10.1016/0003-4916(80)90221-0; Yaffe, DOI 10.1103/PhysRevD.21.1574 | Mack–Petkova: thick-vortex free-energy cost in a finite container is a sufficient condition for static-quark confinement. Yaffe: if thin magnetic flux cannot spread into thick tubes, nonconfinement follows. | These are implications/obstructions, not random-commutator estimates. Vortex free energy is input; no common normalizer and no (16). The criteria concern compact groups with centre / SU(N), but supply no order-one 4D Wilson SU(2) premise. Read status: Mack–Petkova PDF excerpts (DESY scan); Yaffe abstract only, as recorded in gap-lit-grok-paths.md D.1. |
| Davis, Kibble, Rajantie, Shanahan, arXiv:hep-lat/0009037 | Nonperturbative construction in 3D SU(2)+adjoint Higgs expresses defect free energies, including vortex tension, from twisted translation-invariant boundary conditions in terms of ’t Hooft loops. Its abstract's 4D pure-SU(2) extension concerns monopole mass in maximally Abelian gauge. | Direct twist/’t Hooft comparison, but no random commutator and no (CF)/(16). The 3D model includes matter; the 4D statement is monopoles, not the target vortex bound. Abstract read: [arXiv](https://arxiv.org/abs/hep-lat/0009037). |
| Tomboulis 2007, arXiv:0707.2179; Ito–Seiler, arXiv:0711.4930 and 0803.3019; Seiler, arXiv:0901.4246 | Tomboulis claims all-coupling 4D SU(2) confinement by potential-moving decimations of ordinary and twisted partition functions. Ito–Seiler/Seiler identify missing interpolation or weak-to-strong-coupling steps and note that a route not using non-Abelian structure would also apply to deconfining 4D U(1). | No random-commutator argument. The claimed result is disputed, not an established proof of (CF), vortex smallness or (16). Relevant sources and dispute read in row 778 and the prior reviews; not used as theorem. |
| Morikawa–Suzuki, arXiv:2501.07042, DOI 10.1093/ptep/ptaf072; 2026 follow-up arXiv:2601.20159 | Direct numerical computation of ’t Hooft partition function / flux sectors in 4D SU(2), with Fourier relations between electric and magnetic sectors. | No commutator averaging, common normalizer, or rigorous area bound for (16). Correct model/dimension, but simulations are GUIDE only. Abstract/definitions are in gap-lit-flux.md D.4. |

The 2026 preprint “Center-twisted Gribov spectra and the finite-volume
Gaussian response in the refined Gribov–Zwanziger framework,”
[arXiv:2609.03525](https://arxiv.org/abs/2609.03525), studies a continuum
Gribov–Zwanziger setting with background 1-form-symmetry twist and Gaussian
response, distinguishing that background from a dynamical centre vortex.
Relation to (CF)/(16): the abstract gives no commutator average, Wilson-lattice
vortex bound, or centre-odd trace estimate. It is not a 4D Wilson SU(2)
lattice result. Read status: abstract only; a forward-search hit, not a
supplier.

### Migdal–Kadanoff and decimation

Migdal–Kadanoff recursions for SU(2)/SU(3) lattice gauge theory use character
expansions and approximate bond/plaquette decimation. Creutz and Roberts
study these recursions with analytic approximations at weak/strong coupling
and numerical methods between them, Nuclear Physics B 190 (1981), 217–235,
DOI 10.1016/0550-3213(81)90491-0. The recursion is exact in 2D but
approximate in higher dimensions; it does not average the word [A,B] for
independent Haar elements. Tomboulis's disputed potential-moving use of
decimations compares twisted and untwisted partition functions but does not
employ row 778's character multiplier. Publisher abstract read:
[ScienceDirect](https://doi.org/10.1016/0550-3213(81)90491-0).

**Relation to (CF)/(16):** character expansions and scale transformations
are nearby concepts, but neither proves a common conditional normalizer.
2D exactness does not extend by analogy; 4D decimation is approximate and
the all-coupling claim remains disputed.

### Wilson area laws for commutator-shaped loops

I found general strong-coupling Wilson-loop area-law results, but no
published area law for a Wilson observable formed from a product of
transported commutator holonomies with row 778's role, and no theorem
transferring such a law to vortex free energy. Row 778 itself constructs

    W_a = (1/2) tr product_x P_x[A_x,B_x]P_x^{-1}

and proves area suppression in each twisted Wilson measure from separated
conditional link pairs. This is the lane's own result, not a literature
precedent. It is not independently checked by this literature search.
Strong-coupling ordinary-loop literature does not apply at the target
order-one coupling, and the target centre-odd parity operator is not this
contractible, centre-neutral loop word.

The Haar word-measure literature explains the auxiliary word's contraction.
It does **not** compare the word's expectation with the electric-flux trace:
row 778 (15) shows that after conditional integration the commutator
densities normalize to one while the twist-dependent factors
C_k product_x z_{k,x} remain. A common representation or another estimate
on those normalizers is exactly the open comparison (CF). Even a bound on
the word alone leaves (16) open.

## Relation to row 778, claim by claim

| Literature statement | Relation to (CF) | Relation to (16) | 4D Wilson SU(2)? |
|---|---|---|---|
| Magee–Puder: E[chi([A,B])]=1/d; Schur gives d^(-2)I | Establishes Haar local averaging, not the two twist normalizers. | No comparison with electric parity trace or S_ev. | Group identity applies; no 4D Gibbs statement. |
| Products of g Haar commutators / surface word | Exact representation averages of a surface-word measure. | No flux-sector inequality. | Compact-group mathematics, not 4D Wilson. |
| Garge–Sharma compact-Lie fibre formula | Exact commutator-map fibres, not push-forward density or twist ratios. | None. | General group result includes SU(2), no gauge theory. |
| 2D heat-kernel Yang–Mills genus formula | Exact surface partition evaluation with dimension/Casimir weights; no 4D normalizers. | No trace bound. | No: dimension, action and geometry differ. |
| TY/Kanazawa inequalities | Consume a twist ratio; do not derive (CF). | Wilson-loop implication after smallness, not proof of (16). | Yes as a conditional finite-4D implication, not as supplier. |
| 3D SU(2)+adjoint-Higgs vortex / ’t Hooft-loop work | Different action/observable; no CF. | No. | No for pure 4D Wilson SU(2). |
| MK/decimation and disputed all-coupling claim | No commutator measure or established common normalizer. | No verified order-one parity estimate. | Related intended model, but disputed proof is unusable. |
| Numerical 4D flux studies | Can guide a conjectured relation, not establish CF. | GUIDE only. | Model/dimension match, not proof. |

## Source and search record

I read the sa-index README and obligations list, grepped the outline chunks
and CA-I 4.12–4.19 chunk set for commutator, Frobenius, surface-word, twist,
flux and vortex terms, and followed the nearby outline object used by row 778:
chunk 02's neighboring rows around lines 2195–2313 and source
/tmp/sa_ym4.tex:2190–2250. It is the one-bond Wilson convolution, whose SU(2)
irreducible coefficients are positive modified Bessel coefficients. It is
not a Haar commutator law and contains no twist/free-energy comparison.
The CA-I index hits in chunks 03–04 use “commutator” for Lie brackets in
Hessian/localization formulas; another is Wilson-action renormalization in
item 4.18. Neither is random group commutator averaging or a flux-sector
estimate. No matching object was found by targeted grep in outline or CA-I.
The account was fetched once to /tmp/sa_ca_I.tex and never read wholesale.
Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text**. This is not a claim about material outside the searched terms.

The owner's papers directory /Users/jonBridger/ym4d-papers was absent in this
environment. No paper or extracted paper text was downloaded into the
checkout. Open web/arXiv copies were inspected in place; no refusal or bot
check was encountered.

Searches covered arXiv records/HTML, publisher and author-accessible pages,
and forward results through 2026. The Magee–Puder surface-word trail reaches
later compact-group trace work (Fulman, 2025/2026); recent twist searches
locate numerical flux-sector work and distinct continuum
Gribov–Zwanziger proposals. A second pass through those later sources did not
identify a 3D/4D lattice-gauge application of commutator averaging to vortex
free energies or centre-odd observables. This is a literature search result,
not an absence theorem. Read status is stated per source above.

RESULT: No located publication uses random-commutator averaging to prove a vortex free-energy or centre-odd observable bound in 3D/4D lattice gauge theory; compact-group and 2D surface formulas explain the Haar contraction but do not provide (CF), control the twist normalizers in (15), or prove the 4D Wilson SU(2) parity estimate (16).
