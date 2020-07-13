word = input()

croatias=( "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")

for croatia in croatias:
    word = word.replace(croatia, '0')

print(len(word))


