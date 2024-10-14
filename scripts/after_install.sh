#!/bin/bash
# 일반 사용자 권한으로 실행됩니다.

cd /home/ubuntu/app

# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate

# pip 업그레이드
pip install --upgrade pip

# 의존성 설치
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
