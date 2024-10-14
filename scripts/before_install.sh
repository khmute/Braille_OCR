#!/bin/bash
# 기존 애플리케이션 파일 삭제 또는 백업

# 패키지 목록 업데이트
apt-get update

# 필요한 패키지 설치
apt-get install -y python3-full python3-pip python3-venv

# 현재 사용자에게 /home/ubuntu/app 디렉토리에 대한 소유권 부여
chown -R ubuntu:ubuntu /home/ubuntu/app
