#!/usr/bin/env python3

import os
import re
import requests
from urllib.parse import urlparse, unquote
from pathlib import Path
import time

def find_media_urls(content_dir):
    """Parse all markdown files and extract media URLs"""
    media_urls = set()

    # Patterns to match different types of media URLs
    patterns = [
        r'https?://yoav\.blog/wp-content/uploads/[^\s\)"\'<>]+',
        r'https?://(?:www\.)?yoav\.blog/wp-content/uploads/[^\s\)"\'<>]+',
        r'/wp-content/uploads/[^\s\)"\'<>]+',
        r'src=["\']([^"\']+wp-content/uploads/[^"\']+)["\']',
        r'href=["\']([^"\']+wp-content/uploads/[^"\']+)["\']',
        r'\!\[.*?\]\(([^)]+wp-content/uploads/[^)]+)\)',  # Markdown images
        r'\[.*?\]\(([^)]+wp-content/uploads/[^)]+)\)',     # Markdown links
    ]

    # Walk through all markdown files
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                print(f"Scanning: {filepath}")

                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    for pattern in patterns:
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        for match in matches:
                            if isinstance(match, tuple):
                                match = match[0]

                            # Clean up the URL
                            if match.startswith('/'):
                                url = f"https://yoav.blog{match}"
                            elif not match.startswith('http'):
                                url = f"https://yoav.blog/{match}"
                            else:
                                url = match

                            # Only keep wp-content/uploads URLs
                            if 'wp-content/uploads' in url:
                                # Remove query strings and fragments
                                url = url.split('?')[0].split('#')[0]
                                media_urls.add(url)

    return media_urls

def download_file(url, local_path):
    """Download a single file"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        # Skip if file already exists
        if os.path.exists(local_path):
            print(f"  Skipping (exists): {os.path.basename(local_path)}")
            return True

        # Download the file
        response = requests.get(url, timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; Hugo site migration)'
        })
        response.raise_for_status()

        # Save the file
        with open(local_path, 'wb') as f:
            f.write(response.content)

        print(f"  Downloaded: {os.path.basename(local_path)}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  Error downloading {url}: {e}")
        return False

def main():
    print("WordPress Media Downloader for Hugo Migration")
    print("=" * 50)

    # Paths
    content_dir = "content"
    static_dir = "static"

    # Find all media URLs
    print("\nStep 1: Scanning content for media URLs...")
    media_urls = find_media_urls(content_dir)
    print(f"\nFound {len(media_urls)} unique media files")

    # Download each file
    print("\nStep 2: Downloading media files...")
    success_count = 0
    failed_urls = []

    for i, url in enumerate(media_urls, 1):
        print(f"\n[{i}/{len(media_urls)}] Processing: {url}")

        # Extract the path after the domain
        parsed = urlparse(url)
        path = unquote(parsed.path)

        # Remove leading slash
        if path.startswith('/'):
            path = path[1:]

        # Create local path
        local_path = os.path.join(static_dir, path)

        # Download the file
        if download_file(url, local_path):
            success_count += 1
        else:
            failed_urls.append(url)

        # Be nice to the server
        time.sleep(0.1)

    # Summary
    print("\n" + "=" * 50)
    print(f"Download complete!")
    print(f"Successfully downloaded: {success_count}/{len(media_urls)} files")

    if failed_urls:
        print(f"\nFailed downloads ({len(failed_urls)}):")
        for url in failed_urls[:10]:  # Show first 10 failures
            print(f"  - {url}")
        if len(failed_urls) > 10:
            print(f"  ... and {len(failed_urls) - 10} more")

        # Save failed URLs to a file
        with open('failed_downloads.txt', 'w') as f:
            for url in failed_urls:
                f.write(url + '\n')
        print("\nFailed URLs saved to: failed_downloads.txt")

    # Show disk usage
    total_size = 0
    for root, dirs, files in os.walk(os.path.join(static_dir, 'wp-content')):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))

    print(f"\nTotal size: {total_size / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()