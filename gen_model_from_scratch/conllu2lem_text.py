#!/usr/bin/env python3
"""
Script to convert CoNLL-U format to space-separated word-lemma format.
Reads from stdin, outputs to stdout.
"""

import sys
import re

def process_conllu_line(line):
    """Process a single CoNLL-U line and return formatted output."""
    line = line.strip()
    
    # Skip empty lines and comments
    if not line or line.startswith('#'):
        return None
    
    # Split by tabs (CoNLL-U format)
    fields = line.split('\t')
    
    # Skip lines that don't have enough fields or are multiword tokens
    if len(fields) < 10 or '-' in fields[0] or '.' in fields[0]:
        return None
    
    # Extract relevant fields
    word = fields[1]  # FORM
    lemma = fields[2]  # LEMMA
    upos = fields[3]   # UPOS
    feats = fields[5]  # FEATS
    
    
    # Format word with spaces between characters
    word_spaced = ' '.join(list(word))
    
    # Format lemma with spaces between characters
    lemma_spaced = ' '.join(list(lemma))
    
    # Build the output line
    # w o r d UPOS TAG1 TAG2 ... ::: l e m m a
    output_parts = [word_spaced, upos]
    
    # Add additional tags if they're not empty or underscore
    if feats and feats != '_':
        # Split features by | and add each as a tag
        for feat in feats.split('|'):
            if feat:
                output_parts.append(feat)
    
    # Add separator and lemma
    output_parts.extend([':::', lemma_spaced])
    
    return ' '.join(output_parts)

def main():
    """Main function to process stdin and output to stdout."""
    for line in sys.stdin:
        result = process_conllu_line(line)
        if result:
            print(result)

if __name__ == "__main__":
    main()
