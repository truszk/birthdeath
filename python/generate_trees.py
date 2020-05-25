import dendropy
from dendropy.simulate import treesim
from math import log

import os


# generates a birth-death tree with n taxa
# from an alternative parametrization
# r = lambda - mu
# eps = mu/lambda
def generate_bd_tree(r, eps, ntaxa):
	lbda = r/(1.0 - eps)
	mu = lbda*eps
	tree = treesim.birth_death_tree(birth_rate = lbda, death_rate = mu, num_extant_tips = ntaxa)
	return tree


nexus2phyjson_path = r"/home/jakub/goth/webppl/nexus2phyjson/nexus2phyjson/nexus2phyjson"

n_taxa = [4, 16, 128, 1024] 
birth_rate = [0.1, 1.0, 10.0]
epsilon = [0.0, 0.2, 0.7] # death_rate/birth_rate
trees_per_scenario = 3
data_dir = r'data/synthetic/'

if not os.path.isdir(data_dir):
	os.makedirs(data_dir)

for n in n_taxa:
	for brate in birth_rate:
		for eps in epsilon:
			for i in range(trees_per_scenario):
				drate = brate*eps
				#time_for_expected_n_taxa = log(n)/(brate-drate)
				tree = treesim.birth_death_tree(birth_rate = brate, death_rate = drate, num_extant_tips = n, gsa_ntax = n+1)
				tree.seed_node.edge_length = None # no info about the length of the root branch

				filename = data_dir + 'tree_n'+str(n)+"_b"+str(brate)+"_e"+str(eps)+"_"+str(i)
				print("Writing tree file:"+filename)
				# write as nexus for use with nexus2phyjson
				tree.write(path=filename+".nex",schema="nexus")
				# convert to phyjson
				os.system(nexus2phyjson_path+" <"+filename+".nex"+" >"+filename+".phyjson")

				# compute and store the log-likelihood under the specified model - might be useful for testing
				ll = dendropy.model.birthdeath.birth_death_likelihood(tree = tree, birth_rate = brate, death_rate = drate, condition_on="taxa")

				ll_file = open(filename+".ll","w")
				ll_file.write(str(ll))
				ll_file.close()




