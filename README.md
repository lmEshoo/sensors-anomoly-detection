# sensors-anomoly-detection

## Prerequisites
- [Docker install](https://medium.freecodecamp.org/the-easy-way-to-set-up-docker-on-a-raspberry-pi-7d24ced073ef)


## Usage

```bash
make
```

### Steps to configure One Class SVM:
1. Input the filename you wish to use on line 10. The default file should contain 11 channels of sensor data with some added anomalous data at the bottom.
*If using custom sensor data, make sure data is well formatted. No headers, comma separated, unix format, only integers or floats
2. If you wish to change to parameters of the model, change them on line 28 (nu default is .05, gamma default is .00005).
*nu is the percentage of outliers, gamma is the fiteness of the model to training data. Lower values create a more generalized model.
3. The remainder of the code will print information on tensors, labels, anomaly labels for training and test datasets, and eigenvalues for visualization to the console.
4. A 2D and 3D graph should appear (one may be behind the other)


## Output

All graphs will be located in `./outputs` folder