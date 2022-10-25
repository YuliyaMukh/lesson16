import string

str = """Norway’s domestic security agency has arrested a man claiming to be a Brazilian academic whom it suspects of being a Russian spy.

“We have requested that a Brazilian researcher at the University of Tromsø be expelled from Norway because we believe he represents a threat to fundamental national interests,” the police security service (PST) deputy chief Hedvig Moe told the public broadcaster NRK.

The security agency was concerned he “may have acquired a network and information about Norway’s policy in the north”, Moe said. “Even if this … is not a threat to the security of the kingdom, we are worried it could be misused by Russia.”"""

# a = 1003
# b = 198
# c = 789
d = {}
alfabet = string.ascii_lowercase

s = str.lower()

for ch in alfabet:

    d[ch] = s.count(ch)
# for key, value in d.items():
#
#     print(key," ", value)

max_key = "a"
min_key = "a"
for key in d:
    if d[key] > d[max_key]:
        max_key = key

    if d[key] < d[min_key]:
        min_key = key

print(max_key," - ", d[max_key])
print(min_key," - ", d[min_key])