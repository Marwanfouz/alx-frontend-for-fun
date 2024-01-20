#!/usr/bin/python3

"""
Script that converts markdown to HTML
"""
import sys
import os

if len(sys.argv) < 2:
    sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
    sys.exit(1)

Markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(Markdown_file):
    sys.stderr.write(f'Missing {Markdown_file}\n')
    sys.exit(1)

sys.exit(0)
