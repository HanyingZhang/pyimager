
import sys
import os
import pytest
from pyimager.pyimager import *

input_path = "./tests/milad.jpg"
def test_circropper_output():
    img = Image.open(input_path).convert("RGB")
    imgArray_1 = np.array(img)
    imgArray_2 = circropper(input_path, "result.png", 0)
    assert imgArray_1.shape[0] == imgArray_2.shape[0] 
    assert imgArray_1.shape[1] == imgArray_2.shape[1] 
    assert imgArray_1.shape[2] == imgArray_2.shape[2]-1

def test_circropper_input_value():
    try:
        imgArray_2 = circropper(input_path, "result.png", 1000)
    except ValueError:
        pass
    else:
        print("not error happens")

def test_stype():
    img_array = reducolor(0, 'tests/mandrill.jpg')
    color_n = len(np.unique(img_array.reshape(np.prod(img_array.shape[:2]),3), axis=0))
    assert color_n == 2, f'Should return two colors only, {color_n} colors are returned'
    img_array = reducolor(1, 'tests/mandrill.jpg')
    color_n = len(np.unique(img_array.reshape(np.prod(img_array.shape[:2]),3), axis=0))
    assert color_n == 8, f'Should return eight colors, {color_n} colors are returned'    
    try:
        img_array = reducolor(2, 'tests/mandrill.jpg')  
    except StyleException:
        pass
    else:
        assert False, f'Should not allow code other than 0 and 1 and raise StyleException'
    
