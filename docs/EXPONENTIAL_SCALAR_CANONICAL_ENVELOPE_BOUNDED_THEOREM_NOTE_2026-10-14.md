# A tighter canonical scalar envelope from the field excursion

Status: conditional support.
Claim type: bounded_theorem.
Scientific author: /root.
Primary runner: `scripts/exponential_scalar_canonical_envelope_check.py`.

The finite-body bridge needs a controlled field interval and canonical Hessian,
not an assigned interior equilibrium. Re-expressing the supplied potential in
the conformal factor gives a sharper computable upper envelope and an improved
sufficient convexity criterion. These extend some checked parameter cases where
the earlier sufficient criterion was inconclusive; a failed sufficient test is
not an instability or multiplicity result.

The [supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[local normalization](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md)
and [finite-body theorem](EXPONENTIAL_SCALAR_FINITE_BODY_BOUNDED_THEOREM_NOTE_2026-10-14.md)
are the complete canonical dependencies. Their fixed flat metric, held particle
source, zero infinity boundary and negative-branch restrictions persist. The
canonical scalar here is dchi=sqrt(K_uu)du along x=y=0. The action, scale,
material and realized environment are not derived by this refinement.

The complete personal derivation follows, with original filenames identifying
source history in the recovery archive.

## A canonical potential envelope from the conformal excursion

Personally derived by /root. Conditional support under the same flat held-source,
negative-branch and vacuum-boundary premises as the finite-body result. This
refines an overly loose coordinate bound; it does not select the supplied action,
nu, k, scale or physical environment.

Use c=rhoStar/(2Q), -Delta V=c, P=||V||infinity, L=1+k and LP<1. The prior
elliptic comparison gives

 B=kP(1-LP/2)/(1-LP)^2,  exp(-B)<=A<=1,
 q=beta^2<=qMax=min[a,k/(1-LP)^2], 0<=d=-beta_chi<=L.

Define z=A, r=s/(1+s), zMin2=exp(-2B), Delta=1-zMin2,

 EMin=zMin2/[1+s(1-zMin2)], ellMax=-ln EMin,
 hMax=1-r zMin2.

The exact relation E=z^2/[1+s(1-z^2)] is monotone in z. Thus on the whole
reachable field interval E>=EMin and 0<=ell=-ln E<=ellMax. Writing
t=sE/(1+sE)=r z^2, one has 0<t<1 and 1-t<=hMax.
This uses the directly bounded conformal factor, avoiding division by a small
vacuum coordinate metric. EMin may be much below1/2 without invalidating it.

### 1. Exact canonical Hessian formulas

The base potential can be written without u as

 Ubase=3/2+(3/2)s(1-z^2)^2,
 Ubase_chichi=6s z^2[d(1-z^2)+2q(2z^2-1)].             (1)

For the regulator let g=u/(1+sE), so Ureg=nu(1+s)g^2/2.
Direct canonical differentiation gives

 Ureg_chichi = nu(1+s)/a * {
   q[1+3t ell+(2t^2-t)ell^2]
   +(d/2)(1-t)ell(1+t ell) }.                         (2)

Both are exact, with the original kinetic coefficient and variable coupling.
They include the canonical connection term. Neither formula assumes a positive
total Hessian. Equation(2) is checked independently by differentiating u/F with
d/dchi=(1/sqrt(K))d/du.

Dropping only negative terms and using the bounded positive factors gives

 Mc^2 = Hv^2 * {6s[L Delta+2qMax]
   +nu(1+s)/a * [qMax(1+3ellMax+2ellMax^2)
          +(L/2)hMax ellMax(1+ellMax)]},              (3)

such that Y_chichi<=Mc^2 on every reachable negative field value. For example,
the possibly negative factor 2z^2-1 in(1) is bounded above by1; the negative
-t ell^2 in(2) is dropped before multiplying by qMax. No sign reversal is hidden.
At fixed parameters P->0, (3) tends to the exact vacuum mass
Hv^2*4(3+3k+nu)/(1-3k).

Consequently the prior integrated surface-force theorem remains valid with
Mbar^2 replaced by Mc^2, or by the smaller of the two independently valid
envelopes. A smaller envelope is a tighter necessary bound, not a better fit.
The existing18 numerical profiles are already exposed development cases.

### 2. An improved sufficient convexity domain

Equation(1) is strictly positive if zMin2>=1/2. For the regulator, the exact
g_chichi expression in the earlier uniqueness note is nonpositive whenever
1+(ln E)/F=1-(1-t)ell>=0. Therefore the sufficient criteria

    B<=ln(2)/2,  hMax ellMax<=1                       (4)

give a strictly positive total canonical Hessian throughout the reachable
interval. Under LP<1, the earlier Kato contraction and ground-state form
argument then derive uniqueness, radial symmetry for a spherical source and
linear scalar stability with the source fixed. No new proof of existence is
needed: the earlier negative-cone existence result uses the original nu>0
premise. Failure of either criterion is uninformative, not an instability.

These conditions can succeed where the older sufficient bound
2sqrt(a)Wb/sqrt(K0)<=ln2 fails. They do not establish uniform validity at the
excluded parameter endpoints. In particular ellMax can diverge as k approaches
1/3, and the regulator and its condition retain that dependence. No endpoint is
silently admitted, and no observed k value is supplied.

### 3. Observation-facing scope and prospective challenge

The force normalization is still held particle mass and Gvac; surrounding matter,
support stresses, a calibrated source mass, finite measurement radius and metric
response remain open. This improvement removes a coordinate-conditioning artifact
from a sufficient local theorem. It supplies no Solar-System or laboratory fit.

Before executing: verify both canonical identities against the original u action,
the exact vacuum limit, conformal inversion and all inequality directions. Compare
old/new envelopes only on the exposed18 source cases, and record when neither
lower bracket is informative. Freeze additional near-endpoint rational k cases
before evaluating either criterion; use high precision to resolve cancellation.
Those cases are synthetic prediction controls, not independent observations.
Actually altered connection/regulator coefficients, conformal inversion and
inequality signs must fail mathematical witnesses. Preserve all failures.

## Evidence and limits

The original refinement has96/0 controls:18 already exposed body comparisons
and6 prospectively specified mathematical endpoint cases. Four of those six
pass the new criterion while failing the old sufficient criterion. No new BVP
solutions at those six points and no measured physics test are claimed. The
force bound is a radial surface bound, not a lower bound at arbitrary distance.

The canonical runner recomputes the original excursion and surface controls
before supplying their fresh full outputs to the exact refinement body. Its
488 controls are220+172+96; repeated cases are not additional independent
evidence. Full profiles and exact input hashes are recoverable. Default temporary
paths are deleted after execution; recovery is by preserved bytes and hashes.

Independent direct-action checks give2075/0 with distinct parameter fixtures,
216 field points, endpoint sequences and six actual damaged programs. The
reviewer's initial tolerance-parser failure and parser-only correction are
preserved. No tolerance or physics fixture was relaxed. Four sampled cases
that fail a sufficient criterion still have positive sampled Hessians; this
does not imply convexity everywhere or stability outside the theorem's domain.

The original finite-body serialization, flux-resolution, mesh-budget, proof
decay and radial-scope repairs remain in the parent theorem's recovery archive.
The prior uniqueness review's aggregate-output exposure remains disclosed;
the new envelope mathematical check read no producer implementation or outputs.
Canonical correspondence is openly a source comparison, not a blind experiment.

The exact formulas remain conditional on0<k<1/3, nu>0 and LP<1. Fixed-k P->0
recovers the vacuum mass. The limit k->1/3 at fixed nonzero P is nonuniform:
the regulator convexity condition eventually fails. No uniform endpoint,
action selector, empirical confidence level, state or absolute scale follows.
The scalar form bound keeps source and metric fixed. Moving matter, full gravity,
nonlinear settling, actual body composition and observation likelihood remain open.

Recovery source: `docs/work_history/physics/revised-scalar-canonical-envelope-20261014/README.txt`.
