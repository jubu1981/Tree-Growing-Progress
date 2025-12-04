# Tree Growing Progress

This project visualizes progress using a tree that grows as the usage percentage increases. It's a simple and fun way to track adoption or completion of a goal.

## Features

- **Visual Progress**: A tree image that changes based on the usage percentage.
- **Interactive Slider**: An interactive slider to manually adjust and see the usage percentage.
- **Growth Stages**: A clear table showing the different stages of the tree's growth.
- **Automated Updates**: A batch script to easily update the usage value and push the changes to a Git repository.

## How to Use

1.  **View the Progress**: Open the https://jubu1981.github.io/Tree-Growing-Progress/ in a web browser to see the current progress.
2.  **Update the Usage**:
    *   Run the `update_and_push.bat` script.
    *   Enter the new usage value when prompted.
    *   The script will automatically update the `index.html` file, commit the changes to Git, and push them to the `main` branch.

## Tree Growth Stages

| Image                                                                                               | Usage Threshold |
| --------------------------------------------------------------------------------------------------- | --------------- |
| <img src="Tree-Fullsize.png" alt="Tree Fullsize" style="width: 50px; height: auto;">                  | ≥ 75%           |
| <img src="Tree-Big.png" alt="Tree Big" style="width: 50px; height: auto;">                            | 70% - 74%       |
| <img src="Tree-Medium.png" alt="Tree Medium" style="width: 50px; height: auto;">                      | 60% - 69%       |
| <img src="Tree-Small.png" alt="Tree Small" style="width: 50px; height: auto;">                        | 50% - 59%       |
| <img src="Pre-Tree.png" alt="Pre Tree" style="width: 50px; height: auto;">                            | 40% - 49%       |
| <img src="Seed.png" alt="Seed" style="width: 50px; height: auto;">                                    | < 40%           |

## Files

-   `index.html`: The main page that displays the tree and progress.
-   `update_and_push.bat`: A script to update the usage value and push changes to the repository.
-   `*.png`: Image files for the different stages of the tree's growth.

## Hosting

This project is deployed on GitHub Pages and is accessible at [https://jubu1981.github.io/Tree-Growing-Progress/](https://jubu1981.github.io/Tree-Growing-Progress/).
