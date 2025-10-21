#!/usr/bin/env python3
"""
Star Citizen Kill Feed Tracker - Launcher

Choose between command-line and GUI versions
"""

import sys
import os

def main():
    # Directly start the GUI application (no CLI option)
    try:
        from sc_kill_feed_gui import main as gui_main
    except Exception as e:
        print(f"Error starting GUI: {e}")
        sys.exit(1)
    gui_main()

if __name__ == '__main__':
    main()

