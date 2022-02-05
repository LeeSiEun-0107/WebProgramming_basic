# import 패키지.모듈
# from unit import *
# from unit import item
# import unit.item
# import unit.character  # unit 패키지 안에 character 모듈
# import unit.monster

# unit.character.test()

# from 패키지 import 모듈
# item.test()

# from 패키지 import * : 모든 모듈 가져오기
# init 모듈 수정 후 사용
# from unit import *
# character.test()

# 패키지 자체를 import
# init 모듈 수정
import unit

unit.character.test()
unit.item.test()
unit.monster.test()
