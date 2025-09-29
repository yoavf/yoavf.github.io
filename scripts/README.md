# WordPress to Hugo Migration Scripts

These scripts were used to migrate a WordPress blog to Hugo with the PaperMod theme.

## Scripts

### `download_wp_media.py`
Downloads media files referenced in WordPress posts to the Hugo static directory.

**Usage:**
```bash
python3 download_wp_media.py
```

**What it does:**
- Scans all markdown files for wp-content/uploads image URLs
- Downloads only the images actually referenced in posts
- Preserves the original directory structure
- Shows progress and reports any failed downloads

### `convert_to_bundles.py`
Converts WordPress posts from individual .md files to Hugo page bundles.

**Usage:**
```bash
python3 convert_to_bundles.py
```

**What it does:**
- Converts each post from `posts/post-name.md` to `posts/post-name/index.md`
- Creates an `images/` directory for each post
- Copies images referenced in each post to its bundle
- Updates image paths from `/wp-content/uploads/...` to `images/...`
- Enables Hugo's image processing for each post

## Post-Migration Cleanup

After running these scripts:

1. **Image optimization** happens automatically via Hugo's page resources
2. **Thumbnails** are generated at build time using `.Fit "600x400 q75"`
3. **Page bundles** allow for better organization and faster builds
4. **Local images** eliminate external dependencies

## Notes

- These scripts were designed for a specific WordPress export format
- Image processing requires images to be in page bundles (not static/)
- The scripts handle broken URLs and missing files gracefully
- All original images are preserved in their new locations