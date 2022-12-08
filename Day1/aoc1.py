# Challenge 1
print(max(list(map(lambda x: sum([int(i) for i in x.split(',')]),','.join(list(map(lambda x: str(x[:-1]) if x!= '\n' else "-", open("input.txt", 'r').readlines()))).split(",-,")))))

# Challenge 2
print(sum(sorted(list(map(lambda x: sum([int(i) for i in x.split(',')]),','.join(list(map(lambda x: str(x[:-1]) if x!= '\n' else "-", open("input.txt", 'r').readlines()))).split(",-,"))))[-3:]))