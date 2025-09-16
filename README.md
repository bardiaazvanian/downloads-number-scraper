MakerWorld Download Counter Automation
A Python automation script that extracts download counts from MakerWorld.com using Selenium with persistent browser sessions.

Features
Automated Data Extraction: Retrieves download counts from MakerWorld models

Persistent Sessions: Uses Chrome user profiles to maintain login sessions

Cloudflare Bypass: Implements anti-detection measures to bypass Cloudflare protection

Cross-Platform: Works on Windows, Linux, and cloud environments (Appwrite ready)

Installation
Clone the repository:

bash
git clone https://github.com/your-username/makerworld-download-counter.git
cd makerworld-download-counter
Install dependencies:

bash
pip install -r requirements.txt
Install ChromeDriver (automatically handled by undetected-chromedriver)

Usage
First-Time Setup (Manual Login Required)
bash
python initial_login.py
Follow the prompts to manually log in to MakerWorld and Google in the browser window that opens.

Regular Usage
bash
python main.py
For Specific Model URL
bash
python main.py --url "https://makerworld.com/en/models/your-model-id"
Configuration
The script uses:

undetected-chromedriver for stealth browsing

Persistent Chrome profile in ./chrome_profile/

Automatic session management

Headless mode support for server environments

Docker Support
bash
docker build -t makerworld-scraper .
docker run -v $(pwd)/chrome_profile:/app/chrome_profile makerworld-scraper
Appwrite Deployment
Create Appwrite function

Add environment variables if needed

Mount volume for chrome_profile persistence

Set up scheduled execution

File Structure
text
├── main.py                 # Main automation script
├── initial_login.py        # First-time setup script
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── chrome_profile/        # Chrome session storage (auto-created)
└── README.md              # This file
Requirements
Python 3.9+

Google Chrome

ChromeDriver (auto-installed)

Required packages in requirements.txt

Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Create a Pull Request

License
MIT License - see LICENSE file for details

Disclaimer
This project is for educational purposes only. Ensure compliance with MakerWorld's Terms of Service and robots.txt guidelines.
