import number_theory_functions
from random import randrange
import math

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        first = 10^(digits - 1)
        last = 10^digits - 1
        p = number_theory_functions.generate_prime(digits/2)
        q = number_theory_functions.generate_prime(digits/2)
        N = p*q

        phi = (p-1)*(q-1)
        
        for i in range(digits * 10):
            e = randrange(1, phi - 1 )
            d = number_theory_functions.modular_inverse(e,phi)
            if(d != 0):
                break
        
        
        return (N,e) (N,d)
        


    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        N = self.public_key[0]
        e = self.public_key[1]
        c = number_theory_functions.modular_exponent(m, e, N)
        return c



    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        N = self.private_key[0]
        d = self.private_key[1]
        m = number_theory_functions.modular_exponent(c,d , N)
        return m


if __name__ == '__main__':
    print('started')