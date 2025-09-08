#!/usr/bin/env python3
"""
Crack-Time - Password Security Awareness Tool
Educational tool to estimate password cracking time and promote security awareness

Author: Security Education Team
License: MIT
Version: 1.0.0
"""

import sys
import time
import os
from utils.ui import UI
from utils.calculator import PasswordCalculator
from utils.suggestions import PasswordSuggestions


class CrackTime:
    """
    Main application class for the Crack-Time password security awareness tool.
    
    This tool helps users understand password security by calculating estimated
    crack times and providing security recommendations.
    """
    
    def __init__(self):
        """Initialize the CrackTime application."""
        self.ui = UI()
        self.calculator = PasswordCalculator()
        self.suggestions = PasswordSuggestions()
    
    def startup_animation(self):
        """Display animated startup banner and initialization sequence."""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        # Simulate loading sequence
        print(self.ui.GREEN + "[INFO] Initializing Crack-Time Security Suite..." + self.ui.RESET)
        time.sleep(0.5)
        
        loading_items = [
            "Loading brute-force algorithms",
            "Initializing password analyzers", 
            "Loading security databases",
            "Preparing recommendations engine"
        ]
        
        for item in loading_items:
            print(f"{self.ui.GREEN}[+] {item}..." + self.ui.RESET)
            time.sleep(0.3)
        
        print(f"\n{self.ui.BRIGHT_GREEN}[✓] System ready! Welcome to Crack-Time v1.0.0{self.ui.RESET}")
        time.sleep(1)
    
    def display_disclaimer(self):
        """Display important security disclaimer and educational notice."""
        self.ui.print_section_header("⚠️  SECURITY DISCLAIMER")
        
        disclaimer_text = """
╔═══════════════════════════════════════════════════════════════════════════════╗
║                            EDUCATIONAL USE ONLY                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  • This tool is designed for PASSWORD SECURITY AWARENESS only                ║
║  • DO NOT use for unauthorized access attempts                               ║
║  • Crack time estimates are theoretical and educational                       ║
║  • Always use strong, unique passwords for your accounts                     ║
║  • Enable two-factor authentication wherever possible                        ║
║                                                                               ║
║  By using this tool, you agree to use it responsibly and ethically.         ║
╚═══════════════════════════════════════════════════════════════════════════════╝
        """
        
        print(self.ui.YELLOW + disclaimer_text + self.ui.RESET)
        input(f"\n{self.ui.CYAN}Press Enter to continue...{self.ui.RESET}")
    
    def get_user_password(self):
        """
        Safely get password input from user with privacy protection.
        
        Returns:
            str: The password entered by the user
        """
        self.ui.clear_screen()
        self.ui.print_section_header("🔐 PASSWORD ANALYSIS")
        
        print(f"{self.ui.GREEN}Enter a password to analyze its security strength:")
        print(f"{self.ui.YELLOW}(Your password will not be stored or transmitted){self.ui.RESET}")
        
        # Get password input (visible for educational purposes)
        password = input(f"\n{self.ui.CYAN}Password: {self.ui.RESET}")
        
        if not password:
            print(f"{self.ui.RED}[ERROR] Password cannot be empty!{self.ui.RESET}")
            return None
            
        return password
    
    def analyze_password(self, password):
        """
        Perform comprehensive password analysis and display results.
        
        Args:
            password (str): The password to analyze
        """
        self.ui.print_section_header("📊 ANALYSIS RESULTS")
        
        # Calculate password metrics
        analysis = self.calculator.analyze_password(password)
        
        # Display basic metrics
        self.display_basic_metrics(password, analysis)
        
        # Display crack time estimates
        self.display_crack_times(analysis)
        
        # Display strength rating
        self.display_strength_rating(analysis['strength_score'])
        
        # Show security warnings if needed
        self.show_security_warnings(password, analysis)
    
    def display_basic_metrics(self, password, analysis):
        """
        Display basic password metrics and characteristics.
        
        Args:
            password (str): The original password
            analysis (dict): Analysis results from calculator
        """
        print(f"{self.ui.BRIGHT_GREEN}Password Characteristics:{self.ui.RESET}")
        print("─" * 50)
        
        metrics = [
            ("Length", len(password), "characters"),
            ("Character Set Size", analysis['charset_size'], "possible characters"),
            ("Entropy", f"{analysis['entropy']:.2f}", "bits"),
            ("Possible Combinations", f"{analysis['total_combinations']:,}", "")
        ]
        
        for metric, value, unit in metrics:
            print(f"{self.ui.GREEN}  {metric:.<20} {self.ui.CYAN}{value} {unit}{self.ui.RESET}")
    
    def display_crack_times(self, analysis):
        """
        Display estimated crack times at different attack speeds.
        
        Args:
            analysis (dict): Analysis results containing crack times
        """
        print(f"\n{self.ui.BRIGHT_GREEN}Estimated Crack Times (Average Case):{self.ui.RESET}")
        print("─" * 50)
        
        speeds = [
            ("Script Kiddie", "1K/sec", analysis['crack_times']['slow']),
            ("Dedicated Hacker", "1M/sec", analysis['crack_times']['medium']),
            ("Nation State", "1B/sec", analysis['crack_times']['fast']),
            ("Quantum Computer", "1T/sec", analysis['crack_times']['quantum'])
        ]
        
        for attacker_type, speed, crack_time in speeds:
            color = self.get_time_color(crack_time)
            print(f"{self.ui.GREEN}  {attacker_type} ({speed}): {color}{crack_time}{self.ui.RESET}")
    
    def get_time_color(self, time_str):
        """
        Get appropriate color for crack time based on security level.
        
        Args:
            time_str (str): The formatted time string
            
        Returns:
            str: ANSI color code
        """
        if any(word in time_str.lower() for word in ['second', 'minute', 'hour']):
            return self.ui.RED
        elif 'day' in time_str.lower() or 'week' in time_str.lower():
            return self.ui.YELLOW
        elif 'month' in time_str.lower() or 'year' in time_str.lower():
            return self.ui.GREEN
        else:
            return self.ui.BRIGHT_GREEN
    
    def display_strength_rating(self, strength_score):
        """
        Display password strength rating with visual indicators.
        
        Args:
            strength_score (int): Calculated strength score (0-100)
        """
        print(f"\n{self.ui.BRIGHT_GREEN}Password Strength Rating:{self.ui.RESET}")
        print("─" * 50)
        
        # Determine strength level and color
        if strength_score < 25:
            level = "CRITICAL"
            color = self.ui.RED
            bars = "█" * 1 + "░" * 9
        elif strength_score < 50:
            level = "WEAK"
            color = self.ui.YELLOW
            bars = "█" * 3 + "░" * 7
        elif strength_score < 75:
            level = "MODERATE"
            color = self.ui.CYAN
            bars = "█" * 6 + "░" * 4
        elif strength_score < 90:
            level = "STRONG"
            color = self.ui.GREEN
            bars = "█" * 8 + "░" * 2
        else:
            level = "MILITARY-GRADE"
            color = self.ui.BRIGHT_GREEN
            bars = "█" * 10
        
        print(f"  Strength: {color}{level} ({strength_score}/100){self.ui.RESET}")
        print(f"  Progress: [{color}{bars}{self.ui.RESET}]")
    
    def show_security_warnings(self, password, analysis):
        """
        Display security warnings and improvement suggestions.
        
        Args:
            password (str): The original password
            analysis (dict): Analysis results
        """
        warnings = self.suggestions.get_warnings(password, analysis)
        
        if warnings:
            print(f"\n{self.ui.RED}⚠️  Security Warnings:{self.ui.RESET}")
            print("─" * 50)
            for warning in warnings:
                print(f"{self.ui.RED}  ⚠  {warning}{self.ui.RESET}")
        
        # Always show suggestions
        suggestions = self.suggestions.get_suggestions(password, analysis)
        if suggestions:
            print(f"\n{self.ui.BRIGHT_GREEN}💡 Improvement Suggestions:{self.ui.RESET}")
            print("─" * 50)
            for suggestion in suggestions:
                print(f"{self.ui.GREEN}  ✓  {suggestion}{self.ui.RESET}")
    
    def show_educational_tips(self):
        """Display educational tips about password security."""
        self.ui.print_section_header("🎓 PASSWORD SECURITY TIPS")
        
        tips = [
            "Use at least 12 characters (preferably 16+)",
            "Include uppercase, lowercase, numbers, and symbols",
            "Avoid dictionary words and personal information",
            "Use unique passwords for each account",
            "Consider using a password manager",
            "Enable two-factor authentication (2FA)",
            "Regularly update passwords for critical accounts",
            "Use passphrases for easier memorization"
        ]
        
        for i, tip in enumerate(tips, 1):
            print(f"{self.ui.GREEN}  {i}. {tip}{self.ui.RESET}")
        
        print(f"\n{self.ui.CYAN}Remember: A strong password is your first line of defense!{self.ui.RESET}")
    
    def main_menu(self):
        """Display and handle the main menu interface."""
        while True:
            self.ui.clear_screen()
            self.ui.print_section_header("🔐 CRACK-TIME MAIN MENU")
            
            options = [
                "Analyze Password Security",
                "View Security Tips",
                "About Crack-Time",
                "Exit"
            ]
            
            for i, option in enumerate(options, 1):
                print(f"{self.ui.GREEN}  [{i}] {option}{self.ui.RESET}")
            
            choice = input(f"\n{self.ui.CYAN}Select option (1-{len(options)}): {self.ui.RESET}")
            
            if choice == '1':
                self.password_analysis_flow()
            elif choice == '2':
                self.show_educational_tips()
                input(f"\n{self.ui.CYAN}Press Enter to continue...{self.ui.RESET}")
            elif choice == '3':
                self.show_about()
            elif choice == '4':
                self.ui.print_goodbye()
                sys.exit(0)
            else:
                print(f"{self.ui.RED}Invalid option! Please try again.{self.ui.RESET}")
                time.sleep(1)
    
    def password_analysis_flow(self):
        """Handle the complete password analysis workflow."""
        password = self.get_user_password()
        if password:
            print(f"\n{self.ui.GREEN}[INFO] Analyzing password security...{self.ui.RESET}")
            time.sleep(1)  # Simulate analysis time
            
            self.analyze_password(password)
            
            print(f"\n{self.ui.BRIGHT_GREEN}Analysis complete!{self.ui.RESET}")
            input(f"\n{self.ui.CYAN}Press Enter to continue...{self.ui.RESET}")
    
    def show_about(self):
        """Display information about the Crack-Time tool."""
        self.ui.clear_screen()
        self.ui.print_section_header("ℹ️  ABOUT CRACK-TIME")
        
        about_text = f"""
{self.ui.BRIGHT_GREEN}Crack-Time v1.0.0{self.ui.RESET}
{self.ui.GREEN}Password Security Awareness Tool{self.ui.RESET}

{self.ui.CYAN}Purpose:{self.ui.RESET}
Educational tool designed to help users understand password security
by estimating theoretical crack times and providing security guidance.

{self.ui.CYAN}Features:{self.ui.RESET}
• Real-time password strength analysis
• Crack time estimation at various attack speeds
• Security warnings and improvement suggestions
• Educational tips and best practices

{self.ui.CYAN}Disclaimer:{self.ui.RESET}
This tool is for educational purposes only. All calculations are
theoretical and should not be used for malicious activities.

{self.ui.YELLOW}Remember: Strong passwords save lives (and data)!{self.ui.RESET}
        """
        
        print(about_text)
        input(f"\n{self.ui.CYAN}Press Enter to return to main menu...{self.ui.RESET}")
    
    def run(self):
        """Main application entry point."""
        try:
            self.startup_animation()
            self.display_disclaimer()
            self.main_menu()
        except KeyboardInterrupt:
            print(f"\n\n{self.ui.YELLOW}[INFO] Application interrupted by user.{self.ui.RESET}")
            self.ui.print_goodbye()
            sys.exit(0)
        except Exception as e:
            print(f"\n{self.ui.RED}[ERROR] An unexpected error occurred: {e}{self.ui.RESET}")
            sys.exit(1)


if __name__ == "__main__":
    app = CrackTime()
    app.run()