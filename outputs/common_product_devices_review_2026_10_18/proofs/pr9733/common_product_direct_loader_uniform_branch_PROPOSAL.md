# Narrow-source L1 bound and a conditional uniform record-branch interface

ROOT proposal requiring a distinct check. The scalar bound below is exact under its stated source premises. The branch transfer is an abstract conditional interface: no finite loader theorem or numerical error allocation is asserted here. It must be instantiated only after the new finite construction supplies its normalization, early comparison and whole-interval cut bounds.

## Exact scalar premises and bound

Use the checked source amplitude

F(k)=-i sqrt(2/pi) rho sin(k) exp(ik)/[(2-rho²)cos(k)-i rho² sin(k)].

Let 0<rho²<=h<=10^-3 and rho<=1. Let 0<=chi<=1 be supported in |k-pi/2|<=3h/4. Suppose p=||chi F||²>=1/2 and set g=chi F/sqrt(p). These are the exact launcher/cutoff premises in sourcefb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4 and source550946fdebc4e68522c997ed914e23a8baf40cb660dfc22e4f09e00add1216a3, with checks51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1 and6a4866e76cc5c6c760284c9a3f6c07c71410f701d727e8765edc8f6a57d328a4. Their complete arguments were previously read at these unchanged identities; the new claim here uses only the displayed F, support and p.

On this support, q=k-pi/2 obeys |cos k|=|sin q|>=2|q|/pi and sin k>=1/2. Also 2-rho²>=1. Hence

|g(k)| <= (2/sqrt(pi)) rho / sqrt(4q²/pi²+rho^4/4).

Integrating this even bound over |q|<=3h/4 gives

||g||_1 <= 2sqrt(pi) rho asinh(3h/(pi rho²))
        <= 4rho log(1+2h/rho²) =: L(rho,h).                 (1)

For the second inequality, asinh(x)=log(x+sqrt(1+x²))<=log(1+2x), 2sqrt(pi)<4 and6/pi<2. No derivative or numerical approximation is used. The normalization p matters; this is not an unnormalized-source bound silently reused for g.

For an illustrative policy h=epsilon/10^6, rho=epsilon sqrt(h)/10^4, 0<epsilon<=1, (1) gives

||g||_1 <=4*10^-7 epsilon^(3/2) log(1+2*10^8/epsilon²)
        <=8*10^-6 epsilon.                                (2)

For the last bound put x=sqrt(epsilon)<=1 and A=2*10^8. The function x log(1+A/x^4) is increasing on (0,1]: its derivative is log(1+A/x^4)-4A/(x^4+A)>log(1+A)-4>0. Its maximum is log(1+A)<20. This policy is merely an example and is not asserted to be the final loader's selected policy.

## Conditional complete-branch transfer

Consider the checked stationary direct loader89489c13a6450f142c8ac2212ee680bc7272addcff30c53fcb01e52dff4ee7a9 and review9818c72551eec2d2be17224dde6e07335f1ff7157b94a91c4a372aff3873343d. Its exact common scalar is c; the full forward comparator is z^D U_f with U_f=X_R C_P SWAP and auxiliary identity. Inputs have R=0. References are passive. No active old Hamiltonian is admitted.

Assume a separately proved exact normalized infinite one-head packet Psi(t) on this graph, synthesized with normalized g and an input isometry I_in on the selected incoming rays. Its external integrand is [exp(-ink)I_in+exp(ink)S I_in] exp(iell k-itE)g. Its complete internal integrand is T(k) exp(iell k-itE)g, with ||T(k)||<=T0 on the support. Suppose ||S-S0||<=d_s there, including all exterior channels. These are operator bounds on all allowed data/passive-reference input vectors.

Let J embed the actual finite device in the infinite comparison space with all added head coordinates vacant. Let Pi_fin restrict the one-head sector to its physical head sites, including emitters, and keep every physical data/reference register. Let P1 project R onto1; it commutes with Pi_fin. Suppose a new finite theorem establishes, for every t in [t0,t_plus],

||J psi_fin(t)-exp(-ict)Psi(t)|| <= E0+Ecut(t).                (3)

Define V(t) as the ideal outgoing Fourier field with S0 I_in=z^D U_f I_in, restricted to the actual output-ray sites, all other physical heads vacant, and common phase exp(-ict). DO NOT divide by its norm. In particular ||V(t)||<=1 by full-line Parseval, with the appropriate exact input/reference isometry. It can be tiny or zero at early times.

The incoming part of Psi(t) has R=0 and is annihilated by P1. The ideal outgoing part has R=1 only on the right/output rays, since U_f flips R and has no reflected block. The external error (S-S0) gives vector norm at most d_s after synthesis by full-line Parseval followed by restriction to n>=1 and physical sites. The internal part contributes at most T0||g||_1/sqrt(2pi), uniformly in time, by the triangle inequality for its finite-vector integral. Thus, on the physical Hilbert space,

||P1 psi_fin(t)-V(t)|| <= E0+Ecut(t)+d_s+T0 L(rho,h)/sqrt(2pi),  (4)

for t in [t0,t_plus]. Every physical output is retained; no unobserved internal register is traced out. The estimate bounds an ABSOLUTE UNNORMALIZED BRANCH-COMPARISON error. It does not bound ||P1 psi_fin(t)|| by that small number, since the correct R=1 branch can have order-one norm. Nor does it imply an error bound after conditioning on a rare event.

There is deliberately no conclusion for t<t0 from (3). Extending to [0,t_plus] requires BOTH a direct precontact bound on ||P1 psi_fin(t)|| and a bound on ||V(t)|| over [0,t0]. The latter is a negative-position/early outgoing tail estimate for the ideal full-line field. An actual early flag bound alone is insufficient, because comparison against a nonzero V still costs its norm. Those two extra terms must be included explicitly in any application.

For normalized input vectors, if the right side of (4) is Ebr, the corresponding unhalved trace norm of the two subnormalized pure output operators is at most2Ebr, since both vector norms are at most one. Uniformity under passive reference gives the corresponding channel-norm statement only on the specified input contract; no normalized-success or arbitrary unknown-initial-R statement follows. Mixed fixed old states can be treated by a passive purification when the separate finite theorem provides that same uniform contract.

No permanent halt, irreversible record, capture/reset, native Hamiltonian or old-processor identification is proved. The estimate is an interface awaiting an actual finite theorem. Same-model and source-exposed ancestry is explicit: ROOT proposed the loader and read its stationary support before writing this possible strengthening. No executable, simulation, source modification, retained audit, editable prompt or model change occurs here.
