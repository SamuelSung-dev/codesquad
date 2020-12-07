# 코드스쿼드 마스터즈 코스 테스트

## branch step-2 - 평면 큐브 구현하기

- Cube2d 객체

  - 현재 상태인 cube 와 큐브 상태를 보여주는 show(), 큐브를 움직이는 함수들로 구현

- main.py
  - 입력을 받아 list로 정리
    - 입력 문자가 U, R, L, B 인 경우에만 그 다음 ' 을 확인하여 actions list에 저장
    - 입력 문자가 Q인 경우는 다음문자 확인 안함
  - actions list에 맞는 행동을 실행
