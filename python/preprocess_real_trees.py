import dendropy
import os

nexus2phyjson_path = r"/home/jakub/goth/webppl/nexus2phyjson/nexus2phyjson/nexus2phyjson"

real_data_dir = r"data/empirical/"

def newick_to_phyjson(filename):
	tree = dendropy.Tree.get(path=filename,schema="newick")
	tree.write(path=filename+".nex",schema="nexus")
	# convert to phyjson
	os.system(nexus2phyjson_path+" <"+filename+".nex"+" >"+filename+".phyjson")

tree_files = [file for file in os.listdir(real_data_dir) if file.endswith("tre")]

for file in tree_files:
	print("Processing: "+real_data_dir+file)
	newick_to_phyjson(real_data_dir+file)