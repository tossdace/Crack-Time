"""
UI Module for Crack-Time Password Security Tool
Handles all user interface elements, colors, and visual formatting

Author: Security Education Team
License: MIT
"""

import os
import sys
import time
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)


class UI:
    """
    User Interface class providing styled terminal output and formatting.
    
    This class handles all visual elements including colors, banners,
    progress indicators, and screen formatting for the Crack-Time tool.
    """
    
    def __init__(self):
        """Initialize UI with color definitions and styling options."""
        # Color definitions using colorama
        self.RED = Fore.RED + Style.BRIGHT
        self.GREEN = Fore.GREEN
        self.YELLOW = Fore.YELLOW + Style.BRIGHT
        self.BLUE = Fore.BLUE
        self.CYAN = Fore.CYAN + Style.BRIGHT
        self.MAGENTA = Fore.MAGENTA
        self.WHITE = Fore.WHITE + Style.BRIGHT
        self.BRIGHT_GREEN = Fore.GREEN + Style.BRIGHT
        self.RESET = Style.RESET_ALL
        
        # Background colors
        self.BG_BLACK = Back.BLACK
        self.BG_RED = Back.RED
        self.BG_GREEN = Back.GREEN
    
    def clear_screen(self):
        """Clear the terminal screen for better user experience."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """
        Display the main application banner with ASCII art and branding.
        Creates an impressive hacker-style visual identity.
        """
        banner = f"""
{self.BRIGHT_GREEN}
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║   ██████╗██████╗  ██████╗  ██████╗██╗  ██╗      ████████╗██╗███╗   ███╗███████║
║  ██╔════╝██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝      ╚══██╔══╝██║████╗ ████║██╔════║
║  ██║     ██████╔╝███████║ ██║     █████╔╝ █████╗   ██║   ██║██╔████╔██║█████╗ ║
║  ██║     ██╔══██╗██╔══██║ ██║     ██╔═██╗ ╚════╝   ██║   ██║██║╚██╔╝██║██╔══╝ ║
║  ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗          ██║   ██║██║ ╚═╝ ██║███████║
║   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝          ╚═╝   ╚═╝╚═╝     ╚═╝╚══════║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                    PASSWORD SECURITY AWARENESS TOOL                          ║
║                          Educational Use Only                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝
{self.RESET}"""
        print(banner)
        
        # Add animated typing effect for subtitle
        subtitle = "Analyzing password strength since 2025..."
        print(f"\n{self.CYAN}                      ", end="")
        for char in subtitle:
            print(char, end="", flush=True)
            time.sleep(0.03)
        print(f"{self.RESET}\n")
    
    def print_section_header(self, title):
        """
        Print a styled section header for organizing content.
        
        Args:
            title (str): The title text for the section
        """
        border_length = len(title) + 6
        border = "═" * border_length
        
        print(f"\n{self.BRIGHT_GREEN}╔{border}╗")
        print(f"║   {title}   ║")
        print(f"╚{border}╝{self.RESET}\n")
    
    def print_matrix_effect(self, duration=2):
        """
        Display a brief matrix-style digital rain effect.
        
        Args:
            duration (int): Duration of the effect in seconds
        """
        import random
        import string
        
        matrix_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
        
        print(f"{self.GREEN}", end="")
        start_time = time.time()
        
        while time.time() - start_time < duration:
            line = "".join(random.choice(matrix_chars) for _ in range(80))
            print(line)
            time.sleep(0.05)
        
        print(f"{self.RESET}")
    
    def print_progress_bar(self, current, total, bar_length=40, prefix="Progress"):
        """
        Display a progress bar for long-running operations.
        
        Args:
            current (int): Current progress value
            total (int): Total progress value
            bar_length (int): Length of the progress bar
            prefix (str): Text to display before the progress bar
        """
        percent = (current / total) * 100
        filled_length = int(bar_length * current // total)
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        
        print(f"\r{self.GREEN}{prefix}: |{self.BRIGHT_GREEN}{bar}{self.GREEN}| "
              f"{percent:.1f}% Complete{self.RESET}", end="", flush=True)
        
        if current == total:
            print()  # New line when complete
    
    def print_warning_box(self, message):
        """
        Display a prominently styled warning message.
        
        Args:
            message (str): The warning message to display
        """
        lines = message.strip().split('\n')
        max_length = max(len(line) for line in lines)
        border_length = max_length + 4
        
        print(f"{self.YELLOW}╔{'═' * border_length}╗")
        print(f"║{'  ⚠️  WARNING  ⚠️  '.center(border_length)}║")
        print(f"╠{'═' * border_length}╣")
        
        for line in lines:
            print(f"║  {line.ljust(max_length)}  ║")
        
        print(f"╚{'═' * border_length}╝{self.RESET}")
    
    def print_success_box(self, message):
        """
        Display a success message with positive styling.
        
        Args:
            message (str): The success message to display
        """
        lines = message.strip().split('\n')
        max_length = max(len(line) for line in lines)
        border_length = max_length + 4
        
        print(f"{self.GREEN}╔{'═' * border_length}╗")
        print(f"║{'  ✓  SUCCESS  ✓  '.center(border_length)}║")
        print(f"╠{'═' * border_length}╣")
        
        for line in lines:
            print(f"║  {line.ljust(max_length)}  ║")
        
        print(f"╚{'═' * border_length}╝{self.RESET}")
    
    def print_info_box(self, message):
        """
        Display an informational message with neutral styling.
        
        Args:
            message (str): The information message to display
        """
        lines = message.strip().split('\n')
        max_length = max(len(line) for line in lines)
        border_length = max_length + 4
        
        print(f"{self.CYAN}╔{'═' * border_length}╗")
        print(f"║{'  ℹ️  INFORMATION  ℹ️  '.center(border_length)}║")
        print(f"╠{'═' * border_length}╣")
        
        for line in lines:
            print(f"║  {line.ljust(max_length)}  ║")
        
        print(f"╚{'═' * border_length}╝{self.RESET}")
    
    def print_hacker_prompt(self, text="Enter command"):
        """
        Display a hacker-style command prompt.
        
        Args:
            text (str): The prompt text to display
            
        Returns:
            str: User input
        """
        prompt = f"{self.GREEN}┌──({self.BRIGHT_GREEN}crack-time{self.GREEN})─[{self.CYAN}~{self.GREEN}]\n"
        prompt += f"└─{self.WHITE}$ {text}: {self.RESET}"
        
        return input(prompt)
    
    def animate_text(self, text, delay=0.05):
        """
        Display text with a typewriter animation effect.
        
        Args:
            text (str): The text to animate
            delay (float): Delay between each character
        """
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()  # New line after animation
    
    def print_ascii_skull(self):
        """Display a warning skull for critical security issues."""
        skull = f"""{self.RED}
                    ███████
                  ███████████
                 █████████████
                ███████████████
               █████████████████
              ███████████████████
             █████████████████████
            ███████████████████████
           █████████████████████████
          ███████   █████   ███████
         █████               █████
        ████                 ████
       ███    ███████████    ███
      ██   ███████████████   ██
     █   █████████████████   █
        ███████████████████
       █████████████████████
      ███████████████████████{self.RESET}
        """
        print(skull)
    
    def print_security_shield(self):
        """Display a security shield for strong passwords."""
        shield = f"""{self.BRIGHT_GREEN}
              ████████████████
            ██                ██
          ██                    ██
        ██        ██████        ██
      ██        ██      ██        ██
    ██        ██          ██        ██
  ██        ██              ██        ██
██        ██      SECURE      ██        ██
██        ██                  ██        ██
██          ██              ██          ██
  ██          ██          ██          ██
    ██          ████████          ██
      ██                        ██
        ██                    ██
          ██                ██
            ████████████████{self.RESET}
        """
        print(shield)
    
    def print_goodbye(self):
        """Display a goodbye message when exiting the application."""
        goodbye_msg = f"""
{self.BRIGHT_GREEN}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  Thank you for using Crack-Time!                             ║
║                                                               ║
║  Remember: Strong passwords are your first line of defense   ║
║                                                               ║
║  Stay secure, stay protected! 🛡️                             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{self.RESET}
        """
        print(goodbye_msg)
    
    def print_loading_spinner(self, duration=3, message="Loading"):
        """
        Display a loading spinner animation.
        
        Args:
            duration (int): Duration of the spinner in seconds
            message (str): Loading message to display
        """
        spinner_chars = "|/-\\"
        start_time = time.time()
        
        while time.time() - start_time < duration:
            for char in spinner_chars:
                print(f"\r{self.GREEN}{message}... {char}{self.RESET}", end="", flush=True)
                time.sleep(0.1)
        
        print(f"\r{self.GREEN}{message}... Complete!{self.RESET}")
    
    def get_styled_input(self, prompt, color=None):
        """
        Get user input with consistent styling.
        
        Args:
            prompt (str): The input prompt
            color (str): Optional color override
            
        Returns:
            str: User input
        """
        if color is None:
            color = self.CYAN
        
        return input(f"{color}{prompt}{self.RESET}")
    
    def print_divider(self, char="═", length=70):
        """
        Print a visual divider line.
        
        Args:
            char (str): Character to use for the divider
            length (int): Length of the divider
        """
        print(f"{self.GREEN}{char * length}{self.RESET}")
    
    def print_centered_text(self, text, width=80):
        """
        Print text centered within the specified width.
        
        Args:
            text (str): Text to center
            width (int): Width to center within
        """
        print(f"{self.CYAN}{text.center(width)}{self.RESET}")