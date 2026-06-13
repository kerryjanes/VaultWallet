# test_vaultwallet.py
"""
Tests for VaultWallet module.
"""

import unittest
from vaultwallet import VaultWallet

class TestVaultWallet(unittest.TestCase):
    """Test cases for VaultWallet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultWallet()
        self.assertIsInstance(instance, VaultWallet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultWallet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
