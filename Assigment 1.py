import pandas as pd

# Sample data (replace this with actual data)
data = {
    'username': ['user1', 'user2', 'user3', 'user4', 'user5'],
    'followers': [150, 5000, 100, 3000, 2000],
    'following': [100, 100, 50, 5000, 10],
    'posts': [50, 100, 5, 1000, 200],
    'likes': [10, 300, 0, 400, 50],
    'comments': [2, 50, 0, 50, 5],
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Criteria
FOLLOWER_THRESHOLD = 500
FOLLOWING_THRESHOLD = 1000
ENGAGEMENT_THRESHOLD = 0.01  # 1% engagement rate
FOLLOWER_FOLLOWING_RATIO_THRESHOLD = 1.5  # Following should not exceed followers by 50%

# Calculate Engagement Rate
df['engagement_rate'] = (df['likes'] + df['comments']) / df['followers']

# Calculate Follower/Following Ratio
df['follower_following_ratio'] = df['followers'] / df['following']

# Flagging criteria
df['is_potential_fake'] = (
    (df['followers'] < FOLLOWER_THRESHOLD) |
    (df['following'] > FOLLOWING_THRESHOLD) |
    (df['engagement_rate'] < ENGAGEMENT_THRESHOLD) |
    (df['follower_following_ratio'] < FOLLOWER_FOLLOWING_RATIO_THRESHOLD)
)

# Extract potential fake followers
potential_fake_followers = df[df['is_potential_fake']]

# Output the result
print("Potential Fake Followers:")
print(potential_fake_followers[['username', 'followers', 'following', 'engagement_rate', 'follower_following_ratio']])

# Save report to CSV
potential_fake_followers.to_csv('potential_fake_followers.csv', index=False)
