#### Dependencies
- WebPPL
- python 3.x
- dendropy (I used version 4.4.0)
- nexus2phyjson

The scripts will probably not work on Windows due to '/' vs. '\' difference in path conventions.

#### Preparing data

Before running the python scripts, make sure you update the path to your nexus2phyjson installation in both scripts.

To generate synthetic data, run

``
python python/generate_trees.py
``

To convert the empirical data to phyjson, put the *tre files in ``data/empirical`` and run

``
python python/preprocess_real_trees.py
``

To run the benchmarks presented in the talk, run

``
python python/benchmark_on_tree.py
''
#### Running the main program

To run MCMC (Metropolis-Hastings), type

``
webppl bdInferMCMC.wppl --require . --require fs -- --tree path/to/phyjson/file [--burnin burnin --lag lag --samples nsamples]
``
Where:
- `burnin' is the number of initial MCMC steps discarded as burn-in period  (default: 5000)
- `lag' is the number of MCMC steps discarded between any two consecutive samples collected (default: 100)
- `nsamples' is the total number of samples collected (default: 300)

To run SMC, type
``
webppl bdInferSMCUnsorted.wppl --require . --require fs -- --tree path/to/phyjson/file [--rejuvSteps steps --samples nsamples]
``

Where:
- `rejuvSteps' is the number of rejuvenation steps at each iteratiion (default: 0, in all experiments rejuvSteps was at most 1)
- `nsamples' is the number of particles (default: 300)

