# 내장보듈 : 파이썬 설치 시 자동으로 설치되는 모듈

import pyautogui as pg
from math import pi, ceil as c
print(pi)
print(c(2.8))

# 외부 모듈 : 다른 사람이 만든 파이썬 파일 pip로 설치해서 사용
# pyautogui : 마우스 자동으로 움직이거나 키보드를 자동으로 입력하게 만드는 모듈


pg.moveTo(500, 500, duration=2)  # 화면 500 500 위치에 2초동안 이동해라
