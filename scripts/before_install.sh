#!/bin/bash
# 기존 애플리케이션 파일 삭제 또는 백업
rm -rf /home/ubuntu/app/*

hooks:
    BeforeInstall:
    - location: scripts/before_install.sh
        runas: root
