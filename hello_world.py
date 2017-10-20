def say():
    # computing
    can = 36 * 2
    cbn = 25 * 2 + 1 + 50
    ccn = cbn + 7
    cdn = cbn + ccn - cbn
    cen = cdn + 3
    cfn = int(can / 2) - 4
    cgn = ccn + 11
    chn = cgn - 20 + 12
    cin = cgn - 5
    cjn = ccn - cbn + ccn - 7
    ckn = ccn - cjn + cbn - 1
    cln = ckn - cbn + int(can / 4) * 2 - 2
    # inisialisasi char
    char = [can, cbn, ccn, cdn, cen, cfn, cgn, chn, cin, cjn, ckn, cln]
    # mapping
    mapped = map(chr, char)
    # listing
    listed = list(mapped)
    # joining :3
    result = "".join(listed)
    # outputing :s
    print(result)

say()
