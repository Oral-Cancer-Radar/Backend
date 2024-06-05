import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define directories for training and validation data
train_dir = 'path/to/train'
val_dir = 'path/to/val'

# Image data generators with data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,asynca
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)