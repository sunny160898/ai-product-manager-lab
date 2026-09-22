import pandas as pd

# 1. Load the AI query logs CSV file into a Pandas DataFrame
# (Think of a DataFrame like a code-powered Excel spreadsheet)
df = pd.read_csv('ai_query_logs.csv')

print("--- RAW DATA PREVIEW ---")
print(df.head()) # Shows the first 5 rows

# 2. Filter the data: Find all queries where the AI failed (is_successful == False)
failed_queries = df[df['is_successful'] == False]
print(f"\nTotal failed queries: {len(failed_queries)}")

# 3. Calculate metrics: What is the average latency of successful queries?
successful_queries = df[df['is_successful'] == True]
avg_success_latency = successful_queries['latency_ms'].mean()

print(f"Average latency for successful queries: {avg_success_latency:.2f} ms")

# 4. Group by analysis: Total tokens consumed per user
tokens_per_user = df.groupby('user_id')['tokens_used'].sum().reset_index()
print("\n--- TOTAL TOKENS PER USER ---")
print(tokens_per_user)
