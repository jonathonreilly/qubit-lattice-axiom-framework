## Repo search

Written by Codex (GPT-6; dispatch specifies gpt-6-astra, xhigh; this runtime
does not expose a more specific serving-model ID), checking the text at
`b04caeebcf05279bcc07f315b90fa29b74681676`. Research check, not an audit;
no status grant and no mass gap claimed. This file does not check the full
assumptions exercise, invent a new attack, or read row 1054's check.

The task-specific prior note is absent. The general digest
`prior/repo-search-2026-11-08.md` concerns thirteen earlier RG targets,
not this new FLUX-W check. Its relevant transfer hit is
PR 10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`. I fetched that PR and read its
header and lines 98–151 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
It constructs a positive local one-step witness. It supplies neither the
present flux comparison nor a uniform continuum gap. Credit: that earlier
Codex construction. The digest reports the same source blob on PR 10133;
I did not repeat its proof or re-fetch that duplicate.

Current main is `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`.
Its `research/mass-gap/library/gap-crux-restate.md:29–35` already contains
TM and TM-c, including centre-flip commutation. I read that exact range.
This is direct prior work, reused below; FLUX-W(a) is not a new theorem.
An exact-label search for FLUX-W and T_JW-lat in main's mass-gap section
found no hit. The task supplies no separate "Repo prior work" hit.
The local open registry, open-core and l17c contain no matching target or
owner under those labels. This check stays on row 1055; rows 1051 and 1053
retain the proof routes. Row 1054's file was not opened.

The lead reports searches of main and PRs 10114, 10133, 10134 and 10141.
I checked the relevant hit above, not every unrelated RG hit or every PR
afresh. This is a bounded search record, not a theorem of absence.

## Work checkpoint

1. Check the registry, relevant repo hits, and outline/account index entries.
2. Test a crossing plaquette and a two-state transfer operator by hand.
3. Check FLUX-W (a)-(d), including TM-c, PHYS-SEED and G1.
4. Check T_JW-lat, its frozen-group tests, and the set-aside conclusions.
5. Give corrected text, compare the terminal targets, and state one RESULT.

All five steps are complete. The open mathematical obligations and the
limits of the check are recorded below; none is discharged by a run.
Downloads use the new directory `/tmp/sa-gap-flux-w-check-astra.autDUT`.

## First hand tests

**Crossing plaquette.** Write a positively oriented spatial plaquette as
\(U_i(x)U_k(x+\hat i)U_i(x+\hat k)^{-1}U_k(x)^{-1}\), with \(k\ne i\).
Its two direction-\(i\) bonds have the same initial \(i\)-coordinate.
At the cut they are both flipped, including the inverse bond. The product
becomes \((-U_i(x))U_k(x+\hat i)(-U_i(x+\hat k))^{-1}U_k(x)^{-1}\),
which equals the original product. Elsewhere neither bond is flipped.
The argument works at the periodic seam. A plaquette without direction
\(i\) has no flipped bond. This proves the claimed spatial plaquette count.
It does not claim invariance of a temporal plaquette when just one endpoint
slice is flipped: that plaquette has one sign. The transfer identity needs
simultaneous flips on both endpoint slices.

**Two-state transfer operator.** Let
\(T=\begin{pmatrix}a&b\\b&a\end{pmatrix}\), \(a>b>0\), and let
\(C\) exchange the two coordinates. This is positivity improving and positive
definite. Its normalized vacuum is \((1,1)/\sqrt2\), with eigenvalue
\(a+b\). The odd vector \((1,-1)/\sqrt2\) has eigenvalue \(a-b\).
Thus \(E_{\rm odd}=m=\log((a+b)/(a-b))\). The claimed inequality passes,
and equality is possible. Keeping \(a=1\) and letting \(b\downarrow0\)
shows that symmetry and positivity alone give no uniform positive bound.
These are written calculations, not numerical tests.

## FLUX-W (a)–(d)

**(a): HOLDS.** Here "every plaquette" means spatial plaquettes on the
slice; for the kernel it means the slab under simultaneous endpoint flips.
Let \(z_\ell=-1\) on the cut bonds and \(+1\) elsewhere. Put
\((c_i u)_\ell=z_\ell u_\ell\) and \((C_i f)(u)=f(c_i u)\).
Product Haar invariance makes \(C_i\) unitary. It is an involution.
Centrality gives \(c_i(h\cdot u)=h\cdot(c_i u)\), so \(C_iP=PC_i\)
for the gauge projection \(P\). The spatial calculation above gives
\(V(c_i u)=V(u)\).

Use the actual gauge-averaged kernel from `gap-transfer.md:108–136`:
\[
A(u,v)=e^{-(V(u)+V(v))/2}\int dh\prod_\ell
c\big((h\cdot v)_\ell u_\ell^{-1}\big),\qquad
c(g)=e^{-\beta(1-\tfrac12\operatorname{tr}g)}.
\]
For every temporal plaquette factor,
\[
(h\cdot c_i v)_\ell(c_i u)_\ell^{-1}
=z_\ell(h\cdot v)_\ell u_\ell^{-1}z_\ell^{-1}
=(h\cdot v)_\ell u_\ell^{-1}.
\]
Consequently \(A(c_i u,c_i v)=A(u,v)\). Changing variables \(v=c_iw\)
in the integral gives \(TC_i=C_iT\), including on \(\operatorname{Ran}P\).
This checks the exact commutation clause of TM-c at
`gap-crux-restate.md:35`. A single-slice flip instead produces the twist;
it must not be used as the invariance argument.

**(b): HOLDS.** Simplicity makes \(C_i\psi_0=\alpha_i\psi_0\).
Both functions are strictly positive and have the same norm. Thus
\(\alpha_i\) is positive and has absolute value one, hence equals one.
This establishes finite-volume vacuum invariance, independently of any
thermodynamic statement about broken symmetry.

**(c): HOLDS, with the zero-sector convention made explicit.** The three
\(C_i\) commute, so their joint eigenspaces reduce \(T\). If \(e_i=1\),
\(\langle\psi_0,f\rangle=\langle C_i\psi_0,C_if\rangle
=-\langle\psi_0,f\rangle\) for \(f\in\mathcal H_e\). Thus
\(\mathcal H_e\subset\psi_0^\perp\) for \(e\ne0\). The positive compact
spectral theorem gives
\(\|T|_{\mathcal H_e}\|\le\|T|_{\psi_0^\perp}\|=\lambda_1\).
Taking logarithms proves \(E_e\ge m\). If a sector is zero or its operator
norm is zero, define its energy as \(+\infty\). This avoids assuming a
nonzero eigenvalue just to state the inequality. With the usual nonzero
Wilson sectors the original definition gives the same answer.

**(d): HOLDS as a conditional implication, with units and domain explicit.**
The source is `gap-phys-seed.md:311–320`, not merely the later summary.
Its hypotheses include \(\ell_1/(4a_j)\in\mathbb N\), at least 3,
eventually. Use the 1/5041 seed form, enlarging \(\ell\) first if needed.
Choose \(0<q'<1\) so \(5041S_j(\ell/(2a_j);(\ell/a_j)^3)\le q'\)
for all \(j\ge j_0\). Corollary S3',
`gap-crux-restate.md:217–219`, applies at each such \(j\) with
\(N_j=\ell/(2a_j)\). It covers **every integer** \(n\ge2N_j\), not
only dyadic cubes. Hence, simultaneously for all such \(j,n,e\ne0\),
\[
\frac{E_{e,j}(n)}{a_j}\ge\frac{m_j(n^3)}{a_j}
\ge \frac{\log(1/q')}{a_jN_j}
=\frac{2\log(1/q')}{\ell}=:M_*.
\]
The physical sides covered are \(L=a_jn\ge\ell\). There is one \(j_0\)
for all the later cube sizes. This verifies G1's use in row 1052.
Here (W) is the repaired version in `parts/gap.md:21–23`: its witness
\(L\) must be at least \(4L_0\), where \((L_0,D_0)\) bounds BDD-Delta.
`gap-zd-astra.md:403–418` checks this repair. The unrepaired version in
the older dichotomy note omits the domain needed to use \(D^+(L/4)\).
\((W)\Rightarrow\)(PHYS-SEED) remains the cited conditional engine;
this check does not prove (W), verify the account's spacing compatibility,
or recheck that whole engine.

**Source chronology.** Row 1052 line 561's `gap-zd-astra.md` citation exists
at this pin (518 lines). Its item 18 supplies the domain repair just used.
The older `gap-dichotomy.md:35–43` absence report is stale. An early working
draft of this check repeated that report; direct inspection corrected it.

## T_JW-lat and the continuum implication

**A2, lines 194–198: HOLDS given a reconstructed positive semigroup.**
Reflection positivity and translation invariance alone must not substitute
for existence of that semigroup; its domain, contraction and continuity
requirements remain in the continuum datum. Once it exists, put
\(\psi_F=[F]-\langle F\rangle\Omega\). The positive spectral measure gives
\[
\mu_F([0,\Delta-\varepsilon])
\le e^{t(\Delta-\varepsilon)}\langle\psi_F,e^{-tH}\psi_F\rangle
\le C_F e^{-\varepsilon t}.
\]
Let \(t\to\infty\), then take the union over positive rational
\(\varepsilon<\Delta\). The projection onto \([0,\Delta)\) kills all
these centred vectors. Totality and boundedness of a spectral projection
extend this to \(\Omega^\perp\). It acts as identity on \(\Omega\).
Thus the kernel is exactly \(\mathbb C\Omega\), and the gap is at least
\(\Delta\). This proof needs total positive-time **polynomial** vectors,
including multi-time products, not just single-field two-point functions.

**Line 485, sufficiency: HOLDS AFTER CORRECTION of scope.** A precise
version sufficient for the requested lattice route is the following.

> Choose cutoff states \(\nu_j\) and lattice representatives \(F_j\) for
> a class \(\mathcal C\) total in the intended continuum Hilbert space.
> Assume a continuum time-reflection datum with (P1)–(P4), (H2) and (TOT).
> For some \(\Delta>0\), each \(F\in\mathcal C\) has a finite \(C_F\)
> independent of \(j\), with
> \(0\le u_{j,F}(t_j)\le C_F e^{-\Delta t_j}\) at physical lattice
> times \(t_j\to t>0\) (even lattice times suffice), where
> \(u_{j,F}(t_j)=\nu_j(\overline{\Theta F_j}\,\tau_{t_j}F_j)
> -|\nu_j(F_j)|^2\), and (H2) gives its limit \(u_{\infty,F}(t)\).
> Then A2 gives a gap at least \(\Delta\) and a unique vacuum in that
> continuum Hilbert space.

Taking the limit of the displayed inequality proves this version directly.
The original universal quantifier over states is sufficient if it includes
the chosen states and the same uniform constants. It is unnecessary for
existence of one theory. The represented observables, state class and
meaning of "total" must be specified. In particular all DLR states need
not be translation invariant or reflection positive.

There is also the exact route already on file: prove a cutoff spectral gap
on the full cutoff OS space, then use Proposition P'. At a fixed cutoff,
A2 needs no constant uniform across vectors or cutoffs if its tested vectors
are total there. The resulting operator bound implies
\(u_{j,F}(t_j)\le e^{-\Delta(t_j-s_j)}u_{j,F}(s_j)\) for even lattice
times \(t_j\ge s_j>0\). Even times avoid any issue with negative
eigenvalues of a discrete transfer contraction. Pass to the limit at
fixed positive \(s<t\) using (H2), then apply the
same spectral argument. This is why the growth of renormalized sup norms
does not defeat P'. It is not legitimate just to pass the bounded-local-
function constants \(\|F_j\|_\infty^2\) to a renormalized limit.

**Line 485, identification with G2: FAILS at "this is the lane's (G2)-(G3)"**
if "torus limits or DLR states" includes arbitrary DLR states.
`gap-seed-limit.md:119–123,138–177,188–204` proves the assertion for
limits of its **admissible torus sequences**. It explicitly leaves
subsequence independence open and does not prove even DLR membership
there, much less coverage of every DLR state. G1 does not fill that missing
state-class argument. No counterexample for Wilson SU(2) is asserted;
the advertised deduction to the larger class is unsupported.

Replace that sentence by:

> For admissible torus-limit states in Proposition P, the cutoff spectral
> bound and Proposition P' give this continuum gap implication. Extending
> the statement to every DLR state requires a separate theorem.

**"Gives the Jaffe–Witten gap": HOLDS only for the full specified theory.**
The conclusion above is a mass gap in the Hilbert space to which TOT
refers. With existence, relativistic axioms, non-triviality and full
Yang–Mills observable identification supplied for that same space, it
gives the gap clause of the SU(2) Jaffe–Witten target. It does not supply
those premises. In particular GOAL's T0 concerns the scalar
\(\operatorname{tr}F^2\) sector. Its TOT does not identify that sector
with the Hilbert space of all required local gauge-invariant fields.

This restriction is already in the literature we are using. The outline
index, chunk 01 rows at 581–599 and chunk 29 at 31860–31882, and the
neighbouring obligations, separate scalar reconstruction, full-theory
identification and a mass gap. I read SA 31860–31882: it states those
limitations explicitly. CA-I 2688–2713 likewise asserts a curvature
Hilbert space and separately lists Wightman fields, clustering, vacuum
uniqueness and a mass gap among things not asserted there. These are
scope statements, not contradictions of the conditional implication.

## Section 6c: which tests bind

**Flat implies pure gauge: HOLDS AFTER CORRECTION of the nonabelian proof.**
The first inadequate justification is line 508's parenthesis using
\(H_1=0\). Abelian homology is not enough for a nonabelian connection.
Use plaquette homotopy, or the following explicit grid argument instead.

On a rectangular box, root at its lowest corner. A monotone path to a
vertex is a word of positive coordinate steps. Any two such words with
the same endpoint differ by adjacent swaps of distinct coordinate steps.
Flatness gives exactly the equality of the two path products for each
swap; every square stays inside the box. Let \(p(x)\) be this common
transport from the root to \(x\). For each positive edge \(x\to y\),
\(p(y)=p(x)U_{xy}\). The gauge transformation \(g(x)=p(x)\) therefore
has \(g(x)U_{xy}g(y)^{-1}=1\). Reverse edges follow by inversion.

Every finite loop in \(\mathbb Z^4\) lies in such a box, so has identity
holonomy. Fix a root at zero and any finite path to each vertex. The
preceding fact makes its transport path-independent; the same formula
defines one global gauge transformation. No compatibility assumption on
independently chosen infinite spanning trees is needed. This proof works
for any group. On a general region the hypothesis is simple connectivity
of the plaquette **2-complex**, not just a condition on its graph or H1.

**Frozen \(Z_2,Q_8,2T\): HOLDS for the stated gap test, with two limits.**
At the exact flat constraint every local gauge-invariant observable on
\(\mathbb Z^4\) takes its value at the identity field. Its connected
correlations vanish. The local gauge-invariant OS space is one-dimensional,
so the gap inequality is vacuous. This gives no counterexample to an
infinite-volume local gap implication. The periodic tests measure global
holonomies, which are absent from this local state space.

This is compatible with, and does not undo, the earlier Codex result
`gap-crux-exercise2-check-astra.md:227–259` (row 884). Its two Q8/2T
flat triples \((1,1,1)\) and \((i,1,1)\) remain distinct after gauge
conjugation and centre flips. They produce two **centre-even** torus
states. That proof is prior work, not redone here. Its finite-beta bound
has beta depending on the specified box and time. It does not claim
failure of every-box seeds at one fixed finite beta.

The two limits on the new conclusion are these:

- Exact flatness proves the frozen statement only. It does not prove
  weak-coupling mixing at finite beta; that needs its own estimates.
- The frozen local theory does not satisfy the full non-trivial Yang–Mills
  target. It is a positive control for the **gap inequality only**, which
  is how line 484 defines T_JW. It cannot separate two full SU(2)
  construction targets or prove strictness for SU(2).

Thus "these frozen holonomy counterexamples do not test the local
infinite-volume gap" is correct. "They bind exactly torus statements"
is too broad: other non-simply-connected domains or nonlocal observable
algebras can also retain holonomy. State the domain actually checked.

**Ordered Ising, line 498: FAILS at "two pure phases ... so Omega is not
unique" as an assertion about a selected T_JW theory.** Vacuum uniqueness
is internal to one reconstructed representation. It is not uniqueness
among all states of the same Euclidean specification. The implication
requires a mixture, or an explicit demand to treat all DLR states.

Here is the precise correction. Suppose two translation-invariant phases
\(\nu_+,\nu_-\) cluster and a local real \(A\) has means \(m\) and
\(-m\), \(m\ne0\). In their equal mixture \(\nu\),
\[
\lim_{t\to\infty}\{
\nu(A\tau_tA)-\nu(A)^2\}=m^2>0.
\]
This follows by averaging the two clustering limits. The mixture fails
A2. Selecting \(\nu_+\) instead removes this particular obstruction;
existence of \(\nu_-\) does not put a second vacuum into its Hilbert
space. Consequently the ordered-Ising device can test a universal
all-DLR conclusion or a specified symmetric mixture/torus limit. It does
not by itself refute an existential single-phase local-gap tool. The
calculation is conditional on the two clustering phases; it does not
rebuild finite-temperature Ising phase theory.

**Other rows: retained only in their exact original scopes.** A massless
factor remains an obstruction when the factor is present in the target
observable algebra and the tested hypothesis holds for the product.
For \(H=H_1\otimes1+1\otimes H_2\), the subspace
\(\Omega_1\otimes\Omega_2^\perp\) already carries the second factor's
low energies. Changing boundary topology does not remove them. U(1) and
the photon serve the same role subject to their cited model and parameter
hypotheses. No new proof of the published U(1) input is claimed here.

D2, SUB, SHEET and the pinned-cell obstructions still refute their exact
hypothesis forms where proved, whether or not the final target changes.
They do not refute every replacement form. Ceilings still delimit their
named estimate families. K7/\(w_p\) still need the same coupling and
first-passage qualifiers. Five dimensions and the numerical transition
claims remain guidance, not theorem-grade counterexamples. These are
logical scope checks; the underlying proofs are not rechecked in this row.

## Section 6d: set-aside methods

**HOLDS AFTER CORRECTION as a bounded bookkeeping conclusion; not a new
universal no-go.** I read the actual tables in
`gap-crux-exercise2-max.md:392–415` (rows 1–18),
`gap-crux-exercise3-max.md:489–513` (rows 19–33), the NP premises in
`gap-crux-exercise4-max.md:342–372,579–596`, and
`parts/gap.md:96–150,203–245`. No proof method becomes proved or a
previously false lemma becomes true merely by deleting a flux consumer.
The source tables are themselves digests, not complete proofs of every
listed exclusion.

| Group | Disposition under the corrected target comparison |
|---|---|
| Rows 1–3, 6–10, 12, 15–18 | Existing local defects, restricted estimate ranges or missing inputs are unchanged where they were actually established. |
| Rows 4–5 | The torus step and MONO-Delta claims keep their original verdicts. Do not justify a blanket exclusion of selected-phase local-gap methods by line 498's Ising argument. |
| Row 11 | Already **not set aside**: its negative verdict was withdrawn in the source table. |
| Rows 13–14; exercise-4 Fact T | Flux-target arguments become unnecessary for the local-gap route. Their original claims are not repaired. Fact T alone still has no supplied local-clustering consumer. |
| Rows 19–21, 24–27, 29–33 | Exact false forms remain false; open or merely tried forms remain open or tried. The current state file already narrows several earlier broad exclusions. |
| Row 22 | Missing from row 1052's list: changing an engine supplies no estimate, but its usefulness for a different terminal target is not refuted by the old slogan. No new input is supplied here. |
| Row 23 | The U(1) obstruction remains for a carrier with the same class-wide hypotheses; first-passage restrictions must still be checked. |
| Row 28 | Already narrowed by row 998. K7 is not a refutation of every ultraviolet-aware form. |
| Later blocks 1004–1050 | Keep the individual domains, reopenings and missing inputs reported in `parts/gap.md`. No exhaustive recheck of their proofs is claimed. |

Replace lines 514 and 528's blanket reading by:

> The frozen-holonomy scope correction alone revives none of the listed
> methods as a proved route to a local gap. It makes some torus/flux
> obligations optional. Existing false statements remain false on their
> original domains. Their rejection does not exclude a new local-gap
> statement with different hypotheses. Open and already reopened forms
> stay open; no new attack is undertaken here.

In particular Proposition NP concerns persistence of a periodic Casimir
contraction. Its original counterexample and consumer do not change when
one stops using that route. No claim that it rules out every
infinite-volume single-phase construction follows.

## The Reading and the proposed replacement of (W)

**One direction: HOLDS conditionally.** With the repaired wall, the stated
engine and compatible continuum data,
\[
(W)\Longrightarrow
\begin{cases}
\text{a uniform physical gap on all sufficiently large periodic cubes},\\
\text{the flux bounds of FLUX-W(d)},\\
\text{a local continuum gap in the specified total observable sector}.
\end{cases}
\]
The last line needs the separate continuum datum, (H2) and (TOT).
The flux inequality is not itself an existence or reconstruction theorem.

**The Reading, line 563: HOLDS AFTER CORRECTION to this one-way meaning.**
Call (d) uniform finite-torus flux separation. At finite volume the vacuum
is centre invariant by (b) at every positive coupling, before (W) is known.
Interpreting uniform separation as an unbroken thermodynamic one-form
symmetry needs a definition and a limit theorem. In particular a constant
positive lower bound for \(E_e(L)\) is not a lower bound proportional to
\(L\), and no positive string tension or Wilson area law was proved here.

**"Weaker ... by exactly the flux clause", line 565: FAILS as a proved
comparison.** There are three distinct missing implications.

1. The printed T_JW-lat includes a larger state class than G2. Its all-DLR
   version is not proved to follow from (W).
2. Even after matching that class, no converse from the local gap and
   flux separation to the thermal seed is proved. The seed bounds
   \(\sum_{r\ge1}e^{-N E_r}\), not only the bottom of each sector.
   A lower bound on each \(E_r\) supplies no bound on the number of terms.
   For example, \(K\) levels of energy \(M\) contribute
   \(K e^{-NM}\) for arbitrary finite \(K\). This elementary spectral
   observation is not claimed as a symmetric Wilson-model counterexample.
   The need for an additional bound is already recorded in
   `gap-phys-seed.md:306–309` (Corollary Z2 and its open converse) and
   `gap-assume-opus.md:90` (item 52). It is prior work, not a new obstacle.
3. Global torus states invisible to local observables need not all be
   centre-odd. Row 884's Q8/2T example is explicitly centre-even. Thus
   deleting just the nonzero electric-flux sectors does not identify the
   remaining torus trace with the local infinite-volume Hilbert space.

The source's recalled finite-group phase picture is a motivation for a
distinction. It is not a proved separating SU(2) construction. With full
non-triviality restored, the exactly frozen trivial theory cannot serve
as that witness either.

**Corrected replacement text.**

> (W) is a sufficient periodic thermal criterion. Given the specified
> continuum data it yields a local mass gap, and it also enforces uniform
> separation of nonzero electric-flux sectors on large periodic cubes.
> The Jaffe–Witten gap clause on a selected infinite-volume local theory
> does not explicitly require these finite-torus conclusions. We have
> not proved an equivalence, identified their exact difference, or proved
> strictness for pure SU(2). A replacement terminal criterion should name
> the cutoff states and the full continuum observable class it serves.

Replacing (W) by that **matched local-gap criterion** loses the periodic
thermal seed, its state-count/Casimir control and its all-sector finite-box
conclusions. It retains the gap clause needed for the selected continuum
theory when the reconstruction and identification premises hold. It lets
a proof avoid those extra outputs. That is a change of proof obligation,
not a new estimate or progress on the SU(2) gap. The universal all-DLR
version keeps an additional state-selection demand that this replacement
does not need. Whether either local criterion is easier for SU(2) remains
OPEN. The checked material supplies no quantitative mechanism deciding it.

## Check coverage and verdicts

| Requested statement | Verdict |
|---|---|
| FLUX-W(a), spatial plaquette count and transfer commutation | HOLDS, with the simultaneous-endpoint kernel calculation above |
| FLUX-W(b), invariant finite-volume vacuum | HOLDS |
| FLUX-W(c), nonzero-flux energy at least the full gap | HOLDS; equality possible |
| FLUX-W(d), uniform physical flux bound from repaired (W) | HOLDS conditionally on the stated engine and spacing domain |
| T_JW-lat supplies the gap clause | HOLDS AFTER CORRECTION: matched state class, full TOT and separate existence/identification premises |
| Printed all-DLR T_JW-lat is just G2–G3 | FAILS as a deduction at line 485 |
| Frozen holonomy tests refute this local-gap target | They do not; the scoping HOLDS AFTER the flatness, topology and non-triviality corrections |
| Ordered-Ising phases force nonunique vacuum in a selected theory | FAILS at line 498; a mixture or universal-state quantifier is needed |
| No set-aside method is revived solely by this scoping | HOLDS AFTER the bounded bookkeeping correction; no new exclusion |
| (W) equals the JW gap plus exactly a flux/unbroken-centre clause | FAILS as an equivalence; the one-way Reading HOLDS AFTER CORRECTION |

Primary text checked: row 1052 lines 194–198, 480–528 and 552–565,
with its definitions at 81–104. The two hand tests and the kernel,
projection, spectral-measure and grid-path arguments above are written
without computer-assisted steps and can be formulated in Lean. No Lean
proof was written or run. No numerical computation was used.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their outline and complete-account text, at `31a47c543775`. Both files
were fetched once into the new scratch directory. The outline index's
README, relevant chunk rows and neighbours, and obligations were used
before SA 2313–2335 and 31860–31882. The 4.12–4.19 account index has no
matching flux/gap entry; none of those RG items is an input here. The
CA-full index and GOAL's locator led to CA-I 2688–2713. No whole external
manuscript was read. Balaban's RG is background to the chosen trajectory;
no Balaban formula or new primary-paper theorem is imported by this check.
The transfer and seed results remain credited to their existing lane
authors and checks; row 1052 is Claude Opus 5.5 high's text.

Not covered: the other assumptions, C8 or the claimed new 2D proofs, full
U(1)/Ising/finite-beta finite-group phase theorems, all set-aside proofs,
the whole seed engine, the continuum existence construction, full
Yang–Mills identification, or any new attack. No source, registry,
FINISH, audit or status file was changed. The only repository output is
this research check. Row 1054 was not read.

RESULT: HOLDS AFTER CORRECTION overall: FLUX-W(a)–(d) holds conditionally with the stated domains; the all-DLR identification, selected-phase Ising argument and "exactly the flux clause" comparison fail as deductions; a matched local-gap target suffices given full continuum data, strictness and relative difficulty for SU(2) remain OPEN, and no mass gap is claimed.
