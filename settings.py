BASE_DIR = ".\\"
BASE_IMAGES256_DIR = BASE_DIR + "\\data_preprocessed_images\\"
BASE_TRAIN_SEGMENT_DIR = BASE_DIR + "\\data_segmenter_train\\"
PATIENT_PRED_DIR = BASE_DIR + "\\data_patient_predictions\\"

MODEL_NAME = "model_v1"
TRAIN_EPOCHS = 30
FOLD_COUNT = 6
TARGET_SIZE = 256
CROP_INDENT_X = 32
TARGET_CROP = 184
CROP_INDENT_Y = 32 - ((TARGET_CROP - 160) / 2) # 172 high on top.. , 279
CROP_SIZE = 16
