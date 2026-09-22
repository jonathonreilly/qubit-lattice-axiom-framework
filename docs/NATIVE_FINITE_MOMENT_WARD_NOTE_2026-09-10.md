---
claim_id: native_finite_moment_ward_note_2026-09-10
claim_type: bounded_theorem
claim_scope: "Finite-moment Ward error bounds and a certified fifth half-moment supplier in the supplied native model; historical fixed-family negative certification deferred."
upstream_dependencies:
  - native_ward_direct_overlap_note_2026-09-10
  - native_finite_excitation_ward_note_2026-09-09
runner: scripts/native_finite_moment_ward_2026_09_10.py
actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
bare_retained_allowed: false
---

# Finite moments for the native Ward scalar

**Type:** bounded_theorem

**Status: conditional-support.** Historical canonical and runner review assertions are preserved in the original packet. Two completed degree-(1,0) certificates are inconclusive. A separate historical saved-data screen addresses that fixed-family question; its negative certification is deferred under the current claim disposition below. A new positive-integral certificate supplies the fifth half-moment needed by a different, higher-first-degree route. None of these statements determines the sign or nonvanishing of the physical node scalar.

Use the original supplied infinite Gaussian reference, CAR and normalization of the [direct overlap note](NATIVE_WARD_DIRECT_OVERLAP_NOTE_2026-09-10.md) and [bounded Ward theorem](NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md). In particular D_A=H0+B_A≥δ=h/4, R_A=−D_A⁻¹, g=γ0 and J_A=2iγ(d_A), with J_A*J_A=8h²I. There are fifteen two-link defects and ninety ordered disjoint pairs. The disjoint-pair adjacency T has norm6. The exact identity is

    8α = <x,Tx> − Re<x,Tg v>,
    x_A=R_AΩ,   v_A=R_A J_A R_AΩ.

The reference constant c=<B_A>=μ/3 is not the impurity ground-energy shift. All local formulas below use h=1; restoring units gives α in h⁻².

## A computable residual certificate

Choose real polynomials p_A and q_A. Put uhat_A=p_A(D_A)Ω, xhat_A=−uhat_A, b_A=J_A uhat_A and vhat_A=q_A(D_A)b_A. Define certified nonnegative residual bounds

    r_A ≥ ||(1−D_A p_A(D_A))Ω||,
    t_A ≥ ||b_A−D_A vhat_A||,
    e_A=r_A/δ,   f_A=(j e_A+t_A)/δ,   j=2√2h.

Coercivity gives ||x−xhat||≤E=||e|| and ||v−vhat||≤F=||f||. Also ||x||≤X=√15/δ and ||v||≤V=j√15/δ². Expanding the two quadratic expressions, using ||T||=6 and ||g||=1, proves

    |8α−What| ≤ 6[E(2X+E)+EV+(X+E)F],
    What=<xhat,T xhat>−Re<xhat,Tg vhat>.

This retains the original boundary sources. It makes no impurity-vacuum replacement. A strict sign conclusion requires the entire nominal interval to exceed the certified error interval in magnitude.

Finite polynomial residuals reduce to finite vacuum moments and Wick contractions. The complete local derivations, including domain and convergence premises, are preserved in the packet's HIERARCHY.md and DEGREE10.md. For degree-one p, the vacuum moments m0 through m4 are respectively

    P: 1, c, 2, 10c, 20+36c²−2cν/3,
    O: 1, c, 2, 4c+ν/3, 22+4cν/3.

The two fixed choices solve either the residual normal equations (m2 m3; m3 m4)p=(m1,m2), or the variational equations (m1 m2; m2 m3)p=(m0,m1). The actual interval residuals are checked afterward. There is no fitted choice based on the eventual sign.

## Historical fixed-family exclusion evidence — current certification deferred

The following argument records the original narrow conditional evidence. It is not a currently closed negative claim; the constructive hierarchy and moment supplier do not require this exclusion.

Fix one tested p family and let a=||xhat||. Since J_A*J_A=j²I, ||b||=ja exactly. For any domain vector vhat, let T_res bound ||b−D vhat||. Then ||vhat||≤(ja+T_res)/δ and

    |What| ≤ 6[a²(1+j/δ)+a T_res/δ].

The same reported error satisfies F≥T_res/δ. Set C=E(2X+E+V). Because a≤X+E, subtraction yields

    |What|−Error ≤ 6[a²(1+j/δ)−C].

Thus C≥a²(1+j/δ) excludes both strict sign gates for every second polynomial, with this fixed p and this error estimator. Equality also excludes a strict gate. This is a quantified certificate-family limitation, not a physical no-go.

The saved source norms give a²=(12s0P+3s0O)/8 at h=1. The separate screen uses lower endpoints for C and upper endpoints for a²(1+8√2). Both completed fixed modes satisfy that sufficient inequality. The original degree-(1,0) run itself remained INDETERMINATE_SIGN; the subsequent screen, using only saved E and s0 intervals, returned CERTIFICATE_FAMILY_EXCLUDED for both modes. Neither completed calculation was replayed in this package.

## The new fifth half-moment supplier

Write X=6−2Σcosθ in the canonical dispersion, A(t)=E[(X+t²)⁻¹], M1=6, M2=42, and ω5=E[X^(5/2)]. Tonelli and polynomial division give

    ω5=(2/π)∫₀∞Q5(t)dt,
    Q5(t)=E[X³/(X+t²)]=42−6t²+t⁴−t⁶A(t).

The existing catalog has1742 Gauss nodes and3484 endpoint oracle evaluations, each returning A and A′. No new oracle was called for ω5. On a dyadic panel[a,2a], the rho4 ellipse is z/a=3/2+(17/16)cosθ+i(15/16)sinθ. Since (3/2)²−(17/16)²−(15/16)²=31/128>0, Re z>|Im z| and Re z²>0. Therefore |Q5(z)|≤EX²=42, with analytic domination. Degree51 exactness of Gauss26 and the Chebyshev tail bound give panel radius (16/3)a M4⁻⁵². Summing the67 panels from2⁻⁶⁴ to8 gives radius below1792·4⁻⁵²; the implemented certificate conservatively uses1904·4⁻⁵².

At ε=2⁻⁶⁴, L=42ε−2ε³+ε⁵/5 and the low integral lies in [L−(17/60)ε⁷/7,L]. The correction has negative sign. At t≥8, forty terms give

    Σ(n=0..39)(−1)^n M(n+3)/[(2n+1)8^(2n+1)],

with nonnegative remainder at most M43/(81·8⁸¹). Exact phase multinomials provide those integer moments; directed input and arithmetic intervals, Machin π bounds, and all low/middle/high pieces remain separate in the saved output. The accepted full width is below the predefined10⁻²⁴ target. The root's saved reconciliation covers all1742 node and tail arithmetic steps; this package reuses that certificate rather than replaying it.

This supplier enables different first-polynomial routes. For example the reviewed degree-(2,0) algebra uses O_iΩ=D^iΩ through i=3, with O2 generally not Hermitian as a local polynomial. Moments must use O_i*O_j with actual reversed words and conjugated coefficients. The required sixth vacuum moment and cubic-source contractions close on c,ν,ω5. That is a source theorem and prospective implementation boundary; no higher-degree numerical outcome is claimed here.

## Evidence and remaining work

The packet copies exact original results, receipts, proof sources and an original-to-local hash map. Original NOT_EXECUTED wording in historical derivations records their prelaunch status; current execution claims derive only from the separately copied accepted receipts. The compact runner checks identity controls and preserved result structure only. It does not invoke a native solver, oracle, catalog integrand, or saved full-node reconstruction.

Independent constituent checks do not replace independent review of this assembled note. The original packet records historical parent and affected-runner review outcomes; current source review is separate. Full integration pipeline, changed-audit readiness and formal audit remain UNRUN; citation graph delivery receipt is recorded in the packet. The full α remains open. The appropriate next test changes the first polynomial or proves a sharper state-dependent error estimate; the historical fixed-p screen does not certify the outcome of a different estimator.


## Current compact evidence boundary

The [canonical cache](../logs/runner-cache/native_finite_moment_ward_2026_09_10.txt) records only the current compact receipt, identity and synthetic checks. The current capture budget is 30 seconds and 384 MiB with external process-tree supervision. Historical source, results and resource receipts retain their original identities and protocol limits; this compact run does not repeat their numerical calculations. The raw original packet and its input manifests are retained under `outputs/native_finite_moment_ward_2026_09_10_inputs/`. Historical review assertions are provenance, not a current review verdict.

## Current claim disposition

Current claims are the constructive identities, valid conditional enclosure bounds, moment-supplier constructions and explicitly finite certificate outcomes described above. Certification of the historical constant-trial/all-q exclusions, zero-dual exclusion and norm-only optimality claim is deferred: the exact-target No-Go Discipline route requirement is unmet. Their original proofs and results remain byte-exact in the input packets as historical conditional evidence. They are not current closed negative claims or premises needed to establish the constructive bounds.

## No-Go Discipline record and limitation

Historical argument (current negative certification deferred): The all-q obstruction concerns only the two frozen first polynomials, the original gap error estimator and certified residual bounds. The constant-trial obstruction concerns the specified residual-optimal constant p, constant q and stated scalar inputs. Neither is an obstruction to alpha or to all estimators.

**N1 — Actual mechanisms and unresolved quota.** The unit records the following five genuinely different historical mechanisms. They are not five failed in-domain attacks against any one negative theorem. The exact-target five-route requirement is not established by this inventory; no No-Go Discipline Gate PASS is asserted for those negative claims. The table preserves actual attempts without inventing additional tests.

| Mechanism | Actual retained outcome | Relation to the original all-q obstruction |
| --- | --- | --- |
| Polynomial inverse approximation with gap-residual error | Degree10 and degree20 certificates remain indeterminate | Only the frozen degree10 first polynomials and original estimator are covered; degree20 lies outside |
| Posterior trial-norm enclosure | Degree10 and degree20 certificates remain indeterminate | A different error functional, outside that obstruction |
| Quadratic spectral-residual envelope | Two fixed degree10 choices remain indeterminate | A different estimator using residual moments |
| Correlated signed-dual correction | Five fixed scales narrow the enclosure but remain indeterminate | A different center and error estimator |
| Quartic spectral envelope with higher Gaussian moments | Two same-degree20 modes remain indeterminate | A new moment mechanism and first polynomials outside the original target |

Changing polynomial degree alone, changing lambda, or supplying the moments does not create an additional mechanism family. No row rules out the full physical alpha problem.

**N2 — Dependencies, not independent obstructions.** The supplied model, reference and CAR/normal-order conventions define the objects; the Ward identity defines the observable; the channel gap controls inverse bounds. Certified numerical moments are downstream conditional data, not independent physical constraints. The determinant germ uses bounded h0, finite-rank perturbation and absence of a zero atom; it does not itself require the impurity gap. The inverse and quartic estimates separately require that gap. No count of independent impossibility arguments is inferred from these dependencies.

**N3 — Exact hypotheses.** The all-q bound retains the frozen first polynomial and original residual error functional, with honest residual bounds for the second trial. The constant-trial statement retains the specified constant choices and scalar inputs. The zero-dual screen retains its original errors. Norm-only sharpness allows abstract error vectors obeying the stated norm bounds and operator premises; extra native correlations can improve the estimate. All numerical conclusions inherit the supplied model and the certified input intervals.

**N4 — Residual-to-claim record.** The paths below identify retained historical negative evidence and finite descriptive outcomes, not current negative certification or new executions.

| Retained record | Exact residual or conclusion | What it does not establish |
| --- | --- | --- |
| Finite-moment `imports/ALL_Q.md` and `ALLQ_RESULT.json` | Neither strict-sign test succeeds for the frozen p and original error estimator | Failure of another p or estimator |
| Finite-moment `imports/DEGREE10.md`, constant section | The specified original constant p/q sign test is inconclusive | Failure of every constant trial or error bound |
| Correlated `source_draft/proofs/sharp.md`, section 2 | Sharp abstract norm-only remainder, with extremizers in the 6 and -3 eigenspaces | Realization by the actual native errors |
| Correlated `source_draft/evidence/zero/RESULT.json` and sharp proof section 1 | The fixed zero-dual lower-endpoint screen does not become strictly positive | Failure of signed-dual corrections |
| Signed-dual and quartic saved results | Particular certified enclosures contain zero | A general physical no-go or alpha equal to zero |

**N5 — Resolution and execution scope.** Per element: exact rational, sign and identity checks apply to the retained finite inputs. Per site: no new sitewise native calculation is executed. Per mode: only the stated saved modes and candidates are compared. Per block: compact receipt checks and synthetic controls cover the declared packet. Lattice wide: infinite-model conclusions rely on their stated analytical proofs and premises; compact checks do not replay the numerical catalog, native moments or an infinite lattice.

**N6 — Missing implication.** Indeterminate certificates leave a sign decision open; they do not require a new axiom. A better first polynomial, a sharper certified residual estimate or additional justified correlations can change the certificate. Those routes require their own compatible nominal, residual and input proofs.

**N7 — Concrete steelman.** A signed-dual route takes y=s(V-tJU) and z=-tU, retains the signed corrections <r,y>+<s,z>, and computes both residual norms from complete Gram data. A successful attack would certify the corrected positive endpoint. The retained lambda=1 attempt narrows the interval but does not prove that endpoint positive. A richer first polynomial with certified higher moments is another concrete route. These escapes change the old obstruction's domain; they preserve its narrow algebra while preventing a universal inference. Scaling lambda scales both trial vectors linearly, not quadratically.

**N8 — Prior-work echo.** The constant-trial limitation led to degree-one/two trials; the original all-q error obstruction led to posterior and spectral estimators; the zero-dual limitation led to signed corrections. These are recorded changes of scope, not proofs of a physical sign and not demands for new axioms. The unresolved exact-target N1 quota remains a packet limitation, separately from validity of the conditional algebra and positive enclosure constructions.

The current [hierarchy proof](work_history/repo/review_feedback/pr8079-evidence/kept/pr8079-HIERARCHY-3d2cbcb326f3df28.md) and [degree-one proof](work_history/repo/review_feedback/pr8079-evidence/kept/pr8079-DEGREE10-bf797a38935a935a.md) are preserved raw supporting inputs of this note. Their historical execution language retains its original meaning.

## Recovered scientific input closure

The [scientific recovery manifest](work_history/repo/review_feedback/pr8079-8083-scientific-recovery/manifest.json) binds the relevant catalog geometry and endpoint records, producer and arithmetic-root sources, and saved rho5/omega5/omega79 arithmetic payloads. Existing exact catalog objects are reused from landed archives. Original compact packets retain the degree20 event stream and later trial/Gram/moment records. The manifest is a declared proof-identity input; the compact runner does not read or recompute every recovered numerical payload. Historical execution receipts keep their original dates, source identities and resource scopes.
