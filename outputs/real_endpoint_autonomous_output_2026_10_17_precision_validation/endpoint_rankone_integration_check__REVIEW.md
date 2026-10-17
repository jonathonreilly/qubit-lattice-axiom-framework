# Integration check: corrected structured positive-block corollary

Finding: the exact corrected draft supports the full four-state identity, positivity, inclusion in the checked (P1) contract, sharper fixed-phase ratio bound and stated .000347/.001347 operator ceilings. No further mathematical correction is needed. This checks the root's corrected draft as written; it does not validate the earlier incorrect structural source or constitute an independent origin of its correction.

## Sources, exposure and limits

Root draft, read fully: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/endpoint_precision_publication/RANKONE_COROLLARY_DRAFT.md`, SHA256 `564fd057908dbb4c8919271c8bdf066d4376460a890b57f4f5ae4a2217d435d1`.

Current W note: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`, SHA256 `bdd1e8ab42bf472a9f75c01e598c15857f0e383a09f06b80f8cfd59b8ab0a39e`. Its appended positive precision section, from (P1) through the stated scope, was read completely. Its nominal body at supplied milestone97ccd9f9 was previously read under SHA256 `bc75051b87d62e65ea7953f11c2fcd320f1a9ab853c7a346f32e9314859cb1a5`; the canonical Q convention is reused from that verified body.

Positive-contract independent review, read fully: `../endpoint_static_precision_check/REVIEW.md`, SHA256 `40f7649071bc0eeb192a7832c64510c4185d39d31b6c27e9064a77fd5fa6a5f5`.

Root reported independently spotting the |11> failure and supplied this corrected draft before the check. The correction and desired constants were exposed to this reviewer; this is source-exposed integration review, not a new independent discovery of either construction or correction. The corrected original structural proposal was pending and was not needed to establish the algebra of this exact draft. Previous related endpoint/source work is exposed. No scientific execution, inherited runner, simulation, numerical integration or Git operation occurred. Only source reads/hashes and this report write occurred; no W, publication, checkpoint, source, prior-report or prompt edits were made.

## 1. Full four-state operator and positivity

Use the ordered basis |00>, |10>, |01>, |11>, with the emitter first. The canonical definition is

    Q(-kappa)=kappa(n_e+n_end)
                    -kappa(a_e* a_end+a_end* a_e).

It has vacuum value0, one-excitation matrix [[kappa,-kappa],[-kappa,kappa]], and double-occupation value2kappa. Set t0=kappa0/J, alpha0=kappa0²/J and e_base=E0-alpha0. The canonical E0>.0048 and J>.03 ensure e_base>0 at kappa0=10^-8.

For chi_t=t|10>-|01>, the draft's operator

    B(t)=e_base n_e+J[|chi_t><chi_t|+(1+t²)|11><11|]

is a sum of positive operators on the same adjacent qubit pair. It is real and number-conserving. chi_t is deliberately not normalized: its squared norm is1+t², and the coefficient J in front of its outer product is therefore exactly the desired one-excitation matrix scale. Its full matrix has blocks

    vacuum: 0,
    one excitation: [[e_base+Jt²,-Jt],[-Jt,J]],
    double occupation: e_base+J(1+t²).

With t=r t0, kappa_a=Jt=r kappa0 and Delta=(r²-1)alpha0, one has e_base+Jt²=E0+Delta. The three canonical positive terms in the draft have identical values in every sector:

    Q(-kappa_a)+(E0+Delta-kappa_a)n_e+(J-kappa_a)n_end.

In particular their |11> value is 2kappa_a+(E0+Delta-kappa_a)+(J-kappa_a)=E0+Delta+J, exactly the draft's value. At r=1 the equality is to the original full local block, with |11> value E0+J. This is stronger than equality only on the one-head sector.

The original completion (1-t)² would instead give e_base+J(1-t)²=E0+Delta+J-2kappa_a on |11>. At nominal t0 it is deficient by2kappa0, exactly as the correction record says. The corrected1+t² is necessary for the advertised full-operator identity. The correction does not require any auxiliary qubits or change of graph support.

The other ordinary J bond at the endpoint remains present, so its total one-head diagonal is2J. The background is therefore unchanged. The block vacuum value remains0 and no new common scalar c_new is introduced. This corollary is not the different fixed-spectrum rotation, which changed the background endpoint diagonal.

## 2. Exact inclusion in (P1)

For r in [1-4e-6,1], r lies inside [1-1e-5,1], kappa_a is positive and does not exceed the checked upper endpoint10^-8. Also

    |r²-1|<=1-(1-4e-6)²
             =8e-6-16e-12<8e-6,
    |Delta|<8e-6 alpha0<1e-5 alpha0.

Thus this entire structured family is a literal subset of (P1), not merely a perturbation presumed close by continuity. The full block identity above identifies the actual Hamiltonian, including the compensation, with an allowed Hamiltonian in that contract. Consequently its already checked real spectral/mass, full Schur, complete localized/tail, seed, phase and finite-transfer bounds apply without an additional background-change argument.

In particular the actual-to-own-waveform ceiling remains <.000320 for every t>=4e21, with both q_a and q_0<10^-10, and the same fixed M=2e23 finite transfer<.001 on [4e21,8e21]. These are imported conditional results from the checked positive contract, not re-proved here. The supplied background, J, old K/W, seed and exact baseline remain part of their hypotheses.

## 3. Sharper complex fixed-target comparison

With x=E(k)-E0, z=exp(ik), D0=x+alpha0 z and Da=x-Delta+r²alpha0 z, the prescribed correlation gives exactly

    Da-D0=(r²-1)alpha0(z-1),
    Fa/F0=rD0/Da.

No fixed propagation or scattering phase is dropped: the ratio cancels the identical numerator factors at the same reference planes. On I subset(0,pi),

    |z-1|/sin(k)=2sin(k/2)/[2sin(k/2)cos(k/2)]
                  =1/cos(k/2)<1.1.

The numerical band margin follows from the exact k0 definition: q0>4 implies cos(k0)>15/17, hence cos(k)>.88 throughout the sigma=10^-6 band. Thus cos²(k/2)>.94 and 1/cos(k/2)<1.1. This bound is on the unchanged band, not an assumption of k=0 or a linearized phase.

Since |D0|>=alpha0 sin(k), the relative denominator perturbation is at most eta_r=1.1|r²-1|<8.8e-6. Subtracting the full complex ratio gives

    |Fa/F0-1|<=(|r-1|+eta_r)/(1-eta_r)=epsilon_r.

Using |r-1|<=4e-6,

    2epsilon_r<2*(4e-6+8.8e-6)/(1-8.8e-6)<.000026.

The non-strict intermediate form correctly includes r=1, where the exact error is zero. The final uniform numerical ceiling is still strict.

For g=Fa/sqrt(p0), ||g-f0||<=epsilon_r and ||g||=sqrt(pa/p0). Positive normalization gives ||fa-g||=|1-||g||||<=epsilon_r. Hence ||fa-f0||<=2epsilon_r with the common complex phase fixed; no arbitrary phase optimization or reciprocal normalization penalty is needed. The reference masses are the actual positive band integrals already covered by (P1).

## 4. Complete error sum and finite target

Common Fourier evolution and half-line restriction contract the profile difference. Positive normalization of each physical half-line packet costs q_l², so

    ||beta_a-beta_0||<.000026+2e-20.

This is an upper-bound comparison and therefore does not require the lower-bound projection qualification relevant to the separate detuning limitation. It tensors the same old unitary and blank-output isometry, with no extra old-column aggregation factor.

Adding the imported actual-to-own-waveform error yields

    infinite complete error<.000320+.000026+2e-20
                            <.000347.

The explicit rounded margin is almost10^-6. Adding the unchanged finite transfer<.001 gives <.001347 on [T,2T]. Equivalently start with the actual finite bound. The finite device is fixed before delivery; the target stays the embedded infinite nominal beta_0, without finite-profile renormalization.

Twice the operator ceilings are exactly .000694 and .002694, the stated unhalved trace ceilings. Arbitrary passive references, all emitter/source/core/closed-tail outputs, exp(-ic_new t) and full exp(-itK)W are retained through the imported contract. A stipulated preparation-isometry norm error adds once by unitarity. These numbers meet historical .0013/.0023 OPERATOR tolerances, but do not preserve the tighter actual-parameter .000320/.001320 guarantees.

## 5. Units, precision scope and disposition

t=kappa/J is dimensionless in the supplied model units. Its relative reduction is <=4e-6 and its absolute change is bounded by

    |t-t0|<=4e-6*kappa0/J<4e-6*10^-8/.03
                           <1.34e-12.

The draft's absolute tolerance is therefore correct and is not a dimensional energy tolerance. The emitted energy detuning is separately Delta=(r²-1)kappa0²/J. The positive e_base and J are fixed supplied coefficients. Arbitrary baseline errors, generic block scaling, independent matrix-entry errors, or errors elsewhere in the Hamiltonian are outside the corollary. Positivity and rank-one structure alone do not provide a mechanism that protects the baseline.

The corrected draft can be integrated as this conditional structured-parameter corollary, subject to the same source qualifications as (P1). Its pending corrected-source review remains a provenance/integration task, not an algebraic gap in the exact draft examined here. Preserve the original |11> defect and correction record. No new independent origin, scientific execution, native precision mechanism, retained audit, universal robustness, practical units/runtime or permanent finite-storage claim follows from this review.
