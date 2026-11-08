# Full two-block response research check

Status: complete, including focused review of the final delta. Author research gate only, not a landing review or formal independent audit.

Reviewed candidate: `/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/SU2_TWO_BLOCK_BOUNDARY_RESPONSE.md`, all 523 lines, SHA256 `393e0ffb959be634b98847ff4f6610cf2ddd3aa6c3cbe5a27e84eb48fb737b32`. Worktree HEAD was `89faef229ff6e6bde42baad15ed8270c2f4087d8`; the candidate and its evidence directory were untracked. The source is frozen by bytes, not by that HEAD.

Final candidate after the separately checked delta: 548 lines, SHA256 `934b10582986d3d484e158af2913050d872788d1ee3171720abe3e37daa1073c`. The finding below applies to this final hash. Line references in the substantive proof sections refer to the initial hash; final-delta line references are explicitly marked. No numbered formula changed.

Scope: source normalizations, total cumulance through order four, adjacent shared-edge contraction and its response, posterior influence constants and support counts, and a separate derivation of the weighted coarse estimate. Supplied premises read: `MASS_GAP_CONSTRUCTION_ASTRA.md` lines 253–419 and `PROOF.md` lines 1976–2005 in the same directory. No claim is made about other source content or the continuum/weak-coupling bridge.

Finding: **no mathematical defect found in the stated finite-model identities or sufficient one-step contraction domain at the reviewed source hash.** This is a bounded research decision, with the coverage and limits below. It does not establish the physical-scale bridge, a mass gap, or retained status.

No repository, prompt, audit, commit, or PR changes are authorized or performed by this checker.

## Source receipt

| Source | Read scope | SHA256 |
|---|---|---|
| `SU2_TWO_BLOCK_BOUNDARY_RESPONSE.md`, initial | All 523 lines | `393e0ffb959be634b98847ff4f6610cf2ddd3aa6c3cbe5a27e84eb48fb737b32` |
| `SU2_TWO_BLOCK_BOUNDARY_RESPONSE.md`, final | Final source displayed completely; complete six-hunk delta checked against the initial source | `934b10582986d3d484e158af2913050d872788d1ee3171720abe3e37daa1073c` |
| `MASS_GAP_CONSTRUCTION_ASTRA.md` | Lines 253–419, section 2 | `a5d31da82721607e0ba04fef84675706bd3f2c568644224cce7dc86b0bb968e2` |
| `PROOF.md` | Lines 1976–2005, supplied paths and setting | `6ee69cd974567f9baf7a2fd40fc088391df6536357b869c875b84f5833d49f69` |
| `docs/ai_methodology/SCIENCE_WORKFLOW.md` | Complete workflow; governs scope only | `71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3` |

Applicable entry instructions were read. The discovery-loop skill was inspected for applicability; no discovery campaign, PR process, or audit workflow was invoked for this bounded check. The scientific derivations below do not import conclusions from the candidate's prior checker records or cited comparison paper, neither of which was needed or examined.

## Exact source and boundary calculus

**Lines 76–140: W, Q, and the global partition function remain distinct.** With the exterior fixed, the normalization of the interior coarse density is Q, not the full Wilson partition function. Integrating the interior kernels gives Q because every kernel, including its U-dependent denominator, has mass one. The identities obtained by twice differentiating log W and log Q therefore give the conditional and exterior-conditioned fine covariances separately. The mixed density derivative has both the product of scores and the difference of covariances. Averaging it to zero gives (8).

For completeness, differentiating E_p a first in s gives Cov_p(a,m_F). Differentiating that expression in t gives

    Cov_p(a,c_FG) + kappa_3,p(a,m_F,m_G),

because ∂_t m_F=c_FG and the p-score is m_G−M_G. This independently checks (9)'s otherwise easily omitted conditional-mean response. A second total-covariance decomposition over the exterior, whose density is Q_xi/Z_beta(s,t), gives (10). The final exterior covariance in (10) is required; a fixed xi does not yield the original Wilson covariance.

**Lines 144–202: finite changes and total cumulance.** The boundary kernel ratio is exp H_j pointwise in U; the radial normalizer cancels from that ratio but remains in both baseline measures. Bounded exponential tilting gives ∂_u cumulant_n=kappa_(n+1)(…,H_j). Applying the ordinary integral remainder to c_FG gives (13), including the repeated H_j. Applying the rectangle identity with two independently changed coordinates gives (14). The rho subtraction is needed for log p but not log W.

Direct differentiation of E_p c_FG produces E_p kappa_3,pi(F,G,H_j)+Cov_p(c_FG,h). Direct differentiation of Cov_p(m_F,m_G) produces the other three terms in (15). None is redundant when conditional means respond.

For (16), expanding conditional moments and then the cumulant's partition formula yields exactly the five partition types 4, 3+1, 2+2, 2+1+1, and 1+1+1+1, with multiplicities 1, 4, 3, 6, and 1. In particular, the 2+2 terms are covariances of conditional covariances, not products of their expectations. The 2+1+1 terms are third cumulants, not uncentered products. An exact rational finite-state disintegration check of all 5 third-order and 15 fourth-order partitions is recorded below; every partition-type group is nonzero in that example, and both reconstruction discrepancies are exactly zero.

## Independently checked shared-edge moment

**Lines 206–283.** Here is a scalar integration-by-parts route, distinct from both the displayed radial Hessian proof and its cited character/Fierz check. For r>0 write M=rW and V=WY. Under the tilt, x=Re Y has density proportional to e^(zx)(1−x²)^(1/2) on [−1,1], z=lambda r. Its mean is b(z). Integration of the derivative of e^(zx)(1−x²)^(3/2), whose boundary values vanish, gives

    z[1−E x²] = 3 E x,
    E x² = 1−3a(z),       E y_i y_j = a(z) delta_ij,
    a(z)=b(z)/z.

The remaining three coordinates have mean zero, and all mixed scalar/vector moments vanish. Thus the second moment has transverse eigenvalue a and longitudinal eigenvalue 1−3a, as in (20).

Cyclic trace gives w(VA)=w(YAW) and w(V^dagger B)=w(Y^dagger W^dagger B). The coefficient-vector scalar product is w(AW W^dagger B)=w(AB), while their scalar components are w(AW) and w(W^dagger B). Therefore

    E[w(VA)w(V^dagger B)]
      = a w(AB)+(1−4a)w(AW)w(W^dagger B).

Subtracting the product b² w(AW)w(W^dagger B) yields (18). The six other coarse links are distinct, so averaging their ordered products replaces A,B by Abar,Bbar. This uses their conditional independence given U, regardless of overlapping fine footprints. It does not commute matrices or replace an oriented nonunitary mean by its inverse.

The local expansion b=z/4−z³/96+O(z⁵) gives

    [1−4a−b²]/r² = −lambda²/48 + O(lambda⁴r²),

so h_lambda(0) and the lambda^6/4^7 coefficient in (21) are correct. At r=0, the shared link is Haar, the two conditional means vanish, and the surviving second moment is w(Abar Bbar)/4. At lambda=0, the other-link means also vanish, so this adjacent-plaquette conditional covariance is zero; the fixed one-link A=B=1 control is instead 1/4. These are different experiments, correctly distinguished in the note.

**Lines 287–317.** The law of total covariance gives Cov_p(W_P,W_Q)=Cov_rho(B_P,B_Q)+E_rho C_PQ. The three functions of U have no explicit exterior interpolation parameter. Differentiating once therefore gives the third cumulant of the two means plus Cov_rho(C_PQ,H_j). Differentiating twice gives the fourth cumulant of the means plus the third cumulant of C_PQ. Both (23) and (24) retain the conditional-covariance response; it would be incorrect to keep only the mean covariance.

## Independent semigroup derivation of the quantitative bound

This derives the load-bearing covariance estimate and boundary comparison by a different route from the note's maximal coupling and infinitesimal tilt. All functions below may be bounded measurable; oscillations use suprema over the explicitly defined everywhere-positive conditional densities.

**Posterior interactions and topology, lines 362–403.** For any subset of conditioned coarse links, including endpoint interpolations, the fine posterior contains precisely the kernel factors in (27). Unconditioned links integrate to one, removing their whole factor. For each conditioned factor, q_c is a convex combination of unit quaternion endpoints and has norm at most one; the radial denominator remains Z(lambda r_c), not a normalizer at an interpolated boundary norm.

A function in an interval of width R has mixed rectangle bounded by 2R. Consequently each Wilson plaquette contributes 4beta, each linear soft term 4lambda, and the radial term lambda²: the latter follows from 0≤log Z(lambda r)≤lambda²/2. The TV bound for a conditional likelihood ratio whose logarithm has oscillation D is tanh(D/4), hence at most D/4. These facts give exactly

    B_ef = beta n^p_ef + (lambda+lambda²/4)n^s_ef,    e≠f.

No differentiability or single occurrence of a fine link along a path is used in this range argument. Repeated fine edges therefore do not invalidate it.

Every S4-prime path lies within its two endpoint blocks except for the single crossing of their common face. Each endpoint block has 4(L−1)L³ internal edges, and the face has L³ crossing edges. Thus |S_c|≤(8L−7)L³=s_L. An internal edge can occur only in the eight incident coarse-link supports; a crossing edge only in the support for its own coarse face. Each fine edge belongs to six distinct plaquettes, each with three other edges. Summing B gives q=18beta+8(s_L−1)(lambda+lambda²/4). These are upper bounds even if algebraic cancellations make the true footprint smaller. The at-least-three-blocks torus hypothesis avoids periodic adjacency degeneracies. The separate explicit path enumeration below confirms these counts for L=3,5, without replacing the general geometric proof.

**Semigroup covariance estimate.** Let E_e be heat-bath conditional expectation at fine coordinate e under one of these posteriors pi, let N be the number of fine coordinates, and let

    P = N^(-1) sum_e E_e,
    L = sum_e(E_e−I),       P_t = exp(tL).

Write delta f for the column vector of single-coordinate oscillations. For j≠e, changing coordinate j in E_e f gives

    delta_j(E_e f) ≤ delta_j f + B_ej delta_e f,
    delta_e(E_e f)=0.

It follows by iteration and Poissonization that

    delta(P_t f) ≤ exp[t(B^T−I)] delta f.

Since the row sums of B are at most q<1, the right side tends to zero in l1 at rate at least 1−q. Invariance of pi then implies P_t f→E_pi f uniformly. Heat-bath conditional expectation is self-adjoint, and integrating the generator identity gives

    Cov_pi(f,g)
      = integral_0^infinity sum_e E_pi[Cov_e(P_t f,g)] dt.

The one-coordinate range covariance inequality bounds the integrand by (1/4) sum_e delta_e(P_t f)delta_e g. Hence

    |Cov_pi(f,g)|
      ≤ (1/4) delta g^T (I−B^T)^(-1) delta f
      = (1/4) delta f^T D delta g,       D=(I−B)^(-1).

This reproduces (30), including its factor 1/4, without using a tilted comparison measure. It applies uniformly to the posterior interpolations because the same B bounds all of them.

**Coarse influences.** Let R_ie=1_(e in S_i). The two endpoint insertions in (25) satisfy delta A_i≤4lambda R_i and delta H_j≤4lambda R_j. The rectangle integral therefore has absolute value at most 4lambda²(RDR^T)_ij. Normalizing the coarse one-site density subtracts a term independent of its own coordinate, so its boundary likelihood-ratio log oscillation has the same bound. The TV lemma gives

    C_ij ≤ tanh[lambda²(RDR^T)_ij] ≤ lambda²(RDR^T)_ij,    i≠j.

The identity term in D explicitly retains S_i∩S_j. It cannot be dropped when the two coarse edges have overlapping fine footprints.

**Weighted resolvent and coarse sum.** Put r=5L and use the stated periodic l1 midpoint distance. The two-block rectangle is contained in the radius-r ball about its coarse midpoint; each B-step connects fine edges at distance at most 2r. For q_alpha=e^(2r alpha)q<1, the path expansion for B^n and the triangle inequality give

    sup_e sum_f e^(alpha d(e,f))D_ef ≤ sum_(n≥0)q_alpha^n
                                             =1/(1−q_alpha).

For each e∈S_i and f∈S_j,

    d(i,j)≤r+d(e,f)+r.

Summing first over coarse j containing a fixed fine f incurs at most the incidence factor eight. Summing next over e∈S_i incurs at most s_L. Therefore

    sup_i sum_(j≠i)e^(alpha d(i,j))C_ij
       ≤ 8s_L lambda² e^(2r alpha)/(1−q_alpha) = Q_alpha.

Including the coarse diagonal during this upper bound is harmless. Solving Q_alpha<1 is exactly e^(2r alpha)[q+8s_L lambda²]<1, which yields (33) and the alpha interval in lines 464–465. There is no hidden additional factor of two or support-incidence factor.

**Many changed exterior links by a Poisson equation.** For two coarse laws mu,nu on J with different exteriors, use the mu heat-bath semigroup and define

    h = integral_0^infinity(P_t f−mu f)dt,
    L_mu h = mu f−f.

Since nu L_nu h=0,

    nu f−mu f = nu[(L_nu−L_mu)h].

At equal interior environments the one-site kernel difference is at most b_i≤sum_(j in H)C_ij, by telescoping the changed exterior coordinates. The same oscillation contraction as above gives delta h≤(I−C_JJ^T)^(-1)delta f, hence

    |nu f−mu f|≤delta f^T(I−C_JJ)^(-1)C_JH 1_H.

The weighted row norm is submultiplicative by the distance triangle inequality. Its geometric sum is Q_alpha/(1−Q_alpha), and every path ending in H has total length at least d(i,H). This proves both inequalities of (34) with the stated decay factor. This second derivation covers the actual two-region boundary conditional, not merely a formal covariance matrix.

## Limits, attempted counterexamples, and quantifier checks

| Case challenged | Outcome at the reviewed lines |
|---|---|
| lambda=0 with arbitrary finite beta | Lines 137–140 and 465–467 are correct: coarse density is product Haar and all coarse responses vanish, while W=Q=Z retains the full source covariance. Fine Dobrushin contraction is unnecessary for this exact endpoint. |
| beta=lambda=0 | B=0, D=I, C=0. The logarithmic formula choosing alpha must be read separately from its undefined zero denominator; the note explicitly treats this endpoint. |
| M=0 with lambda>0 | Lines 221–239 have the correct continuous limits. A shared Haar link can transmit the singlet second moment when the other six conditional means are nonzero. |
| Overlapping S_i,S_j | Lines 432–439 correctly include the identity part of D and do not infer independence from disjoint coarse labels. |
| Repeated fine edges in an S4-prime path | The path average may repeat a fine edge, but its value remains a unit quaternion before averaging and the mixed-rectangle bound is a range bound. Support counts count distinct edges, which is sufficient. Explicit repetitions occur in the enumeration below. |
| Repeated coarse edges | The shared edge in the adjacent pair is integrated by its second moment. The other six are explicitly required distinct at lines 206–210. The note does not justify replacing arbitrary further repeated coarse edges by first moments, and its worked formula does not claim that scope. |
| Discrete boundary endpoints | Lines 156–158 interpolate positive weights, not group elements. Intermediate q_c lies in the unit ball and preserves all quantitative bounds. No differentiable group-coordinate chart is assumed. |
| Conditioning versus the original Wilson law | Equations (8), (10), and (22) keep rho distinct from mu_beta. Restoring the original fine covariance requires averaging the exterior and its additional covariance term. |
| Nonzero source strengths | Lines 357–360 correctly limit (28)–(34) to zero fine sources. The exact identities hold at arbitrary bounded real source strengths, but B would require additional interactions for a quantitative source-tilted estimate. |
| Fixed-volume versus uniform estimates | Compactness justifies the finite-source identities; their general Taylor-remainder statement is explicitly not cutoff-uniform. The constants in (29)–(34) are volume-independent only for fixed L,beta,lambda satisfying (33). |
| One blocking step versus a physical multistep construction | Lines 485–505 correctly leave the weak-coupling trajectory, cutoff-uniform decay, and source/continuum bridge open. The posterior of a final-layer boundary is the entire hidden chain; earlier kernel normalizers remain. No identification of blocked marginals with a Wilson action is made. |

The shared-edge identities can also be stated at the last layer conditional on the entire finite hidden chain: conditional independence is then only for the last-layer links, the functions B_P,B_Q,C_PQ depend on the last hidden layer, and every averaging rho is the full hidden posterior. This observation extends the exact identities, not the one-step bounds (28)–(34).

## Actual deterministic checks

The checker executed two self-contained Python calculations with no repository dependencies. The first used exact rational arithmetic on six hidden states and three coarse states, with positive joint weights

    w(x,u)=(u+1)(x+2)+(u²+3x mod 7)+1,

and fine observables u−2, (u² mod 7)−3, (−1)^u(u+1), and (3u mod 5)−2. The ordinary cumulant was evaluated from its moment/partition formula; the conditional reconstruction independently grouped every partition of the labelled argument set. The second explicitly generated all 24 coordinate orders and all L^4 starting sites for each of four coarse directions, collected raw fine-edge supports, and translated them over a three-blocks-per-direction periodic torus. Undirected fine-edge multiplicity was counted before cancellations, which is the conservative support relevant to the bound.

Complete result log:

```text
TOTAL_CUMULANCE 3 PARTITIONS 5 EXACT_DIFFERENCE 0 GROUPS_NONZERO True GROUP_TYPES [(1, 1, 1), (2, 1), (3,)]
TOTAL_CUMULANCE 4 PARTITIONS 15 EXACT_DIFFERENCE 0 GROUPS_NONZERO True GROUP_TYPES [(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]
TOPOLOGY L 3 SUPPORT_SIZES [459, 459, 459, 459] S_BOUND 459 MAX_INCIDENCE 8 MAX_RADIUS 5 R_BOUND 15 PATHS_WITH_REPEATED_FINE_EDGE 1920 MAX_MULTIPLICITY 2
TOPOLOGY L 5 SUPPORT_SIZES [4125, 4125, 4125, 4125] S_BOUND 4125 MAX_INCIDENCE 8 MAX_RADIUS 10 R_BOUND 25 PATHS_WITH_REPEATED_FINE_EDGE 14976 MAX_MULTIPLICITY 2
```

These calculations are limited finite checks, not a proof of all parameters. The general proofs are the conditional cumulant expansion, geometric support argument, and semigroup derivation above. No numerical integration, fitted constants, stochastic sampling, or formal proof assistant was used.

Exact supplemental command executed, with stdout preserved immediately above in this report:

```sh
python3 - <<'PY'
from itertools import product, permutations
from collections import Counter
from fractions import Fraction as Q
from math import factorial

# Exact independent finite-state check of conditional cumulant reconstruction.
def partitions(xs):
    if not xs:
        yield []
        return
    a,*tail=xs
    for p in partitions(tail):
        yield [(a,)]+p
        for i in range(len(p)):
            yield p[:i]+[(a,)+p[i]]+p[i+1:]
def mean(vals, probs):
    return sum(v*p for v,p in zip(vals,probs))
def cumulant(vectors, probs):
    ans=Q(0)
    for p in partitions(list(range(len(vectors)))):
        term=Q((-1)**(len(p)-1)*factorial(len(p)-1))
        for block in p:
            vals=[Q(1) for _ in probs]
            for i in block:
                vals=[a*b for a,b in zip(vals,vectors[i])]
            term*=mean(vals,probs)
        ans+=term
    return ans
weights=[[Q((u+1)*(x+2)+(u*u+3*x)%7+1) for u in range(6)] for x in range(3)]
total=sum(map(sum,weights))
p=[sum(row)/total for row in weights]
pi=[[w/sum(row) for w in row] for row in weights]
mu=[sum(weights[x][u] for x in range(3))/total for u in range(6)]
ys=[[Q(u-2) for u in range(6)],[Q(u*u%7-3) for u in range(6)],[Q((-1)**u*(u+1)) for u in range(6)],[Q(3*u%5-2) for u in range(6)]]
for n in (3,4):
    groups={}
    for part in partitions(list(range(n))):
        vectors=[[cumulant([ys[i] for i in b], pp) for pp in pi] for b in part]
        key=tuple(sorted(map(len,part),reverse=True))
        groups[key]=groups.get(key,Q(0))+cumulant(vectors,p)
    lhs=cumulant(ys[:n],mu)
    rhs=sum(groups.values())
    print('TOTAL_CUMULANCE',n,'PARTITIONS',sum(1 for _ in partitions(list(range(n)))),'EXACT_DIFFERENCE',lhs-rhs,'GROUPS_NONZERO',all(v!=0 for v in groups.values()),'GROUP_TYPES',sorted(groups))

# Explicit S4-prime raw path support, including repeated fine edges.
orders=list(permutations(range(4)))
def axial(root, dest, order):
    cur=list(root); out=[]
    for d in order:
        while cur[d]!=dest[d]:
            sign=1 if dest[d]>cur[d] else -1
            base=cur.copy()
            if sign<0: base[d]-=1
            out.append((tuple(base),d))
            cur[d]+=sign
    return out
for L in (3,5):
    h=(L-1)//2; N=3*L; supports=[]; repeated=0; maxmulti=0; maxradius=0
    for d in range(4):
        root=(0,0,0,0); target=tuple(L if k==d else 0 for k in range(4)); support=set()
        for y in product(range(-h,h+1),repeat=4):
            yy=tuple(y[k]+(L if k==d else 0) for k in range(4))
            for order in orders:
                seq=axial(root,y,order)+axial(y,yy,(d,))+list(reversed(axial(target,yy,order)))
                ctr=Counter(seq); repeated+=any(v>1 for v in ctr.values()); maxmulti=max(maxmulti,max(ctr.values()))
                support.update(seq)
        supports.append(support)
        for pos,ed in support:
            mid=[pos[k]+(Q(1,2) if k==ed else 0) for k in range(4)]
            dist=sum(min(abs(mid[k]-(Q(L,2) if k==d else 0))%N,N-(abs(mid[k]-(Q(L,2) if k==d else 0))%N)) for k in range(4))
            maxradius=max(maxradius,dist)
    incidence=Counter()
    for block in product(range(3),repeat=4):
        offset=tuple(L*b for b in block)
        for support in supports:
            for pos,ed in support:
                incidence[(tuple((pos[k]+offset[k])%N for k in range(4)),ed)]+=1
    sL=(8*L-7)*L**3
    print('TOPOLOGY','L',L,'SUPPORT_SIZES',[len(s) for s in supports],'S_BOUND',sL,'MAX_INCIDENCE',max(incidence.values()),'MAX_RADIUS',str(maxradius),'R_BOUND',5*L,'PATHS_WITH_REPEATED_FINE_EDGE',repeated,'MAX_MULTIPLICITY',maxmulti)
PY
```

## Final delta check and binding

The author supplied `/Users/jonreilly/Documents/Codex/sussman-alpoge-process-review-20261108/ym-mass-gap-bridge/source-note-initial.md` and `source-note-final.delta` in that directory. The preserved initial file hashes to the exact initially reviewed value. Independently, reversing the six stated changes in the final in-memory text reproduced that same SHA256; an approximate reconstruction would not suffice. The complete supplied delta was then read, and the final source was rehashed.

```text
EXACT_ORIGINAL_RECONSTRUCTION 393e0ffb959be634b98847ff4f6610cf2ddd3aa6c3cbe5a27e84eb48fb737b32 LINES 523
PRESERVED_ORIGINAL 393e0ffb959be634b98847ff4f6610cf2ddd3aa6c3cbe5a27e84eb48fb737b32
CURRENT_FINAL 934b10582986d3d484e158af2913050d872788d1ee3171720abe3e37daa1073c
```

Focused dispositions, using final line numbers:

- Lines 15–22: added status/trace metadata preserves the finite-model scope and names the physical-scale task as future work. This check does not run a metadata validator or confer audit status.
- Line 32: changing the prior-art link to a code-formatted filename makes no mathematical change. The referenced slab note was not used as a proof premise here.
- Lines 71–74: the S³ coordinate density is normalized since (2/pi)B(1/2,3/2)=1. Its even moment is (2/pi)B(n+1/2,3/2)=(2n)!/[4^n n!(n+1)!]. Uniform convergence of the exponential on [−1,1] yields the displayed Z series. The addition is correct.
- Lines 355–358: gamma_i is exactly the full coarse single-site conditional whose likelihood-ratio oscillation was bounded by (25). The supremum definition of C_ij matches the semigroup and comparison uses; no block marginal is substituted.
- Lines 522–527: the last-layer shared-edge extension is correct under the whole hidden posterior, as derived above. It does not extend the quantitative one-step estimates or identify intermediate laws as Wilson measures.
- Lines 539–543: the newly described semigroup/Poisson check and finite enumeration correspond to work actually done in this report. Supplemental symbolic checks by others were not independently inspected here. The text correctly denies treating such checks as a general proof premise.

No new defect or additional open finite-model obligation was introduced by this delta. The mathematical disposition is bound to final SHA256 `934b10582986d3d484e158af2913050d872788d1ee3171720abe3e37daa1073c`.

## Disposition and remaining uncertainty

No defect requiring a mathematical source correction was found. The source can support the bounded research decision stated in its opening, conditional on the supplied Wilson action and normalized soft kernel. It does not supply the ontology-to-action map or the physical weak-coupling estimates.

This was one fresh-context derivation in the same provider, with the supervising model and reasoning effort inherited. It gives a different mathematical route for the load-bearing estimate, not formal audit independence. The original historical provenance claims at initial lines 509–519 and the contents of their referenced prior check records were not verified; the final delta's new description of this check was verified as stated above. No claim is made about unexamined sections of the premise documents. Any later mathematical edit or change to the kernel/path premises reopens the affected part of this check; metadata-only edits require an explicit diff receipt connecting their final bytes to this frozen source.
