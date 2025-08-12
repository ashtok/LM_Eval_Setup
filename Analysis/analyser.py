#!/usr/bin/env python3
"""
Extracts synset IDs from multiple JSONL files where predictions are incorrect (acc != 1.0).
Saves all unique incorrect synset IDs to a single output file.
"""

import json
from pathlib import Path
from typing import Set, Tuple, List

# ---------------------------- Configuration ----------------------------

INPUT_FILES = [
    # Your input files here (same as before)
    "D:\\Masters In Germany\\Computer Science\\Semester 4\\LM_Eval_Setup\\lm-evaluation-harness\\results\\samples_hypernymy_mono_2025-07-29T19-48-09.332370.jsonl",
    "D:\\Masters In Germany\\Computer Science\\Semester 4\\LM_Eval_Setup\\lm-evaluation-harness\\results\\samples_hypernymy_mono_2025-07-29T19-58-52.110387.jsonl",
    "D:\\Masters In Germany\\Computer Science\\Semester 4\\LM_Eval_Setup\\lm-evaluation-harness\\results\\samples_hypernymy_mono_2025-07-29T20-10-03.502108.jsonl",
    "D:\\Masters In Germany\\Computer Science\\Semester 4\\LM_Eval_Setup\\lm-evaluation-harness\\results\\samples_meronymy_mono_2025-07-29T19-48-09.332370.jsonl",
    "D:\\Masters In Germany\\Computer Science\\Semester 4\\LM_Eval_Setup\\lm-evaluation-harness\\results\\samples_meronymy_mono_2025-07-29T19-58-52.110387.jsonl",
    "D:\\Masters In Germany\\Computer Science\\Semester 4\\LM_Eval_Setup\\lm-evaluation-harness\\results\\samples_meronymy_mono_2025-07-29T20-10-03.502108.jsonl",
]

OUTPUT_FILE_PATH = "D:\\Masters In Germany\\Computer Science\\Semester 4\\LM_Eval_Setup\\Analysis\\incorrect_synsets.txt"

# ------------------------- Core Extraction Logic -------------------------

def extract_incorrect_synset_ids_from_file(file_path: str) -> Tuple[Set[str], dict]:
    """
    Extracts synset IDs from lines with incorrect predictions (acc != 1.0) in a JSONL file.

    Args:
        file_path (str): Path to input JSONL file.

    Returns:
        Tuple[Set[str], dict]: Set of unique incorrect synset IDs and stats dictionary.
    """
    synset_ids = set()
    stats = {
        'file': file_path,
        'total_lines': 0,
        'incorrect_predictions': 0,
        'synset_ids_found': 0,
        'duplicates_in_file': 0
    }

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                stats['total_lines'] += 1

                try:
                    data = json.loads(line)
                    # Save synset_id only if prediction is incorrect
                    if data.get("acc", 1.0) != 1.0:
                        stats['incorrect_predictions'] += 1

                        metadata = data.get('doc', {}).get('metadata', {})
                        synset_id = metadata.get('synset_id')

                        if synset_id:
                            stats['synset_ids_found'] += 1
                            if synset_id in synset_ids:
                                stats['duplicates_in_file'] += 1
                            synset_ids.add(synset_id)

                except json.JSONDecodeError as e:
                    print(f"⚠️  JSON decode error on line {line_num} in {file_path}: {e}")
                except Exception as e:
                    print(f"⚠️  Error on line {line_num} in {file_path}: {e}")

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"❌ Error reading file '{file_path}': {e}")

    return synset_ids, stats


# --------------------------- File Writer ---------------------------

def save_synset_ids(synset_ids: Set[str], output_file: str) -> bool:
    """
    Saves synset IDs to a file, one per line.

    Args:
        synset_ids (Set[str]): Synset IDs to save.
        output_file (str): Output file path.

    Returns:
        bool: True if saved successfully, False otherwise.
    """
    try:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            for synset_id in sorted(synset_ids):
                f.write(f"{synset_id}\n")

        print(f"✅ Synset IDs saved to: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Failed to save file '{output_file}': {e}")
        return False


# --------------------------- Main Driver ---------------------------

def main() -> int:
    print("=" * 70)
    print("📚 Multi-File Synset ID Extractor for Incorrect Predictions (Intersection)")
    print("=" * 70)

    all_incorrect_sets: List[Set[str]] = []
    all_stats: List[dict] = []

    for input_file in INPUT_FILES:
        print(f"\n📂 Processing file: {input_file}")
        synset_ids, stats = extract_incorrect_synset_ids_from_file(input_file)
        all_stats.append(stats)
        all_incorrect_sets.append(synset_ids)

        print(f"   • Incorrect predictions   : {stats['incorrect_predictions']}")
        print(f"   • Synset IDs found        : {stats['synset_ids_found']}")
        print(f"   • Unique in this file     : {len(synset_ids)}")
        print(f"   • Duplicates in file      : {stats['duplicates_in_file']}")

    # Compute intersection of all incorrect synset ID sets:
    if all_incorrect_sets:
        intersection_synset_ids = set.intersection(*all_incorrect_sets)
    else:
        intersection_synset_ids = set()

    print("\n📊 Summary Across All Files:")
    total_lines = sum(s['total_lines'] for s in all_stats)
    total_incorrect = sum(s['incorrect_predictions'] for s in all_stats)
    total_found = sum(s['synset_ids_found'] for s in all_stats)

    print(f"   • Total files processed      : {len(INPUT_FILES)}")
    print(f"   • Total lines processed      : {total_lines}")
    print(f"   • Total incorrect predictions: {total_incorrect}")
    print(f"   • Total synset IDs found     : {total_found}")
    print(f"   • Synset IDs incorrect in ALL files (intersection): {len(intersection_synset_ids)}")
    print(f"   • Sample synset IDs          : {list(sorted(intersection_synset_ids))[:5]}")

    print(f"\n💾 Saving intersected results to: {OUTPUT_FILE_PATH}")
    if save_synset_ids(intersection_synset_ids, OUTPUT_FILE_PATH):
        print(f"\n🎉 Extraction complete: {len(intersection_synset_ids)} unique synset IDs incorrect in ALL files saved.")
        return 0
    else:
        return 1


# --------------------------- Entry Point ---------------------------

if __name__ == "__main__":
    import sys
    sys.exit(main())
