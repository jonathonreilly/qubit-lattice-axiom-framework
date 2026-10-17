# Common-offset scalar escape and actual local/core comparison

Status: new root derivation requiring a distinct check. This extends the checked original-window common-offset inverse/moment interface to represented source and background amplitudes. It does not establish traveling output, a finite runtime certificate, or closeness to the zero-offset target.

## Domain and unchanged physical premises

Use the complete domain, positive six-block installation, original physical windows, shared B, source vacuum and full-fiber definitions of `three_site_common_mode_actual_interface/PROPOSAL.md` (9225b6ea). In particular |Delta|<d, residual |r_i|<=epsilon lambda, relative squared-bond errors<=epsilon<=.005, and the physical load is m_j(D), not m_j(D-Delta). The actual inverse requires Theta<1 as defined there. Let

    y=delta-Delta, R=sqrt(y²+lambda²),
    beta=3(lambda+|Delta|)/j,
    B_eps=20epsilon+16epsilon²+4epsilon³,
    m=1-beta-B_eps,
    a_bar=a0+b0|Delta|, Dmax=d+|Delta|,
    kappa²=3jlambda(1+e3), c=(1-Theta)m.

The bounds below retain the unchanged processor's calibrated windows and all complementary columns. Delta changes a source-only potential, not a global identity. Physical carrier phases are retained in the scalar formula; no full-Hamiltonian phase equivalence is asserted.

## 1. Shifted cubic comparison for all three nominal scalar source sites

First set the relative/residual errors to zero, but retain Delta. For the scalar source seed, the three spectral polynomials in y are

    p0=1, p1=-sqrt(3)y/lambda,
    p2=(3y²-lambda²)/(sqrt(8)lambda²).

Let rho_M(y)=8lambda^5/[3pi(y²+lambda²)^3] on the full line. Its moments are 1, lambda²/3, lambda^4 at orders 0,2,4, with odd moments zero. Thus integral ||p(y)||² rho_M(y)dy=3. In the ACTUAL nominal scalar source, the centered second/fourth seed moments have these same values: H_center first reaches the port only on its third application, so its second-power norm uses only a1,a2. Equivalently its three orthonormal Jacobi polynomials each have squared norm one. This fact is valid for the isolated nominal source, not a claim that the loaded processor has that scalar spectral measure.

The physical band is |delta|<2j, delta=y+Delta. With s=sqrt(1-delta²/(4j²)) and q_Delta the nominal determinant,

    rho_Delta/rho_M = s R^6/|q_Delta|²,
    |q_Delta-(y+i lambda)^3|<=beta R³.

Consequently on the band,

    |rho_Delta/rho_M-1|
       <=[delta²/(4j²)+2beta+beta²]/(1-beta)².          (1)

Here beta<1 follows from the inherited domain. The inequality uses 1-s<=delta²/(4j²) and the squared determinant difference; it is not a density approximation at the band thresholds.

Cauchy–Schwarz gives

    integral ||p|| rho_M <=sqrt(3),
    integral ||p|| delta² rho_M <=sqrt(3)(Delta²+lambda²),

because integral delta^4 rho_M=(Delta²+lambda²)². Outside the physical band |y|>=b=2j-|Delta|. With

    V_Delta=sqrt(16/(15pi)) (lambda/b)^(5/2),

the cubic outside mass is at most V_Delta², and its vector polynomial tail is at most sqrt(3)V_Delta by another Cauchy–Schwarz inequality. The normalized physical scalar measure has no hidden atoms under the checked scalar common-mode theorem. Therefore the all-three-site scalar amplitude vector differs, uniformly in real t, from its full-line cubic integral by at most

    Evec_Delta=sqrt(3){[2beta+beta²+(Delta²+lambda²)/(4j²)]
                             /(1-beta)²+V_Delta}.      (2)

This argument bounds the integrated vector norm; it does not identify pointwise wavefunctions at unequal energies. The comparison integral retains exp[-it(2j+Delta)] and the Fourier factor exp(-ity). Its norm for t>=0 is exactly

    F(lambda t)=exp(-lambda t)*sqrt(
       (1+lambda t+(lambda t)²/3)²
       +(lambda t+(lambda t)²)²/3+2(lambda t)^4/9).      (3)

The signs and common phases of the scalar vector follow from integrating the displayed p, rather than being adjusted to fit an actual output. Only its norm is used subsequently.

## 2. Residual errors at the same supplied Delta

The checked scalar common-mode complex ratio gives

    chi=B_eps/(1-beta), nu=(1+epsilon)^(3/2)-1,
    L=(nu+chi)/(1-chi), D_rho=2L+L².

These compare the perturbed and nominal sources at the SAME Delta. They do not compare a shifted source to the zero-offset packet. The three perturbed Jacobi polynomials are

    p_e=(1, -(y-r0)/a1,
                    [(y-r0)(y-r1)-a1²]/(a1a2)).

The polynomial perturbation proof from the checked local-reference source carries over because the nominal second/fourth moments about y are unchanged, as proved above. In full detail its component L2 bounds are

    B1=1/sqrt(1-epsilon)-1+sqrt(3)epsilon/sqrt(1-epsilon),
    B2=[epsilon+(sqrt(3/2)+1/sqrt(8))epsilon
                                  +(3/sqrt(8))epsilon²]/(1-epsilon),
    Bpol=sqrt(B1²+B2²),
    Elocal=Bpol+D_rho(sqrt(3)+Bpol).                    (4)

Indeed split p_e rho_e-p rho_Delta as (p_e-p)rho_Delta plus p_e(rho_e-rho_Delta); the first integral is <=Bpol and the second <=D_rho(sqrt(3)+Bpol). The common physical carrier has unit modulus. Hence the perturbed scalar all-three-source amplitude obeys

    ||v_e,Delta(t)||<=min(1,F(lambda t)+Evec_Delta+Elocal). (5)

This is still a scalar reference statement.

## 3. Transfer to all three ACTUAL source heads

The reference last-source column is exactly

    Rref E2=(a1a2,-a2 A0,P_r)^T Qref^-1,
    A0=D-Delta-r0, P_r=A0 A1-a1².

At a selected eigenvalue its numerator has norm <=C_eps R², with

    C_eps=1+sqrt(c0²+c1²+c2²),
    c0=(2sqrt(2)/3)epsilon,
    c1=sqrt(8/3)[(1-sqrt(1-epsilon))/2+epsilon sqrt(1+epsilon)],
    c2=4epsilon/3+epsilon².

This is the unchanged polynomial inequality expressed in y; the determinant bound is mR³. On the complementary eigenvalues z=x-Delta with |z|>.1849, the same numerator estimate and |qref|>.99|z|³ give a joint-column bound <6 (including all three rows). This bound is distinct from the <6 bound for P_r/qref alone; its numerator has leading z² and the explicit smaller a1,a2 terms, so its norm is <1.000002|z|² on this domain, giving <6 as well.

The exact resolvent subtraction remains in its ordered form

    (R-Rref)E0=kappa²(Rref E2)[G-m_j(D)]a1a2 Q^-1.      (6)

No G is commuted through a source factor. On the selected input use the checked full inverse 1/[(1-Theta)mR³], and on the complementary input use 170/(1-Theta). The physical background error is bounded by a_bar+b0|y|, not merely a0+b0|y|. Integrating both lips on the unchanged physical window, which in y is a subset of [-Dmax,Dmax], gives sufficient allowances

    Dsel=kappa²a1a2/[pi(1-Theta)] * {
       C_eps/m² [a_bar*pi/(2lambda³)+b0/lambda²]
                    +6/m [2a_bar/lambda²+2b0/lambda]},

    Dwrong=170kappa²a1a2/[pi(1-Theta)] * {
       C_eps/m [2a_bar asinh(Dmax/lambda)
                    +2b0(sqrt(Dmax²+lambda²)-lambda)]
                          +12a_bar Dmax+6b0 Dmax²}.    (7)

For the selected integral we extended positive integrands to the full real line. The four needed integrals are pi/(2lambda³), 1/lambda², 2/lambda², 2/lambda for 1/R4, |y|/R4, 1/R3, |y|/R3. For wrong inputs the finite symmetric enclosure gives the asinh and square-root integrals. The coefficients retain both spectral lips. Lower-lip Q is treated separately, not declared the adjoint of upper-lip Q.

The scalar reference has the same exact shifted sixth moment as the installed prefix, so truncation outside its original-center window costs at most eta_ref=sqrt(2mu6)/(d-|Delta|)^3 under the inherited two-input convention. Applying the same orthogonal-input/record aggregation as the checked local/core interface, the REPRESENTED actual source amplitude is bounded for t>=0 by

    S_Delta(t)<=F(lambda t)+Evec_Delta+Elocal+eta_ref
                                      +sqrt(2)Dsel+2Dwrong. (8)

An optional min(1,...) cannot be asserted for the represented vector solely because it is spatially restricted after spectral truncation unless that contraction is explicitly used; all factors here are contractions, but the displayed safe sum suffices. The ACTUAL global omitted state is separate and has not been added to (8). It must be charged once in a later complete synthesis. Reference truncation is a different error.

## 4. Background coordinates and closed tails

The source compression is unchanged, so the checked full background recovery L0=14000 still applies. The source-to-background column is -kappa L a1a2 Q^-1. Extending the shifted-window integral of 1/R³ to the real line and paying both physical windows/lips yields

    B_Delta(t)<=4kappa a1a2 L0/[pi(1-Theta)m lambda²]
             <=8sqrt(2)(1+epsilon)kappa L0/(3pi c).     (9)

It includes every non-source finite coordinate and every closed tail, not the propagating stationary ray. No claim about outgoing/incoming packets or physical normalization follows from (8)–(9). The actual outside state remains uncharged in both represented pieces.

## Scope and checks needed

The new steps needing selective checking are the shifted all-three-site cubic density comparison (1)–(3), moment-based transfer of (4), actual shifted-window Stone integrals (7), and their use without moving the physical windows or changing the load. Full conditions and conditional physical calibration are inherited, not rederived. No numerical performance point, runtime, finite receiver, permanent Record, native supplier or complete-output theorem is asserted. Common-offset waveform/phase and processor energy dependence remain necessary traveling/time obligations.

Root authored this extension and previously authored local-reference and outgoing ancestors. The independent common-mode and actual-interface checks are reused evidence, not blind independence. No numerical dynamics, integration, sweep, solver or scientific runner was used. Only this research proposal was written; no axiom, prompt, Git, canonical or audit modification.

## Exact source pins

- `three_site_common_mode_source/PROPOSAL.md`: `5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb`.

- `three_site_common_mode_source_check/REVIEW.md`: `af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb`.

- `three_site_common_mode_actual_interface/PROPOSAL.md`: `9225b6ea6533dea56db4f8b7157deac5c6f52e5927b554052c59299622a13957`.

- `three_site_common_mode_actual_interface_check/REVIEW.md`: `e9b32196906e1d4b5010ac9b30d348e438d6e88fcdac82d51ae107f3f7ba1cea`.

- `three_site_perturbed_local_reference/PROPOSAL.md`: `b36ef9001996fd031bfabd8541776be27831050cac6b67fee1016cf10f04b504`.

- `three_site_perturbed_local_reference_check/REVIEW.md`: `3db966162b1c49a28041a8c0a04eaa9c5bebb7613718894d43227b3e65cd18c7`.

- `three_site_perturbed_local_core/PROPOSAL.md`: `7c5fcdae5cb9682e6d4f1babe1390ddbb58446416df0f4309fb056f14c1688a7`.

- `three_site_perturbed_local_core_check/REVIEW.md`: `e23d90ee489dcded97cb2397e95e378b7cba3c58747110a0ac1849036a7bc990`.

- `prepared_core_recovery/PROPOSAL.md`: `cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9`.

- `prepared_core_dwell_check/REVIEW.md`: `88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819`.

- `prepared_core_composition_check/REVIEW.md`: `52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c`.
