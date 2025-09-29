#!/usr/bin/env python3

import os
import re
import shutil
from pathlib import Path

def extract_images_from_post(content):
    """Extract all wp-content image URLs from post content"""
    patterns = [
        r'/wp-content/uploads/([^"\'<>\s]+\.(jpg|jpeg|png|gif))',
        r'https://yoav\.blog/wp-content/uploads/([^"\'<>\s]+\.(jpg|jpeg|png|gif))',
    ]

    images = set()
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                images.add(match[0])  # Get the filename part
            else:
                images.add(match)

    return list(images)

def convert_post_to_bundle(post_file):
    """Convert a single post to a page bundle"""

    post_path = Path(post_file)

    # Skip if already converted
    if post_path.parent.name != "posts":
        print(f"Skipping {post_path.name} - already converted")
        return

    # Read post content
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract slug from filename or front matter
    filename_slug = post_path.stem
    if filename_slug.startswith('2'):  # Remove date prefix
        filename_slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename_slug)

    # Create bundle directory
    bundle_dir = post_path.parent / filename_slug
    bundle_dir.mkdir(exist_ok=True)

    # Move post to index.md in bundle
    bundle_post = bundle_dir / "index.md"
    shutil.move(str(post_path), str(bundle_post))

    # Extract images referenced in this post
    image_urls = extract_images_from_post(content)

    if image_urls:
        # Create images directory in bundle
        images_dir = bundle_dir / "images"
        images_dir.mkdir(exist_ok=True)

        images_copied = 0

        for image_url in image_urls:
            # Find the image in static or assets
            static_path = Path(f"static/wp-content/uploads/{image_url}")
            assets_path = Path(f"assets/wp-content/uploads/{image_url}")

            source_path = None
            if static_path.exists():
                source_path = static_path
            elif assets_path.exists():
                source_path = assets_path

            if source_path:
                dest_path = images_dir / Path(image_url).name
                if not dest_path.exists():
                    shutil.copy2(str(source_path), str(dest_path))
                    images_copied += 1

        # Update image paths in post content
        updated_content = content
        for image_url in image_urls:
            filename = Path(image_url).name
            old_pattern = f"/wp-content/uploads/{image_url}"
            new_pattern = f"images/{filename}"
            updated_content = updated_content.replace(old_pattern, new_pattern)

        # Write updated content
        with open(bundle_post, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Converted: {filename_slug}")
        print(f"  → Copied {images_copied} images")
        print(f"  → Updated {len(image_urls)} image references")
    else:
        print(f"Converted: {filename_slug} (no images)")

    return filename_slug

def main():
    """Convert all posts to page bundles"""
    posts_dir = Path("content/posts")

    print("Converting posts to page bundles...")
    print("=" * 60)

    # Get all .md files in posts directory (not subdirectories)
    post_files = [f for f in posts_dir.glob("*.md")]

    total_converted = 0

    for post_file in post_files:
        try:
            convert_post_to_bundle(post_file)
            total_converted += 1
        except Exception as e:
            print(f"Error converting {post_file.name}: {e}")

    print("=" * 60)
    print(f"Converted {total_converted} posts to page bundles")

    # Update the layout to work with all posts
    print("\nUpdating layout to work with all posts...")

if __name__ == "__main__":
    main()