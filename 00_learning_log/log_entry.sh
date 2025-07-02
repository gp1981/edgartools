#!/bin/bash

LOG_DIR="./00_learning_log"
TEMPLATE="$LOG_DIR/template.md"
DATE=$(date "+%Y-%m-%d")
OUTPUT="$LOG_DIR/learning_journal.md"

# Copy template to a temp file
TMP_FILE=$(mktemp /tmp/log_entry_XXXX.md)
cp "$TEMPLATE" "$TMP_FILE"

# Replace {{date}} placeholder
sed -i '' "s/{{date}}/$DATE/" "$TMP_FILE"

# Open in your preferred editor (change 'nano' to 'vim' or 'code' if you prefer)
code "$TMP_FILE"

# Append edited temp file to the main journal
cat "$TMP_FILE" >> "$OUTPUT"
echo -e "\n---\n" >> "$OUTPUT"

# Clean up
rm "$TMP_FILE"

echo "✅ Entry added to $OUTPUT"
