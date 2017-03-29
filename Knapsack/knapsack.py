for case in range(int(input().strip())):
    N = int(input().strip())
    W = int(input().strip())
    values = [int(v) for v in input().strip().split(" ")]
    weights = [int(w) for w in input().strip().split(" ")]
    vals = {}
    for index, v in enumerate(values):
        vals[v] = weights[index]
    print(N, W, vals)
