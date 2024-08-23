# Fake Follower Detection Script

## Overview

This repository contains a Python script designed to identify and flag potential fake followers in social media profiles. The script analyzes key metrics like engagement rate, follower/following ratio, and account activity to determine the likelihood of an account being fake or inactive.

## Features

- **Engagement Rate Analysis**: Calculates the engagement rate based on the number of likes and comments relative to the follower count.
- **Follower/Following Ratio**: Assesses the balance between followers and following to detect abnormal patterns.
- **Threshold-Based Flagging**: Flags accounts that fall below specified thresholds for engagement, followers, and other criteria.
- **CSV Report Generation**: Outputs a list of potential fake followers to a CSV file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/fake-follower-detection.git
   cd fake-follower-detection
   ```

2. **Install dependencies**:
   The script relies on Python's `pandas` library. Install it using pip:
   ```bash
   pip install pandas
   ```

## Usage

1. **Prepare Data**:
   Replace the sample data in the script with your actual social media profile data. The data should include the following columns:
   - `username`: The handle or username of the account.
   - `followers`: Number of followers the account has.
   - `following`: Number of accounts the user is following.
   - `posts`: Number of posts made by the account.
   - `likes`: Total number of likes received on posts.
   - `comments`: Total number of comments received on posts.

2. **Run the Script**:
   Execute the script to analyze the data and flag potential fake followers:
   ```bash
   python fake_follower_detection.py
   ```

3. **View the Report**:
   The script will print the potential fake followers to the console and save them to a CSV file named `potential_fake_followers.csv`.

## Logic and Thresholds

The script uses the following logic and thresholds to flag potential fake followers:

- **Engagement Rate**:
  - Formula: `(likes + comments) / followers`
  - Threshold: Accounts with an engagement rate below 1% are flagged.

- **Follower/Following Ratio**:
  - Formula: `followers / following`
  - Threshold: Accounts with a ratio below `1.5` are flagged.

- **Follower Count**:
  - Threshold: Accounts with fewer than `500` followers are flagged.

- **Following Count**:
  - Threshold: Accounts following more than `1000` users are flagged.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Dipti Ranjan at diptiranjanpati100@gmail.com
