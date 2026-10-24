# Taste-staircase arithmetic and the unresolved contraction bridge

**Type:** bounded_theorem
**Date:** 2026-05-10; source correction 2026-10-21.
**Status:** partial narrowing of the former four-obstruction no-go; independent audit owns effective status.
**Runner:** `scripts/frontier_hierarchy_bbs_staggered_taste_blocking_bridge_narrow.py`.
The original proof, proposed classification and execution counts remain recoverable at f24d17d97d372df977476e4a69674577f31af575. No claim ID or audit verdict is changed.

## 1. Corrected finite staircase arithmetic

Supply the model substitution n_k=16-k for k=0,...,16 in the SU(3) one-loop coefficient, with C_A=3 and T_F=1/2:

```text
b_k=(11 C_A-4 T_F n_k)/3=(1+2k)/3,
b_0=1/3 (16 supplied tastes), b_16=11 (zero supplied tastes),
sum_{k=0}^{15} b_k=256/3.
```

The old statement interchanged the endpoint indices; its proof and runner used the ordering above. The substitution of taste count for active flavors and sixteen RG steps is a supplied model premise, not proved by this arithmetic.

For supplied alpha=0.09067 and u0=0.87768138, define the truncated one-loop diagnostic

```text
u_k=u0 - |log(alpha)|/(8 pi²) sum_{j=0}^{k-1} b_j.
```

Its cumulative subtraction is about 2.594, exceeding u0. This shows breakdown of that perturbative inverse-coupling trajectory before completing sixteen steps. It is not a rigorous physical pole or a theorem excluding contraction of a nonperturbative coordinate. The former runner instead used 907/10000=0.0907; the repaired runner discloses and checks both close supplied values, without treating their difference as a new physical prediction.

## 2. Why the former four-obstruction proof is withdrawn

**Published hypotheses:** [Brydges–Slade's abstract](https://arxiv.org/abs/1403.7256) distinguishes perturbative coupling flow from an additional nonperturbative coordinate and gives conditions for contraction of the latter. It reports applications to the four-dimensional weakly self-avoiding walk and phi-four model. [The BBS introduction](https://arxiv.org/abs/1907.05474) describes the hierarchical phi-four analysis and Euclidean extension. These descriptions do not establish a universal theorem for the present gauge/fermion staircase, but neither do examples of applications prove an exhaustive domain exclusion. A concrete map, norms and verification of hypotheses are still required here. No computer test of stored citation strings establishes a literature theorem.

**Perturbative increments versus contraction:** increasing b_k or loss of perturbative control in u_k does not determine a Lipschitz/operator norm of an unspecified RG map. In particular, BBS's nonperturbative coordinate need not coincide with the running coupling. The old “equivalently” inference from one to the other was not justified.

**Numerical identification versus impossibility:** an operational coupling ratio and a norm bound have different roles, but equality is not categorically impossible. For any 0<alpha<1, the chosen map T_alpha(x)=alpha x on R has norm alpha. This toy construction supplies no physical RG map; it refutes only the claim that the roles by themselves forbid equality. Proving the desired physical identification remains separate.

**Finite-range summands versus total tail:** a covariance can have a long-range tail while decomposing into finite-range covariances. The former argument conflated these two properties. An elementary counterexample on Z is

```text
C_j(r)=4^(-j) max(1-|r|/2^j,0),  j=0,1,...,
C(r)=sum_j C_j(r).
```

Each C_j is a positive multiple of the autocorrelation of a normalized length-2^j box, hence positive definite and supported in |r|<2^j. The sum converges absolutely. At r=2^n for n>=0,

```text
C(2^n)=sum_{j=n+1}^infty 4^(-j)(1-2^(n-j))
      =4^(-n)(1/3-1/7)=(4/21) r^(-2).
```

Thus a power-law tail alone cannot obstruct finite-range covariance decomposition. This is a counterexample to the inference, not a decomposition of the actual gauge covariance or verification of all BBS hypotheses.

These corrections remove the claimed four independently sufficient obstructions. They do not establish the hierarchy formula or its contraction bridge.

## 3. Supplied source inputs and unresolved obligations

- [alpha definition context](ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md).
- [plaquette normalization context](PLAQUETTE_SELF_CONSISTENCY_NOTE.md).
- [proposed staircase context](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md).
- [one-loop staircase context](YT_P2_TASTE_STAIRCASE_BETA_FUNCTIONS_NOTE_2026-04-17.md).

These sources identify the model being tested; this note does not independently derive or promote their physical premises. To establish a contraction bridge one must specify the action space, norm, blocking map, covariance construction, applicable estimates and physical identification of any contraction factor with alpha. No independence or minimality of these obligations is claimed. Neither success nor impossibility is inferred from absence of a supplied construction.

## 4. Reproduction

Run `python3 scripts/frontier_hierarchy_bbs_staggered_taste_blocking_bridge_narrow.py`. Exact endpoint/sum tests and the specified one-loop diagnostic replace literal literature/domain/Boolean obstruction checks. Counterexamples exercise the missing logical steps. Finite positive-semidefinite Gram matrices support the covariance construction; the autocorrelation proof above gives its general positivity. A successful runner does not certify BBS applicability, an actual RG contraction or a physical hierarchy.

## No-Go Discipline Gate

This is partial narrowing, not a new no-go or packet PASS. N1: the two concrete counterexample mechanisms are scalar norm realization and long-range sums of finite-range covariances; five attempted route families are not claimed. N2: the old four independent walls are withdrawn. N3: supplied taste/flavor substitution, alpha, u0 and one-loop truncation are explicit. N4: scalar beta arithmetic does not certify a nonperturbative norm; a long-range total does not certify nonexistence of a decomposition. N5: finite rung arithmetic and finite covariance Gram matrices only, no physical site dynamics or lattice-limit RG proof. N6: specifying a different coordinate/norm or a proved covariance decomposition remains a possible route; no new axiom is declared necessary. N7: a genuine nonperturbative-coordinate contraction could coexist with a running coupling leaving perturbative control; the missing task is its actual map and estimates. N8: the cited staircase source concerns perturbative running, so its breakdown is not a previously closed nonperturbative no-go. No retained status or independent-wall count follows.
