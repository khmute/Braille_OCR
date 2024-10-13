#!/usr/bin/env python
# coding: utf-8
"""
Local application for Angelina Braille Reader inference
"""
import os
from pathlib import Path
import PIL.Image

import L1_OCR.local_config as local_config
import L1_OCR.model.infer_retinanet_modified as infer_retinanet

def run_ocr(image_path):
    model_weights = 'model.t7'

    image = PIL.Image.open(image_path)
    
    recognizer = infer_retinanet.BrailleInference(
        params_fn=os.path.join(local_config.data_path, 'weights', 'param.txt'),
        model_weights_fn=os.path.join(local_config.data_path, 'weights', model_weights),
        create_script=None)

    uuid_int = recognizer.get_uuid()
    print('UUID: ' + str(uuid_int))
    
    results_dir = local_config.data_path
    
    recognizer.run_and_save(image, results_dir, target_stem=None,
                                        lang='RU', extra_info=None,
                                        draw_refined=recognizer.DRAW_NONE,
                                        remove_labeled_from_filename=False,
                                        find_orientation=False, # 90도 회전해서 올바른 방향 찾기
                                        align_results=True,
                                        process_2_sides=False,
                                        repeat_on_aligned=False,
                                        save_development_info=False)

    return recognizer.get_result()