import json
import os

PATH = 'evals/results.json'

entry = {
    'run': 'baseline',
    'config': {
        'chunk_size': 1000,
        'chunk_overlap': 250,
        'top_k': 4,
        'search_type': 'similarity',
        'embedding': 'BAAI/bge-small-en-v1.5',
        'llm': 'openai/gpt-oss-20b',
        'judge': 'qwen/qwen3.8-27b'
    },
    'hit_rate_pct': 80.0,
    'hit_rate_n': 25,
    'correctness_pct': 88.0,
    'correctness_pct_hand_adjusted': 92.0,
    'correctness_n': 25,
    'refusal_pct': 100.0,
    'refusal_n': 5,
    'judge_hand_check': '9/10 match'
}

if os.path.exists(PATH):
    with open(PATH, 'r', encoding='utf-8') as file:
        results = json.load(file)
else:
    results = []

results.append(entry)

with open(PATH, 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4)