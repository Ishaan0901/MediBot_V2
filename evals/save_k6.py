import json
import os

PATH = 'evals/results.json'

entry = {
    'run': 'k6',
    'config': {
        'chunk_size': 1000,
        'chunk_overlap': 250,
        'top_k': 6,
        'search_type': 'similarity',
        'embedding': 'BAAI/bge-small-en-v1.5'
    },
    'hit_rate_pct': 88.0,
    'hit_rate_n': 25,
    'missed_ids': [1, 3, 22]
}

if os.path.exists(PATH):
    with open(PATH, 'r', encoding='utf-8') as file:
        results = json.load(file)
else:
    results = []

results.append(entry)

with open(PATH, 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4)