FROM python:3.9.1
RUN apt update && apt install -y --no-install-recommends \
        libgdal-dev \
        gcc && \
rm -rf /var/lib/apt/lists/*
RUN mkdir -p /sst
RUN mkdir -p /sentinel
COPY req.txt .
RUN pip install -r req.txt
COPY Collections_Sentinel2_SST_Data.py .
CMD ["python3", "./Collections_Sentinel2_SST_Data.py"]