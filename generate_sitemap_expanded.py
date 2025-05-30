import os
from pathlib import Path
from datetime import date
import xml.etree.ElementTree as ET

# CONFIGURATION
site_url = "https://maram.cc"
content_dirs = ['_chapters', 'considered', 'dispatch', 'mysticism', 'realization', 'reverie']
output_filename = "sitemap.xml"
today = date.today().isoformat()

# Initialize root
urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for content_dir in content_dirs:
    base_path = Path(content_dir)
    if not base_path.exists():
        continue

    for file in base_path.glob("*.md"):
        permalink = None
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("permalink:"):
                        permalink = line.split(":", 1)[1].strip()
                        break
        except Exception as e:
            print(f"Failed to read {file}: {e}")
            continue

        if not permalink:
            permalink = f"/{content_dir.strip('_')}/{file.stem}.html"

        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{site_url}{permalink}"
        ET.SubElement(url, "lastmod").text = today
        ET.SubElement(url, "changefreq").text = "monthly"
        ET.SubElement(url, "priority").text = "0.6"

# Write to file
tree = ET.ElementTree(urlset)
tree.write(output_filename, encoding="utf-8", xml_declaration=True)
print(f"✅ Sitemap written to {output_filename}")