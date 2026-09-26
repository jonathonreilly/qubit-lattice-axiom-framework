# Capture, inertia and which quantity grows

2026-09-21. Primary algebraic diagnostic while catching up with PR8558.
This does not review its uninspected runner or simulations and is not a
new gravitational result. It separates two supplied body closures that
must not be identified merely because they agree initially.

Source: PR8558 at f23fd989d6ef2290319167208ab7098cd7975f62, complete note
SHA1dd75e82e4d0c9c0ff8d5db0f4d521e5205f780369f59a38dfaf92265f2fb772,
read in full. Exact source snapshots live under
`/Users/jonreilly/Documents/Codex/physics-sync-2026-09-20/pr-8558-sources/`.
Main remains5d784d8; ai/execution remains068e916 after the07:15 fetch.
The new note explicitly repairs its earlier free-streaming capture argument,
separates collisional and anisotropic collisionless coefficients, and states
its body law as a closure. Those distinctions should be retained.

Let N_cap be the number of exposed capture sites, M the number of records
assigned to a body, and q1 the product-bath capture rate per exposed site.
In the small-velocity closure, ignore the additional capture from the body
stepping into occupied gas sites. Then

    Q=q1 N_cap,   M'=Q,   P'=Q u(x),
    p=P/M,       x'=p/sqrt(3),
    p'=(Q/M)[u(x)-p].

These equations are bookkeeping under the supplied transfer and body-velocity
clauses. They do not specify where captured permanent records are stored.

For a fixed rigid footprint N_cap=N0 and a constant bath wind u, Q is
constant, and the exact closure solution is

    M(t)=M0+q1 N0 t,
    p(t)=[M0 p0+q1 N0 t u]/[M0+q1 N0 t],
    captured fraction f=q1 N0 t/[M0+q1 N0 t].

Thus the relaxation rate is q1 N0/M(t), not constant q1. With N0=M0 it is
q1/(1+q1 t), and p-u decays as1/(1+q1 t).

A distinct closure makes **every retained record a new exposed capture site**,
N_cap(t)=M(t). It gives M=M0 exp(q1 t), constant relaxation rate q1 and
p-u=(p0-u)exp(-q1 t). This is exactly the extra relationship needed for
PR8558 T5's constant rate. That theorem explicitly says every record
captures; its condition does not automatically follow from the preceding
rigid-set body clause, whose site footprint is fixed. The two closures agree
to first order at t=0 when N0=M0, and differ afterward.

For orientation, at rho=.3 the quoted q1=sqrt(3)rho/2 gives q1 t≈10.3923
at t=40. The fixed-footprint formula then gives f≈.9122, whereas the
recruiting-footprint formula gives f≈.999969. PR8558 reports captured
fractions around.89-.90 in that screen. Those numbers are not a new fit,
validation or code finding: they illustrate why comparison to the measured
fraction u f does not itself test the constant-q1 closure. Its simulations
and runner have not been inspected here.

There is a related exact identity for a radial closure wind u(x) parallel
to x. Angular momentum defined with the retained momentum is conserved:

    d/dt[x cross P]=x' cross P+x cross P'=0.

Specific angular momentum x cross p equals that constant divided by M.
It decays algebraically for the fixed-footprint closure and exponentially
for the recruiting-footprint closure. These statements concern the chosen
continuous closure and do not establish the existence or absence of
microscopic orbits.

Finally, a finite rigid footprint initially containing one permanent record
at every storage site has no unused record capacity. Continued capture
requires explicit transport to additional storage sites, recruitment of new
sites, or departure of old records. An external mass/momentum accumulator
is a useful kinetic abstraction but does not itself provide that site-level
implementation. Swapping an incoming record with an outgoing old record is
one capacity-respecting alternative, but it changes the net capture current
and requires a new force calculation. No such new force is assumed here.
