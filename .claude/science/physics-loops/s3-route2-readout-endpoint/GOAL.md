# Goal

Run a physics-loop campaign on the S3/Route-2 readout endpoint triple. Attack
the source/readout route toward

```text
(-1, -2, 21/4)
```

from first principles, without running audits or applying verdicts. Package
each coherent science block as a review PR and do not push science work to
main.

## Block30 Focus

Factor the remaining Rconn/source-domain bridge into two independent gates:

```text
W1: su3_R_conn_8_9 -> route2_center_TE_minus_8_9
W2: kappa_EW=0 -> R_phys=F_adj=8/9
```

The block asks whether W2 alone can unblock the Route-2 endpoint chain. It
cannot; W1 remains separately load-bearing.
