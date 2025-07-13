Evaluation Commands
Google Gemma-3-1b-it
bash# Analogies evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks analogies_high,analogies_low,analogies_medium,analogies_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Hypernymy evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks hypernymy_high,hypernymy_low,hypernymy_medium,hypernymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Meronymy evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks meronymy_high,meronymy_low,meronymy_medium,meronymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All analogies tasks
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks analogies_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All hypernymy tasks
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks hypernymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All meronymy tasks
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks meronymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10
Qwen3-8B
bash# Analogies evaluation
lm_eval --model hf --model_args pretrained=Qwen/Qwen3-8B --tasks analogies_high,analogies_low,analogies_medium,analogies_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Hypernymy evaluation
lm_eval --model hf --model_args pretrained=Qwen/Qwen3-8B --tasks hypernymy_high,hypernymy_low,hypernymy_medium,hypernymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Meronymy evaluation
lm_eval --model hf --model_args pretrained=Qwen/Qwen3-8B --tasks meronymy_high,meronymy_low,meronymy_medium,meronymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All analogies tasks
lm_eval --model hf --model_args pretrained=Qwen/Qwen3-8B --tasks analogies_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All hypernymy tasks
lm_eval --model hf --model_args pretrained=Qwen/Qwen3-8B --tasks hypernymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All meronymy tasks
lm_eval --model hf --model_args pretrained=Qwen/Qwen3-8B --tasks meronymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10
Mistral-7B-Instruct-v0.3
bash# Analogies evaluation
lm_eval --model hf --model_args pretrained=mistralai/Mistral-7B-Instruct-v0.3 --tasks analogies_high,analogies_low,analogies_medium,analogies_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Hypernymy evaluation
lm_eval --model hf --model_args pretrained=mistralai/Mistral-7B-Instruct-v0.3 --tasks hypernymy_high,hypernymy_low,hypernymy_medium,hypernymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Meronymy evaluation
lm_eval --model hf --model_args pretrained=mistralai/Mistral-7B-Instruct-v0.3 --tasks meronymy_high,meronymy_low,meronymy_medium,meronymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All analogies tasks
lm_eval --model hf --model_args pretrained=mistralai/Mistral-7B-Instruct-v0.3 --tasks analogies_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All hypernymy tasks
lm_eval --model hf --model_args pretrained=mistralai/Mistral-7B-Instruct-v0.3 --tasks hypernymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All meronymy tasks
lm_eval --model hf --model_args pretrained=mistralai/Mistral-7B-Instruct-v0.3 --tasks meronymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10
Google mT5-XXL
bash# Analogies evaluation
lm_eval --model hf --model_args pretrained=google/mt5-xxl --tasks analogies_high,analogies_low,analogies_medium,analogies_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Hypernymy evaluation
lm_eval --model hf --model_args pretrained=google/mt5-xxl --tasks hypernymy_high,hypernymy_low,hypernymy_medium,hypernymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Meronymy evaluation
lm_eval --model hf --model_args pretrained=google/mt5-xxl --tasks meronymy_high,meronymy_low,meronymy_medium,meronymy_mono --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All analogies tasks
lm_eval --model hf --model_args pretrained=google/mt5-xxl --tasks analogies_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All hypernymy tasks
lm_eval --model hf --model_args pretrained=google/mt5-xxl --tasks hypernymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# All meronymy tasks
lm_eval --model hf --model_args pretrained=google/mt5-xxl --tasks meronymy_all --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10
Multilingual Evaluation
For comprehensive multilingual evaluation, you can run additional commands with multilingual task variants. Here's an example set for one model that can be adapted for others:
bash# Multilingual analogies evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks analogies_multilingual --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Multilingual hypernymy evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks hypernymy_multilingual --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Multilingual meronymy evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks meronymy_multilingual --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Cross-lingual analogies evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks analogies_crosslingual --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Cross-lingual hypernymy evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks hypernymy_crosslingual --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10

# Cross-lingual meronymy evaluation
lm_eval --model hf --model_args pretrained=google/gemma-3-1b-it --tasks meronymy_crosslingual --include_path ./lm_eval/tasks/NLP_JMU --device cuda --batch_size 1 --output_path ./results/ --limit 10
Command Parameters Explained
