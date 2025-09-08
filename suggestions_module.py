"""
Password Suggestions Module for Crack-Time Security Tool
Provides security warnings and improvement suggestions

Author: Security Education Team
License: MIT
"""

import random
import string
from typing import List, Dict, Any


class PasswordSuggestions:
    """
    Password improvement suggestions and security warnings generator.
    
    This class analyzes password weaknesses and provides actionable
    recommendations to improve password security.
    """
    
    def __init__(self):
        """Initialize with suggestion templates and security guidelines."""
        # Example strong password patterns (for educational purposes)
        self.example_patterns = [
            "Use passphrases: 'Coffee@Morning#Walk2024'",
            "Mix words with numbers: 'Blue42Sky#Dance'", 
            "Use acronyms: 'My$on!sBorn@2020' (MySonIsBornAt2020)",
            "Random but memorable: 'Pizza$Unicorn&123!'",
            "Professional format: 'Work_Secure#2024$'"
        ]
        
        # Security tips for different scenarios
        self.security_tips = [
            "Use unique passwords for every account",
            "Enable two-factor authentication (2FA) when available",
            "Consider using a reputable password manager",
            "Update passwords regularly for critical accounts",
            "Never share passwords or store them in plain text",
            "Use longer passphrases instead of complex short passwords",
            "Avoid using personal information in passwords",
            "Don't use the same password pattern across sites"
        ]
        
        # Common substitution patterns to avoid
        self.weak_substitutions = {
            'a': '@', 'e': '3', 'i': '1', 'o': '0', 
            's': '$', 't': '7', 'l': '!'
        }
    
    def get_warnings(self, password: str, analysis: Dict[str, Any]) -> List[str]:
        """
        Generate security warnings based on password analysis.
        
        Args:
            password (str): The password being analyzed
            analysis (Dict[str, Any]): Analysis results from calculator
            
        Returns:
            List[str]: List of security warnings
        """
        warnings = []
        
        # Critical length warning
        if analysis['length'] < 8:
            warnings.append("Password is dangerously short - minimum 8 characters required")
        
        # Common password warning
        if analysis['is_common_password']:
            warnings.append("This password appears in common password lists - change immediately!")
        
        # Strength-based warnings
        if analysis['strength_score'] < 25:
            warnings.append("CRITICAL: This password provides virtually no security")
        elif analysis['strength_score'] < 50:
            warnings.append("This password is easily crackable by modern tools")
        
        # Character diversity warnings
        char_types = analysis['character_types']
        used_types = sum(char_types.values())
        
        if used_types < 2:
            warnings.append("Password uses only one type of character - extremely vulnerable")
        elif used_types < 3:
            warnings.append("Limited character variety makes this password weaker")
        
        # Pattern-specific warnings
        if analysis['pattern_issues']:
            if "repeated_characters" in analysis['pattern_issues']:
                warnings.append("Repeated characters make passwords predictable")
            
            if "sequential_characters" in analysis['pattern_issues']:
                warnings.append("Sequential patterns (123, abc) are easily guessed")
            
            if "keyboard_pattern" in analysis['pattern_issues']:
                warnings.append("Keyboard patterns are among the first things hackers try")
            
            if "simple_substitution" in analysis['pattern_issues']:
                warnings.append("Simple substitutions (@ for a) don't significantly improve security")
        
        # Crack time warnings
        crack_times = analysis['crack_times']
        if 'medium' in crack_times:
            medium_time = crack_times['medium']
            if any(unit in medium_time.lower() for unit in ['second', 'minute']):
                warnings.append("A dedicated attacker could crack this in " + medium_time.lower())
        
        return warnings
    
    def get_suggestions(self, password: str, analysis: Dict[str, Any]) -> List[str]:
        """
        Generate improvement suggestions based on password analysis.
        
        Args:
            password (str): The password being analyzed
            analysis (Dict[str, Any]): Analysis results from calculator
            
        Returns:
            List[str]: List of improvement suggestions
        """
        suggestions = []
        
        # Length suggestions
        if analysis['length'] < 12:
            suggestions.append(f"Increase length to at least 12 characters (currently {analysis['length']})")
        elif analysis['length'] < 16:
            suggestions.append("Consider extending to 16+ characters for maximum security")
        
        # Character type suggestions
        char_types = analysis['character_types']
        
        if not char_types['has_uppercase']:
            suggestions.append("Add uppercase letters (A, B, C, etc.)")
        
        if not char_types['has_lowercase']:
            suggestions.append("Add lowercase letters (a, b, c, etc.)")
        
        if not char_types['has_digits']:
            suggestions.append("Include numbers (0-9)")
        
        if not char_types['has_symbols']:
            suggestions.append("Add special characters (!@#$%^&* etc.)")
        
        # Entropy-based suggestions
        if analysis['entropy'] < 50:
            suggestions.append("Increase randomness - avoid predictable patterns")
        
        # Pattern improvement suggestions
        if analysis['pattern_issues']:
            suggestions.append("Remove predictable patterns and sequences")
        
        # Strength-based suggestions
        if analysis['strength_score'] < 75:
            suggestions.extend([
                "Consider using a passphrase (multiple words combined)",
                "Use a password manager to generate strong passwords"
            ])
        
        # Always include general security advice
        suggestions.extend([
            "Make this password unique - don't reuse it elsewhere",
            "Enable two-factor authentication for added security"
        ])
        
        return suggestions
    
    def generate_example_passwords(self, target_length: int = 16) -> List[str]:
        """
        Generate example strong passwords for educational purposes.
        
        Args:
            target_length (int): Target length for generated passwords
            
        Returns:
            List[str]: List of example strong passwords
        """
        examples = []
        
        # Passphrase examples
        word_combinations = [
            ["Solar", "Bridge", "Dance", "2024"],
            ["Quick", "Mountain", "Coffee", "Star"],
            ["Happy", "Dragon", "Music", "Wave"],
            ["Bright", "Forest", "Ocean", "Moon"]
        ]
        
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
        
        for words in word_combinations[:3]:  # Limit to 3 examples
            # Create passphrase with symbols
            password = ""
            for i, word in enumerate(words):
                password += word
                if i < len(words) - 1:
                    password += random.choice(symbols)
            
            # Add random digits if needed to reach target length
            while len(password) < target_length:
                password += str(random.randint(0, 9))
            
            examples.append(password)
        
        return examples
    
    def get_passphrase_suggestions(self) -> List[str]:
        """
        Get suggestions for creating memorable passphrases.
        
        Returns:
            List[str]: List of passphrase creation tips
        """
        return [
            "Use 4-6 random words: 'Correct Horse Battery Staple'",
            "Add numbers and symbols between words: 'Red#Car42Blue$House'",
            "Use a memorable sentence: 'I Love Coffee Every Morning At 7AM!'",
            "Combine hobbies and dates: 'Guitar@Beach#Summer2024'",
            "Use movie quotes with modifications: 'May4th$Force&BeWithYou!'",
            "Mix languages: 'Hello$World#Bonjour@2024'",
            "Use acronyms from sentences: 'MyDogLikes2RunInTheParks!' -> 'MDL2RITP!'"
        ]
    
    def analyze_common_mistakes(self, password: str) -> List[str]:
        """
        Identify common password creation mistakes.
        
        Args:
            password (str): Password to analyze
            
        Returns:
            List[str]: List of identified mistakes
        """
        mistakes = []
        
        # Check for common mistakes
        if password.lower().startswith(('password', 'admin', 'user', 'login')):
            mistakes.append("Starts with a common word - very predictable")
        
        if password.endswith(('123', '!', '.')):
            mistakes.append("Predictable ending pattern")
        
        if len(set(password)) / len(password) < 0.7:  # Low character diversity
            mistakes.append("Too many repeated characters")
        
        # Check for simple patterns
        if password.lower() in ['qwerty123', 'abc123', '123abc', 'password1']:
            mistakes.append("Extremely common weak password pattern")
        
        # Check for simple transformations
        simple_transforms = [
            password.replace('a', '@'),
            password.replace('e', '3'),
            password.replace('i', '1'),
            password.replace('o', '0')
        ]
        
        if any(transform.lower() in ['p@ssword', 'p4ssw0rd', 'adm1n'] for transform in simple_transforms):
            mistakes.append("Simple character substitution is not secure")
        
        # Check for personal info patterns (simplified)
        if any(year in password for year in ['2020', '2021', '2022', '2023', '2024', '2025']):
            mistakes.append("Avoid using current or recent years")
        
        return mistakes
    
    def get_industry_specific_tips(self, industry: str = "general") -> List[str]:
        """
        Provide industry-specific password security recommendations.
        
        Args:
            industry (str): Industry type for tailored advice
            
        Returns:
            List[str]: Industry-specific security tips
        """
        general_tips = [
            "Use unique passwords for work and personal accounts",
            "Implement password rotation policies for critical systems",
            "Train employees on password security best practices",
            "Use enterprise password managers for team coordination",
            "Regularly audit password strength across systems"
        ]
        
        industry_specific = {
            "healthcare": [
                "Ensure HIPAA compliance with strong authentication",
                "Use role-based password policies",
                "Implement automatic screen locks for patient data access"
            ],
            "finance": [
                "Follow PCI DSS requirements for payment systems",
                "Use multi-factor authentication for all financial access",
                "Implement session timeouts for sensitive operations"
            ],
            "education": [
                "Protect student data with strong authentication",
                "Teach password security as part of digital literacy",
                "Use single sign-on (SSO) to reduce password fatigue"
            ],
            "technology": [
                "Use SSH keys instead of passwords where possible",
                "Implement zero-trust security models",
                "Use hardware security keys for critical systems"
            ]
        }
        
        tips = general_tips.copy()
        if industry in industry_specific:
            tips.extend(industry_specific[industry])
        
        return tips
    
    def get_breach_response_advice(self) -> List[str]:
        """
        Provide advice for responding to password breaches.
        
        Returns:
            List[str]: Breach response recommendations
        """
        return [
            "Change the compromised password immediately",
            "Update any accounts that used the same password",
            "Monitor accounts for suspicious activity",
            "Enable breach notifications from security services",
            "Consider identity monitoring services",
            "Review and update all passwords periodically",
            "Use unique passwords for every account going forward",
            "Enable two-factor authentication on all possible accounts"
        ]
    
    def calculate_improvement_impact(self, current_analysis: Dict[str, Any], 
                                   suggested_changes: List[str]) -> Dict[str, Any]:
        """
        Calculate the security impact of suggested improvements.
        
        Args:
            current_analysis (Dict[str, Any]): Current password analysis
            suggested_changes (List[str]): List of suggested improvements
            
        Returns:
            Dict[str, Any]: Impact analysis of improvements
        """
        impact = {
            'strength_increase': 0,
            'time_improvement': "No change",
            'risk_reduction': "Low"
        }
        
        current_score = current_analysis['strength_score']
        
        # Estimate improvement based on suggestions
        projected_score = current_score
        
        for suggestion in suggested_changes:
            if "increase length" in suggestion.lower():
                projected_score += 15
            elif "character" in suggestion.lower():
                projected_score += 10
            elif "pattern" in suggestion.lower():
                projected_score += 8
            elif "unique" in suggestion.lower():
                projected_score += 5
        
        projected_score = min(100, projected_score)
        impact['strength_increase'] = projected_score - current_score
        
        # Estimate time improvement
        if impact['strength_increase'] > 30:
            impact['time_improvement'] = "Years to centuries"
            impact['risk_reduction'] = "High"
        elif impact['strength_increase'] > 20:
            impact['time_improvement'] = "Months to years"
            impact['risk_reduction'] = "Medium"
        elif impact['strength_increase'] > 10:
            impact['time_improvement'] = "Days to weeks"
            impact['risk_reduction'] = "Medium"
        
        return impact