# Cooking Cheatsheet

This repository contains a LaTeX-based project for generating a comprehensive cooking cheatsheet. It includes conversion tables, common ingredient substitutions, and other helpful kitchen references.

## Features
- Professionally typeset cheatsheet using LaTeX.
- Supports International System of Units (SI) with optional imperial conversions.
- Portable development environment provided by Nix flakes.

## Requirements
- [Nix](https://nixos.org/download.html) installed on your system.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/nilp0inter/cooking-cheatsheet.git
   cd cooking-cheatsheet
   ```

2. Build the cheatsheet:
   ```bash
   nix build
   ```

4. Open the generated PDF:

   ```bash
   zathura cheatsheet.pdf  # Or any other PDF viewer
   ```

## File Structure

- cheatsheet.tex: The LaTeX source file for the cooking cheatsheet.
- flake.nix: The Nix flake configuration for the development environment.

## Contributions

Feel free to submit issues or pull requests to improve the cheatsheet or expand its features.
License

This project is licensed under the MIT License. See LICENSE for more information.
