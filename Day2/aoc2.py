s = lambda x: (
    '  BXCYAZAXBYCZCXAYBZ'.index(x[0]+x[2]), #Challenge 1
    '  BXCXAXAYBYCYCZAZBZ'.index(x[0]+x[2])  #Challenge 2
    )

print(*[sum(x)//2 for x in zip(*map(s, open('input.txt')))])