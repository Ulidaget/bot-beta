FROM python:3.11
EXPOSE 8086
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
ENTRYPOINT [ "streamlit", "run", "agent.py", "--server.port=8086", "--server.address=0.0.0.0" ]