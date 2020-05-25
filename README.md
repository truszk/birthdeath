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

#### Running the main program

``
webppl bdInfer.wppl --require fs -- --tree path/to/phyjson/file
``

