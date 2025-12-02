#!/usr/bin/env python3
"""
Example usage of the TreeGrowth class.
Demonstrates how to use the tree growing progress display programmatically.
"""

from tree_growth import TreeGrowth


def main():
    """Example demonstrations of the TreeGrowth class."""
    
    print("=" * 50)
    print("Example 1: Display a specific growth stage")
    print("=" * 50)
    tree = TreeGrowth()
    tree.display_stage(3)  # Display Seedling stage
    
    print("\n" + "=" * 50)
    print("Example 2: Display all stages")
    print("=" * 50)
    tree.display_all_stages()
    
    print("\n" + "=" * 50)
    print("Example 3: Custom animated display with faster delay")
    print("=" * 50)
    tree.display_progress(delay=0.5)
    
    print("\n" + "=" * 50)
    print("Example 4: Get stage information programmatically")
    print("=" * 50)
    print(f"Total number of stages: {len(tree.stages)}")
    for i, stage in enumerate(tree.stages):
        print(f"Stage {i}: {stage['name']} ({stage['age']})")


if __name__ == "__main__":
    main()
