"""
此模块处理验证码图片，并使用tesseract识别验证码
"""

from PIL import Image
import subprocess
from pylab import *

def get_icode_from_img():
    #打开验证码
    img = Image.open("icode.png")
    #转为灰度图
    img = img.convert("L")
    #选择140为阀值进行过滤
    img = img.point(lambda x: 0 if x < 140 else 255)
    arr = array(img)
    #去掉边框
    arr[0] = 255
    arr[20] = 255
    for j in arr:
        j[0] = 255
        j[67] = 255
    img = Image.fromarray(arr)
    #保存图片去噪后的图片到本地，为tif格式
    img.save("icode.tif")
    #使用tesseract识别去噪后的图片上的数字
    subprocess.call(["tesseract", "icode.tif", "icode"])
    f = open("icode.txt")
    result = f.read()
    f.close()
    result = result.strip()
    result = result.replace(" ", "")
    return result
