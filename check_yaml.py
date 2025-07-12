from datasets import load_dataset

dataset = load_dataset(
    "json",
    data_files="D:\\Masters In Germany\\Computer Science\\Semester 4\\Practical_NLP\\LM_Eval\\hypernymy_questions.json",
    split="train"
)
print(dataset[0])
