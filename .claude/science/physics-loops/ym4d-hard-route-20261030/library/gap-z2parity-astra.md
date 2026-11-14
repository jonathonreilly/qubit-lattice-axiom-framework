# Repo search

READ — The target-specific prior record is absent at `d17e0d63fe6a748ae144149598592635cf2240a6`.
The November 8 lead digest concerns large-field/history work. It does not establish a parity estimate.
Its nearest hit, the one-step Wilson witness, is already consumed by the later gap lanes.
I read that witness on fetched PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md:89–166`, under
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
It proves a local positive lower bound, not suppression of electric flux.
I also read `checks/review_massgap_block_literature.md:112–121` there.
Its common-interpolation warning applies to comparing twisted normalizers; it supplies no bound.
Credit those Codex sources. PR 10114 remains `f76f6c649cff7dffbab664d8976e680e8f287fe9`.

READ — Current main is `f07a5b9fc623c34517f8915bb2d3ab9cfe57ce78`.
Its `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:1–110`
concerns a supplied finite-clock Villain law, not this SU(2) parity law.
No assertion from its unreviewed proof is imported.
The existing flux-literature digest, `prior/gap-lit-flux.md:3–69`, records the other PR searches
and separates Fourier identities and conditional confinement criteria from estimates.
The earlier vortex probe, `gap-vortex-astra.md:1–82`, records its source-level follow-up.
These are search records, not evidence that no differently named result exists.

A targeted search of main and the available PR 10114/10133/10134/10141 refs also checked
cycle homology, random currents, local indistinguishability and singlet pairings.
Main's `FINITE_CLOCK_TRANSFER_DISORDER_AND_SPECTRAL_GAP_PERIMETER_BOUNDED_THEOREM_NOTE_2026-09-14.md:304–321`
(under `docs/`) names a local-indistinguishability *hypothesis* for a different clock-model argument.
`docs/CLOCK_PENALTY_LOCAL_NORMAL_FORM_AND_SIMULTANEOUS_GROUND_STATE_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-14.md:434–450`
warns that a neutral constraint space does not itself have that property.
The connected-edge-code note at
`archive/notes/docs/work_history/repo/review_feedback/CONNECTED_EDGE_CODE_ODD_SECTOR_JOIN_CYCLE265_NOTE_2026-07-17.md:494–520`
proposes a parity-reference code; it does not prove this cycle-law estimate.
`docs/GAUGE_VACUUM_PLAQUETTE_WINDOW_INTERTWINER_BASIS_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md:66–119`
contains SU(3) pairing algebra, not this SU(2) winding estimate. No theorem from these hits is imported.
The broad logs, including incidental word/number matches, remain in the scratch directory.
Only main and PR 10114 were freshly fetched for these source checks; the other PR refs
are the recorded local refs, not a claim about their live remote heads.

READ — Close local prior work is `gap-expose-astra.md:88–151,575–617` (exact sector projections
and the consumer), `gap-hs-max.md:98–119,166–208,246–250` (OS, P1, P2, and the open target),
and `gap-crux-restate.md:287–295` (the exact SU(2)/SO(3) centre split).
The split is already done and will not be counted as new.
Credit Claude Fable 5.2 for row 860 and the centre-split source, and Codex for the exposure source.
The twist estimate and common-normalizer comparison remain explicitly open in
`gap-vortex-astra.md:511–611,612–650`, read at this pin.

READ — Searches of `open-registry.md`, `open-core.md` and `l17c.md` for the target,
half-integer cycles, odd sectors and (E17) found no separate owner.
FINISH row 866 assigns this global parity probe. Row 867 assigns a different local
SU(2)/U(1) separation probe; this file does not take over that task.

# Parity proof probe

Research text only; no scientific or audit status is granted. This file records the probe as it proceeds. No computation will discharge a proof obligation.

Author: Codex, configured model and effort; row 866, slot repo2e.
`PROVED` means a written argument by this author, not an independent check or repository standing.
`READ` names source evidence; `ARGUED` marks an interpretation; `GUIDE` is non-proof evidence;
`OPEN` marks an unproved statement. Only this output file is changed.

## Step 1. Sources, contract, and the carrying statement

READ — The requested GOAL and FINISH sections were read. Main's workflow now points to
RULES, SETTINGS and `procedures/research.md`; those and the planning-branch entry were read.
The task's pinned checkout and output-only scope control this probe.
The two requested source downloads were made once, into the newly created directory
`/tmp/sa-gap-z2parity-astra.lP7d0J/`.
They are `sa_ym4.tex` and `sa_ca_I.tex`, both from commit `31a47c543775`.

READ — Index lookup preceded source reading: `sa-index/README.md:1–10`,
`chunk-01.md:57–74`, `chunk-02.md:74–105`, and `obligations.md:17–29`.
Searches included half-integer, odd sector, twist, centre/center, flux, random current and mass gap.
The CA 4.12–4.19 hits concern bond-orientation parity and background twists, not electric-flux parity.
Outline 565–600 separates scalar clustering from a spectral gap; 2195–2243 supplies
the positive one-bond character coefficients; 2313–2335 supplies the positive transfer trace.
These existing proofs are inputs, not work to redo.
Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**.

ARGUED — The parity statement is the correct carrying statement for (E17), by the already
proved identities P1 and (E3). It is exactly the original centre-charged trace problem.
It is not an estimate supplied by high-spin rarity. P2 retains essentially the whole problem.
It is also stronger than the actual sufficient consumer (FQ); neither is itself a complete mass-gap proof.

Let \(\Lambda=(\mathbb Z/a)^2\times(\mathbb Z/c)\times(\mathbb Z/d)\), with
\(a\ge3\), \(c,d\in\{a,2a\}\), time direction 1 and time period \(a\)
(`gap-ext-astra.md:78–128`).
For its allowed spatial twist \(m\) and cut cocycle \(\omega_i\), \(i=3,4\), write
\[
 q_{m,i}(a)=\frac{\operatorname{Tr}(P_{-,i}L_m^a)}{\operatorname{Tr}L_m^a}
 =\Pr_{m,a}\{\langle\omega_i,C\rangle=1\}
 =\frac{1-Z^{m+v_{1i}}/Z^m}{2}.
\]
Here \(C\) is the mod-two cycle of half-integer spatial spins in the one-slice spectral law.
Only its pairing with the chosen cocycle is fixed; this is not a claim about every homology component.
OPEN — At a fixed order-one coupling, prove uniformly over those tori and twists
\[
 \max_{m_2=0,\ i=3,4}q_{m,i}(a)\le C_0a^p\eta_*^{a/2}.
 \tag{P}
\]
The number \(0<\eta_*<1\) is the consumer's lower-bound constant, not a newly fitted rate.
For an interval of couplings, all constants must be uniform on that interval.

GUIDE — The stated density near 0.33 and possible percolation motivate avoiding a dilute-path argument.
Neither the density nor percolation is used as a premise. No numerical run is planned.
The worst-case caps and the failure of (AN1) are retained as supplied route constraints.

Next: examine the positive one-slice law versus the signed objects produced by centre conditioning;
then attempt an actual normalized comparison rather than another local-density estimate.

## Step 2. What positivity survives a change of representation

READ — A closer search found `gap-kappa-order.md:35–60`, Proposition SC and Lemma NP.
These already give the closed-surface expansion and an explicit negative SO(3)-environment weight.
`gap-means-max.md:65–102` additionally gives the pseudoreal Haar sign and a proposed
92-plaquette negative surface. That geometric construction is not rechecked here and is not a premise.
The elementary identity \(\int\chi_{1/2}(g^2)\,dg=-1\) follows there from
\(\chi_{1/2}(g^2)=\chi_{1/2}(g)^2-2\) and character orthogonality.
Credit Claude Fable 5.2. Neither the split nor its sign obstruction is new work in this probe.

PROVED — **The three probability objects must be distinguished.**
For an edge-parity cycle \(b\), put
\[
 w_{m,a}(b)=\operatorname{Tr}(E_bL_m^a).
\]
This is nonnegative: it is
\(\operatorname{Tr}(L_m^{a/2}E_bL_m^{a/2})\).
For even \(a\), it is also \(\|E_bL_m^{a/2}\|_{\rm HS}^2\).
Thus the one-slice cycle law is an honest probability after division by \(Z^m\).
It does not follow that its fully expanded spacetime histories are nonnegative.
The squared norm sums interfering amplitudes before asserting positivity.

Use the existing centre split. For quotient link field \(q\in SO(3)^{E(\Lambda)}\),
choose lifts \(V\), put \(J_p(q)=\tfrac12\operatorname{tr}V_p\), and define
\[
 D_k(q)=2^{-|E(\Lambda)|}\sum_{z\in\{\pm1\}^{E(\Lambda)}}
 \exp\!\left(\beta\sum_p\eta_{k,p}(\delta z)_pJ_p(q)\right).
\]
Changing the lifts reindexes \(z\). Hence \(D_k\) is well defined and positive.
The prior split gives \(Z^k=\int D_k(q)dq\), with normalized quotient Haar measure.
Writing \(\nu_m(dq)=D_m(q)dq/Z^m\), it follows that
\[
 q_{m,i}(a)=\mathbb E_{\nu_m}\frac{1-D_{m+v}(q)/D_m(q)}2. \tag{S}
\]
This is an average of a **signed deficit**, not generally an average of conditional probabilities.

PROVED consequence of the prior Lemma NP — **The integrand in (S) can be negative.**
Take \(m=0\), \(v=v_{13}\), and the two-seam quaternion configuration of NP,
with its second seam relabelled from direction 2 to direction 3.
Its plaquette traces are \(J_p=\eta_{v,p}\). Therefore
\[
 D_0(q)=Z_{\mathbb Z_2}^{v}(\beta),\qquad
 D_v(q)=Z_{\mathbb Z_2}^{0}(\beta).
\]
For \(\beta>0\), the latter is strictly larger. Indeed the finite expansion is
\[
 Z_{\mathbb Z_2}^{k}=(\cosh\beta)^{|P|}
   \sum_{\partial S=0}(\tanh\beta)^{|S|}(-1)^{\langle k,S\rangle}.
\]
The difference \(Z^0_{\mathbb Z_2}-Z^v_{\mathbb Z_2}\) is twice the strictly positive
sum over surfaces pairing oddly with \(v\); a coordinate 13-torus is one such surface.
Thus the integrand in (S) is negative. Continuity in the lifts gives an open set
of quotient environments with that sign, hence positive \(\nu_0\)-measure.
This extends NP to the particular deficit used in this task; it uses its existing construction.

ARGUED — A proof based on ferromagnetic Z2 domination after conditioning has therefore
lost its premise. Replacing \(J_p\) by \(|J_p|\) discards the relevant signs and also changes
\(D_m\), the measure in (S). No comparison of the original ratio follows without another theorem.
The full nonnegative \(q_{m,i}\) arises only after the environment average.

Fact tests: the split itself works for \(U(1)/\{\pm1\}\) and for \(2T/\{\pm1\}\).
For Z2 alone the quotient is a point and the untwisted couplings are positive.
The two anticommuting seam elements used above also belong to \(2T\).
Consequently their existence distinguishes neither SU(2) from frozen 2T nor a confining phase.
For U(1), those particular anticommuting lifts do not exist; this alone is no upper bound on (S).

OPEN after this step: control the full signed environment average with its actual denominator.
Neither positivity of the slice law nor the centre split supplies that control.

## Step 3. Attempt through loops and local reconnections

PROVED — **Local reconnection cannot remove the class being estimated.**
Suppose two mod-two cycles \(b,b'\) agree outside an embedded contractible box \(B\),
and their difference is supported in its cell complex. Then \(b+b'\) is a cycle in \(B\).
Because \(H_1(B;\mathbb F_2)=0\), it is a boundary in \(B\), hence also in the torus.
Thus \([b]=[b']\). More specifically, any decomposition of the even-degree graph \(b\)
into edge-disjoint loops \(\gamma_j\) satisfies
\[
 \sum_j[\gamma_j]=[b],\qquad
 \sum_j\langle\omega,\gamma_j\rangle=\langle\omega,b\rangle\pmod2.
\]
Changing pairings at vertices changes the loops, not this identity.
When the total pairing is odd, some loop remains odd under every reconnection.
This is a topological constraint, not a statement that pairing choices cannot alter statistical weights.

ARGUED — This locates the failure of the first proposed proof: pair creation, fusion and
annihilation remove pairs of winding contributions, but cannot compare the weights of the two total classes.
A random-current switching argument would need an additional relation between *different* cycles and
their Wilson weights. Drawing loops on a given cycle does not provide it.
It also does not provide a probability law for all spacetime spin-foam terms (Step 2).

PROVED — **Local cycle data can miss an order-one parity weight, even at density exactly 1/3.**
This is an auxiliary cycle model, not a counterexample to Wilson theory.
On \(Q=(\mathbb Z/a)\times(\mathbb Z/c)\times(\mathbb Z/d)\), keep only direction-3 and
direction-4 edges. They form \(a\) disjoint square tori, one at each coordinate-2 slice.
In each square torus let \(\mathcal B\) be the space of boundaries of plaquette 2-chains.
Give each affine coset \(\mathcal B+h\) its uniform distribution.
Let \(\mu_0\) use the zero coset in every plane.
Let \(\mu_1\) use a direction-3 winding coset in one plane and zero cosets in the others.

For any edge \(e\) of a plane, adding the boundary of a plaquette containing \(e\) is a
bijection of each coset and flips \(e\). Its occupancy probability is exactly \(1/2\).
There are \(2acd\) such edges among the \(3acd\) edges of \(Q\), so the mean occupied
edge fraction is exactly \(1/3\), in either law.

Let \(B\) be any rectangular box whose coordinate-3 and coordinate-4 projections each omit a row.
A direction-3 winding loop can be translated to a coordinate-4 line outside \(B\).
Adding that loop maps the zero coset bijectively onto the winding coset without changing any
edge of \(B\). Consequently \(\mu_0\) and \(\mu_1\) have identical cycle marginals on \(B\).
This holds for every such box, including every fixed-size box on sufficiently large tori,
not merely for single edges.
Nevertheless their direction-3 homology parities are respectively zero and one.
The mixtures \(\mu_\theta=(1-\theta)\mu_0+\theta\mu_1\), \(0\le\theta<1/2\), therefore have
identical local cycle data and density, while their odd-sector probabilities equal \(\theta\).

These laws are admissible as positive gauge-invariant SU(2) *density matrices*:
put spin \(1/2\) on occupied edges and spin zero elsewhere.
Every vertex has zero, two or four half-integer incident edges, and hence has an invariant tensor.
Choose a normalized spin network \(\psi_b\) for each cycle; different edge-spin assignments are orthogonal.
Then \(\sum_b\mu_\theta(b)|\psi_b\rangle\langle\psi_b|\) realizes precisely this spin distribution.
High spins are absent. For every spatial cocycle its centre character expectation is either
one or \(1-2\theta>0\). None of this makes the density matrix a Wilson transfer power.

ARGUED — The example excludes a deduction from only local cycle marginals, mean density,
low-spin support, Gauss parity and positivity. It excludes neither a Wilson identity linking
the sector normalizations nor a proof using growing noncontractible observables.
Local plaquette moves also preserve each coset, so even their exact relative weights leave
the relative normalization between homology sectors undetermined in this example.

Fact tests: the topological proof uses only mod-two cycles and holds for Z2 and frozen 2T.
Reducing a U(1) integer current modulo two gives the same identity; U(1) retains the stronger
oriented integer class. Thus topology and reconnection alone pass no confinement-selection test.
The density-matrix example is deliberately not a physical comparison model.

OPEN after this attempt: an actual Wilson comparison between homology sectors.
The next attempt keeps the complete signed sum and cancels the contractible vacuum contributions first.

## Step 4. Best remaining route: mark odd plaquettes before taking the logarithm

READ — The analytic method has a precedent, not a new discovery here:
`gap-seed-sc.md:136–149`, by Claude Fable 5.2, combines an extensive logarithm bound
with a high-order zero and Schwarz's lemma. Its variable is small complex \(\beta\),
and its consumer is a different thermal combination.
Here the variable marks only centre-odd representations, while \(\beta\) stays fixed.
The outline's normalized zero-free lemma is also prior work:
index `chunk-04.md:80–93`, `obligations.md:162`, then outline 4693–4730.
Its warning about exponential volume bounds is relevant; it does not supply the radius below.

Define \(N=|P(\Lambda)|=6a^2cd\),
\[
 d\nu_{\rm ce}(U)=Z_{\rm ce}^{-1}\prod_p\cosh(\beta x_p)\,dU,
 \quad t_p=\tanh(\beta x_p),\quad \tau=\tanh\beta<1,
\]
\[
 \mathcal Z_k(\lambda)=\mathbb E_{\nu_{\rm ce}}
       \prod_p(1+\lambda\eta_{k,p}t_p). \tag{M}
\]
This is a polynomial, with \(\mathcal Z_k(0)=1\) and
\(\mathcal Z_k(1)=Z^k/Z_{\rm ce}\).
For \(0\le\lambda\le1\), its plaquette weight is
\[
 \cosh(\beta x)+\lambda\sinh(\beta x)
 =\frac{1+\lambda}{2}e^{\beta x}+\frac{1-\lambda}{2}e^{-\beta x}>0.
\]
In the character expansion, integer-spin coefficients stay fixed and half-integer coefficients
are multiplied by \(\lambda\). This follows from \(\chi_j(-g)=(-1)^{2j}\chi_j(g)\).
It is an exact interpolation of the specified Wilson action, not a replacement plaquette model at \(\lambda=1\).

PROVED — **The twist-dependent logarithm has a zero of area order.**
The existing surface identity SC gives
\[
 \mathcal Z_k(\lambda)=\sum_{\partial S=0}
       \lambda^{|S|}(-1)^{\langle k,S\rangle}A_{\rm ce}(S),
 \qquad A_{\rm ce}(S)=\mathbb E_{\nu_{\rm ce}}\prod_{p\in S}t_p. \tag{M1}
\]
For completeness, closure follows by flipping one link: the even base measure is unchanged,
and a product with an odd number of incident selected plaquettes changes sign.
No nonnegativity of \(A_{\rm ce}(S)\) is assumed.

If \(\langle v_{1i},S\rangle=1\), project its mod-two 2-chain onto the coordinate \(1i\)-torus.
This projection is a 2-cycle of odd degree. In the square cell structure of that torus,
the cycle condition forces the coefficients on adjacent faces to agree.
Thus every one of its \(aL_i\) faces has coefficient one, where \(L_3=c,L_4=d\).
Each needs a distinct preimage face of \(S\), so
\[
 |S|\ge A_i:=aL_i\ge a^2.
\]
It follows that \(\mathcal Z_m-\mathcal Z_{m+v}\) is divisible by \(\lambda^{A_i}\).
Both polynomials equal one at zero. Their logarithmic germs therefore obey
\[
 F_{m,v}(\lambda):=\log\mathcal Z_m(\lambda)-\log\mathcal Z_{m+v}(\lambda)
       =O(\lambda^{A_i}). \tag{M2}
\]
Contractible contributions cancel in this *difference*. A dense slice cycle does not invalidate (M2).

OPEN — **Crux lemma HA (relative homological analyticity).**
For \(I=[43/20,5/2]\), there are \(r>1\), \(B<\infty\), and \(a_0\ge3\), independent of
\(\beta\in I\), \(a\ge a_0\), \(c,d\in\{a,2a\}\), and every required pair \((m,v_{1i})\),
such that the germ \(F_{m,v}\) in (M2) extends holomorphically to \(|\lambda|<r\) and
\[
 |F_{m,v}(\lambda)|\le BN\qquad(|\lambda|<r). \tag{HA}
\]
An equivalent extension is meant if common zeros cancel in the quotient.
No separate nonvanishing of the two polynomials is required by HA.
This is a sufficient, stronger, off-real statement; it is not asserted equivalent to (P).

PROVED conditional implication — **HA supplies (P), with an area gain.**
Apply the maximum principle to \(F_{m,v}(\lambda)/\lambda^{A_i}\) on circles of radius
\(s<r\), and let \(s\uparrow r\). The inherited Schwarz step gives
\[
 |F_{m,v}(1)|\le BN r^{-A_i}.
\]
Along the real segment the factors in (M) are positive, so this branch at one is the
ordinary real \(\log(Z^m/Z^{m+v})\ge0\). Hence
\[
 q_{m,i}(a)=\frac{1-e^{-F_{m,v}(1)}}2
 \le\frac{BN}{2}r^{-A_i}\le12B a^4e^{-(\log r)a^2}. \tag{M3}
\]
Put \(g=-\tfrac12\log\eta_*>0\), \(s=\log r>0\).
The inequality \(-sa^2+ga\le g^2/(4s)\) makes (M3) at most
\(12B e^{g^2/(4s)}a^4\eta_*^{a/2}\).
Thus the consumer's rate is retained, not weakened. The finitely many sizes below \(a_0\)
can be covered by enlarging the constant, since \(q\le1/2\).

### Attempt to prove HA: where the estimates stop

PROVED sufficient input — Suppose, more strongly, every \(\mathcal Z_k\) in each required
pair has no zero on \(|\lambda|<R\), for one \(R>1\) uniform in the same data.
Then HA follows on any fixed \(1<r<R\).
Indeed \(|\mathcal Z_k(\lambda)|\le(1+R\tau)^N\) there.
For its logarithm \(g_k(0)=0\), put \(M=N\log(1+R\tau)\); then \(\Re g_k\le M\).
The function \(h=g_k/(2M-g_k)\) maps this disc to the closed unit disc and vanishes at zero:
\(|2M-g_k|^2-|g_k|^2=4M(M-\Re g_k)\ge0\).
Schwarz's lemma gives \(|h|\le r/R\), hence
\[
 |g_k|\le\frac{2Mr}{R-r},\qquad
 |F_{m,v}|\le\frac{4Mr}{R-r}\quad(|\lambda|\le r).
\]
This proves the stated implication only. The nonvanishing hypothesis is unproved.

**Attempt A: positivity and bounded plaquette factors.**
Each individual factor in (M) has no zero for \(|\lambda|<1/\tau>1\).
That property need not survive the correlated integral.
For the explicit auxiliary law \(t_1=\cdots=t_N=\tau\varepsilon\),
\(\Pr(\varepsilon=\pm1)=1/2\), the analogous polynomial is
\[
 \frac{(1+\tau\lambda)^N+(1-\tau\lambda)^N}{2}.
\]
It is positive on the physical real segment but has a zero at
\(\lambda=i\tan(\pi/(2N))/\tau\), approaching zero as \(N\to\infty\).
This is a counterexample to the proposed analytic inference, not to the Wilson model.
The direct estimate
\(|\mathcal Z_k-1|\le(1+|\lambda|\tau)^N-1\)
only supplies the shrinking disc \(|\lambda|<(2^{1/N}-1)/\tau\).
It does not approach the required radius.

**Attempt B: absolute values in (M1).**
The valid bound \(|A_{\rm ce}(S)|\le\tau^{|S|}\) gives
\[
 |\mathcal Z_m(1)-\mathcal Z_{m+v}(1)|
 \le2\sum_{n\ge A_i}\binom{N}{n}\tau^n,
 \qquad \mathcal Z_m(1)\ge(1-\tau)^N.
\]
The numerator still counts extensive collections of contractible surfaces.
These bounds retain a cost exponential in \(N=O(a^4)\), so the area-order onset does not help.
Taking a logarithm formally cancels vacuum components, but does not establish convergence or HA.
The bare absolute surface majorant already fails in `gap-expose-astra.md:555–573`;
its rederivation is not a new route. The required resummation must precede absolute values.

**Attempt C: condition on SO(3), then prove a uniform analytic bound.**
At the identity quotient environment, (M) becomes a Z2 gauge partition function
with high-temperature parameter \(\lambda\tanh\beta\).
The following hand calculation shows that a background-uniform version of HA is false
already at \(\beta=5/2\). Thus this route cannot be repaired by better constants in a
background supremum. An averaged, signed estimate is still required.

## Step 5. Hand checks against the binding models

### Z2: a uniform large-torus countertest at beta = 5/2

READ — `gap-es1-opus.md:129–152`, by Claude Opus 5.5, already gives the exact
low-temperature cocycle sum and the minimum size of a nontrivial cocycle.
Reuse those identities. The following component argument makes the large-volume comparison uniform.
It concerns *frustrated plaquettes of Z2*, not a Peierls count of the dense SU(2) half-integer cycle.

PROVED — Let \(u=e^{-2\beta}\). Up to a common factor independent of \(k\),
\[
 Z^k_{\mathbb Z_2}=\sum_{D\in k+B^2}u^{|D|}.
\]
Sum this positive measure over all \(64\) cohomology classes. On the dual lattice,
\(D\) is a closed mod-two plaquette surface. Decompose it into components connected
through shared dual edges. Every component is closed: all faces incident to a given edge
belong to the same component. If the total class is nonzero, some component has nonzero class.
The prior minimum-size lemma gives at least \(a^2\) plaquettes in that component on our shapes.

The graph of dual plaquettes joined through shared edges has degree at most \(20\):
four edges per plaquette, at most five other plaquettes at each edge.
For a specified root plaquette, the number of connected sets of size \(n\) is at most
\(80^{n-1}\). To see this, choose a canonical rooted spanning tree for each set.
There are at most \(4^{n-1}\) rooted plane trees, encoded by balanced walks of length \(2n-2\),
and at most \(20^{n-1}\) choices for their embedded edges.
The image of the embedded tree determines the set, so this overcounts every set.

For a particular closed component \(\gamma\), deletion gives an injection into all closed surfaces.
The weight changes by precisely \(u^{|\gamma|}\). Thus the probability that \(\gamma\)
is a component in the all-class ensemble is at most \(u^{|\gamma|}\).
Writing \(b=80u\), the probability of nonzero class is at most
\[
 \varepsilon_a:=N\sum_{n\ge a^2}80^{n-1}u^n
       =\frac{N}{80}\frac{b^{a^2}}{1-b},\qquad b<1. \tag{Z}
\]
No independence assertion is used. For any nonzero class \(v\),
\[
 \frac{Z^v_{\mathbb Z_2}}{Z^0_{\mathbb Z_2}}
 \le\frac{\varepsilon_a}{1-\varepsilon_a}
 \quad(\varepsilon_a<1).
\]
At \(\beta=5/2\), \(b<1\), by the displayed finite arithmetic
\[
 e^5>1+5+\frac{25}{2}+\frac{125}{6}+\frac{625}{24}+\frac{3125}{120}
      =\frac{1097}{12}>80.
\]
Since \(N\le24a^4\), \(\varepsilon_a\to0\). Consequently
\[
 q^{\mathbb Z_2}_{0,i}(a)=\frac{1-Z^{v_{1i}}_{\mathbb Z_2}/Z^0_{\mathbb Z_2}}2
       \longrightarrow\frac12. \tag{Z2-test}
\]
This is a written finite-counting proof, not a numerical phase assignment.

PROVED consequence — A conditional version of HA, uniformly over quotient environments,
would apply at \(q_e=1\) and imply \(q^{\mathbb Z_2}_{0,i}(a)\to0\) by (M3).
Equation (Z2-test) contradicts it. For any proposed fixed constants, strict violation at
a sufficiently large finite torus persists in a neighborhood of the identity environment.
Thus ignoring a single measure-zero flat configuration does not repair a uniform bound.
This does not refute the actual averaged HA for SU(2).

### Frozen 2T: an exact constant parity weight

READ — The flat-holonomy counting principle is already in `gap-kappa-order.md:114–120`;
the 2T centralizers are recorded in `gap-q8test-check-astra.md:171–180`.
No finite-coupling freezing threshold is taken as proved.

PROVED — At zero temperature on any fixed admissible torus, a finite gauge group with
Wilson weight maximized only at the identity has
\(Z^v/Z^0=N_v/N_0\), whenever the two classes have flat representatives.
Here \(N_k\) counts ordered holonomy quadruples satisfying
\([g_\mu,g_\nu]=(-1)^{k_{\mu\nu}}\).
This is the prior counting principle: choose a spanning tree gauge; all remaining flat links
are determined by the four holonomies, and the common number of tree gauges cancels.

For 2T, use the unit quaternions
\(\{\pm1,\pm i,\pm j,\pm k,(\pm1\pm i\pm j\pm k)/2\}\).
There are three cyclic order-four subgroups and four cyclic order-six subgroups.
Two distinct such subgroups meet only in \(\{\pm1\}\).
Every noncentral quaternion commutes only with quaternions on its own imaginary axis.
Thus every commuting quadruple containing a noncentral entry belongs to exactly one of those subgroups.
The untwisted count is
\[
 N_0=2^4+3(4^4-2^4)+4(6^4-2^4)=5856.
\]
For a single twist, say \(v_{13}\), \(g_1g_3=-g_3g_1\).
Conjugation preserves scalar parts, so both quaternions must be purely imaginary.
In 2T they are among \(\pm i,\pm j,\pm k\); anticommutation requires different axes.
There are \(6\cdot4=24\) ordered pairs.
An element commuting with both perpendicular axes must be central, so \(g_2,g_4\)
have two choices each. Hence
\[
 N_{v_{13}}=96,\qquad
 \frac{Z^{v_{13}}}{Z^0}\longrightarrow\frac1{61},\qquad
 q_{0,3}\longrightarrow\frac{30}{61}\quad(\beta\to\infty\text{ at fixed torus}). \tag{2T-test}
\]
These are exact arithmetic counts, with no enumeration run.
They do not interchange \(a\to\infty\) and \(\beta\to\infty\), and they do not establish
the GUIDE freezing claim near \(\beta=2.3\).
They show why fusion parity and anticommuting holonomies alone cannot force the target.
The same frozen counting for Z2 has \(N_v=0\), since all elements commute, and gives \(q=1/2\).

### U(1): the retained integer flux

PROVED comparison-model calculation — In compact free Maxwell theory on a spatial cubic torus
of side \(L\), let \(\theta=LA_i\) be a flat holonomy angle of period \(2\pi\).
The action \((2e^2)^{-1}\int |\dot A|^2\,d^3x\,dt\) restricted to this mode is
\(L(2e^2)^{-1}\int\dot\theta^2dt\).
Its Hamiltonian is \(e^2(-\partial_\theta^2)/(2L)\), with eigenvalues \(e^2n^2/(2L)\),
\(n\in\mathbb Z\). At time period \(L\), the centre flip \(\theta\mapsto\theta+\pi\)
therefore has odd weight
\[
 \frac{\sum_{n\ {\rm odd}}e^{-e^2n^2/2}}
      {\sum_{n\in\mathbb Z}e^{-e^2n^2/2}}>0, \tag{U-test}
\]
independent of \(L\). Neutral oscillator factors cancel from this ratio.
This is a free Maxwell computation, not a proof identifying compact Wilson U(1) with that model.
The U(1) Coulomb-phase obstruction in the brief remains a binding test;
its full finite-torus Wilson matching is not silently inferred from (U-test).

ARGUED — Closure of the mod-two surface, its area-order Taylor onset, and the analytic
implication (M3) all hold also for U(1). Integer charges modulo two play the role of \(2j\bmod2\).
Therefore these proved steps contain no SU(2) selection. Any successful proof of HA must
fail in a Coulomb regime with surviving integer electric flux. No such selective estimate
has been proved in this probe.

## Step 6. Continuity, integer flux, and the stopping point

PROVED — **What the absence of an integer fusion charge says.**
Suppose an abelian-group label \(q_j\) is assigned to each SU(2) irrep, with \(q_0=0\),
and every summand \(V_k\subset V_j\otimes V_l\) must have \(q_k=q_j+q_l\).
Put \(x=q_{1/2}\). Since \(V_{1/2}\otimes V_{1/2}=V_0\oplus V_1\),
\(2x=0\) and \(q_1=0\). Successive tensor products with \(V_{1/2}\) then give
\(q_j=(2j)x\). Thus this grading factors through parity; a grading valued in \(\mathbb Z\)
is trivial. By contrast, U(1) irreps obey \(V_n\otimes V_m=V_{n+m}\) and retain integer charge.
This proves a statement about additive representation labels, not the nonexistence of every
possible emergent or collective conserved observable.

ARGUED — Fusion explains why the natural *exact* class is mod two. It supplies no estimate
on the relative sector weights. Z2 already has that fusion parity; (Z2-test) defeats the inference.
Noncommutativity and anticommuting holonomies are also insufficient, by (2T-test).
Continuity permits the SO(3) environment to vary, but neither connectedness nor a finite-energy
density bound controls the signed average (S). U(1) has a continuous environment as well.
The required combination of continuity and non-Abelian dynamics must therefore enter a quantitative
averaged comparison. It is absent from the proved steps of the marked analytic route.

| Step/input | SU(2) conclusion here | U(1) test | Z2 / frozen 2T test |
|---|---|---|---|
| Positive slice trace and cycle parity | READ reduction, exact carrying observable | Odd integer flux gives the same mod-two observable | Same sector construction |
| Local reconnections / fusion | Preserve total class; no relative-weight estimate | Preserve the stronger integer class as well | Parity alone is shared |
| SO(3) split | READ identity; conditional deficit can have either sign | Quotient split exists, with integer-flux structure retained | Identity environment gives Z2; 2T shares the seam counterexample |
| Marked Taylor onset (M2) | PROVED, area order | Same onset | Same onset |
| HA implies (P) | PROVED implication; HA OPEN | Cannot assume HA in a phase with persistent electric flux | HA fails for Z2 at beta 5/2; a background-uniform SU(2) version fails |
| Full order-one estimate | OPEN | No Coulomb theorem is accidentally derived | Frozen count and finite-beta Z2 test remain incompatible with the target |

## Final checkpoint

The parity formulation is correct for (E17), but is a restatement of its missing charged-sector estimate.
It is not made smaller by (HS), by local fusion, or by the positive one-slice representation.
The real sufficient consumer remains (FQ); this file has not replaced it.

The best route attempted here is **relative homological analyticity (HA)** of the centre-odd marker.
The area-order zero and HA-to-(P) implication are proved above.
HA itself is open and stronger than (P); it could fail even when the real parity estimate holds.
It must not be recorded as an established or automatically easier supplier.

Failed approaches, with their exact limits:

1. Loop switching at fixed cycle: reconnection preserves the total class. Local cycle data also
   leave its weight free, as the density-1/3 construction proves. This does not rule out a new
   identity comparing different Wilson-weighted cycles.
2. Positive Z2 conditioning: the conditional deficit is signed. A bound uniform in its
   environment is false, by the explicit finite-beta Z2 test. An averaged inequality is not refuted.
3. Analytic continuation of the marked sum: real positivity supplies only a shrinking disc;
   absolute estimates retain the extensive vacuum cost. Neither proves HA beyond the physical marker.

Next mathematical decision: either prove the averaged relative bound in HA by summing contractible
decorations before taking absolute values, or find that this stronger complex statement fails and
retain a real normalized winding-sum estimate instead. A local typical-value bound alone is not
that statement. The neighboring row 867 retains ownership of its local separation question.
No additional lane, registry entry, audit verdict, status or claimed closure was created.

Source identity: checkout `d17e0d63fe6a748ae144149598592635cf2240a6`; main and PR source revisions
are recorded in Repo search. Outline SHA-256
`d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`;
CA-I SHA-256 `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.
CA-I 2490–2515 and 2698–2714 were also read; they exclude a claimed mass gap and supply no parity estimate.
There were no numerical runs, numerical certificates or machine enumerations.
No downloads beyond the two requested source files were made.
The written arguments are not independently checked. Work is local in the requested output file;
no commit, push, PR or outward post was made by this session.

RESULT: OPEN — (E17) is exactly the slice-homology parity problem; the marked area-order zero and HA-to-(E17) implication are proved, but the SU(2)-specific averaged estimate HA remains unproved. Local-cycle data and positive conditional-Z2 shortcuts do not supply it; the explicit Z2 and frozen-2T tests remain respected.
