import base64
from collections import Counter
import argparse

def analyze_ciphertext(ciphertext):
    try:
        # Decode the base64-encoded ciphertext
        decoded_ciphertext = base64.b64decode(ciphertext)
        
        # Print the decoded string
        decoded_string = decoded_ciphertext.decode('utf-8', errors='ignore')
        print("Decoded string:", decoded_string)
        
        # Convert to hexadecimal
        hex_representation = decoded_ciphertext.hex()
        
        # Count the frequency of each hex character
        hex_frequency = Counter(hex_representation)
        
        # Display the frequency analysis
        for char, freq in hex_frequency.items():
            print(f"Character: {char}, Frequency: {freq}")
    
    except Exception as e:
        print(f"Error processing ciphertext: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Analyze base64-encoded ciphertext")
    parser.add_argument("ciphertext", help="The base64-encoded ciphertext(s) to analyze, separated by commas")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Split the input by commas to handle multiple ciphertexts
    ciphertexts = args.ciphertext.split(',')
    
    for ciphertext in ciphertexts:
        print(f"Analyzing ciphertext: {ciphertext}")
        analyze_ciphertext(ciphertext)
        print("\n")

if __name__ == "__main__":
    main()
