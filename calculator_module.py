"""
Password Calculator Module for Crack-Time Security Tool
Performs password strength analysis and crack time calculations

Author: Security Education Team
License: MIT
"""

import math
import re
import string
from typing import Dict, Any


class PasswordCalculator:
    """
    Password analysis and calculation engine.
    
    This class provides comprehensive password security analysis including
    character set detection, entropy calculation, and crack time estimation.
    """
    
    def __init__(self):
        """Initialize the password calculator with common patterns and dictionaries."""
        # Common password patterns to check against
        self.common_patterns = [
            r'(.)\1{2,}',  # Repeated characters (aaa, 111, etc.)
            r'(012|123|234|345|456|567|678|789)',  # Sequential numbers
            r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',  # Sequential letters
            r'(qwerty|asdf|zxcv)',  # Keyboard patterns
            r'(password|admin|login|user|guest)',  # Common words (case insensitive)
        ]
        
        # Common weak passwords (subset for demonstration)
        self.weak_passwords = {
            'password', 'password123', '123456', 'qwerty', 'admin', 'letmein',
            'welcome', 'monkey', '1234567890', 'abc123', 'password1', 'admin123',
            'root', 'toor', 'pass', '12345678', 'qwerty123', 'Password1'
        }
        
        # Attack speed definitions (attempts per second)
        self.attack_speeds = {
            'slow': 1_000,           # Script kiddie with basic tools
            'medium': 1_000_000,     # Dedicated hacker with GPU
            'fast': 1_000_000_000,   # Nation state with supercomputer
            'quantum': 1_000_000_000_000  # Theoretical quantum computer
        }
    
    def analyze_password(self, password: str) -> Dict[str, Any]:
        """
        Perform comprehensive password analysis.
        
        Args:
            password (str): The password to analyze
            
        Returns:
            Dict[str, Any]: Complete analysis results including strength metrics
        """
        analysis = {
            'length': len(password),
            'charset_size': self._calculate_charset_size(password),
            'entropy': self._calculate_entropy(password),
            'total_combinations': 0,
            'crack_times': {},
            'strength_score': 0,
            'character_types': self._analyze_character_types(password),
            'pattern_issues': self._check_patterns(password),
            'is_common_password': password.lower() in self.weak_passwords
        }
        
        # Calculate total possible combinations
        analysis['total_combinations'] = analysis['charset_size'] ** analysis['length']
        
        # Calculate crack times for different attack scenarios
        analysis['crack_times'] = self._calculate_crack_times(analysis['total_combinations'])
        
        # Calculate overall strength score
        analysis['strength_score'] = self._calculate_strength_score(password, analysis)
        
        return analysis
    
    def _calculate_charset_size(self, password: str) -> int:
        """
        Calculate the character set size based on password composition.
        
        Args:
            password (str): The password to analyze
            
        Returns:
            int: Size of the character set used
        """
        charset_size = 0
        
        # Check for different character types
        if re.search(r'[a-z]', password):
            charset_size += 26  # lowercase letters
        
        if re.search(r'[A-Z]', password):
            charset_size += 26  # uppercase letters
        
        if re.search(r'[0-9]', password):
            charset_size += 10  # digits
        
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>?/`~]', password):
            charset_size += 32  # common special characters
        
        # Handle edge case of very limited character set
        if charset_size == 0:
            charset_size = len(set(password))  # Fallback to unique characters
        
        return charset_size
    
    def _calculate_entropy(self, password: str) -> float:
        """
        Calculate password entropy in bits.
        
        Args:
            password (str): The password to analyze
            
        Returns:
            float: Entropy in bits
        """
        charset_size = self._calculate_charset_size(password)
        if charset_size <= 1:
            return 0.0
        
        entropy = len(password) * math.log2(charset_size)
        
        # Apply penalties for common patterns
        penalty_factor = 1.0
        
        if self._check_patterns(password):
            penalty_factor *= 0.7  # 30% penalty for patterns
        
        if password.lower() in self.weak_passwords:
            penalty_factor *= 0.3  # 70% penalty for common passwords
        
        return entropy * penalty_factor
    
    def _calculate_crack_times(self, total_combinations: int) -> Dict[str, str]:
        """
        Calculate estimated crack times for different attack scenarios.
        
        Args:
            total_combinations (int): Total possible password combinations
            
        Returns:
            Dict[str, str]: Formatted crack time estimates
        """
        crack_times = {}
        
        # Average case: need to try half of all combinations
        avg_attempts = total_combinations // 2
        
        for speed_name, speed_value in self.attack_speeds.items():
            seconds = avg_attempts / speed_value
            crack_times[speed_name] = self._format_time(seconds)
        
        return crack_times
    
    def _format_time(self, seconds: float) -> str:
        """
        Format time duration into human-readable format.
        
        Args:
            seconds (float): Time in seconds
            
        Returns:
            str: Formatted time string
        """
        if seconds < 1:
            return "< 1 second"
        elif seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.1f} minutes"
        elif seconds < 86400:
            hours = seconds / 3600
            return f"{hours:.1f} hours"
        elif seconds < 31536000:
            days = seconds / 86400
            if days < 7:
                return f"{days:.1f} days"
            elif days < 365:
                weeks = days / 7
                return f"{weeks:.1f} weeks"
            else:
                months = days / 30.44
                return f"{months:.1f} months"
        else:
            years = seconds / 31536000
            if years < 1000:
                return f"{years:.1f} years"
            elif years < 1000000:
                return f"{years/1000:.1f} thousand years"
            elif years < 1000000000:
                return f"{years/1000000:.1f} million years"
            elif years < 1000000000000:
                return f"{years/1000000000:.1f} billion years"
            else:
                return f"{years/1000000000000:.1f} trillion years"
    
    def _analyze_character_types(self, password: str) -> Dict[str, bool]:
        """
        Analyze what types of characters are used in the password.
        
        Args:
            password (str): The password to analyze
            
        Returns:
            Dict[str, bool]: Character type usage flags
        """
        return {
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_digits': bool(re.search(r'[0-9]', password)),
            'has_symbols': bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>?/`~]', password)),
            'has_spaces': ' ' in password,
        }
    
    def _check_patterns(self, password: str) -> list:
        """
        Check for common weak patterns in the password.
        
        Args:
            password (str): The password to check
            
        Returns:
            list: List of detected pattern issues
        """
        issues = []
        
        for pattern in self.common_patterns:
            if re.search(pattern, password.lower()):
                if 'repeated' in pattern or r'(.)\1{2,}' == pattern:
                    issues.append("repeated_characters")
                elif any(seq in pattern for seq in ['012', '123', 'abc']):
                    issues.append("sequential_characters")
                elif any(kb in pattern for kb in ['qwerty', 'asdf']):
                    issues.append("keyboard_pattern")
                elif 'password' in pattern:
                    issues.append("common_words")
        
        # Check for date patterns (YYYY, MMYY, etc.)
        if re.search(r'(19|20)\d{2}', password):
            issues.append("date_pattern")
        
        # Check for simple substitutions (@ for a, 3 for e, etc.)
        substitutions = {'@': 'a', '3': 'e', '1': 'i', '0': 'o', '5': 's', '7': 't'}
        simplified = password.lower()
        for symbol, letter in substitutions.items():
            simplified = simplified.replace(symbol, letter)
        
        if simplified in self.weak_passwords:
            issues.append("simple_substitution")
        
        return issues
    
    def _calculate_strength_score(self, password: str, analysis: Dict[str, Any]) -> int:
        """
        Calculate overall password strength score (0-100).
        
        Args:
            password (str): The original password
            analysis (Dict[str, Any]): Analysis results
            
        Returns:
            int: Strength score from 0 (weakest) to 100 (strongest)
        """
        score = 0
        
        # Length scoring (up to 30 points)
        length = analysis['length']
        if length >= 16:
            score += 30
        elif length >= 12:
            score += 25
        elif length >= 8:
            score += 15
        elif length >= 6:
            score += 10
        else:
            score += 5
        
        # Character diversity scoring (up to 25 points)
        char_types = analysis['character_types']
        type_count = sum(char_types.values())
        
        if type_count >= 4:
            score += 25
        elif type_count == 3:
            score += 20
        elif type_count == 2:
            score += 10
        else:
            score += 5
        
        # Entropy scoring (up to 25 points)
        entropy = analysis['entropy']
        if entropy >= 60:
            score += 25
        elif entropy >= 50:
            score += 20
        elif entropy >= 40:
            score += 15
        elif entropy >= 30:
            score += 10
        else:
            score += 5
        
        # Pattern and common password penalties (up to 20 points)
        penalty_score = 20
        
        if analysis['is_common_password']:
            penalty_score -= 15
        
        if analysis['pattern_issues']:
            penalty_score -= min(len(analysis['pattern_issues']) * 3, 10)
        
        score += max(penalty_score, 0)
        
        # Ensure score stays within bounds
        return max(0, min(100, score))
    
    def get_password_recommendations(self, password: str, analysis: Dict[str, Any]) -> list:
        """
        Generate specific recommendations to improve password strength.
        
        Args:
            password (str): The original password
            analysis (Dict[str, Any]): Analysis results
            
        Returns:
            list: List of improvement recommendations
        """
        recommendations = []
        
        # Length recommendations
        if analysis['length'] < 12:
            recommendations.append("Increase password length to at least 12 characters")
        
        # Character type recommendations
        char_types = analysis['character_types']
        if not char_types['has_uppercase']:
            recommendations.append("Add uppercase letters (A-Z)")
        if not char_types['has_lowercase']:
            recommendations.append("Add lowercase letters (a-z)")
        if not char_types['has_digits']:
            recommendations.append("Add numbers (0-9)")
        if not char_types['has_symbols']:
            recommendations.append("Add special characters (!@#$%^&*)")
        
        # Pattern-specific recommendations
        if analysis['pattern_issues']:
            if "repeated_characters" in analysis['pattern_issues']:
                recommendations.append("Avoid repeating the same character multiple times")
            if "sequential_characters" in analysis['pattern_issues']:
                recommendations.append("Avoid sequential characters (123, abc, etc.)")
            if "keyboard_pattern" in analysis['pattern_issues']:
                recommendations.append("Avoid keyboard patterns (qwerty, asdf, etc.)")
            if "common_words" in analysis['pattern_issues']:
                recommendations.append("Avoid common words like 'password' or 'admin'")
            if "date_pattern" in analysis['pattern_issues']:
                recommendations.append("Avoid using dates or years in passwords")
            if "simple_substitution" in analysis['pattern_issues']:
                recommendations.append("Avoid simple character substitutions (@ for a, 3 for e)")
        
        # Common password warning
        if analysis['is_common_password']:
            recommendations.append("This is a commonly used password - choose something unique")
        
        # General recommendations
        if analysis['strength_score'] < 75:
            recommendations.append("Consider using a passphrase with multiple words")
            recommendations.append("Use a password manager to generate strong passwords")
        
        return recommendations
    
    def estimate_dictionary_attack_time(self, password: str) -> str:
        """
        Estimate time for a dictionary attack (separate from brute force).
        
        Args:
            password (str): Password to analyze
            
        Returns:
            str: Estimated dictionary attack time
        """
        # Simplified dictionary attack estimation
        # Real dictionary attacks would depend on the specific wordlist used
        
        if password.lower() in self.weak_passwords:
            return "< 1 second (in common wordlist)"
        
        # Check if it's a simple variation of a common word
        base_password = password.lower().strip(string.digits + string.punctuation)
        if base_password in self.weak_passwords:
            return "< 1 minute (common word variation)"
        
        # If it contains dictionary words but has good complexity
        if any(word in password.lower() for word in ['password', 'admin', 'user', 'login']):
            return "Minutes to hours (contains dictionary words)"
        
        return "Very long (not in typical dictionaries)"