# Tree-Growing-Progress

A Python program that displays the growing progress of a tree through different stages, from seed to full-grown tree.

## Features

- 🌱 Animated tree growth display showing 8 different stages
- 📊 Progress bar showing growth completion percentage
- 🎨 ASCII art representation of each growth stage
- ⚙️ Multiple display modes (animated, all stages, specific stage)

## Growth Stages

The program displays 8 stages of tree growth:

1. **Seed** (Day 1) - The beginning
2. **Germination** (Week 1) - First roots appear
3. **Sprout** (Week 2) - Breaking through the soil
4. **Seedling** (Month 1) - First leaves emerge
5. **Young Tree** (Month 6) - Small branches forming
6. **Growing Tree** (Year 1) - Expanding canopy
7. **Mature Tree** (Year 3) - Well-established
8. **Full Grown Tree** (Year 5+) - Complete growth

## Usage

### Animated Growth Display (Default)

```bash
python tree_growth.py
```

This displays an animated sequence showing the tree growing through all stages.

### Display All Stages at Once

```bash
python tree_growth.py --all
```

Shows all growth stages in a single view without animation.

### Display Specific Stage

```bash
python tree_growth.py --stage <0-7>
```

Display a specific growth stage (0 = Seed, 7 = Full Grown Tree).

Example:
```bash
python tree_growth.py --stage 5
```

### Help

```bash
python tree_growth.py --help
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Examples

### Animated Progress Example

When you run the default command, you'll see:

```
🌱 Tree Growing Progress 🌳
========================================
Progress: [██████████░░░░░░░░░░░░░░░░░░░░] 33%

Seedling - Month 1
========================================
  \|/  
   |   
   |   
  ---  
========================================
```

### All Stages Example

Running with `--all` flag shows all stages:

```
🌱 Tree Growth Stages 🌳
========================================

Seed - Day 1
========================================
       
   .   
       
========================================

Germination - Week 1
========================================
       
   |   
  ---  
========================================
...
```

## License

This project is open source and available under the MIT License.