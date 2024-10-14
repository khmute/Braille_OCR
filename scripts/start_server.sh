#!/bin/bash
cd /home/ubuntu/app
source venv/bin/activate

# 기존 프로세스 종료
if pgrep -f "flask run"; then pkill -f "flask run"; fi

# 애플리케이션 실행
nohup flask run --host=0.0.0.0 --port=80 &
