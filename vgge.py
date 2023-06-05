from keras.applications import VGG16
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

# Step 1: Load the pre-trained VGG16 model
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(64, 64, 3))

# Step 2: Remove the top layers
base_model.layers.pop()

# Step 3: Freeze the base layers
for layer in base_model.layers:
    layer.trainable = False

# Step 4: Add custom layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(5, activation='softmax')(x)  # Replace 'num_classes' with the number of your classes

# Step 5: Create the new model
model = Model(inputs=base_model.input, outputs=predictions)

# Step 6: Compile the model
model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Step 7: Data augmentation and preprocessing
train_datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'C:/Users/Admin/Desktop/Detection-systems/CNN_DAAT/Train',
        target_size=(64, 64),
        batch_size=8,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        'C:/Users/Admin/Desktop/Detection-systems/CNN_DAAT/Test',
        target_size=(64, 64),
        batch_size=8,
        class_mode='categorical')

# Step 8: Train the model
model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // 8,
        epochs=30,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // 8)

# Step 9: Evaluate the model
scores = model.evaluate(validation_generator, steps=validation_generator.samples // 8)
print("Accuracy: %.2f%%" % (scores[1] * 100))

model.save('unk_vgg_model.h5')