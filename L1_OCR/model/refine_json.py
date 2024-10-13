import cv2
from functools import cmp_to_key
import numpy as np
import PIL
import json
import sys
from braille_utils import postprocess_modified as postprocess


def lines_to_brl(lines):
    '''
    :param lines: list of Line (returned by boxes_to_lines or text_to_lines)
    :return: text as string
    '''
    out_brl = []
    for ln in lines:
        if ln.has_space_before:
            out_brl.append('')
        s = ''
        for ch in ln.chars:
            s += ' ' * ch.spaces_before + chr(ch.label + 0x2800)
        out_brl.append(s)
    return out_brl

def lines_to_list(lines):
    '''
    :param lines: list of Line (returned by boxes_to_lines or text_to_lines)
    :return: list of int
    '''
    out_list = []
    box_list = []
    for ln in lines:
        l = []
        for ch in ln.chars:
            for i in range(ch.spaces_before):
                l.append(0)
            l.append(ch.label)
        out_list.append(l)
    
        b = []
        for ch in ln.chars:
            # spaces before의 좌표를 특정하는 기능이 추가되어야 함
            for i in range(ch.spaces_before):
                b.append(0)
            b.append(ch.original_box)
        box_list.append(b)
    return out_list, box_list


def main(annotation_path):
    # annotations = json.load(open(id + ".json"))
    annotations = json.load(open(annotation_path))
    
    boxes = annotations["prediction"]["boxes"]
    labels = annotations["prediction"]["labels"]
    
    lines = postprocess.boxes_to_lines(boxes, labels, lang='RU')
    result_lines, result_boxes = lines_to_list(lines)
    brl = lines_to_brl(lines)
    
    annotations["prediction"]["lines"] = result_lines
    annotations["prediction"]["boxes_by_lines"] = result_boxes
    annotations["prediction"]["brl"] = brl
    
    
    with open(annotation_path, "w", encoding='utf-8') as f:
        json.dump(annotations, f, indent=4, ensure_ascii=False) 
    
    return annotations
        
        
if __name__ == "__main__":
    annotation_path = sys.argv[1]
    main(annotation_path)