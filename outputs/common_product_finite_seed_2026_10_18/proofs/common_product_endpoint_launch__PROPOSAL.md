# Literal endpoint seed to a normalized directed packet

New bounded author bridge requiring a distinct check. The checked equal-diagonal emitter measure is adopted, not re-proved or claimed as new. From it and the Jacobi recurrence, this note derives an explicit outgoing packet, a complete normalized-output launch bound, and an explicit source residual. It removes supplied wavepacket preparation for the STANDALONE empty half-line launcher. It does not yet compose that launcher with the finite-distance controlled router.

## 1. Positive local launcher and supplied seed

Fix j>0 and 0<gamma<j. Label the emitter s and lead sites n=0,1,... . Use the positive local block

    B=Q_gamma(s,0)+(2j-gamma)n_s+(j-gamma)n_0

and the uniform positive lead blocks Q_j(n,n+1). Here Q_c=c(n_x+n_y-a_x* a_y-a_y* a_x), including its double-occupation diagonal 2c. B has vacuum energy zero, one-head matrix [[2j,-gamma],[-gamma,j]], and double-occupation energy 3j. Each displayed summand is positive. B has norm 3j. Together with the lead bond incident at 0, every one-head diagonal equals 2j. Thus on the bounded one-head space the operator H_gamma has emitter/lead hopping -gamma, subsequent hoppings -j, and common diagonal 2j. Its norm is at most 4j; this also follows from the checked spectrum. No unrestricted infinite-many-head bounded sum is asserted.

This is exactly the positive weak-end family in endpoint_bandcenter_reference section 1 with J=j and kappa=gamma. Counting B as one block, incident norm sums are 3j at s, 5j at lead site 0, and 4j at subsequent sites. Counting its three positive summands separately gives 2j+gamma at s and 3j+gamma at site 0, with the same 4j lead-interior sum. The convention must accompany any load cap. All supports may be nearest neighbors along a straight cubic path. Exact diagonals/coefficient correlation and absence of extra interactions remain supplied.

The initial state is |s>: emitter occupied, every other head vacant. Two disjoint IDENTICAL copies give an encoded path qubit alpha|s_L>+beta|s_R>, tensored with any passive program/reference system. For a basis path this is a sitewise product seed. An arbitrary encoded path qubit is not falsely called a product across its two emitter sites; its logical input coherence is supplied, while all other heads are vacuum. Evolution below is identical on the two path labels and cannot add a relative path phase. No program controls this standalone launcher.

## 2. Adopted checked reference and new exact spatial columns

Set

    E(q)=2j(1-cos q),
    a=2j-gamma^2/j, d=gamma^2/j,
    D(q)=a^2 cos^2 q+d^2 sin^2 q,
    w(q)=2 gamma^2 sin^2 q/[pi D(q)], 0<q<pi.

The reference check 1953d153 proves that w(q)dq is the complete emitter spectral probability measure, with integral one and no omitted atoms or singular mass. It also proves emitter cyclicity. Those are adopted checked premises, not new results here. Its scalar resolvent is [z-gamma^2 m(z)]^-1, with m(-2j cos q+i0)=-e^{iq}/j; the centered resolvent variable is distinct from the full physical E(q).

Use the cyclic spectral representation in which the emitter column is phi_s(q)=sqrt(w(q)), positive. The source equation gives phi_0=(2j cos q/gamma)phi_s. The first lead equation and subsequent uniform recurrence then give, for n>=0,

    phi_n(q)=sqrt(w(q))/(gamma sin q)
        [2j cos q sin((n+1)q)-(gamma^2/j)sin(nq)]
      =sqrt(2/pi) [a cos q sin((n+1)q)
                              +d sin q cos((n+1)q)]/sqrt(D(q)). (1)

The first expression follows by induction from the Jacobi recurrence, including n=0; the second uses sin(nq)=sin((n+1)q)cos q-cos((n+1)q)sin q. No separate spectral multiplicity or normalization is inserted. The checked cyclic spectral theorem makes these columns the full physical representation.

Define the unit-modulus function and the two spectral amplitudes

    u(q)=e^{iq}[d sin q-i a cos q]/sqrt(D(q)),
    g_+(q)=u(q)sqrt(w(q)),
    g_-(q)=conjugate(u(q))sqrt(w(q)).

Then (1) is exactly

    phi_n=(2pi)^(-1/2)[e^{inq}u+e^{-inq}conjugate(u)],

and ||g_+||_L2=||g_-||_L2=1. Both amplitudes are smooth up to the endpoints and vanish there. With

    (O_t f)_n=(2pi)^(-1/2) integral_0^pi e^{inq-itE(q)}f(q)dq,
    (I_t f)_n=(2pi)^(-1/2) integral_0^pi e^{-inq-itE(q)}f(q)dq,

the COMPLETE exact seeded state is

    exp(-itH_gamma)|s>=A(t)|s>+O_t g_+ + I_t g_-,
    A(t)=integral_0^pi w(q)e^{-itE(q)}dq.             (2)

Lead vectors are embedded with source coordinate zero. The two lead terms interfere and are not separately asserted to be normalized half-line states. The full state in (2) has norm one. Increasing n is the outgoing direction because E'(q)>0. The complex factor u and the phase e^{-itE(q)}, including the common e^{-i2jt}, are part of the target; none is fitted away.

## 3. Explicit source residual

The function w/E' is

    h(q)=gamma^2 sin q/[pi j D(q)].

It vanishes at both endpoints. Since a>d>0,

    h'(q)=gamma^2 cos q
       [a^2+(a^2-d^2)sin^2 q]/[pi j D(q)^2].

It increases to q=pi/2 and decreases thereafter. Thus

    integral_0^pi |h'(q)|dq=2h(pi/2)=2j/(pi gamma^2).

Integration by parts against e^{-itE}, with the vanishing endpoint terms, proves for t>0

    |A(t)|<=R_t:=min{1,2j/(pi gamma^2 t)}.           (3)

This is an actual occupied-emitter amplitude bound, not only lost spectral mass or an expected occupation. It charges residual source output in the full comparison below. The bound is sufficient and not optimized; it does not assume exponential decay or substitute a Lorentzian for the checked density.

## 4. Normalized directed packet and complete finite-time error

Choose 0<sigma<sigma'<pi/2 and a real C1 cutoff chi with 0<=chi<=1, equal to one on |q-pi/2|<=sigma, and compactly supported in |q-pi/2|<sigma'. Its exact shape is supplied as a comparison-function choice, not a physical time-dependent control. Adopt the checked reference bound

    p_sigma=integral_{|q-pi/2|>sigma}w(q)dq
       <=P_sigma:=min{1,4gamma^2/[pi a^2 tan sigma]}.  (4)

Hence ||(1-chi)g_+|| and ||(1-chi)g_-|| are at most sqrt(P_sigma). For f=chi g_- define

    v_*=2j cos sigma'>0,
    B_f=||f'||_L1+(2j/v_*)||f||_L1,
    L_t=B_f/sqrt(2pi) sqrt[(t v_*)^-2+(t v_*)^-1].

Direct nonstationary integration by parts gives ||I_t f||<=L_t. At site n its phase derivative has magnitude at least n+t v_*, and its second derivative is at most 2jt. The endpoint terms vanish; the site bound is B_f/[sqrt(2pi)(n+t v_*)]. Squaring and summing uses sum_{n>=0}(n+A)^-2<=A^-2+A^-1. This reuses the method of the preceding router proposal, but applies it to the now explicitly DERIVED launch amplitude.

Both O_t and I_t have norm at most one as maps from L2(0,pi) to ell^2(N_0): extend f by zero on the rest of a Fourier period, apply Parseval on all integer sites, then restrict. Therefore the undesired incoming vector is bounded by L_t+sqrt(P_sigma), and removal of the outgoing exterior band costs at most another sqrt(P_sigma).

Let W_t=O_t(chi g_+), with zero source coordinate, and set

    delta_t=sqrt[R_t^2+(L_t+2sqrt(P_sigma))^2].

Source and lead coordinates are orthogonal, so (2)--(4) give

    ||exp(-itH_gamma)|s>-W_t||<=delta_t.             (5)

Whenever delta_t<1, q_t=||W_t||>=1-delta_t>0. The complete normalized target is beta_t=W_t/q_t, with the emitter VACANT. Normalization costs at most another delta_t, yielding

    ||exp(-itH_gamma)|s>-|0_s> beta_t||
                 <=min{2,2delta_t}.                (6)

The notation |0_s> beta_t is the one-head lead state with emitter vacancy, not a tensor factor containing an extra particle. All lead sites and the residual emitter are included. No measurement, postselection, target-dependent physical renormalization, or partial trace occurs. A positive real q_t fixes the target phase uniquely relative to the formula for g_+.

For two identical disjoint launchers and arbitrary encoded input xi on path/program/passive-reference,

    ||U_launch(t)J_seed xi-J_out(beta_t tensor xi)||
                 <=min{2,2delta_t}.                (7)

The branches are orthogonal and have IDENTICAL amplitudes, so their errors combine by the same operator norm, not by a factor sqrt(2) or by summing branch errors. A passive program in its encoded |ppp> sector is unchanged. If a separately supplied common scalar cI is added, the right target is multiplied by e^{-ict}; no such scalar is dropped. Unhalved output trace/diamond error is at most twice the vector/isometry bound. No physical controlled-router attachment is included in U_launch.

For any desired tolerance, (6) provides a constructive analytical choice: choose gamma/j small enough at a fixed central band to make P_sigma small, then take t large enough to reduce R_t and L_t. The derivative integral in B_f is finite for every fixed positive gamma and specified cutoff. It can grow when gamma shrinks and has not been replaced by an unproved uniform constant. Thus this establishes a bounded existence/launch statement with explicit formulas, not an optimized runtime or apparatus performance certificate.

## 5. Exactly what is still missing for a finite-distance router

At a proposed emitter distance L, the standalone coordinate n increases TOWARD the router, whereas the earlier router radial coordinate increases AWAY from it. Identifying a packet requires the actual coordinate reversal n=L-r (with its precise endpoint convention), the phase e^{iqL}, and elapsed dispersion. Those factors cannot be silently dropped or independently fitted in different program branches.

The launcher's infinite continuation is not the finite-distance router graph. Program-dependent reflection can return to the emitter and change both its self-energy and late source amplitude. Mass one and absence of atoms proved for the reference do not establish either property for that finite network. The actual finite graph has point spectrum and recurrences; reference all-late escape cannot transfer to it.

A finite early-launch approximation is possible only with a proved geometry/time budget. A nearest-neighbor Taylor bound can protect a seed before distant changed edges are reached, but at routing/return times scaling with L it may be useless. No such bound is asserted here beyond its valid early regime. In particular, a generic finite-speed slogan or the unchanged reference measure does not bound the full process after the travel front reaches the router.

The next decisive obligation is a comparison on a specified finite graph and time window: show that the actual emitted state, after outward-to-inward coordinate identification, approximates the router's common incoming packet; propagate it through the junction while bounding source reabsorption, endpoint returns, spectral tails, mediator residual, and finite-cut output; and exhibit one positively normalized common outgoing packet for both coherent program branches. The earlier cell attachment estimate can only be applied after its actual attachment and total elapsed time are specified. This note neither claims that obligation solved nor establishes an impossibility.

ROOT subsequently suggested a concrete next route, recorded as a proposal only: choose an early empty-source time t0 and L much larger than j t0; use a C2 central cutoff and two integrations by parts for boundary amplitudes, then integrate the boundary Duhamel error. With consistent planes, proposed boundary phase derivatives are -t v for the incoming term and 2L+1-t v for the outgoing term. A window t_f v_min>L and t_f v_max<2L may exist when v_max<2v_min. Squared inverse phase-derivative tails could then yield integrated errors of order 1/t0 and 1/L, avoiding the nondecaying logarithmic allowance from a single integration. Exact coordinates, coefficients, endpoint diagonal changes, the two emitter residuals, normalization and the actual finite Hamiltonian remain to be proved; none of these proposed estimates is used in (6) or (7).

The positive result is (6)--(7): a literal emitter seed on an empty half-line launches a derived, normalized, directed packet with explicit full-output error and source residual. The supplied packet premise has been removed for this standalone launch stage, not for the complete finite router.

## 6. Exact provenance and verification limits

Fully read and SHA-256 verified:

* bandcenter_reference_measure_check/REVIEW.md, SHA1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae. Adopt only its explicitly defined equal-diagonal reference operator, complete scalar density, cyclicity and hard-band probability bound. The report itself identifies the reference by its operator, not by another source-file hash.
* endpoint_bandcenter_reference/PROPOSAL.md, SHA510d5b1b51a152f90a8c2054fab382f74fb3f31159359e9c723e89d557380b2c. Adopt only section 1's positive endpoint matrix family, with j/gamma notation. Its parity lane, old internal operation, converter claims and canonical apparatus constants are not premises.
* common_product_autonomous_interface/PROPOSAL.md, SHAbcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5, previously authored/read. Its status remains provisional; this task does not presume its newly launched check passed. Its integration-by-parts method is repeated explicitly here, and its finite-router interface is only the future composition target.

The scalar reference result is already checked at its stated scope. The new recurrence-to-packet identity, source variation calculation, normalized complete-output bound, and path/reference extension are author derivations requiring a distinct check. ROOT suggested the endpoint-launch route; that is design exposure, not independent verification. A broad canonical-note search was not used as evidence and its truncated output does not constitute verification. No old apparatus/runtime theorem is imported.

Only common_product_endpoint_launch/PROPOSAL.md was created. No scientific executable, numerical dynamics, eigensolver, symbolic solver, sweep, canonical/W/Git/PR/checkpoint/editable-prompt/model change or delegation occurred. No retained status is assigned.
