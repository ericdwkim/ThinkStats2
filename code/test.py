import nsfg

df = nsfg.ReadFemPreg()
# print(df)

# print(df.columns[1])

# pregordr = df['pregordr']
# print(pregordr)
# print(type(pregordr))

# print(pregordr[0])
# print(pregordr[2:5])

pregordr = df.pregordr
print(pregordr)
print(pregordr[0])
print(pregordr[2:5])
