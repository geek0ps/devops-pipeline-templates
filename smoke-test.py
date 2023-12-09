import requests
import sys
import argparse

def smoke_test(url, expected_status, expected_content=None):
    try:
        response = requests.get(url)
        if response.status_code != expected_status:
            print(f"Smoke test failed: {url} returned status code {response.status_code}")
            sys.exit(1)
        
        if expected_content and expected_content not in response.text:
            print(f"Smoke test failed: '{expected_content}' not found in response from {url}")
            sys.exit(1)

        print(f"Smoke test passed: {url} returned status code {expected_status} and expected content was found.")
    except requests.RequestException as e:
        print(f"Smoke test failed: Could not connect to {url}")
        print(f"Error: {e}")
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Smoke test a given URL.')
    parser.add_argument('url', type=str, help='URL to test')
    parser.add_argument('--expected_content', type=str, help='Expected content in response', required=False)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    URL = args.url
    EXPECTED_STATUS = 200  
    EXPECTED_CONTENT = args.expected_content

    smoke_test(URL, EXPECTED_STATUS, EXPECTED_CONTENT)
