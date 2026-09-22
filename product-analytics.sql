-- AI Feature Performance & Usage Analytics
-- Objective: Track query volume, high token usage, and average latency per user

SELECT 
    user_id,
    COUNT(query_id) AS total_queries,
    AVG(latency_ms) AS avg_latency_ms,
    SUM(tokens_used) AS total_tokens_consumed
FROM ai_queries
WHERE timestamp >= CURRENT_DATE - INTERVAL '30 days'
  AND tokens_used > 100
GROUP BY user_id
HAVING COUNT(query_id) > 5
ORDER BY total_tokens_consumed DESC;
