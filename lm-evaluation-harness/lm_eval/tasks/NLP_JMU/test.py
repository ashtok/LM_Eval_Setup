# test_task.py
import sys
sys.path.append('lm_eval/tasks/NLP_JMU')
from hypernymy import load_hypernymy_dataset

# Test loading
dataset = load_hypernymy_dataset()
print(f"Dataset loaded successfully! Test split has {len(dataset['test'])} examples")
print("First example:", dataset['test'][0])