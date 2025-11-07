#!/usr/bin/env python3
"""
Tree Growing Progress Display
Displays the growing progress of a tree through different stages.
"""

import time
import sys


class TreeGrowth:
    """Represents the growth stages of a tree."""
    
    def __init__(self):
        """Initialize tree growth stages."""
        self.stages = [
            {
                "name": "Seed",
                "age": "Day 1",
                "art": [
                    "       ",
                    "   .   ",
                    "       "
                ]
            },
            {
                "name": "Germination",
                "age": "Week 1",
                "art": [
                    "       ",
                    "   |   ",
                    "  ---  "
                ]
            },
            {
                "name": "Sprout",
                "age": "Week 2",
                "art": [
                    "   |   ",
                    "   |   ",
                    "  ---  "
                ]
            },
            {
                "name": "Seedling",
                "age": "Month 1",
                "art": [
                    "  \\|/  ",
                    "   |   ",
                    "   |   ",
                    "  ---  "
                ]
            },
            {
                "name": "Young Tree",
                "age": "Month 6",
                "art": [
                    "  __|__",
                    " / | | \\",
                    "   |   ",
                    "   |   ",
                    "  ---  "
                ]
            },
            {
                "name": "Growing Tree",
                "age": "Year 1",
                "art": [
                    "  _\\|/_ ",
                    " / \\|/ \\",
                    "  __|__ ",
                    "    |   ",
                    "    |   ",
                    "   ---  "
                ]
            },
            {
                "name": "Mature Tree",
                "age": "Year 3",
                "art": [
                    "    ___    ",
                    "  _/   \\_  ",
                    " /  |||  \\ ",
                    " \\__|||__/ ",
                    "    |||    ",
                    "    |||    ",
                    "   -----   "
                ]
            },
            {
                "name": "Full Grown Tree",
                "age": "Year 5+",
                "art": [
                    "      ___      ",
                    "   __/   \\__   ",
                    "  /   |||   \\  ",
                    " / ___|||___ \\ ",
                    "  /   |||   \\  ",
                    "  \\___|||___/  ",
                    "      |||      ",
                    "      |||      ",
                    "     -----     "
                ]
            }
        ]
    
    def display_stage(self, stage_index):
        """Display a specific growth stage."""
        if stage_index < 0 or stage_index >= len(self.stages):
            print("Invalid stage index")
            return
        
        stage = self.stages[stage_index]
        print(f"\n{stage['name']} - {stage['age']}")
        print("=" * 40)
        for line in stage['art']:
            print(line)
        print("=" * 40)
    
    def display_progress(self, delay=1.0):
        """Display all growth stages with animation."""
        total_stages = len(self.stages)
        
        print("\n🌱 Tree Growing Progress 🌳")
        print("=" * 40)
        
        for i, stage in enumerate(self.stages):
            # Add spacing between stages
            if i > 0:
                print("\n" * 2)
            
            # Display progress bar
            progress = (i + 1) / total_stages * 100
            bar_length = 30
            filled = int(bar_length * (i + 1) / total_stages)
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"Progress: [{bar}] {progress:.0f}%")
            print()
            
            # Display current stage
            self.display_stage(i)
            
            # Wait before next stage (except for last stage)
            if i < total_stages - 1:
                time.sleep(delay)
        
        print("\n✨ Tree is fully grown! ✨\n")
    
    def display_all_stages(self):
        """Display all stages at once without animation."""
        print("\n🌱 Tree Growth Stages 🌳")
        print("=" * 40)
        
        for i in range(len(self.stages)):
            self.display_stage(i)
            print()


def main():
    """Main function to run the tree growth display."""
    tree = TreeGrowth()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg == "--all":
            tree.display_all_stages()
        elif arg == "--stage" and len(sys.argv) > 2:
            try:
                stage_num = int(sys.argv[2])
                tree.display_stage(stage_num)
            except ValueError:
                print("Usage: python tree_growth.py --stage <0-7>")
        elif arg == "--help" or arg == "-h":
            print("Tree Growing Progress Display")
            print("\nUsage:")
            print("  python tree_growth.py              - Display animated growth")
            print("  python tree_growth.py --all        - Display all stages at once")
            print("  python tree_growth.py --stage <n>  - Display specific stage (0-7)")
            print("  python tree_growth.py --help       - Show this help message")
        else:
            print(f"Unknown option: {arg}")
            print("Use --help for usage information")
    else:
        # Default: show animated progress
        tree.display_progress(delay=1.5)


if __name__ == "__main__":
    main()
