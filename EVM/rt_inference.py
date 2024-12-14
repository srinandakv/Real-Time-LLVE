# Python script to perform realtime inferencing on the AM62A EVM.

import gi 
gi.require_version('Gst', '1.0')
import gst_wrapper      # gst_wrapper.py should be in the same directory as this script
from tflite_runtime.interpreter import Interpreter as tfl
from tflite_runtime.interpreter import load_delegate
import numpy as np
import cv2

# Path to the TFLite model and the artifacts folder
path_to_model = 'zero_dce_model/model/zero_dce_model.tflite'
path_to_artfacts = 'zero_dce_model/artifacts'

# Set up the GStreamer pipeline for HDMI output and USB camera input
sink_str = 'appsrc format=GST_FORMAT_TIME is-live=true block=true do-timestamp=true name=sink_0 ! kmssink sync=false driver-name=tidss'
src_str  = 'v4l2src device=/dev/video0 name=src_0 ! videoconvert ! video/x-raw, width=640, height=480, format=BGR ! appsink'
gst_pipe = gst_wrapper.GstPipe(['videotestsrc ! fakesink'], sink_str)
sink_op = gst_pipe.get_sink('sink_0', 600, 400)
gst_pipe.start()

# Load the TIDL delegate
tidl_delegate_path = '/usr/lib/libtidl_tfl_delegate.so'
tidl_options = {"artifacts_folder": path_to_artfacts,"debug_level": 0,}
tidl_delegate = load_delegate(tidl_delegate_path, options=tidl_options)

# Open the USB camera
cap = cv2.VideoCapture(src_str, cv2.CAP_GSTREAMER)
if not cap.isOpened():
    print("Error: Could not open USB camera.")
    exit(1)

# Load the TFLite model and allocate tensors
interpret = tfl(model_path=path_to_model,experimental_delegates=[tidl_delegate])
interpret.allocate_tensors()
input_details = interpret.get_input_details()
output_details = interpret.get_output_details()

# Perform inferencing on the input frames
try:
    while cap.isOpened():
        ret, input_image = cap.read()
        if ret == True:
            input_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)
            input_image = cv2.resize(input_image, (600, 400))
            input_data = np.array(input_image).astype(np.float32) / 255.0
            input_data = np.expand_dims(input_data, axis=0) 
            interpret.set_tensor(input_details[0]['index'], input_data)
            interpret.invoke()
            output_data = interpret.get_tensor(output_details[0]['index'])
            output_image_data = (output_data[0] * 255 * 255).clip(0, 255).astype(np.uint8)
            gst_pipe.push_frame(output_image_data, sink_op)
except KeyboardInterrupt:
    print ('Stopped by user')
except Exception as e:
    print ('Stopped due to Error:', e)

# Release the resources
print ('Closing....') 
gst_pipe.send_eos(sink_op)
gst_pipe.free()