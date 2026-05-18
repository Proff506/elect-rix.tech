#!/bin/bash
# Save Cloudflare API token securely
# Run this in your terminal: bash ~/projects/elect-rix.tech/save-token.sh
echo ""
echo "=== Cloudflare API Token Setup ==="
echo ""
read -s -p "Paste your Cloudflare API token: " TOKEN
echo ""
mkdir -p ~/.secrets
chmod 700 ~/.secrets
echo -n "$TOKEN" > ~/.secrets/cf-token.txt
chmod 600 ~/.secrets/cf-token.txt
unset TOKEN
echo "Token saved to ~/.secrets/cf-token.txt"
echo "Verification:"
wc -c ~/.secrets/cf-token.txt