#!/usr/bin/env python3
"""
Train a Hugging Face tokenizer (WordLevel) from stdin where each line is
already whitespace-tokenized. Saves a fast tokenizer usable with Transformers.

Input is expected to contain sequences like:
<bos> ... <lemma> OUTPUTHERE <eos>

Special tokens included: <pad>, <unk>, <bos>, <eos>, <lemma>.
"""

import sys
import os
import argparse

# tokenizers (Rust-backed) for efficient training
from tokenizers import Tokenizer
from tokenizers.models import WordLevel
from tokenizers.trainers import WordLevelTrainer
from tokenizers.pre_tokenizers import WhitespaceSplit

# Transformers fast tokenizer wrapper for downstream usage
from transformers import PreTrainedTokenizerFast


def iter_tokenized_lines(stdin_stream):
    """Yield token lists from stdin, skipping empty lines."""
    for line in stdin_stream:
        line = line.strip()
        if not line:
            continue
        # Input is already whitespace-tokenized
        yield line.split()


def train_tokenizer(vocab_size, min_frequency):
    """Train a WordLevel tokenizer from pre-tokenized iterator."""
    special_tokens = ["<pad>", "<unk>", "<bos>", "<eos>", "<lemma>"]

    # Initialize tokenizer with UNK token
    tokenizer = Tokenizer(WordLevel(unk_token="<unk>"))
    tokenizer.pre_tokenizer = WhitespaceSplit()

    # Configure trainer
    trainer = WordLevelTrainer(
        vocab_size=vocab_size,
        min_frequency=min_frequency,
        special_tokens=special_tokens,
        show_progress=True,
    )

    # Train from iterator of token lists
    tokenizer.train_from_iterator(iter_tokenized_lines(sys.stdin), trainer=trainer)

    return tokenizer


def wrap_fast_tokenizer(tokenizer):
    """Wrap a tokenizers.Tokenizer in a Transformers fast tokenizer and set specials."""
    fast_tok = PreTrainedTokenizerFast(
        tokenizer_object=tokenizer,
        unk_token="<unk>",
        pad_token="<pad>",
        bos_token="<bos>",
        eos_token="<eos>",
    )
    # Keep additional special tokens separate
    fast_tok.add_special_tokens({"additional_special_tokens": ["<lemma>"]})
    return fast_tok


def parse_args():
    parser = argparse.ArgumentParser(description="Train a HF WordLevel tokenizer from stdin")
    parser.add_argument(
        "--out",
        type=str,
        default="tokenizer",
        help="Output directory to save the tokenizer",
    )
    parser.add_argument(
        "--vocab-size",
        type=int,
        default=500,
        help="Maximum vocabulary size (including special tokens)",
    )
    parser.add_argument(
        "--min-frequency",
        type=int,
        default=1,
        help="Minimum token frequency to be included in the vocab",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    os.makedirs(args.out, exist_ok=True)

    tokenizer = train_tokenizer(vocab_size=args.vocab_size, min_frequency=args.min_frequency)
    fast_tokenizer = wrap_fast_tokenizer(tokenizer)

    # Save in HF format (tokenizer.json, tokenizer_config.json, special_tokens_map.json)
    fast_tokenizer.save_pretrained(args.out)

    # Also save plain tokenizers JSON for interoperability
    tokenizer.save(os.path.join(args.out, "tokenizer_plain.json"))


if __name__ == "__main__":
    main()


