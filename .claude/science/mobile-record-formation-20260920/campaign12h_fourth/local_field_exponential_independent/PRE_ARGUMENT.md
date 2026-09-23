# Blind PRE: one-link exponential electric moment

Independent reconstruction, 2026-09-23. This file was written without reading
`local_field_exponential_author`, `local_field_moment_author`, or any root
field-exponential candidate. The statement is conditional on the supplied
compensated finite-graph rotor generator and actual resolved or stipulated
coherent birth channels. It is neither a microscopic all-volume estimate nor
a physical selection of that generator.

## Exact claim and hypothesis

Let `G=(A union B,E)` be any finite **simple** bipartite graph with maximum
degree at most `z`, where `z>=1` is fixed independently of the volume. Work on
the physical `P` rotor space with integer electric fields and Gauss law. Let

    h_G=K D_G-2 delta sum_{a<c: N(a) cap N(c) != empty} S_ac^* S_ac,
    S_ac=F_c F_a P,
    L_{a,b,sigma}=sqrt(kappa) P j_{a,b,sigma} F_a P

with `K,delta,kappa>=0`, or replace the two signs at each `(a,b)` by their
stipulated coherent sum. Here each elementary outward hop and birth is a
normalized partial shift of its incident link; the outward destination must
be different from the newborn B site. The birth law is the supplied one, with
no additional channels. For any chosen edge `e`, `lambda>0`, and positive
trace-one initial density with

    m_{e,lambda}(0)=Tr exp(lambda |E_e|) rho_0 < infinity,

the finite-graph semigroup obeys, for all `t>=0`,

    m_{e,lambda}(t) <= m_{e,lambda}(0) exp(C_{lambda,z} t).       (1)

A valid common constant for both instruments is

    C_{lambda,z}
      = (exp(lambda)-1)
          [4 |delta| z^5 (z-1) + 8 kappa z (z-1)^2].            (2)

For the resolved instrument, replace `8 kappa` by `4 kappa`. The constant
does not depend on graph size, rotor cutoff, `K`, or any moment of another
link. It is intentionally coarse. If only one fixed graph is meant, take its
actual maximum degree for `z`. A family has a uniform conclusion only when
its initial chosen-link moments are uniformly bounded.

## Path support and local count

An `S_ac` path chooses at most one outward edge at `a` and one at `c`.
Because `a != c` and the graph is simple, a given link `e=(a,b)` occurs at
most once in a path. There are at most `deg(a)deg(c)<=z^2` such normalized
partial-shift paths. A resolved `L_{a,b,sigma}` has at most `deg(a)-1<=z-1`
paths: the old A record goes to `c != b`, then the new pair is born at
`(a,b)`. Its coherent sign sum has at most `2(z-1)` paths. A given link occurs
in a jump path either as the old-hop edge or as the newborn edge, never both.
Thus **each elementary path changes one chosen link by 0 or +/-1**.

The complete matrix elements also have single-link shift support. In a
nonzero `S_ac^*S_ac` matrix element, two paths meet in one intermediate
physical output. If both use `e`, then the final charge at `b` fixes the
old charge at `a`, so the two shifts of `e` cancel. If one uses it, the net
shift is +/-1; if neither uses it, zero. For a fixed resolved birth channel,
if both paths use `e` as newborn edge its sign is fixed. If both use it as
old-hop edge, the common final charge at its B endpoint fixes the old A
charge. The same conclusion holds for a coherent sign sum because different
newborn signs leave different final charges at `a`; the cross-sign output
inner product is zero. Therefore nonzero matrix elements of `L^*L` and
`L^* f(E_e) L` also shift `e` by at most one. The proof below only needs the
elementary-path statement, so it does not rely on a matrix truncation.

For `e=(a,b)`, only pair anchors containing `a` can act on `E_e`. The number
of other A anchors sharing *some* B neighbor with `a` is bounded by

    sum_{d in N(a)}(deg(d)-1) <= z(z-1).                        (3)

Every other pair and every birth anchored away from `a` commute with a
function of `E_e`. One cannot count only A sites adjacent to `b`: a pair
sharing another B neighbor can still shift `e` through different **input** B
occupations. The exact Gauss-compatible counterexample below establishes
this point. There are at most `2z` resolved or `z` coherent birth channels
anchored at `a`.

## Weighted form estimate

For integer `N>=0` set

    W_N=exp(lambda min(|E_e|,N)),  V_N=W_N^{1/2},
    r=exp(lambda/2)-1.

If `T` is one elementary partial-shift path, its action on `E_e` is 0 or
one unit. Since `n -> min(|n|,N)` is 1-Lipschitz,

    ||V_N^{+/-1} T V_N^{-/+1}|| <= 1+r,
    ||V_N^{+/-1} T V_N^{-/+1}-T|| <= r.                  (4)

The estimates hold uniformly in `N`; a path not using `e` commutes exactly.
For a sum `X` of at most `p` paths, replace 1 by `p` on the right. If
`B=X^*X`, factoring its conjugate into the two conjugated factors gives

    ||V_N^{+/-1} B V_N^{-/+1}-B||
       <= (2r+r^2)p^2 = (exp(lambda)-1)p^2.              (5)

Use `p=z^2` for one pair. Since `W_N=V_N^2`, the relative Hamiltonian
commutator for this pair has norm at most

    ||V_N^{-1} i[-2delta B,W_N] V_N^{-1}||
       <= 4|delta| (exp(lambda)-1) z^4.                 (6)

The `K D_G` term commutes with `W_N` exactly. Summing (6) over (3) gives
the first term of (2).

For one jump `L` whose sum of path norms is at most `ell`, the same
factorization and (5) give

    || V_N^{-1} [L^* W_N L-{L^*L,W_N}/2] V_N^{-1} ||
       <= 2 (exp(lambda)-1) ell^2.                     (7)

Indeed `V_N^{-1} L^* W_N L V_N^{-1}` is
`(V_N L V_N^{-1})^*(V_N L V_N^{-1})`; its difference from `L^*L` is at most
`(exp(lambda)-1)ell^2`. Each of the two weighted anticommutator factors is
bounded by the same difference. A resolved channel has
`ell=sqrt(kappa)(z-1)`, while a coherent one has
`ell=2sqrt(kappa)(z-1)`. Summing over the `2z` or `z` local channels proves
the second term of (2). All these relative forms are self-adjoint; their
operator-norm bounds imply the required upper quadratic-form bound.

## Unbounded domain and volume passage

On each finite graph, `D_G` is a self-adjoint diagonal multiplication
operator with finite electric-support core. The rest of `h_G` and every jump
are bounded. `W_N` is bounded, diagonal, and strongly commutes with `D_G`.
In the interaction picture of `K D_G`, the bounded Hamiltonian and
dissipative coefficients give a trace-norm differentiable mild solution for
any initial trace-class density. `W_N` stays fixed in this picture, and its
relative form estimate (6)-(7) is unchanged because the free diagonal
unitary commutes with `V_N`. No assumption that `rho_0` lies in the full
generator domain, or that it has finite `D_G` expectation, is needed.

Writing `m_N(t)=Tr W_N rho_t`, positivity and (6)-(7) give
`m_N'(t)<=C_{lambda,z} m_N(t)` almost everywhere. Gronwall gives (1) with
`W_N`; monotone convergence as `N` grows gives (1) for the unbounded
exponential weight. This is a real unbounded-domain passage, not a formal
application of the generator to `exp(lambda |E_e|)`.

If the checked compensated volume construction supplies a norm limit for
bounded local observables, apply it first to each `W_N`. Compatible initial
finite-volume states whose one-link exponential moments have common bound
`m_0` then yield `omega_t(W_N)<=m_0 exp(C_{lambda,z}t)` for every `N`;
monotone convergence in the locally normal limit gives the same bound for
the chosen link. This does not exchange a microscopic approximation with
volume, infer a global infinite-volume density, or prove higher electric
moments from a smaller initial exponential parameter.

## Exact support counterexample and finite controls

The independent six-vertex tree has `A={a,c}`, `B={b,d,x,y}`, and oriented
edges `a-b,a-d,c-d,c-x,c-y`. The pair `(a,c)` shares `d`, while `c` is not
adjacent to the monitored link's B endpoint `b`. Its two physical `P` inputs
are:

    input I:  q=(a:+,c:-,b:0,d:+,x:0,y:+), E=(0,0,-1,0,-1)
    input II: q=(a:+,c:-,b:+,d:0,x:0,y:+), E=(-1,1,-1,0,-1).

Both satisfy `div E=q-1_A`. From input I, hop `a->b` then `c->x`.
From input II, hop `a->d` then `c->x`. They reach the **same** two-vacancy
charge/electric word, with fields `(-1,0,-1,1,-1)`. All unsigned amplitudes
are one, so `S_ac^*S_ac` has a nonzero off-diagonal matrix element between
these inputs while `E_(a,b)` differs by one. Hence an attempted count using
only `deg(b)-1` pairs is not valid on all graphs.

The separate script `field_exponential_check.py` verifies the tree Gauss
laws and output identity. It also scans the independently built complete
52-state physical matrix for a seven-site path: all 86 nonzero fourth-order
Hamiltonian entries and all resolved/coherent jump entries have at most
unit shift per link. Its matrix entry `(3,34)=-2` changes leaf link `(1,0)`
although the other anchor `3` is not adjacent to B site `0`. A finite
weighted-generator check at `lambda=0.7`, `delta=kappa=1`, `z=2` found
maximum relative-form eigenvalue `4.5524156969`, below the analytic common
bound `145.9803898757`. This finite tree corroborates signs and support;
it does not prove the all-graph theorem. Full results are in
`FIELD_EXPONENTIAL_PRE_RESULTS.json`.

With unbounded vertex degree, an all-A-plus, B-empty, zero-field star of
degree `z` has chosen-link initial derivative
`4 kappa (z-1)(exp(lambda)-1)` for either instrument. Thus no **degree-free
local differential coefficient of the form used here** follows from the
stated path counting. This derivative alone does not disprove every possible
degree-free finite-time bound. The graph-uniform theorem is stated for a
fixed maximum-degree bound.

## Source identities and limits

- Repository AGENTS: `9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6`.
- Science workflow: `d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4`.
- Supplied compensation note: `42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4`.
- Checked compensated volume candidate: `a0c1389773766c47b41300329cf6b945a8f5e584c2c46853fe34064a9c331bd6`.
- Independent finite-path physical matrix: `cea5eadb26ba699d2230befbcbb805ec6df29db52ca1b78c4da19d720ff85553`.
- Campaign checkpoint read: `88470011c7f03279803f0d84605a3dd04fefb17ddb81f03cbfc2ad401f20132c`.

The proof establishes a conditional bound for the supplied rotor target.
It does not establish native-theory selection of compensation or birth,
uniform microscopic/spin error in volume, electric exponential-moment
creation from an initial density lacking that moment, or a formal audit
verdict. No author field-exponential candidate was read before this PRE.
