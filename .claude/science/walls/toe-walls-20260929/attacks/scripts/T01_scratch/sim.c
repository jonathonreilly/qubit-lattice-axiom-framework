// T01: formation-clause Monte Carlo on a periodic 3D torus (or the open 4-cycle).
// Author: Claude Sonnet 5.5 (same-family check). Compile: cc -O2 -o sim sim.c -lm
//
// usage: ./sim GRAPH CLAUSE p q r L NSAMP NBLK SEED
//   GRAPH : torus | cycle4
//   CLAUSE: U (hazard 1) | E (hazard (1+k)^2) | A (hazard 1/(1+k)) | S (static heat bath)
// output: one CSV row per block:
//   clause,p,q,r,L,blk,n,sum_a1,sum_aopp,sum_aorth,sum_adiag,sum_s,sum_m2,sum_m4
// where per-sample quantities are: a1 = frac of NN edges with equal axis, aopp/aorth similarly,
// adiag = frac of face-diagonal pairs with equal axis, s = mean_x [log g(v_x)+H(g)],
// m2 = |m|^2, m4 = |m|^4, m = mean of the 6-axis unit vectors.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t s[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t next(void) {
    const uint64_t result = rotl(s[1] * 5, 7) * 9;
    const uint64_t t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3];
    s[2] ^= t; s[3] = rotl(s[3], 45);
    return result;
}
static double urand(void) { return (next() >> 11) * (1.0 / 9007199254740992.0); }
static void seed_rng(uint64_t seed) {
    uint64_t z = seed;
    for (int i = 0; i < 4; i++) {
        z += 0x9e3779b97f4a7c15ULL;
        uint64_t x = z;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        s[i] = x ^ (x >> 31);
    }
}

#define MAXN 8192
#define MAXDEG 6
static int N, deg[MAXN], nb[MAXN][MAXDEG];
static int nedges, ea[3 * MAXN], eb[3 * MAXN];
static int ndiag, da[6 * MAXN], db[6 * MAXN];
static int isTorus = 0, L = 0;
static double P, Q_, R_;
static double PHI[6][6];

static int idx(int x, int y, int z) {
    x = (x % L + L) % L; y = (y % L + L) % L; z = (z % L + L) % L;
    return (z * L + y) * L + x;
}

static void build_torus(int Lv) {
    L = Lv; N = L * L * L; isTorus = 1; nedges = 0; ndiag = 0;
    static const int D[6][3] = {{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
    for (int z = 0; z < L; z++) for (int y = 0; y < L; y++) for (int x = 0; x < L; x++) {
        int i = idx(x, y, z);
        deg[i] = 6;
        for (int d = 0; d < 6; d++) nb[i][d] = idx(x + D[d][0], y + D[d][1], z + D[d][2]);
        ea[nedges] = i; eb[nedges++] = idx(x + 1, y, z);
        ea[nedges] = i; eb[nedges++] = idx(x, y + 1, z);
        ea[nedges] = i; eb[nedges++] = idx(x, y, z + 1);
        // face diagonals: (+i,+j) and (+i,-j) for i<j
        da[ndiag] = i; db[ndiag++] = idx(x + 1, y + 1, z);
        da[ndiag] = i; db[ndiag++] = idx(x + 1, y - 1, z);
        da[ndiag] = i; db[ndiag++] = idx(x + 1, y, z + 1);
        da[ndiag] = i; db[ndiag++] = idx(x + 1, y, z - 1);
        da[ndiag] = i; db[ndiag++] = idx(x, y + 1, z + 1);
        da[ndiag] = i; db[ndiag++] = idx(x, y + 1, z - 1);
    }
}
static void build_cycle4(void) {
    N = 4; isTorus = 0; nedges = 4; ndiag = 0;
    for (int i = 0; i < 4; i++) deg[i] = 0;
    for (int i = 0; i < 4; i++) {
        int j = (i + 1) % 4;
        ea[i] = i; eb[i] = j;
        nb[i][deg[i]++] = j; nb[j][deg[j]++] = i;
    }
}

static inline int cls(int a, int b) { return a == b ? 0 : ((a ^ 1) == b ? 1 : 2); }

// Fenwick tree (int64) over site rates
static long long fw[MAXN + 1];
static void fw_add(int i, long long v) { for (i++; i <= N; i += i & -i) fw[i] += v; }
static int fw_find(long long target) { // smallest idx with prefix sum > target
    int pos = 0; int LOG = 1; while ((1 << LOG) <= N) LOG++;
    for (int pw = 1 << LOG; pw; pw >>= 1) {
        int np = pos + pw;
        if (np <= N && fw[np] <= target) { pos = np; target -= fw[np]; }
    }
    return pos; // 0-based site
}

static int val[MAXN], formed[MAXN], kcount[MAXN];
// integer rates: E: (1+k)^2 ; A: 420/(1+k) (420 = lcm(1..7)); U: 1
static long long irate(char clause, int k) {
    if (clause == 'U') return 1;
    if (clause == 'E') return (long long)(1 + k) * (1 + k);
    return 420 / (1 + k);
}

static int draw_content(int x) {
    double w[6]; int any = 0;
    for (int a = 0; a < 6; a++) w[a] = 1.0;
    for (int d = 0; d < deg[x]; d++) {
        int y = nb[x][d];
        if (!formed[y]) continue;
        any = 1;
        for (int a = 0; a < 6; a++) w[a] *= PHI[a][val[y]];
    }
    if (!any) return (int)(urand() * 6);
    double Z = 0; for (int a = 0; a < 6; a++) Z += w[a];
    double u = urand() * Z, c = 0;
    for (int a = 0; a < 6; a++) { c += w[a]; if (u < c) return a; }
    return 5;
}

static void form_race(char clause) {
    for (int i = 0; i <= N; i++) fw[i] = 0;
    for (int i = 0; i < N; i++) { formed[i] = 0; kcount[i] = 0; }
    long long total = 0;
    long long r0 = irate(clause, 0);
    for (int i = 0; i < N; i++) fw_add(i, r0);
    total = r0 * N;
    for (int step = 0; step < N; step++) {
        long long t = (long long)(urand() * (double)total);
        if (t >= total) t = total - 1;
        int x = fw_find(t);
        // remove x
        long long rx = irate(clause, kcount[x]);
        fw_add(x, -rx); total -= rx;
        val[x] = draw_content(x); formed[x] = 1;
        for (int d = 0; d < deg[x]; d++) {
            int y = nb[x][d];
            if (formed[y]) continue;
            long long ro = irate(clause, kcount[y]);
            kcount[y]++;
            long long rn = irate(clause, kcount[y]);
            fw_add(y, rn - ro); total += rn - ro;
        }
    }
}

static void heatbath_sweep(void) {
    for (int x = 0; x < N; x++) {
        double w[6]; for (int a = 0; a < 6; a++) w[a] = 1.0;
        for (int d = 0; d < deg[x]; d++) { int y = nb[x][d]; for (int a = 0; a < 6; a++) w[a] *= PHI[a][val[y]]; }
        double Z = 0; for (int a = 0; a < 6; a++) Z += w[a];
        double u = urand() * Z, c = 0; int pick = 5;
        for (int a = 0; a < 6; a++) { c += w[a]; if (u < c) { pick = a; break; } }
        val[x] = pick;
    }
}

int main(int argc, char **argv) {
    if (argc < 10) { fprintf(stderr, "usage\n"); return 1; }
    const char *graph = argv[1]; char clause = argv[2][0];
    P = atof(argv[3]); Q_ = atof(argv[4]); R_ = atof(argv[5]);
    int Lv = atoi(argv[6]); long nsamp = atol(argv[7]); int nblk = atoi(argv[8]);
    uint64_t seed = strtoull(argv[9], 0, 10);
    seed_rng(seed);
    for (int a = 0; a < 6; a++) for (int b = 0; b < 6; b++) PHI[a][b] = (a == b) ? P : ((a ^ 1) == b ? Q_ : R_);
    if (!strcmp(graph, "torus")) build_torus(Lv); else build_cycle4();
    if (clause == 'S') { for (int i = 0; i < N; i++) { val[i] = (int)(urand() * 6); formed[i] = 1; } for (int t = 0; t < 300; t++) heatbath_sweep(); }
    long per = nsamp / nblk;
    for (int blk = 0; blk < nblk; blk++) {
        double sa1 = 0, sao = 0, saq = 0, sad = 0, ss = 0, sm2 = 0, sm4 = 0;
        for (long it = 0; it < per; it++) {
            if (clause == 'S') { for (int t = 0; t < 3; t++) heatbath_sweep(); }
            else form_race(clause);
            int c[3] = {0, 0, 0};
            for (int e = 0; e < nedges; e++) c[cls(val[ea[e]], val[eb[e]])]++;
            sa1 += (double)c[0] / nedges; sao += (double)c[1] / nedges; saq += (double)c[2] / nedges;
            if (isTorus) {
                int cd = 0; for (int e = 0; e < ndiag; e++) if (val[da[e]] == val[db[e]]) cd++;
                sad += (double)cd / ndiag;
                double mx = 0, my = 0, mz = 0, sc = 0;
                for (int x = 0; x < N; x++) {
                    int a = val[x];
                    if (a == 0) mx++; else if (a == 1) mx--; else if (a == 2) my++; else if (a == 3) my--; else if (a == 4) mz++; else mz--;
                    double g[6], Z = 0; for (int b = 0; b < 6; b++) g[b] = 1.0;
                    for (int d = 0; d < 6; d++) { int y = nb[x][d]; for (int b = 0; b < 6; b++) g[b] *= PHI[b][val[y]]; }
                    for (int b = 0; b < 6; b++) Z += g[b];
                    double H = 0; for (int b = 0; b < 6; b++) { g[b] /= Z; H -= g[b] * log(g[b]); }
                    sc += log(g[a]) + H;
                }
                double m2 = (mx * mx + my * my + mz * mz) / ((double)N * N);
                sm2 += m2; sm4 += m2 * m2; ss += sc / N;
            }
        }
        printf("%c,%g,%g,%g,%d,%d,%ld,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g\n", clause, P, Q_, R_, Lv, blk, per, sa1, sao, saq, sad, ss, sm2, sm4);
    }
    return 0;
}
