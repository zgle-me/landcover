# Windows 10
conda env create --file environment.yml
* but the rectangle selection box didn't show in my case.

# EC2 Ubuntu C4
conda env create --file environment_precise.yml

OR: 
conda create -n MS_landcover python=3.6.9 

. activate MS_landcover

conda install -c conda-forge gdal
conda install -c conda-forge rasterio
conda install -c conda-forge shapely
conda install -c conda-forge rtree
conda install -c conda-forge fiona

pip install opencv-python==3.4.2.17
pip install opencv-contrib-python==3.4.2.17

conda install -c conda-forge proj4
conda install -c conda-forge numpy
conda install -c conda-forge matplotlib
conda install -c conda-forge scikit-learn
...