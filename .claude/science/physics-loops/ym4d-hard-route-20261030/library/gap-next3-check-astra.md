# Repo search

Codex, gpt-6-astra, xhigh; 2026-11-13; checkout `1a1abdd9e36cce1f602cba66965611c957cd4495`. Check of Claude Fable 5.2's FINISH row 898, commissioned by row 902. Research text, not an audit; no status grant.

Before derivation I searched `/Users/jonreilly/Projects/Physics` with bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head` commands. Refs and revisions: `origin/main` = `7fc6b1a3e6444d74c873c3ffc111b9ad0f4fe172`; `pr/10114` = `f76f6c649cff7dffbab664d8976e680e8f287fe9`; `pr/10133` = `89faef229ff6e6bde42baad15ed8270c2f4087d8`; `pr/10134` = `1e70c7211a2cdbc39001e619f1dd89db45e25851`; `pr/10141` = `c73ad7b177d94f89ff37b77386936e3d52b48b05`.

- Terms: `free[- ]wall`, word-bounded `WALL-[12]` and `W-ENG`, `super[- ]?multiplicativ`, `Corollary S2`, `FLUX-Z2`, `THERM-DI`, `UNIV-FP`. The completed narrow query hit only `archive_unlanded/historic_intake_originals/branch01/266_COUPLED_OS_INTERIOR_DESCENT_SUBSEQUENTIAL_INFINITE_TIME_TRANSFER_BOUNDED_THEOREM_NOTE_2026-07-12.md:442`, on all five refs. Its exact table statement is “Single-step positivity fails but a blocked positive channel exists.” This is a different free two-step transfer problem; it supplies no wall or seed inequality here.
- A completed method query, `thermal sum|wall overlap|Mack.Petkova|supermultiplicativ`, returned no hits on those five refs. Earlier broader queries hit unrelated firewall, law-engine, seed and plane-flip records and reached their caps. Those capped searches establish no absence claim.
- In this checkout the relevant prior results are `gap-crux-restate.md:127–144,176–205`: Proposition N's positive noninteger spectral-weight counterexample, Lemmas K/X/E, Theorem S and Corollary S2. Their exact relevant content is: positive spectral weights alone do not give the doubling estimate; symmetric **trace** families do, and S2 gives `S(2n;4n) <= ((1+S(n;2n))^4-1)^2`. The new vector example uses Proposition N's Poisson-weight mechanism. Credit that prior argument; this check does not claim a new obstruction method.
- `gap-zero-transport-check.md:168–193`, by Claude Opus 5.5, already gives `(TM_B)`: positive trace-class free-space transfer, simple positive top eigenvector, and `Z(k,B)=Tr T_B^k`. It supplies the transfer input that row 898 calls merely ARGUED. Its proof ports `gap-transfer.md` and Sussman–Alpoge's GL3/GL8. No new transfer-construction lane is needed.
- `gap-mine858-opus.md:125–138`, by Claude Opus 5.5, states the unproved vector `(W-ENG)` with a gap on **every** larger box, and asks whether fixed-horizon universality controls the first-passage seed. It explicitly retains the free-wall/account-state bridge. This is the immediate target, not a previous proof of it.

`prior/gap-next3-check-astra.md` is absent. The November 8 repository digest concerns earlier UV matching targets, not these seed inequalities. The registry has no match for `gap-next3`, free walls, `WALL-1/2`, `W-ENG`, `GLUE-1` or `UNIV-FP`. This is the commissioned check of row 898, not a competing proof lane for its open inputs.

The outline index was used first: README; chunk-02:90–108 and neighbouring transfer rows; chunk-01:62–73; obligations:24,27,156. The cited source reads are `YM4_sketch_500.tex:2195–2257,2313–2336,588–599`, at the supplied `31a47c543775` revision. GL3 gives positive, factorially decaying convolution eigenvalues; GL8 gives the torus trace using normalized gauge Haar measure. The outline separately requires a positive spectral gap estimate. These are credited inputs, not proofs of WALL-1/2. Balaban is not used as an unseen supplier.

The `/sa` directory is a source export without Git metadata; `31a47c543775` is the supplied provenance, not a revision independently verified there. The actual cited text was read. No numerical run or computer-assisted step discharges a proof obligation.

## Conventions and transfer input

Below, line references without a filename refer to `gap-next3-max.md` at the pinned checkout. Use its **unnormalized** plaquette weight `exp(beta x_p)`, real `beta >= 0`, Haar probability, and unrestricted gauge transformations at free boundaries. Periodic directions have at least three sites; this avoids degenerate plaquettes with repeated links. Free directions count sites, so free propagation has exponent `b-1`. All statements concern finite bare-Wilson boxes unless further hypotheses are named.

The existing `(TM_B)` construction applies to the mixed cylinder as well: changing the finite spatial graph changes its bond and plaquette lists, not its factorization. Multiplying from `exp[-beta(1-x_p)]` to this note's weight multiplies the transfer by a positive scalar. Positivity, simplicity, normalized spectra and gauge projection survive. For the space channel, `v_a=B_0^(1/2)>0` and its positive Perron vector have strictly positive inner product; hence `w_0(a)>0`. This fills the named input in FW5, without assuming a wall estimate.

## FW1 — HOLDS (line 402)

The displayed site transformation multiplies an edge by `Omega(x)Omega(y)`. This is `-1` exactly on the cut edges, including for the reverse orientation. There is no wrapping edge returning across the free boundary. Gauge averaging therefore makes the flip the identity on the physical transfer space. With all three spatial directions free, no nontrivial spatial electric centre-flip sector remains.

“No twist” means no nontrivial global centre twist of the cylinder: its spatial box is contractible and spacetime has only the periodic time circle. Equivalently, the would-be temporal twist trace is `Tr(M^a C)=Tr(M^a)`. It does not say that arbitrary plaquette sign defects or fixed boundary charges are absent. No fixed boundary gauge condition or charged boundary Hilbert space is present here. First failing step: none within this scope.

## FW2 — HOLDS (line 404: free-side super-multiplicativity)

The two disjoint site boxes contain all noncrossing links. Add the cut links with independent Haar probability. This gives the exact ratio

\[
\frac{Z(b_1+b_2)}{Z(b_1)Z(b_2)}
=\mathbb E_{\mathrm{cut}}\exp\!\left(\beta\sum_{p\text{ crossing}}x_p\right).
\]

Each ordinary crossing plaquette contains two distinct cut links, each occurring once. Integrating either one first gives `E_cut x_p=0`, since the Haar integral of the fundamental matrix is zero. Independence between different plaquettes is unnecessary. Jensen gives the asserted lower bound. Dividing its logarithm by the periodic time length and taking that length to infinity gives `e(b_1+b_2)>=e(b_1)+e(b_2)`. The transfer trace converges to its top logarithmic eigenvalue at each fixed spatial box. First failing step: none.

Keep the stated weight normalization. With `exp[-beta(1-x_p)]`, the ratio acquires `exp(-beta #crossing plaquettes)`; the same raw super-multiplicativity statement would not hold in that convention.

## FW3 — HOLDS (line 406: finite wall cost, signs and monotonicity)

For fixed time length, the crossed representation is a positive spectral moment in `b-1`. Cauchy–Schwarz gives `W(a,b)^2<=W(a,b-1)W(a,b+1)`. Its logarithm divided by `a`, followed by `a -> infinity`, proves discrete convexity of `e(b)`.

FW2 and the linear bound from `|x_p|<=1` give a finite superadditive limit `f=lim e(b)/b=sup e(b)/b`. Thus `D(b)=fb-e(b)>=0`. Convexity of `e` makes `D` concave. A negative increment of a concave sequence persists or becomes more negative; it would contradict `D>=0`. Hence `D` is nondecreasing.

For free transverse sides `c,d`, the cut has `aN` plaquettes, with `N=cd+(c-1)d+c(d-1)`. Their exponential is at most `exp(beta aN)`. Therefore

\[
e(b_1+b_2)\le e(b_1)+e(b_2)+\beta N,
\quad e(qb)\le q e(b)+(q-1)\beta N.
\]

Divide the second inequality by `q` and let `q -> infinity`: `fb<=e(b)+beta N`. Consequently `0<=D(b)<=beta N`, `D_inf` exists, and `delta_e(b)=D_inf-D(b)>=0` decreases to zero. The stated decomposition `e(b)=fb-D_inf+delta_e(b)` follows. “Finite” here is at fixed transverse box and coupling; this is not a transverse-volume-uniform wall bound. The superadditive sign differs from periodic Lemma K; `delta_e` itself is nonnegative and decreasing. First failing step: none.

## FW4 — HOLDS (line 408: the seed box only)

List eigenvalues with multiplicity and remove the one simple Perron eigenvalue. Every remaining normalized eigenvalue contributes once to `S(a;B)`. Thus `exp[-a m(B)]<=S(a;B)` and `m(B)>=a^(-1)log(1/S(a;B))`. If `S=0`, the transfer has rank one and the gap is infinite in this convention. A positive lower bound requires `S<1`. This is a statement about that box alone. First failing step: none.

## Vector counterexample — HOLDS in the stated abstract class (section 6.2)

Fix the other three lengths and write `N=z^2 bcd`, with `A` the coefficient of `t` displayed in the author’s formula. Then

\[
Z(t)=e^{At-N}\exp(Ne^{-mt})
=\sum_{k\ge0}e^{-N}\frac{N^k}{k!}(e^{A-mk})^t.
\]

This is exactly the spectral measure of the unit vector with coordinates `sqrt(e^{-N}N^k/k!)` for the positive diagonal operator with eigenvalues `e^{A-mk}`. The operator is trace class; every coordinate is nonzero, so its cyclic space contains every eigenvector. Its gap is exactly `m`. The formula extends to `t=0` with `Z(0)=1`. Axis symmetry is explicit. The superadditivity difference is `N(1-e^{-mt})(1-e^{-mt'})>=0`. Dividing by the top contribution gives `S_W=exp(Ne^{-mt})-1`.

Choose `0<s<min(s_W,1,1/C)`, `N_0>=3`, `z^2=s/(16N_0^3)`, and `0<mu<log(1/(Cs))`, with `m=mu/N_0`. At `(t;b,c,d)=(N_0;2N_0,2N_0,2N_0)`, `N=s/2` and

\[
S_W=e^{(s/2)e^{-\mu}}-1<e^{s/2}-1<s.
\]

The last strict inequality follows from `log(1+s)=int_0^s (1+u)^(-1)du>s/2`. Every larger box still has gap `m`, below `N_0^(-1)log(1/(C S_W))`. Thus no such universal implication follows from these spectral and symmetry properties.

Scope matters: this is not a local Wilson counterexample, nor a family of mixed-boundary **trace** partition functions. Physical free-time vectors are `B_0^(1/2)`, with exponent `n-1` and generally nonunit norm. The normalized abstract class is a counterexample to positivity/axis-exchange reasoning, not a literal characterization of every property of the Wilson family. Its small-overlap mechanism is already present in Proposition N of `gap-crux-restate.md`; the normalized vector realization is the new application checked here. The note correctly leaves the Wilson `(W-ENG)` unresolved. Its separate warning about the cyclic space is also correct: it need not contain `A Omega` for local observables `A`.

## FW5 — HOLDS (lines 438–440: crossing identity)

At each fixed `a,c,d`, the crossed transfer is positive and has positive top overlap, as above. Hence

\[
\gamma(b,a)=\log\!\left(1+\sum_{j\ge1}
\frac{w_j(a)}{w_0(a)}(r_j(a)/r_0(a))^{b-1}\right)
\]

is nonnegative, nonincreasing and bounded for `b>=1`. Equating the two exact partition functions gives

\[
ae(b)+g(a,b)=(b-1)\epsilon(a)+\omega(a)+\gamma(b,a).
\]

Division by `b` and FW3 give `p(a)=epsilon(a)-af=lim_b g(a,b)/b>=0`. Substitution, with the author's `c(a)=omega(a)-a(f-D_inf)`, gives exactly

\[
g(a,b)=(b-1)p(a)+c(a)+\gamma(b,a)-a\delta_e(b).
\]

The minus sign and the `b-1` are correct. No sign for `c(a)` follows. All limits hold with the other sides and coupling fixed. First failing step: none.

## FW6 — HOLDS (lines 443–445: enlargement at fixed time)

Spectral calculus gives `0<=R_a^h<=r_0(a)^h I`, for integer `h>=1`. Applied inside the positive moment, this yields `W(a,b+h)<=r_0(a)^h W(a,b)`. Subtract `a[e(b+h)-e(b)]` from the logarithmic inequality. FW3 and `epsilon-af=p` give

\[
g(a,b+h)-g(a,b)
\le hp(a)+a[\delta_e(b)-\delta_e(b+h)]
\le hp(a)+a\delta_e(b).
\]

Both inequalities have the stated direction. No wall term was silently discarded; its constant part cancels. First failing step: none.

## Tube corollary — HOLDS (line 456)

For fixed free sides `c,d`, exchange of the two periodic axes preserves the same partition function. Each channel is a positive trace-class transfer with simple top eigenvalue. The plaquette bound gives finite `inf log W(a,b)/(ab)`. These are precisely the hypotheses of the existing Corollary S2; reuse it.

Writing `s=S(n;2n)` and `n_k=2^k n`, the asserted one-step estimate and `s<=1/20` give

\[
S(n_k;2n_k)\le (19s)^{2^k}/19,
\qquad m(2n_k;c,d)\ge n^{-1}\log(1/(19s)).
\]

Here `S(n_k;2n_k)` abbreviates the spatial cross-section `(2n_k,c,d)`, with only its first side periodic. Thus there is one spatial winding direction and one electric flip; no magnetic two-cycle of the spatial cross-section remains. The two free sides never enlarge. This is the stated tube result, not a four-dimensional volume theorem. The sentence that its thermal sum “grows with cd” is physical motivation, not a proved monotonicity theorem, and is unnecessary to this conclusion.

## Conditional WALL engine — HOLDS AFTER CORRECTION (sections 6.3, 5.2)

The algebraic recursion is correct. State its domain and constants explicitly. Assume nonnegative absolute `C_1,C_2` supply WALL-1/2 for **every** mixed rectangle used below, at the same coupling, with `3<=a<=b/2` and the two spectator sides at least `b`. Put

\[
k=1+C_1+C_2,\qquad A=k^3,\qquad B=4A^2.
\]

FW6 with `h=b` gives `g(a,2b;c,d)<=k g(a,b;c,d)`. Starting from `(b,b,b)`, enlarge one free side at a time. The next side to enlarge is still `b`; both its spectators are at least `b`. Thus all three applications are admitted and

\[
1+S(a;(2b)^3)\le (1+S(a;b^3))^A,
\quad S(2a;(2b)^3)\le[(1+S(a;b^3))^A-1]^2.
\]

If `0<=x<=1/B`, then `Ax<=1/(4A)<=1/4`, and
`(1+x)^A-1<=e^{Ax}-1<=Ax e^{Ax}<=2Ax`.
The last bound follows, for example, from `e^u<=1/(1-u)<=4/3<2` for `0<=u<=1/4`. Hence `s_{j+1}<=B s_j^2`. For a seed `0<s_0<1/B`, induction proves

\[
s_j\le (B s_0)^{2^j}/B,
\qquad m((2^j b)^3)\ge \frac{\log(1/(B s_0))}{a}
\quad(j\ge0).
\]

The `s_0=0` case is the rank-one case. No computer arithmetic is used.

**Required correction.** This proves the dyadic-cube conclusion actually stated in section 5.2. It does **not** prove C1's earlier `(W'-ENG)` conclusion on every box with all sides at least `b`. No free-boundary monotonicity or covering argument supplies that stronger quantifier here. Use the dyadic theorem above. The passage to local correlations and identification with the account's state remain separate, as the author acknowledges. Finally, this is conditional on WALL-1/2 for the literal Wilson family; it does not automatically extend FW2/3 to the nonlocal effective action at first passage.

## Attack 1 fact tests — HOLDS AFTER CORRECTION

The dyadic implication is a valid conditional research target, as proved above. It has not passed all four fact tests as defined at the start of the source note.

- **F1:** pending for the named interacting U(1) comparison. A group-independent engine is not itself required to fail; some premise or the seed must fail in a model with the same gapless conclusion. The quoted photon estimates are GUIDE. They do not prove failure of this exact free-wall seed, or supply its limit-state bridge.
- **F2:** the free-wall topology distinction is sound. In the strictly frozen finite-group box, every flat field is gauge equivalent to the trivial field, so the flat physical space is one-dimensional. The extra periodic holonomy states used against an even **torus** trace are absent. This does not assert a uniform estimate at the quoted finite freezing couplings.
- **F3:** passes structurally. WALL-1/2 are unconditioned inequalities; they invoke none of the forbidden worst-case response bounds.
- **F4:** not met. Removing one seed component supplies no known method for the remaining order-one glue number. The author explicitly admits this. Keep attack 1 as an engine-development proposal, not as an attack already meeting F4.

The suggested free-scalar calculation is a sensible test of a proposed universal-class theorem. A scalar failure, however, would not by itself refute a **Wilson-specific** engine; scalar success would not prove it. The guide calculations in section 5.2 are not proofs of WALL-1/2. No such test or new proof lane is run here.

The final “independence” sentence must also retain its inputs: attack 1 uses the Wilson cut identity and the unproved WALL bounds, not positivity and axis exchange alone. No counterexample in section 6.2 proves the trace WALL bounds impossible.

## Attack 2: FLUX-Z2 — FAILS with the printed “every torus” quantifier

The author's self-correction at line 532 already notices the missing number of surface positions. It absorbs that number on `(a,b,b,b)`. That does not repair the unrestricted quantifier at lines 497 and 562. Here is a hand-checkable counterexample within its stated SU(2) family, with the centre-blind part set to zero.

Take a rectangular periodic Wilson lattice `(a,b,c,d)`, all lengths at least three, and the `(1,2)` centre twist. Fix `a,b`, put `A=ab`, and let `c,d` be arbitrary. At any fixed such finite lattice the integrals are analytic near `beta_F=0`. Their leading twist-sensitive term gives

\[
1-\frac{Z^v}{Z^0}
=2cd\left(\frac{\beta_F}{4}\right)^A+O(\beta_F^{A+1}). \tag{FZ}
\]

Details of the coefficient, without enumeration:

1. Expand each `exp(beta_F x_p)` in its Taylor series. Under the substitution `U_e -> -U_e`, a nonzero Haar integral must have even total incidence at each edge. Plaquettes with odd multiplicity therefore form a closed mod-two surface. Twisting changes exactly the terms whose surface pairs oddly with the twist.
2. Project such a surface to the `(1,2)` torus. Its mod-two two-cycle has degree one. Every one of the `ab` base faces must occur at least once. Hence the total Taylor degree is at least `A`. At degree exactly `A`, there are no repeated faces or faces of other orientations. Closure forces one flat `(1,2)` plane, at a fixed transverse site. There are exactly `cd` such planes.
3. Each plane contributes `4^(-A)`: write `x_p=chi_(1/2)(U_p)/2` and orient the faces consistently. Haar orthogonality on each edge contributes `1/2`; contraction leaves one dimension factor `2` per vertex. Since the torus has `E=2A` and `V=A`, `int prod_p chi_(1/2)(U_p)=2^(V-E)=2^(-A)`. The `A` normalized traces contribute the other `2^(-A)`. A twisted plane changes sign, giving the factor two in (FZ).
4. All lower coefficients of `Z^0-Z^v` vanish and `Z^0(0)=1`, so division by `Z^0` preserves this leading coefficient. The remainder is for this fixed finite lattice; no volume-uniform Taylor assertion is needed.

For any proposed universal `C`, choose `c,d` so `2cd/4^A>C^A`. Then take a sufficiently small positive `beta_F`. Since `tanh(beta_F)/beta_F -> 1`, (FZ) gives

\[
1-Z^v/Z^0>(C\tanh\beta_F)^A,
\qquad C\tanh\beta_F<1.
\]

This contradicts FLUX-Z2 as printed. It is the transverse-position factor, not a failure of the strong-coupling idea.

**Surviving repair, not proved here:** retain a volume/position prefactor in a convergent connected expansion, or restrict the torus shapes before absorbing it into `C^A`. Line 532 proposes just this for `(a,b,b,b)`. Its signed-activity cluster estimate still needs a proof with denominator/control constants; positivity of the two final partition functions alone does not bound their ratio. This check does not refute the restricted-shape proposal.

## Attack 2: universality, multiplet and fact tests — FAILS as a passed route

**UNIV-FP remains an open question, not a supplied port.** Row 900 quotes a fixed-horizon result from the later `YM4_1400.tex`; that file and revision are outside the allowed source corpus. I did not open it or infer its theorem from a quotation. Searches of the supplied full-account index and raw I–III for `hrt-regular-trajectory`, `different horizons`, `fixed-horizon` and `universality` locate no matching fixed-horizon supplier. The last term has unrelated short-distance/universality mentions. The bounded primary read CA-I:470–489 specifies the bare density `rho_0=exp[-g_0^(-2)A(U)]` and its Wilson measure, not the proposed mixed-weight family. Consequently no mixed-weight, first-passage, K-uniform **seed** comparison is supplied by these sources. This is a missing input, not a theorem that such universality is impossible.

**MULTIPLET is also only a proposed theorem.** Topology can list eight `H^2(T^3,Z_2)` classes for an appropriate SO(3) bundle problem. That count does not prove eight low eigenstates, their isolation, or their exponentially small splitting for the lattice measure being used. One needs the spectral premise and a consumer subtracting the appropriate whole multiplet. Neither is proved here. A small fundamental twist deficit supplies no such premise by itself.

**F1's stated reason is false.** U(1) has the exact quotient `U(1)/{+1,-1} ~= U(1)`, represented by the squaring map. Write a link as `e^{i theta}=z e^{i phi}`, choosing a representative modulo pi. For a fundamental cosine term and any part invariant under link signs,

\[
\cos\theta_p=(dz)_p\cos\widetilde\theta_p,
\qquad |K_p|=|\beta_F\cos\widetilde\theta_p|\le\beta_F.
\]

Thus precisely the same bounded conditional Z2 coupling exists. “U(1) has no centre quotient of this kind” cannot justify a PASS. This does not refute a flux-only comparison: such a comparison can coexist with a gapless quotient sector. The full glue-plus-flux route must supply the discrimination.

F2 is appropriately retested for the **changed mixed measure**, rather than imported from Wilson confinement. Passing its flux part for Q8/2T would not prove a glue seed. F3 is structurally acceptable if the signed expansion is proved within its actual small-`beta_F` range. F4 is **conditional and unverified**: the unrestricted FLUX-Z2 is false, its restricted-shape repair is unproved here, and UNIV-FP and MULTIPLET have no suppliers. Mack–Petkova and Fröhlich are credited as the note's recalled method, not silently imported as proofs of these quantified statements.

## Attack 3: mean transport implication — HOLDS AFTER CORRECTION

Reuse `gap-glue-check-astra.md:334–400`: the thermal inequality is weaker than the all-level logarithmic-derivative hypothesis, and a box-uniform comparison gives only a fixed-bare-coupling seed without a cutoff bridge. The relevant elementary calculation is as follows.

Fix the **spatial box B**, the Hilbert space and an invariant sector. Write its normalized energies as `E_j(s)`, including `E_0=0`, and

\[
X(s,t;B)=\log\sum_j e^{-tE_j(s)}.
\]

Whenever the differentiated sums are justified,

\[
\partial_s X=-t\langle E'_j\rangle_{s,t},\qquad
\partial_t X=-\langle E_j\rangle_{s,t}.
\]

Thus THERM-DI is exactly `-<E'_j><=C(s)<E_j>`, not a bound on each level. If it holds throughout a path for all the required times and boxes, with integrable box-independent `C>=0`, let `t'(s)=C(s)t(s)`. Then `d_s X(s,t(s);B)<=0`, and

\[
X(s_1,t;B)\le X\left(s_0,t\exp[-\int_{s_0}^{s_1}C(s)\,ds];B\right).
\]

This is the usable conditional comparison. The spatial enlargement/initial-seed family still has to be supplied, as in the cited TR1 repair.

**Corrections:** `partial_t` holds B fixed; it is not differentiation along `b=rt`. C5's “fixed lattice shape ratio” reading would include spatial-size variation and is not the displayed energy identity. For decreasing pin strength use a path coordinate increasing towards the unpinned endpoint; changing its orientation changes the derivative sign. For first passage, a finite-interval constant is insufficient: the physical time dilation and initial-size constants must stay bounded along the cutoff sequence. Absence of a phase transition is not equivalent to this quantitative thermal derivative bound.

## Attack 3: pin path and fact tests — FAILS as stated

**The pin path lacks the claimed even-sector spectral family.** The cited primary source `gap-exit-max.md:462–513` proves the exact HL identity for the **full pinned partition function**, then bounds differences of local pin expectations in its strong-coupling/strong-pinning regions. It does not define a conserved pure-gauge centre-even sector along that path. The pin factor is

\[
\exp\left(q\sum_\ell \tfrac12\operatorname{tr}U_\ell\right).
\]

Under a centre flip, its cut-link terms change sign. Its ratio is `exp[-2q sum_(cut links) x_l]`, generally different from one. The fixed fundamental pin therefore breaks the flip symmetry. One cannot track `S_ev` as a sum of eigenvalues in that invariant sector for `q>0` using HL. Keeping `V=1` removes a supremum; it does not restore the symmetry. A full-trace pinned transport, or a separately justified projected quantity and consumer, is a possible repair, not a supplied glue-only reduction.

**F2's periodic finite-group exemption was already refuted.** No new attack on it is made here. Read and reuse `gap-crux-exercise2-check-astra.md:227–266`, repeated correctly in `gap-glue-check-astra.md:404–421`. The flat triples `(1,1,1)` and `(i,1,1)` for Q8 and 2T remain inequivalent under conjugation and central flips. Their even flat space therefore has dimension at least two. The prior hand bound is

\[
S_{\rm ev}(t;B)\ge\left(\frac{1-\eta}{1+\eta}\right)^t\ge\frac12,
\quad
\beta\ge d_G^{-1}\log(16E(|G|-1)t),
\]

with `eta=(1+(|G|-1)e^{-beta d_G})^E-1+e^{-beta d_G}`, `d_Q8=1`, `d_2T=1/2`. This defeats the blanket reason “frozen finite groups are gapped, so F2 is not needed for glue.” A local gap does not eliminate extra even torus states. The witness concerns each fixed box at sufficiently large beta; it does not settle every box at one fixed beta or the numerical band `[2.3,2.6]`. Attack 3's literal periodic `S_ev` must retain this test. The free-wall alternative has the different topology discussed under attack 1.

**F1:** a genuinely gapless same-sector endpoint would obstruct uniform transport from a uniform initial gap. But the named Villain input does not establish the needed free-wall/even-transfer statement here. Its primary text, `gap-tu-retry.md:231–255`, proves nonsummability of a plaquette score in periodic local limits and explicitly says its ensuing bridge is Langevin, “not the transfer-operator bridge.” The source's proposed Villain calculation is future work. No PASS follows from the transition names or quoted guide numbers.

**F3:** the mean inequality at a fixed invariant spectral family uses no forbidden supremum and passes this structural test. The pin-sector problem must first be repaired. **F4:** not met: there is neither a proved order-one supplier for THERM-DI nor a first-passage comparison. As the author admits, a successful finite-interval argument would first give a bare-coupling result.

Thus the coupling-path **conditional** comparison survives. The proposed pin-path identification and the assertion that the selected attacks already pass their fact tests do not.

## Verdict table and scope

| Statement | Verdict | Exact scope or correction |
|---|---|---|
| FW1 | HOLDS | Unrestricted boundary gauge group; global centre sectors/twists |
| FW2 | HOLDS | Literal Wilson weight `exp(beta x)`; ordinary plaquettes |
| FW3 | HOLDS | Finite wall cost at fixed transverse box; both monotonicities as stated |
| FW4 | HOLDS | Gap of the seed box itself |
| FW5 | HOLDS | Positive top wall overlap supplied by the existing transfer construction |
| FW6 | HOLDS | One free-side enlargement, with both residual terms retained |
| Vector counterexample | HOLDS | Abstract positive moment family; not a Wilson counterexample |
| Tube corollary | HOLDS | Two fixed free sides; existing S2 reused |
| Conditional WALL engine | HOLDS AFTER CORRECTION | Dyadic cubes; `s_0<1/[4(1+C_1+C_2)^6]`; no every-box conclusion |
| Attack 1 fact-test assessment | HOLDS AFTER CORRECTION | F1 pending, F2 topology distinction valid, F3 passes, F4 not met |
| FLUX-Z2 for every torus | FAILS | Exact small-coupling coefficient (FZ); restricted-shape repair remains open |
| Attack 2 fact-test assessment | FAILS | U(1) quotient exists; UNIV-FP and multiplet suppliers missing |
| Mean thermal comparison | HOLDS AFTER CORRECTION | Fixed spatial box, invariant sector, correct path orientation and differentiability |
| Attack 3 pin-path/fact-test assessment | FAILS | Pin breaks centre flip; periodic finite-group exemption already refuted; F1/F4 not established |

This checks the requested new statements line by line and reuses the cited prior results. It does not recheck the whole row digest, the account, unavailable literature, guide phase diagrams or subjective success probabilities. Only this output file was written. The author note, FINISH, registry, ledgers and refs were not edited. No numerical proof, audit, commit, push or outward post was performed; the file is local and uncommitted in the requested pinned checkout.

RESULT: FW1–FW6, the abstract vector counterexample and the tube corollary HOLD; the conditional WALL engine HOLDS AFTER CORRECTION to dyadic cubes with explicit constants. The three-attack fact-test endorsement FAILS as stated: unrestricted FLUX-Z2 is false, U(1) has the asserted quotient, the periodic Q8/2T exemption is already refuted, and the pin path has no conserved pure-gauge even sector. WALL-1/2, restricted-shape flux control, UNIV-FP, MULTIPLET, THERM-DI and every order-one/first-passage seed remain open; no mass gap or scientific status is granted.
