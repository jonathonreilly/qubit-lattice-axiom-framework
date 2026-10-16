# Coupling inverse correction

The focused checker identified that the error integrals in v1 equation14
were written without explicit limits. If inherited from equation12, they
would incorrectly reverse sign for y<x. V2 specifies increasing limits on
[min(x,y),max(x,y)] and adds reversed-endpoint numerical controls. V1 and its
25 passing author controls are preserved; they did not exercise this
notation ambiguity. V2 also specifies that a pre-pulse observation at time0
means its left limit. Mathematical pulse and coupling formulae are unchanged.
