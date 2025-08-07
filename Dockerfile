# 1. 경량 Python 베이스 이미지 사용
FROM python:3.11-slim

# 2. 시스템 패키지 및 Tesseract OCR 설치
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. 작업 디렉토리 설정
WORKDIR /app

# 4. Python 의존성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 애플리케이션 코드 복사
COPY . .

# 6. 포트 개방
EXPOSE 10000

# 7. Gunicorn을 통한 서버 실행
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
