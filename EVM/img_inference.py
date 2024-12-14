# Python script to perform inferencing on a single image.

from tflite_runtime.interpreter import Interpreter as tfl
from tflite_runtime.interpreter import load_delegate
import numpy as np
import cv2

# Path to the TFLite model and the artifacts folder
path_to_artifacts = 'zero_dce_model/artifacts'
path_to_model = 'zero_dce_model/model/zero_dce_model.tflite'

# Path to input and output image
input_image_path = 'image.jpg'
output_image_path = 'image_enhanced.jpg'

# Load the TIDL delegate
tidl_delegate_path = '/usr/lib/libtidl_tfl_delegate.so'
tidl_options = {"artifacts_folder": path_to_artifacts, "debug_level": 0,}
tidl_delegate = load_delegate(tidl_delegate_path, options=tidl_options)

# Read the input image
input_image = cv2.imread(input_image_path)

# Load the TFLite model and allocate tensors
interpret = tfl(model_path=path_to_model,experimental_delegates=[tidl_delegate])
interpret.allocate_tensors()
input_details = interpret.get_input_details()
output_details = interpret.get_output_details()

# Perform inferencing on the input image
input_image = cv2.resize(input_image, (600, 400))
input_data = np.array(input_image).astype(np.float32) / 255
input_data = np.expand_dims(input_data, axis=0) 
interpret.set_tensor(input_details[0]['index'], input_data)
interpret.invoke()
output_data = interpret.get_tensor(output_details[0]['index'])
output_image_data = (output_data[0] * 255 * 255).clip(0, 255).astype(np.uint8)

# Save the output image
cv2.imwrite(output_image_path, output_image_data)
print ('Closing....')