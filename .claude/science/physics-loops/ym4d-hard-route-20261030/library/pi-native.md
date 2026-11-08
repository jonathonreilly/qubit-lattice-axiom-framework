## Repo search

The lead searched main and PRs #10114, #10133, #10134 and #10141.
`prior/repo-search-2026-11-08.md`, sections 1 and 12, records the relevant hits.
`prior/pi-native.md` is absent at the task pin.
I checked the following primary passages after fetching their PR heads.

| Source checked | Result and closeness |
|---|---|
| PR #10141, `research/ym4d/library/out-pi.md:273–356` | The existing inverse and walk theorem assumes complete whole-action reads. Its boundary counterexamples concern that convention. |
| Same PR, `research/ym4d/library/layer-thm-part.md:1333–1341,1385–1408` | The action, rows, boundary coefficients and domains must match. Native inner-action admission remains separate. |
| Same PR, `research/ym4d/library/out-gw.md:54–64` | The frame estimate follows after PI admission. General localized admission is excluded. |
| PR #10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/RTARGET.md:695–725` | A soft-action saddle and proposed boundary walks. This is a different operator; its general-background input remains open. |

The checked heads are `c73ad7b177d94f89ff37b77386936e3d52b48b05`
and `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
The PR #10141 files are snapshots of this route, not independent proofs.
Credit their Claude and Codex contributors.
The registry retains PI-ADMIT under `pi-admit`; row 573 assigns this native boundary supplier.
The buffered-cut construction remains with `bz-own`.

# PI on the native localized cut

Codex, 2026-11-08; research base `3c88234f7a67e19c37bf44b34751bd98620e80aa`.
FINISH row 573. Research text, not an audit; this grants no scientific status.
Only this file is a repository output. No computer-assisted proof is used.

Credit **Tadeusz Balaban** for the propagator and localization methods.
Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text**, for every account definition and result used below.
Write **SA** and **I** for their outline and account I at `31a47c543775`.
Write **N** for [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex)
at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.

`bz-122.md` already identifies the literal cut and its inward staircase.
`c0-sup.md` already identifies PI's genuine exterior reads.
`pi-admit.md`, section 7, already proves the difference between the two Hessians.
`leaf-sc.md` supplies symmetric rows on the admitted **whole-action** class.
Its use of “native” names the averaging prescription, not an inner-action boundary theorem.
None of these results is rederived here.

## 1. Result: the native inverse already has a source proof

**Stop under the task's prior-work rule.** The operator-level target is
already covered in N. Its proof includes the true inner action, bare boundary,
projected gauge, coarse inverse and local carrier expansion.
It is substantially more than the boundary sketch cited by `pi-admit.md`.
The relevant proof continues well beyond N 31940–32015.

This finding does **not** prove item 10 on its prescribed stage domain.
N expressly leaves admission of a separately fixed history geometry to its caller.
It also distinguishes its constructed carrier family from a previously prescribed switched family.
Those are the existing application questions, not another missing native inverse theorem.
No new inverse proof or new supplier lane is proposed here.

The classifications below describe the source text, not an independent check.
The source proof remains a cited research input.
SA's index was consulted at `chunk-10.md`, neighbouring rows 10113–10546,
and `obligations.md:520–560`.
The `ca-4.12-4.19` README and relevant box-domain rows retain application-side admission.
N was located through `pi-admit.md`, section 7, then its exact labels.

## 2. Kill test: a one-plaquette-deep bare cut

The native bare model passes the test. Here is the flat specialization
of SA 10505 and N 28243–28263, not a new all-layer argument.

Let E be the bonds inside a finite cut, and P its inner plaquettes.
Take every row bare and take U=1. Then Q=Q'=I, R=0, and

\[
 \Delta_{a,\mathrm{in}}=d_P^Td_P+\eta^{-2}I,
 \qquad G_0=\Delta_{a,\mathrm{in}}^{-1},
 \qquad q_0=\Delta_{a,\mathrm{in}}.                 \tag{1}
\]

Here \((d_PA)(p)=\eta^{-1}\sum_{b\in\partial p}\epsilon_{pb}A(b)\).
Every plaquette has four edges. Every bond belongs to at most six plaquettes.
Cauchy–Schwarz therefore gives

\[
 0\le d_P^Td_P\le24\eta^{-2}I,
 \qquad I\le\eta^2\Delta_{a,\mathrm{in}}\le25I.    \tag{2}
\]

This includes a four-dimensional slab only one plaquette deep.
Deleting outer plaquettes preserves (2). No exterior link enters it.
Gauge zero modes of the inner curl receive the bare row mass.

For a single plaquette, orient its four edges consistently and write
\(s=(1,1,1,1)^T\). In each colour component, the explicit matrix is

\[
 \Delta_{a,\mathrm{in}}=\eta^{-2}(I+ss^T),\qquad
 G_0=\eta^2\left(I-\frac{ss^T}{5}\right).           \tag{3}
\]

Multiplication verifies (3), since \(s^Ts=4\).
This elementary cell is a boundary diagnostic, not an asserted reached history.

The same bare model has uniform decay. Put
\(E_0=I-\eta^2\Delta_{a,\mathrm{in}}/13\).
Equation (2) gives \(\|E_0\|\le12/13\), and hence

\[
 G_0=\frac{\eta^2}{13}\sum_{n\ge0}E_0^n.           \tag{4}
\]

Join two bonds when they share an inner plaquette.
At graph distance r, the matrix entry of \(E_0^n\) vanishes for n<r.
The remaining geometric sum bounds that entry of G_0 by
\(\eta^2(12/13)^r\).
Disconnected components have zero off-diagonal entries.
This is a hand argument; no eigenvalue computation was run.

For small real fields, N's native Wilson estimate gives the bare lower bound
\((1-C\kappa)\eta^{-2}\|A\|_2^2\); see `npl:boundary-gap`, N 28256–28263.
Choose \(C\kappa\le1/4\). For a complex perturbation E with
\(\|\eta^2E\|<1/4\), the real inverse and its Neumann series give
\(\|(\Delta_{a,\mathrm{in}}+E)^{-1}\|\le2\eta^2\).
N supplies the coefficient estimate on its specified complex tube.
Thus the bare edge itself causes no singularity on that class.
This statement retains smallness on every **present inner** plaquette.
Smallness only on boxes far from the boundary would not be that hypothesis.

## 3. The existing native proof, with exact source locations

| N source and label | What the source proves or defines |
|---|---|
| 26979–27028, `ch:layered-site-restoration`, `lsi:site-operators` | Sites and bonds are inner to the original determining region. The action contains precisely its inner plaquettes. Fine measure is \(\eta^4\); top and row measures are \(\xi^4\). The site average is the actual own-pillar average. |
| 27666–27716, `fms:boundary-removal` | The bare row mass controls the true outer collar, including zero-extension jumps. Nonbare patches stay inside the region. |
| 28236–28334, `npl:boundary-gap`, `thm:npl-proper-gap` | The real all-layer precision has a uniform energy gap. The form contains the inner Wilson Hessian and projected gauge. Its proof treats the bare boundary directly. |
| 31558–31669, `lpw:positive-operators`, `lpw:compression` | Genuine compressions of the positive scalar and Feynman operators retain complete averaging carriers and the original list of inner plaquettes. |
| 31944–32015, `lpw:slow-commutator`, `lpw:parametrix-identity` | Bare boundary commutators cost \(C/m\). The exact local parametrix does not fill exterior plaquettes. |
| 32138–32261, `lpw:positive-local-walks` | Exact normally convergent local inverse families, with holomorphic coefficients and uniform weighted cell norms. |
| 32633–32715, `prop:cci-positive-coarse-inverse` | The positive coarse Gram and projection matrices have local inverse families on a common complex tube. The proof gives the convergent inverse series. |
| 32717–32800, `cor:cci-row-inverse` | The same construction applies to the actual normalized \(QG_0Q^\sharp\). This is the required coarse inverse, not merely the scalar inverse. |
| 33223–33248, `ncw:zero-current-Woodbury`, `ncw:G0-family` | An exact positive-factor identity constructs the projected native G_0 and its complete carrier family. |
| 33321–33360, `ncw:normalized-field-row`, `ncw:first-row-Schur` | Physical normalization of the coarse inverse, and its complex/current perturbation series. |
| 33528–33645, `prop:ncw-named-families` | Native current-corrected inverses, coarse inverses and lifts have exact local families. Constants are uniform in depth, compatible volume and admitted shape. |
| 40831–40937, `dnr:linear-families` | The native families have the first-order output and transpose bounds used by response consumers. |
| 40955 onward, `dnr:parameter-families` | Complete carrier tags give enlarged switch discs and surviving exponential decay. This constructs a family; it does not identify an earlier assignment. |

In particular, N 26995–26998 fixes the native graph before any inversion.
N 31967–31973 explicitly retains missing exterior plaquettes.
N 32717–32800 supplies the coarse inverse that the earlier positive-walk result alone would not supply.
These are the decisive additions to the prior-work record.

The source assumptions remain: separated aligned geometry, admitted actual means,
small real inner curvature, positive row weights, and the specified small complex C1 tube.
Current-corrected statements also retain their touching-current ceiling.
A claim about a predetermined history must check these constants and that whole parameter image.
N 32279–32286 and 32794–32799 explicitly retain that distinction.

Balaban's underlying sources are [*Propagators for lattice gauge theories in
a background field*](https://doi.org/10.1007/BF01240355), CMP **99** (1985), 389–434, pp. 393–395,
(3.21)–(3.27), pp. 409–416, (3.87)–(3.108), and p. 422, (3.132).
The localization is *Large Field Renormalization I*, CMP **122** (1989),
175–202, p. 180, (1.19)–(1.20), and p. 188, (1.56)–(1.58).
Part II, CMP **122**, 355–392, pp. 361 and 370, (1.22), (1.52)–(1.53),
contains later interior separations, not a new exterior collar for this birth.
These page/formula attributions are reused from `out-pi.md` and `bz-122.md`.
The latter already checked the localization against the original PDFs.
No new original-page verification is claimed here: the allowed paper directory
was absent, and the attempted Euclid downloads returned HTML instead of PDFs.
The stopping reason is the existing N proof, not unavailable papers.

## 4. Translation to PI's scale convention

This is a coordinate identification of the existing native theorem.
It does not identify the inner action with the whole action.
Use \(m_c=\xi_c\), \(a_f=m^{-2}\), and the physical transpose throughout.
N 33321–33335 defines

\[
 \mathcal Q_n=mQ,\qquad
 \mathcal Q_n^\sharp=Q^\sharp m^{-3},\qquad
 T_0=mQG_0Q^\sharp m^{-3}.
\]

Consequently, as an operator on physical rows,

\[
 q_{0,\mathrm{in}}=(QG_0Q^\sharp)^{-1}
                    =m^{-3}T_0^{-1}m.                    \tag{5}
\]

If \(B_C(c,c')\) is a counting-coordinate carrier coefficient of \(T_0^{-1}\),
its physical density is exactly

\[
 q_C(c,c')=m_c^{-3}m_{c'}^{-3}B_C(c,c').                   \tag{6}
\]

Indeed (5) gives a counting entry \(m_c^{-3}B_C(c,c')m_{c'}\).
Dividing by the source measure \(m_{c'}^4\) proves (6).
Thus N's carrier bounds have precisely PI's symmetric density scaling.

To use PI's asymmetric convention, retain its existing scale-distance argument,
`out-pi.md`, section 8. If \(g\) is the minimum layer gap in local units,

\[
 \frac{m_{c'}}{m_c}\le L\exp\{(\log L)d(c,c')/g\}.
\]

A source carrier bound with spatial rate s therefore gives

\[
 |q_{0,\mathrm{in}}(c,c')|
 \le CL\,m_c^{-2}m_{c'}^{-4}
             e^{-[s-(\log L)/g]d(c,c')}.                 \tag{7}
\]

Require the source's scale reserve so the bracket is positive;
see N 32602–32620 and `ncw:scale-reserve`, N 32907–32920.
Its common-rate and shell floors remain attached.
Here d is N's physical layer metric. No equality with PI's more
restrictive lattice-contour metric is asserted.
Multiplying each carrier coefficient by the endpoint weights in (6)
preserves holomorphy, locality and the exact sum.
The source's reserved carrier rate supplies exponential summability.
This is a local carrier expansion of the needed type.
It is not a termwise identification with PI's particular tile words.

For the row response, N uses per-length datum:
\(H=G_0Q^\sharp q_{0,\mathrm{in}}\) at zero current.
CA-I 13640–13647 uses raw angles and hence \(H_0=Hm^{-1}\).
This is an exact change of coordinates. No boundary correction is hidden in it.

## 5. The localized entry and its consumers

The geometric cut is already known from `bz-122.md`, (2)–(7).
Its tower is \(T_j=P_j\cap D_j\), with \(T_0=Z\), and

\[
 d_\infty(T_{j+1},T_j^c)
       \ge\min\{d_\infty(P_{j+1},P_j^c),M_1\ell_{j+1}\}. \tag{8}
\]

Use (8) to compare the actual gap with N's separation threshold.
N may choose its final carrier tile larger than its initial tile.
Its proof explicitly does not identify that tile with a prescribed history size.
Thus (8) is a comparison formula, not automatic admission at the original constants.

Interior data must include every retained inner bond, plaquette and row carrier.
They need not include any exterior plaquette.
On that trace, sufficiently small S1-loc and the actual C1 twist bounds
give N's real curvature and complex-tube inputs by the existing local coefficient comparison.
But the task's original stage radii cannot be replaced by smaller radii without proving their image fits.
S2+ has no exterior coefficient to control in this native graph.
Any genuine interior stencil requirement remains.

| Consumer | What it can use | Exact remaining distinction |
|---|---|---|
| Native zero-current inverse calls, CA-I 13583–13589, 13624–13665 | The native G_0, q_0 and projection algebra; (5)–(7) give the physical scale conversion. | This applies when the caller's Delta is the inner Hessian on the same graph. It does not change a whole-action caller. |
| Item 10's native response at switches one, I 131725–131746 | The native inverse input after matching its determining geometry, actual rows and domain. | The full localized layer, its current radius and its displayed H_max do not follow from a bare inverse alone. I 131568 calls these statements inputs. |
| Item 10 at general switches | N's newly constructed complete carrier family can support a native response construction. | Equality to the prescribed H_sigma requires the same filing, masks, node factors, equation and parameter image. Agreement at switches one does not prove this. |
| GW1 | N already constructs the corresponding native G_1, coarse inverse and H_1 families; see `prop:ncw-named-families` and `dnr:linear-families`. | `out-gw1.md:31–77` explicitly uses the whole-action PI graph. Its posted theorem is not automatically a theorem about a different graph or word assignment. |
| LAYER-M | Native primitive families provide candidate inputs to the reduced tagged construction. | `out-m3.md:7–59` distinguishes its new switched current from the older chart current. The mass tag and complete assignment must match. A q_0 estimate alone does not establish that identity. |

The whole-action/native difference is already proved in `pi-admit.md`, (17).
It is nonzero even at identity, so a small-field change of coordinates cannot simply erase it.
We do not repeat that counterexample or call it a failure of the native inverse.

The short change of representation proved here is only (5)–(6), together with
the raw-datum factor \(m^{-1}\). Those are physical-coordinate identities.
No exact change between distinct actions or switched assignments has been established.

## 6. Disposition and status table

The proposed missing native inverse theorem should be replaced by the source chain in section 3.
Under the task's explicit no-duplication rule, this lane stops at that discovery.
It does not claim stopping alternative (a) for the full actual-entry assertion.
It has neither an actual-entry counterexample nor three new failed routes to report.
Inventing them would repeat existing work or misstate the outcome.

The remaining application work overlaps the registry's PI-ADMIT row,
owned by `pi-admit`, and LAYER-M, owned by `m3`.
This note records the new source locations for those owners.
It changes no registry, FINISH row, scientific status or public claim.

| Statement | Status |
|---|---|
| Flat one-plaquette-deep native boundary model | Pass; explicit hand check (1)–(4), specializing the existing bare-mass mechanism. |
| Native all-layer inverse and local expansion | Already proved in N on its stated admitted class; cited here, not independently checked. |
| PI physical scaling and raw-datum conversion | Exact identities (5)–(6); decay conversion reuses PI section 8. |
| Bare outer edge requires an exterior gauge for the native problem | No; the cited native construction uses only present inner coefficients. |
| Full item-10 admission with its original constants and domains | Open application match; not established by this source mapping. |
| Equality to the prescribed switched H_sigma / LAYER-M assignment | Open representation match; equality at switches one is insufficient. |
| New proof, actual-entry counterexample, or scientific status grant | None. Stop follows the prior-work rule. |

**First open input:** the actual-entry match at I 131725–131746.
For every point of its prescribed stage and switch domain, identify the native graph,
rows, pair and carrier assignment with the cited N construction.
Verify its fixed separation, tube and current ceilings on that whole image,
and identify the resulting switched response with the prescribed H_sigma.
This is an application and representation obligation, not another native inverse estimate.
