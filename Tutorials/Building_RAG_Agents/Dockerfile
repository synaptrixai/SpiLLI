# Use official Ubuntu 24.04 LTS image as base
FROM ubuntu:24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        python3.12 \
        python3.12-dev \
        python3-pip \
        software-properties-common \
        wget \
        zip jq unzip xvfb dos2unix

# Create working directory
WORKDIR /app

# Install venv support
RUN apt-get install -y python3.12-venv

# Create and activate virtualenv
RUN python3.12 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Google Chrome
RUN wget -qO- https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-keyring.gpg && \
    echo 'deb [signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver (matching the installed Chrome version)
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}') && \
    CHROMEDRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/latest-patch-versions-per-build.json" | \
    jq -r --arg ver "$CHROME_VERSION" '.[$ver]') && \
    wget -q https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf chromedriver-linux64.zip chromedriver-linux64

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install SpiLLI SDK (will need the .pem file at build time)
COPY SpiLLI.pem /root/.spilli/
RUN pip install --index-url https://well.synaptrix.org --upgrade SpiLLI

# Make sure all packages are properly installed
RUN ldconfig

# Copy entrypoint script for Jupyter setup
COPY entrypoint.sh ./
RUN dos2unix ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Expose ports 8080 and 8888 (Jupyter)
EXPOSE 8080
EXPOSE 8888

# Default command to start the container
CMD ["/app/entrypoint.sh"]