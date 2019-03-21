steps to running code:
1) Ensure all imported libraries are installed on your machine (I used anaconda).
*ggplot did not come installed with my set up initially. Please install using command: conda install -c conda-forge ggplot
*pandas, sklearn.decomposition, matplotlib.pyplot, and mpl_toolkits.mplot3d are also used
2) Input the filename you wish to use on line 11. The default file should contain 11 channels of sensor data with some added anomalous data at the bottom.
*If using custom sensor data, make sure data is well formatted. No headers, comma separated, unix format, only integers or floats
3) If you wish to change to parameters of the model, change them on line 29 (nu default is .05, gamma default is .00005).
*nu is the percentage of outliers, gamma is the fiteness of the model to training data. Lower values create a more generalized model.
4) The remainder of the code will print information on tensors, labels, anomaly labels for training and test datasets, and eigenvalues for visualization.
5) A 2D graph should appear initially showing a approximation of the high dimensional data. Closing this will show a 3D visualization for the same data.