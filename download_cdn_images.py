import os
import re
import time
import urllib.request
import urllib.error

POSTS_DIR = "/Users/musakokcen/Documents/GitHub/githubpages/blog/_posts"
ASSETS_DIR = "/Users/musakokcen/Documents/GitHub/githubpages/blog/assets"
CDN_PATTERN = re.compile(r'https://cdn-images-1\.medium\.com/[^\s\)\'"]+')

FILE_TO_SLUG = {
    "2020-10-26-configure-firebase-push-notification.md":           "2020-10-26-configure-firebase-push-notification",
    "2020-10-26-how-to-use-a-firebase-function-to-handle-incoming.md": "2020-10-26-how-to-use-a-firebase-function-to-handle-incoming",
    "2021-06-25-how-do-we-implement-unit-tests-unit-test-practices.md": "2021-06-25-how-do-we-implement-unit-tests-unit-test-practices",
    "2022-02-24-testing-onesignal-push-notifications-on-the-simula.md": "2022-02-24-testing-onesignal-push-notifications-on-the-simula",
    "2022-10-26-build-a-chat-feature-using-pusher-channels-in-swif.md": "2022-10-26-build-a-chat-feature-using-pusher-channels-in-swif",
    "2023-03-26-code-the-hidden-language-of-computer-hardware-and.md":  "2023-03-26-code-the-hidden-language-of-computer-hardware-and",
    "2023-05-29-recap-of-the-first-6-months-in-munich.md":           "2023-05-29-recap-of-the-first-6-months-in-munich",
    "2024-04-30-enhance-your-development-toolkit-adding-xcode-inst.md": "2024-04-30-enhance-your-development-toolkit-adding-xcode-inst",
}

HEADERS = {"User-Agent": "Mozilla/5.0"}
DELAY_BETWEEN = 5       # seconds between successful downloads
RETRY_WAIT    = 60      # seconds to wait after a 429
MAX_RETRIES   = 3

total_downloaded = 0
total_skipped    = 0
total_failed     = 0


def download_with_retry(url):
    """Download url; returns bytes on success, None on failure."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status == 200:
                    return resp.read()
                print(f"    HTTP {resp.status} (attempt {attempt})")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"    429 Too Many Requests — waiting {RETRY_WAIT}s (attempt {attempt}/{MAX_RETRIES})")
                time.sleep(RETRY_WAIT)
            else:
                print(f"    HTTP error {e.code}: {e} (attempt {attempt})")
                return None
        except Exception as e:
            print(f"    Error: {e} (attempt {attempt})")
            return None
    return None


for filename, slug in FILE_TO_SLUG.items():
    md_path      = os.path.join(POSTS_DIR, filename)
    asset_folder = os.path.join(ASSETS_DIR, slug)

    if not os.path.exists(md_path):
        print(f"[SKIP] File not found: {md_path}")
        continue

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    cdn_urls = CDN_PATTERN.findall(content)

    if not cdn_urls:
        print(f"[OK]   No CDN URLs in {filename}")
        continue

    print(f"\n[FILE] {filename} — {len(cdn_urls)} CDN URL(s) found")

    modified_content = content
    for url in cdn_urls:
        raw_filename = url.split("/")[-1]
        img_filename = raw_filename.split("?")[0].split("#")[0]
        local_path   = os.path.join(asset_folder, img_filename)
        local_url    = f"/assets/{slug}/{img_filename}"

        if os.path.exists(local_path):
            print(f"  [EXISTS] {img_filename} — updating reference only")
            modified_content = modified_content.replace(url, local_url)
            total_skipped += 1
            continue

        print(f"  [DL]    {img_filename}")
        data = download_with_retry(url)
        if data is not None:
            os.makedirs(asset_folder, exist_ok=True)
            with open(local_path, "wb") as img_file:
                img_file.write(data)
            print(f"          -> saved ({len(data):,} bytes)")
            modified_content = modified_content.replace(url, local_url)
            total_downloaded += 1
            time.sleep(DELAY_BETWEEN)
        else:
            print(f"  [WARN]  All retries failed for {url} — keeping CDN URL")
            total_failed += 1

    if modified_content != content:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(modified_content)
        print(f"  [SAVED] {filename} updated.")

print(f"\n=== Done ===")
print(f"  Downloaded : {total_downloaded}")
print(f"  Already had: {total_skipped}")
print(f"  Failed      : {total_failed}")
