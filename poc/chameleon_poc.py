#!/usr/bin/env python3
import argparse
import sys

# This is a simplified proof-of-concept of the Zero-Width Character encoder.
# For clarity, it does not include the encryption layer from the full Chameleon design.

ZWC_MAP = {
    '00': '\u200b',  # ZERO WIDTH SPACE
    '01': '\u200c',  # ZERO WIDTH NON-JOINER
    '10': '\u200d',  # ZERO WIDTH JOINER
    '11': '\ufeff',  # ZERO WIDTH NO-BREAK SPACE
}
ZWC_REV_MAP = {v: k for k, v in ZWC_MAP.items()}

def encode(cover_text, secret_message):
    """Encodes a secret message into a cover text using zero-width characters."""
    
    # 1. Convert secret message to a binary string
    binary_secret = ''.join(format(ord(char), '08b') for char in secret_message)
    
    # 2. Encode the binary string into zero-width characters
    zwc_payload = ''
    i = 0
    while i < len(binary_secret):
        # Handle cases where the last chunk is less than 2 bits
        chunk = binary_secret[i:i+2]
        if len(chunk) < 2:
            chunk = chunk + '0' * (2 - len(chunk)) # Pad with '0'
        
        zwc_payload += ZWC_MAP[chunk]
        i += 2
        
    # 3. Intersperse the ZWC payload into the cover text
    # We will inject one ZWC after each character of the cover text.
    if len(zwc_payload) > len(cover_text):
        raise ValueError(f"Cover text is too short. Needs at least {len(zwc_payload)} characters, but has {len(cover_text)}.")

    result = []
    payload_idx = 0
    for char in cover_text:
        result.append(char)
        if payload_idx < len(zwc_payload):
            result.append(zwc_payload[payload_idx])
            payload_idx += 1
            
    return "".join(result)

def decode(stego_text):
    """Decodes a secret message from a text containing zero-width characters."""
    
    # 1. Extract zero-width characters from the text
    zwc_payload = [char for char in stego_text if char in ZWC_REV_MAP]
    
    # 2. Convert the zero-width characters back to a binary string
    binary_secret = "".join([ZWC_REV_MAP[char] for char in zwc_payload])
    
    # 3. Convert the binary string back to the original message
    secret_message = ""
    i = 0
    while i < len(binary_secret):
        byte_chunk = binary_secret[i:i+8]
        if len(byte_chunk) < 8:
            break # Ignore incomplete bytes at the end
            
        decimal_val = int(byte_chunk, 2)
        secret_message += chr(decimal_val)
        i += 8
        
    return secret_message

def main():
    parser = argparse.ArgumentParser(
        description="Chameleon PoC: Hides secret messages in text using Zero-Width Characters.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # --- Encode command ---
    parser_encode = subparsers.add_parser("encode", help="Encode a secret message into a cover text.")
    parser_encode.add_argument("cover_file", help="Path to the cover text file (e.g., a README).")
    parser_encode.add_argument("secret_message", help="The secret string to hide.")

    # --- Decode command ---
    parser_decode = subparsers.add_parser("decode", help="Decode a secret message from a steganographic text file.")
    parser_decode.add_argument("stego_file", help="Path to the file containing the hidden message.")
    
    args = parser.parse_args()
    
    try:
        if args.command == "encode":
            with open(args.cover_file, 'r', encoding='utf-8') as f:
                cover_text = f.read()
            
            stego_text = encode(cover_text, args.secret_message)
            print(stego_text)

        elif args.command == "decode":
            with open(args.stego_file, 'r', encoding='utf-8') as f:
                stego_text = f.read()
            
            secret_message = decode(stego_text)
            print(secret_message)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
