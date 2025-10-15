# Copilot Instructions for This Codebase

## Overview
This project is a simple Pygame application. The main file is `pygame.py`, which initializes a window and loads a background image (`forpygame.jpg`).

## Key Files
- `pygame.py`: Main entry point. Sets up the Pygame window, loads the background, and contains the main loop.
- `forpygame.jpg`: Background image used in the game window.

## Architecture & Patterns
- The code uses a single main loop in `main()` to handle events and keep the window open.
- The `draw()` function is intended for rendering but is currently incomplete (missing coordinates for `blit`).
- All logic is contained in a single file; there are no modules or complex structures.

## Developer Workflows
- **Run the app:** Execute `python pygame.py` from the project root.
- **Dependencies:** Requires the `pygame` library. Install with `pip install pygame` if not present.
- **Assets:** Ensure `forpygame.jpg` is present in the root directory for the background to load.

## Project-Specific Conventions
- The window size is fixed at 1000x800 pixels.
- The background image filename is hardcoded as `forpygame.jpg`.
- The project does not use classes or advanced Pygame patterns (e.g., sprite groups, scenes).

## Known Issues
- The `draw()` function is not called in the main loop, so nothing is rendered.
- The event loop sets `run - False` instead of `run = False` (typo), so the window may not close as expected.
- The window caption is set to an empty string.

## Example: Main Loop Pattern
```python
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    # Drawing and update logic should go here
```

## Recommendations for AI Agents
- Focus on single-file, procedural Pygame patterns.
- When adding features, follow the style of direct function calls and global variables.
- If refactoring, consider introducing classes for game objects and separating logic into modules as the project grows.

---
For more details on writing effective instructions for AI agents, see [VS Code Copilot Instructions Docs](https://aka.ms/vscode-instructions-docs).
