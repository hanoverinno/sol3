This is the source code for the 3rd prize solution to the [Second National Data Science Bowl](https://www.kaggle.com/c/second-annual-data-science-bowl) hosted by Kaggle.com. For documenation about the approach look [here](http://juliandewit.github.io/kaggle-ndsb/)

#### Dependencies & data
I used the anaconda default distribution with all the libraries that came with it.
Next to this I used opencv(cv2), pydicom and MxNet (20151228 but later version will most probably be fine).
For detailed windows 64 installation instructions look [here]().

The dicom data needs to be downloaded from [Kaggle](https://www.kaggle.com/c/second-annual-data-science-bowl/data) and must be but in the data_kaggle/train /validate and /test folders.

#### Adjust settings


#### Run the solution 
1. python step0_preprocess.py<br> As a result the /data_preprocessed_images folder will contain preprocessed images and some extra csv files will be generated in the root folder.
2. python step1_train_segmenter.py<br>As a result you will have (a) trained model(s) in the root folder
3. python step2_predict_volumes.py<br>As a result you will have a csv containing raw predictions for all 1140 patients. Also the data_patient_predictions will contain all generated overlays and csv data per patient for debugging.
4. python step3_calibrate.py<br>As a result you will have a csv file containing all the calibrated predictions
5. python step4_submission.py<br>As a result the /data_submission_files folder will contain a submission file.
 
#### Hardware
The solution should be gentle on the GPU because of the small batchsize. Any recent GPU supported by MxNet should do the job I figure.




