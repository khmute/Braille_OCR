#!/bin/bash
# 의존성 설치 등
cd /home/ubuntu/app

# 가상환경 생성 및 활성화 (선택 사항)
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
pip3 install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
