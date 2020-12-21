import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('results/benchmark_burnin')
df.columns = ['run','algorithm','crit','burnin','err_lbda','err_mu','time']
df['err_lbda'] = df['err_lbda'].abs()
f,ax=plt.subplots()
ax.set(xscale='log')
sns.lineplot(data=df,x='burnin',y='err_lbda',ax=ax)
plt.savefig('results/burnin_err_lbda.png')

f,ax=plt.subplots()
ax.set(xscale='log')
sns.lineplot(data=df,x='burnin',y='time',ax=ax)
plt.savefig('results/burnin_time.png')



df = pd.read_csv('results/benchmark_lag')
df.columns = ['run','algorithm','crit','lag','err_lbda','err_mu','time']
df['err_lbda'] = df['err_lbda'].abs()
f,ax=plt.subplots()
ax.set(xscale='log')
sns.lineplot(data=df,x='lag',y='err_lbda',ax=ax)
plt.savefig('results/lag_err_lbda.png')

f,ax=plt.subplots()
ax.set(xscale='log')
sns.lineplot(data=df,x='lag',y='time',ax=ax)
plt.savefig('results/lag_time.png')

df = pd.read_csv('results/benchmark_samplesrejuv')
df.columns = ['run','algorithm','crit','particles-rejuvenation','err_lbda','err_mu','time']
df['err_lbda'] = df['err_lbda'].abs()
f,ax=plt.subplots()
ax.set(xscale='log')
ax.set(xlabel='particles')
sns.lineplot(data=df,x='particles-rejuvenation',y='err_lbda',ax=ax)
plt.savefig('results/rejuv_err_lbda.png')


df = pd.read_csv('results/benchmark_samplesnorejuv')
df.columns = ['run','algorithm','crit','particles-no-rejuvenation','err_lbda','err_mu','time']
df['err_lbda'] = df['err_lbda'].abs()
#plt.figure()
sns.lineplot(data=df,x='particles-no-rejuvenation',y='err_lbda',ax=ax)
ax.set(xlabel='particles')
plt.savefig('results/bothrejuv_err_lbda.png')

#--time

df = pd.read_csv('results/benchmark_samplesrejuv')
df.columns = ['run','algorithm','crit','particles-rejuvenation','err_lbda','err_mu','time']
f,ax=plt.subplots()
ax.set(xscale='log')
ax.set(xlabel='particles')
sns.lineplot(data=df,x='particles-rejuvenation',y='time',ax=ax)
plt.savefig('results/rejuv_time.png')


df = pd.read_csv('results/benchmark_samplesnorejuv')
df.columns = ['run','algorithm','crit','particles-no-rejuvenation','err_lbda','err_mu','time']
#plt.figure()
sns.lineplot(data=df,x='particles-no-rejuvenation',y='time',ax=ax)
ax.set(xlabel='particles')
plt.savefig('results/bothrejuv_time.png')

df = pd.read_csv('results/benchmark_all')

df.columns = ['run','algorithm','crit','value','err_lbda','err_mu','time']
df['err_lbda'] = df['err_lbda'].abs()

f,ax=plt.subplots()
ax.set(xscale='log')
ax.set(yscale='log')
sns.scatterplot(data=df,x='time',y='err_lbda',hue='algorithm',ax=ax)
plt.savefig('results/time_err_lbda.png')

