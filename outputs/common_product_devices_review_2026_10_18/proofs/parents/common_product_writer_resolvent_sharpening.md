# Exact band-center writer inverse and a uniform bound of ten

New authored bounded sharpening requiring a distinct check. For the actual 24-head positive writer, in both record-X sectors, the outgoing inverse satisfies

    ||L_x(k)^-1|| < 10,  |k-pi/2|<=10^-3.

An exact Hadamard reduction and algebraic inverse certificate prove a center bound below9; a resolvent perturbation then proves the displayed full-band result. No floating-point eigenvalue or condition-number estimate is used. This replaces one local inverse constant in the existing packet proposal; it does not establish a finite-seed theorem, runtime or faithful completion herald.

ROOT proposed examining the exact center inverse as an alternative to the conservative recurrence estimate. That is design exposure, not prior validation. The original packet source remains unchanged.

## 1. Pinned physical object and outgoing sign

The writer is exactly the one in `autonomous_record_route/PROPOSAL.md`, SHA256 `93445d7d52e32859c980f0a0ebc6024238bedc7571d09e145ab1b128d8292f56`, and its check `autonomous_record_route_check/REVIEW.md`, SHA256 `c5f3e1d7cef939e1bfa95df19f970e4da454cd12a74f068147b6cd50cdf51d5a`. Both are under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/outputs/attached_record_2026_10_17/source_checks/` and were fully read and hash-verified in the immediately preceding coherent task.

The target for substitution is `common_product_stage_record_packet/PROPOSAL.md`, SHA256 `3477197cdf54d18ab538c517726d64f3dbc556f6ddb7a6d4b2608b458d34eeb9`, under the parent renewal directory. It was read completely and its hash verified here. Its local inverse B=10^31 is a proved but very conservative upper bound, not a physical parameter to be changed. The present calculation retains its matrix, signs, reference planes and record sectors.

Divide energies by j>0 and subtract the writer's actual common vacancy scalar c_R=4(sqrt(2)-1)j. Let H_x be the dimensionless internal 24-by-24 head matrix in X_R sector x=+1 or -1. Delete external lead hoppings but retain their contribution1 to each port diagonal. If E_P embeds the two port coordinates and P=E_P E_P*, then

    L_x(k)=H_x-2(1-cos k)I-zP, z=exp(ik).       (1)

The term is -zP, not its conjugate: the external lead equation gives psi_1=z psi_0+(z^-1-z)f for incoming amplitude f. Therefore the exact internal map and scattering matrix are

    V_x(k)=-2i sin(k)L_x(k)^-1 E_P,
    S_w,x(k)=E_P*V_x(k)-I.                     (2)

Neither the common scalar nor the port-origin scattering phase is altered by this analysis.

## 2. Positive-block assembly and exact two-chain reduction

Index arm0 from its terminal to attachment by0,...,10; arm1 by11,...,21; and the U,F port heads by22,23. Each arm has ten edges. Ordinary arm hopping is -1. Arm1 has hopping -sqrt(2) on its position2--3 and5--6 edges, exactly the two supplied phase cells. Their four endpoint occupations add2-sqrt(2). The attachment-to-port hopping matrix is -U with

    U=(1/sqrt(2))[[1,1],[1,-1]].

In particular its fourth entry is positive; replacing all junction signs by negative ones would be a different, rank-deficient mixer. The supplied positive vacancy at each attachment and port contributes -(sqrt(2)-1) to the relative occupation diagonal after its scalar is subtracted. At both terminals the contact contributes1+x. Each port retains the external-bond diagonal1.

Equivalently the resulting H_x has ordinary diagonals2, phase-site diagonals3, terminal diagonals2+x, and the stated hoppings. These diagonal values follow from the full positive inventory, not from an assumed ideal arm. The executable assembles the inventory first, including each bond's positive occupation terms, before subtracting the scalar and energy.

At k0=pi/2, subtracting2I and adding the outgoing port term -iP leaves terminal diagonals x, phase-site diagonals1, other arm diagonals0, and port diagonals -i. Now apply the real orthogonal transformation T=diag(I_22,U) to the two port coordinates only. Since U²=I, the attachment-port block becomes -I. The port block -iI and P are invariant. Reordering into each arm followed by its rotated port gives the exact unitary equivalence

    T*L_x(k0)T  ~  A_x direct_sum B_x.          (3)

Here A_x,B_x are symmetric tridiagonal12-by-12 matrices, numbered0,...,11:

    A_x: diagonal (x,0,0,0,0,0,0,0,0,0,0,-i),
         all eleven off-diagonals -1;
    B_x: diagonal (x,0,1,1,0,1,1,0,0,0,0,-i),
         off-diagonal -sqrt(2) at edges2 and5,
         all other off-diagonals -1.            (4)

The actual graph therefore separates after a port basis change without modifying either phase cell or terminal contact. This is a calculation on the literal writer, not an effective Hamiltonian approximation. For general k the same basis change still gives two chains; only the band-center values are needed for the following certificate.

## 3. Exact algebraic inverse certificate

All arithmetic in this section is in Q(sqrt(2),i). For a symmetric tridiagonal matrix with diagonal d_a and off-diagonal e_a, define leading and trailing continuants by

    theta_0=1, theta_1=d_0,
    theta_(a+1)=d_a theta_a-e_(a-1)^2 theta_(a-1),
    phi_12=1, phi_11=d_11,
    phi_a=d_a phi_(a+1)-e_a^2 phi_(a+2).

For a<=b its inverse entry is

    (J^-1)_(a,b)=(-1)^(a+b)(product_(r=a)^(b-1)e_r)
                         theta_a phi_(b+1)/theta_12, (5)

with empty product1 and symmetry for a>b. This formula follows from tridiagonal cofactors or direct multiplication of the recurrence solutions; its denominators are the complete determinant. The accompanying exact calculation checks every entry against (5), as well as both left and right inverse identities for the original assembled24-by-24 matrix. These checks certify the inverse of the assembled object; the positive-block and sign correspondence in section2 is a separate necessary part of the certificate.

The exact squared row norms of A_x^-1 are6 for all twelve rows, for either x. For B_x^-1 the exact squared row norms, ordered0,...,11, are:

| Sector | Squared row norms of B_x^-1 |
| --- | --- |
| x=+1 | 6, 6, 6, 21/2, 5/2, 19/2, 13/2, 13/2, 13/2, 13/2, 13/2, 13/2 |
| x=-1 | 6, 6, 6, 3/2, 19/2, 5/2, 11/2, 11/2, 11/2, 11/2, 11/2, 11/2 |

Summing gives the exact Frobenius squares

    ||A_+^-1||_F²=||A_-^-1||_F²=72,
    ||B_+^-1||_F²=159/2,
    ||B_-^-1||_F²=129/2.                        (6)

As a further exact check, the original24-by-24 determinants are -4 for x=+1 and4 for x=-1. Its complete inverse Frobenius squares are303/2 and273/2, respectively. The stronger bound uses the direct sum (3), not that complete sum:

    ||L_x(k0)^-1||
      =max{||A_x^-1||,||B_x^-1||}
      <=sqrt(159/2)<9.                         (7)

No spectral norm is identified with a Frobenius norm; (7) uses the valid upper bound and the exact maximum rule for an orthogonal direct sum. In particular there is no spurious factor from the two arms or record sectors.

## 4. Resolvent perturbation over the full selected band

For real k with |k-k0|<=h,

    L_x(k)-L_x(k0)=2 cos(k)I-(z-i)P,
    ||L_x(k)-L_x(k0)||<=2h+h=3h.               (8)

The inequalities use |cos k-cos k0|<=|k-k0| and |exp(ik)-exp(ik0)|<=|k-k0|. The internal matrix is k-independent; no hopping or terminal derivative was omitted. Multiplying (8) by the center inverse gives norm below27h. Thus whenever h<=10^-3,

    L_x(k)^-1=[I+L_x(k0)^-1(L_x(k)-L_x(k0))]^-1
                                                      L_x(k0)^-1,
    ||L_x(k)^-1|| < 9/(1-27h)
                    <=9000/973<10.              (9)

This is a genuine positive margin for both sectors across the whole interval. It does not follow merely from scattering unitarity or an unsupported assertion that there are no poles. There is no parameter sweep or interpolation between numerical samples. Equation (9) proves a uniform B=10 admissible wherever the packet source used its local B=10^31.

The source's domain h<=10^-3 is retained even though the Neumann argument alone allows a larger interval. No larger-band writer scattering-error contract is imported from that observation. Spectrum outside the stated interval and overlaps of an actual finite seed with localized states remain untouched.

## 5. Explicit derivative replacements

Write G=L_x^-1. Since ||L_x'||<=3 and ||L_x''||<=3,

    G'=-G L_x' G,
    G''=2G L_x' G L_x' G-G L_x''G.

Using B=10 gives uniformly on the full selected band

    ||G||<=10,
    ||G'||<=300,
    ||G''||<=18300.                            (10)

Differentiating the exact prefactor -2i sin(k) in (2), and using the bounds2 for it and its first two derivatives, gives

    ||V_x||<=20,
    ||V_x'||<=2*10+2*300=620,
    ||V_x''||<=2*10+4*300+2*18300=37820,
    ||S_w,x'||<=620,
    ||S_w,x''||<=37820.                        (11)

The exact scattering norm remains1 by the established physical scattering equation; (11) concerns derivative bounds, not a replacement of unitarity. All quantities in (10),(11) are derivatives with respect to the dimensionless momentum k. No power of j is missing: (1) already uses dimensionless energy E/j, while physical evolution still uses E and the original scalar.

A direct substitution into the older packet formulas can conservatively use B=10, a0=20, a1=w1=800 and w2=56000, since those are exactly its formulas2B,8B²,56B³. Alternatively the freshly derived smaller values a0=20,a1=w1=620,w2=37820 are valid inputs. Any author updating downstream feedback constants must state which set is used and recompute the corresponding explicit formulas; this note does not edit or certify that substitution automatically.

Both physical writer copies coupled to one record are handled by direct sums over path in each conserved X_R sector, then orthogonal sector recombination. Consequently the same bounds apply to their complete48-head internal map without a factor2 or a duplicated record. Passive references tensor identity and do not change the constants. The signed junction, phase cells, coefficient values, contact blocks, source support and common stationary phase remain exactly unchanged.

## 6. Reproduction, limitations and distinct-check gate

The accompanying files in this directory are:

* `certify_inverse.py`: exact SymPy assembly of the positive-block relative matrix, Hadamard decoupling, inverse identities, continuant entry checks and rational norm sums.
* `certificate.txt`: complete stdout from the successful run, including both record sectors, every rational row-norm certificate and the full determinants.

Reproduce with Python3 and SymPy (the recorded run used1.14.0):

    python3 certify_inverse.py

The executable uses no Float, numerical eigenvalue routine, numerical integration or fit. It certifies fixed finite exact matrices, not a sampled band; the continuum statement comes from the analytic norm perturbation (8)-(9). The row-norm table and recurrences provide a compact exact route for a checker who does not rely on the stored output. A sign or diagonal mismatch in the physical assembly would invalidate the result even if an inverse routine could invert that wrong matrix; hence section2 and the original writer definitions are load-bearing checks.

The earlier B=10^31 estimate remains a valid loose bound at its stated scope. This calculation identifies its large size as proof pessimism in the generic recurrence/observability estimate, not evidence of an enormous actual writer resonance on this band. The bound10 is sufficient, not asserted optimal, and does not identify the exact smallest singular value.

No finite emitter, source launch, complete-device early match, output cut, duration, accuracy/resource exponent or all-time Record implication is proved here. The complete staged network still has its feedback denominator, cable derivatives and internal-map bookkeeping, which must use these local constants through their own proved interfaces. Point-spectrum weight of a supplied seed is not paid by this local inverse calculation.

This is newly authored work after ROOT's suggested method and full source exposure. I previously inspected the writer and reviewed the staged composition, and authored the earlier four-port core. Those are disclosed exposure; neither they nor the successful exact program constitute an independent check of this new sharpening. A distinct reviewer should verify the positive-block matrix, junction signs, phase-cell positions, outgoing sign, port rotation, exact row sums/continuants, resolvent factorization and all derivative product rules before integration. No retained or formal audit status is assigned.

Only this proposal and its exact certificate program/output were created in the assigned directory. No source outside this directory, W/Git/checkpoint/axiom/editable prompt or model was changed. No publication, delegation, parameter sweep, floating-point certificate or new physical assumption was used.
