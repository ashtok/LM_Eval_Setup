# LM_Eval_Setup: Resource-Sensitive Semantic Benchmarking for LLMs

A comprehensive benchmarking framework for evaluating Large Language Models on custom-designed semantic understanding tasks, built on top of [EleutherAI's lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).

**Authors:** Pallabi Pathak & Ashutosh Mahajan  
**Institution:** NLP Group, University of Würzburg (M.Sc. Computer Science, 2025)

---

## Overview

This project evaluates how well modern LLMs understand core semantic relationships — analogies, definitions, hypernymy, and meronymy — across languages with varying resource levels (high, medium, low, and monolingual English). The benchmark is designed to expose resource sensitivity: how model performance degrades as training data for the target language decreases.

All tasks use a **multiple-choice format** with 4 options, evaluated under 5-shot learning by default. Metrics are accuracy (raw) and normalized accuracy (penalizes confidence calibration).

---

## Repository Structure

```
LM_Eval_Setup/
├── lm-evaluation-harness/              # EleutherAI harness (modified)
│   ├── lm_eval/
│   │   └── tasks/
│   │       └── NLP_JMU/               # Custom task definitions (128 MB)
│   │           ├── Analogies/
│   │           │   ├── analogies_{all,high,medium,low,mono}.yaml
│   │           │   └── semantic_analogy_questions_{all,en_to_high,...}.json
│   │           ├── Gloss/
│   │           │   ├── gloss_{all,high,medium,low,mono}.yaml
│   │           │   └── gloss_questions_{all,en_to_high,...}.json
│   │           ├── Hypernymy/
│   │           │   ├── hypernymy_{all,high,medium,low,mono}.yaml
│   │           │   └── hypernymy_questions_{all,en_to_high,...}.json
│   │           ├── Meronymy/
│   │           │   ├── meronymy_{all,high,medium,low,mono}.yaml
│   │           │   └── meronymy_questions_{all,en_to_high,...}.json
│   │           └── MSI_Benchmark/
│   │               ├── msi_{hr,md,lr}_custom_task.yaml
│   │               └── msi_benchmark_{high,medium,low}_resource.jsonl
│   └── results/                        # Evaluation outputs (30 MB)
│       ├── google__gemma-3-1b-it/
│       ├── google__gemma-7b-it/
│       ├── Qwen__Qwen3-8B/
│       ├── mistralai__Mistral-7B-Instruct-v0.3/
│       ├── meta-llama__Llama-3.1-8B-Instruct/
│       └── google__mt5-large/
├── Analysis/
│   └── analyser.py                     # Error analysis: incorrect synset extraction
├── check_yaml.py                       # YAML config validation utility
├── hypernymy_questions.json            # Sample hypernymy data
├── requirements.txt                    # Python dependencies
└── Commands.txt                        # Full log of completed evaluation runs
```

---

## Tasks

### 1. Semantic Analogies (`analogies_*`)

Tests analogical reasoning of the form **A : B :: C : ?**. Questions are cross-lingual (English → target language) drawn from multilingual WordNet synset pairs.

- **Dataset size:** ~212,500 questions (combined)
- **Metrics:** `acc`, `acc_norm`

### 2. Gloss Understanding (`gloss_*`)

Given a word in a target language, the model selects the correct English definition (gloss) from 4 options. Tests whether models can bridge word-meaning relationships across languages.

- **Dataset size:** ~25,000–60,000 questions depending on variant
- **Metrics:** `acc`, `acc_norm`

### 3. Hypernymy (`hypernymy_*`)

Given a word pair, the model identifies which option correctly expresses the "is-a" (hypernymy) relationship. Tests hierarchical semantic understanding.

- **Dataset size:** ~610,000 questions (combined)
- **Metrics:** `acc`, `acc_norm`

### 4. Meronymy (`meronymy_*`)

Tests part-whole relationship detection. Given a word, the model identifies its correct meronym or holonym from 4 options.

- **Dataset size:** ~610,000 questions (combined)
- **Metrics:** `acc`, `acc_norm`

### 5. Multi-Scale Inference Benchmark (`msi_*`)

A cross-resource evaluation task that combines multiple semantic inference subtypes across resource strata. Uses F1 as the primary metric rather than raw accuracy.

- **Variants:** `msi_hr_custom_task` (high), `msi_md_custom_task` (medium), `msi_lr_custom_task` (low)
- **Metrics:** `acc`, `f1`, `precision`, `recall`

---

## Resource Strata

Each task (except MSI) is available in five variants:

| Variant | Suffix | Description |
|---------|--------|-------------|
| Combined | `_all` | All resource levels merged |
| High-resource | `_high` | Languages with rich training data (e.g., German, French, Spanish) |
| Medium-resource | `_medium` | Languages with moderate data (e.g., Turkish, Dutch) |
| Low-resource | `_low` | Languages with sparse data (e.g., Welsh, Basque) |
| Monolingual | `_mono` | English-only questions |

---

## Task Configuration Format

Each task is defined via a YAML file using the lm-evaluation-harness format:

```yaml
task: hypernymy_all
dataset_path: json
dataset_kwargs:
  data_files: "./lm_eval/tasks/NLP_JMU/hypernymy_questions_all.json"
output_type: multiple_choice
test_split: train
num_fewshot: 5
doc_to_text: "{{prompt}}"
doc_to_target: "{{answer_index}}"
doc_to_choice: "{{options}}"
metric_list:
  - metric: acc
    aggregation: mean
    higher_is_better: true
  - metric: acc_norm
    aggregation: mean
    higher_is_better: true
```

Each JSON data entry follows this schema:

```json
{
  "id": "hypernymy_en_to_de_0001",
  "prompt": "Which word is a hypernym of 'Hund' (dog)?",
  "options": ["Tier", "Katze", "Haus", "Baum"],
  "answer_index": 0,
  "metadata": {
    "language_pair": "en_to_de",
    "resource_level": "high",
    "synset_id": "dog.n.01"
  }
}
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ashtok/LM_Eval_Setup.git
cd LM_Eval_Setup/lm-evaluation-harness
```

### 2. Install Dependencies

```bash
pip install -e .
pip install -r ../requirements.txt
```

Key dependencies:

| Package | Version |
|---------|---------|
| transformers | 4.53.1 |
| torch | 2.7.1 |
| datasets | 4.0.0 |
| accelerate | 1.8.1 |
| peft | 0.16.0 |
| evaluate | 0.4.4 |
| scikit-learn | 1.7.0 |
| pandas | 2.3.1 |

### 3. Verify Task Discovery

```bash
lm_eval --tasks list --include_path ./lm_eval/tasks/NLP_JMU
```

You should see all `analogies_*`, `gloss_*`, `hypernymy_*`, `meronymy_*`, and `msi_*` tasks listed.

---

## Running Evaluations

### Basic Command Structure

```bash
lm_eval --model hf \
        --model_args pretrained=<HF_MODEL_ID> \
        --tasks <TASK_LIST> \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size <N> \
        --output_path ./results/
```

### Example: Evaluate a Single Model on All Tasks

```bash
lm_eval --model hf \
        --model_args pretrained=meta-llama/Llama-3.1-8B-Instruct \
        --tasks analogies_all,hypernymy_all,meronymy_all,gloss_all \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 4 \
        --output_path ./results/
```

### Example: Resource-Stratified Evaluation

```bash
lm_eval --model hf \
        --model_args pretrained=Qwen/Qwen3-8B \
        --tasks hypernymy_high,hypernymy_medium,hypernymy_low,hypernymy_mono \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 2 \
        --output_path ./results/
```

### Example: MSI Benchmark

```bash
lm_eval --model hf \
        --model_args pretrained=mistralai/Mistral-7B-Instruct-v0.3 \
        --tasks msi_hr_custom_task,msi_md_custom_task,msi_lr_custom_task \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 4 \
        --output_path ./results/
```

### Example: With Detailed Sample Logging

```bash
lm_eval --model hf \
        --model_args pretrained=meta-llama/Llama-3.1-8B-Instruct \
        --tasks hypernymy_mono,meronymy_mono \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 4 \
        --output_path ./results/ \
        --write_out \
        --log_samples
```

### Recommended Batch Sizes by Model Size

| Model Size | Recommended `--batch_size` |
|------------|---------------------------|
| ~1B parameters | 8–16 |
| ~3B parameters | 4–8 |
| ~7–8B parameters | 2–4 |
| >10B parameters | 1–2 |

### Using SafeTensors (for encoder-decoder models like mT5)

```bash
lm_eval --model hf \
        --model_args pretrained=google/mt5-large,use_safetensors=True \
        --tasks analogies_all,hypernymy_all,meronymy_all \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 2 \
        --output_path ./results/
```

---

## Evaluation Results

All results are stored in `lm-evaluation-harness/results/<model_name>/` as timestamped JSON files. The table below summarizes accuracy (`acc`) on the combined (`_all`) variants.

### Accuracy on Combined Task Variants (5-shot)

| Model | Parameters | Analogies | Hypernymy | Meronymy | Gloss |
|-------|-----------|-----------|-----------|----------|-------|
| **Meta LLaMA-3.1-8B-Instruct** | 8B | **0.496** | **0.701** | **0.592** | — |
| **Qwen3-8B** | 8B | 0.461 | 0.666 | 0.543 | **0.703** |
| **Mistral-7B-Instruct-v0.3** | 7B | 0.446 | 0.618 | 0.503 | — |
| **Gemma-7B-it** | 7B | 0.376 | 0.486 | 0.361 | 0.652 |
| **Gemma-3-1B-it** | 3.1B | 0.371 | 0.461 | 0.402 | 0.493 |
| **mT5-large** | 1.2B | 0.274 | 0.386 | 0.319 | — |

> Random chance baseline for 4-choice multiple choice is **0.25**. All models exceed this baseline.

### Key Observations

- **LLaMA-3.1-8B** achieves the best performance on relational tasks (hypernymy, meronymy, analogies), suggesting stronger cross-lingual structural understanding.
- **Qwen3-8B** leads on gloss understanding, indicating stronger multilingual definitional knowledge.
- **mT5-large** (encoder-decoder architecture) consistently underperforms decoder-only models despite being trained multilingually, likely due to the generative multiple-choice format.
- All 7–8B instruction-tuned decoder models significantly outperform the 3.1B Gemma model, confirming a scale effect.
- Resource level has a measurable impact: all models show higher accuracy on `_mono` (English) and `_high` variants compared to `_low`, confirming resource sensitivity.

---

## Analysis Tools

### analyser.py

Located in `Analysis/analyser.py`. Post-evaluation error analysis script that:

1. Reads per-sample JSONL prediction files from evaluation runs
2. Extracts synset IDs for all incorrect predictions
3. Computes the intersection of failed synsets across multiple models
4. Outputs consistently hard semantic concepts to `incorrect_synsets.txt`

**Usage:**

```bash
cd Analysis/
python analyser.py
```

**Output files:**
- `incorrect_synsets.txt` — Synset IDs that all evaluated models failed on
- `correct_synsets.txt` — Synset IDs that all models answered correctly

This enables identifying which semantic concepts are universally difficult, regardless of model architecture or scale.

### check_yaml.py

Simple YAML validation utility for task configuration files. Run before adding new tasks to catch syntax errors:

```bash
python check_yaml.py
```

---

## Results File Format

Each evaluation produces a JSON file with the following structure:

```json
{
  "results": {
    "hypernymy_high": {
      "alias": "hypernymy_high",
      "acc,none": 0.436,
      "acc_stderr,none": 0.0071,
      "acc_norm,none": 0.365,
      "acc_norm_stderr,none": 0.0069
    }
  },
  "configs": {
    "hypernymy_high": { }
  },
  "versions": { },
  "n-shot": 5,
  "date": "2025-07-14T..."
}
```

When `--log_samples` is enabled, a corresponding `.jsonl` file is saved with per-instance predictions, including the model's chosen option and the correct answer — used as input for `analyser.py`.

---

## Adding New Tasks

To add a custom task:

1. Prepare your dataset as a JSON file with fields: `id`, `prompt`, `options` (list of 4), `answer_index`, `metadata`.
2. Create a YAML config file in `lm_eval/tasks/NLP_JMU/` following the format above.
3. Validate the YAML: `python check_yaml.py`
4. Run a quick sanity check with `--limit 10` to verify the task loads correctly:

```bash
lm_eval --model hf \
        --model_args pretrained=google/gemma-3-1b-it \
        --tasks your_new_task \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 4 \
        --limit 10
```

---

## Citation

If you use this benchmark in your research, please cite:

```bibtex
@misc{PathakMahajan2025NLPBenchmark,
  author       = {Pallabi Pathak and Ashutosh Mahajan},
  title        = {LM\_Eval\_Setup: Resource-Sensitive Semantic Benchmarking for Large Language Models},
  year         = {2025},
  institution  = {University of W\"{u}rzburg, NLP Group},
  url          = {https://github.com/ashtok/LM_Eval_Setup}
}
```

---

## Acknowledgements

This project builds on [EleutherAI's lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness). Task data is derived from multilingual WordNet and related lexical databases.

Special thanks to the **NLP Group, University of Würzburg** for guidance and computational resources.
