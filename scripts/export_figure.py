"""Optional Playwright export for the self-contained Sankey HTML figures."""
from pathlib import Path


def export(stem: Path, width: int, height: int):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={'width': width, 'height': height}, device_scale_factor=2)
        page.goto(stem.with_suffix('.html').resolve().as_uri(), wait_until='load')
        page.evaluate('document.fonts.ready')
        page.locator('svg').screenshot(path=str(stem.with_suffix('.png')))
        page.pdf(path=str(stem.with_suffix('.pdf')), print_background=True, prefer_css_page_size=True)
        browser.close()
