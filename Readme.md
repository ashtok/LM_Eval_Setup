# LM_Eval_Setup: Benchmarking Custom NLP Tasks

A comprehensive benchmarking framework for evaluating Large Language Models (LLMs) on custom-designed semantic evaluation tasks, built on top of [EleutherAI's lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).

## 🎯 Overview

This repository provides tools and datasets for analyzing LLM performance across five key semantic understanding tasks:
- **Semantic Analogies** - Testing analogical reasoning capabilities
- **Gloss Understanding** - Matching words to their definitions
- **Hypernymy** - Detecting hierarchical "is-a" relationships
- **Meronymy** - Identifying part-whole relationships
- **Multi-Scale Inference (MSI)** - Cross-resource benchmarking

The project was conducted as part of the M.Sc. in Computer Science under the NLP group at the **University of Würzburg**, focusing on resource sensitivity and semantic understanding across different model scales.

## 📁 Repository Structure

```
lm-evaluation-harness/lm_eval/tasks/NLP_JMU/
│
├── Analogies/
│   ├── analogies_all.yaml
│   ├── analogies_{high,low,medium,mono}.yaml
│   ├── semantic_analogy_questions_all.json
│   └── semantic_analogy_questions_en_to_{high,low,medium}.json
│
├── Gloss/
│   ├── gloss_all.yaml
│   ├── gloss_{high,low,medium,mono}.yaml
│   ├── gloss_questions_all.json
│   ├── gloss_questions_en_to_{high,low,medium}.json
│   └── gloss_questions_monolingual_en.json
│
├── Hypernymy/
│   ├── hypernymy_all.yaml
│   ├── hypernymy_{high,low,medium,mono}.yaml
│   ├── hypernymy_questions_all.json
│   └── hypernymy_questions_en_to_{high,low,medium}.json
│
├── Meronymy/
│   ├── meronymy_all.yaml
│   ├── meronymy_{high,low,medium,mono}.yaml
│   ├── meronymy_questions_all.json
│   └── meronymy_questions_en_to_{high,low,medium}.json
│
├── MSI_Benchmark/
│   ├── msi_benchmark_{high,medium,low}_resource.jsonl
│   ├── msi_{hr,md,lr}_custom_task.yaml
│
├── test.py
└── commands.txt
```

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ashtok/LM_Eval_Setup.git
cd LM_Eval_Setup/lm-evaluation-harness
```

### 2. Install Dependencies
```bash
pip install -e .
pip install torch transformers accelerate datasets
```

### 3. Verify Setup
All custom task definitions are pre-configured in `./lm_eval/tasks/NLP_JMU/`

## 🚀 Usage

### Basic Command Structure
```bash
lm_eval --model hf \
        --model_args pretrained=<MODEL_NAME> \
        --tasks <TASK_LIST> \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size <N> \
        --output_path ./results/
```

### Example: Full Evaluation
Evaluate Google Gemma-7B-it on all semantic tasks:

```bash
lm_eval --model hf \
        --model_args pretrained=google/gemma-7b-it \
        --tasks analogies_all,hypernymy_all,meronymy_all,gloss_all \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 4 \
        --output_path ./results/
```

### Task Variants
Each task supports multiple resource-level variants:
- `*_all` - Combined dataset
- `*_high` - High-resource languages
- `*_medium` - Medium-resource languages  
- `*_low` - Low-resource languages
- `*_mono` - Monolingual English

### MSI Benchmark
```bash
lm_eval --model hf \
        --model_args pretrained=<MODEL_NAME> \
        --tasks msi_hr_custom_task,msi_md_custom_task,msi_lr_custom_task \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --device cuda \
        --batch_size 8 \
        --output_path ./results/
```

## 📊 Tasks & Evaluation Metrics

| Task | Description | Variants | Metrics |
|------|-------------|----------|---------|
| **Analogies** | Semantic analogy solving (A:B :: C:?) | 5 variants | Accuracy |
| **Gloss** | Word-definition matching | 5 variants | Accuracy |
| **Hypernymy** | Hierarchical relationship detection | 5 variants | Accuracy |
| **Meronymy** | Part-whole relationship identification | 5 variants | Accuracy |
| **MSI Benchmark** | Multi-scale inference evaluation | 3 resource levels | F1, Precision, Recall |

## 🤖 Evaluated Models

The framework has been tested on:

- **Google Gemma** (3-1B-it, 7B-it)
- **Qwen3-8B**
- **Mistral-7B-Instruct-v0.3**
- **Google mT5-large**
- **Meta LLaMA-3.1-8B-Instruct**

## 📈 Output & Analysis

### Results Structure
- **JSON files**: Quantitative metrics in `./results/`
- **Detailed logs**: Enable with `--write_out --log_samples`
- **Per-model analysis**: Individual performance breakdowns
- **Resource sensitivity**: Cross-lingual performance comparison

### Analysis Capabilities
- Model performance comparison across semantic tasks
- Resource-level sensitivity analysis
- Task-specific error analysis
- Cross-model behavioral studies

## 🔄 Advanced Options

### Detailed Logging
```bash
# Enable comprehensive logging
lm_eval --model hf \
        --model_args pretrained=<MODEL_NAME> \
        --tasks <TASK_LIST> \
        --include_path ./lm_eval/tasks/NLP_JMU \
        --write_out \
        --log_samples \
        --output_path ./results/
```

### Custom Batch Sizes
- **Small models (1-3B)**: `--batch_size 8-16`
- **Medium models (7-8B)**: `--batch_size 4-8`
- **Large models (>10B)**: `--batch_size 1-4`

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Add your custom tasks following our YAML structure
4. Submit a pull request with detailed description

## 📄 Citation

If you use this benchmark in your research, please cite:

```bibtex
@misc{PathakMahajan2025NLPBenchmark,
  author       = {Pallabi Pathak and Ashutosh Mahajan},
  title        = {LM_Eval_Setup: Benchmarking Semantic and Resource-Sensitive NLP Tasks},
  year         = {2025},
  institution  = {University of Würzburg},
  url          = {https://github.com/ashtok/LM_Eval_Setup}
}
```

## 🙏 Acknowledgements

This work builds on the **lm-evaluation-harness** by [EleutherAI](https://github.com/EleutherAI/lm-evaluation-harness). 

Special thanks to the **NLP Group, University of Würzburg** for their guidance and support.

⭐ **Star this repository** if you find it useful for your NLP research!
