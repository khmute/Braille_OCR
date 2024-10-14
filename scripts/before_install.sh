#!/bin/bash
# 기존 애플리케이션 파일 삭제 또는 백업
rm -rf /home/ubuntu/app/*

apt-get update
apt-get install -y python3 python3-pip python3-venv