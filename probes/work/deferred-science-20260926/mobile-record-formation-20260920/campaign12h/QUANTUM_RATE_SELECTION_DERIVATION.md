# Primary derivation: operational consistency and the formation clock

2026-09-21. Personally derived after the single-qubit interface calculation,
before access to the separate quantum-interface check. This is a conditional
ordinary-quantum-operation interface, not an inference from the minimal axioms.
It gives positive instruments as well as obstructions. Primary exact and
numerical checks are complete; independent scrutiny is pending.

## Interface and notation

A parent is an unknown physical qubit in one of the six Pauli-axis pure states
rho_a=(I+v_a dot sigma)/2. Multiple parents are independently prepared, with
joint density operator tensor_i rho_(a_i). No extra preparation-label register
or input-correlated ancilla is available. The instrument and its ancillary
input are fixed independently of the unknown labels. Parents may be disturbed.
An occurrence of formation is an observable event; where specified it also
has a classical six-valued mark b. These are additional physical bridge
assumptions. They are not supplied by the one-site possibility algebra alone.

Write D=p+q+4r, with p,q,r>0. Let W_ab=6p/D for equal contents, 6q/D for
opposite contents and 6r/D for orthogonal contents, so each row sums to six.
For k parent labels A=(a_1,...,a_k), put

```
U_b(A)=product_i W_(b,a_i),       Z(A)=sum_b U_b(A),
P(b|A, formation)=U_b(A)/Z(A).
```

A Markovian event instrument has positive rate operators F_b, with rates
R_b(A)=Tr[F_b tensor_i rho_(a_i)]. Its total rate is H(A)=sum_b R_b(A).
More generally these are the first derivatives of a differentiable observed
event probability at a fixed time, provided the microscopic input preparation
is the stated density operator. For sufficiently small dt, dt F_b are effect
operators and I-dt sum_b F_b is the no-event effect. Positivity, linearity
and the same prepared density operator giving the same statistics are the
only quantum facts used in the rate tests below.

## 1. A content-dependent success clock does not repair a one-parent kernel

Allow arbitrary nonnegative input-dependent H(a), with a nonzero event
operator, and require the stipulated conditional classical kernel exactly
on every input for which H(a)>0. Because all p,q,r are positive, it is useful
to formulate the requirement directly as

```
R_b(a)=H(a) W_ba/6
```

for all six inputs, including any zero-rate inputs. Since H is the expectation
of a positive qubit operator, it has the form H(a)=c+u dot v_a, with c>0.
Every R_b is also affine in v_a. For a fixed b along coordinate i, equality
of the antipodal input averages from axis i and an orthogonal axis requires

```
c(p+q-2r) + (p-q) sign(b) u_i = 0.
```

The same equation for the opposite output -b changes only the second sign.
Consequently p+q=2r is necessary, and if p!=q then u_i=0 for every i.
Thus postselection by a quantum occurrence event does not rescue a kernel
off the same Born-compatible surface. On that surface with nonzero j,
the one-parent event rate must be input independent. If p=q=r, the classical
mark carries no information, and a separate nonconstant positive event
operator is possible. The zero event operator never produces a conditional
law and is not counted as a realization.

This argument does not assume cubic covariance of the unknown instrument.
It allows arbitrary quantum filtering, but not a correlated classical record
of which preparation label was selected.

## 2. Product odds select the clock on the nontrivial j-family

On p+q=2r, define j=(p-q)/(2r), so -1<j<1 and
W_ba=1+j v_b dot v_a. Assume j!=0. Suppose positive rate operators implement
the product conditional odds for k>=1 parents. Define

```
h(A)=H(A)/Z(A),       R_b(A)=h(A) product_i W_(b,a_i).
```

Fix all parent labels except a_i. Dividing each R_b by the positive constant
product_(l!=i) W_(b,a_l) shows that the six functions
h(a_i)(1+j v_b dot v_(a_i)) are affine in the remaining Bloch vector.
Summing them over b shows that h itself is affine:

```
h(a_i)=c+u dot v_(a_i).
```

For output b along axis l, the antipodal average of
h(a_i)(1+j v_b dot v_(a_i)) over inputs on axis l is
c+j sign(b) u_l. Over either orthogonal input axis it is c. Hence u_l=0
for every l. Thus h is independent of a_i, for every choice of the other
inputs. Repeating for each coordinate of the label tuple proves h(A)=C,
a constant over all six-to-the-k input preparations. Since the product
states span the Hermitian operators on k qubits, the rate operators are unique:

```
F_b = C tensor_i (I+j v_b dot sigma_i),
H(A)=C Z(A),              C>=0.
```

These F_b are positive for |j|<=1 and implement the desired rates. For the
strict positive-weight domain -1<j<1 and a nonzero process, take C>0.
For sufficiently small dt, the jump Kraus operators sqrt(dt F_b) together
with sqrt(I-dt sum_b F_b) form an explicit instrument. Conditional on the
classical mark b one can prepare a newborn qubit rho_b as another output.
The instrument changes the parent qubits; no nondemolition claim is made.

This derives the product-weight hazard, up to an overall multiplier, from
the stated quantum-interface and conditional-odds requirements. It does not
select C, j, the spatial rate schedule, the physical time unit, or the number
of parents k. Constants C_k can differ with a known occupancy geometry or
other fixed classical context; the argument fixes dependence on the unknown
input content, within that context. For j=0 the uniqueness argument fails
and a separate content-sensitive event effect is possible even though the
classical output mark is uniform.

For k>=2, replacing H(A)=C Z(A) by a constant occurrence clock generally
breaks this interface even on the j-family: Z(A) is not constant. Thus the
distinction between conditional odds and occurrence rate has an operational
consequence, under these additional physical assumptions.

## 3. Two-parent occurrence alone exposes the axis-population component

Discard the classical mark requirement. Retain only the supplied product
birth intensity for a vacancy with two parents a,c and all other neighbors
empty:

```
H(a,c)=epsilon sum_b W_ba W_bc=epsilon (W^2)_ac.
```

This is an observable event rate even if no newborn content label can be
read. Prepare parent c=+x. For the other parent compare the equal mixture
of +/-x with the equal mixture of +/-y. Both prepare exactly I/2. A single
fixed quantum operation must give the same occurrence rate, yet the supplied
rates differ by

```
Delta H = epsilon [6(p+q-2r)/D]^2 / 2.
```

To see this without a spectral assumption, write the normalized equal,
opposite and orthogonal weights as P,Q,R. The first preparation averages
the two hazards to (P+Q)^2/2+4R^2; the second gives 2R(P+Q)+2R^2. Their
difference is (P+Q-2R)^2/2. Therefore exact occurrence-rate realizability
requires p+q=2r. This test needs neither a classical output mark nor perfect
preservation of the parents. A preparation-label side channel would change
the resource premise and evade the test.

The condition is sufficient for this two-parent occurrence rate. On the
j-family the unique rate operator is

```
R = epsilon [6 I tensor I + 2 j^2 sum_(i=x,y,z) sigma_i tensor sigma_i].
```

Its triplet eigenvalue is epsilon(6+2j^2); its singlet eigenvalue is
6 epsilon(1-j^2). It is positive, and the positive individual F_b from
section 2 sum to it. The event can be implemented as a measurement, subject
to its necessary parent disturbance and no-event back action.

Let an approximate quantum rate operation have worst-case absolute rate
error delta over the 36 product inputs. The two equal-density preparations
above then imply

```
delta >= epsilon [6(p+q-2r)/D]^2 / 4.
```

This is a lower bound, not generally the optimal value: positivity of the
two-qubit rate operator can impose an additional error. It is a rate error
in the supplied abstract time units, not an empirical experimental bound.
Do not replace it by a relative error without specifying nonzero reference
rates. A direct unrestricted positive-operator fit is a useful check.

## 4. Operational limits and the next decision

The earlier one-parent quantum-only newborn marginal erases the axis
parameter, so it could not alone exclude that component. The two-parent
occurrence test is a different, stronger observable for the stated clock.
It does not retract the earlier marginal-only escape: those interfaces ask
for different accessible statistics. A clock or interaction that hides
the offending statistics is a different model requiring its own test.

Positive rate operators supply a consistent event instrument, not immutable
unknown physical parent records. The information/disturbance proof in
`QUANTUM_FORMATION_INTERFACE_DERIVATION.md` remains relevant. Orthogonal
pointer facts, a classical content-label register, or a larger spatial
encoding can implement different interfaces, with their extra resources
declared. None of these conditional tests identifies which meaning the
axiomatic word "record" must have.

The high-leverage positive implication is limited but concrete: ordinary
quantum operational consistency can constrain both the admissibility menu
and its occurrence clock, if that physical bridge is supplied. This is
stronger than choosing a stochastic clock for convenience, but it is not
yet a derivation of quantum theory, permanent record formation, or the TOE.

## Primary verification

`quantum_rate_selection_check.py` checks the symbolic two-parent rate operator
and its singlet/triplet spectrum. Exact sparse elimination gives a one-dimensional
space of allowable clock multipliers at j=1/2 for one, two and three parents;
at j=0 the dimensions are 4,16,64, as predicted for general multilinear qubit
effects. Off-surface one-parent controls include both p!=q and p=q: in the
latter case an odd three-dimensional linear residue exists, but every
nonzero such total-rate operator is indefinite and is excluded by positivity.
This distinction prevents a mistaken purely linear no-solution assertion.

Fifteen explicit instruments, at j=-0.8,-0.5,0,0.5,0.8 and one through three
parents, satisfy positivity, completeness, and every prescribed marked rate
within floating-point tolerance. An exact j=1/2 two-parent constant-clock
counterexample gives probabilities 69/286 and 1/4 for two preparations of
the same I/2 tensor rho_(+x), a discrepancy -5/572. The corresponding
unnormalized marked rates have identical mixture averages, as required.

Ten unrestricted positive two-qubit rate-operator fits obey the necessary
rate-error lower bound. Their optima also agree with a primary candidate
piecewise formula within 9.1e-9; that stronger formula is not a theorem claim
of this note because its complete optimization proof has not been carried
here. For raw (12,1,2), the necessary lower bound is 81/49, whereas the
numerical optimum is about 2.833819242, illustrating the extra positivity cost.

The first symbolic run failed because SymPy returned algebraically equal
triplet eigenvalues in factored and expanded forms as different dictionary
keys. The failed source, log and hashes are preserved in
`quantum_rate_initial_failure/`. Canonical expansion with addition of their
multiplicities fixes the comparison; the rate operator and its predicted
spectrum are unchanged. Full final results and the source hash are in
`QUANTUM_RATE_SELECTION_RESULTS.json`.
