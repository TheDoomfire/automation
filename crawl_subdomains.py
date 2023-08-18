import requests
import re

def crawl_subdomains(domain):
  """Crawls all subdomains of a domain."""
  subdomains = []
  response = requests.get(f"https://{domain}")
  for link in response.text.split("/"):
    if re.match(r"^[a-z0-9-]+$", link):
      subdomains.append(link)
  return subdomains

if __name__ == "__main__":
  subdomains = crawl_subdomains("https://autolazy.vercel.app")
  print(subdomains)