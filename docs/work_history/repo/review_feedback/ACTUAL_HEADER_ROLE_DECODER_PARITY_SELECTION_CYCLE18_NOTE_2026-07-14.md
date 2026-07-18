# Actual-Header Role Decoder And Parity Selection — Cycle 18

**Date:** 2026-07-14

**Type:** exact actual-motif reconstruction, strongest-positive decoder theorem,
complete center--fragment instrument, paired same-boundary law probe,
primary-source boundary, and N1--N8 scoped-negative gate

**Authority:** none. This review-feedback note is not a retained theorem,
audit verdict, axiom proposal, primitive, law registration, context selection,
or owner ruling. It changes no axiom, primitive, registry, audit, queue, policy,
or retained surface. It creates only this authority-free note and its exact
companion runner.

**Companion runner:**
`scripts/actual_header_role_decoder_parity_selection_cycle18_2026_07_14.py`

## Result Up Front

The actual Cycle-13/14 header closes the spatial half of the decoder seam. A
single additional operational relation closes the internal `X/Y` half
conditionally. The present propagation grammar does not yet state that
relation independently, so the closure is a strong exact-law target rather
than a foundation theorem.

Three results matter.

### 1. Actual-header geometry theorem

The six permanent records are exactly

```text
site:     t+e   t+2e  t+3e  t+u   t+2u  t+d+e+u
content:   H1     H0     H1    H1     H0       H1
```

with `u=d cross e`. Exhaustive decoding over every trigger and all 24 ordered
cardinal proper frames recovers one and only one `(t,d,e)`. The three-record
line identifies `e`; the two-record line and cross product identify `u`; the
data line identifies `d`. Swapping `e` and `u` does not reproduce the same
header. This is the **actual-header geometry theorem**.

Cycle 14 adds a preparation certificate at `q=t-e`. That already singles out
the negative-`e` rail. One new relay position and one apparatus position fit
the existing geometry exactly:

```text
certificate:        q   = t-e
role relay:          r   = t+d-e
apparatus fragment:  f   = t+2d-e = center-e
center:              b   = t+2d.
```

Every displayed link `q-r`, `r-f`, and `f-b` is nearest-neighbor. The relay
and fragment collide with none of the actual header, data, certificate, or
three positive-side builder layers. Twelve exact straight cells remain
collision-free, and all sites co-transform under every proper cubic rotation.

So the existing typed geometry can carry a local apparatus arm without an
absolute direction and without a second spatial program.

### 2. Paired-role result

The same records still admit two proper spatial-to-internal role decoders.
Writing internal Bloch directions as `(X_f,Y_f,Z_f)`:

```text
remaining-leg decoder J_X:
    d -> Z_f,   e -> X_f,   u -> Y_f;

header-leg decoder J_Y:
    d -> Z_f,   e -> Y_f,   u -> -X_f.
```

Both maps are orthogonal with determinant `+1`. Both preserve
`d cross e=u`; both map propagation to the `Z_f` selected by `CZ-CZ`; both
transport unchanged under the straight self-writing grammar; and both are
proper-cubic equivariant when their complete internal action is co-transported.
They differ by a proper quarter-turn about `Z_f`.

The actual `H1/H0=Y_f+/-` records occur on both the long `e` line and the
short `u` line. The pattern distinguishes the two *spatial* roles, but it
contains no clause saying whether the `Y_f` content names the long or short
role. Hence the header alone does not choose `J_X` over `J_Y`.

Bell-fusion capability and nondemolition also tie them. The runner constructs
two complete local center--fragment interactions on the same site `f`, with
the same reset blank `|Z_f+>`, same target flip, same target `Z_f` decoder,
same header, same trigger boundary, and same nearest-neighbor support. One
copies the center `X_f` PVM; the other copies `Y_f`. Both have a unique
two-dimensional pointer commutant, exactly dephase their pointer, make
orthogonal fragment states, preserve pointer eigenstates, and leave a
maximally entangled endpoint pair.

### 3. Parity-certificate selection theorem

The three-site cluster has the exact stabilizer

```text
Z_a X_b Z_c |Cluster> = |Cluster>.
```

For an arbitrary center qubit involution

```text
A = n_x X_f + n_y Y_f + n_z Z_f,
```

the center-sign/endpoint-parity correlator is

```text
< Z_a A_b Z_c > = n_x.
```

A deterministic binary certificate requires absolute correlation `1`. Unit
norm then forces `n_y=n_z=0`, hence

```text
A = +X_f or -X_f.
```

Those two signs are the same unordered PVM; they only exchange its outcome
names. Therefore:

> If the center record is required to be a deterministic readable certificate
> of the two endpoint `Z_f` records' parity, the actual cluster and endpoint
> decoder uniquely select the center `X_f` PVM up to outcome swap.

This is the **parity-certificate selection theorem**. It is stronger than Bell
success: every equatorial center basis, including `Y_f`, leaves maximally
entangled endpoints, but only `X_f` makes the later endpoint `Z_f` parity a
deterministic function of the center sign.

The exact future transcripts expose the difference:

```text
remaining-leg X law:
    4 complete center/witness/endpoint transcripts, each weight 1/4;
    center sign fixes endpoint XOR exactly.

header-leg Y law:
    8 complete transcripts, each weight 1/8;
    center sign does not fix endpoint XOR.
```

### What is closed and what is not

If “center certificate” is given the operational meaning

```text
s_center = (-1)^(z_left xor z_right),
```

then the header geometry, cluster interaction, endpoint `Z_f` records, and
decoder consistency select the remaining apparatus leg and `X_f` context.
No absolute `X` basis and no context axiom are needed.

But the current propagation automaton does not independently impose that
meaning. Its readiness predicate merely asks whether the center content name
starts with the literal string `X`; Cycle 13 lists the projective `X`
instrument as explicit law field `D2`. Counting that hard-coded name as a
derivation would be circular. The XOR relation currently appears as a theorem
*after* the supplied `X` read, while downstream readiness uses only the
presence of a center-stage record and a forward endpoint trigger.

Accordingly the **smallest exact-law field** that separates the two role laws
without a privileged matrix label is the operational parity-certificate
contract:

```text
PC: the signed center record equals the product of the two endpoint Z records.
```

Equivalently in role language: `CENTER_POINTER = COMPLEMENT(H,Z)`, not
`CENTER_POINTER = H`. `PC` is preferable because it is a readable transcript
relation and can be falsified. It may ultimately derive from the one fixed
admissibility law. This cycle does not derive that law or promote `PC` to an
axiom.

Orientation reversal only swaps outcome labels: `X_f=-iY_fZ_f` becomes
`-X_f`, leaving the unordered binary PVM intact. Chirality does not turn the
`X_f` law into the `Y_f` law.

No axiom text is proposed. This cycle does not establish that a new axiom is
required.

## Exact Question And Answer Matrix

| question | strongest exact answer | remaining condition |
|---|---|---|
| does the six-record pattern uniquely recover spatial roles? | yes; it uniquely decodes `t,d,e,u=d cross e` | none inside the finite motif |
| does swapping `e` and `u` preserve the header? | no | no spatial-role ambiguity remains |
| is there an unused NN apparatus site selected by existing geometry? | yes; the certificate rail gives `f=center-e` through one NN relay | the relay/write clause is an exact-law extension |
| do header `Y` and trigger/endpoint `Z` construct `X`? | yes, `X=-iYZ` after cross-site comparison is supplied | physical connection/transport remains law content |
| does the actual header bind `Y` to `e` or `u`? | no; `H` contents occupy both rays and two proper role maps survive | parity/apparatus decoder |
| does proper-cubic covariance choose a role map? | no; both maps co-transform exactly | a covariant class is not one member |
| does positive chirality choose `X` over `Y`? | no; both maps are proper | `X/Y` is a quarter-turn about `Z` |
| does Bell fusion choose `X`? | no; every equatorial PVM tested gives concurrence one | phase/parity semantics |
| does nondemolition choose `X`? | no; both exact controlled copies are nondemolition | apparatus relation |
| does deterministic endpoint-parity certification choose `X`? | yes, uniquely up to outcome swap | status/derivation of the certificate contract |
| can the fragment blank be law-generated? | yes conditionally; an onsite reset inside the event maps every input to `|Z+>` | reset target and irreversibility are law content |
| can role readiness travel by NN support? | yes; `C(q)` can append a same-content relay at `r=q+d`, and `f` neighbors both relay and center | why this relay clause is Nature's law |
| do the paired laws have different readable futures? | yes; four parity-fixed versus eight parity-unfixed transcripts | statistics/actuality interpretation still separate |
| does this make an event occur? | no | occurrence/fairness |
| does it make the imprint irreversible? | no; the copy unitary squares to identity | append/no-return scope |
| does it choose one actual transcript? | no | actuality and probability |

## Framework And Predecessor Boundary

The current foundation supplies:

- the cubic lattice, nearest-neighbor adjacency, standard translations, and
  proper cubic rotations;
- one unprivileged `M_2(C)` possibility domain per site;
- one fixed nearest-neighbor admissibility rule whose detailed content is not
  stated in the axiom memo; and
- formed permanent records with one locked content and content-only additive
  scalar readout.

It explicitly withholds context selection, measurement basis, formation rule,
update dynamics, probability, and physical persistence dynamics. The approved
primitive registry adds only units conversion, kinetic-form isotropy, and
pointwise evaluation at a supplied realized state. None supplies this header,
connection, role map, apparatus, blank reset, parity contract, event, or actual
branch.

Cycle 13 supplies the exact six-record header as boundary/program data and
lists:

```text
Q2  shared relational Pauli frame       explicit import
D1  CZ_ab CZ_bc                         explicit law value
D2  projective center X instrument      explicit law value
D3  projective endpoint Z instruments  explicit law value.
```

Cycle 14 makes future headers self-writing and data preparation law-generated.
Its certificate is at `q=t-e`, and three builder layers copy the header along
`d`. It retains the same `CZ-X-Z` event package and frame/connection import.

Cycle 15 derives binary Lüders form from completeness, attainability, and exact
repeatability once the context/event exists. Cycle 16 derives a pointer PVM
from a supplied exact interaction with a simple system-side commutant. Cycle
17 uses `CZ-CZ`'s selected `Z_f` and the transported header `Y_f` to construct
`X_f=-iY_fZ_f`, leaving only the actual header-to-leg/apparatus decoder seam.

This cycle attacks that exact seam. It does not count any predecessor's
explicit `X` label as new evidence for `X`.

## 1. The Actual Six-Record Decoder

Let

```text
g=(t,d,e),
u=d cross e,
a=t+d,
b=t+2d,
c=t+3d.
```

The exact header offsets are

```text
e, 2e, 3e, u, 2u, d+e+u,
```

with contents

```text
H1,H0,H1,H1,H0,H1.
```

The companion runner repeats the actual Cycle-13/14 decoder rather than
replacing it with an abstract triad. It searches every candidate trigger and
all ordered perpendicular cardinal `(d,e)` pairs. The base motif and every
translated/proper-rotated motif decode exactly once.

Why uniqueness holds is visible without coordinates:

- the only three-step collinear header ray is the `e` ray;
- the two-step ray perpendicular to it and `d` is `u`;
- the displaced corner record at `d+e+u` fixes the forward side; and
- `u=d cross e` fixes the proper hand.

The header therefore supplies a genuine ordered spatial program. This is more
than an unoriented triangle and more than the abstract full-frame resource
tested in Cycle 17.

### What the typed content supplies

In the current exact representation,

```text
H1/H0 = Y_f+/-;
trigger and endpoint records = Z_f+/-.
```

The cluster interaction independently selects the onsite `Z_f` commutant.
Conditional on the cross-site frame comparison already named as `Q2`, the two
noncommuting record rays construct `X_f=-iY_fZ_f`.

But every header site, whether on the `e` ray, the `u` ray, or the corner,
uses the same `H/Y_f` content family. The geometry distinguishes long and
short rays; the internal content does not say which ray is “the `Y_f` leg.”
That remaining association is precisely a role decoder.

## 2. A Nearest-Neighbor Certificate/Apparatus Rail

Cycle 14 places its preparation certificate at

```text
q=t-e.
```

The center is `b=t+2d`. The negative-`e` corridor between them contains

```text
r=q+d=t+d-e,
f=q+2d=t+2d-e=b-e.
```

This gives the exact local chain

```text
C certificate at q
  --NN--> same-content role relay at r
  --NN--> open/resettable fragment at f
  --NN--> center b.
```

The fragment is not on the positive-side header-builder corridor. In
particular, `b+e` and `b+u` would collide with Cycle 14's second builder layer,
whereas `b-e` does not. The certificate position therefore gives a materially
better apparatus arm than an arbitrary transverse neighbor.

For a straight chain, each cell contributes

```text
q_n=t_n-e,
r_n=t_n+d-e,
f_n=t_n+2d-e,
q_(n+1)=t_n+3d-e.
```

These sites tile the negative-`e` rail without collision. A same-content `C`
relay at `r_n` carries only stage/role readiness; it need not introduce a new
one-site possibility type. The local event at `f_n` sees the relay and center
as its two nearest neighbors.

This is an exact constructive role-transport path. It is not a derivation that
the current admissibility rule must append the relay. The relay clause is a
candidate exact-law field and consumes one permanent site per cell.

## 3. The Two Proper Role Decoders

Use ordered spatial basis `(d,e,u)` and internal basis `(X_f,Y_f,Z_f)`. The
two exact maps are

```text
J_X(d)=Z_f,  J_X(e)=X_f,  J_X(u)=Y_f;

J_Y(d)=Z_f,  J_Y(e)=Y_f,  J_Y(u)=-X_f.
```

Both preserve orientation because

```text
Z_f cross X_f = Y_f,
Z_f cross Y_f = -X_f.
```

They are related by a positive quarter-turn about `Z_f`. For every proper
cubic spatial rotation `R`, define the transported internal action

```text
rho_J(R)=J R J^{-1}.
```

Then

```text
J R = rho_J(R) J
```

for both maps. Covariance therefore transports either decoder; it does not
select one.

The physical interpretation is sharp:

- `J_X` associates the `Y_f` header ray with the short/normal role `u`, so the
  certificate-selected `e` apparatus arm reads the remaining axis `X_f`;
- `J_Y` associates the same `Y_f` header ray with the long/transverse role
  `e`, so that same apparatus arm reads the header axis `Y_f`.

Both use the same record dictionary and boundary. Straight self-writing copies
the same `(d,e,u)` and therefore transports either fixed role assignment
unchanged.

This paired map is the exact clause-delete control for the positive decoder
theorem below.

## 4. Complete Center--Fragment Interaction

The candidate extension uses the actual sites and integrates blank preparation
so no external fragment state is assumed.

### Phase P: existing data preparation

As in Cycle 14, reset `a,b,c` to `|+ + +>` and append `C` at `q=t-e`.

### Phase R: one-edge role relay

If `C` is at `q` and `r=q+d` is open, append the same certificate content `C`
at `r`. This is one nearest-neighbor write. Its geometric position, not a new
content alphabet, says that the next negative-`e` site is the center fragment.

### Phase E: integrated blank reset, cluster, and read

When `r` carries the relay and `f=r+d` is open:

1. reset the fragment onsite to `|Z_f+>`;
2. apply `CZ_ab CZ_bc` on the two existing NN data edges;
3. apply on the NN center--fragment edge

   ```text
   U_A=P_A+ tensor I + P_A- tensor X_f(fragment),
   ```

   where `A=X_f` for `J_X` or `A=Y_f` for `J_Y`;
4. read the fragment in `Z_f`; and
5. append the matching center `A+/-` record and fragment `Z_f+/-` witness
   record.

The reset may be composed into the instrument. For every incoming fragment
density operator it supplies the same blank, so there is no hidden open-state
dependence. This pays the same irreversibility price as Cycle 14's data reset.

For either `A`, the exact system-side commutant of `U_A` is

```text
span{I,A}.
```

The target conditional states are `|Z_f+>` and `|Z_f->`; the center pointer
states are unchanged. The target `Z_f` result therefore implements the binary
repeatable `A` instrument. Cycle 15 then supplies Lüders form conditionally.

The construction is a complete center--fragment instrument, not a derivation
of occurrence or actuality. Appending both records is a candidate branch law.
Before a sampled/global completion, the two branches remain allowed coherent
alternatives.

### Phase endpoints and growth

After the center certificate, read `a,c` in `Z_f` as before. The forward
endpoint record at `c` enables header growth. The new fragment and relay lie
on the negative-`e` rail and do not intersect any of the three header-builder
layers.

The existing hard-coded readiness test checks an `X` prefix. For scientific
comparison it must be factored into:

```text
is a valid center-certificate content for this role decoder?
```

Both paired laws then have the same stage grammar. The hard-coded X prefix is
not a derivation; it is the predecessor's explicit `D2` value rendered as a
string predicate.

## 5. Bell Fusion Versus Parity Certification

Bell entanglement is too weak a selector. For every equatorial axis

```text
A(phi)=cos(phi)X_f+sin(phi)Y_f,
```

either center outcome leaves the endpoints in a maximally entangled pure
state. `phi=0` and `phi=pi/2` therefore tie `X_f` and `Y_f` under concurrence.
Both complete apparatus interactions are also nondemolition, so adding
repeatability does not break the tie.

The endpoint record decoder supplies a stronger operational question. Endpoint
records are in `Z_f`. Their signed product is the observable `Z_a Z_c`. The
cluster stabilizer relation gives

```text
Z_a X_b Z_c=+I on the prepared cluster.
```

For `A=n_xX+n_yY+n_zZ`, linearity and the exact vanishing of the other two
correlators give

```text
<A_b Z_a Z_c>=n_x.
```

The center outcome and endpoint parity are unbiased binary variables in this
state. A deterministic signed relation requires their correlation magnitude
to be one. Cauchy saturation for a unit vector forces `A=+/-X_f`.

This is a uniqueness theorem over every binary rank-one qubit PVM, not just a
comparison of three labels.

### Outcome sign and orientation

The theorem selects an unordered PVM. If orientation is reversed,

```text
X_f=-iY_fZ_f -> -X_f.
```

The same two projectors exchange names. The parity contract becomes either

```text
s_center =  z_left z_right
```

or

```text
s_center = -z_left z_right,
```

depending on label convention. Orientation reversal only swaps outcome
labels; it does not produce the `Y_f` PVM.

## 6. Exact Same-Boundary Transcript Pair

Both laws begin with the same six-record header and the same seventh trigger
record:

- the exact six `H1/H0` header records; and
- the same trigger `Z0` at `t`.

Both use the same plus data reset, same certificate/relay/fragment sites, same
fragment reset, same `CZ-CZ`, same target flip, same endpoint `Z_f` reads, and
same straight growth grammar.

### Remaining-leg `X_f` law

The fragment witness repeats the center sign. Endpoint records obey

```text
left xor right = 0 for center +,
left xor right = 1 for center -.
```

There are four complete tuples, each with Born-instrument weight `1/4`.

### Header-leg `Y_f` law

The fragment witness still repeats the center sign and the conditional endpoint
state is maximally entangled. But both endpoint parities occur for either
center sign. There are eight complete tuples, each with weight `1/8`.

Thus the same actual header and boundary have distinct future record
transcripts. This is stronger than a matrix-label comparison.

### Smallest separating field

The two laws differ in a binary role field:

```text
READ_ROLE in {REMAINING_LEG, HEADER_LEG}.
```

The operational parity contract removes that free field:

```text
PC: center sign is the endpoint-Z parity certificate.
```

Then `READ_ROLE=REMAINING_LEG` and `A=X_f` follow. `PC` is the smallest useful
separator because it mentions only eventual readable records, not a chosen
matrix or coordinate axis.

It is not yet independently present in the propagation grammar. Calling the
stage record a “certificate” does not supply what it certifies. That semantic
must be derived from the final exact law, included as a candidate law field,
or tested as an empirical target.

## 7. Clause-Delete Ledger

| deleted clause | exact control | result |
|---|---|---|
| typed six-record header | no unique `t,d,e,u` motif | `HEADER_GEOMETRY` lost |
| corner/line asymmetry | swapping transverse roles can survive | spatial role ordering lost |
| Cycle-14 certificate position `q=t-e` | both negative-`e` and negative-`u` center neighbors are unused | apparatus arm not selected geometrically |
| one-edge role relay | fragment site does not receive local stage readiness | `ROLE_TRANSPORT` remains a finite-radius convention/import |
| cross-site `Y/Z` connection | `-iYZ` cannot compare records at different sites | internal frame not physical |
| parity-certificate contract | exact `J_X/J_Y` and apparatus pair survive | `CONTEXT` role bit remains |
| Bell fusion | longitudinal `Z` competitor returns | equatorial class no longer selected |
| nondemolition | apparatus no longer guarantees a stable repeated pointer | Cycle-15 reduction unavailable |
| blank reset | same `U_X` with an `X`-eigenblank induces the identity channel | no fragment imprint |
| execution | zero and one applications differ | `EVENT` occurrence not supplied |
| future-operation restriction | `U_A^2=I` erases the coherent imprint | `PERSISTENCE` not supplied dynamically |
| branch selection | executed copy remains a pure entangled state | `ACTUALITY` not supplied |

The parity theorem does not hide the other interfaces. It selects context only
after exact cluster preparation, endpoint decoder, and certificate semantics
are fixed.

## 8. Interface Map

| interface | conditional closure in this cycle | exact residual |
|---|---|---|
| `HEADER_GEOMETRY` | actual six records uniquely decode `t,d,e,u` | why this seed/pattern is realized |
| `ROLE_TRANSPORT` | certificate at `q`, one NN relay at `r`, and fragment at `f` give a covariant collision-free rail | derive relay append and shared internal comparison from admissibility |
| `CONTEXT` | parity-certificate semantics uniquely selects center `X_f` up to sign; apparatus commutant verifies it | derive or adopt `PC` as exact-law content, not by literal X label |
| `BLANK` | integrated reset makes every fragment input `|Z_f+>` | reset target/irreversibility and its selection |
| `EVENT` | supplied complete CP instrument has two exact branches | readiness-to-occurrence rule |
| `PERSISTENCE` | record-set extension can be stipulated after the branch | physical no-return/future-operation scope |
| `ACTUALITY` | none | one actual branch and probability/frequency law |

The actual motif materially closes geometry and offers a complete local
apparatus. The remaining context field can be reduced to one operational
record relation. It does not collapse occurrence or actuality.

## 9. Constitutional Readout

This cycle supports no `X`, frame, chirality, parity, apparatus, or witness
sentence in the Record axiom.

The successful selection chain is downstream and law-specific:

```text
actual header geometry
  + transported H/Y and trigger/endpoint Z contents
  + cluster stabilizer
  + operational center-parity certificate semantics
  + complete NN center-fragment instrument
  -> center X PVM up to outcome swap
  + exact repeatability
  -> Lüders branches.
```

A generic axiom phrase such as “records use the remaining leg” would merely
hide the decoder. A generic phrase such as “a record is a parity certificate”
would be false for arbitrary records. The exact relation belongs in the
candidate law/theorem dossier until the one fixed admissibility rule forces it.

The most economical next action is to ask whether `PC` follows from a more
general record-consistency principle already needed elsewhere—for example,
whether every stage certificate must be the minimal deterministic function of
the future disjoint records it enables. That principle has not been stated or
proved here and must not be inferred from the word “certificate.”

## 10. Primary-Source Ledger

| primary source | content used | boundary here |
|---|---|---|
| Raussendorf, Browne, and Briegel, [*The one-way quantum computer — a non-network model of quantum computation*](https://arxiv.org/abs/quant-ph/0108118) | cluster states plus sequences of local one-qubit measurements can process and route quantum information | begins with the cluster resource and measurement program; it does not select this framework's header, read role, or event law |
| Hein, Eisert, and Briegel, [*Multi-party entanglement in graph states*](https://arxiv.org/abs/quant-ph/0307130) | graph states arise from Ising-edge interactions; stabilizer formalism and local Pauli-measurement transformation rules characterize their correlations | supplies the standard graph-state setting, not this exact record decoder or law selector |
| Głowacki, [*Operational Quantum Frames*](https://arxiv.org/abs/2304.07021) | a quantum reference frame is a physical system with a covariant observable; operational equivalence is defined through available relative effects | supports testing complete framed transcripts rather than matrix labels; does not select `J_X` or `J_Y` |
| Carmeli, Heinosaari, and Toigo, [*Covariant quantum instruments*](https://arxiv.org/abs/0805.3917) | covariant instruments admit a general structure theorem and irreducible-representation characterization | covariance organizes a family after action and outcome space are supplied; it does not choose the parity member |
| Bagan, Baig, and Muñoz-Tapia, [*Aligning Reference Frames Using Quantum States*](https://arxiv.org/abs/quant-ph/0106014) | an orthogonal trihedron can be encoded and recovered as physical quantum information | does not derive the actual six-record motif or bind its typed axis to one spatial leg |

Every finite conclusion used here—the header decoder, support collision test,
role maps, stabilizer, correlator, apparatus commutants, and transcripts—is
also checked directly by the companion runner.

## 11. Exact Runner Coverage

The companion runner checks:

1. authority, foundation, primitive-registry, predecessor, and primary-source
   contracts;
2. the exact six header sites and `H1,H0,H1,H1,H0,H1` contents;
3. unique decoding of the base header and all 24 translated/rotated copies;
4. failure of the `e/u` spatial swap to preserve the header;
5. exact certificate, relay, fragment, and center coordinates;
6. all three NN role-rail edges and avoidance of header/data/builder support;
7. twelve collision-free straight cells;
8. two exact proper role maps `J_X/J_Y`, their relative `Z` quarter-turn, and
   full proper-cubic intertwining;
9. unchanged role propagation under the straight self-writing grammar;
10. orientation reversal `X -> -X` and unordered-PVM invariance;
11. fragment reset from arbitrary pure, mixed, and coherent inputs;
12. paired same-blank `X/Y` controlled-copy unitaries, simple commutants,
    dephasing, orthogonal witnesses, and nondemolition;
13. the complete four-qubit cluster--fragment branch instrument;
14. exact middle stabilizer `Z-X-Z`;
15. the general correlation identity `<Z A Z>=n_x` on named and random axes;
16. uniqueness of the correlation-saturating PVM;
17. concurrence one for every sampled equatorial center PVM and zero for `Z`;
18. four `X` transcripts at `1/4` versus eight `Y` transcripts at `1/8`;
19. the deterministic endpoint-parity separator;
20. blank, execution, reversal, actual-branch, and alternate-arm deletes; and
21. the formal interface and N1--N8 contracts.

## No-Go Discipline Gate

**No-go discipline status: `PASS`** for this narrow finite claim:

> The actual six-record header, proper-cubic covariance, Bell concurrence,
> nondemolition, and role-consistent straight propagation do not by themselves
> select `J_X` rather than `J_Y`; deleting the endpoint-parity certificate
> contract leaves the displayed same-header paired laws.

The exact positive theorem is equally important: adding the operational
parity-certificate contract uniquely selects the `X_f` PVM. This is not a
universal no-go against deriving that contract from the eventual fixed
admissibility rule. The overall result remains
`partial-attempt-with-named-untested-routes`.

### N1 — Alternative-Route Enumeration

| route | honesty | attempted closure | result |
|---|---|---|---|
| raw six-record pattern | ATTEMPTED | decode spatial frame directly | succeeds uniquely for `t,d,e,u` |
| long/short header asymmetry | ATTEMPTED | distinguish `e` from `u` without internal labels | succeeds spatially; does not bind `Y_f` to one ray |
| typed `H/Y` contents | ATTEMPTED | infer the `Y_f` leg from where H records sit | fails uniquely because H records occupy both rays and the corner |
| trigger/data `Z` role | ATTEMPTED | bind propagation `d` to `Z_f` | succeeds conditionally through trigger/endpoints and `CZ-CZ` commutant |
| Cycle-14 certificate site | ATTEMPTED | select an unused apparatus arm | negative-`e` rail is exact and collision-free |
| NN role relay | ATTEMPTED | transport readiness locally to the center fragment | one same-content relay gives exact local support; relay occurrence remains law content |
| proper-cubic covariance | ATTEMPTED | select one spatial/internal map | both `J_X/J_Y` intertwine exact transported actions |
| chirality | ATTEMPTED | choose remaining versus header leg | both maps are proper; reversing hand only changes `X` sign |
| Bell concurrence | ATTEMPTED | require maximally entangled endpoints | every equatorial axis ties |
| nondemolition/simple commutant | ATTEMPTED | demand a stable exact pointer | both paired controlled copies pass |
| hard-coded X readiness prefix | ATTEMPTED AND REJECTED AS CIRCULAR | use current string grammar to select X | merely restates explicit field `D2` |
| endpoint-parity certificate | ATTEMPTED | require center sign to determine later endpoint XOR | succeeds uniquely for `+/-X` PVM |
| phase-sensitive continuation | RULED IN BY CYCLE 17 | separate X/Y downstream | succeeds but is less minimal than already-present endpoint Z parity |
| full unique admissibility law | UNTESTED POSITIVE ROUTE | derive relay, parity semantics, event, and persistence jointly | strongest surviving route; can retire `PC` as an import |

Thirteen routes were executed or inherited exactly and one stronger route is
kept open. Several positive routes succeed, so no broad context no-go ships.

### N2 — Wall-Independence Audit

After retiring raw spatial geometry, the collapsed open-condition set is:

- `F`: physically transport/compare the `H/Y`, trigger/endpoint `Z`, and role
  relay across the motif;
- `D`: derive the operational parity-certificate semantics and hence the
  remaining-leg apparatus relation;
- `B`: select the fragment reset target and irreversible blank-preparation
  operation;
- `E`: derive occurrence and future-operation/no-return scope; and
- `A`: derive one actual transcript and its probability/frequency law.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `F,D` | no; transported frame records admit both role maps | no; an abstract parity decoder can be hard-coded without deriving frame transport | yes |
| `F,B` | no; frame transport does not reset a fragment | no; a blank has no cross-site comparison law | yes |
| `F,E` | no; records/relay do not schedule themselves | no; occurrence can execute either frame law | yes |
| `F,A` | no; a frame names alternatives | no; an actuality rule need not derive a frame | yes |
| `D,B` | no; parity semantics does not prepare the witness | no; the same blank supports X or Y apparatus | yes |
| `D,E` | no; a selected pointer relation does not execute | no; event occurrence can apply either paired decoder | yes |
| `D,A` | no; X has two attainable outcomes | no; a history selector does not derive why its center means parity | yes |
| `B,E` | no; a blank may remain unused | no; an event can act on a nonblank state | yes |
| `B,A` | no | no | yes |
| `E,A` | no; coherent execution retains both branches | no; one history does not derive readiness or no-return | yes |

The relay site's spatial existence is closed by geometry; its append event is
part of `F/E`. Chirality sign is not an independent context wall because it
only permutes the two selected outcomes.

### N3 — Hidden-Wall Scan

| trigger | classification |
|---|---|
| “we assume” / “by construction” | no proof substitute; each prepared state, relay, map, and semantics appears as a displayed condition or candidate-law field |
| “as is standard” / “standard QFT” | absent from load-bearing inference |
| “the framework provides” | used only through direct current axiom/registry inventory |
| “bridge context” / “background” | no hidden use; cross-site comparison, reset, relay, apparatus, and decoder are explicit |
| “naturally” / “obviously” | absent from inferential steps |
| “registered” | only the approved primitive inventory; no primitive is enlarged |
| “canonical” | Cycle-14 reset target is called law-selected, not canonical; no role map or parity contract gets standing by naming |
| “certificate” | explicitly split into stage marker versus operational endpoint-parity semantics; the word alone carries no theorem |

The hidden conditions most likely to slip through are precisely the ones the
runner deletes: content transport, the relay write, reset target, apparatus
role, execution, no-return scope, and actual branch.

### N4 — Residual Matching

| prior witness | residual there | residual used here | match? |
|---|---|---|---|
| `APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md:159-232,312-343` | exact header, supplied frame, explicit `X/Z` instruments, center parity theorem | actual header/decoder seam and parity output | yes |
| `SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md:216-343,370-386` | certificate `t-e`, straight builder geometry, reset, same `CZ-X-Z` law fields | actual role rail and blank/event extension | yes |
| `RELATIONAL_POINTER_CONTEXT_SELECTION_CYCLE16_NOTE_2026-07-14.md:456-504,723-740` | `CZ-CZ` selects `Z`; Bell capability ties `X/Y`; full apparatus is open route | apparatus commutant and Bell tie | yes |
| `CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md:217-403,723-742` | two rays construct `X`; actual header-position decoder remains N7 target | exact target attacked here | yes |
| `FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md:141-216` | spatial group does not itself supply onsite `PU(2)` lift; decoder must co-transform | paired proper role maps | yes |
| `RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md:18-96,683-724` | repeatability derives Lüders after context/event | consumed only after `PC` selects context | yes |

No hard-coded predecessor `X` value is used as a witness that `X` is derived.
No Bell-entanglement theorem is misquoted as a parity theorem.

### N5 — Rhetoric And Resolution Audit

| resolution | exactly tested | untested extension and wording limit |
|---|---|---|
| one finite six-record header | exhaustive decoder over candidate triggers/cardinal frames | not every possible header code |
| twelve straight cells | collision-free role rail and builder support | turning/branching/multi-front rails remain unclassified |
| one qubit role map | exact `J_X/J_Y` proper pair | not all higher-carrier representations |
| one center + one fragment | complete controlled copy and reset | not every apparatus dilation |
| one three-site cluster | arbitrary center Bloch axis correlation functional | not arbitrary graph resources |
| endpoint records | exact local `Z/Z` transcript distribution | other endpoint contexts could select another center observable |
| orientation | sign reversal and outcome-PVM swap | no general matter/Weyl chirality theorem |
| actuality | one finite coherent branch pair | no universal interpretation no-go |

Accordingly the note says the tested generic conditions leave the displayed
role pair. It does not say no future admissibility theorem can derive `PC` or a
different complete decoder.

### N6 — Partial-Closure Paths And Primitive Scan

The registry contains only `minimal_axioms`, `scale_reference_primitive`,
`kinetic_isotropy_primitive`, and `realized_state_primitive`. The latter three
supply no header, connection, role relay, apparatus, blank, parity semantics,
event, persistence, or actuality selector.

Concrete retirement paths are:

1. define center certificate operationally by the endpoint-parity transcript,
   then apply the exact uniqueness theorem here;
2. derive `PC` from a broader minimal-certificate consistency principle, if
   such a principle is independently needed and made exact;
3. derive the relay append and `Z` blank reset from the actual nearest-neighbor
   admissibility rule;
4. replace the irreversible reset with an exact archive/dilation and prove its
   no-return sector;
5. derive cross-site frame comparison from the self-written `H/B/D` content
   sequence rather than importing `Q2`;
6. enlarge the exact law to include occurrence and append scope, making the
   center--fragment commutant a theorem of the selected law; and
7. pursue actuality/statistics independently through a sampled instrument,
   unique global history, or other exact completion.

Paths 1--3 can retire the context/blank fields without a new axiom. No
unapproved primitive receives premise weight.

### N7 — Strongest Hostile Steelman

**Hostile steelman:** The note is being too conservative about the word
“certificate.” Cycle 13 does not merely call the center a stage token; it
proves that the center sign fixes endpoint parity and describes that relation
as what the clock certificate locks. Cycle 14 preserves the same intended
decoder. If the scientific identity of a center certificate is its readable
parity relation—not its literal `X` string—then `PC` is already the operational
specification of the candidate, not a new arbitrary field. The cluster
stabilizer theorem then forces the remaining-leg `X_f` PVM, the negative-`e`
certificate rail supplies the apparatus arm, the complete interaction in this
cycle supplies its simple commutant, and Cycle 15 derives Lüders form. The
context seam is closed inside the candidate law without an axiom.

The steelman succeeds conditionally and is the strongest reading of the
result. It demotes any broad negative. The remaining audit question is exact:
does the current candidate law define “center certificate” by future parity,
or does it merely produce parity after separately specifying `D2=X`? The live
readiness code presently uses the latter shape: it checks an `X` name and does
not consume endpoint XOR. Until the law interface is rewritten and audited in
operational terms, `PC` remains an explicit candidate-law condition.

The paired countermodel survives only after deleting `PC`; it does not refute
the successful operational decoder theorem.

### N8 — Cross-Cycle Echo

The prescribed repository search was rerun for `structurally undecidable`,
`no retained primitive`, `requires new axiom`, and
`cannot be derived from A_min`. All physics-loop `NO_GO_LEDGER.md` files were
also searched for reference-frame, role-decoder, pointer, measurement-basis,
readout-context, parity-certificate, and chirality walls. No matching retained
ledger result was imported as proof.

The relevant cross-cycle mechanisms are:

- Cycle 16 retired generic context supply after a simple interaction
  commutant is known;
- Cycle 17 retired a full independent Pauli frame by using two physical rays;
- this cycle retires abstract spatial-triad supply with the actual header and
  reduces the final azimuth to one operational record relation;
- earlier decoder/co-recoding work shows that a fixed readable relation can
  distinguish presentation-conjugate laws; `PC` is such a relation;
- previous stage-certificate work warns that a record marking completion does
  not automatically state what physical fact it certifies; the stage/parity
  split preserves that warning;
- prior reset work converts a prepared-state boundary into exact law content
  but does not derive the reset target; the integrated fragment reset has the
  same status; and
- prior occurrence/actuality controls remain untouched by context closure.

The repeated retirement mechanism is constructive: add exact interaction and
operational decoder data, then recompute what becomes a theorem. Nothing here
supports new generic Record prose.

## Bottom Line

The strongest actual-motif construction is now:

```text
six typed header records
    -> unique spatial d,e,u

Cycle-14 certificate at t-e
    -> collision-free negative-e apparatus rail

transported H/Y + trigger/endpoint Z
    -> full internal frame and candidate X=-iYZ

cluster stabilizer + center-is-endpoint-parity semantics
    -> unique center X PVM up to outcome swap

one NN role relay + integrated Z-blank reset + controlled copy
    -> complete local center-fragment instrument with simple X commutant

binary attainability and repeatability
    -> Lüders form.
```

This is the first route in the sequence that uses the actual record header and
the already-produced endpoint transcript to select `X`, rather than an
abstract frame or a matrix name.

The remaining decision is not “X or Y?” in the axiom set. It is whether the
candidate exact law's center certificate is operationally defined by endpoint
parity. If yes, the context seam closes conditionally and only frame transport,
reset/relay selection, occurrence, persistence, and actuality remain. If no,
the same-header `J_X/J_Y` pair proves that one binary role field is still in
the law.

Orientation and chirality only determine which center sign is called even;
they do not select a different PVM. No axiom need follows from this cycle.

## Verification

Run:

```bash
python3 scripts/actual_header_role_decoder_parity_selection_cycle18_2026_07_14.py
```
