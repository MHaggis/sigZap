# SigZap

![SigZap Logo](assets/images/logo.png)


SigZap is a Streamlit application designed to facilitate the search across multiple network signature sets at once. 
It provides a user-friendly interface to quickly and efficiently query different rule sets. 
The application connects to a SQLite database where the rule sets are stored and allows the user to select a specific category 
and enter a search term. The results are then displayed in a clear and readable format. 
This tool is particularly useful for network administrators and security analysts who need to quickly identify and analyze 
network traffic patterns and potential security threats.

## How to use SigZap

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/mhaggis/SigZap.git
   ```
2. Navigate to the cloned directory.
   ```
   cd SigZap
   ```
3. Install the required Python packages.
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit application.
   ```
   streamlit run sigZap.py
   ```
5. Open your web browser and go to `http://localhost:8501` to view the application.

# Future

- [ ] Ability to update rules via workflow on Cron
- [ ] Update rules from App
- [ ] Create Snort rules from the App

(these 3 additions are mostly done, just testing before release)