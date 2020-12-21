import subprocess
import dendropy
import pandas
import pickle


tree_file = 'data/synthetic/tree_n1024_b1.0_e0.2_1.phyjson'

smc_script = './bdInferSMCUnsorted.wppl'
mcmc_script = './bdInferMCMC.wppl'

def get_output_and_time(arglist):
	arglist_with_time = ['time']+arglist
	p = subprocess.Popen(arglist_with_time,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out = p.stdout.readlines()
	err = p.stderr.readlines()
	timestr = err[-2].split(b'user')[0]
	time = float(timestr)
	return out,time

burnvals = [1000, 10000, 100000, 300000]
samples = 1000
lag = 100
trueLambda = 1.0
trueMu = 0.2

trialno = 6 # we might want to repeat this, not sure how long it will take so for now run just once

for burnin in burnvals:
	out,time = get_output_and_time(['webppl', mcmc_script, '--require', '.', '--require', 'fs', '--', '--tree', tree_file,'--burnin',str(burnin), '--samples', str(samples),'--lag',str(lag),'--trueLambda',str(trueLambda),'--trueMu',str(trueMu)])
	errLambda = float(out[-3].split()[-1])
	errMu = float(out[-2].split()[-1])
	print(str(trialno)+',MCMC,burnin,'+str(burnin)+','+str(errLambda)+','+str(errMu)+','+str(time))

lagvals = [1, 100, 500, 1000]
burnin = 10000

for lag in lagvals:
	out,time = get_output_and_time(['webppl', mcmc_script, '--require', '.', '--require', 'fs', '--', '--tree', tree_file,'--burnin',str(burnin), '--samples', str(samples),'--lag',str(lag),'--trueLambda',str(trueLambda),'--trueMu',str(trueMu)])
	errLambda = float(out[-3].split()[-1])
	errMu = float(out[-2].split()[-1])
	print(str(trialno)+',MCMC,lag,'+str(lag)+','+str(errLambda)+','+str(errMu)+','+str(time))

#---- SMC---

samplesvals = [100, 300, 1000]
rejuvSteps = 1

for samples in samplesvals:
	out, time = get_output_and_time(['webppl', smc_script, '--require', '.', '--require', 'fs', '--', '--tree', tree_file, '--samples', str(samples),'--rejuvSteps',str(rejuvSteps),'--trueLambda',str(trueLambda),'--trueMu',str(trueMu)])
	errLambda = float(out[-3].split()[-1])
	errMu = float(out[-2].split()[-1])
	print(str(trialno)+',SMC,samplesrejuv,'+str(samples)+','+str(errLambda)+','+str(errMu)+','+str(time))

samplesvals = [100, 300, 1000, 3000]
rejuvSteps = 0

for samples in samplesvals:
	out, time = get_output_and_time(['webppl', smc_script, '--require', '.', '--require', 'fs', '--', '--tree', tree_file, '--samples', str(samples),'--rejuvSteps',str(rejuvSteps),'--trueLambda',str(trueLambda),'--trueMu',str(trueMu)])
	errLambda = float(out[-3].split()[-1])
	errMu = float(out[-2].split()[-1])
	print(str(trialno)+',SMC,samplesnorejuv,'+str(samples)+','+str(errLambda)+','+str(errMu)+','+str(time))





