#!/usr/bin/env python3
"""
ASCII Art Generator - Simple CLI Tool
"""

import pyfiglet
import sys
from datetime import datetime

class ASCIIArtGenerator:
    def __init__(self):
        self.available_fonts = [
            'standard', '3-d', '3x5', '5lineoblique', 'acrobatic',
            'alligator', 'alligator2', 'alphabet', 'avatar', 'banner',
            'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic',
            'bell', 'big', 'bigchief', 'binary', 'block',
            'bubble', 'bulbhead', 'calgphy2', 'caligraphy', 'catwalk',
            'chunky', 'coinstak', 'colossal', 'computer', 'contessa',
            'contrast', 'cosmic', 'cosmike', 'cricket', 'cursive',
            'cyberlarge', 'cybermedium', 'cybersmall', 'diamond',
            'digital', 'doh', 'doom', 'dotmatrix', 'drpepper',
            'eftichess', 'eftifont', 'eftipiti', 'eftirobot',
            'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'fender',
            'fourtops', 'fraktur', 'fuzzy', 'goofy', 'gothic',
            'graffiti', 'hollywood', 'invita', 'isometric1',
            'isometric2', 'isometric3', 'isometric4', 'italic',
            'ivrit', 'jazmine', 'jerusalem', 'katakana', 'kban',
            'larry3d', 'lcd', 'lean', 'letters', 'linux', 'lockergnome',
            'madrid', 'marquee', 'maxfour', 'mike', 'mini', 'mirror',
            'mnemonic', 'morse', 'moscow', 'nancyj-fancy', 'nancyj-underlined',
            'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre', 'pawp',
            'peaks', 'pebbles', 'pepper', 'poison', 'puffy', 'pyramid',
            'rectangles', 'relief', 'relief2', 'rev', 'roman', 'rot13',
            'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sblood',
            'script', 'serifcap', 'shadow', 'short', 'slant', 'slide',
            'small', 'smiscript1', 'smkeyboard', 'smscript', 'smshadow',
            'smslant', 'smtengwar', 'speed', 'stampatello', 'standard',
            'starwars', 'stellar', 'stop', 'straight', 'tanja', 'tengwar',
            'term', 'thick', 'thin', 'threepoint', 'ticks', 'ticksslant',
            'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint',
            'univers', 'usaflag', 'weird'
        ]
    
    def generate_art(self, text, font='standard'):
        """Generate ASCII art from text"""
        try:
            if font not in self.available_fonts:
                print(f"Font '{font}' not found. Using 'standard' font.")
                font = 'standard'
            
            result = pyfiglet.figlet_format(text, font=font)
            return result
        except Exception as e:
            return f"Error generating ASCII art: {str(e)}"
    
    def list_fonts(self, num=20):
        """Display available fonts"""
        print(f"\nAvailable Fonts (showing {min(num, len(self.available_fonts))} of {len(self.available_fonts)}):")
        print("-" * 50)
        for i, font in enumerate(self.available_fonts[:num], 1):
            print(f"{i:3}. {font}")
        print("\nUse '--list-fonts all' to see all available fonts.")
    
    def preview_fonts(self, text, num=5):
        """Preview text in multiple fonts"""
        print(f"\nPreview of '{text}' in different fonts:")
        print("-" * 60)
        preview_fonts = ['standard', 'block', 'slant', 'banner', 'doom']
        
        for font in preview_fonts[:num]:
            print(f"\nFont: {font}")
            print("-" * 40)
            art = self.generate_art(text, font)
            print(art)
            print()

def main():
    import argparse
    
    generator = ASCIIArtGenerator()
    
    parser = argparse.ArgumentParser(
        description='Generate ASCII art from text',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Hello World"
  %(prog)s "Python" --font doom
  %(prog)s "Test" --font slant --save output.txt
  %(prog)s --list-fonts
  %(prog)s --preview "Sample"
        """
    )
    
    parser.add_argument('text', nargs='?', help='Text to convert to ASCII art')
    parser.add_argument('-f', '--font', default='standard', help='Font to use (default: standard)')
    parser.add_argument('-s', '--save', metavar='FILE', help='Save output to file')
    parser.add_argument('-l', '--list-fonts', nargs='?', const=20, metavar='NUMBER',
                       help='List available fonts (optionally specify number to show)')
    parser.add_argument('-p', '--preview', metavar='TEXT',
                       help='Preview TEXT in different fonts')
    
    args = parser.parse_args()
    
    # List fonts if requested
    if args.list_fonts is not None:
        if args.list_fonts == 'all':
            num = len(generator.available_fonts)
        else:
            try:
                num = int(args.list_fonts)
            except:
                num = 20
        generator.list_fonts(num)
        return
    
    # Preview fonts if requested
    if args.preview:
        generator.preview_fonts(args.preview)
        return
    
    # Generate ASCII art if text provided
    if args.text:
        art = generator.generate_art(args.text, args.font)
        
        # Add header
        header = f"ASCII Art Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        header += f"\nText: '{args.text}' | Font: {args.font}"
        header += "\n" + "=" * 50 + "\n"
        
        output = header + art
        
        # Display to console
        print(output)
        
        # Save to file if requested
        if args.save:
            try:
                with open(args.save, 'w', encoding='utf-8') as f:
                    f.write(output)
                print(f"\nArt saved to: {args.save}")
            except Exception as e:
                print(f"Error saving file: {str(e)}")
    else:
        parser.print_help()
        print("\n" + "=" * 60)
        print("Try these examples:")
        print("  ascii_art.py 'Hello' --font slant")
        print("  ascii_art.py 'Python' --font doom --save output.txt")
        print("  ascii_art.py --list-fonts 10")
        print("  ascii_art.py --preview 'Test'")

if __name__ == "__main__":
    main()
