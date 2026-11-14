# Repo search

**Search refs:** `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` in `/Users/jonreilly/Projects/Physics`; `git grep -n -i -E`, restricted to `*.md` and `*.tex`. The required repo-search note `library/prior/repo-search-2026-11-08.md` was read; its target is unrelated and it supplies no finite-subgroup gauge-literature result. The broader finite-subgroup, freezing, Wilson, and named-author searches were capped locators. Targeted follow-ups found these relevant hits:

| Ref and file | Exact statement | Closeness |
|---|---|---|
| `pr/10114` (also repeated on `pr/10133`), `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/briefs_hrp/AUTHOR_BRIEF_HRP.md:63` | “Gauge groups: `Z_2`, `Z_3`, and a finite subgroup of `SU(2)` (`Q8`, or the binary tetrahedral group of order 24).” The next bullets call for exact reflection-positivity Gram matrices on small periodic lattices. | Directly names Q8 and 2T as finite-group gauge controls in a YM4D proof project, but it is a preregistered computational check brief, not a literature result, freezing comparison, coefficient formula, or suppression bound. The brief itself says finite checks confirm algebra only. |
| `origin/main` (same file on `pr/10133`), `docs/BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28.md:25–60, 128–139` | Identifies `2O` as the 48 unit quaternions in `SU(2)`, gives its central sign and spinorial/non-spinorial irreducible dimensions, and explicitly limits the result to finite-group/quaternion/character theory. | Exact finite-subgroup representation data, but about a discrete spinor sign; no Wilson lattice action, freezing, tilted character coefficients, or high-spin suppression. |
| All five refs, targeted for `Petcher`, `Weingarten`, `Bhanot`, `Creutz-Jacobs-Rebbi`, `Hartung`, finite-subgroup gauge theory, freezing, and Wilson with `Q_8`/`2T`/`2O`/`2I` | No matching literature statements located. | Search result only; not evidence that no such work exists. |
| All five refs, targeted for `character coefficient`, high-spin/adjoint suppression, strong-coupling, and one-slice terms | Generic SU(2) character/transfer material appears, but no relevant finite-group spin-by-spin comparison or high-spin suppression statement was identified. | Nearby transfer/character work does not answer the finite-subgroup comparison question. |

No `q8filter`, `q8test`, finite-subgroup gauge, or freezing owner appears in this lane's `library/open-registry.md`. `library/prior/gap-lit-q8filter.md` was absent before this task. I read the existing `library/prior/gap-lit-icosa.md`; its finite-subgroup and high-spin literature review overlaps this request substantially, so I carry its findings forward and focus this note on Q8/2T spin-resolved Wilson coefficients and the narrower suppression question. The requested item is not fully covered elsewhere.

# Provenance and scope

Research reading note for FINISH row 855, at lane checkout `c588008759e976f54c9dc8630fae4124d7f5de78`. It is not an audit, proof, or status change. The task forbids computer-assisted steps; no numerical or program step was run. The specified prior file was absent. I read `library/gap-q8test-opus.md` sections 1 and 3, plus the overlapping literature statements in `library/prior/gap-lit-icosa.md` and the finite-group comparison in `library/gap-assume-opus.md` §3.1. No outside-the-checkout source was searched or read; this note reports only source claims already quoted or cited in the checkout.

## Prior literature coverage reused

The finite-subgroup/freezing question is already substantially covered in `library/prior/gap-lit-icosa.md` §2. I preserve its reported statements here rather than repeat its broader discussion. “Exact statement” below means the statement as reported from the cited publication in that existing note; I did not retrieve or independently read the papers in this task.

| Author and year | Exact statement already recorded in the checkout | Closeness to row 855 |
|---|---|---|
| D. Petcher and D. H. Weingarten (1980), *Monte Carlo calculations and a model of the phase structure for gauge theories on discrete subgroups of SU(2)* | The simulations of the binary tetrahedral, octahedral, and icosahedral groups show two phases separated by first-order transitions; critical coupling decreases as subgroup order grows. For the 120-element binary icosahedral group, mean plaquette, square loops, and estimated string tension agree with SU(2) over a wide coupling range. | Directly covers finite-subgroup SU(2) approximation and freezing/transition behavior, but the evidence is Monte Carlo plus a model. It gives no spin-resolved Wilson coefficient or high-spin rarity bound. The existing note says the abstract gives no numerical critical couplings. |
| C. Rebbi (1980), *Phase structure of non-Abelian lattice gauge theories* | Reports a two-phase structure and first-order transitions in the studied finite non-Abelian models; for three discrete SU(2) subgroups the critical coupling moves toward zero as group order grows, and the high-temperature phase confines. | Directly relevant to transitions and confinement, but numerical/model-specific; no representation-by-representation estimate. |
| G. Bhanot, K. Bitar, and R. Salvador (1987), *On solving four-dimensional SU(2) gauge theory by numerically finding its partition function* | Numerically compares SU(2) and its 120-element subgroup on lattices through `4^4`, observing transitions/crossovers and finite-size zeros. | Direct SU(2)/finite-subgroup comparison, limited to finite-volume numerical results; no uniform coefficient or suppression bound. |
| G. Bhanot and R. Rebbi (1981), *Monte Carlo simulations of lattice models with finite subgroups of SU(3) as gauge groups* | Their five finite SU(3) subgroups have first-order freezing transitions before the continuum scaling limit. | Adjacent evidence about finite-group digitization, but the gauge group is SU(3), not SU(2), Q8, or 2T. |
| H. Grosse and H. Kühnelt (1981), *Phase structure of lattice gauge theories for non-Abelian subgroups of SU(3)* | Studies SU(3)-subgroup phase structure by Monte Carlo and strong-coupling expansions; reports splitting of a transition as group order increases. | Adjacent SU(3) result; it supplies no SU(2) spin comparison or one-slice estimate. |
| Tobias Hartung, Andreas Jakobs, Karl Jansen, Stefan Ostmeyer, and Carsten Urbach (2022), *Digitising SU(2) gauge fields and the freezing transition*; related 2022 preprint *Digitizing SU(2) Gauge Fields and What to Look Out for When Doing So* | The recorded account says they compare subgroup and non-subgroup discretizations and explain freezing at sufficiently weak coupling through the finite minimum spacing of group elements. Table IV is recorded as hot/cold-start Monte Carlo on `8^4`, with freezing estimates Q8 `1.15(15)`, 2T `2.15(15)`, 2O `3.20(10)`, and 2I `5.70(20)` in the lane's beta normalization. | Directly covers all four named binary groups and their freezing scales, but these are simulation estimates and a discretization explanation, not exact spin coefficient or suppression bounds. The source of the estimates is `library/gap-assume-opus.md` §3.1; the paper-level summary is in `gap-lit-icosa.md` §2. |
| Creutz–Jacobs–Rebbi | No matching bibliographic entry or finite-subgroup SU(2) statement was found in the bounded local searches. | Unresolved identification: no author/year/title or exact claim can responsibly be supplied from the permitted corpus. This is a search result, not evidence that no such work exists. |

## Spin-resolved coefficients and high-spin suppression

### What is explicit in the existing research text

The SA outline is explicit for the **continuous SU(2) one-link convolution**, not for finite subgroups. In `/Users/jonreilly/sa/YM4_sketch_500.tex:2197–2239`, it defines the Wilson kernel and gives the spin-ℓ coefficient `c_l = 2 e^{-beta} I_{2l+1}(beta)/beta > 0`; its character coefficient is `d_l c_l = e^{-beta}(I_{2l}(beta)-I_{2l+2}(beta))`. The outline records a positive Bessel-series representation, factorial decay in the index, and the ratio bound `I_{n+1}/I_n <= beta/(2(n+1))`. This is an exact one-link spectral suppression statement in the SU(2) setting. The neighboring outline rows discuss positivity, trace class, and smooth half-kernel multipliers. They do not give finite-group coefficients or rarity for the interacting one-slice law.

The lane's row-843 research note, `library/gap-q8test-opus.md` §§1, 3, works out the finite-group comparison at a **tilted one-plaquette/kinetic-factor** level. It gives

```math
r^{Q_8}_V=\frac{\sinh\beta}{\cosh\beta+3},\qquad
r^{2T}_V=\frac{\sinh\beta+4\sinh(\beta/2)}{\cosh\beta+3+8\cosh(\beta/2)},
```

and the conjugate-pair eigenvalues for the other center-odd 2T irreps. Its Theorem 3.4 compares the SU(2) spin-5/2 Bessel ratio `I_6/I_1` to those Q8/2T defining-representation eigenvalues and proves strict separation for every positive beta; Corollary 3.7 gives a spin-2-shaped space whose SU(2) norm is `r_{3/2}` and also separates from Q8/2T. This is unusually close to the requested finite-group, spin-by-spin coefficient comparison, but it is **an existing lane derivation**, not an identified published result or an independent verification. Its own section title and proof concern a one-plaquette convolution filter.

There is a second, distinct local result: `library/gap-assume-opus.md` §3.1 records Hartung et al.'s Monte Carlo freezing estimates above. Those guide the location where fixed-group behavior changes; they are not bounds on the high-spin coefficients.

### Literature result and remaining gap

Within the searched repository refs and the literature summaries already in this checkout, I found no published statement comparing SU(2) Wilson character coefficients with Q8, 2T, 2O, or 2I **spin by spin** under the exponentially tilted one-plaquette law. The local row-843 calculation supplies such a comparison for Q8 and 2T at the one-plaquette/kinetic-factor level, so that exact algebraic question is not new within this lane. It is not the same as the SU(2)-only Bessel decay in the outline, and the freezing simulations do not supply it.

For high-spin suppression, the outline's Bessel/factorial decay is a genuine SU(2) single-link supplier, and the row-843 filter is a lane-derived single-factor comparison. The literature summary in `gap-lit-icosa.md` §3 records general Peter–Weyl/spin-network expansions, Casimir labels, and strong-coupling surface/area-law estimates in their own convergence regimes, but reports no uniform high-spin/Casimir suppression estimate for the interacting four-dimensional Wilson one-slice law at order-one beta. I found no closer published supplier in the bounded search. In particular, no located result upgrades the one-link or kinetic-factor decay to rarity under the interacting one-slice distribution needed by the row-843 (HS) obligation. This is a scoped search conclusion, not a claim of nonexistence.

The targeted search of CA-I, CA-II, and CA-III found no finite-subgroup, Q8/2T, Wilson-character-coefficient, Bessel, Peter–Weyl, or high-spin statement matching this target. One CA-II occurrence of “quadratic Casimir in the adjoint representation” is in a local Yang–Mills renormalization calculation and does not concern lattice Wilson character suppression. `library/lit-balaban.md` records that the Balaban papers are unavailable in this checkout; its quotations and secondary summaries provide no target-specific result, and I did not attempt to retrieve them.

## Disposition

Finite-subgroup SU(2) approximation and freezing are already known here as published simulation/model results, including estimates for Q8 and 2T. The outline already contains exact SU(2) one-link Bessel decay. Row 843 already derives spin-resolved Q8/2T tilted one-plaquette comparisons. I did not locate a published source for that comparison, or a published high-spin rarity bound for the interacting one-slice law. Thus the narrower literature gap remains the passage from a single-link/filter coefficient to interacting one-slice high-spin rarity; this reading note adds no proof, audit, or status.

RESULT: Reading note complete. Prior finite-subgroup/freezing coverage reused; no located literature supplier for interacting one-slice high-spin rarity.

