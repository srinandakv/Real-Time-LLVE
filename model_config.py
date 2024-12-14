# Model configuration to compile the tflite model for C7x DL accelerator
# using edgeai_tidl_tools.

import os
import platform
from common.config_utils import AttrDict, create_model_config


models_base_path = '../../../models/public/'
if platform.machine() == 'aarch64':
    numImages = 100
else : 
    import requests
    import onnx
    numImages = 3

models_configs = {
    "zero_dce_model": create_model_config(
        source=AttrDict(
            model_url="",
        ),
        preprocess=AttrDict(
            resize=(600,400),
            crop=(600,400),
            data_layout="NHWC",
            resize_with_pad=False,
            reverse_channels=False,
        ),
        session=AttrDict(
            session_name="tflitert",
            model_path=os.path.join(models_base_path, "zero_dce_model.tflite"),
            input_mean=[0, 0, 0],
            input_scale=[1 / 255, 1 / 255, 1 / 255],
            input_optimization=True,
        ),
        task_type="custom",
        extra_info=AttrDict(num_images=numImages, num_classes=0),
    ),
}