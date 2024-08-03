    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    train_generator = train_datagen.flow_from_directory(
        'data/train',  # This is the target directory
        target_size=(150, 150),  # All images will be resized to 150x150
        batch_size=32,
        class_mode='binary'  # Since we use binary_crossentropy loss, we need binary labels
    )
    