import dendropy
import sys

filename = sys.argv[1]
brate = float(sys.argv[2])
drate = float(sys.argv[3])

tree = dendropy.Tree.get(path=filename,schema="nexus")
ll = dendropy.model.birthdeath.birth_death_likelihood(tree = tree, birth_rate = brate, death_rate = drate, condition_on="taxa")
print(ll)