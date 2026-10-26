# Attempt: J:derive:review-20261016-nearest-site-prime-closure:a1

Obligation (J-9658-2 of REVIEW_AGENT_WORK.json): certify exhaustive coverage of the two
eleven-dimensional nearest-site unitarity varieties, and independently verify the real-locus or trace
reductions of the unadopted nearest-site flatness candidate. Same-family worker (Claude Sonnet 5.5),
unrefereed. Nothing here is adopted, audited or a replacement PR.

## Plain-language summary

The candidate says: a one-amplitude-per-site walk on staggered 2x2x2 blocks, covariant under the
signed cube-rotation action, with hops only between nearest sites, cannot move. Its proof used one
computer algebra system (Singular) to list eight solution components and then checked each by hand
or by a trace test.

I rebuilt both families and their equations from the signed generators, and then covered the whole
solution set a different way: a case tree computed with sympy (case splits on products that must vanish,
a scaling "chart" argument, and splits on factorisations), ending in 25 pieces per family. I did not use the
Singular components to build the tree. Then I checked three things on those pieces:

1. every piece lies inside one of Singular's printed components, and all eight printed components are used,
   so the printed list does cover everything (this is the "prime coverage" question);
2. on every piece, the traces of the first eight powers of the walk matrix do not depend on momentum, so
   the eigenvalues do not depend on momentum, for every complex solution, hence for every unitary one;
3. a separate real-number argument shows that every unitary solution uses only "inward and on-site" hops,
   or only "outward and on-site" hops, and both kinds are visibly momentum-independent (up to a diagonal
   gauge). Seven of the 25 pieces per family contain no real unitary solution at all.

All of this is exact computer algebra in sympy, plus short hand-checkable reductions. The one thing
not independently certified is that sympy's Groebner and factorisation outputs are what they claim (no
cofactor certificates). So these are CHECKED, not PROVED. Result: no nearest-site covariant walk of either
declared signed class disperses.

## What I read (as required)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
  in full (130 lines) in the read-only view of current main (`a77a3449c91a753b06ce2a63876cd460b62cb4cf`),
  plus the four node entries of `docs/audit/data/axiom_premise_nodes.json` (minimal_axioms, scale_reference,
  kinetic_isotropy, realized_state primitives).
- All 35 source objects of the brief, extracted with `git show 2bb6c1a5...:path`: 35 of 35 sha256 equal the
  brief's values (`RECOVERY_STATUS.json`). `2bb6c1a5...` is an ancestor of the read-view main head.
  The scope file `.claude/science/review-fixes/review-drain-20261016/CUBIC_TICK_SCOPE.md` was also read.
- Prior art searched: `gh pr list --search` for nearest-site, staggered block tick, minAssGTZ, spinorial block walk
  returns only closed PR 9658 (the source campaign) and closed PR 9636; no open PR addresses this
  obligation. The probes view has no earlier attempt on this id (only `PR9658_FOLLOWUP.md`).

## Premises, split by origin

- **Axioms say** (MINIMAL_AXIOMS lines 37-41, 45-53): sites are `Z^3` with nearest-neighbour adjacency,
  translations, and proper cubic rotations about each site; each site has local possibilities with algebra
  `M_2(C)`. The axioms say nothing about a tick, a walk, a block, an amplitude per site, or unitarity
  (lines 114-130 say dynamics is downstream; line 178 lists the staggered-Dirac gate as open).
  No registered primitive is used (`kinetic_isotropy`, `scale_reference`, `realized_state` are not needed).
- **The lane supplied** (ASSUMED, model, not axiom content; same as the note
  `docs/STAGGERED_ONE_QUBIT_BLOCKS_...2026-10-16.md`, "Declared objects"): one complex amplitude per site;
  2x2x2 blocks with translation by 2; cube rotations acting about block centres by signed permutations of the
  eight corners; one-tick walk `W = sum_n A_n z^n`, unitary for all `z` on the torus, covariant
  `A_{Rn} = D(R) A_n D(R)^T`; nearest-site means every site displacement lies in `{-1,0,1}^3`.
  The block origin is a supplied choice (the note says nothing selects it) and block-centre covariance is
  not the axiom's "rotations about each site". READING: the conclusion is about this model only.
- **Two signed classes** (ASSUMED): the two diagonal-sign-gauge classes of signed corner actions found by the
  source's enumeration (sign vectors on the two quarter-turn generators with `D^4 = -1` generating a group of
  order 48 with central `-1`). I do not classify arbitrary projective lifts or central extensions (J-9658-3).

## Steps

Labels: PROVED = full argument here; CHECKED = executed by `check.py` (line ids in brackets);
ASSUMED = premise; READING = interpretation.

1. **ASSUMED** the model above.
2. **CHECKED [A1-A5]** Census of the declared sign pairs. 64 sign vectors per generator have `D^4 = -1`;
   the 64 x 64 pairs give 512 order-48 groups (128 distinct matrix groups). All 128 are equivalent under
   conjugation by diagonal `+-1` matrices to one of two representatives, 64 each, and the two are not
   equivalent. (Same census as the source's `gaugecheck.py`, recomputed.)
3. **CHECKED [B1, B7]** Family regeneration without the source code path. Orbit method: a covariant entry
   `(n, v_out, v_in)` generates an orbit under the 48 signed elements; the orbit supports a parameter iff its
   signs are consistent. Result for both classes: 216 allowed entries, 11 consistent orbits of sizes
   8,24,24,24,24,24,24,8,24,24,8, hop types `ooo, oo0, ooi, o00, o0i, o0i, oii, 000, 00i, 0ii, iii`
   (o: step across a block face, i: step inside the block). Independent exact check: the rank of the covariance
   equations of the two generators over `Q` is 205, so the solution space has dimension 11.
4. **CHECKED [B2-B4]** (known from the independent review; repeated only as the base of the chain) The
   regenerated hop matrices equal the source `model.json` / `model1.json` entry by entry. The regenerated
   `W^dagger W - 1` coefficients give 45 distinct polynomials up to sign, equal as a set to the source's 79 listed
   polynomials up to sign (the source lists both signs), for both classes.
5. **CHECKED [B5, B6]** (new bookkeeping fact) The 55 generators of `nearest_site/nn_min.sing` are exactly the
   class-0 two-sided unitarity set (`W^dagger W = 1` together with `W W^dagger = 1`, 55 distinct up to sign) after
   negating the variables `c3, c4, c8, c9` (and their conjugates). They are not the class-1 set. So the original
   Singular run in `nearest_site/` treated class 0 only, in sign-flipped coordinates and with the two-sided ideal;
   `independent_check_B8` used the one-sided ideal for both classes. The varieties agree (step 9).
6. **PROVED** Reductions used by the tree.
   (a) *Scaling.* `T_l(c, cb) = (l c, l^-1 cb)` maps each generator to itself: every generator is bilinear in
   `c x cb` or is the normalisation `sum_t w_t c_t cb_t - 1`. So `V(I)` is `T`-invariant. Each coefficient of a
   power of `z` in `tr W(z)^p` is a polynomial in `c` alone, homogeneous of degree `p`, so it vanishes at a point iff it
   vanishes on the orbit.
   (b) *Chart cover.* On `V(I)`, `c != 0`, since `c = 0` turns the normalisation into `-1 = 0`. Fix an order of
   the free `c`-variables of a case. Let `a` be the first one with `c_a != 0`; `T_{1/c_a}` moves the point to `c_a = 1`,
   `c_j = 0` for earlier `j`. So the case is covered by these charts.
   (c) *Splitting.* If `h = h_1 ... h_k` lies in the ideal `J`, then `V(J)` is contained in the union of the `V(J + h_i)`.
   A monomial in `J` is the case of single variables.
   (d) *Newton.* Over `Q`, `tr W^p` for `p = 1..8` fixes the characteristic polynomial of an `8 x 8` matrix.
   (e) *Structure of pure supports.* Along an axis, a hop of type `0` has `n_a = 0 = vo_a - vi_a`; type `o` has
   `n_a = +-1` with `vo_a - vi_a = n_a` (from `|vo - vi - 2n| <= 1`); type `i` has `n_a = 0`. Hence an orbit without
   `i` has `n = vo - vi` for all its entries, so its part of `W(z)` is `Z M Z^-1` with `Z = diag(z^v)`, and a sum of such
   parts is `Z W(1) Z^-1`: constant spectrum. An orbit without `o` has `n = 0`: no `z` at all. [G1 enumerates this.]
7. **CHECKED [C1]** Exhaustive elimination tree, no Singular output used. Root: the monomial generators
   `c0 cb10, c10 cb0, c2 cb6, c6 cb2` and their consequences, split exhaustively (14 minimal zero patterns).
   Per root: the chart cover of 6(b). Per node: reduced Groebner basis (sympy Buchberger, grevlex), then split on a
   monomial in the basis, or on the factors of a basis element (the factor product is multiplied back and compared
   exactly). Result per class: 85 nodes, 9 factor splits, **25 leaf varieties**. Each leaf is `V(basis)` in a chart.
8. **CHECKED [C2, C3]** Every original generator reduces to 0 modulo every leaf basis (so each leaf lies in `V(I)`;
   with 7 the leaves' union is `V(I)`), and so does every `W W^dagger - 1` generator (the two-sided ideal has the
   same variety).
9. **CHECKED [D1]** Flatness (trace route, complex strength). On every leaf of both classes, each non-constant
   `z`-coefficient of `tr W(z)^p`, `p = 1..8`, reduces to 0 modulo the leaf basis (in the ideal itself, no radical
   powers needed). With 6(a), (d): at every complex point of `V(I)` the characteristic polynomial of `W(z)` does not
   depend on `z`.
10. **CHECKED [E1-E6]** Coverage of the printed Singular lists. For `sing0.log`, `sing1.log` (8 components each,
    dimensions 4,4,2,2,2,2,4,4) and for the original `nn_min.out` (sign-flipped to class-0 coordinates): every leaf
    lies in at least one printed component (every printed generator reduces to 0 modulo the leaf basis, always to the
    first power; all printed generators are first checked to be homogeneous for the scaling weight `#c - #cb`, so
    evaluating them on a chart `c_a = 1` is legitimate) and all eight printed components receive a leaf. For `sing0.log` and `sing1.log` each printed component
    also receives a leaf that lies in no other component (so none of the eight is redundant for the leaf cover). With
    step 8 this gives `V(I) = union of leaves`, contained in the union of the printed components; that each printed
    component lies in `V(I)` is Singular's claim and was not re-tested. I did not test primality or minimality.
11. **CHECKED [G0-G2]** Real-locus route (independent of the trace route). For real points `cb = conj c`; on a chart
    `c'_k = x_k + i y_k`, `cb'_k = r (x_k - i y_k)`, `r = |c_a|^2 > 0`. Each leaf basis element is split into real and
    imaginary parts, a Groebner basis over `Q` is computed, and sound positivity rules are applied: a constant or pure
    power of `r` means no real point; a monomial means one of its `x,y` factors vanishes; a polynomial whose monomials
    are all even in every `x,y` variable with coefficients of one sign forces each monomial to vanish. Result for each class:
    7 of 25 leaves have no real point; the remaining states have support inside `{ooo,oo0,o00,000}` (9 states) or
    `{000,00i,0ii,iii}` (9 states); none is mixed. By 6(e) every such real point is flat.
    This reproduces the candidate's final real-locus dichotomy (purely inward / purely outward / constant) for both
    classes, by a route that does not use the printed components. I did not reproduce its component-by-component
    statements (components 1-8 of the candidate), because my pieces are not the printed components.
12. **CHECKED [F1-F5]** Sampling evidence only: 56 / 51 numerical unitary solutions (class 0 / 1) and 44 / 46
    numerical points of the complex variety all lie on some leaf; spectra of the unitary ones are `k`-independent to
    3e-13; their supports are pure. A first version of the sampling check failed on one constant-walk-type point
    (`c7 cb7 = 1`, other coordinates ~3e-6 because the ideal is not radical there); I then loosened the zero-pattern
    tolerance to 1e-4. A second edit that also raised the chart threshold to 1e-3 produced six false
    "uncovered" points (each matched a leaf with residual below 1e-7); I reverted that threshold to 1e-9. Both
    edits are tolerances in a sampling test only.
13. **CHECKED [controls]** D2: with no constraints the trace test reports `k`-dependence at `p = 2`. D3: dropping the
    lower half (by degree) of the largest leaf basis does the same. B6': the 55 `nn_min` generators are not the class-1
    set. A5: the two sign classes are inequivalent. F4: a random non-unitary covariant vector has a `k`-dependent
    characteristic polynomial. E-block: leaves lie in only some printed components, so the containment test discriminates.

**Statement S (CHECKED in sympy; conditional on step 1; not a PROVED theorem).** For each of the two declared signed
classes, every complex solution of the nearest-site covariant unitarity equations has a `z`-independent characteristic
polynomial, and every unitary solution is purely inward-or-on-site or purely outward-or-on-site; its spectrum does not
depend on `k`. READING: within this model a nearest-site walk cannot propagate.

## What is new relative to the sources

- Not new (retrieval / known): the family and equation match (steps 3-4 of the independent review), the eight printed
  components, the B8 trace test on the printed primes, the numerical flat hits.
- New, CHECKED: (i) an exhaustive cover of `V(I)` for both classes built without Singular, in a different algebra
  system; (ii) exact leaf-by-leaf containment in all printed components (Singular's list covers `V(I)`, and every
  printed component is needed); (iii) the trace-flatness result on the leaves, which transfers to every printed
  component; (iv) an independent real-locus route confirming the pure-inward / pure-outward dichotomy, with seven
  real-empty leaves per class; (v) the `nn_min.sing` identification of step 5; (vi) the sign-pair census.

## First unresolved step

**U1 (soundness of the computer algebra).** Every split element and every leaf basis element is a sympy
`groebner`/`factor_list` output that is asserted, not certified, to lie in the ideal generated by its inputs. The
cover (steps 7-8) and the flatness reductions (9, 11) inherit that. Evidence in favour: the leaves' union matches an
independent system's list (step 10), all sampled numerical points (56 + 51 unitary, 44 + 46 complex) are covered, and a
mutated basis fails. Next
artifact: explicit cofactor certificates `f = sum a_i g_i` for the 9 factor-split elements per class, and for the leaf
basis elements, or a second independent Groebner implementation. Until then, call this CHECKED relative to sympy.

Also open, not touched: primality and minimality of the printed components (not needed for flatness);
other signed lifts, central extensions and projective actions (J-9658-3); the integer classes; larger blocks,
interactions, continuous time; and any identification with the axiom's "rotations about each site".

## Route and residual record (truthful; no invented failures)

Tried and what happened:
- Whole ideal, 22 variables, 45 generators: sympy `groebner` with `buchberger` and with `f5b`, two background runs
  each started at the beginning; stopped by me after several minutes without finishing (no result, not a proof of
  hardness). `f5b` also did not finish on a trivially inconsistent small system (stopped after about 8 minutes).
- Tree without charts (splits on monomials and factors only): finished, 45 and 44 leaves, flat on all, about 9-14
  minutes per class. Kept only as a cross-check of step 9 (not part of `check.py`).
- Variable reorderings (4 random permutations) on the heaviest node: 4 to 9 minutes each under load; no gain.
  Splitting on one variable zero / nonzero with a saturation variable: slower. Chart cover: 5 times faster; used.
- Real locus by my own positivity rules (monomials, even-power sums) on the chart leaves: closed all leaves for both classes in about 16 s per class.
Residual, in the candidate's N1-N8 terms: N1 routes not excluded by this work remain the candidate's own list
(longer hops, other sign classes, larger blocks, interactions, continuous time). N4 inputs: sympy outputs (U1).
N7 strongest objection: the family could differ from the physical one by a convention; mitigated by the sign-pair census
and the exact rank, not by a classification of all projective lifts.

## Execution and input record

- Environment: macOS 25.6, Python 3.12.8, sympy 1.14.0, numpy 2.4.1, scipy 1.17.0, mpmath 1.3.0. No Singular, Sage, M2.
- Inputs: the 35 hash-verified objects; `check.py` embeds hash-checked copies of `model.json`, `model1.json`,
  `sing0.log`, `sing1.log`, `nn_min.sing`, `nn_min.out` for comparison only; nothing is read from disk.
- `check.py`: one process, exact arithmetic for all algebra, numpy/scipy only for the sampling block. Final full run:
  `TOTAL: PASS=56 FAIL=0`, wall 4 min 45 s, user CPU 252 s; an earlier identical-logic run peaked at about 120 MB.
  Two earlier full runs took 407 s and 648 s of wall time because other workers loaded the machine (load average
  above 30); one earlier run failed its sampling checks for the tolerance reasons in step 12.
- Files in the output directory: `ATTEMPT.md`, `check.py`, `RECOVERY_STATUS.json`. Working scripts and leaf pickles
  stayed in the scratchpad `work/` directory and are not deliverables.
