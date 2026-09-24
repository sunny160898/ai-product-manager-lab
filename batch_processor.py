### 3. Core Python Implementation (`batch_processor.py`)

```python
import asyncio
import logging
import json
from openai import AsyncOpenAI

# (import asyncio
import logging
import json
from openai import AsyncOpenAI

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class AsyncLLMBatchEngine:
    def __init__(self, model_name: str = "gpt-4o-mini", max_concurrent: int = 10):
        self.client = AsyncOpenAI()
        self.model_name = model_name
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def process_single_prompt(self, task_id: int, prompt: str, retries: int = 3) -> dict:
        async with self.semaphore:
            delay = 1.0
            for attempt in range(retries):
                try:
                    response = await self.client.chat.completions.create(
                        model=self.model_name,
                        messages=[{"role": "user", "content": prompt}]
                    )
                    return {
                        "task_id": task_id,
                        "status": "success",
                        "output": response.choices[0].message.content
                    }
                except Exception as e:
                    logging.warning(f"Task {task_id} failed on attempt {attempt+1}: {e}")
                    if attempt == retries - 1:
                        return {"task_id": task_id, "status": "failed", "error": str(e)}
                    await asyncio.sleep(delay)
                    delay *= 2  # Exponential backoff

    async def run_batch(self, prompts: list[str]) -> list[dict]:
        tasks = [self.process_single_prompt(i, prompt) for i, prompt in enumerate(prompts)]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    sample_prompts = [
        "Explain quantum computing in one sentence.",
        "What is token bucket rate limiting?",
        "Define vector embeddings simply."
    ]
    engine = AsyncLLMBatchEngine(max_concurrent=2)
    loop = asyncio.get_event_loop()
    batch_results = loop.run_until_complete(engine.run_batch(sample_prompts))
    
    print(json.dumps(batch_results, indent=2)))
