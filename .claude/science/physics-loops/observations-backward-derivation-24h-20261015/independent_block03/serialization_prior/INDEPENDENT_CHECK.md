# Focused independent material and boundary check

This is a source-bound mathematical check for the campaign author. It is not a
formal audit, retained-grade verdict, empirical test, or approval to land work.
Authorship remains with root. Only this `independent_block03/` directory was
written; the author's runners were neither read nor executed.

## Source identity and scope

| Source in the parent pack | SHA256 |
| --- | --- |
| `BLOCK03_MATERIAL_CANDIDATE_v1.md` | `52b32068d094aea7c13d60ede00423bafcd384ac1c4107908ad3d51a842340b7` |
| `BLOCK03_BOUNDARY_PROBE_v1.md` | `0689282625c3663026b29b8fe71f05de13f5cba1f774a6c423d6f8391bef99bc` |

The material inverse and its static dust family are checked below. The boundary
probe is a separate conditional statement about a larger stipulated geometric
domain. No raw observations or external references were used. Git state was not
queried or changed during this block; these are file-content identities, not a
claim about a branch tip.

No material algebraic error or excess physical inference was found within the
two sources' stated hypotheses. The requested mathematical checks are complete:
35 core checks, 13 boundary checks, and 3 conservation/dimension/provenance
checks, all successful. These counts include grouped component identities,
defect expressions, and source-identity checks; they are not empirical tests.

## Independent sourced derivation

I varied the reduced gravitational action while keeping the sphere radius
`a(r)` independent of the radial coordinate. With `f=F`, its Lagrangian, after
discarding a total derivative, is

    Lg = sqrt(B)[(a^2 f' + 2af a')N' + Nf(a')^2 + 2Na f'a']
         + Nf/sqrt(B) - Na^2 sqrt(B) Z(f)(f')^2/2
         - Na^2 V(f)/sqrt(B).

The curvature integration by parts for this form was independently checked in
block 01; this runner imports no earlier code. Varying `N,B,a` before setting
`a=r` retains the angular equation. If `E_t,E_r,E_a` denote mixed gravitational
residuals including the scalar terms, the sourced equations are
`E_t=-rho`, `E_r=p_r`, `E_a=p_t`. The combinations give

    (Ga-Gt)F - B(1/r-N'/N)F' = rho+p_t,
    ZB(F')^2 = F(Gr-Gt) - rho-p_r - BF''
               - (B'/2-BN'/N)F',
    V = -FGt-rho-ZB(F')^2/2-BF''-(B'/2+2B/r)F'.

Thus the source terms and signs in equations (1)-(2) are correct. For
`d=B(1/r-N'/N) != 0`, the first equation is `F'-uF=-s`, so
`(F/M)'=-s/M`. The displayed affine transport follows with `M(r0)=1`.
It propagates one initial scalar value along one connected chart; it does not
fix that value. Conservation is an additional consistency condition, not an
extra free normalization datum. Direct mixed-stress divergence independently
gives `p_r'+(rho+p_r)N'/N+2(p_r-p_t)/r=0`, as stated in the source.

## Dust variation and regular-center field equations

Writing `X=g^{mu nu} T_,mu T_,nu`, variation of the declared matter action before
imposing any constraint yields

    X+1=0,
    div(lambda grad T)=0,
    T_mu nu = lambda T_,mu T_,nu - lambda(X+1)g_mu nu/2.

The last term vanishes on shell. `T=t`, `lambda=rho0`, `N=1` gives the stated
stress and solves both dust equations. The future velocity can be taken as
`u^mu=-grad^mu T`; the sign does not change its stress. Substituting `X+1=0`
in the action before metric variation would incorrectly erase this nonzero
stress; the runner includes that defect control.

For the center check I used spatial Cartesian coordinates `x_i`, not the
singular spherical coordinate basis. Put `s=sum_i x_i^2`, `B=1-ks`,
`A=2kC-rho0`. The geometry is

    g_ij = delta_ij + k x_i x_j/B,
    g^ij = delta^ij - k x_i x_j,
    Gamma^a_ij = k x_a g_ij,
    Ricci_ij = 2k g_ij,  R4=6k.

For `F=(C-rho0 s/2)/B`, direct differentiation gives

    partial_i F = A x_i/B^2,
    Hess_ij F = (A/B)g_ij + 3kA x_i x_j/B^3,
    |grad F|^2 = A^2 s/B^3,
    box F = 3A/B^2.

On this profile, `Z=-3kB/A`, `Z_F=6k^2 B^2/A^2`, `V_F=-6k/B`.
In the spatial metric equation the anisotropic scalar kinetic and Hessian
terms cancel. The temporal and isotropic spatial equations reduce to zero.
The scalar equation reduces independently to

    3k - 9k/B + 3k^2 s/B + 6k/B = 0.

At the center the metric is Euclidean, its connection vanishes,
`F=C`, `grad F=0`, `Hess F=A delta`, and `box F=3A`. The values
`Z(C)=3k/(rho0-2kC)` and `V_C(C)=2rho0-3kC` are finite for every allowed `C`.
These are direct regular-coordinate statements; no division by `F'(0)` occurs.

## Domain, dimensions, and what varies

The interval `rho0 R^2/2 < C < rho0/(2k)` is nonempty because `kR^2<1`.
Let `delta=rho0-2kC>0`. Throughout the ball, `B>0`,
`C-rho0 r^2/2>0`, and

    rho0-2kF = delta/B > 0.

Consequently `F>0`, `F<rho0/(2k)`, `Z=3kB/delta>0`, and
`2FZ+3=3rho0/(rho0-2kF)>0`. Also `F'=-delta r/B^2<0` for `r>0`.
The center-based affine solution uses `u=2kr/B`, `s=rho0 r/B`; both
extend smoothly to zero. With `M=1/B`, the particular integral is
`integral_0^r rho0 t dt=rho0 r^2/2`. Regularity imposes no extra condition on
`C`. Finiteness here is for each fixed member, not a uniform bound as
`C` approaches the excluded upper endpoint.

In natural units with mass dimension denoted by brackets:

| Quantity | Mass dimension |
| --- | --- |
| `r,T` (and boundary `chi`) | `-1` |
| `k,F,C` | `2` |
| `rho0,lambda,V` | `4` |
| `Z` | `-2` |
| `omega=FZ,N,B` | `0` |

The action density, all sourced metric terms, and the inequalities are
dimensionally consistent. The supplied dimensional `rho0,k` are inputs;
this construction does not derive an absolute calibration.

The author's distinction between different candidate potentials and solutions
of one fixed action is necessary and correct. For a second profile labeled
`C2`, using the potential labeled `C` gives mixed temporal and scalar residuals

    E^t_t - T^t_t
      = 3k(C-C2)(rho0-2kC2)/[(rho0-2kC) B^2],
    E_F
      = 12k^2(C-C2)/[(rho0-2kC) B].

They are nonzero for distinct allowed `C,C2`. Changing the dust density while
holding metric, scalar profile, and action fixed also violates the temporal
equation. These controls establish a reconstruction family of different
actions; they do not establish observational discrimination.

In any future perturbation calculation, `rho0` and `k` appearing in the action's
functions are fixed parameters of each reconstructed action, even though the
construction expresses them using background data. Replacing them by a changed
source density during a disturbance would retune the action. Further,

    V_C'(C)=-6k,
    V_C''(C)/Z(C)=4k

are independent of `C`. Neither ratio alone is the physical mass of the coupled
metric-scalar-dust system. A varying coefficient in `V_C` by itself does not
prove that an actual preparation and readout distinguishes the members.

## Separate boundary probe

I computed the connection and Ricci tensor directly for
`dchi^2+r(chi)^2 dOmega^2`, then substituted
`r=sin(sqrt(k)chi)/sqrt(k)`. Its scalar angular Hessian is
`Hess^theta_theta F=(r_chi/r)F_chi`. Since `Ga-Gt=2k`, the angular-minus-time
equation is therefore

    2kF-rho0 = (r_chi/r)F_chi
              = sqrt(k) cot(sqrt(k)chi) F_chi.

This derivation never divides by `r_chi`. At the equator the proper-radius
metric is regular (apart from the usual angular chart poles), while the
coefficient `r_chi/r` vanishes. Off the equator, the invariant
`(F-rho0/(2k)) cos^2(sqrt(k)chi)` is constant. A finite field forces that
constant to vanish on each hemisphere. There is no nonconstant smooth piecewise
continuation through the equator within the stated static spherical ansatz.

The resulting constant branch satisfies the metric equations only when
`F0=rho0/(2k)` and `V(F0)=rho0/2`; its scalar equation separately requires
`V_F(F0)=3k`. Finite `Z(F0)` and higher derivatives of `V` remain undetermined,
subject to any separately imposed kinetic condition. For example,
`V=rho0/2+3k(F-F0)+h(F-F0)^2` leaves `h` arbitrary.

This constant branch must be solved separately from the local nonconstant
action family. Its slope condition `+3k` is different from the local family's
center slope `-6k`, and the latter's `Z` diverges as `C` approaches `F0`.
Treating the profile limit as a smooth limit of those actions would be invalid;
the source explicitly avoids that inference.

For the displayed local members, `r_zero=sqrt(2C/rho0)` lies between the stated
`R` and the equatorial radius. Thus extending the same positive branch already
encounters `F=0` before the equator. The local result and this larger-domain
conditional result are compatible. A complete spherical geometry with the
same dust everywhere is an additional hypothetical input, not something the
local construction or this check establishes. No general global action
uniqueness, stability, history, or measured action selection follows.

## Exact next obligation

To make progress toward discrimination, derive a coupled metric-scalar-dust
response with each candidate action held fixed, specify a source preparation
and observable readout whose required inputs are independently justified, and
show which response combination depends on `C`. The current exact background
family and hypothetical global boundary do not supply that experiment or its
history. No source edit is required by the completed check. This next physical
response obligation remains open; it is distinct from a pending computation
in the present check.

## Execution evidence

All completed runs used Python 3.12.8 and SymPy 1.14.0.

| Completed checker | Evidence | Successful / failed |
| --- | --- | --- |
| `check_material_factored.py` | `factored_evidence.json`, `factored_stdout.txt` | 35 / 0 |
| `check_boundary.py` | `boundary_evidence.json`, `boundary_stdout.txt` | 13 / 0 |
| `check_conservation.py` | `conservation_evidence.json`, `conservation_stdout.txt` | 3 / 0 |

The first `check_material.py` attempt was interrupted after 9 minutes 22 seconds
wall time and 6 minutes 57.40 seconds accumulated CPU time, while SymPy expanded
the rational Cartesian spatial equation. Its code, traceback, and measured
process cost are preserved. It generated no completed evidence JSON and is not
counted as a successful run. `SESSION_FAILURES.md` records the interruption.

The completed core checker changes only rational simplification from
`factor(cancel(e))` to `factor(cancel(together(e)))`, adds incremental progress,
and uses a separate evidence filename. Its run was bounded to 120 seconds by
`subprocess.run(..., timeout=120)` and completed in 3.738660874776542 seconds
with exit code 0. `attempt02_execution.json` preserves timing and child resource
use; `attempt02_changes.diff` preserves the exact checker delta. There was no
mathematical failure in this replacement run and no change to either source.

The JSON evidence stores every residual, source hash, and checker hash. The
stdout files preserve actual output. `MANIFEST.json` binds the saved artifacts
and excludes its own recursive hash. To reproduce the completed core check,
run `check_material_factored.py` from this directory under an external timeout;
its only reads outside this directory are the explicitly named source file and
ordinary Python/SymPy runtime imports. The other two checkers have the same
source-local scope. No owned checker remains running.
