## Repo search

Terms searched with `git grep -n -i -E` over `*.md` and `*.tex`:
`marginal triviality|marginal dimension|logarithmic gain|gain per scale|Aizenman.?Duminil`,
`random current|switching lemma|switching principle|current representation`, and
`marginal|logarithmic correction|logarithmic factor|four-dimensional Ising|four-dimensional phi.?4`.
Refs: `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141` in
`/Users/jonreilly/Projects/Physics`.

The targeted searches for the marginal method and the strict `random current|switching lemma|switching principle` query returned no lines on any of the five refs. The broad `current representation` search did return terminology-only false positives. For example, `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/ALIGN2_55.md:115` says “Put `j := P^TD^⊥g` (a plain-current representation of the functional `g`).” This is a finite-dimensional linear representation, not a probabilistic random-current expansion or switching lemma, so it is not close to the Ising argument. Other `docs/` hits concern Fourier/current variables in unrelated models. No file hit supplied an application of the 4D Ising marginal method to lattice gauge theory.

The prior repository search `library/prior/repo-search-2026-11-08.md` predates this target and concerns other hard-route objects; it does not record a search for the marginal method. The current scoped search is the relevant one.

# Marginal-dimension method and gauge-theory distance

Reading note for FINISH row 885. Research text only; it grants no status. No
proof step was attempted or computer-assisted. Existing lane literature
summaries are credited below and reused; this note reads the assigned primary
sources for the specific logarithmic-gain statement and source-checks related
gauge papers.

## Existing lane work (do not redo)

`library/prior/gap-lit.md` and `gap-crux-lit-cross.md` already report
Forsström–Viklund’s random-current/switching result at abstract level, including
the small/large-coupling correlation decay and small-coupling area law. The
cross note already reports Aizenman Part III’s 3D $\mathbb Z_2$ gauge
application at HTML-summary level. `gap-lit-assoc.md` already reports
Duncan–Schweinhart’s finite-coefficient plaquette random-cluster/FKG route.
Those are credited and only the assigned paper’s exact logarithmic theorem
and primary-source details are new here. The supplied `repo-search-2026-11-08.md`
is a prior search of different proof objects and has no marginal-method
coverage. `open-registry.md` has no owner row for this reading item or for an
Aizenman–Duminil-Copin gauge transfer; its substring hit `S8 — Own marginal
cancellation` is a different open response-cancellation statement.

## Assigned 2021 result: what the logarithm is

Michael Aizenman and Hugo Duminil-Copin, “Marginal triviality of the scaling
limits of critical 4D Ising and $\phi_4^4$ models,” *Annals of Mathematics*
194 (2021), 163–235 ([paper](https://annals.math.princeton.edu/2021/194-1/p03),
[arXiv:1912.07973](https://arxiv.org/abs/1912.07973)). The assigned paper’s
main field-theory conclusion is Theorem 1.2: in dimension four, any random
field reachable by the paper’s stated lattice-cutoff $\phi^4$ constructions
and satisfying its condition (1.10) is a generalized Gaussian process. For
the nearest-neighbor ferromagnetic Ising model on $\mathbb Z^4$, Theorem 1.3
gives the quantitative input. For $c,C>0$, every $\beta\le\beta_c$,
$L\le\xi(\beta)$, and pairwise $L$-separated $x,y,z,t$,

$$
|U_4^\beta(x,y,z,t)|\le {C\over B_L(\beta)^c}
\sum_{u\in\mathbb Z^4}\prod_{v\in\{x,y,z,t\}}
\langle\sigma_u\sigma_v\rangle_\beta,
\qquad B_L(\beta)=\sum_{x\in\Lambda_L}
\langle\sigma_0\sigma_x\rangle_\beta^2.
$$

This is the exact gain: a power of the truncated bubble diagram multiplies
the ordinary tree-diagram bound. It is not an unconditional statement that
the factor is $(\log L)^{-c}$. The authors explain that if the two-point
function is of order $L^{-2}$ in four dimensions, then $B_L$ is of order
$\log L$, yielding that logarithmic improvement. In their unconditional
argument the useful scale count is made in bubble coordinates: choose
$\ell_0=0$ and
$\ell_{k+1}=\inf\{\ell:B_\ell(\beta)\ge D B_{\ell_k}(\beta)\}$
for sufficiently large fixed $D$. Then $D^k\le B_{\ell_k}(\beta)\le
C D^k$. Proposition 5.1 says the probability of fewer than $\delta K$
intersection-clustering scales among these $K$ scales is at most
$2^{-\delta K}$, and the proof chooses $K\ge c\log B_L$ while
$2\ell_K\le L$. Thus a fixed positive fraction of bubble-doubling scales
produces geometric suppression; since the number of such scales is of order
$\log B_L$, the resulting gain is a power of $B_L^{-1}$. If
$B_L\asymp\log L$, that is a negative power of $\log L$.

The positive geometry is not a decorative interpretation. For a finite Ising
ferromagnet, a current is $n:E\to\mathbb Z_{\ge0}$ with source set
$\partial n=\{x:\sum_y n(x,y)\text{ is odd}\}$ and weight
$w(n)=\prod_{\{x,y\}}(\beta J_{xy})^{n(x,y)}/n(x,y)!$.
For $J_{xy}\ge0$ these are nonnegative weights and normalize to probability
laws when the source set is fixed. A two-current switching identity (paper
Lemma 2.3) changes source sets $A,B$ to $A\triangle B,\varnothing$ and
inserts the event that the sum current contains a subcurrent with source set
$B$. In particular it turns the four-point Ursell function into a negative
product of two two-point functions times a probability that two source
clusters intersect (paper (2.11)); comparison with independent currents and
multiscale intersection control then sharpen the tree bound. The proof’s
positive object is the ferromagnetic random-current law together with this
exact source-switching identity. The paper extends its Ising argument to
$\phi^4$ through the Griffiths–Simon class/decomposition into binary
variables; the Ising current formula is not asserted verbatim for an arbitrary
continuous-spin or gauge measure.

## Lattice-gauge uses found

Existing lane work is reused rather than repeated: `prior/gap-lit.md` had
already recorded the abstract of Forsström–Viklund; `prior/gap-crux-lit-cross.md`
recorded the Part III 3D $\mathbb Z_2$ application; and `prior/gap-lit-assoc.md`
recorded the Duncan–Schweinhart plaquette-random-cluster route. Their earlier
read levels and stated limits remain credited. The new primary-source checks
below sharpen exact scope, not the lane’s standing.

* **Malin P. Forsström and Fredrik Viklund (2025), “A current expansion for
  Ising lattice gauge theory,” arXiv:2502.19942** ([arXiv page](https://arxiv.org/abs/2502.19942)). Their Theorem 1.1 represents the finite-volume Wilson partition function with loop source $\gamma$ as a positive sum over plaquette currents $n$ with $\hat\partial n=\gamma$ and weights $w(n)=\prod_p(2\beta)^{n(p)}/n(p)!$; the support is a surface with boundary $\gamma$. Lemma 1.2 is the corresponding source-switching identity for two loop sources. For Ising ($\mathbb Z_2$) lattice gauge theory they derive Wilson-loop nonnegativity for all $\beta$, Griffiths’ second inequality and monotonicity in $\beta$, an area-law estimate at sufficiently small $\beta$, and exponential correlation decay at sufficiently small and sufficiently large $\beta$. They explicitly leave use near the critical value as an interesting question. **Closeness:** the closest hit structurally: it supplies positive surface currents and a switching lemma in a gauge model. Its gauge group is $\mathbb Z_2$; it does not prove a marginal-dimension intersection-clustering estimate, a logarithmic gain near criticality, or an SU(2) statement.

* **Michael Aizenman (2025), “Geometric Analysis of Ising Models, Part III,”
  arXiv:2509.02850** ([arXiv page](https://arxiv.org/abs/2509.02850)). Theorem 9.1 states for the pure $\mathbb Z_2$ lattice gauge model on $\mathbb Z^3$ an area-law upper bound on square Wilson loops for $0\le\beta<\beta_c$ and a perimeter-law lower bound for $\beta>\beta_c$, with the transition related by duality to the Ising critical point. The paper explains the perimeter lower bound using duality and an FK argument, and remarks that key steps can instead use the random-current representation (with a tighter squared two-point connection bound). Elsewhere it extends the Ising current representation to mixed-sign couplings by switching cancellations that recover positive sums on frustration-free configurations. **Closeness:** relevant geometric representation and an actual gauge-theory application, but the gauge result is 3D $\mathbb Z_2$ and is a duality/sharpness result, not the 4D logarithmic cumulant improvement. The frustration extension concerns Ising interactions, not an SU(2) gauge-link measure.

* **Paul Duncan and Benjamin Schweinhart (2025), “Topological Phases in the
  Plaquette Random-Cluster Model and Potts Lattice Gauge Theory,” CMP 406,
  145** ([publisher open article](https://doi.org/10.1007/s00220-025-05322-5),
  [arXiv:2207.08339](https://arxiv.org/abs/2207.08339)). For prime $q$ and
  coefficients in $\mathbb F_q$, they couple the $(i-1)$-dimensional
  $q$-state Potts lattice gauge model to an $i$-plaquette random-cluster model;
  an $(i-1)$-cycle is null-homologous exactly with probability equal to the
  corresponding generalized Wilson-loop expectation. They prove a sharp
  homological-percolation transition on the $2i$-dimensional torus at
  $p_{sd}=\sqrt q/(1+\sqrt q)$. **Closeness:** positive geometric gauge
  representation and sharpness, but it is plaquette random-cluster/FKG and
  homology, not random-current switching or the marginal logarithmic gain;
  it is not non-Abelian SU(2). This was already in the lane’s prior literature
  note.

* **Ulrik Thinggaard Hansen, Jianping Jiang and Frederik Ravn Klausen
  (2025 preprint), “A General Coupling for Ising Models and Beyond,”
  arXiv:2506.10765** ([arXiv page](https://arxiv.org/abs/2506.10765)). The
  abstract puts Ising, random-cluster, random-current and loop $O(1)$ graphical
  models in one coupling framework, and says the Loop-Cluster coupling is
  generalized to lattice gauge theories. **Closeness:** an adjacent graphical
  coupling result only; the abstract does not state a marginal theorem,
  logarithmic gain or an SU(2) current switching estimate.

The explicit gauge applications above are the finite-group cases
$\mathbb Z_2$ or finite $q$; the Hansen–Jiang–Klausen hit is only an
abstract-level graphical-coupling lead and is not an SU(2) result stated
there. The search did not find a source that transfers
Aizenman–Duminil-Copin’s 4D marginal improvement to continuous non-Abelian
Wilson theory. This is a bounded-search result, not a literature-absence
theorem.

## What a YM analogue would have to supply

For a specific gauge-invariant observable family, it would need all of the
following as proved identities/estimates, not as a diagrammatic analogy:

1. A normalized, nonnegative finite-volume geometric measure at the actual
   gauge coupling, with sources encoding the chosen observables (for Wilson
   loop observables, a plausible current would be a plaquette-valued surface
   current whose boundary records the loop insertions).
2. An exact switching identity for pairs of those currents that moves the
   source data and expresses the connected four-observable or Wick-defect
   term as a positive intersection/overlap event. Separate positivity of the
   partition-function character coefficients would not by itself establish
   this identity or the needed observable formula.
3. A multiscale intersection-clustering estimate uniform in volume, cutoff,
   source geometry and the tuned coupling, with a gauge-invariant analogue of
   $B_L$ and enough bubble-doubling scales to yield a gain such as
   $B_L^{-c}$ (and $ (\log L)^{-c}$ only when $B_L$ is proved comparable to
   $\log L$).
4. A justified passage from these finite-volume estimates to the intended
   continuum observable and OS/Wightman limits. One would also have to check
   the consequence for nontriviality: an Ising-style Wick-defect gain is a
   Gaussianity mechanism and cannot by itself be advertised as evidence of
   an interacting Yang–Mills limit.

The existing lane statement in row 878 that SU(2)’s signed surface expansion
lacks the needed positive geometric representation is a lane diagnosis, not a
theorem proved by the literature survey. Forsström–Viklund show the exact
switching/positive-surface template for $\mathbb Z_2$; neither their paper nor
Aizenman Part III supplies the analogous identity for SU(2). The outline’s
SA lines 11687–11715 call its own objects “current corrections” but identify
them as resolvent expansions cited to Balaban B85c, equations (3.130)–(3.138),
and leave actual-block matching open; this is a different use of “current,”
not a random-current construction. No claim about Balaban’s papers beyond
those outline quotations is needed here.

## Access record

The requested local download/read workflow was attempted in a new directory,
`/tmp/gap-lit-marginal-20261113`. `curl` could not resolve
`export.arxiv.org` (DNS/network failure), so the directory remains empty and
these papers were **not** read with Python `-I`. The computer-use browser
host was also unavailable. Instead, I read the open IHES PDF text for
Aizenman–Duminil-Copin and the arXiv HTML text for Part III and
Forsström–Viklund through the web reader, at the theorem and section locations
above. This substitutes primary-source text access, but does not satisfy the
requested Python-I/local-copy procedure.
The note is consequently a source-based reading, not an independent
re-derivation or check.
